"""Sprint 26, work item 14: the verification runs on the real plugin. The standard is review/verify-criteria.md (committed before any run).

Arms: B = the plugin before Sprint 26 (plugin tree of 432807e, equal to main's), C = the plugin at HEAD.
Groups: roles (C, 5 entries x 3), sub (C, the subagent probe), model (C, the model calls a role itself),
        trig (B and C, six questions on the direct path, two on the role-command path, x 3),
        s24 (B and C, the Sprint 24 "read in full before drafting" prompts G1 G2 D1 R1 x 3, and G1's correction).

    python -X utf8 -I scripts/verify_test.py selftest
    python -X utf8 -I scripts/verify_test.py build --out DIR                      build both plugin copies and the fixtures
    python -X utf8 -I scripts/verify_test.py run --out DIR --group roles [--arm B,C] [--n 3] [--parallel 2] [--max-seconds 540] [--skip-done] [--only TAG,...]
    python -X utf8 -I scripts/verify_test.py report --out DIR                      the tables, from the evidence files

Raw output goes to --out, outside the repository. Sessions are claude-magpie stream-json sessions with a throwaway home and a
whitelist environment (the helpers of scripts/stranger_test/driver.py); evidence is read from the event stream, never from what
the model says about itself. Memory rule (PO 2026-11-23): no start line and no one-at-a-time requirement; the one thing kept is
a watchdog that stops the running sessions when free memory falls under --watchdog-mb (a session it stops is a technical failure,
rerun once); nothing here changes an environment variable to dodge the system's memory reaping or detaches a process.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import difflib
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
import carrier_test as ct  # noqa: E402  (read_stream, text_of, free_mb, Gate, TOOLS, LIMITS, MODEL)
import driver  # noqa: E402  (make_env, magpie_prefix, Session, neutral_parent, rmtree)

BASE_REV = "432807e"
ARM_REVS = {"B": BASE_REV, "C": "HEAD"}
FIXTURE_REV = "00c224b"  # the templates the Sprint 24 fixtures were made from
S24_FIXTURES = REPO / "scrum" / "documents" / "sprint" / "sprint-24-loading-reliability-validation" / "fixtures"
MEM_START = "# IDEO-Scrum Memory"
MEM_END = "**departures**"
TOOLS_NO_AGENT = ct.TOOLS_NO_AGENT
TOOLS_AGENT = ct.TOOLS
LIMITS = ct.LIMITS
MODEL = ct.MODEL
DRAFT_MIN = 300  # characters: the first assistant text this long after the prompt is the first draft
WATCHDOG_MB = 1200  # the default of --watchdog-mb; 2,000 MB (the carrier test's line) stopped every run once another session was testing DSH

ENTRY_ORDER = {
    "developer": ["ideo-kernel", "scrum-kernel", "sprint-kernel", "memory"],
    "scrum-master": ["ideo-kernel", "scrum-kernel", "sprint-kernel", "design-kernel", "memory"],
    "designer": ["ideo-kernel", "scrum-kernel", "design-kernel", "memory"],
    "stakeholder": ["ideo-kernel", "scrum-kernel", "memory"],
    "supporter": ["ideo-kernel", "scrum-kernel", "memory"],
}

# ---- the Sprint 24 prompts (verbatim from the Sprint 24 host trials) and the Sprint 17 flow questions ---------------
S24_PROMPTS = {
    "G1": "我就是产品负责人。小馆已经能查借到什么书；每周都有读者因为不清楚到期日或续借结果白跑柜台，也有读者只能在闭馆后处理。下一周能做一条短信提醒。产品日志 1.2 还空着，给我拟一个 Product Goal，先在对话里给首稿。",
    "G2": "可以启动这个冲刺的 Planning，先只做 Why。现状是读者知道哪天到期，但还看不出能不能续、有没有续上；柜台最近收到了这些求助。手上的想法是短信提醒、续借入口和回执。结合产品日志，给我拟一条本期 Sprint Goal，先在对话里说。",
    "D1": "准许做这个设计冲刺的共情，暂不进定义。我是来续借的读者：上周五 19 点我赶到柜台，门已经关了；手机上点了两次续借，只看到『处理中』，我第二天又跑了一趟。馆长说旧的线上入口下月要关。基于这些材料，先在对话里拟设计挑战、设计目标和设计问题。",
    "R1": "这个冲刺已进入 What，先用 HMW 精化 PBI-001：『作为读者，我想在续借被拒时知道接下来还能怎么办，以便在到期前作决定。』甲说想马上知道能否借到另一本，乙只想知道必须何时归还。先在对话里给精化草案，不进 How。",
    "G1_FIX": "上一稿不合方法论，我要的是 Product Goal。请重拟。",
}
S24_FIXTURE = {"G1": "g1", "G2": "g2", "D1": "g2", "R1": "r1"}  # D1 uses G2's fixture
S24_ENTRY = "/ideo-scrum:scrum-master"

# the flow questions of Sprint 17 (scrum/sprint-17-conventions-rewrite/test-questions.md, commit 86b0af5), the ones that tell the kernels apart
TRIG_Q = {
    "Q2": "Sprint 里精化做到一半，碰到一个问题：这个读书笔记工具的用户到底是谁，对他们来说怎样才算好用，我们自己说不清，手上的资料里也没有现成的答案。这时候该怎么办？这个 Sprint 接下来怎么走？",
    "Q3": "我有个想法：给一家社区图书馆做一个帮读者找书的工具。现在手上只有这一句话，没有产品日志，也不知道读者具体要什么。我想把这件事正式做起来，第一步该做什么？",
    "Q4": "设计走到构思这一步了：挑战、设计目标、设计问题和地图都写进日志了，PO 也选出了要解决的那个问题。接下来怎么得到方案？谁来做，各自怎么做，最后怎么选？",
    "Q9": "聊天里冒出一个问题：这个工具的通知该不该做成可关闭的？我们说不清用户会怎么想，也没有现成的答案。PO 没说用哪种方法。你打算怎么定？",
    "Q10": "PO 说这个问题就用 IDEO 五阶段法跑一遍，弄清「新用户第一次打开这个工具会卡在哪」，并留下记录。你打算怎么跑、记在哪里？",
    "Q11": "设计开始了，要写设计目标和地图。设计目标该怎么写？地图画到什么程度？",
}
# acceptable kernels, and the old convention file names that count as "read the rules" in arm B (Sprint 17: Read, or a Grep that reaches the file)
TRIG_EXPECT = {
    "Q2": {"kernels": ["sprint-kernel", "ideo-kernel", "design-kernel"], "old": ["sprint-log.md", "ideo-log.md", "design-log.md"]},
    "Q3": {"kernels": ["scrum-kernel", "design-kernel"], "old": ["product-log.md", "overview.md", "design-log.md"]},
    "Q4": {"kernels": ["design-kernel"], "old": ["design-log.md"]},
    "Q9": {"kernels": ["ideo-kernel"], "old": ["ideo-log.md"]},
    "Q10": {"kernels": ["ideo-kernel"], "old": ["ideo-log.md"]},
    "Q11": {"kernels": ["design-kernel"], "old": ["design-log.md"]},
}
TRIG_DIRECT = ["Q2", "Q3", "Q4", "Q9", "Q10", "Q11"]
TRIG_COMMAND = ["Q2", "Q3"]  # also through /ideo-scrum:scrum-master <question>

SUB_MESSAGES = [
    "/ideo-scrum:developer",
    "Use the Agent tool to start one general-purpose subagent. Give it exactly this task and nothing else, no rules and no background: "
    "\"Suggest a folder name for a new Sprint about a login-page redesign. Reply with just the folder name.\" Then tell me what the subagent answered.",
]
MODEL_MESSAGES = ["Please call the Skill tool now with the skill `ideo-scrum:developer`, then reply with the single word ready."]


# ---- required reads (the plugin's own "Before drafting" paragraphs, arm by arm) -----------------------------------
def F(path: str, section: tuple | None = None) -> dict:
    return {"kind": "file", "path": path, "section": section}


def SK(skill: str) -> dict:
    return {"kind": "skill", "skill": skill}


def PJ(path: str, section: tuple) -> dict:
    return {"kind": "project", "path": path, "section": section}


SEC_PRODUCT_12 = (r"^### 1\.2 ", r"^#{2,3} ")  # product template §1.2 up to the next heading
SEC_SPRINT_11_12 = (r"^### 1\.1 ", r"^## 2\. ")
SEC_SPRINT_22 = (r"^### 2\.2 ", r"^## 3\. ")
SEC_DESIGN_1 = (r"^## 1\. ", r"^## 2\. ")  # §1 and §§1.1-1.3
SEC_LOG_12 = (r"^### 1\.2 ", r"^### 1\.3 ")  # the project's own product log, §1.2
REF_PB = "skills/scrum-kernel/references/scrum-artifact-product-backlog.md"
REF_SB = "skills/scrum-kernel/references/scrum-artifact-sprint-backlog.md"
PLANNING = "skills/sprint-kernel/events/scrum-event-sprint-planning.md"
STEPS = ["skills/design-kernel/steps/1-1-define-the-challenge.md", "skills/design-kernel/steps/1-2-start-at-the-end.md",
         "skills/design-kernel/steps/1-3-ask-the-experts.md"]
EMPATHIZE = "skills/ideo-kernel/IDEO-modes/empathize.md"
DEFINE = "skills/ideo-kernel/IDEO-modes/define.md"
HMW = "skills/ideo-kernel/methods/how-might-we-questions.md"
D = "skills/memory/details/"
REQUIRED = {
    "B": {
        "G1": [F("skills/scrum-kernel/overview.md"), F(REF_PB), F("skills/scrum-kernel/conventions/product-log.md"), F("template/product-backlog-template.md", SEC_PRODUCT_12)],
        "G2": [F("skills/scrum-kernel/overview.md"), F("skills/sprint-kernel/conventions/sprint-log.md"), F(PLANNING), F(REF_SB),
               F("template/sprint-backlog-template.md", SEC_SPRINT_11_12), PJ("scrum/ProductBacklog.md", SEC_LOG_12)],
        "D1": [*[F(s) for s in STEPS], F(EMPATHIZE), F("skills/scrum-kernel/overview.md"), F("skills/ideo-kernel/conventions/ideo-log.md"),
               F("skills/design-kernel/conventions/design-log.md"), F("template/design-backlog-template.md", SEC_DESIGN_1)],
        "R1": [F("skills/scrum-kernel/overview.md"), F("skills/sprint-kernel/conventions/sprint-log.md"), F(PLANNING), F(REF_PB),
               F("skills/scrum-kernel/conventions/product-log.md"), F(DEFINE), F(HMW), F("template/sprint-backlog-template.md", SEC_SPRINT_22)],
    },
    "C": {
        "G1": [SK("ideo-scrum:memory"), F(D + "goal-fixed.md"), F(D + "product-log.md"), F(REF_PB), F("template/product-backlog-template.md", SEC_PRODUCT_12)],
        "G2": [SK("ideo-scrum:memory"), F(D + "sprint.md"), F(D + "goal-fixed.md"), F(D + "gates.md"), F(D + "refinement.md"), F(PLANNING), F(REF_SB),
               F("template/sprint-backlog-template.md", SEC_SPRINT_11_12), PJ("scrum/ProductBacklog.md", SEC_LOG_12)],
        "D1": [SK("ideo-scrum:memory"), F(D + "design.md"), F(D + "gates.md"), F(D + "roles.md"), *[F(s) for s in STEPS], F(EMPATHIZE),
               F("template/design-backlog-template.md", SEC_DESIGN_1)],
        "R1": [SK("ideo-scrum:memory"), F(D + "sprint.md"), F(D + "goal-fixed.md"), F(D + "gates.md"), F(D + "refinement.md"), F(PLANNING), F(REF_PB),
               F(D + "product-log.md"), F(DEFINE), F(HMW), F("template/sprint-backlog-template.md", SEC_SPRINT_22)],
    },
}


# ---- reading a stream -----------------------------------------------------------------------------------------------
def parse_stream(path: pathlib.Path) -> dict:
    """The calls in event order (with their results and, for a Skill, the body that follows), the assistant texts, the result events.
    parent is the id of the Agent call a call was made under (None for the top level)."""
    rows = ct.read_stream(path)
    calls, texts, results = [], [], []
    by_id: dict[str, dict] = {}
    last_skill = None
    init = None
    for i, r in enumerate(rows):
        t = r.get("type")
        if t == "system" and r.get("subtype") == "init":
            init = {"permissionMode": r.get("permissionMode"), "tools": r.get("tools"), "model_set": bool(r.get("model"))}
        if t == "assistant":
            parent = r.get("parent_tool_use_id")
            for b in (r.get("message") or {}).get("content") or []:
                if not isinstance(b, dict):
                    continue
                if b.get("type") == "tool_use":
                    c = {"id": b.get("id"), "name": b.get("name"), "input": b.get("input") or {}, "i": i, "parent": parent,
                         "ok": None, "text": "", "ri": None, "body": ""}
                    calls.append(c)
                    by_id[c["id"]] = c
                elif b.get("type") == "text" and (b.get("text") or "").strip():
                    texts.append({"i": i, "parent": parent, "text": b["text"]})
        elif t == "user":
            content = (r.get("message") or {}).get("content")
            blocks = content if isinstance(content, list) else ([{"type": "text", "text": content}] if isinstance(content, str) else [])
            for b in blocks:
                if not isinstance(b, dict):
                    continue
                if b.get("type") == "tool_result":
                    c = by_id.get(b.get("tool_use_id"))
                    if c is not None:
                        c["ok"] = not b.get("is_error")
                        c["text"] = ct.text_of(b.get("content"))
                        c["ri"] = i
                        if c["name"] == "Skill":
                            last_skill = c
                elif b.get("type") == "text":
                    tx = b.get("text") or ""
                    if tx.startswith("Base directory for this skill") and last_skill is not None and not last_skill["body"]:
                        last_skill["body"] = tx
        elif t == "result":
            results.append({"i": i, "text": r.get("result") or "", "is_error": bool(r.get("is_error")), "subtype": r.get("subtype"),
                            "denials": len(r.get("permission_denials") or [])})
    return {"calls": calls, "texts": texts, "results": results, "n": len(rows), "init": init}


def skill_of(c: dict) -> str | None:
    return (c["input"] or {}).get("skill") if c["name"] == "Skill" else None


def memory_body_ok(c: dict | None, canaries: tuple = (MEM_START, MEM_END)) -> bool:
    return bool(c and c["ok"] and canaries[0] in c["body"] and canaries[1] in c["body"])


def top_level(p: dict) -> list:
    return [c for c in p["calls"] if c["parent"] is None]


# ---- the judges ----------------------------------------------------------------------------------------------------
def judge_roles(p: dict, entry: str, canaries: tuple = (MEM_START, MEM_END)) -> dict:
    """Entry criterion: the first calls are exactly the entry's Skill calls in its order, each succeeded, the Memory's text arrived
    (start and end markers in its body), and no other tool came before the Memory call."""
    exp = [f"ideo-scrum:{k}" for k in ENTRY_ORDER[entry]]
    top = top_level(p)
    first = top[: len(exp)]
    order_ok = len(first) == len(exp) and all(c["name"] == "Skill" and skill_of(c) == e and c["ok"] for c, e in zip(first, exp))
    mem = next((c for c in top if skill_of(c) == "ideo-scrum:memory"), None)
    body = memory_body_ok(mem, canaries)
    mem_pos = top.index(mem) if mem else None
    others_before = [f"{c['name']}:{skill_of(c) or ''}" for c in (top[:mem_pos] if mem_pos is not None else top) if c["name"] != "Skill"]
    ok = order_ok and body and not others_before
    return {"pass": ok, "order_ok": order_ok, "memory_body": body, "memory_chars": len(mem["body"]) if mem else 0,
            "other_tools_before_memory": others_before, "seen": [f"{c['name']}:{skill_of(c) or ''}:{'ok' if c['ok'] else 'ERR'}" for c in top[:8]], "expected": exp}


def judge_sub(p: dict, canaries: tuple = (MEM_START, MEM_END)) -> dict:
    ag = next((c for c in p["calls"] if c["name"] in ("Agent", "Task")), None)
    if ag is None:
        return {"agent": False, "memory_loaded": False}
    sub = [c for c in p["calls"] if c["parent"] == ag["id"]]
    mem = next((c for c in sub if skill_of(c) == "ideo-scrum:memory"), None)
    return {"agent": True, "memory_loaded": memory_body_ok(mem, canaries), "delegation_prompt": (ag["input"] or {}).get("prompt"),
            "sub_calls": [f"{c['name']}:{skill_of(c) or (c['input'] or {}).get('file_path') or ''}" for c in sub][:12],
            "sub_skills": [skill_of(c) for c in sub if c["name"] == "Skill"], "answer": (ag["text"] or "")[:300]}


def judge_model(p: dict, role: str = "developer", canaries: tuple = (MEM_START, MEM_END)) -> dict:
    top = top_level(p)
    first = top[0] if top else None
    called = bool(first and first["name"] == "Skill" and skill_of(first) == f"ideo-scrum:{role}" and first["ok"])
    mem = next((c for c in top if skill_of(c) == "ideo-scrum:memory"), None)
    final = p["results"][-1]["i"] if p["results"] else None
    return {"role_called": called, "skills": [skill_of(c) for c in top if c["name"] == "Skill"], "memory_loaded": memory_body_ok(mem, canaries),
            "memory_before_reply": bool(mem and final is not None and mem["ri"] is not None and mem["ri"] < final)}


def judge_trig(p: dict, q: str, arm: str, path: str, canaries: tuple = (MEM_START, MEM_END)) -> dict:
    """Behavior only (Sprint 18's way): was an acceptable kernel loaded, and were the rules read. Arm B reads the old convention file (a Read,
    or a Grep that reaches it); arm C has the Memory's text in the context (its Skill body) or reads a file of its details/."""
    exp = TRIG_EXPECT[q]
    top = top_level(p)
    skills = [skill_of(c) for c in top if c["name"] == "Skill" and c["ok"]]
    kernel = any(f"ideo-scrum:{k}" in skills for k in exp["kernels"])
    if arm == "B":
        rules = any(c["ok"] and ((c["name"] == "Read" and any((c["input"].get("file_path") or "").replace("\\", "/").endswith("/" + f) for f in exp["old"]))
                                 or (c["name"] == "Grep" and any(f in json.dumps(c["input"]) or f in (c["text"] or "") for f in exp["old"])))
                    for c in top)
    else:
        mem = next((c for c in top if skill_of(c) == "ideo-scrum:memory"), None)
        rules = memory_body_ok(mem, canaries) or any(c["name"] == "Read" and c["ok"] and "/skills/memory/" in (c["input"].get("file_path") or "").replace("\\", "/") for c in top)
    return {"pass": kernel and rules, "kernel": kernel, "rules": rules, "skills": skills, "path": path}


# ---- the "read in full before drafting" judge ----------------------------------------------------------------------
def line_numbers(text: str) -> set:
    """The line numbers a Read result shows ("12<tab>text")."""
    return {int(m.group(1)) for m in re.finditer(r"^\s*(\d+)[\t\u2192]", text or "", re.M)}


def section_lines(text: str, section: tuple | None) -> set:
    lines = text.replace("\r\n", "\n").split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    if section is None:
        return set(range(1, len(lines) + 1))
    start_re, end_re = (re.compile(x) for x in section)
    start = next((n for n, l in enumerate(lines, 1) if start_re.search(l)), None)
    if start is None:
        raise ValueError(f"no heading {section[0]!r}")
    end = next((n - 1 for n, l in enumerate(lines, 1) if n > start and end_re.search(l)), len(lines))
    return set(range(start, end + 1))


def rel_of(path: str) -> tuple[str, str]:
    p = (path or "").replace("\\", "/")
    if "/ideo-scrum/" in p:
        return "plugin", p.split("/ideo-scrum/", 1)[1]
    if "/plugin/" in p:  # Sprint 24's plugin copies were folders called plugin
        return "plugin", p.split("/plugin/", 1)[1]
    if "/project/" in p:
        return "project", p.rsplit("/project/", 1)[1]
    return "other", p


def draft_index(p: dict) -> int | None:
    """The event index of the first draft: in the second turn (the prompt after the entry), the first assistant text of DRAFT_MIN
    characters or more at the top level; else the result event that ends the turn."""
    if len(p["results"]) < 2:
        return None
    lo, hi = p["results"][0]["i"], p["results"][1]["i"]
    for t in p["texts"]:
        if t["parent"] is None and lo < t["i"] < hi and len(t["text"]) >= DRAFT_MIN:
            return t["i"]
    return hi


def judge_a(p: dict, required: list, file_text, canaries: tuple = (MEM_START, MEM_END), template_by_name: bool = False) -> dict:
    """Did every required text arrive in full before the first draft. file_text(kind, rel) gives the text of a required file of this arm
    (the plugin's, or the fixture project's). Coverage is by the line numbers of the successful Reads, accumulated over ranges; a Skill
    call counts only with the body (the Memory's start and end markers in it)."""
    d = draft_index(p)
    if d is None:
        return {"pass": False, "draft_i": None, "missing": ["no second turn"], "items": []}
    items = []
    for req in required:
        if req["kind"] == "skill":
            c = next((c for c in top_level(p) if skill_of(c) == req["skill"] and c["ok"] and c["ri"] is not None and c["ri"] < d), None)
            ok = bool(c) and (req["skill"] != "ideo-scrum:memory" or memory_body_ok(c, canaries))
            items.append({"item": req["skill"], "ok": ok})
            continue
        kind = "project" if req["kind"] == "project" else "plugin"
        need = section_lines(file_text(kind, req["path"]), req["section"])
        got: set = set()
        for c in p["calls"]:
            if c["name"] != "Read" or not c["ok"] or c["ri"] is None or c["ri"] >= d:
                continue
            k, rel = rel_of((c["input"] or {}).get("file_path") or "")
            same = rel == req["path"] or (template_by_name and req["path"].startswith("template/") and rel.split("/")[-1] == req["path"].split("/")[-1])
            if k == kind and same:
                got |= line_numbers(c["text"])
        missing = sorted(need - got)
        items.append({"item": req["path"] + ("" if req["section"] is None else " [section]"), "ok": not missing, "missing_lines": len(missing)})
    return {"pass": all(i["ok"] for i in items), "draft_i": d, "missing": [i["item"] for i in items if not i["ok"]], "items": items}


def judge_fix(p: dict) -> dict:
    """G1's correction (Sprint 24's way): between the correction and the redraft, the text of `Commitment: Product Goal` arrived again."""
    if len(p["results"]) < 3:
        return {"reread": False, "note": "no third turn"}
    lo, hi = p["results"][1]["i"], p["results"][2]["i"]
    d2 = next((t["i"] for t in p["texts"] if t["parent"] is None and lo < t["i"] < hi and len(t["text"]) >= DRAFT_MIN), hi)
    got = [c for c in top_level(p) if c["ok"] and c["ri"] is not None and lo < c["ri"] < d2 and "Commitment: Product Goal" in (c["text"] or c["body"])]
    return {"reread": bool(got), "by": [f"{c['name']}:{(c['input'] or {}).get('file_path') or skill_of(c) or ''}" for c in got][:3]}


# ---- the plugin copies and the fixtures -----------------------------------------------------------------------------
def git(*args: str) -> bytes:
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, check=True).stdout


def build_arm(out: pathlib.Path, arm: str) -> dict:
    rev = ARM_REVS[arm]
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
        except TypeError:  # Python before 3.12 has no filter argument
            tar.extractall(dest, members=members)
    return {"arm": arm, "rev": rev, "commit": commit, "plugin_tree": tree, "path": str(dest / "ideo-scrum")}


def apply_fills(base_tpl: str, fixture: str, new_tpl: str) -> str:
    """The fixture is the old template with a few fills; make the same fills in the new template (each anchored on a unique line)."""
    base, fix, new = (x.replace("\r\n", "\n").split("\n") for x in (base_tpl, fixture, new_tpl))
    out = list(new)
    for tag, i1, i2, j1, j2 in reversed(difflib.SequenceMatcher(None, base, fix, autojunk=False).get_opcodes()):
        if tag == "equal":
            continue
        if tag == "replace" and (i2 - i1) == (j2 - j1):
            for k in range(i2 - i1):
                hits = [n for n, l in enumerate(out) if l == base[i1 + k]]
                if not hits:  # the placeholder line was reworded since: its first eight characters (e.g. "> Now: <") still anchor it
                    hits = [n for n, l in enumerate(out) if l.startswith(base[i1 + k][:8])]
                if len(hits) != 1:
                    raise ValueError(f"fill anchor {base[i1 + k]!r} found {len(hits)} times in the new template")
                out[hits[0]] = fix[j1 + k]
        elif tag == "insert":
            hits = [n for n, l in enumerate(out) if l == base[i1 - 1]]
            if len(hits) != 1:
                raise ValueError(f"insert anchor {base[i1 - 1]!r} found {len(hits)} times in the new template")
            out[hits[0] + 1:hits[0] + 1] = fix[j1:j2]
        else:
            raise ValueError(f"unexpected edit {tag} in a fixture")
    return "\n".join(out)


def build_fixtures(out: pathlib.Path) -> None:
    """Arm B: the Sprint 24 fixtures as they are (the old templates' wording). Arm C: the same fills in the current templates."""
    tpl = {"ProductBacklog.md": ("skills/scrum-kernel/conventions/product-backlog-template.md", "template/product-backlog-template.md"),
           "SprintBacklog.md": ("skills/sprint-kernel/conventions/sprint-backlog-template.md", "template/sprint-backlog-template.md")}
    for arm in ("B", "C"):
        dest = out / "fixtures" / arm
        if dest.exists():
            driver.rmtree(dest)
        for src in S24_FIXTURES.rglob("*.md"):
            rel = src.relative_to(S24_FIXTURES)
            target = dest / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            text = src.read_text(encoding="utf-8")
            if arm == "C":
                old_path, new_path = tpl[src.name]
                base = git("show", f"{FIXTURE_REV}:plugins/ideo-scrum/{old_path}").decode("utf-8")
                new = (out / "plugins" / "C" / "ideo-scrum" / new_path).read_text(encoding="utf-8")
                text = apply_fills(base, text, new)
            target.write_text(text, encoding="utf-8", newline="\n")


# ---- trials ----------------------------------------------------------------------------------------------------------
def trial_list(group: str, arms: list[str], n: int) -> list[dict]:
    t = []
    if group == "roles":
        for entry in ENTRY_ORDER:
            for k in range(1, n + 1):
                t.append({"group": "roles", "arm": "C", "key": entry, "n": k, "messages": [f"/ideo-scrum:{entry}"], "tools": TOOLS_NO_AGENT, "fixture": None})
    elif group == "sub":
        for k in range(1, n + 1):
            t.append({"group": "sub", "arm": "C", "key": "developer", "n": k, "messages": SUB_MESSAGES, "tools": TOOLS_AGENT, "fixture": None})
    elif group == "model":
        for k in range(1, n + 1):
            t.append({"group": "model", "arm": "C", "key": "developer", "n": k, "messages": MODEL_MESSAGES, "tools": TOOLS_NO_AGENT, "fixture": None})
    elif group == "trig":
        for arm in arms:
            for path, qs in (("direct", TRIG_DIRECT), ("command", TRIG_COMMAND)):
                for q in qs:
                    for k in range(1, n + 1):
                        msg = TRIG_Q[q] if path == "direct" else f"/ideo-scrum:scrum-master {TRIG_Q[q]}"
                        t.append({"group": "trig", "arm": arm, "key": f"{q}-{path}", "n": k, "messages": [msg], "tools": TOOLS_NO_AGENT, "fixture": None})
    elif group == "s24":
        for arm in arms:
            for key in ("G1", "G2", "D1", "R1"):
                for k in range(1, n + 1):
                    msgs = [S24_ENTRY, S24_PROMPTS[key]] + ([S24_PROMPTS["G1_FIX"]] if key == "G1" else [])
                    t.append({"group": "s24", "arm": arm, "key": key, "n": k, "messages": msgs, "tools": TOOLS_NO_AGENT, "fixture": S24_FIXTURE[key]})
    else:
        sys.exit(f"unknown group {group}")
    for x in t:
        x["tag"] = f"{x['group']}-{x['arm']}-{x['key']}-{x['n']}"
    return t


ACTIVE: dict[str, "driver.Session"] = {}
ACTIVE_LOCK = threading.Lock()
WATCHDOG = {"tripped": False, "free_mb": None, "tags": []}


def judge_trial(trial: dict, out: pathlib.Path, stream: pathlib.Path) -> dict:
    p = parse_stream(stream)
    g, arm, key = trial["group"], trial["arm"], trial["key"]
    ev = {"calls": len(p["calls"]), "results": len(p["results"]), "init": p["init"], "denials": sum(r["denials"] for r in p["results"])}
    if g == "roles":
        ev["judge"] = judge_roles(p, key)
    elif g == "sub":
        ev["judge"] = judge_sub(p)
    elif g == "model":
        ev["judge"] = judge_model(p)
    elif g == "trig":
        q, path = key.split("-")
        ev["judge"] = judge_trig(p, q, arm, path)
    elif g == "s24":
        plugin = out / "plugins" / arm / "ideo-scrum"
        fx = out / "fixtures" / arm / trial["fixture"] / "scrum"

        def file_text(kind: str, rel: str) -> str:
            base = plugin if kind == "plugin" else fx.parent
            return (base / rel).read_text(encoding="utf-8")

        ev["judge"] = judge_a(p, REQUIRED[arm][key], file_text)
        if key == "G1":
            ev["fix"] = judge_fix(p)
        ev["turn_texts"] = [r["text"] for r in p["results"]]  # the drafts, for the content reading
    return ev


def run_trial(out: pathlib.Path, trial: dict, attempt: int = 1) -> dict:
    tag = trial["tag"]
    d = out / "trials" / tag
    if d.exists():  # a rerun starts clean; the earlier attempt is kept as .attemptK, counted as a technical failure
        k = 1
        while (out / "trials" / f"{tag}.attempt-{k}").exists():
            k += 1
        shutil.move(str(d), str(out / "trials" / f"{tag}.attempt-{k}"))
    d.mkdir(parents=True)
    root = pathlib.Path(tempfile.mkdtemp(prefix="s26v-", dir=driver.neutral_parent()))
    t0 = time.time()
    status = "ok"
    try:
        env, _home = driver.make_env(root / "env")
        proj = root / "project"
        proj.mkdir()
        if trial["fixture"]:
            shutil.copytree(out / "fixtures" / trial["arm"] / trial["fixture"] / "scrum", proj / "scrum")
        tools = trial["tools"]
        cmd = driver.magpie_prefix() + ["-p", "--input-format", "stream-json", "--output-format", "stream-json", "--verbose",
                                        "--include-hook-events", "--model", MODEL, "--tools", tools, "--allowedTools", tools,
                                        "--disallowedTools", "Bash,PowerShell,Write,Edit,NotebookEdit",
                                        "--permission-mode", "dontAsk", "--strict-mcp-config",
                                        "--setting-sources", "project,local", "--plugin-dir", str(out / "plugins" / trial["arm"] / "ideo-scrum")]
        s = driver.Session(tag, cmd, proj, env, d / "stream.jsonl")
        with ACTIVE_LOCK:
            ACTIVE[tag] = s
        s.start()
        for m in trial["messages"]:
            r = s.send(m, LIMITS["message_s"])
            if r["status"] != "ok":
                status = r["status"]
                break
        s.close()
    except Exception as e:  # a harness failure is a technical failure of the trial, recorded
        status = f"harness-error: {e}"
    finally:
        with ACTIVE_LOCK:
            ACTIVE.pop(tag, None)
        driver.rmtree(root)
    if WATCHDOG["tripped"] and status != "ok":
        status = "watchdog"
    ev = judge_trial(trial, out, d / "stream.jsonl") if (d / "stream.jsonl").exists() else {}
    res = {"tag": tag, "group": trial["group"], "arm": trial["arm"], "key": trial["key"], "n": trial["n"], "status": status,
           "attempt": attempt, "seconds": round(time.time() - t0, 1), "evidence": ev}
    (d / "evidence.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return res


def watchdog_loop(stop: threading.Event, threshold_mb: int) -> None:
    low = 0
    while not stop.wait(5.0):
        try:
            f = ct.free_mb()
        except Exception:
            continue
        low = low + 1 if f < threshold_mb else 0
        if low >= 2 and not WATCHDOG["tripped"]:
            WATCHDOG.update(tripped=True, free_mb=f)
            with ACTIVE_LOCK:
                WATCHDOG["tags"] = list(ACTIVE)
                for s in list(ACTIVE.values()):
                    driver.kill_tree(s.proc)
            print(f"[watchdog] free {f} MB under {threshold_mb} MB twice: the running sessions were stopped: {WATCHDOG['tags']}", flush=True)


def attempts_of(out: pathlib.Path, tag: str) -> int:
    return 1 + len(list((out / "trials").glob(f"{tag}.attempt-*")))


def cmd_build(a) -> int:
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    arms = {arm: build_arm(out, arm) for arm in ARM_REVS}
    build_fixtures(out)
    (out / "arms.json").write_text(json.dumps(arms, indent=1), encoding="utf-8")
    for arm, info in arms.items():
        print(arm, info["rev"], info["commit"][:10], "plugin tree", info["plugin_tree"][:10])
    return 0


def cmd_run(a) -> int:
    out = pathlib.Path(a.out)
    arms = a.arm.split(",")
    trials = trial_list(a.group, arms, a.n)
    if a.only:
        want = set(a.only.split(","))
        trials = [t for t in trials if t["tag"] in want]
    done, todo = 0, []
    for t in trials:
        ev = out / "trials" / t["tag"] / "evidence.json"
        status = None
        if ev.exists():
            try:
                status = json.loads(ev.read_text(encoding="utf-8")).get("status")
            except ValueError:
                status = None
        if status == "ok" and a.skip_done:
            done += 1
        elif status is not None and status != "ok" and attempts_of(out, t["tag"]) > a.retry_limit:
            print(f"[stop] {t['tag']} was stopped again after its one rerun ({status}); not run again, report it")
            continue
        else:
            todo.append(t)
    print(f"{len(trials)} trials in the group, {done} already have valid evidence, {len(todo)} to run (parallel {a.parallel})")
    gate = ct.Gate(a.soft_free_mb) if a.soft_free_mb else None
    deadline = time.time() + a.max_seconds if a.max_seconds else None
    left: list[str] = []
    stop = threading.Event()
    threading.Thread(target=watchdog_loop, args=(stop, a.watchdog_mb), daemon=True).start()

    def one(t):
        if deadline and time.time() > deadline:
            left.append(t["tag"])
            return {"tag": t["tag"], "status": "not started (time box)", "seconds": 0}
        if WATCHDOG["tripped"]:
            left.append(t["tag"])
            return {"tag": t["tag"], "status": "not started (watchdog)", "seconds": 0}
        if gate:
            gate.enter()
        try:
            if deadline and time.time() > deadline:
                left.append(t["tag"])
                return {"tag": t["tag"], "status": "not started (time box)", "seconds": 0}
            return run_trial(out, t, attempts_of(out, t["tag"]))
        finally:
            if gate:
                gate.leave()

    with concurrent.futures.ThreadPoolExecutor(max_workers=a.parallel) as ex:
        for res in ex.map(one, todo):
            j = (res.get("evidence") or {}).get("judge") or {}
            print(res["tag"], res["status"], res["seconds"], "pass=" + str(j.get("pass")) if "pass" in j else "")
    stop.set()
    if WATCHDOG["tripped"]:
        print(f"[watchdog] tripped at {WATCHDOG['free_mb']} MB; stopped: {WATCHDOG['tags']}; the rest of the batch was not started")
        return 5
    if left:
        print(f"[box] time box reached: {len(left)} trials not started, for the next call")
        return 4
    return 0


def cmd_report(a) -> int:
    out = pathlib.Path(a.out)
    rows = []
    for f in sorted((out / "trials").glob("*/evidence.json")):
        if ".attempt-" in f.parent.name:
            continue
        rows.append(json.loads(f.read_text(encoding="utf-8")))
    groups: dict = {}
    for r in rows:
        j = (r.get("evidence") or {}).get("judge") or {}
        groups.setdefault((r["group"], r["arm"], r["key"]), []).append((r["status"], j))
    lines = ["| group | arm | key | valid | pass | notes |", "| --- | --- | --- | --- | --- | --- |"]
    for (g, arm, key), v in sorted(groups.items()):
        valid = [j for s, j in v if s == "ok"]
        if g in ("sub", "model"):
            n = sum(1 for j in valid if j.get("memory_loaded"))
        else:
            n = sum(1 for j in valid if j.get("pass"))
        bad = [s for s, _ in v if s != "ok"]
        lines.append(f"| {g} | {arm} | {key} | {len(valid)}/{len(v)} | {n}/{len(valid)} | {', '.join(bad) if bad else ''} |")
    text = "\n".join(lines)
    (out / "report.md").write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


# ---- the self-test: known results ----------------------------------------------------------------------------------
def cmd_selftest(a) -> int:
    ok = True

    def check(cond: bool, what: str) -> None:
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    # 1. the section and line machinery
    text = "# T\n\n## 1. Why\n\n### 1.1 Goal\nx\ny\n\n### 1.2 DoD\nz\n\n## 2. What\nw\n"
    check(section_lines(text, SEC_SPRINT_11_12) == set(range(5, 12)), "a section runs from its heading to the line before the next ## heading")
    check(section_lines(text, None) == set(range(1, 14)), "no section means every line")
    check(line_numbers("     1\ta\n    22\tb\n\n  3\u2192c") == {1, 22, 3}, "the line numbers of a Read result, tab or arrow")

    # 2. synthetic streams: a role entry that loads in order, one that skips the Memory, one that reads before it
    def stream(events: list) -> pathlib.Path:
        f = pathlib.Path(tempfile.mkdtemp(prefix="vt-")) / "s.jsonl"
        f.write_text("\n".join(json.dumps(e, ensure_ascii=False) for e in events) + "\n", encoding="utf-8")
        return f

    def use(i, name, inp):
        return {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": f"t{i}", "name": name, "input": inp}]}}

    def res(i, text="", err=False):
        return {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": f"t{i}", "content": text, "is_error": err}]}}

    def body(text):
        return {"type": "user", "isSynthetic": True, "message": {"content": [{"type": "text", "text": "Base directory for this skill: x\n\n" + text}]}}

    def skill_events(i, name, text):
        return [use(i, "Skill", {"skill": f"ideo-scrum:{name}"}), res(i, f"Launching skill: ideo-scrum:{name}"), body(text)]

    mem_text = f"{MEM_START}\nlines\n- {MEM_END} end"
    good = sum((skill_events(i, k, mem_text if k == "memory" else "k") for i, k in enumerate(ENTRY_ORDER["developer"], 1)), []) + [{"type": "result", "result": "done"}]
    check(judge_roles(parse_stream(stream(good)), "developer")["pass"], "roles: the right Skill calls in order, the Memory's text arrived")
    r = judge_roles(parse_stream(stream(skill_events(1, "ideo-kernel", "k") + skill_events(2, "scrum-kernel", "k") + skill_events(3, "sprint-kernel", "k") + [{"type": "result", "result": "d"}])), "developer")
    check(not r["pass"] and not r["order_ok"], "roles: no Memory call fails")
    r = judge_roles(parse_stream(stream(skill_events(1, "ideo-kernel", "k") + skill_events(2, "scrum-kernel", "k") + [use(9, "Read", {"file_path": "x"}), res(9, "1\ta")]
                                        + skill_events(3, "sprint-kernel", "k") + skill_events(4, "memory", mem_text) + [{"type": "result", "result": "d"}])), "developer")
    check(not r["pass"] and r["other_tools_before_memory"], "roles: a Read before the Memory fails")
    r = judge_roles(parse_stream(stream(sum((skill_events(i, k, "k") for i, k in enumerate(ENTRY_ORDER["developer"], 1)), []) + [{"type": "result", "result": "d"}])), "developer")
    check(not r["pass"] and not r["memory_body"], "roles: a Memory call whose text is missing fails")
    check(not judge_roles(parse_stream(stream(good)), "designer")["pass"], "roles: the order must be the entry's own")

    # 3. real carrier streams (the stand-in Memory, its own markers)
    car = pathlib.Path(r"S:\IDEO-Scrum-Archives\sprint-26-plugin-memory\carrier-formal-10k")
    if car.exists():
        c = json.loads((car / "canaries.json").read_text(encoding="utf-8"))
        marks = (c["MEMORY-START"], c["MEMORY-END"])
        outs = [judge_roles(parse_stream(car / "trials" / f"role-A1-developer-{k}" / "stream.jsonl"), "developer", marks) for k in (1, 2, 3)]
        check(all(o["pass"] for o in outs), "roles: the three carrier Developer sessions (known 3/3) pass")
        o = judge_roles(parse_stream(car / "trials" / "role-A1-scrum-master-1" / "stream.jsonl"), "scrum-master", marks)
        check(o["pass"], "roles: a carrier Scrum Master session passes with the Scrum Master order: " + str(o["seen"][:6]))
        s = judge_sub(parse_stream(car / "trials" / "subagent-A1-developer-1" / "stream.jsonl"), marks)
        check(s["agent"] and not s["memory_loaded"] and "Suggest a folder name" in (s["delegation_prompt"] or ""), "sub: the carrier subagent session (known 0/1) shows an Agent call with the bare task and no Memory")
    else:
        print("skip carrier streams (not found)")

    # 4. the A judge on Sprint 24's streams, with Sprint 24's known counts: the candidate read everything before drafting in 12 of 12, the baseline in 0 of 12
    s24 = pathlib.Path(r"S:\IDEO-Scrum-Archives\sprint-24-loading-reliability\h8-h11\raw\streams")
    if s24.exists():
        def old_text(rev: str):
            def file_text(kind: str, rel: str) -> str:
                if kind == "project":
                    return (S24_FIXTURES / "g2" / rel).read_text(encoding="utf-8")
                cands = [f"plugins/ideo-scrum/{rel}", f"plugins/ideo-scrum/skills/scrum-kernel/conventions/{rel.split('/')[-1]}",
                         f"plugins/ideo-scrum/skills/sprint-kernel/conventions/{rel.split('/')[-1]}", f"plugins/ideo-scrum/skills/design-kernel/conventions/{rel.split('/')[-1]}"]
                for c in cands:
                    try:
                        return git("show", f"{rev}:{c}").decode("utf-8")
                    except subprocess.CalledProcessError:
                        continue
                raise FileNotFoundError(rel)
            return file_text

        counts = {"B": [0, 0], "C": [0, 0]}
        latest: dict = {}
        for stamp in sorted(s24.iterdir()):
            if not stamp.is_dir():
                continue
            for trial in stamp.iterdir():
                name = trial.name.split(".")[0]
                if name[:2] in ("G1", "G2", "D1", "R1") and trial.is_dir():
                    for arm in ("B", "C"):
                        f = trial / arm / "session.jsonl"
                        if f.exists():
                            latest[(name, arm)] = f
        arm_rev = {"B": "00c224b", "C": "a482a52"}
        for (name, arm), f in sorted(latest.items()):
            key = name.split("-")[0]
            p = parse_stream(f)
            j = judge_a(p, REQUIRED["B"][key], old_text(arm_rev[arm]), template_by_name=True)
            counts[arm][1] += 1
            counts[arm][0] += 1 if j["pass"] else 0
            print(f"   {name}/{arm}: {'pass' if j['pass'] else 'no'}  missing={j['missing'][:4]}")
        check(counts["C"] == [12, 12], f"s24: the candidate (known 12/12 read in full before drafting): {counts['C']}")
        check(counts["B"][0] == 0 and counts["B"][1] == 12, f"s24: the baseline (known 0/12): {counts['B']}")
    else:
        print("skip Sprint 24 streams (not found)")
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("selftest").set_defaults(fn=cmd_selftest)
    b = sub.add_parser("build")
    b.add_argument("--out", required=True)
    b.set_defaults(fn=cmd_build)
    r = sub.add_parser("run")
    r.add_argument("--out", required=True)
    r.add_argument("--group", required=True, choices=["roles", "sub", "model", "trig", "s24"])
    r.add_argument("--arm", default="B,C")
    r.add_argument("--n", type=int, default=3)
    r.add_argument("--parallel", type=int, default=2)
    r.add_argument("--max-seconds", type=int, default=0)
    r.add_argument("--soft-free-mb", type=int, default=2765, help="below this the run drops to one session at a time (politeness, not a start condition); 0 = off")
    r.add_argument("--watchdog-mb", type=int, default=WATCHDOG_MB, help="stop the running sessions when free memory is under this twice in a row")
    r.add_argument("--skip-done", action="store_true")
    r.add_argument("--retry-limit", type=int, default=1, help="how many times a stopped trial may be run again")
    r.add_argument("--only", default="")
    r.set_defaults(fn=cmd_run)
    rp = sub.add_parser("report")
    rp.add_argument("--out", required=True)
    rp.set_defaults(fn=cmd_report)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
