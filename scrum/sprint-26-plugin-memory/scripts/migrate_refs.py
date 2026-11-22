"""Sprint 26 row 13: move the references to the old conventions to the Memory, by rule, so a person reviews diffs and not a hunt.

    python -X utf8 -I scripts/migrate_refs.py                   dry run: per file, the lines that would change, and what is left over
    python -X utf8 -I scripts/migrate_refs.py --apply           write the changed files
    python -X utf8 -I scripts/migrate_refs.py --file PATH ...   only these files (a path suffix)
    python -X utf8 -I scripts/migrate_refs.py --left            list every reference that no rule handles (the part done by hand)
    python -X utf8 -I scripts/migrate_refs.py --selftest

A reference to an old rule becomes "Memory `handle`" (the handles the rule lives under now: scripts/assemble_memory.py's
mapping, with a few corrections for numbers that were cited for their meaning, below). Four shapes are handled:
  A  path or name, then the number    (`overview.md`, convention 12) / (sprint log, convention 14) / `../x/sprint-log.md`, conventions 22 and 24
  B  number, then the path            convention 26 in `../skills/design-kernel/conventions/design-log.md` / convention 17 of `overview.md`
  L  a Markdown link to an old file   [sprint-log](../plugins/.../sprint-log.md), convention 10  ->  [Memory](.../memory/SKILL.md) `handle`
  C  a bare number, by the file it sits in (a template or a kernel's SKILL.md names its own old convention file)
A path with no number, a heading, and prose that describes the old files are left for a person (--left).
"""
from __future__ import annotations

import difflib
import os
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import assemble_memory as am  # noqa: E402
import check_drafts as cd  # noqa: E402
import refs_inventory as ri  # noqa: E402

REPO = ri.REPO
MEMORY_SKILL = REPO / "plugins" / "ideo-scrum" / "skills" / "memory" / "SKILL.md"
SKIP = {"CHANGELOG.md"}  # the release history: its old entries describe what the files said then
CODE = {"scripts/check_docs.py", "scripts/board_check/check.py", "scripts/check_dsh.mjs", "plugins/ideo-scrum/hooks/commitments.sh"}  # comments and checks in code: by hand
SHORT = {"overview": "overview", "product-log": "product-log", "sprint-log": "sprint-log", "design-log": "design-log", "ideo-log": "ideo-log",
         "sprint log": "sprint-log", "product log": "product-log", "design log": "design-log", "ideo log": "ideo-log"}
# a bare "convention N" in these files means a rule of this old file
HOST = {
    "plugins/ideo-scrum/template/sprint-backlog-template.md": "sprint-log",
    "plugins/ideo-scrum/template/design-backlog-template.md": "design-log",
    "plugins/ideo-scrum/template/ideo-backlog-template.md": "ideo-log",
    "plugins/ideo-scrum/template/product-backlog-template.md": "product-log",
    "plugins/ideo-scrum/skills/design-kernel/SKILL.md": "design-log",
    "plugins/ideo-scrum/skills/sprint-kernel/SKILL.md": "sprint-log",
    "plugins/ideo-scrum/skills/ideo-kernel/SKILL.md": "ideo-log",
    "plugins/ideo-scrum/commands/designer.md": "design-log",
    "plugins/ideo-scrum/commands/developer.md": "sprint-log",
}
# numbers cited for their meaning: the handles that carry it now (assemble_memory.handles_for gives only the rule's own lines)
FIX = {
    "sprint-log#24": ["stage-gates", "read-the-goal"],   # gates between stages in a Sprint
    "design-log#26": ["stage-gates"],  # gates between stages in a design (the Ideate gate has its own line, ideate-arrangement)
    "sprint-log#25": ["ask-the-po"],
    "design-log#21": ["ask-the-po"],
    "design-log#24": ["log-is-the-handoff"],
    "ideo-log#2": ["sprint-or-modes"],            # how a design sprint and the five modes differ
    "overview#17": ["goal-fixed", "commitment-table"],  # "Goal fixed, plan flexible"
    "sprint-log#20": ["goal-fixed"],
}

NUMS = r"(?P<nums>\d+(?:\s*(?:[–-]|to)\s*\d+)?(?:\s*(?:,|and also|and)\s*\d+(?:\s*(?:[–-]|to)\s*\d+)?)*)"
FILEPAT = r"(?P<f>overview|product-log|sprint-log|design-log|ideo-log)\.md"
NAMEPAT = r"(?P<n>overview|sprint[ -]log|product[ -]log|design[ -]log|ideo[ -]log)"
FOLDER = r"(?:\s+in\s+the\s+[\w-]+\s+skill(?:'s|’s)?\s+folder)?"
RE_LINK = re.compile(r"\[(?P<label>[^\]]*)\]\((?P<url>[^)\s]*?" + FILEPAT + r")(?P<anchor>#[^)\s]*)?\)(?:\s*,\s*conventions?\s+" + NUMS + r")?")
RE_A = re.compile(r"(?:`?[\w./-]*?" + FILEPAT + r"`?|(?<![\w`-])" + NAMEPAT + r")" + FOLDER + r"\s*,?\s*conventions?\s+" + NUMS)
RE_B = re.compile(r"conventions?\s+" + NUMS + r"\s+(?:in|of)\s+`?[\w./-]*?" + FILEPAT + r"`?")
RE_C = re.compile(r"\bconventions?\s+" + NUMS, re.I)


def rows() -> dict[str, dict]:
    r, _ = cd.load(cd.DEFAULT_DIR)
    return r


def handles(rows_: dict[str, dict], short: str, spec: str) -> list[str]:
    out: list[str] = []
    short = short.replace(" ", "-")
    for n in ri.numbers(re.sub(r"\s+to\s+", "-", spec)):
        rid = f"{short}#{n}"
        for h in FIX.get(rid) or am.handles_for(rows_, rid):
            if h not in out:
                out.append(h)
    return out


def memory(hs: list[str]) -> str:
    return "Memory " + ", ".join(f"`{h}`" for h in hs) if hs else "Memory `?`"


def migrate_line(rel: str, line: str, rows_: dict[str, dict]) -> str:
    def link(m: re.Match) -> str:
        if not m.group("nums"):
            return m.group(0)  # a link with no number: a person says which lines it is about
        url = os.path.relpath(MEMORY_SKILL, (REPO / rel).parent).replace("\\", "/")
        return f"[Memory]({url}) " + ", ".join(f"`{h}`" for h in handles(rows_, SHORT[m.group("f")], m.group("nums")))

    line = RE_LINK.sub(link, line)
    line = RE_A.sub(lambda m: memory(handles(rows_, SHORT.get(m.group("f") or m.group("n"), (m.group("f") or m.group("n")).replace(" ", "-")), m.group("nums"))), line)
    line = RE_B.sub(lambda m: memory(handles(rows_, SHORT[m.group("f")], m.group("nums"))), line)
    host = HOST.get(rel)
    if host:
        line = RE_C.sub(lambda m: memory(handles(rows_, host, m.group("nums"))), line)
    return line


def targets(only: list[str]) -> list[pathlib.Path]:
    out = []
    for p in ri.files():
        rel = p.relative_to(REPO).as_posix()
        if rel in SKIP or rel in CODE or rel.startswith("plugins/ideo-scrum/skills/memory/") or rel.startswith("scrum/"):
            continue
        if only and not any(rel.endswith(o) for o in only):
            continue
        out.append(p)
    return out


def left_in(rel: str, text: str) -> list[tuple[int, str]]:
    out = []
    for no, line in enumerate(text.split("\n"), 1):
        if ri.scan_line(rel, no, line) or "Memory `?`" in line:
            out.append((no, line.strip()))
    return out


def run(argv: list[str]) -> int:
    only = [argv[i + 1] for i, a in enumerate(argv) if a == "--file"]
    rows_ = rows()
    changed_total = left_total = 0
    for p in targets(only):
        rel = p.relative_to(REPO).as_posix()
        text = p.read_text(encoding="utf-8")
        lines = text.split("\n")
        new = [migrate_line(rel, ln, rows_) for ln in lines]
        diff = [(i + 1, a, b) for i, (a, b) in enumerate(zip(lines, new)) if a != b]
        new_text = "\n".join(new)
        left = left_in(rel, new_text)
        if not diff and not left:
            continue
        changed_total += len(diff)
        left_total += len(left)
        if "--left" in argv:
            for no, ln in left:
                print(f"{rel}:{no}: {ln[:230]}")
            continue
        print(f"=== {rel}: {len(diff)} lines change, {len(left)} lines still carry a reference")
        if "--quiet" not in argv:
            for no, a, b in diff:
                print(f"  {no}: - {a.strip()[:260]}\n  {no}: + {b.strip()[:260]}")
        if "--apply" in argv and diff:
            p.write_text(new_text, encoding="utf-8", newline="\n")
    print(f"{changed_total} lines change; {left_total} lines still carry a reference (by hand)")
    return 0


def selftest() -> int:
    ok = True

    def check(cond: bool, what: str) -> None:
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    r = rows()
    t = migrate_line("plugins/ideo-scrum/commands/developer.md", "(`overview.md`, convention 12) and (`../skills/sprint-kernel/conventions/sprint-log.md`, conventions 22 and 24)", r)
    check(t == "(Memory `stage-gates`) and (Memory `log-is-the-handoff`, `stage-gates`, `read-the-goal`)", f"shape A: {t}")
    t = migrate_line("x.md", "wait for permission under convention 26 in `../skills/design-kernel/conventions/design-log.md` first", r)
    check(t == "wait for permission under Memory `stage-gates` first", f"shape B: {t}")
    t = migrate_line("docs/glossary.md", "| [sprint-log](../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md), convention 10 |", r)
    check(t == "| [Memory](../plugins/ideo-scrum/skills/memory/SKILL.md) `checkpoints` |", f"shape L: {t}")
    t = migrate_line("plugins/ideo-scrum/template/design-backlog-template.md", "(conventions 16 and 19)", r)
    check(t == "(Memory `design-stages`, `design-ends`, `design-conclusions`)", f"shape C: {t}")
    t = migrate_line("docs/quick-start.md", "(overview, convention 17) and (sprint log, convention 14)", r)
    check(t == "(Memory `goal-fixed`, `commitment-table`) and (Memory `reviewer-required`)", f"names: {t}")
    t = migrate_line("README.md", "[Departures](plugins/ideo-scrum/skills/scrum-kernel/overview.md#departures-from-the-official-guides)", r)
    check(t.endswith("overview.md#departures-from-the-official-guides)"), "a link with no number is left")
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else run(sys.argv[1:]))
