"""Frequency test (Sprint 19, blocks 5-6): drive a sample project through a scripted long session under each
arm, check that the arm really is what it claims, judge the two probes, and summarize.

The standard is `frequency-test.md` in this folder (committed before this script was run). This script
implements it; it changes no judgment, pass line, probe wording, or goal text.

usage (all with `python -X utf8 -I`):
  frequency_test.py selftest
  frequency_test.py smoke  --out DIR [--arm A2]
  frequency_test.py run    --out DIR [--arms A0,A1,A2,A3,A4] [--reps 3] [--parallel 1]
  frequency_test.py tokens --out DIR [--reps 3]
  frequency_test.py judge  --out DIR

Raw streams go to --out (outside the repo). The channel is `claude-magpie.cmd -p` with a whitelist
environment: nothing is inherited from the host except the names listed in WHITELIST.
"""
import argparse
import concurrent.futures
import json
import os
import pathlib
import queue
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unicodedata

REPO = pathlib.Path(__file__).resolve().parents[3]
PLUGIN = REPO / "plugins/ideo-scrum"
EXE = "claude-magpie.cmd"
WHITELIST = {"systemroot", "path", "userprofile", "appdata", "localappdata", "homedrive", "homepath", "comspec",
             "pathext", "temp", "tmp", "claude_code_git_bash_path", "msys_no_pathconv"}

# ---- the sample project (frequency-test.md, section 3) ------------------------------------------------
PRODUCT = "ExportKit：把订单导出成 CSV 文件的小工具。"
PRODUCT_GOAL = "导出又快又稳：一万行订单一分钟内导完，出错能从断点接着导。"
V1 = "导出先稳：失败的行单独记下来，不拖垮整批；PO 看一眼错误清单就知道哪几行要补。"
V2 = "导出先快：先做按列选择，只导 PO 勾选的列；本冲刺不碰错误清单。"
V1_CLAUSE = "失败的行单独记下来"
RULE = ("做阶段决定前，先把本冲刺 Sprint Goal 的原文引用出来（照抄 `scrum/` 下冲刺日志 1.1 那一格）；"
        "引用不出来，就先去读日志，不要编。\n")
SPRINT_DIR = "scrum/sprint-01-batch-export"

FILES = {
    "CLAUDE.md": RULE,
    "README.md": ("# ExportKit\n\nExportKit 把订单导出成 CSV 文件。\n\n## 用法\n\n"
                  "运行 `python -m exportkit orders.json` 导出全部订单；加 `--resume` 从上次断掉的地方接着导。\n\n"
                  "## 输出\n\n输出文件是 `orders.csv`，编码 UTF-8，逗号分隔。\n\n## 许可\n\nMIT\n"),
    "src/export.py": ("import csv\nimport json\n\n\ndef read_orders(path):\n    with open(path, encoding='utf-8') as f:\n"
                      "        return json.load(f)\n\n\ndef write_csv(rows, columns, path='orders.csv'):\n"
                      "    with open(path, 'w', newline='', encoding='utf-8') as f:\n"
                      "        w = csv.writer(f)\n        w.writerow(columns)\n        for r in rows:\n"
                      "            w.writerow([r.get(c, '') for c in columns])\n\n\n"
                      "def export_all(src, columns):\n    rows = read_orders(src)\n    write_csv(rows, columns)\n"
                      "    return len(rows)\n"),
    "tests/test_export.py": ("from src.export import export_all, read_orders, write_csv\n\n\n"
                             "def test_read_orders(tmp_path):\n    assert read_orders(tmp_path / 'a.json') == []\n\n\n"
                             "def test_write_csv_empty(tmp_path):\n    write_csv([], ['id'], tmp_path / 'o.csv')\n\n\n"
                             "def test_export_all(tmp_path):\n    assert export_all(tmp_path / 'a.json', ['id']) == 0\n"),
    "scrum/ProductBacklog.md": (f"# 一、Product\n\n## 1.1 Product\n\n| 承诺 | {PRODUCT} |\n| --- | --- |\n\n"
                                f"## 1.2 Product Goal\n\n| 承诺 | {PRODUCT_GOAL} |\n| --- | --- |\n"),
    f"{SPRINT_DIR}/SprintBacklog.md": (
        "# Sprint Backlog — Sprint 01 (batch-export)\n\n> Started: 2026-11-13 | Branch: main\n"
        "> Now: Increment：做块 2\n> Waiting for PO: None\n\n## 1. Why\n\n### 1.1 Sprint Goal\n\n"
        f"| 承诺 | {V1} |\n| --- | --- |\n\n### 1.2 Definition of Done\n\n- 测试通过\n"),
}

P1 = "Why 阶段定完了。现在要进入 What 阶段：我想把「导出错误清单页面」这一条选进本冲刺。请你做这个阶段决定。"
P2 = "压缩之后接着做。现在要进入 What 阶段：我想把「选择要导出的列」这一条选进本冲刺。请你做这个阶段决定。"
FILLER = {
    1: "读一下 README.md，用一句话说它是做什么的。",
    2: "src/export.py 里有哪些函数？只列函数名。",
    3: "tests/test_export.py 里有几个测试？",
    4: "src/export.py 的 write_csv 对空列表会怎样？",
    5: "把 README.md 里提到的命令列出来。",
    6: "src/export.py 里有没有写死的文件名？",
    7: "tests/test_export.py 的测试各检查什么？一行一个。",
    8: "README.md 有没有提到输出的编码？",
    10: "src/export.py 一共多少行？",
    11: "README.md 的标题有哪些？",
    12: "tests 目录里除了 test_export.py 还有别的文件吗？",
    13: "src/export.py 里 write_csv 的参数是什么？",
}


def scenario():
    """The steps of one run (frequency-test.md section 4): 14 prompts, one goal change, one /compact."""
    steps = []
    for i in range(1, 6):
        steps.append({"say": FILLER[i], "label": f"T{i}"})
    steps.append({"replace": {"file": f"{SPRINT_DIR}/SprintBacklog.md", "old": V1, "new": V2}, "label": "change"})
    for i in range(6, 9):
        steps.append({"say": FILLER[i], "label": f"T{i}"})
    steps.append({"say": P1, "label": "P1"})
    for i in range(10, 13):
        steps.append({"say": FILLER[i], "label": f"T{i}"})
    steps.append({"say": "/compact", "label": "compact"})
    steps.append({"say": FILLER[13], "label": "T13"})
    steps.append({"say": P2, "label": "P2"})
    return steps


# arm -> env for the hook (the test-only mode switch in commitments.sh)
ARMS = {
    "A0": {"IDEO_SCRUM_COMMITMENTS": "off"},
    "A1": {"IDEO_SCRUM_COMMITMENTS_MODE": "start"},
    "A2": {"IDEO_SCRUM_COMMITMENTS_MODE": "every"},
    "A3": {"IDEO_SCRUM_COMMITMENTS_MODE": "every-n", "IDEO_SCRUM_COMMITMENTS_N": "5"},
    "A4": {"IDEO_SCRUM_COMMITMENTS_MODE": "changed"},
}
# how many non-empty injections of ours a whole run must show: SessionStart startup + compact, plus prompts
EXPECTED_INJECTIONS = {"A0": 0, "A1": 2, "A2": 2 + 14, "A3": 2 + 2, "A4": 2 + 1}
MARKERS = ("Commitments from this project's logs", "本项目日志里的承诺")


def build_fixture(dest):
    dest = pathlib.Path(dest)
    for rel, text in FILES.items():
        p = dest / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8", newline="\n")
    return dest


# ---- the driver: one process, one message at a time ----------------------------------------------------
def clean_env(extra):
    env = {k: v for k, v in os.environ.items() if k.lower() in WHITELIST}
    sh = shutil.which("sh")
    if sh:
        env["CLAUDE_CODE_GIT_BASH_PATH"] = str(pathlib.Path(sh).with_name("bash.exe"))
    env["MSYS_NO_PATHCONV"] = "1"
    for k in ("TEMP", "TMP"):
        env[k] = tempfile.mkdtemp(prefix="freq-tmp-")
    env.update(extra)
    return env


def drive(cwd, out_path, steps, env_extra, turn_timeout=420, model="haiku"):
    """Returns {'status','turns','exit'}; writes every stream line, plus harness markers, to out_path."""
    cwd = pathlib.Path(cwd)
    tools = "Read,Grep,Glob"
    cmd = [EXE, "-p", "--input-format", "stream-json", "--output-format", "stream-json", "--verbose",
           "--include-hook-events", "--model", model, "--tools", tools, "--allowedTools", tools,
           "--plugin-dir", str(PLUGIN)]
    proc = subprocess.Popen(cmd, cwd=str(cwd), env=clean_env(env_extra), stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    results, lock = queue.Queue(), threading.Lock()
    out = open(out_path, "w", encoding="utf-8", newline="\n")

    def emit(line):
        with lock:
            out.write(line + "\n")
            out.flush()

    def reader():
        for raw in proc.stdout:
            line = raw.decode("utf-8", "replace").rstrip("\r\n")
            emit(line)
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if d.get("type") == "result":
                results.put(d)
        results.put(None)

    err = []
    threading.Thread(target=reader, daemon=True).start()
    threading.Thread(target=lambda: [err.append(r.decode("utf-8", "replace")) for r in proc.stderr], daemon=True).start()

    status, turns = "ok", 0
    for i, st in enumerate(steps):
        emit(json.dumps({"type": "harness", "index": i, "label": st.get("label"),
                         "step": "replace" if "replace" in st else "say"}, ensure_ascii=False))
        if "replace" in st:
            r = st["replace"]
            f = cwd / r["file"]
            text = f.read_text(encoding="utf-8")
            if r["old"] not in text:
                status = f"step {i}: text to replace not found"
                break
            f.write_text(text.replace(r["old"], r["new"], 1), encoding="utf-8", newline="\n")
            continue
        msg = {"type": "user", "message": {"role": "user", "content": st["say"]}}
        proc.stdin.write((json.dumps(msg, ensure_ascii=False) + "\n").encode("utf-8"))
        proc.stdin.flush()
        try:
            d = results.get(timeout=turn_timeout)
        except queue.Empty:
            status = f"step {i}: no result within {turn_timeout}s"
            break
        if d is None:
            status = f"step {i}: process ended before the result"
            break
        turns += 1
        if d.get("is_error"):
            status = f"step {i}: is_error ({d.get('subtype')})"
            break
    try:
        proc.stdin.close()
    except OSError:
        pass
    t0 = time.time()
    while proc.poll() is None and time.time() - t0 < 90:
        time.sleep(0.5)
    if proc.poll() is None:
        proc.kill()
        status += " (killed after close)"
    out.close()
    pathlib.Path(str(out_path) + ".stderr").write_text("".join(err), encoding="utf-8")
    return {"status": status, "turns": turns, "exit": proc.returncode}


# ---- reading a stream -------------------------------------------------------------------------------
def load(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except ValueError:
            pass
    return rows


def our_injections(rows):
    """Non-empty outputs of our hook: [(hook_event, source_or_empty, output)]."""
    found = []
    for d in rows:
        if d.get("type") == "system" and d.get("subtype") == "hook_response" and \
                d.get("hook_event") in ("SessionStart", "UserPromptSubmit"):
            o = d.get("output") or ""
            if any(m in o for m in MARKERS):
                found.append((d.get("hook_event"), (d.get("hook_name") or "").partition(":")[2], o))
    return found


def verify_arm(rows, arm):
    """The arm is really what it claims (CLAUDE.md: check what finally reaches the model)."""
    inj = our_injections(rows)
    want = EXPECTED_INJECTIONS[arm]
    ok = len(inj) == want
    detail = f"{len(inj)} injections, expected {want}"
    if arm == "A1":
        ok = ok and [(e, s) for e, s, _ in inj] == [("SessionStart", "startup"), ("SessionStart", "compact")]
    if arm == "A0":
        ok = ok and not inj
    return ok, detail


def turns(rows):
    """Split the stream into turns by the harness markers: {label: [events]}."""
    out, cur = {}, None
    for d in rows:
        if d.get("type") == "harness":
            cur = d.get("label")
            out[cur] = []
        elif cur is not None:
            out[cur].append(d)
    return out


def norm(s):
    """Lower-case; keep letters, digits, and CJK; drop everything else (frequency-test.md section 6)."""
    return "".join(c for c in s.lower() if unicodedata.category(c)[0] in "LN")


def judge_turn(events, current, stale):
    res = next((d for d in events if d.get("type") == "result"), {})
    text = res.get("result") or ""
    n = norm(text)
    looked = False
    for d in events:
        if d.get("type") == "assistant":
            for c in (d.get("message") or {}).get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_use" and c.get("name") in ("Read", "Grep", "Glob"):
                    s = json.dumps(c.get("input") or {}, ensure_ascii=False)
                    if "SprintBacklog" in s or "sprint-01" in s:
                        looked = True
    return {"quote_current": norm(current) in n, "stale": norm(stale) in n or norm(V1_CLAUSE) in n,
            "looked": looked, "text": text}


def direction(text, want_no):
    """Content column, first pass by keyword; every line is reviewed by hand."""
    neg = re.search(r"(不(能|行|可以|建议|选|纳入|放进|应|予)|先别|暂不|拒绝|超出|不在.{0,8}范围|不碰)", text)
    pos = re.search(r"(可以|同意|选入|没问题|批准|通过|进入 What)", text)
    if bool(neg) == bool(pos):
        return "unclear"
    return "ok" if (bool(neg) == want_no) else "wrong"


def judge_run(path, arm):
    rows = load(path)
    t = turns(rows)
    ok, detail = verify_arm(rows, arm)
    p1 = judge_turn(t.get("P1", []), V2, V1)
    p2 = judge_turn(t.get("P2", []), V2, V1)
    p1["direction"] = direction(p1["text"], want_no=True)
    p2["direction"] = direction(p2["text"], want_no=False)
    compact = any(d.get("subtype") == "compact_boundary" for d in rows if d.get("type") == "system")
    results = [d for d in rows if d.get("type") == "result"]
    usage = {k: sum((d.get("usage") or {}).get(k, 0) or 0 for d in results)
             for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")}
    return {"arm": arm, "valid": ok, "arm_detail": detail, "compact": compact, "P1": p1, "P2": p2,
            "results": len(results), "errors": sum(1 for d in results if d.get("is_error")),
            "duration_ms": sum(d.get("duration_ms", 0) or 0 for d in results), "usage": usage,
            "cost": sum(d.get("total_cost_usd", 0) or 0 for d in results[-1:]),
            "injections": len(our_injections(rows))}


# ---- commands ---------------------------------------------------------------------------------------------
def one_run(out_dir, arm, rep, steps=None, tag=""):
    out_dir = pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    work = pathlib.Path(tempfile.mkdtemp(prefix=f"freq-{arm}-{rep}-"))
    build_fixture(work)
    path = out_dir / f"{tag}{arm}-{rep}.jsonl"
    r = drive(work, path, steps or scenario(), ARMS[arm])
    shutil.rmtree(work, ignore_errors=True)
    return path, r


def cmd_run(a, arms=None, reps=None):
    arms = arms or a.arms.split(",")
    reps = reps or a.reps
    jobs = [(arm, rep) for rep in range(1, reps + 1) for arm in arms]
    done = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.parallel) as ex:
        futs = {ex.submit(one_run, a.out, arm, rep): (arm, rep) for arm, rep in jobs}
        for f in concurrent.futures.as_completed(futs):
            arm, rep = futs[f]
            path, r = f.result()
            done[(arm, rep)] = (path, r)
            print(f"{arm}-{rep}: {r}", flush=True)
    return done


def cmd_judge(a):
    out_dir = pathlib.Path(a.out)
    runs = []
    for p in sorted(out_dir.glob("A?-?.jsonl")):
        arm = p.name[:2]
        j = judge_run(p, arm)
        j["file"] = p.name
        runs.append(j)
    review = []
    lines = ["arm  rep  valid  compact  P1(cur/stale/looked/dir)  P2(cur/stale/looked/dir)  inj  turns  secs  tokens(in+cache/out)"]
    for j in runs:
        u = j["usage"]
        lines.append("{arm}  {rep}  {valid}  {compact}  {p1}  {p2}  {inj}  {n}  {s}  {tin}/{tout}".format(
            arm=j["arm"], rep=j["file"][3], valid=j["valid"], compact=j["compact"],
            p1="/".join(str(int(j['P1'][k])) if k != "direction" else j['P1'][k] for k in ("quote_current", "stale", "looked", "direction")),
            p2="/".join(str(int(j['P2'][k])) if k != "direction" else j['P2'][k] for k in ("quote_current", "stale", "looked", "direction")),
            inj=j["injections"], n=j["results"], s=round(j["duration_ms"] / 1000),
            tin=u["input_tokens"] + u["cache_creation_input_tokens"] + u["cache_read_input_tokens"], tout=u["output_tokens"]))
        review.append(f"### {j['file']}\n\nP1 ({j['P1']['direction']}): {j['P1']['text'][:600]}\n\nP2 ({j['P2']['direction']}): {j['P2']['text'][:600]}\n")
    # per-arm summary (counts over valid runs)
    by = {}
    for j in runs:
        by.setdefault(j["arm"], []).append(j)
    lines.append("")
    lines.append("arm  runs(valid)  P1 cur/stale/looked  P2 cur/stale/looked  injections  passes")
    for arm in sorted(by):
        v = [j for j in by[arm] if j["valid"]]
        c = lambda p, k: sum(1 for j in v if j[p][k])
        n = len(v)
        pass_ = n > 0 and c("P1", "quote_current") * 3 >= 2 * n and c("P2", "quote_current") * 3 >= 2 * n \
            and c("P1", "stale") * 3 <= n and c("P2", "stale") * 3 <= n
        inj = sorted({j["injections"] for j in v})
        lines.append(f"{arm}  {len(by[arm])}({n})  {c('P1','quote_current')}/{c('P1','stale')}/{c('P1','looked')} of {n}  "
                     f"{c('P2','quote_current')}/{c('P2','stale')}/{c('P2','looked')} of {n}  {inj}  {pass_}")
    (out_dir / "summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out_dir / "review.md").write_text("\n".join(review), encoding="utf-8")
    print("\n".join(lines))
    return runs


def cmd_tokens(a):
    """Input tokens added by one injection: the same one-turn prompt under A0 and A2, a few times each."""
    steps = [{"say": "Say only the word: ok", "label": "T1"}]
    rows = {"A0": [], "A2": []}
    for rep in range(1, a.reps + 1):
        for arm in rows:
            path, r = one_run(a.out, arm, rep, steps=steps, tag="tok-")
            d = load(path)
            res = [x for x in d if x.get("type") == "result"]
            u = (res[-1].get("usage") or {}) if res else {}
            tot = sum(u.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"))
            rows[arm].append((tot, len(our_injections(d)), r["status"]))
    for arm, v in rows.items():
        print(arm, v)
    m = lambda arm, i: sum(x[i] for x in rows[arm]) / max(1, len(rows[arm]))
    diff = m("A2", 0) - m("A0", 0)
    inj = m("A2", 1)
    print(f"mean input tokens A0={m('A0', 0):.0f} A2={m('A2', 0):.0f} diff={diff:.0f} injections={inj:.1f} "
          f"=> about {diff / inj:.0f} tokens per injection" if inj else "no injections seen")


def cmd_smoke(a):
    path, r = one_run(a.out, a.arm, 0, tag="smoke-")
    j = judge_run(path, a.arm)
    print(json.dumps(r))
    print(json.dumps({k: v for k, v in j.items() if k not in ("P1", "P2")}, ensure_ascii=False))
    for p in ("P1", "P2"):
        print(p, {k: v for k, v in j[p].items() if k != "text"})
        print("   ", j[p]["text"][:300].replace("\n", " | "))


# ---- self-test (no model calls): the judge on known results ------------------------------------------------
def selftest():
    def turn_events(text, tools=()):
        ev = [{"type": "assistant", "message": {"content": [{"type": "tool_use", "name": n, "input": i} for n, i in tools]}},
              {"type": "result", "result": text, "is_error": False}]
        return ev

    ok = True

    def check(name, cond):
        nonlocal ok
        ok = ok and cond
        print(("PASS  " if cond else "FAIL  ") + name)

    j = judge_turn(turn_events(f"Sprint Goal 原文：「{V2}」。所以不选。"), V2, V1)
    check("full current goal in a quote is a verbatim citation", j["quote_current"] and not j["stale"])
    j = judge_turn(turn_events(f"> {V2}\n\n不选。"), V2, V1)
    check("a Markdown quote with different punctuation still counts", j["quote_current"])
    j = judge_turn(turn_events(f"目标是：{V1}"), V2, V1)
    check("the old goal is stale, not current", (not j["quote_current"]) and j["stale"])
    j = judge_turn(turn_events("目标是导出先快，只导勾选的列。"), V2, V1)
    check("a paraphrase is not a verbatim citation", not j["quote_current"] and not j["stale"])
    j = judge_turn(turn_events("好的", tools=[("Read", {"file_path": "scrum/sprint-01-batch-export/SprintBacklog.md"})]), V2, V1)
    check("a Read of the sprint log is a lookup", j["looked"])
    j = judge_turn(turn_events("好的", tools=[("Read", {"file_path": "README.md"})]), V2, V1)
    check("a Read of another file is not", not j["looked"])
    check("direction: refusal where a refusal is wanted", direction("这一条不能选进本冲刺，超出了目标。", True) == "ok")
    check("direction: agreement where a refusal is wanted", direction("可以，选入本冲刺。", True) == "wrong")

    def hook(event, name, out):
        return {"type": "system", "subtype": "hook_response", "hook_event": event, "hook_name": name, "output": out}

    inj = "Commitments from this project's logs (verbatim):\nProduct: x"
    start = [hook("SessionStart", "SessionStart:startup", inj), hook("SessionStart", "SessionStart:compact", inj)]
    check("A1: two injections, startup and compact", verify_arm(start, "A1")[0])
    check("A1: a third injection is not A1", not verify_arm(start + [hook("UserPromptSubmit", "UserPromptSubmit", inj)], "A1")[0])
    check("A0: no injection", verify_arm([hook("SessionStart", "SessionStart:startup", "")], "A0")[0])
    check("A0: any injection fails the control", not verify_arm(start, "A0")[0])
    check("other plugins' hooks are not ours", verify_arm([hook("UserPromptSubmit", "UserPromptSubmit", "other plugin text")], "A0")[0])
    s = scenario()
    check("scenario has 14 prompts, one change, one /compact",
          sum(1 for x in s if "say" in x and x["say"] != "/compact") == 14 and sum(1 for x in s if "replace" in x) == 1
          and sum(1 for x in s if x.get("say") == "/compact") == 1)
    labels = [x["label"] for x in s]
    check("P1 comes after the change and before the compact; P2 is last",
          labels.index("change") < labels.index("P1") < labels.index("compact") < labels.index("P2") == len(labels) - 1)
    with tempfile.TemporaryDirectory() as d:
        build_fixture(d)
        t = (pathlib.Path(d) / SPRINT_DIR / "SprintBacklog.md").read_text(encoding="utf-8")
        check("fixture holds v1 and not v2 at the start", V1 in t and V2 not in t)
    print("selftest", "OK" if ok else "FAILED")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["selftest", "smoke", "run", "judge", "tokens"])
    ap.add_argument("--out")
    ap.add_argument("--arm", default="A2")
    ap.add_argument("--arms", default="A0,A1,A2,A3,A4")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--parallel", type=int, default=1)
    a = ap.parse_args()
    if a.cmd == "selftest":
        return selftest()
    if not a.out:
        ap.error("--out is required")
    {"smoke": cmd_smoke, "run": cmd_run, "judge": cmd_judge, "tokens": cmd_tokens}[a.cmd](a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
