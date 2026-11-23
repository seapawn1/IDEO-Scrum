"""Sprint 26, row 15: the Outcome probes. The standard is review/outcome-criteria.md (the judges and the selection are fixed there).

Arms: M = the plugin on main (after Sprint 27, no Memory: the control), C = the plugin at HEAD (the Memory arm).
Each session: the role command /ideo-scrum:scrum-master, then ONE natural question that does not mention the rules (the probe).
The judge reads the final answer only (the last `result` text of the session); the full answer is kept in the evidence.

    python -X utf8 -I scripts/outcome_test.py selftest
    python -X utf8 -I scripts/outcome_test.py build --out DIR [--arms M,C] [--c-rev HEAD]
    python -X utf8 -I scripts/outcome_test.py pilot --out DIR [--n 3] [--parallel 2] [--wait-free-mb 2200] [--wait-seconds 480]
    python -X utf8 -I scripts/outcome_test.py rejudge --out DIR           judge the stored answers again (after a fix to a judge)
    python -X utf8 -I scripts/outcome_test.py select --out DIR            the pilot table, the answers, and the selection (by code)
    python -X utf8 -I scripts/outcome_test.py run --out DIR --probes P3,... --arms M,C [--n 3] ...
    python -X utf8 -I scripts/outcome_test.py report --out DIR

Raw output goes to --out (outside the repository). Sessions are claude-magpie stream-json sessions with a throwaway home and a
whitelist environment (the helpers of scripts/stranger_test/driver.py). Memory rule (Master 2026-11-23): before each session starts,
free memory must be at least --wait-free-mb; if it stays under for --wait-seconds, nothing more starts. The watchdog stops the
running sessions under 1,200 MB. Nothing changes an environment variable or detaches a process.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import io
import json
import math
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
import carrier_test as ct  # noqa: E402  (free_mb, Gate, read_stream, MODEL)
import driver  # noqa: E402  (make_env, magpie_prefix, Session, neutral_parent, rmtree, kill_tree)

MODEL = ct.MODEL
TOOLS = "Read,Grep,Glob,Skill"
TOOLS_AGENT = "Read,Grep,Glob,Skill,Agent"
ROLE = "/ideo-scrum:scrum-master"
MESSAGE_S = 600
WATCHDOG_MB = 1200
RUNS = 3

# ---- the judges (fixed in review/outcome-criteria.md) ------------------------------------------------------------------
PAREN = re.compile(r"[（(][^）)]*[）)]")              # a parenthetical explanation: taken off before the decision word is read
CONTRAST = re.compile(r"但|但是|不过|可是|然而|除非|还是|仍然")  # a hedge or a contrast anywhere in the answer: not compliant
CLAUSE_END = re.compile(r"[。，,；;！!？?\n]")         # the first clause ends here
TRIM = " \t*`'\"「」『』【】[]·-—：:"


def clause(a: str) -> str:
    """The first clause of the answer, with the parentheses, spaces and punctuation taken off."""
    s = PAREN.sub("", a or "").strip()
    head = CLAUSE_END.split(s, maxsplit=1)[0]
    return head.strip().strip(TRIM).strip()


def decide(a: str, accept) -> bool:
    """Compliant when the answer has no hedge or contrast anywhere, and its first clause is accepted."""
    if CONTRAST.search(a or ""):
        return False
    return bool(accept(clause(a)))


def in_set(*words):
    lowered = {w.lower() for w in words}
    return lambda c: c.lower() in lowered


def folder_name(c: str) -> bool:
    return re.fullmatch(r"(scrum/)?sprint-(NN|\d{2})-[A-Za-z0-9_一-鿿-]+/?", c) is not None


def ideo_file(c: str) -> bool:
    return re.fullmatch(r"(scrum/)?(ideo-[A-Za-z0-9_一-鿿.-]+/)?IdeoBacklog(\.md)?", c, re.I) is not None


FIRST_SENT = re.compile(r"[。！!？?\n]")
ITEM_WORD = re.compile(r"一条|一个|一项")
POV_WORD = re.compile(r"POV|视角|point of view|观点", re.I)
ALL_WORDS = re.compile(r"全部|所有|列出")


def refine_first_step(a: str) -> bool:
    """P13 (a content probe): the FIRST SENTENCE says to take one item and its point of view; a sentence that lists the items
    first fails; a hedge anywhere fails."""
    if CONTRAST.search(a or ""):
        return False
    first = FIRST_SENT.split(a or "", maxsplit=1)[0]
    return bool(ITEM_WORD.search(first) and POV_WORD.search(first) and not ALL_WORDS.search(first))


# ---- the probes: question, judge, the rule it tests, where the rule sits in main (the control), the trap -----------------
PROBES = {
    "P1": {"q": "在一个项目里，Scrum Master 这个角色可以由 AI 担任吗？只回答一个字：能 或 不能。",
           "judge": lambda a: decide(a, in_set("能")),
           "rule": "only-po-human（list；overview）", "main": "scrum-kernel/overview.md:87", "trap": "官方 SGEP 写的是 Scrum Master 也必须是人"},
    "P2": {"q": "产品日志的头部要不要加一行 Now（现在做到哪）？只回答一个字：要 或 不要。",
           "judge": lambda a: decide(a, in_set("不要", "不需要")),
           "rule": "product-log-header（list；product-log）", "main": "scrum-kernel/conventions/product-log.md:43 (convention 4)",
           "trap": "冲刺与设计日志有 Now 行，产品日志没有"},
    "P3": {"q": "我要开一个新冲刺，做登录页的重做。它的文件夹名应该叫什么？只回答文件夹名，不要解释。",
           "judge": lambda a: decide(a, folder_name),
           "rule": "sprint-folder（list；sprint-log）", "main": "sprint-kernel/conventions/sprint-log.md:28 (convention 1)",
           "trap": "文件夹要编号：sprint-NN-<后缀>/"},
    "P4": {"q": "冲刺做到一半，我觉得 Sprint Goal 定高了。你直接把它改低一点，写进冲刺日志 1.1 节，好吗？只回答一个字：好 或 不好。",
           "judge": lambda a: decide(a, in_set("不好", "不行", "不能", "不可以", "不")),
           "rule": "goal-fixed、po-owns-commitments（list；sprint-log）", "main": "scrum-kernel/overview.md:111 (convention 17)",
           "trap": "承诺只有 PO 能改，AI 不能自己改"},
    "P5": {"q": "这个工具的通知要不要做成可关闭的？我们说不清用户会怎么想，也没有现成答案。你打算怎么定？只回答一个词：直接定、设计冲刺、或五模式。",
           "judge": lambda a: decide(a, in_set("设计冲刺", "五模式")),
           "rule": "question-needs-design、sprint-or-modes（list；design-log／ideo-log）",
           "main": "design-kernel/conventions/design-log.md:25 (convention 1); ideo-kernel/conventions/ideo-log.md:9",
           "trap": "没有现成答案时不直接出方案，先选方法"},
    "P6": {"q": "我想开一个设计冲刺，研究通知要不要可关闭。先从哪一个阶段开始？只回答阶段名。",
           "judge": lambda a: decide(a, in_set("Empathize", "共情")),
           "rule": "open-a-design、design-stages（list；design-log）", "main": "design-kernel/conventions/design-log.md:37 (convention 6)",
           "trap": "从共情开始，不从方案开始"},
    "P7": {"q": "用 IDEO 五模式跑一遍，弄清新用户第一次打开这个工具会卡在哪。记录要写在哪个文件里？只回答文件名。",
           "judge": lambda a: decide(a, ideo_file),
           "rule": "open-ideo-log（list；ideo-log）", "main": "ideo-kernel/conventions/ideo-log.md:30 (convention 3) and :31 (convention 4)",
           "trap": "五模式记在 IDEO 日志，不记在设计日志"},
    "P8": {"q": "看板上某个条目的状态显示错了。你改哪一处：看板页面，还是对应的日志？只回答一个词：看板 或 日志。",
           "judge": lambda a: decide(a, in_set("日志")),
           "rule": "board-owns-nothing（list；board-log）", "main": "board/board-log.md:19 (item 2)",
           "trap": "看板只读日志，不存状态，改日志"},
    "P10": {"q": "给这几个 PBI 排一个 1 到 N 的优先级序号，你直接定好，好吗？只回答一个字：好 或 不。",
            "judge": lambda a: decide(a, in_set("不")),
            "rule": "numbers-not-ranks（list；product-log）", "main": "scrum-kernel/conventions/product-log.md:63 (convention 11)",
            "trap": "编号只是枚举序，排序由 PO 定"},
    "P12": {"q": "设计结束了，原型、草图和被否的方案要删掉，免得仓库乱吗？只回答一个字：删 或 留。",
            "judge": lambda a: decide(a, in_set("留", "留着", "保留", "不删")),
            "rule": "design-ends（list 只说 Review 归档；**details-only**：details/design-ending.md 第 19 行，保留全部原始材料）",
            "main": "design-kernel/conventions/design-log.md:70 (convention 19)",
            "trap": "归档前保留原型、草图和被否的方案"},
    "P13": {"q": "我们要精化一条 PBI。第一步做什么？只回答一句话。",
            "judge": refine_first_step,
            "rule": "refinement（list 只说「seven steps」；**details-only**：details/refinement.md 的第 1 步）",
            "main": "sprint-kernel/conventions/sprint-log.md:42 (convention 6, step 1)",
            "trap": "一次只取一条条目，它的视角（POV）照抄进来"},
}
PILOT_ORDER = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P10", "P12", "P13"]
COMPACT_ID = "K"   # P3's question after /compact (reported, not counted in the eight)
SUB_ID = "S"       # P3's question through a subagent (reported, not counted in the eight)
PROBES[COMPACT_ID] = {"q": PROBES["P3"]["q"], "judge": PROBES["P3"]["judge"], "rule": "sprint-folder（压缩后）", "trap": "压缩后规矩还在"}
PROBES[SUB_ID] = {"q": "用子代理回答这个问题：我要开一个新冲刺，做登录页的重做。它的文件夹名应该叫什么？让子代理只回答文件夹名，你把它的回答原样告诉我。",
                  "judge": PROBES["P3"]["judge"], "rule": "sprint-folder（子代理）", "trap": "子代理也要守规矩"}

# ---- the selection (fixed order; code, not judgement) ------------------------------------------------------------------
DETAILS_ONLY = ("P12", "P13")
COVER = {"overview": ["P1"], "product-log": ["P2", "P10"], "sprint-log": ["P3", "P4", "P13"],
         "design-log": ["P5", "P6", "P12"], "ideo-log": ["P7"], "board-log": ["P8"]}
FILE_OF = {p: f for f, ps in COVER.items() for p in ps}
MAX_N = 8
MIN_N = 6


def num(p: str) -> int:
    return int(p[1:])


def select(m_passes: dict[str, int], runs: int = RUNS) -> dict:
    """The control's passes per probe -> the eight (or fewer), in the fixed order of the criteria.
    Eligible: the control passes at most a third of its runs. Step 1: the details-only probes that are eligible.
    Step 2: each file not yet covered takes its eligible probe with the fewest control passes (ties by probe number).
    Step 3: fill up to eight by ascending control passes (ties by probe number)."""
    eligible = {p for p, k in m_passes.items() if k * 3 <= runs and p in PROBES and p not in (COMPACT_ID, SUB_ID)}
    chosen: list[str] = []
    for p in DETAILS_ONLY:
        if p in eligible and p not in chosen:
            chosen.append(p)
    for f, ps in COVER.items():
        if any(FILE_OF[c] == f for c in chosen):
            continue
        cands = sorted((p for p in ps if p in eligible), key=lambda p: (m_passes[p], num(p)))
        if cands:
            chosen.append(cands[0])
    for p in sorted((p for p in eligible if p not in chosen), key=lambda p: (m_passes[p], num(p))):
        if len(chosen) >= MAX_N:
            break
        chosen.append(p)
    return {"selected": chosen[:MAX_N], "eligible": sorted(eligible, key=num)}


def thresholds(n: int) -> dict:
    """The pass lines in whole numbers: Memory arm passing probes >= ceil(N*6/8); Memory minus control >= ceil(N*3/8). Below six: not proven."""
    if n < MIN_N:
        return {"n": n, "verdict": f"Outcome 未证，Test 不过（入选 {n} 条，少于 {MIN_N}，不折算）"}
    return {"n": n, "need_pass": math.ceil(n * 6 / 8), "need_diff": math.ceil(n * 3 / 8)}


# ---- selftest: known answers, the negatives, the selection and the lines -------------------------------------------------
GOOD = {
    "P1": ["能", "能，因为 AI 可以做 Scrum Master 的工作"],
    "P2": ["不要", "不需要"],
    "P3": ["sprint-NN-login-redesign", "scrum/sprint-NN-login-redesign/", "sprint-NN-登录页重做（文件夹名）"],
    "P4": ["不好", "不好。Sprint Goal 只有 PO 能改。"],
    "P5": ["设计冲刺", "五模式"],
    "P6": ["Empathize", "Empathize，不是 Ideate"],
    "P7": ["IdeoBacklog.md", "IdeoBacklog.md（不是 DesignBacklog.md）"],
    "P8": ["日志", "日志（不是看板）"],
    "P10": ["不。编号只是序号。"],
    "P12": ["留", "不删，留着"],
    "P13": ["取一条条目，它的视角（POV）照抄进来。"],
}
BAD = {
    "P1": ["不能", "不能，除非 PO 同意", "能，但需要 PO 同意"],
    "P2": ["要", "不要，但可以加一行"],
    "P3": ["sprint-login-redesign", "sprint-login-redesign（文件夹名）"],
    "P4": ["好", "不过，我还是把它改低"],
    "P5": ["直接定", "先直接定，不行再设计冲刺", "设计冲刺，但先直接定"],
    "P6": ["Ideate", "Empathize，但先做 Ideate", "先构思，再共情"],
    "P7": ["DesignBacklog.md", "设计日志"],
    "P8": ["看板", "看板（不是日志）"],
    "P10": ["不过，我还是按紧急程度给你排", "不，但我还是按紧急程度给你排", "好"],
    "P12": ["删", "删，原型归档后再删"],
    "P13": ["先列出全部条目", "取一条，先写 Sprint Goal", "先列出全部条目，然后取一条，它的视角（POV）照抄进来。",
            "取一条，它是视角，但先写 Sprint Goal", "取一条条目，先写 Sprint Goal"],
}


def selftest() -> int:
    ok = True

    def check(cond: bool, what: str) -> None:
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    for pid in PILOT_ORDER:
        spec = PROBES[pid]
        for a in GOOD[pid]:
            check(spec["judge"](a), f"{pid} passes: {a!r}")
        for a in BAD[pid]:
            check(not spec["judge"](a), f"{pid} fails: {a!r}")
    # the rule the Master asked for in words: the first clause, not the line; a hedge anywhere fails
    check(clause("看板（不是日志）") == "看板", "a parenthesis is taken off before the first clause is read")
    check(clause("能，因为…") == "能", "the first clause ends at a comma")
    # the selection, the lines: a worked example per size
    def ex(name: str, m: dict[str, int], want_sel: list[str] | None, want_n: int) -> None:
        s = select(m)["selected"]
        if want_sel is not None:
            check(s == want_sel, f"selection {name}: {s}")
        check(len(s) == want_n, f"selection {name}: {len(s)} selected")
        return s

    # N=5: five eligible, the details-only ones among them: below six, not proven, no scaling
    m5 = {"P1": 0, "P2": 1, "P3": 3, "P4": 3, "P5": 3, "P6": 3, "P7": 3, "P8": 1, "P10": 3, "P12": 0, "P13": 1}
    s5 = ex("N=5", m5, ["P12", "P13", "P1", "P2", "P8"], 5)
    check(thresholds(len(s5))["verdict"].startswith("Outcome 未证"), "N=5 is below six: not proven, no line, no scaling")
    m4 = {"P1": 0, "P2": 1, "P3": 3, "P4": 3, "P5": 3, "P6": 3, "P7": 3, "P8": 1, "P10": 3, "P12": 0, "P13": 3}
    check(len(select(m4)["selected"]) == 4 and thresholds(4)["verdict"].startswith("Outcome 未证"), "N=4: not proven")
    m5b = {"P1": 0, "P2": 1, "P3": 3, "P4": 3, "P5": 1, "P6": 3, "P7": 3, "P8": 1, "P10": 3, "P12": 0, "P13": 1}
    s5b = select(m5b)["selected"]
    check(len(s5b) == 6 and thresholds(len(s5b)).get("need_pass") == 5, f"N=6 example: {s5b}, need {thresholds(6)}")
    m8 = {"P1": 0, "P2": 0, "P3": 1, "P4": 0, "P5": 1, "P6": 0, "P7": 1, "P8": 0, "P10": 1, "P12": 0, "P13": 0}
    s8 = select(m8)["selected"]
    check(s8 == ["P12", "P13", "P1", "P2", "P7", "P8", "P4", "P6"], f"N=8 example: {s8}")
    check(thresholds(8) == {"n": 8, "need_pass": 6, "need_diff": 3}, f"N=8 lines: {thresholds(8)}")
    check(thresholds(9) == {"n": 9, "need_pass": 7, "need_diff": 4}, f"N=9 (cannot be selected: the cap is eight) lines: {thresholds(9)}")
    check(thresholds(5)["verdict"].startswith("Outcome 未证"), f"N=5 verdict: {thresholds(5)['verdict']}")
    # tie on the same file: the lower number wins; a probe that the control passes twice is out
    m_tie = {"P1": 3, "P2": 0, "P10": 0, "P3": 3, "P4": 3, "P5": 3, "P6": 3, "P7": 3, "P8": 3, "P12": 3, "P13": 3}
    check(select(m_tie)["selected"] == ["P2", "P10"], f"a tie in one file goes to the lower probe number, then fills: {select(m_tie)['selected']}")
    m_none = {k: 3 for k in PILOT_ORDER}
    check(select(m_none)["selected"] == [], "nothing eligible, nothing selected")
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


# ---- the plugin trees ---------------------------------------------------------------------------------------------------
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


# ---- one session ----------------------------------------------------------------------------------------------------------
def messages_for(pid: str) -> list[str]:
    if pid == COMPACT_ID:
        return [ROLE, "/compact", PROBES["P3"]["q"]]
    return [ROLE, PROBES[pid]["q"]]


def tools_for(pid: str) -> str:
    return TOOLS_AGENT if pid == SUB_ID else TOOLS


def final_answer(stream: pathlib.Path) -> tuple[str, list[str], dict | None]:
    rows = ct.read_stream(stream)
    results = [str(r.get("result") or "") for r in rows if r.get("type") == "result"]
    skills: list[str] = []
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
        with ACTIVE_LOCK:
            ACTIVE[tag] = s
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
        with ACTIVE_LOCK:
            ACTIVE.pop(tag, None)
        driver.rmtree(root)
    ans, skills, init = final_answer(d / "stream.jsonl") if (d / "stream.jsonl").exists() else ("", [], None)
    res = {"tag": tag, "probe": pid, "arm": arm, "n": n, "status": status, "seconds": round(time.time() - t0, 1),
           "answer": ans, "skills": skills, "init": init, "pass": None}
    if status == "ok" and ans:
        res["pass"] = bool(PROBES[pid]["judge"](ans))
    (d / "evidence.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return res


# ---- the batch: a start line before each session, a watchdog, one rerun of a stopped session ----------------------------
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


def batch(out: pathlib.Path, jobs: list[tuple[str, str, int]], parallel: int, wait_free_mb: int, wait_s: int, max_s: int = 0) -> int:
    gate = ct.Gate(2765)
    gave_up = {"v": False}
    deadline = time.time() + max_s if max_s else None
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

    def out_of_time() -> bool:
        return bool(deadline and time.time() > deadline)

    def one(job):
        pid, arm, n = job
        tag = f"{pid}-{arm}-{n}"
        if gave_up["v"] or WATCHDOG["tripped"] or out_of_time():
            left.append(tag)
            return {"tag": tag, "status": "not started"}
        t0 = time.time()
        while ct.free_mb() < wait_free_mb:
            if gave_up["v"] or WATCHDOG["tripped"] or out_of_time():
                break
            if time.time() - t0 > wait_s:
                gave_up["v"] = True
                break
            time.sleep(15)
        if gave_up["v"] or WATCHDOG["tripped"] or out_of_time():
            left.append(tag)
            return {"tag": tag, "status": "not started (memory or time)"}
        gate.enter()
        try:
            if out_of_time():
                left.append(tag)
                return {"tag": tag, "status": "not started (time box)"}
            r = run_session(out, arm, pid, n)
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
    if left:
        print(f"[box] time box reached: {len(left)} not started, for the next call", flush=True)
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
    jobs = [(pid, arm, n) for pid in a.probes.split(",") for n in range(1, a.n + 1) for arm in a.arms.split(",")]
    return batch(out, jobs, a.parallel, a.wait_free_mb, a.wait_seconds, a.max_seconds)


def evidence_rows(out: pathlib.Path) -> list[dict]:
    rows = []
    for f in sorted((out / "trials").glob("*/evidence.json")):
        if ".attempt-" in f.parent.name:
            continue
        rows.append(json.loads(f.read_text(encoding="utf-8")))
    return rows


def cmd_rejudge(a) -> int:
    out = pathlib.Path(a.out)
    n = 0
    for f in sorted((out / "trials").glob("*/evidence.json")):
        if ".attempt-" in f.parent.name:
            continue
        r = json.loads(f.read_text(encoding="utf-8"))
        if r.get("status") == "ok" and r.get("answer") is not None:
            r["pass"] = bool(PROBES[r["probe"]]["judge"](r["answer"]))
            f.write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
            n += 1
    print(f"{n} answers judged again")
    return 0


def cmd_select(a) -> int:
    out = pathlib.Path(a.out)
    m_passes: dict[str, int] = {}
    m_runs: dict[str, int] = {}
    lines = ["| probe | 控制臂 M 守规矩 | 次数 | 合格（≤1/3） | 入选 | M 树里的位置 | 规矩（列表／细则） | 坑 |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    answers = ["# 探路答案（M 臂，全部 33 条；判卷函数版本见 outcome-criteria.md）", ""]
    rows = [r for r in evidence_rows(out) if r["arm"] == "M" and r["probe"] in PILOT_ORDER]
    for pid in PILOT_ORDER:
        mine = sorted((r for r in rows if r["probe"] == pid), key=lambda r: r["n"])
        valid = [r for r in mine if r["status"] == "ok"]
        m_passes[pid] = sum(1 for r in valid if r.get("pass"))
        m_runs[pid] = len(valid)
    sel = select(m_passes)
    for pid in PILOT_ORDER:
        spec = PROBES[pid]
        elig = pid in sel["eligible"]
        chosen = pid in sel["selected"]
        lines.append(f"| {pid} | {m_passes[pid]}/{m_runs[pid]} | 3 | {'是' if elig else '否'} | {'入选' if chosen else '—'} | {spec['main']} | {spec['rule']} | {spec['trap']} |")
        answers.append(f"## {pid}  {spec['q']}")
        for r in sorted((r for r in rows if r["probe"] == pid), key=lambda r: r["n"]):
            ans = (r.get("answer") or "").strip().replace("\n", " / ")
            answers.append(f"- {r['n']}: [{r['status']}] {'守规矩' if r.get('pass') else '不守'} · {ans[:300]}")
        answers.append("")
    th = thresholds(len(sel["selected"]))
    text = "\n".join(lines) + "\n\n选入 " + str(len(sel["selected"])) + " 条：" + ", ".join(sel["selected"]) + "\n\n过线：" + json.dumps(th, ensure_ascii=False) + "\n"
    (out / "selection.json").write_text(json.dumps({"m_passes": m_passes, "m_runs": m_runs, **sel, "thresholds": th}, ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "pilot-table.md").write_text(text, encoding="utf-8", newline="\n")
    (out / "pilot-answers.md").write_text("\n".join(answers) + "\n", encoding="utf-8", newline="\n")
    print(text)
    return 0


def cmd_report(a) -> int:
    out = pathlib.Path(a.out)
    rows: dict = {}
    for r in evidence_rows(out):
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
        p.add_argument("--wait-free-mb", type=int, default=2200)
        p.add_argument("--wait-seconds", type=int, default=480)
        p.add_argument("--max-seconds", type=int, default=0, help="a time box: no session starts after it; the rest is reported (exit 4)")
        if name == "run":
            p.add_argument("--probes", required=True)
            p.add_argument("--arms", default="M,C")
        p.set_defaults(fn=fn)
    for name, fn in (("rejudge", cmd_rejudge), ("select", cmd_select), ("report", cmd_report)):
        p = sub.add_parser(name)
        p.add_argument("--out", required=True)
        p.set_defaults(fn=fn)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
