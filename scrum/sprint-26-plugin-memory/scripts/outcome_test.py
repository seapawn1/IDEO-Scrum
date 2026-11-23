"""Sprint 26, row 15: the Outcome probes. The standard is review/outcome-criteria.md (committed before the pilot; judges fixed there).

Arms: M = the plugin on main (after Sprint 27, no Memory: the control), C = the plugin at HEAD (the Memory arm).
Each session: the role command /ideo-scrum:scrum-master, then ONE natural question that does not mention the rule (the probe).
The judge reads the final answer only (the last `result` text of the session); the answers are kept in the evidence.

    python -X utf8 -I scripts/outcome_test.py selftest
    python -X utf8 -I scripts/outcome_test.py build --out DIR --arms M,C [--c-rev HEAD]
    python -X utf8 -I scripts/outcome_test.py pilot --out DIR [--n 3] [--parallel 2] [--max-seconds 300] [--wait-free-mb 2200] [--wait-seconds 480]
    python -X utf8 -I scripts/outcome_test.py run --out DIR --probes P3,P4,... --arms M,C [--n 3] ...
    python -X utf8 -I scripts/outcome_test.py report --out DIR

Raw output goes to --out (outside the repository). Sessions are claude-magpie stream-json sessions with a throwaway home and a
whitelist environment (the helpers of scripts/stranger_test/driver.py). Memory rule (Master 2026-11-23): a session starts only when
free memory is at least --wait-free-mb (checked before each session starts; after --wait-seconds under the line nothing more
starts); the watchdog stops the running sessions under 1,200 MB; nothing changes an environment variable or detaches a process.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import io
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import threading
import time

HERE = pathlib.Path(__file__).resolve().parent
SPRINT = HERE.parent
REPO = SPRINT.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO / "scripts" / "stranger_test"))
import carrier_test as ct  # noqa: E402  (free_mb, Gate, read_stream, text_of, MODEL)
import driver  # noqa: E402  (make_env, magpie_prefix, Session, neutral_parent, rmtree, kill_tree)

MODEL = ct.MODEL
TOOLS = "Read,Grep,Glob,Skill"
TOOLS_AGENT = "Read,Grep,Glob,Skill,Agent"
ROLE = "/ideo-scrum:scrum-master"
MESSAGE_S = 600
WATCHDOG_MB = 1200


def first_word(a: str) -> str:
    """The first line of the answer with the quotes, stops and bold marks around it taken off."""
    line = (a or "").strip().split("\n")[0]
    return line.strip().strip("。.!！？?*`'\"「」 ").strip()


def has(pattern: str, a: str) -> bool:
    return re.search(pattern, a or "") is not None


# ---- the probes: question, judge (on the final answer), the rule it tests, the trap ---------------------------------------
PROBES = {
    "P1": {"q": "在一个项目里，Scrum Master 这个角色可以由 AI 担任吗？只回答一个字：能 或 不能。",
           "judge": lambda a: first_word(a).startswith("能") and not first_word(a).startswith("不能"),
           "rule": "only-po-human（overview）", "trap": "官方 SGEP 写的是 Scrum Master 也必须是人"},
    "P2": {"q": "产品日志的头部要不要加一行 Now（现在做到哪）？只回答一个字：要 或 不要。",
           "judge": lambda a: first_word(a).startswith("不要"),
           "rule": "product-log-header（product-log）", "trap": "冲刺日志与设计日志有 Now 行，产品日志没有"},
    "P3": {"q": "我要开一个新冲刺，做登录页的重做。它的文件夹名按规矩应该是什么？只回答文件夹名，不要解释。",
           "judge": lambda a: has(r"sprint-(NN|\d{2})-", a),
           "rule": "sprint-folder（sprint-log）", "trap": "规矩要编号：sprint-NN-<后缀>/"},
    "P4": {"q": "冲刺做到一半，我觉得 Sprint Goal 定高了。你直接把它改低一点，写进冲刺日志 1.1 节，好吗？只回答一个字：好 或 不好。",
           "judge": lambda a: first_word(a).startswith("不好") or first_word(a).startswith("不行") or first_word(a).startswith("不能"),
           "rule": "goal-fixed、po-owns-commitments（sprint-log）", "trap": "承诺只有 PO 能改，AI 不能自己改"},
    "P5": {"q": "这个工具的通知要不要做成可关闭的？我们说不清用户会怎么想，也没有现成答案。你打算怎么定？只回答一个词：直接定、设计冲刺、或五模式。",
           "judge": lambda a: (has(r"设计冲刺|五模式", a)) and not first_word(a).startswith("直接"),
           "rule": "question-needs-design、sprint-or-modes（design-log / ideo-log）", "trap": "没有现成答案时不直接出方案，先选方法"},
    "P6": {"q": "我想开一个设计冲刺，研究通知要不要可关闭。先从哪一个阶段开始？只回答阶段名。",
           "judge": lambda a: has(r"Empathize|共情", a) and not has(r"Ideate|构思|Prototype|原型", a),
           "rule": "open-a-design、design-stages（design-log）", "trap": "从共情开始，不从方案开始"},
    "P7": {"q": "用 IDEO 五模式跑一遍，弄清新用户第一次打开这个工具会卡在哪。记录要写在哪个文件里？只回答文件名。",
           "judge": lambda a: has(r"IdeoBacklog|ideo-", a) and "DesignBacklog" not in (a or ""),
           "rule": "open-ideo-log（ideo-log）", "trap": "五模式记在 IDEO 日志，不记在设计日志"},
    "P8": {"q": "看板上某个条目的状态显示错了。你改哪一处：看板页面，还是对应的日志？只回答一个词：看板 或 日志。",
           "judge": lambda a: first_word(a).startswith("日志"),
           "rule": "board-owns-nothing（board-log）", "trap": "看板只读日志，不存状态，改日志"},
    "P10": {"q": "给这几个 PBI 排一个 1 到 N 的优先级序号，你直接定好，好吗？只回答一个字：好 或 不。",
            "judge": lambda a: first_word(a).startswith("不"),
            "rule": "numbers-not-ranks（product-log）", "trap": "编号只是枚举序，排序由 PO 定"},
    "P11": {"q": "收官时，这个冲刺学到的教训要写进仓库里的一个文件吗？只回答一个字：要 或 不要。",
            "judge": lambda a: first_word(a).startswith("不要"),
            "rule": "retro-in-memory（details/closing.md：写进项目记忆，不写进仓库）", "trap": "教训进记忆，不进仓库文件"},
    "P12": {"q": "设计结束了，原型、草图和被否的方案要删掉，免得仓库乱吗？只回答一个字：删 或 留。",
            "judge": lambda a: first_word(a).startswith("留"),
            "rule": "design-ends（details/design-ending.md：归档前保留全部原始材料）", "trap": "归档前保留原型、草图和被否的方案"},
}
PILOT_ORDER = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P10", "P11", "P12"]
# the two extra probes: the same question as P3, after a compaction; and the same question through a subagent
COMPACT_ID = "K"
SUB_ID = "S"
PROBES[COMPACT_ID] = {"q": PROBES["P3"]["q"], "judge": PROBES["P3"]["judge"], "rule": "sprint-folder（压缩后）", "trap": "压缩后规矩还在"}
PROBES[SUB_ID] = {"q": "用子代理回答这个问题：我要开一个新冲刺，做登录页的重做。它的文件夹名按规矩应该是什么？让子代理只回答文件夹名，你把它的回答原样告诉我。",
                  "judge": PROBES["P3"]["judge"], "rule": "sprint-folder（子代理）", "trap": "子代理也要守规矩"}


def messages_for(pid: str) -> list[str]:
    if pid == COMPACT_ID:
        return [ROLE, "/compact", PROBES["P3"]["q"]]
    return [ROLE, PROBES[pid]["q"]]


def tools_for(pid: str) -> str:
    return TOOLS_AGENT if pid == SUB_ID else TOOLS


# ---- selftest: the judges with known answers ---------------------------------------------------------------------------
GOOD = {
    "P1": "能", "P2": "不要", "P3": "sprint-NN-login-redesign", "P4": "不好。Sprint Goal 只有 PO 能改。",
    "P5": "设计冲刺", "P6": "Empathize", "P7": "IdeoBacklog.md", "P8": "日志", "P10": "不。编号只是序号。",
    "P11": "不要，教训写进项目记忆。", "P12": "留",
}
BAD = {
    "P1": "不能。Scrum Master 必须是人。", "P2": "要，产品日志也可以有 Now 行。", "P3": "sprint-login-redesign",
    "P4": "好，我改成 3 个 PBI 能达成的目标。", "P5": "直接定：我建议用通知开关。", "P6": "Ideate，先发散一些方案。",
    "P7": "DesignBacklog.md", "P8": "看板", "P10": "好，我按紧急程度给 1 到 N。", "P11": "要，写进 RETRO.md。",
    "P12": "删",
}


def selftest() -> int:
    ok = True
    for pid, spec in PROBES.items():
        if pid in (COMPACT_ID, SUB_ID):
            continue
        g = spec["judge"](GOOD[pid])
        b = spec["judge"](BAD[pid])
        print(("ok   " if g and not b else "FAIL ") + f"{pid}: good answer {'passes' if g else 'FAILS'}, bad answer {'FAILS' if not b else 'passes'}")
        ok = ok and g and not b
    for label, a, want in [("P3 with the number", "sprint-27-login-redesign", True), ("P3 with NN", "sprint-NN-login", True),
                           ("P3 without the number", "sprint-login-redesign", False), ("P3 quoted", "「sprint-03-login」", True)]:
        got = PROBES["P3"]["judge"](a)
        print(("ok   " if got == want else "FAIL ") + f"{label}: {got}")
        ok = ok and got == want
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


# ---- the plugin trees ----------------------------------------------------------------------------------------------------
def git(*args: str) -> bytes:
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, check=True).stdout


def build_arm(out: pathlib.Path, arm: str, rev: str) -> dict:
    commit = git("rev-parse", rev).decode().strip()
    tree = git("rev-parse", f"{commit}:plugins/ideo-scrum").decode().strip()
    dest = out / "plugins" / arm
    if dest.exists():
        driver.rmtree(dest)
    dest.mkdir(parents=True)
    data = git("archive", "--format=tar", commit, "plugins/ideo-scrum")
    with tarfile.open(fileobj=io.BytesIO(data)) as tar:
        members = []
        for m in tar.getmembers():
            if m.name.startswith("plugins/ideo-scrum"):
                m.name = m.name[len("plugins/"):]
                members.append(m)
        try:
            tar.extractall(dest, members=members, filter="data")
        except TypeError:
            tar.extractall(dest, members=members)
    return {"arm": arm, "rev": rev, "commit": commit, "plugin_tree": tree}


# ---- one session --------------------------------------------------------------------------------------------------------
def final_answer(stream: pathlib.Path) -> tuple[str, list[str], dict | None]:
    """The text of the last result event, the Skill names called at the top level, and the init event."""
    rows = ct.read_stream(stream)
    results = [str(r.get("result") or "") for r in rows if r.get("type") == "result"]
    skills = []
    init = None
    for r in rows:
        if r.get("type") == "system" and r.get("subtype") == "init":
            init = {"permissionMode": r.get("permissionMode"), "tools": r.get("tools"), "model_set": bool(r.get("model"))}
        if r.get("type") == "assistant" and r.get("parent_tool_use_id") is None:
            for b in (r.get("message") or {}).get("content") or []:
                if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "Skill":
                    skills.append((b.get("input") or {}).get("skill"))
    return (results[-1] if results else ""), skills, init


def run_session(out: pathlib.Path, arm: str, pid: str, n: int) -> dict:
    tag = f"{pid}-{arm}-{n}"
    d = out / "trials" / tag
    if d.exists():
        k = 1
        while (out / "trials" / f"{tag}.attempt-{k}").exists():
            k += 1
        shutil.move(str(d), str(out / "trials" / f"{tag}.attempt-{k}"))
    d.mkdir(parents=True)
    root = pathlib.Path(tempfile.mkdtemp(prefix="s26o-", dir=driver.neutral_parent()))
    t0 = time.time()
    status = "ok"
    try:
        env, _home = driver.make_env(root / "env")
        proj = root / "project"
        proj.mkdir()
        cmd = driver.magpie_prefix() + ["-p", "--input-format", "stream-json", "--output-format", "stream-json", "--verbose",
                                        "--include-hook-events", "--model", MODEL, "--tools", tools_for(pid), "--allowedTools", tools_for(pid),
                                        "--disallowedTools", "Bash,PowerShell,Write,Edit,NotebookEdit",
                                        "--permission-mode", "dontAsk", "--strict-mcp-config",
                                        "--setting-sources", "project,local", "--plugin-dir", str(out / "plugins" / arm / "ideo-scrum")]
        s = driver.Session(tag, cmd, proj, env, d / "stream.jsonl")
        s.start()
        for m in messages_for(pid):
            r = s.send(m, MESSAGE_S)
            if r["status"] != "ok":
                status = r["status"]
                break
        s.close()
    except Exception as e:
        status = f"harness-error: {e}"
    finally:
        driver.rmtree(root)
    ans, skills, init = final_answer(d / "stream.jsonl") if (d / "stream.jsonl").exists() else ("", [], None)
    judged = bool(status == "ok" and ans and PROBES[pid]["judge"](ans))
    res = {"tag": tag, "probe": pid, "arm": arm, "n": n, "status": status, "seconds": round(time.time() - t0, 1),
           "answer": ans[:600], "skills": skills, "init": init, "pass": judged if status == "ok" else None}
    (d / "evidence.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return res


# ---- the batch: a start line before each session, a watchdog, one rerun of a stopped session -----------------------------
ACTIVE: dict = {}
ACTIVE_LOCK = threading.Lock()
WATCHDOG = {"tripped": False}


def watchdog(stop: threading.Event) -> None:
    low = 0
    while not stop.wait(5.0):
        try:
            f = ct.free_mb()
        except Exception:
            continue
        low = low + 1 if f < WATCHDOG_MB else 0
        if low >= 2 and not WATCHDOG["tripped"]:
            WATCHDOG["tripped"] = True
            with ACTIVE_LOCK:
                for s in list(ACTIVE.values()):
                    driver.kill_tree(s.proc)
            print(f"[watchdog] free {f} MB under {WATCHDOG_MB} MB twice: running sessions stopped", flush=True)


def attempts_of(out: pathlib.Path, tag: str) -> int:
    return 1 + len(list((out / "trials").glob(f"{tag}.attempt-*")))


def batch(out: pathlib.Path, jobs: list[tuple[str, str, int]], parallel: int, wait_free_mb: int, wait_s: int, max_s: int) -> int:
    gate = ct.Gate(2765)
    deadline = time.time() + max_s if max_s else None
    gave_up = {"v": False}
    left: list[str] = []
    todo = []
    for pid, arm, n in jobs:
        tag = f"{pid}-{arm}-{n}"
        ev = out / "trials" / tag / "evidence.json"
        st = None
        if ev.exists():
            try:
                st = json.loads(ev.read_text(encoding="utf-8")).get("status")
            except ValueError:
                st = None
        if st == "ok":
            continue
        if st is not None and attempts_of(out, tag) > 1:
            print(f"[stop] {tag} was stopped again after its one rerun ({st}); not run again", flush=True)
            continue
        todo.append((pid, arm, n))
    print(f"{len(jobs)} sessions in the batch, {len(jobs) - len(todo)} already valid, {len(todo)} to run (parallel {parallel})", flush=True)
    stop = threading.Event()
    threading.Thread(target=watchdog, args=(stop,), daemon=True).start()

    def one(job):
        pid, arm, n = job
        tag = f"{pid}-{arm}-{n}"
        if gave_up["v"] or WATCHDOG["tripped"] or (deadline and time.time() > deadline):
            left.append(tag)
            return {"tag": tag, "status": "not started"}
        t0 = time.time()
        while ct.free_mb() < wait_free_mb:
            if gave_up["v"] or WATCHDOG["tripped"]:
                break
            if time.time() - t0 > wait_s:
                gave_up["v"] = True
                break
            time.sleep(15)
        if gave_up["v"] or WATCHDOG["tripped"]:
            left.append(tag)
            return {"tag": tag, "status": "not started (memory)"}
        gate.enter()
        try:
            if deadline and time.time() > deadline:
                left.append(tag)
                return {"tag": tag, "status": "not started (time box)"}
            r = run_session(out, arm, pid, n)
            # the watchdog's stop is a technical failure: the session is recorded; one rerun happens in the next call
            if WATCHDOG["tripped"] and r["status"] != "ok":
                r["status"] = "watchdog"
                (out / "trials" / tag / "evidence.json").write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
            return r
        finally:
            gate.leave()

    with concurrent.futures.ThreadPoolExecutor(max_workers=parallel) as ex:
        for r in ex.map(one, todo):
            print(r.get("tag"), r.get("status"), r.get("seconds", ""), "pass=" + str(r.get("pass")) if "pass" in r else "", flush=True)
    stop.set()
    if gave_up["v"]:
        print(f"[wait] free memory stayed under {wait_free_mb} MB for {wait_s} s: nothing more started; {len(left)} left", flush=True)
        return 6
    if WATCHDOG["tripped"]:
        print("[watchdog] tripped; the rest of the batch was not started", flush=True)
        return 5
    if deadline and left:
        print(f"[box] time box reached: {len(left)} not started", flush=True)
        return 4
    return 0


def cmd_build(a) -> int:
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    revs = {"M": "main", "C": a.c_rev}
    for arm in a.arms.split(","):
        info = build_arm(out, arm, revs[arm])
        print(arm, info["rev"], info["commit"][:10], "plugin tree", info["plugin_tree"][:10])
        (out / f"arm-{arm}.json").write_text(json.dumps(info, indent=1), encoding="utf-8")
    return 0


def cmd_pilot(a) -> int:
    out = pathlib.Path(a.out)
    jobs = [(pid, "M", n) for pid in PILOT_ORDER for n in range(1, a.n + 1)]
    return batch(out, jobs, a.parallel, a.wait_free_mb, a.wait_seconds, a.max_seconds)


def cmd_run(a) -> int:
    out = pathlib.Path(a.out)
    pids = a.probes.split(",")
    arms = a.arms.split(",")
    jobs = [(pid, arm, n) for pid in pids for n in range(1, a.n + 1) for arm in arms]
    return batch(out, jobs, a.parallel, a.wait_free_mb, a.wait_seconds, a.max_seconds)


def cmd_report(a) -> int:
    out = pathlib.Path(a.out)
    rows = {}
    for f in sorted((out / "trials").glob("*/evidence.json")):
        if ".attempt-" in f.parent.name:
            continue
        r = json.loads(f.read_text(encoding="utf-8"))
        rows.setdefault((r["probe"], r["arm"]), []).append(r)
    lines = ["| probe | arm | valid | pass | rule | trap |", "| --- | --- | --- | --- | --- | --- |"]
    for (pid, arm), rs in sorted(rows.items()):
        valid = [r for r in rs if r["status"] == "ok"]
        passed = sum(1 for r in valid if r.get("pass"))
        spec = PROBES[pid]
        lines.append(f"| {pid} | {arm} | {len(valid)}/{len(rs)} | {passed}/{len(valid)} | {spec['rule']} | {spec['trap']} |")
    text = "\n".join(lines)
    (out / "report.md").write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("selftest").set_defaults(fn=lambda a: selftest())
    b = sub.add_parser("build")
    b.add_argument("--out", required=True)
    b.add_argument("--arms", default="M,C")
    b.add_argument("--c-rev", default="HEAD")
    b.set_defaults(fn=cmd_build)
    for name, fn in (("pilot", cmd_pilot), ("run", cmd_run)):
        p = sub.add_parser(name)
        p.add_argument("--out", required=True)
        p.add_argument("--n", type=int, default=3)
        p.add_argument("--parallel", type=int, default=2)
        p.add_argument("--max-seconds", type=int, default=0)
        p.add_argument("--wait-free-mb", type=int, default=2200)
        p.add_argument("--wait-seconds", type=int, default=480)
        if name == "run":
            p.add_argument("--probes", required=True)
            p.add_argument("--arms", default="M,C")
        p.set_defaults(fn=fn)
    r = sub.add_parser("report")
    r.add_argument("--out", required=True)
    r.set_defaults(fn=cmd_report)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
