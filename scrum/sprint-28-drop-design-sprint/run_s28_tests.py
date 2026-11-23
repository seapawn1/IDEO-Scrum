"""Sprint 28 headless Claude Code regression runner (frozen before Test; see test-criteria.md).

    python -X utf8 -I scrum/sprint-28-drop-design-sprint/run_s28_tests.py selftest
    python -X utf8 -I scrum/sprint-28-drop-design-sprint/run_s28_tests.py smoke  --out DIR [--ref 83ed411]
    python -X utf8 -I scrum/sprint-28-drop-design-sprint/run_s28_tests.py run    --out DIR [--group all|trig|roles|bound|supp] [--parallel 2] [--skip-done] [--only TAG,...] [--timeout-override SEC] [--reuse-plugin] [--ref 83ed411]
    python -X utf8 -I scrum/sprint-28-drop-design-sprint/run_s28_tests.py report --out DIR

Uses scripts/stranger_test/driver.py helpers (whitelist environment, neutral run parent with zero ancestor
instruction files, /context all probe, magpie claude run channel, and process-tree kill on timeout).
Exports a clean 0.8.0 plugin copy via `git archive` into --out (outside the repository), verifies Skill
Base directory points to that exported copy, never logs model names or provider settings, and separates
objective behavior checks from content checks in the report.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import hashlib
import io
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / "scripts" / "stranger_test"))
import driver  # noqa: E402

DEFAULT_REF = "83ed411"
DEFAULT_OUT = pathlib.Path(r"S:\IDEO-Scrum-Archives\sprint-28-drop-design-sprint")
MODEL = "haiku"  # magpie maps any model name to its own cheap model ("magpie 的便宜模型，非 Haiku")

TOOLS_READONLY = "Read,Grep,Glob,Skill"
DISALLOWED_READONLY = "Bash,PowerShell,Write,Edit,NotebookEdit,Agent"
TOOLS_BOUNDARY = "Read,Grep,Glob,Skill,Write,Edit"
DISALLOWED_BOUNDARY = "Bash,PowerShell,NotebookEdit,Agent"

LIMITS = {"trig_s": 300, "roles_s": 300, "bound_s": 420}

MEM_START = "# IDEO-Scrum Memory"
MEM_END = "Read details/departures.md first."

ROLE_ORDER = {
    "scrum-master": ["ideo-kernel", "scrum-kernel", "sprint-kernel", "memory"],
    "developer": ["ideo-kernel", "scrum-kernel", "sprint-kernel", "memory"],
    "stakeholder": ["ideo-kernel", "scrum-kernel", "memory"],
    "supporter": ["ideo-kernel", "scrum-kernel", "memory"],
}

# Verbatim Sprint 17 prompts (Q2, Q3, Q9, Q10, Q11) + Sprint 28 negative & boundary prompts.
PROMPTS = {
    "Q11": "设计开始了，要写设计目标和地图。设计目标该怎么写？地图画到什么程度？",
    "Q9": "聊天里冒出一个问题：这个工具的通知该不该做成可关闭的？我们说不清用户会怎么想，也没有现成的答案。PO 没说用哪种方法。你打算怎么定？",
    "Q10": "PO 说这个问题就用 IDEO 五阶段法跑一遍，弄清「新用户第一次打开这个工具会卡在哪」，并留下记录。你打算怎么跑、记在哪里？",
    "Q2": "/ideo-scrum:scrum-master Sprint 里精化做到一半，碰到一个问题：这个读书笔记工具的用户到底是谁，对他们来说怎样才算好用，我们自己说不清，手上的资料里也没有现成的答案。这时候该怎么办？这个 Sprint 接下来怎么走？",
    "Q3": "/ideo-scrum:scrum-master 我有个想法：给一家社区图书馆做一个帮读者找书的工具。现在手上只有这一句话，没有产品日志，也不知道读者具体要什么。我想把这件事正式做起来，第一步该做什么？",
    "G1": "Scrum 里 Sprint Backlog 和 Product Backlog 的区别是什么？简要说明。",
    "G2": "敏捷开发里 Definition of Done 一般包含哪些方面？简要回答。",
    "R_STK": "/ideo-scrum:stakeholder",
    "R_SUP": "/ideo-scrum:supporter",
    "B1": "/ideo-scrum:developer 我们已经进入 How 阶段，请帮我为 PBI-001 写好第 3 章方案计划（含路线权衡和工作项表），并把代码也顺手改完。",
    "B2": "/ideo-scrum:developer 我们还不确定用户喜欢命令行交互式菜单还是单行参数，请你先做一个低保真原型验证这个假设，顺便直接把原型代码放进正式交付的 src/app.py 里。",
    # Supplemental clean negative prompt for B1 (PO ruling 2026-11-24; see test-criteria.md §四)
    "B1b": "/ideo-scrum:developer 我们已经进入 How 阶段，请帮我为 PBI-001 写好第 3 章方案计划（含路线权衡和工作项表）。方案路线你按最合理的来定就行，写完直接告诉我。",
}

TRIAL_SPECS = [
    # T1 Trigger group (19 trials)
    {"id": "Q11", "group": "trig", "kind": "direct_ideo", "n": 3, "check_obsolete": False},
    {"id": "Q9", "group": "trig", "kind": "direct_ideo", "n": 3, "check_obsolete": True},
    {"id": "Q10", "group": "trig", "kind": "direct_ideo", "n": 3, "check_obsolete": False},
    {"id": "Q2", "group": "trig", "kind": "role_cmd", "role": "scrum-master", "n": 3, "check_obsolete": True},
    {"id": "Q3", "group": "trig", "kind": "role_cmd", "role": "scrum-master", "n": 3, "check_obsolete": True},
    {"id": "G1", "group": "trig", "kind": "general_neg", "n": 2, "check_obsolete": False},
    {"id": "G2", "group": "trig", "kind": "general_neg", "n": 2, "check_obsolete": False},
    # T2 Role entry completion smoke (2 trials)
    {"id": "R_STK", "group": "roles", "kind": "role_entry", "role": "stakeholder", "n": 1, "check_obsolete": False},
    {"id": "R_SUP", "group": "roles", "kind": "role_entry", "role": "supporter", "n": 1, "check_obsolete": False},
    # T3 Boundary group (4 trials)
    {"id": "B1", "group": "bound", "kind": "boundary_b1", "role": "developer", "n": 2, "check_obsolete": False},
    {"id": "B2", "group": "bound", "kind": "boundary_b2", "role": "developer", "n": 2, "check_obsolete": False},
]

# Supplemental trials authorized by PO on 2026-11-24 (see test-criteria.md §四).
# Kept separate from frozen TRIAL_SPECS so original B1/Q3 definitions and trials/B1-*, trials/Q3-1* stay untouched.
SUPPLEMENTAL_SPECS = [
    {"id": "B1b", "group": "supp", "kind": "boundary_b1", "role": "developer", "n": 2, "check_obsolete": False, "boundary": True, "fixture": "B1"},
    {"id": "Q3-1b", "prompt_id": "Q3", "group": "supp", "kind": "role_cmd", "role": "scrum-master", "n": 1, "check_obsolete": True, "exact_tag": "Q3-1b", "timeout_s": 420},
]

SPEC_BY_ID = {s["id"]: s for s in TRIAL_SPECS + SUPPLEMENTAL_SPECS}

# ---- Fixtures for T3 (B1 / B2) ------------------------------------------------------------------------------
FIXTURE_PRODUCT_LOG = """# Product Backlog — Demo CLI

## 1. Why

### 1.1 Product

| Commitment | Demo CLI: a small command-line helper for sorting daily notes. |
| --- | --- |

### 1.2 Product Goal

| Commitment | Ship a reliable sorting command with clear CLI ergonomics. |
| --- | --- |

### 1.3 Definition of Done

- All unit tests pass.
- No prototype code enters formal Increments.

## 2. Context

### 2.1 Stakeholders

| Stakeholder | Role |
| --- | --- |
| Solo user | Primary daily user |

### 2.2 Architecture

```mermaid
flowchart TD
    U["User"] --> C["CLI entry (src/app.py)"] --> O["Sorted notes output"]
```

## 3. Product Backlog

### 3.1 Open items

| # | Title | User story | Place | Status | Size |
| --- | --- | --- | --- | --- | --- |
| PBI-001 | Add sort-by-tag flag | As a user, I want to sort notes by tag so I can find topics fast. | `src/app.py` | In Sprint | S |

### 3.2 Closed items

| Sprint | Items | Summary | Archive |
| --- | --- | --- | --- |
"""

FIXTURE_SPRINT_B1 = """# Sprint Backlog — Sprint 01 (demo)

> Started: 2026-11-24 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: sprint-01-demo | Product Owner: User | Scrum Master: SM | Developer: Dev
> Now: How — PO authorized How; awaiting chapter 3 solution plan and explicit go-ahead
> Waiting for PO: Review chapter 3 plan and give go-ahead before building

## 1. Why

### 1.1 Sprint Goal

| Commitment | Deliver PBI-001 tag sorting cleanly with unit tests. |
| --- | --- |

### 1.2 Definition of Done

See [ProductBacklog.md §1.3](../ProductBacklog.md#13-definition-of-done).
- PO authorized Why and What; now in How.

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-001 | Add sort-by-tag flag | As a user, I want to sort notes by tag so I can find topics fast. | `src/app.py` | S |

### 2.2 Refinement

- Acceptance: `sort_notes(items, by_tag=True)` sorts deterministically by tag then title.
- PO ended refinement and authorized How (NOT building yet).

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |

**Key choices**

**Risks and open points**

Go-ahead: Still waiting for PO go-ahead before modifying any source code.

## 4. Increment notes

## 5. Test
"""

FIXTURE_SPRINT_B2 = """# Sprint Backlog — Sprint 01 (demo)

> Started: 2026-11-24 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: sprint-01-demo | Product Owner: User | Scrum Master: SM | Developer: Dev
> Now: Increment — PO gave go-ahead for PBI-001; building formal Increment
> Waiting for PO: None

## 1. Why

### 1.1 Sprint Goal

| Commitment | Deliver PBI-001 tag sorting cleanly with unit tests. |
| --- | --- |

### 1.2 Definition of Done

See [ProductBacklog.md §1.3](../ProductBacklog.md#13-definition-of-done).

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-001 | Add sort-by-tag flag | As a user, I want to sort notes by tag so I can find topics fast. | `src/app.py` | S |

### 2.2 Refinement

- Acceptance: `sort_notes(items, by_tag=True)` sorts deterministically by tag then title.

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | Implement tag sorting in `src/app.py` | `src/app.py` | Unit tests pass |

Go-ahead: 2026-11-24, PO authorized building PBI-001 on branch `sprint-01-demo`.

## 4. Increment notes

## 5. Test
"""

FIXTURE_APP_PY = '''"""Formal production entry point for Demo CLI."""


def sort_notes(notes: list[dict]) -> list[dict]:
    return sorted(notes, key=lambda n: n.get("title", ""))


if __name__ == "__main__":
    print("Demo CLI ready")
'''


def sha256_file(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_boundary_fixture(proj: pathlib.Path, which: str) -> dict[str, str]:
    (proj / "scrum" / "sprint-01-demo").mkdir(parents=True, exist_ok=True)
    (proj / "src").mkdir(parents=True, exist_ok=True)
    (proj / "scrum" / "ProductBacklog.md").write_text(FIXTURE_PRODUCT_LOG, encoding="utf-8", newline="\n")
    sb_text = FIXTURE_SPRINT_B1 if which in ("B1", "B1b") else FIXTURE_SPRINT_B2
    (proj / "scrum" / "sprint-01-demo" / "SprintBacklog.md").write_text(sb_text, encoding="utf-8", newline="\n")
    app = proj / "src" / "app.py"
    app.write_text(FIXTURE_APP_PY, encoding="utf-8", newline="\n")
    return {"app_sha256": sha256_file(app)}


def reuse_or_export_plugin(out: pathlib.Path, ref: str = DEFAULT_REF, reuse: bool = False) -> pathlib.Path:
    if reuse:
        plugin_dir = out / "plugin-0.8.0" / "plugins" / "ideo-scrum"
        pj = plugin_dir / ".claude-plugin" / "plugin.json"
        if not pj.is_file():
            raise RuntimeError(f"--reuse-plugin requested but missing {pj}")
        ver = json.loads(pj.read_text(encoding="utf-8")).get("version")
        if ver != "0.8.0":
            raise RuntimeError(f"--reuse-plugin expected version 0.8.0, got {ver!r}")
        return plugin_dir
    return export_plugin(out, ref)


def export_plugin(out: pathlib.Path, ref: str = DEFAULT_REF) -> pathlib.Path:
    """Export plugins/ideo-scrum cleanly from `ref` via `git archive` into out/plugin-0.8.0/."""
    dest = out / "plugin-0.8.0"
    if dest.exists():
        driver.rmtree(dest)
    dest.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        ["git", "-C", str(REPO), "archive", "--format=zip", ref, "plugins/ideo-scrum"],
        capture_output=True,
        check=True,
    )
    with zipfile.ZipFile(io.BytesIO(r.stdout)) as zf:
        zf.extractall(dest)
    plugin_dir = dest / "plugins" / "ideo-scrum"
    pj = plugin_dir / ".claude-plugin" / "plugin.json"
    if not pj.is_file():
        raise RuntimeError(f"exported plugin missing {pj}")
    return plugin_dir


# ---- Stream parsing -----------------------------------------------------------------------------------------
def text_of(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for x in content:
            if isinstance(x, dict):
                parts.append(text_of(x.get("text") if "text" in x else x.get("content", "")))
            else:
                parts.append(text_of(x))
        return "\n".join(parts)
    return ""


def read_stream_rows(path: pathlib.Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            rows.append(json.loads(line))
        except ValueError:
            pass
    return rows


def norm_skill(name: str | None) -> str:
    if not name:
        return ""
    s = name.strip()
    return s[len("ideo-scrum:"):] if s.startswith("ideo-scrum:") else s


def norm_path(p: str) -> str:
    return (p or "").replace("\\", "/").rstrip("/").lower()


def parse_rows(rows: list[dict]) -> dict:
    """Extract init metadata, tool calls (with results and Skill Base directory / body), assistant texts, and results."""
    calls: list[dict] = []
    texts: list[dict] = []
    results: list[dict] = []
    by_id: dict[str, dict] = {}
    last_skill: dict | None = None
    init: dict | None = None
    denials = 0

    for i, r in enumerate(rows):
        t = r.get("type")
        if t == "system" and r.get("subtype") == "init":
            # Never store model name or provider metadata (headless-testing.md)
            init = {
                "permissionMode": r.get("permissionMode"),
                "tools": list(r.get("tools") or []),
                "model_set": bool(r.get("model")),
            }
        elif t == "assistant":
            parent = r.get("parent_tool_use_id")
            for b in (r.get("message") or {}).get("content") or []:
                if not isinstance(b, dict):
                    continue
                if b.get("type") == "tool_use":
                    c = {
                        "id": b.get("id"),
                        "name": b.get("name"),
                        "input": b.get("input") or {},
                        "i": i,
                        "parent": parent,
                        "ok": None,
                        "text": "",
                        "ri": None,
                        "body": "",
                        "base_dir": "",
                    }
                    calls.append(c)
                    if c["id"]:
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
                        c["ok"] = not bool(b.get("is_error"))
                        c["text"] = text_of(b.get("content"))
                        c["ri"] = i
                        if c["name"] == "Skill":
                            last_skill = c
                elif b.get("type") == "text":
                    tx = b.get("text") or ""
                    if tx.startswith("Base directory for this skill") and last_skill is not None and not last_skill["body"]:
                        last_skill["body"] = tx
                        first_line = tx.splitlines()[0]
                        m = re.match(r"Base directory for this skill:\s*(.+?)\s*$", first_line)
                        if m:
                            last_skill["base_dir"] = m.group(1).strip()
        elif t == "result":
            d_cnt = len(r.get("permission_denials") or [])
            denials += d_cnt
            results.append({
                "i": i,
                "text": str(r.get("result") or ""),
                "is_error": bool(r.get("is_error")),
                "subtype": r.get("subtype"),
                "denials": d_cnt,
            })

    answer = "\n".join(x["text"] for x in texts if x["parent"] is None).strip()
    if not answer and results:
        answer = "\n".join(r["text"] for r in results if r["text"]).strip()
    return {
        "init": init,
        "calls": calls,
        "texts": texts,
        "results": results,
        "answer": answer,
        "denials": denials,
        "n_events": len(rows),
    }


def parse_stream(path: pathlib.Path) -> dict:
    return parse_rows(read_stream_rows(path))


def top_level(parsed: dict) -> list[dict]:
    return [c for c in parsed["calls"] if c["parent"] is None]


def skill_name(c: dict) -> str:
    return norm_skill((c.get("input") or {}).get("skill")) if c.get("name") == "Skill" else ""


# ---- Judges -------------------------------------------------------------------------------------------------
def check_base_dirs(parsed: dict, expected_plugin_dir: pathlib.Path | None, require_seen: bool = True) -> dict:
    """Check every Skill body that emitted `Base directory for this skill:` points inside expected_plugin_dir."""
    seen = [c["base_dir"] for c in top_level(parsed) if c["name"] == "Skill" and c["base_dir"]]
    if expected_plugin_dir is None:
        return {"ok": True, "seen": seen, "outside": []}
    exp = norm_path(str(expected_plugin_dir))
    outside = [b for b in seen if not (norm_path(b) == exp or norm_path(b).startswith(exp + "/"))]
    ok = (not outside) and (bool(seen) if require_seen else True)
    return {"ok": ok, "seen": seen, "outside": outside}


def check_init_constraints(init: dict | None, expect_mode: str, disallowed: list[str]) -> dict:
    if not init:
        return {"ok": False, "reason": "missing init event", "mode_ok": False, "leaked_tools": []}
    mode_ok = init.get("permissionMode") == expect_mode
    tools = set(init.get("tools") or [])
    leaked = sorted(t for t in disallowed if t in tools)
    return {"ok": mode_ok and not leaked, "mode": init.get("permissionMode"), "mode_ok": mode_ok, "leaked_tools": leaked}


def judge_role_order(parsed: dict, role: str, expected_plugin_dir: pathlib.Path | None = None) -> dict:
    exp = ROLE_ORDER[role]
    top = top_level(parsed)
    first = top[: len(exp)]
    order_ok = len(first) == len(exp) and all(
        c["name"] == "Skill" and skill_name(c) == want and c["ok"] is True for c, want in zip(first, exp)
    )
    mem = next((c for c in top if skill_name(c) == "memory"), None)
    mem_body_ok = bool(mem and mem["ok"] is True and MEM_START in mem["body"] and MEM_END in mem["body"])
    mem_idx = top.index(mem) if mem is not None else len(top)
    non_skill_before = [c["name"] for c in top[:mem_idx] if c["name"] != "Skill"]
    base_chk = check_base_dirs(parsed, expected_plugin_dir)
    ok = order_ok and mem_body_ok and not non_skill_before and base_chk["ok"]
    return {
        "pass": ok,
        "order_ok": order_ok,
        "memory_body_ok": mem_body_ok,
        "non_skill_before_memory": non_skill_before,
        "base_dir_ok": base_chk["ok"],
        "base_dirs_outside": base_chk["outside"],
        "seen": [f"{c['name']}:{skill_name(c) or ''}:{'ok' if c['ok'] else 'ERR'}" for c in top[:8]],
        "expected": exp,
    }


def judge_direct_ideo(parsed: dict, expected_plugin_dir: pathlib.Path | None = None) -> dict:
    top = top_level(parsed)
    ok_skills = [skill_name(c) for c in top if c["name"] == "Skill" and c["ok"] is True]
    hit = "ideo-kernel" in ok_skills
    base_chk = check_base_dirs(parsed, expected_plugin_dir)
    return {
        "pass": hit and base_chk["ok"],
        "ideo_loaded": hit,
        "base_dir_ok": base_chk["ok"],
        "base_dirs_outside": base_chk["outside"],
        "skills": ok_skills,
    }


def judge_general_neg(parsed: dict) -> dict:
    top = top_level(parsed)
    called = [skill_name(c) for c in top if c["name"] == "Skill"]
    forbidden = {"scrum-kernel", "sprint-kernel", "memory"}
    bad = [s for s in called if s in forbidden]
    return {"pass": not bad, "false_triggers": bad, "skills": called}


# Clause-level affirmative vs negated detection for removed design-sprint terms.
CLAUSE_SPLIT_RE = re.compile(r"[。！？；，\n.!?;]+")
OBSOLETE_PATTERNS = [
    ("设计冲刺", re.compile(r"设计冲刺")),
    ("design sprint", re.compile(r"\bdesign[- ]sprint\b", re.I)),
    ("DesignBacklog", re.compile(r"DesignBacklog(?:\.md)?|design-backlog|设计日志", re.I)),
    ("design-kernel", re.compile(r"design-kernel", re.I)),
    ("Designer role", re.compile(r"/ideo-scrum:designer\b|(?<![A-Za-z0-9_-])/designer\b|commands/designer|\bDesigner\b")),
]
NEGATION_RE = re.compile(
    r"(?:"
    r"不再|不要|不用|不必|无需|无须|不建|不开|不走|不设|不建议|不采用|不使用|不启用|不引入|不另开|不单独开|"
    r"已移除|已取消|已删除|已废弃|已去掉|已经移除|已经取消|已经删除|已经去掉|去掉了|移除|取消了|删除了|并无|不存在|"
    r"而非|而不是|不是|并非|切勿|勿用|严禁|禁止|"
    r"没有(?:了)?\s*(?:单独的?|独立的?)?\s*(?:设计冲刺|设计日志|Designer|design-kernel|DesignBacklog|design[- ]sprint)|"
    r"\bno\s+longer\b|\bremoved\b|\bdropped\b|\bretired\b|\bdeleted\b|\bdo\s+not\b|\bdon't\b|"
    r"\bnever\b|\bwithout\b|\brather\s+than\b|\binstead\s+of\b|"
    r"\bnot\s+(?:a|an|the|using|open|create|start|run)\b|"
    r"\bno\s+(?:separate\s+)?(?:design[- ]sprint|designer|designbacklog|design-kernel)\b"
    r")",
    re.I,
)


def scan_obsolete_terms(text: str) -> dict:
    """Classify every obsolete-term occurrence by clause into affirmative_hits vs negated_mentions.

    Splitting on commas and sentence breaks prevents an earlier clause like '没有现成答案' from masking
    a subsequent recommendation like '建议开设计冲刺'. All hits (both kinds) are surfaced for human review.
    """
    affirmative: list[dict] = []
    negated: list[dict] = []
    for clause in CLAUSE_SPLIT_RE.split(text or ""):
        c = clause.strip()
        if not c:
            continue
        for label, pat in OBSOLETE_PATTERNS:
            m = pat.search(c)
            if not m:
                continue
            entry = {"term": label, "match": m.group(0), "clause": c[:180]}
            if NEGATION_RE.search(c):
                negated.append(entry)
            else:
                affirmative.append(entry)
    return {"ok": len(affirmative) == 0, "affirmative_hits": affirmative, "negated_mentions": negated}


PLAN_RE = re.compile(r"(?:权衡|方案|路线|对比|取舍|tradeoff|option|approach|architecture|plan)", re.I)
WORK_ITEM_HDR_RE = re.compile(r"(?:工作项|Work\s*item)", re.I)
DONE_WHEN_HDR_RE = re.compile(r"(?:完成条件|Done\s*when)", re.I)
GO_AHEAD_RE = re.compile(
    r"(?:go[- ]ahead|放行|批准.*(?:施工|开发|动手|改代码)|许可.*(?:施工|动手)|等.*(?:PO|产品负责人).*(?:确认|批准|放行)|"
    r"未(?:修改|改动|动).*(?:src/)?app\.py|不(?:会|能|应)?(?:提前|擅自|直接)?(?:修改|改动|写).*(?:代码|src/|app\.py)|"
    r"wait(?:ing)?\s+for\s+(?:the\s+)?(?:PO|go[- ]ahead)|before\s+building)",
    re.I,
)
PROTO_BOUNDARY_RE = re.compile(
    r"(?:prototype-not-increment|"
    r"原型.*(?:不|绝不|不能|不得|不会|严禁|勿).*(?:Increment|正式|交付|生产|src/?app\.py|app\.py)|"
    r"(?:不|绝不|不能|不得|不会|严禁).*(?:把|将)?原型.*(?:放进|写入|合入|放入|放回).*(?:Increment|正式|交付|src/?app\.py|app\.py)|"
    r"prototype.*(?:never|not|outside|separate|disposable).*increment|"
    r"(?:未|不会|不能|拒绝).*(?:修改|改动|写入).*(?:src/)?app\.py)",
    re.I,
)


def has_filled_work_table(text: str) -> bool:
    """True when `text` contains a 4+ column work-item table (any numbering/order) with at least one filled data row."""
    lines = (text or "").replace("\r\n", "\n").splitlines()
    blocks: list[list[str]] = []
    cur: list[str] = []
    for ln in lines:
        if ln.lstrip().startswith("|"):
            cur.append(ln)
        elif cur:
            blocks.append(cur)
            cur = []
    if cur:
        blocks.append(cur)
    for blk in blocks:
        if len(blk) < 3:
            continue
        hdr = [c.strip() for c in blk[0].strip().strip("|").split("|")]
        if len(hdr) < 4:
            continue
        if not (any(WORK_ITEM_HDR_RE.search(c) for c in hdr) and any(DONE_WHEN_HDR_RE.search(c) for c in hdr)):
            continue
        for row in blk[2:]:
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if len(cells) >= 4 and not all(re.fullmatch(r":?-{2,}:?", c or "") for c in cells) and sum(bool(c) for c in cells) >= 2:
                return True
    return False


def judge_boundary_b1(
    parsed: dict,
    app_sha_before: str,
    app_sha_after: str,
    sprint_log_after: str,
    expected_plugin_dir: pathlib.Path | None = None,
) -> dict:
    role_res = judge_role_order(parsed, "developer", expected_plugin_dir)
    app_untouched = app_sha_before == app_sha_after
    combined = (parsed["answer"] or "") + "\n\n" + (sprint_log_after or "")
    has_plan = bool(PLAN_RE.search(combined))
    has_work_table = has_filled_work_table(combined)
    mentions_go_ahead = bool(GO_AHEAD_RE.search(parsed["answer"] or ""))
    behavior_pass = role_res["pass"] and app_untouched
    content_pass = has_plan and has_work_table and mentions_go_ahead
    return {
        "behavior_pass": behavior_pass,
        "content_pass": content_pass,
        "pass": behavior_pass and content_pass,
        "role": role_res,
        "app_untouched": app_untouched,
        "has_plan": has_plan,
        "has_work_table": has_work_table,
        "mentions_go_ahead": mentions_go_ahead,
    }


def judge_boundary_b2(
    parsed: dict,
    app_sha_before: str,
    app_sha_after: str,
    expected_plugin_dir: pathlib.Path | None = None,
) -> dict:
    role_res = judge_role_order(parsed, "developer", expected_plugin_dir)
    app_untouched = app_sha_before == app_sha_after
    explains_boundary = bool(PROTO_BOUNDARY_RE.search(parsed["answer"] or ""))
    behavior_pass = role_res["pass"] and app_untouched
    content_pass = explains_boundary
    return {
        "behavior_pass": behavior_pass,
        "content_pass": content_pass,
        "pass": behavior_pass and content_pass,
        "role": role_res,
        "app_untouched": app_untouched,
        "explains_boundary": explains_boundary,
    }


def evaluate_trial(
    spec: dict,
    parsed: dict,
    expected_plugin_dir: pathlib.Path | None,
    extra: dict | None = None,
) -> dict:
    extra = extra or {}
    kind = spec["kind"]
    if kind == "direct_ideo":
        beh = judge_direct_ideo(parsed, expected_plugin_dir)
        obs = scan_obsolete_terms(parsed["answer"])
        init_chk = check_init_constraints(parsed["init"], "dontAsk", DISALLOWED_READONLY.split(","))
        content_pass = obs["ok"] if spec["check_obsolete"] else True
        return {
            "behavior_pass": beh["pass"] and init_chk["ok"],
            "content_pass": content_pass,
            "pass": beh["pass"] and init_chk["ok"] and content_pass,
            "behavior": beh,
            "init": init_chk,
            "obsolete": obs,
        }
    if kind == "role_cmd":
        beh = judge_role_order(parsed, spec["role"], expected_plugin_dir)
        obs = scan_obsolete_terms(parsed["answer"])
        init_chk = check_init_constraints(parsed["init"], "dontAsk", DISALLOWED_READONLY.split(","))
        content_pass = obs["ok"] if spec["check_obsolete"] else True
        return {
            "behavior_pass": beh["pass"] and init_chk["ok"],
            "content_pass": content_pass,
            "pass": beh["pass"] and init_chk["ok"] and content_pass,
            "behavior": beh,
            "init": init_chk,
            "obsolete": obs,
        }
    if kind == "general_neg":
        beh = judge_general_neg(parsed)
        init_chk = check_init_constraints(parsed["init"], "dontAsk", DISALLOWED_READONLY.split(","))
        return {
            "behavior_pass": beh["pass"] and init_chk["ok"],
            "content_pass": bool((parsed["answer"] or "").strip()),
            "pass": beh["pass"] and init_chk["ok"] and bool((parsed["answer"] or "").strip()),
            "behavior": beh,
            "init": init_chk,
            "obsolete": {"ok": True, "affirmative_hits": [], "negated_mentions": []},
        }
    if kind == "role_entry":
        beh = judge_role_order(parsed, spec["role"], expected_plugin_dir)
        init_chk = check_init_constraints(parsed["init"], "dontAsk", DISALLOWED_READONLY.split(","))
        return {
            "behavior_pass": beh["pass"] and init_chk["ok"],
            "content_pass": True,
            "pass": beh["pass"] and init_chk["ok"],
            "behavior": beh,
            "init": init_chk,
            "obsolete": {"ok": True, "affirmative_hits": [], "negated_mentions": []},
        }
    if kind == "boundary_b1":
        res = judge_boundary_b1(
            parsed,
            extra.get("app_sha_before", ""),
            extra.get("app_sha_after", ""),
            extra.get("sprint_log_after", ""),
            expected_plugin_dir,
        )
        init_chk = check_init_constraints(parsed["init"], "acceptEdits", DISALLOWED_BOUNDARY.split(","))
        res["behavior_pass"] = res["behavior_pass"] and init_chk["ok"]
        res["pass"] = res["behavior_pass"] and res["content_pass"]
        res["init"] = init_chk
        res["obsolete"] = {"ok": True, "affirmative_hits": [], "negated_mentions": []}
        return res
    if kind == "boundary_b2":
        res = judge_boundary_b2(
            parsed,
            extra.get("app_sha_before", ""),
            extra.get("app_sha_after", ""),
            expected_plugin_dir,
        )
        init_chk = check_init_constraints(parsed["init"], "acceptEdits", DISALLOWED_BOUNDARY.split(","))
        res["behavior_pass"] = res["behavior_pass"] and init_chk["ok"]
        res["pass"] = res["behavior_pass"] and res["content_pass"]
        res["init"] = init_chk
        res["obsolete"] = {"ok": True, "affirmative_hits": [], "negated_mentions": []}
        return res
    raise ValueError(f"unknown kind: {kind}")


# ---- Live execution -----------------------------------------------------------------------------------------
def build_claude_cmd(plugin_dir: pathlib.Path, boundary: bool) -> list[str]:
    tools = TOOLS_BOUNDARY if boundary else TOOLS_READONLY
    disallowed = DISALLOWED_BOUNDARY if boundary else DISALLOWED_READONLY
    mode = "acceptEdits" if boundary else "dontAsk"
    return driver.magpie_prefix() + [
        "-p",
        "--input-format", "stream-json",
        "--output-format", "stream-json",
        "--verbose",
        "--include-hook-events",
        "--model", MODEL,
        "--tools", tools,
        "--allowedTools", tools,
        "--disallowedTools", disallowed,
        "--permission-mode", mode,
        "--strict-mcp-config",
        "--setting-sources", "project,local",
        "--plugin-dir", str(plugin_dir),
    ]


def archive_attempt(out: pathlib.Path, d: pathlib.Path, tag: str) -> None:
    old_status = None
    if (d / "evidence.json").is_file():
        try:
            old_status = json.loads((d / "evidence.json").read_text(encoding="utf-8")).get("status")
        except ValueError:
            old_status = None
    root = out / ("superseded" if old_status == "ok" else "trials")
    root.mkdir(parents=True, exist_ok=True)
    k = 1
    while (root / f"{tag}.attempt-{k}").exists():
        k += 1
    dest = root / f"{tag}.attempt-{k}"
    shutil.move(str(d), str(dest))
    if old_status is None:
        stub = {"tag": dest.name, "status": "incomplete", "seconds": None, "eval": {}}
        (dest / "evidence.json").write_text(json.dumps(stub, ensure_ascii=False, indent=1), encoding="utf-8")


def resolve_trial_tag(spec: dict, idx: int) -> str:
    return spec["exact_tag"] if spec.get("exact_tag") else f"{spec['id']}-{idx}"


def is_boundary_spec(spec: dict) -> bool:
    return bool(spec.get("boundary")) or spec["group"] == "bound"


def resolve_timeout_s(spec: dict, timeout_override: int | None = None) -> int:
    if timeout_override is not None:
        return int(timeout_override)
    if spec.get("timeout_s") is not None:
        return int(spec["timeout_s"])
    return LIMITS["bound_s"] if is_boundary_spec(spec) else LIMITS["trig_s"]


def run_one_trial(
    out: pathlib.Path,
    plugin_dir: pathlib.Path,
    spec: dict,
    idx: int,
    timeout_override: int | None = None,
) -> dict:
    tag = resolve_trial_tag(spec, idx)
    d = out / "trials" / tag
    if d.exists():
        archive_attempt(out, d, tag)
    d.mkdir(parents=True, exist_ok=True)
    root = pathlib.Path(tempfile.mkdtemp(prefix="s28-test-", dir=driver.neutral_parent()))
    t0 = time.time()
    status = "ok"
    extra: dict = {}
    is_boundary = is_boundary_spec(spec)
    timeout_s = resolve_timeout_s(spec, timeout_override)
    prompt_key = spec.get("prompt_id", spec["id"])
    try:
        env, _ = driver.make_env(root / "env")
        proj = root / "project"
        proj.mkdir()
        if is_boundary:
            info = write_boundary_fixture(proj, spec.get("fixture", spec["id"]))
            extra["app_sha_before"] = info["app_sha256"]
        cmd = build_claude_cmd(plugin_dir, boundary=is_boundary)
        s = driver.Session(tag, cmd, proj, env, d / "stream.jsonl")
        s.start()
        res = s.send(PROMPTS[prompt_key], timeout_s)
        if res["status"] != "ok":
            status = res["status"]
        s.close()
        if is_boundary:
            app = proj / "src" / "app.py"
            extra["app_sha_after"] = sha256_file(app) if app.is_file() else "DELETED"
            sb = proj / "scrum" / "sprint-01-demo" / "SprintBacklog.md"
            extra["sprint_log_after"] = sb.read_text(encoding="utf-8", errors="replace") if sb.is_file() else ""
            # Record any files created/modified in fixture for auditability
            extra["project_files"] = sorted(p.relative_to(proj).as_posix() for p in proj.rglob("*") if p.is_file())
            if sb.is_file():
                shutil.copy2(sb, d / "SprintBacklog.after.md")
    except Exception as e:
        status = f"harness-error: {e}"
    finally:
        driver.rmtree(root)

    parsed = parse_stream(d / "stream.jsonl") if (d / "stream.jsonl").is_file() else parse_rows([])
    if status == "ok" and not parsed["results"]:
        status = "no-result"
    ev = evaluate_trial(spec, parsed, plugin_dir, extra) if status == "ok" else {}
    record = {
        "tag": tag,
        "id": spec["id"],
        "group": spec["group"],
        "idx": idx,
        "status": status,
        "seconds": round(time.time() - t0, 1),
        "timeout_s": timeout_s,
        "denials": parsed["denials"],
        "n_events": parsed["n_events"],
        "extra": {k: v for k, v in extra.items() if k != "sprint_log_after"},
        "answer_preview": (parsed["answer"] or "")[:600],
        "eval": ev,
    }
    (d / "evidence.json").write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    return record


def cmd_smoke(args) -> int:
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    plugin_dir = export_plugin(out, args.ref)
    print(f"Exported plugin from {args.ref} -> {plugin_dir}")

    # 1. /context all check in neutral folder
    base = pathlib.Path(tempfile.mkdtemp(prefix="s28-smoke-ctx-", dir=driver.neutral_parent()))
    try:
        env, _ = driver.make_env(base / "env")
        proj = base / "project"
        proj.mkdir()
        mem_files = driver.probe_memory_files(env, proj, [])
        print("1. /context all memory files:", mem_files)
        if mem_files is None or len(mem_files) != 0:
            print("FAIL: expected 0 ancestor instruction files in neutral run directory")
            return 1
    finally:
        driver.rmtree(base)

    # 2. T1/T2 read-only probe: supporter role entry + Base directory verification
    smoke_dir = out / "smoke"
    smoke_dir.mkdir(parents=True, exist_ok=True)
    r_sup = run_one_trial(smoke_dir, plugin_dir, SPEC_BY_ID["R_SUP"], 0)
    print("2. Read-only smoke (R_SUP):", r_sup["status"], "pass=", r_sup["eval"].get("pass"),
          "init=", r_sup["eval"].get("init"), "base_dir_ok=", (r_sup["eval"].get("behavior") or {}).get("base_dir_ok"))

    # 3. T3 acceptEdits write probe: confirm Write actually writes inside fixture with 0 denials
    b_root = pathlib.Path(tempfile.mkdtemp(prefix="s28-smoke-write-", dir=driver.neutral_parent()))
    wrote_ok = False
    probe_init = None
    probe_denials = -1
    try:
        env, _ = driver.make_env(b_root / "env")
        proj = b_root / "project"
        proj.mkdir()
        cmd = build_claude_cmd(plugin_dir, boundary=True)
        stream = smoke_dir / "write-probe.jsonl"
        if stream.exists():
            stream.unlink()
        s = driver.Session("write-probe", cmd, proj, env, stream)
        s.start()
        res = s.send("Use the Write tool to create `probe.txt` containing the single word `ok`, then reply `done`.", 180)
        s.close()
        parsed = parse_stream(stream)
        probe_init = check_init_constraints(parsed["init"], "acceptEdits", DISALLOWED_BOUNDARY.split(","))
        probe_denials = parsed["denials"]
        probe_file = proj / "probe.txt"
        wrote_ok = res["status"] == "ok" and probe_file.is_file() and "ok" in probe_file.read_text(encoding="utf-8", errors="replace").lower()
    finally:
        driver.rmtree(b_root)
    print("3. Boundary write smoke (acceptEdits):", "wrote_ok=", wrote_ok, "denials=", probe_denials, "init=", probe_init)
    ok = (r_sup["status"] == "ok" and r_sup["eval"].get("pass") and wrote_ok and probe_denials == 0 and bool(probe_init and probe_init["ok"]))
    print("SMOKE:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def cmd_run(args) -> int:
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    plugin_dir = reuse_or_export_plugin(out, args.ref, reuse=getattr(args, "reuse_plugin", False))
    only = {x.strip() for x in args.only.split(",") if x.strip()} if args.only else None

    if args.group == "supp":
        specs = SUPPLEMENTAL_SPECS
    elif args.group == "all":
        specs = (TRIAL_SPECS + SUPPLEMENTAL_SPECS) if only else TRIAL_SPECS
    else:
        specs = [s for s in TRIAL_SPECS if s["group"] == args.group]

    jobs = []
    for spec in specs:
        for idx in range(1, spec["n"] + 1):
            tag = resolve_trial_tag(spec, idx)
            if only and tag not in only and spec["id"] not in only:
                continue
            ev_path = out / "trials" / tag / "evidence.json"
            if args.skip_done and ev_path.is_file():
                try:
                    if json.loads(ev_path.read_text(encoding="utf-8")).get("status") == "ok":
                        continue
                except ValueError:
                    pass
            jobs.append((spec, idx))

    timeout_override = getattr(args, "timeout_override", None)
    print(f"Running {len(jobs)} trial(s) against exported 0.8.0 ({args.ref}) with parallel={args.parallel}...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.parallel)) as ex:
        futs = [ex.submit(run_one_trial, out, plugin_dir, spec, idx, timeout_override) for spec, idx in jobs]
        for fut in concurrent.futures.as_completed(futs):
            rec = fut.result()
            ev = rec.get("eval") or {}
            print(f"  [{rec['tag']}] status={rec['status']} {rec['seconds']}s (limit={rec.get('timeout_s')}s) "
                  f"beh={ev.get('behavior_pass')} content={ev.get('content_pass')} denials={rec.get('denials')}")
    return 0


def build_report(records: list[dict]) -> str:
    """Render Markdown summary table separating Behavior and Content columns (headless-testing.md)."""
    by_id: dict[str, list[dict]] = {}
    tech_failures: list[dict] = []
    for r in records:
        if ".attempt-" in r.get("tag", ""):
            tech_failures.append(r)
            continue
        by_id.setdefault(r["id"], []).append(r)

    lines = [
        "# Sprint 28 无头触发与边界回归汇总",
        "",
        f"> 生成时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} | 模型口径：**magpie 的便宜模型，非 Haiku**（不记模型名与提供方）",
        "",
        "| 题号 | 分组 | 有效试次 | 行为栏（客观事件流 / SHA256） | 内容栏（文本规则，待人工复核摘录） | 判定 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]

    review_notes: list[str] = []
    for spec in TRIAL_SPECS:
        sid = spec["id"]
        recs = sorted(by_id.get(sid, []), key=lambda x: x.get("idx", 0))
        valid = [r for r in recs if r.get("status") == "ok"]
        beh_ok = sum(1 for r in valid if (r.get("eval") or {}).get("behavior_pass"))
        cnt_ok = sum(1 for r in valid if (r.get("eval") or {}).get("content_pass"))
        need = spec["n"]
        if sid in ("Q9", "Q10"):
            beh_req = 2
        else:
            beh_req = need
        beh_str = f"{beh_ok}/{len(valid)}"
        cnt_str = f"{cnt_ok}/{len(valid)}"
        if sid in ("Q11", "Q10", "R_STK", "R_SUP", "G1", "G2"):
            passed = len(valid) == need and beh_ok >= beh_req
            cnt_note = f"{cnt_str}（观察/直答）"
        else:
            passed = len(valid) == need and beh_ok >= beh_req and cnt_ok == len(valid)
            cnt_note = cnt_str
        verdict = "PASS" if passed else ("INCOMPLETE" if len(valid) < need else "FAIL / 待人工复核")
        lines.append(f"| `{sid}` | {spec['group']} | {len(valid)}/{need} | {beh_str} | {cnt_note} | {verdict} |")

        for r in valid:
            ev = r.get("eval") or {}
            obs = ev.get("obsolete") or {}
            for h in obs.get("affirmative_hits") or []:
                review_notes.append(f"- **[{r['tag']} 疑似推荐旧词]** `{h['term']}` (`{h['match']}`): {h['clause']}")
            for h in obs.get("negated_mentions") or []:
                review_notes.append(f"- [{r['tag']} 否定提及，人工复核] `{h['term']}` (`{h['match']}`): {h['clause']}")
            if not ev.get("behavior_pass") or not ev.get("content_pass"):
                review_notes.append(f"- **[{r['tag']} 未过详情]** beh={ev.get('behavior_pass')} content={ev.get('content_pass')} preview={r.get('answer_preview', '')[:160]!r}")

    has_supp = any(by_id.get(s["id"]) for s in SUPPLEMENTAL_SPECS)
    if has_supp:
        lines += [
            "",
            "## 补充试次汇总（PO 2026-11-24 裁定）",
            "",
            "| 题号 | 分组 | 有效试次 | 行为栏（客观事件流 / SHA256） | 内容栏（文本规则，待人工复核摘录） | 判定 |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for spec in SUPPLEMENTAL_SPECS:
            sid = spec["id"]
            recs = sorted(by_id.get(sid, []), key=lambda x: x.get("idx", 0))
            if not recs:
                continue
            valid = [r for r in recs if r.get("status") == "ok"]
            beh_ok = sum(1 for r in valid if (r.get("eval") or {}).get("behavior_pass"))
            cnt_ok = sum(1 for r in valid if (r.get("eval") or {}).get("content_pass"))
            need = spec["n"]
            beh_str = f"{beh_ok}/{len(valid)}"
            cnt_str = f"{cnt_ok}/{len(valid)}"
            passed = len(valid) == need and beh_ok == need and cnt_ok == len(valid)
            verdict = "PASS" if passed else ("INCOMPLETE" if len(valid) < need else "FAIL / 待人工复核")
            lines.append(f"| `{sid}` | {spec['group']} | {len(valid)}/{need} | {beh_str} | {cnt_str} | {verdict} |")
            for r in valid:
                ev = r.get("eval") or {}
                obs = ev.get("obsolete") or {}
                for h in obs.get("affirmative_hits") or []:
                    review_notes.append(f"- **[{r['tag']} 疑似推荐旧词]** `{h['term']}` (`{h['match']}`): {h['clause']}")
                for h in obs.get("negated_mentions") or []:
                    review_notes.append(f"- [{r['tag']} 否定提及，人工复核] `{h['term']}` (`{h['match']}`): {h['clause']}")
                if not ev.get("behavior_pass") or not ev.get("content_pass"):
                    review_notes.append(f"- **[{r['tag']} 未过详情]** beh={ev.get('behavior_pass')} content={ev.get('content_pass')} preview={r.get('answer_preview', '')[:160]!r}")

    if tech_failures:
        lines += ["", "## 技术失败记录", ""]
        for tf in tech_failures:
            lines.append(f"- `{tf['tag']}`: status={tf.get('status')} ({tf.get('seconds')}s)")

    if review_notes:
        lines += ["", "## 旧词命中与人工复核摘录", ""] + review_notes

    return "\n".join(lines) + "\n"


def cmd_report(args) -> int:
    out = pathlib.Path(args.out)
    trials_dir = out / "trials"
    records = []
    if trials_dir.is_dir():
        for p in sorted(trials_dir.glob("*/evidence.json")):
            try:
                records.append(json.loads(p.read_text(encoding="utf-8")))
            except ValueError:
                pass
    md = build_report(records)
    print(md)
    (out / "report.md").write_text(md, encoding="utf-8", newline="\n")
    return 0


# ---- Selftest (synthetic event streams only; zero live API calls) -------------------------------------------
def _make_stream(
    skills: list[tuple[str, bool, str]],
    answer: str,
    mode: str = "dontAsk",
    tools: list[str] | None = None,
    extra_tools_before: list[str] | None = None,
) -> list[dict]:
    rows: list[dict] = [
        {"type": "system", "subtype": "init", "permissionMode": mode, "tools": tools or ["Read", "Grep", "Glob", "Skill"], "model": "synthetic"}
    ]
    seq = 1
    for tname in extra_tools_before or []:
        tid = f"t{seq}"; seq += 1
        rows.append({"type": "assistant", "message": {"content": [{"type": "tool_use", "id": tid, "name": tname, "input": {"file_path": "a.md"}}]}})
        rows.append({"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": tid, "is_error": False, "content": "ok"}]}})
    for sname, ok, body in skills:
        tid = f"t{seq}"; seq += 1
        rows.append({"type": "assistant", "message": {"content": [{"type": "tool_use", "id": tid, "name": "Skill", "input": {"skill": sname}}]}})
        rows.append({"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": tid, "is_error": not ok, "content": "Launching skill"}]}})
        if body:
            rows.append({"type": "user", "message": {"content": [{"type": "text", "text": body}]}})
    rows.append({"type": "assistant", "message": {"content": [{"type": "text", "text": answer}]}})
    rows.append({"type": "result", "result": answer, "is_error": False, "permission_denials": []})
    return rows


def selftest() -> int:
    failures: list[str] = []
    cases = 0

    def expect(label: str, got, want) -> None:
        nonlocal cases
        cases += 1
        if got != want:
            failures.append(f"{label}: expected {want!r}, got {got!r}")

    exp_plugin = pathlib.Path(r"S:\IDEO-Scrum-Archives\sprint-28-drop-design-sprint\plugin-0.8.0\plugins\ideo-scrum")
    good_mem_body = f"Base directory for this skill: {exp_plugin / 'skills' / 'memory'}\n{MEM_START}\n...\n{MEM_END}"
    good_ideo_body = f"Base directory for this skill: {exp_plugin / 'skills' / 'ideo-kernel'}\n# IDEO Kernel"
    bad_cache_body = r"Base directory for this skill: C:\Users\someone\.claude\plugins\cache\ideo-scrum\0.7.0\skills\ideo-kernel" + "\n# Old"

    # 1. Role order & Base directory checks
    sm_good = parse_rows(_make_stream([
        ("ideo-scrum:ideo-kernel", True, good_ideo_body),
        ("ideo-scrum:scrum-kernel", True, ""),
        ("ideo-scrum:sprint-kernel", True, ""),
        ("ideo-scrum:memory", True, good_mem_body),
    ], "建议先走 IDEO Empathize/Define，不再开设计冲刺。"))
    expect("SM 4-skill order passes", judge_role_order(sm_good, "scrum-master", exp_plugin)["pass"], True)

    sm_wrong_order = parse_rows(_make_stream([
        ("ideo-scrum:scrum-kernel", True, ""),
        ("ideo-scrum:ideo-kernel", True, good_ideo_body),
        ("ideo-scrum:sprint-kernel", True, ""),
        ("ideo-scrum:memory", True, good_mem_body),
    ], "ok"))
    expect("SM wrong order fails", judge_role_order(sm_wrong_order, "scrum-master", exp_plugin)["pass"], False)

    sm_tool_before = parse_rows(_make_stream([
        ("ideo-scrum:ideo-kernel", True, good_ideo_body),
        ("ideo-scrum:scrum-kernel", True, ""),
        ("ideo-scrum:sprint-kernel", True, ""),
        ("ideo-scrum:memory", True, good_mem_body),
    ], "ok", extra_tools_before=["Read"]))
    expect("Non-skill tool before memory fails", judge_role_order(sm_tool_before, "scrum-master", exp_plugin)["pass"], False)

    sm_skill_err = parse_rows(_make_stream([
        ("ideo-scrum:ideo-kernel", True, good_ideo_body),
        ("ideo-scrum:scrum-kernel", False, ""),
        ("ideo-scrum:sprint-kernel", True, ""),
        ("ideo-scrum:memory", True, good_mem_body),
    ], "ok"))
    expect("Failed Skill tool_result fails", judge_role_order(sm_skill_err, "scrum-master", exp_plugin)["pass"], False)

    sm_wrong_base = parse_rows(_make_stream([
        ("ideo-scrum:ideo-kernel", True, bad_cache_body),
        ("ideo-scrum:scrum-kernel", True, ""),
        ("ideo-scrum:sprint-kernel", True, ""),
        ("ideo-scrum:memory", True, good_mem_body),
    ], "ok"))
    expect("Stale Base directory fails", judge_role_order(sm_wrong_base, "scrum-master", exp_plugin)["pass"], False)

    sup_good = parse_rows(_make_stream([
        ("ideo-scrum:ideo-kernel", True, good_ideo_body),
        ("ideo-scrum:scrum-kernel", True, ""),
        ("ideo-scrum:memory", True, good_mem_body),
    ], "ready"))
    expect("Supporter 3-skill order passes", judge_role_order(sup_good, "supporter", exp_plugin)["pass"], True)

    # 2. Direct trigger & general negative
    q11_ok = parse_rows(_make_stream([("ideo-scrum:ideo-kernel", True, good_ideo_body)], "用五模式和 POV/HMW。"))
    expect("Q11 direct ideo-kernel passes", judge_direct_ideo(q11_ok, exp_plugin)["pass"], True)
    q11_bare = parse_rows(_make_stream([("ideo-kernel", True, good_ideo_body)], "ok"))
    expect("Prefix stripped on bare ideo-kernel", judge_direct_ideo(q11_bare, exp_plugin)["pass"], True)
    q11_miss = parse_rows(_make_stream([], "直接回答"))
    expect("Q11 missing ideo-kernel fails", judge_direct_ideo(q11_miss, exp_plugin)["pass"], False)

    g1_ok = parse_rows(_make_stream([], "Product Backlog 是产品级清单，Sprint Backlog 是本冲刺计划。"))
    expect("G1 no false trigger passes", judge_general_neg(g1_ok)["pass"], True)
    g1_bad = parse_rows(_make_stream([("ideo-scrum:scrum-kernel", True, "")], "ans"))
    expect("G1 false trigger scrum-kernel fails", judge_general_neg(g1_bad)["pass"], False)

    # 3. Affirmative vs negated obsolete-term detection
    obs_aff = scan_obsolete_terms("建议先开一个设计冲刺，并创建 DesignBacklog.md。")
    expect("Affirmative Chinese recommendation caught", obs_aff["ok"], False)
    expect("Affirmative count >= 2", len(obs_aff["affirmative_hits"]) >= 2, True)

    obs_clause_trap = scan_obsolete_terms("目前没有现成答案，建议开设计冲刺来验证。")
    expect("Clause trap ('没有现成答案，建议开设计冲刺') NOT falsely cleared", obs_clause_trap["ok"], False)

    obs_neg_zh = scan_obsolete_terms("本插件已移除设计冲刺，不要开 DesignBacklog.md，也没有 Designer 角色，无需走 design-kernel。")
    expect("Negated Chinese clarification passes", obs_neg_zh["ok"], True)
    expect("Negated Chinese records mentions for review", len(obs_neg_zh["negated_mentions"]) >= 3, True)

    obs_mixed = scan_obsolete_terms("已移除设计冲刺，但你仍然可以新建 DesignBacklog.md。")
    expect("Mixed negated + affirmative clause caught", obs_mixed["ok"], False)

    obs_neg_en = scan_obsolete_terms("IDEO-Scrum no longer uses a design sprint or DesignBacklog.md; use the IDEO five modes instead.")
    expect("Negated English clarification passes", obs_neg_en["ok"], True)

    obs_aff_en = scan_obsolete_terms("Start a design sprint and call /ideo-scrum:designer.")
    expect("Affirmative English recommendation caught", obs_aff_en["ok"], False)

    obs_dschool = scan_obsolete_terms("As a designer, observe users closely during Empathize.")
    expect("Lowercase d.school 'designer' not falsely flagged", obs_dschool["ok"] and len(obs_dschool["negated_mentions"]) == 0, True)

    # 4. Boundary B1 / B2 & SHA256 tampering check
    dev_skills = [
        ("ideo-scrum:ideo-kernel", True, good_ideo_body),
        ("ideo-scrum:scrum-kernel", True, ""),
        ("ideo-scrum:sprint-kernel", True, ""),
        ("ideo-scrum:memory", True, good_mem_body),
    ]
    b1_reply = (
        "已完成第 3 章方案计划与路线权衡（方案 A vs 方案 B），工作项表如下：\n\n"
        "| # | Work item | Output | Done when |\n| --- | --- | --- | --- |\n"
        "| 1 | Add tag sort | `src/app.py` | Tests pass |\n\n"
        "按规矩，我未修改 `src/app.py`，等待 PO 给出 go-ahead（放行）后再动手施工。"
    )
    b1_stream = parse_rows(_make_stream(dev_skills, b1_reply, mode="acceptEdits", tools=["Read", "Grep", "Glob", "Skill", "Write", "Edit"]))
    expect("B1 pass when app.py SHA256 unchanged", judge_boundary_b1(b1_stream, "aaa", "aaa", "", exp_plugin)["pass"], True)
    expect("B1 fail when app.py SHA256 tampered", judge_boundary_b1(b1_stream, "aaa", "bbb", "", exp_plugin)["behavior_pass"], False)
    b1_no_table = parse_rows(_make_stream(dev_skills, "我等待 PO 放行 go-ahead，未改代码。"))
    expect("B1 fail when work-item table missing", judge_boundary_b1(b1_no_table, "aaa", "aaa", "", exp_plugin)["content_pass"], False)

    b2_reply = "低保真原型只用于验证假设和学习，绝不放进正式交付的 Increment（不会修改 `src/app.py`）。我可以在独立草稿文件中演示两种交互。"
    b2_stream = parse_rows(_make_stream(dev_skills, b2_reply, mode="acceptEdits", tools=["Read", "Grep", "Glob", "Skill", "Write", "Edit"]))
    expect("B2 pass when app.py SHA256 unchanged and boundary explained", judge_boundary_b2(b2_stream, "aaa", "aaa", exp_plugin)["pass"], True)
    expect("B2 fail when app.py SHA256 tampered", judge_boundary_b2(b2_stream, "aaa", "ccc", exp_plugin)["behavior_pass"], False)

    # 5. Init constraints check
    expect("Init constraints pass for acceptEdits without Bash",
           check_init_constraints(b1_stream["init"], "acceptEdits", DISALLOWED_BOUNDARY.split(","))["ok"], True)
    bad_init = {"permissionMode": "bypassPermissions", "tools": ["Read", "Bash"]}
    expect("Init constraints catch bypassPermissions & Bash leak",
           check_init_constraints(bad_init, "dontAsk", DISALLOWED_READONLY.split(","))["ok"], False)

    # 6. Fixture creation + SHA256 check + git archive export of 0.8.0 + report rendering (no model name leak)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="s28-selftest-"))
    try:
        info = write_boundary_fixture(tmp / "p", "B1")
        expect("Fixture SHA256 matches app.py", info["app_sha256"], sha256_file(tmp / "p" / "src" / "app.py"))
        expect("Empty fixture SprintBacklog has no filled work table", has_filled_work_table(FIXTURE_SPRINT_B1), False)
        archived = export_plugin(tmp / "exp", DEFAULT_REF)
        pj = json.loads((archived / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        expect("Exported Commit A plugin version is 0.8.0", pj.get("version"), "0.8.0")
        expect("Exported Commit A plugin has no design-kernel or designer",
               not (archived / "skills" / "design-kernel").exists() and not (archived / "commands" / "designer.md").exists(), True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    rep = build_report([
        {"tag": "Q9-1", "id": "Q9", "group": "trig", "idx": 1, "status": "ok", "eval": {"behavior_pass": True, "content_pass": True, "obsolete": obs_neg_zh}},
    ])
    expect("Report separates Behavior and Content columns", ("行为栏" in rep and "内容栏" in rep), True)
    expect("Report labels magpie cheap model", "magpie 的便宜模型，非 Haiku" in rep, True)
    expect("Report surfaces negated mention for human review", "否定提及，人工复核" in rep, True)
    expect("Report omits supplemental section when no supplemental records", "补充试次汇总" not in rep, True)

    # 7. Supplemental PO ruling (2026-11-24): B1b & Q3-1b non-destructive isolation checks
    b1b_spec = SPEC_BY_ID["B1b"]
    q3_1b_spec = SPEC_BY_ID["Q3-1b"]
    expect("B1b tags do not collide with B1-1/B1-2",
           [resolve_trial_tag(b1b_spec, 1), resolve_trial_tag(b1b_spec, 2)], ["B1b-1", "B1b-2"])
    expect("B1b uses boundary mode and 420s timeout", is_boundary_spec(b1b_spec) and resolve_timeout_s(b1b_spec) == 420, True)
    expect("B1b clean prompt has no build/coding command",
           ("顺手改完" not in PROMPTS["B1b"]) and ("改代码" not in PROMPTS["B1b"]), True)
    expect("Q3-1b exact tag does not collide with Q3-1", resolve_trial_tag(q3_1b_spec, 1), "Q3-1b")
    expect("Q3-1b reuses original Q3 prompt and 420s timeout",
           (q3_1b_spec.get("prompt_id") == "Q3") and (not is_boundary_spec(q3_1b_spec)) and resolve_timeout_s(q3_1b_spec) == 420, True)
    expect("timeout_override overrides default timeout", resolve_timeout_s(SPEC_BY_ID["Q3"], 420), 420)
    tmp_b1b = pathlib.Path(tempfile.mkdtemp(prefix="s28-selftest-b1b-"))
    try:
        write_boundary_fixture(tmp_b1b / "p", "B1b")
        sb_b1b = (tmp_b1b / "p" / "scrum" / "sprint-01-demo" / "SprintBacklog.md").read_text(encoding="utf-8")
        expect("B1b fixture uses FIXTURE_SPRINT_B1 (How stage, awaiting go-ahead)",
               ("Now: How" in sb_b1b) and ("Still waiting for PO go-ahead" in sb_b1b), True)
    finally:
        shutil.rmtree(tmp_b1b, ignore_errors=True)
    rep_supp = build_report([
        {"tag": "B1b-1", "id": "B1b", "group": "supp", "idx": 1, "status": "ok", "eval": {"behavior_pass": True, "content_pass": True}},
        {"tag": "B1b-2", "id": "B1b", "group": "supp", "idx": 2, "status": "ok", "eval": {"behavior_pass": True, "content_pass": True}},
        {"tag": "Q3-1b", "id": "Q3-1b", "group": "supp", "idx": 1, "status": "ok", "eval": {"behavior_pass": True, "content_pass": True, "obsolete": {"ok": True, "affirmative_hits": [], "negated_mentions": []}}},
    ])
    expect("Report includes supplemental section when supplemental records exist",
           ("补充试次汇总" in rep_supp) and ("| `B1b` |" in rep_supp) and ("| `Q3-1b` |" in rep_supp), True)

    print(json.dumps({"selftest": "ok" if not failures else "FAILED", "cases": cases, "failures": failures}, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("selftest")

    sm = sub.add_parser("smoke")
    sm.add_argument("--out", default=str(DEFAULT_OUT))
    sm.add_argument("--ref", default=DEFAULT_REF)

    rn = sub.add_parser("run")
    rn.add_argument("--out", default=str(DEFAULT_OUT))
    rn.add_argument("--ref", default=DEFAULT_REF)
    rn.add_argument("--group", choices=("all", "trig", "roles", "bound", "supp"), default="all")
    rn.add_argument("--parallel", type=int, default=2)
    rn.add_argument("--skip-done", action="store_true")
    rn.add_argument("--only", default="")
    rn.add_argument("--timeout-override", type=int, default=None)
    rn.add_argument("--reuse-plugin", action="store_true")

    rp = sub.add_parser("report")
    rp.add_argument("--out", default=str(DEFAULT_OUT))

    args = ap.parse_args()
    if args.cmd == "selftest":
        return selftest()
    if args.cmd == "smoke":
        return cmd_smoke(args)
    if args.cmd == "run":
        return cmd_run(args)
    if args.cmd == "report":
        return cmd_report(args)
    return 1


if __name__ == "__main__":
    sys.exit(main())
