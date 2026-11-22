"""Sprint 26, rows 6-8: check the drafters' files and count what the list would weigh.

    python -X utf8 -I scripts/check_drafts.py check [--dir DIR]     schema, coverage, handles, format, merges
    python -X utf8 -I scripts/check_drafts.py stats [--dir DIR]     lines, characters, by section, by role tag, long files
    python -X utf8 -I scripts/check_drafts.py lines [--dir DIR]     print the list as it would stand (section by section)
    python -X utf8 -I scripts/check_drafts.py --selftest

The drafters (a workflow run outside the session, scripts/draft_rules.wf.js) write to
S:/IDEO-Scrum-Archives/sprint-26-plugin-memory/draft/<chunk>.json. Nothing here judges whether a line says the right
thing: that is for me, Master and the PO, one line at a time. This only catches what a script can.
"""
from __future__ import annotations

import glob
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).resolve().parent
SPRINT = HERE.parent
ANN = SPRINT / "review" / "annotations"
LEDGER = SPRINT / "review" / "ledger.json"
DEFAULT_DIR = SPRINT / "review" / "draft"  # my own drafts are committed with the log; the cheap drafters' (if any) went to the archive

SECTIONS = ["roles", "product-log", "sprint", "design", "ideo", "board", "meta"]
ROLES = {"dev", "sm", "des", "stk", "po"}
LONG_FILES = {"roles-and-routing", "stage-gates", "goal-fixed", "layers-and-folders", "sprint-closing", "sprint-refinement",
              "design-ending", "design-stages", "board-writing", "departures", "names", "product-log-details",
              "ideo-ending", "handoff", "sprint-stages", "flow-maps"}
REQUIRED = ["id", "line", "lines", "section", "long_file", "merged_into", "adds_to_target", "absorbed", "where_else", "note"]
LINE = re.compile(r"^- \*\*([a-z0-9]+(?:-[a-z0-9]+){0,4})\*\*(?: \[([a-z,]+)\])? (.+)$")
CJK = re.compile(r"[㐀-鿿　-〿＀-￯]")
LIMIT_SOFT, LIMIT_HARD = 130, 150


def ledger_ids() -> list[str]:
    led = json.loads(LEDGER.read_text(encoding="utf-8"))
    return [r["id"] for f in led["files"] for r in f["rules"]]


def block_ids() -> list[str]:
    """The non-numbered blocks of the six files (quotes, paragraphs, diagrams, the Departures table): `overview@5` is the
    fifth block of overview.md. Each needs a decision: a line, a long file that carries it, or where it went / why it goes."""
    led = json.loads(LEDGER.read_text(encoding="utf-8"))
    return [f"{f['short']}@{k}" for f in led["files"] for k in range(1, len(f["blocks"]) + 1)]


def annotations() -> dict[str, dict]:
    out = {}
    for p in sorted(ANN.glob("*.json")):
        for o in json.loads(p.read_text(encoding="utf-8")):
            out[o["id"]] = o
    return out


def line_problems(line: str) -> list[str]:
    errs = []
    m = LINE.match(line)
    if not m:
        return [f"not '- **handle** [roles] text': {line[:60]!r}"]
    handle, roles, rest = m.groups()
    if roles and not set(roles.split(",")) <= ROLES:
        errs.append(f"{handle}: roles {roles!r} not in {sorted(ROLES)}")
    if CJK.search(line):
        errs.append(f"{handle}: the line has Chinese characters (Memory lines are English)")
    if re.search(r"convention\s+\d|conventions\s+\d|\bsee .*\.md\b", line, re.I):
        errs.append(f"{handle}: refers to a convention number or a file instead of a handle or long/ file")
    for lf in re.findall(r"long/([A-Za-z0-9_-]+)\.md", line):
        if lf not in LONG_FILES:
            errs.append(f"{handle}: long file {lf!r} is not in the list")
    if len(line) > LIMIT_HARD:
        errs.append(f"{handle}: {len(line)} characters (limit {LIMIT_HARD})")
    return errs


def load(d: pathlib.Path) -> tuple[dict[str, dict], list[str]]:
    problems, rows = [], {}
    files = sorted(glob.glob(str(d / "*.json")))
    if not files:
        problems.append(f"no draft files in {d}")
    for fp in files:
        name = pathlib.Path(fp).name
        try:
            data = json.loads(pathlib.Path(fp).read_text(encoding="utf-8"))
        except ValueError as e:
            problems.append(f"{name}: not valid JSON ({e})")
            continue
        for o in data if isinstance(data, list) else []:
            if not isinstance(o, dict) or "id" not in o:
                problems.append(f"{name}: an item without id")
                continue
            if o["id"] in rows:
                problems.append(f"{o['id']}: drafted twice ({name})")
            rows[o["id"]] = {**o, "_file": name}
    return rows, problems


def run_check(d: pathlib.Path, complete: bool = True) -> int:
    rows, problems = load(d)
    ann = annotations()
    ids = ledger_ids()
    handles: dict[str, str] = {}
    via_needs: list[tuple[str, str]] = []
    blocks = set(block_ids())
    for i, o in rows.items():
        if "@" in i:  # a non-numbered block: no annotation; it needs a line, or where_else saying where it went or why it goes
            if i not in blocks:
                problems.append(f"{i}: not a block in the ledger")
                continue
            miss = [k for k in REQUIRED if k not in o]
            if miss:
                problems.append(f"{i}: missing fields {miss}")
                continue
            bl = [o["line"]] if o["line"] else (o["lines"] or [])
            if not bl and not o["where_else"]:
                problems.append(f"{i}: a block with no line needs where_else (where it went, or why it is dropped)")
            if bl and o["section"] not in SECTIONS:
                problems.append(f"{i}: section {o['section']!r} not in {SECTIONS}")
            for ln in bl:
                for e in line_problems(ln):
                    problems.append(f"{i}: {e}")
                m = LINE.match(ln)
                if m:
                    if m.group(1) in handles:
                        problems.append(f"{i}: handle {m.group(1)} is also used by {handles[m.group(1)]}")
                    handles[m.group(1)] = i
            continue
        if i not in ann:
            problems.append(f"{i}: not in the ledger")
            continue
        miss = [k for k in REQUIRED if k not in o]
        if miss:
            problems.append(f"{i}: missing fields {miss}")
            continue
        lines = [o["line"]] if o["line"] else (o["lines"] or [])
        if o["line"] and o["lines"]:
            problems.append(f"{i}: both line and lines are set")
        rec = ann[i]["recommend"]
        if rec in ("留", "改") and not lines:
            # a rule that lives only in a long file has no line of its own; the list line that points at it is `via`
            if o.get("via") and o.get("long_file"):
                via_needs.append((i, o["via"]))
            else:
                problems.append(f"{i}: recommend {rec} but no line (a rule kept only in a long file needs `via` and `long_file`)")
        if rec == "并":
            if lines:
                problems.append(f"{i}: recommend 并 but a line was written")
            if not o["merged_into"] or o["merged_into"] not in ann:
                problems.append(f"{i}: 并 needs merged_into a ledger id")
            if not o["adds_to_target"]:
                problems.append(f"{i}: 并 needs adds_to_target")
        if rec == "删":
            if lines:
                problems.append(f"{i}: recommend 删 but a line was written")
            if not o["where_else"]:
                problems.append(f"{i}: 删 needs where_else (or '无' with a note)")
        if o["section"] not in SECTIONS and lines:
            problems.append(f"{i}: section {o['section']!r} not in {SECTIONS}")
        if o["long_file"] and not str(o["long_file"]).startswith("NEW:") and o["long_file"] not in LONG_FILES:
            problems.append(f"{i}: long_file {o['long_file']!r} is not in the list (use NEW:<name>)")
        for ln in lines:
            for e in line_problems(ln):
                problems.append(f"{i}: {e}")
            m = LINE.match(ln)
            if m:
                h = m.group(1)
                if h in handles:
                    problems.append(f"{i}: handle {h} is also used by {handles[h]}")
                handles[h] = i
    for i, h in via_needs:
        if h not in handles:
            problems.append(f"{i}: via {h!r} is not the handle of any drafted line")
    if complete:
        problems += [f"{i}: not drafted" for i in ids + sorted(blocks) if i not in rows]
    # a rule that absorbs others must name them, and every 并 must be absorbed by its target
    for i, o in rows.items():
        t = o.get("merged_into")
        if t and t in rows and i not in (rows[t].get("absorbed") or []):
            problems.append(f"{i} merges into {t}, but {t} does not list it in absorbed")
    print(f"{len(rows)} rules drafted; {len(handles)} distinct handles; {len(problems)} problems")
    for p in problems:
        print("  " + p)
    return 1 if problems else 0


def run_stats(d: pathlib.Path) -> int:
    rows, _ = load(d)
    sec, roles, longs = Counter(), Counter(), Counter()
    total = n = long_idx = 0
    soft = 0
    for o in rows.values():
        lines = [o["line"]] if o.get("line") else (o.get("lines") or [])
        for ln in lines:
            n += 1
            total += len(ln) + 1
            sec[o.get("section")] += len(ln) + 1
            m = LINE.match(ln)
            roles[(m.group(2) if m and m.group(2) else "all")] += 1
            if "long/" in ln:
                long_idx += 1
            if len(ln) > LIMIT_SOFT:
                soft += 1
        if o.get("long_file"):
            longs[o["long_file"]] += 1
    print(f"{n} lines, {total} characters (the proposed budget is 8,000; the hook hard limit is 10,000); {long_idx} index lines; {soft} lines over {LIMIT_SOFT}")
    print("characters by section:", dict(sec))
    print("lines by role tag:", dict(roles))
    print("long files named:", dict(longs))
    return 0


def run_lines(d: pathlib.Path) -> int:
    rows, _ = load(d)
    by = defaultdict(list)
    for i in sorted(rows, key=lambda s: (s.replace("@", "#").rsplit("#", 1)[0], int(s.replace("@", "#").rsplit("#", 1)[1]) + (1000 if "@" in s else 0))):
        o = rows[i]
        for ln in ([o["line"]] if o.get("line") else (o.get("lines") or [])):
            by[o.get("section")].append((i, ln))
    for s in SECTIONS:
        print(f"\n## {s}")
        for i, ln in by.get(s, []):
            print(f"{ln}    <{i}>")
    return 0


def selftest() -> int:
    ok = True

    def check(cond: bool, what: str):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    check(line_problems("- **go-ahead** [dev,sm] Build only after the PO's go-ahead.") == [], "a good line passes")
    check(line_problems("- **ask-the-po** Ask the Product Owner when unsure.") == [], "a line without roles passes")
    check(any("not '- **handle**" in e for e in line_problems("Ask the PO.")), "planted defect: no handle")
    check(any("roles" in e for e in line_problems("- **x-y** [boss] Do it.")), "planted defect: an unknown role")
    check(any("Chinese" in e for e in line_problems("- **x-y** 先问 PO。")), "planted defect: Chinese in a line")
    check(any("convention" in e for e in line_problems("- **x-y** Do it, see convention 24.")), "planted defect: a convention number")
    check(any("not in the list" in e for e in line_problems("- **x-y** Do it. → long/made-up.md")), "planted defect: an unknown long file")
    check(any("characters" in e for e in line_problems("- **x-y** " + "a" * 230)), "planted defect: a line over the hard limit")
    check(line_problems("- **stage-gates** Wait for the PO. → long/stage-gates.md") == [], "a known long file passes")
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    d = DEFAULT_DIR
    if "--dir" in argv:
        i = argv.index("--dir")
        d = pathlib.Path(argv[i + 1])
        argv = argv[:i] + argv[i + 2 :]
    if "--selftest" in argv:
        return selftest()
    if argv[:1] == ["check"]:
        return run_check(d, complete="--partial" not in argv)
    if argv[:1] == ["stats"]:
        return run_stats(d)
    if argv[:1] == ["lines"]:
        return run_lines(d)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
