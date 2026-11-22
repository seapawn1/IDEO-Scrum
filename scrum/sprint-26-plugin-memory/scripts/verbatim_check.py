"""Sprint 26: word-for-word checks. Nothing here uses the extractor's parser, so it checks the extractor too.

    python -X utf8 -I scripts/verbatim_check.py ledger              three rules per file (first, middle, last) against the source
    python -X utf8 -I scripts/verbatim_check.py ledger --all        every rule
    python -X utf8 -I scripts/verbatim_check.py contains DRAFT NEEDLES.json
                                                                   every string in NEEDLES.json (a list) occurs in DRAFT, character for character
    python -X utf8 -I scripts/verbatim_check.py --selftest          prove each check can fail

`ledger` re-reads each source file, cuts the lines the ledger names, and compares the result with the ledger's text.
The cut must start at `N. **` and must be followed by a line that cannot belong to the rule (blank + non-indented line,
heading, or end of file). `contains` is for the drafts: quotations from the books and the Product Owner's own words
must reach the Memory unchanged.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPRINT = HERE.parent
REPO = SPRINT.parents[1]
LEDGER = SPRINT / "review" / "ledger.json"
RULE = re.compile(r"^(\d+)\. \*\*")


def read_lines(path: Path) -> list[str]:
    lines = path.read_bytes().decode("utf-8").replace("\r\n", "\n").split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    return lines


def check_rule(lines: list[str], rule: dict) -> list[str]:
    a, b = rule["line_start"], rule["line_end"]
    errors = []
    cut = "\n".join(lines[a - 1 : b])
    if cut != rule["text"]:
        errors.append(f"{rule['id']}: the ledger text differs from lines {a}-{b} of the source")
    m = RULE.match(lines[a - 1])
    if not m or int(m.group(1)) != rule["number"]:
        errors.append(f"{rule['id']}: line {a} does not start rule {rule['number']}")
    if b < len(lines):
        nxt = lines[b]  # the line after the rule
        beyond = lines[b + 1] if b + 1 < len(lines) else ""
        ok = nxt.strip() == "" and not (beyond.startswith("   ")) or nxt.startswith("#") or RULE.match(nxt)
        if not ok:
            errors.append(f"{rule['id']}: the line after the rule (line {b + 1}) could belong to it: {nxt[:40]!r}")
    return errors


def pick(rules: list[dict], everything: bool) -> list[dict]:
    if everything or len(rules) <= 3:
        return rules
    return [rules[0], rules[len(rules) // 2], rules[-1]]


def run_ledger(everything: bool) -> int:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    errors, checked = [], 0
    for f in ledger["files"]:
        lines = read_lines(REPO / f["path"])
        for r in pick(f["rules"], everything):
            errors += check_rule(lines, r)
            checked += 1
    print(f"checked {checked} rules; {len(errors)} problems")
    for e in errors:
        print("  " + e)
    return 1 if errors else 0


def missing(draft: str, needles: list[str]) -> list[str]:
    return [n for n in needles if n not in draft]


def run_contains(draft_path: str, needles_path: str) -> int:
    draft = Path(draft_path).read_bytes().decode("utf-8").replace("\r\n", "\n")
    needles = json.loads(Path(needles_path).read_text(encoding="utf-8"))
    bad = missing(draft, needles)
    print(f"{len(needles)} strings; {len(bad)} missing")
    for n in bad:
        print("  missing: " + n[:90])
    return 1 if bad else 0


def selftest() -> int:
    ok = True

    def check(cond: bool, what: str):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    lines = ["# T", "", "1. **A** — one", "2. **B** — two", "    more of two", "", "## H", "3. **C** — three"]
    good = {"id": "t#2", "number": 2, "line_start": 4, "line_end": 5, "text": "2. **B** — two\n    more of two"}
    check(check_rule(lines, good) == [], "a correct cut passes")
    check(any("differs" in e for e in check_rule(lines, {**good, "text": "2. **B** — twx\n    more of two"})), "planted defect: one changed character is caught")
    check(any("differs" in e for e in check_rule(lines, {**good, "line_end": 4, "text": "2. **B** — two"})) is False, "a shorter cut with its own matching text is judged on its boundary instead")
    check(any("could belong" in e for e in check_rule(lines, {**good, "line_end": 4, "text": "2. **B** — two"})), "planted defect: a cut that stops before an indented line is caught")
    check(any("does not start" in e for e in check_rule(lines, {**good, "number": 9})), "planted defect: a wrong number is caught")
    check(missing("alpha beta", ["alpha", "beta"]) == [], "contains: all present")
    check(missing("alpha beta", ["alpha", "bet a"]) == ["bet a"], "planted defect: a changed quotation is caught")
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


def main() -> int:
    argv = sys.argv[1:]
    if "--selftest" in argv:
        return selftest()
    if argv[:1] == ["ledger"]:
        return run_ledger("--all" in argv)
    if argv[:1] == ["contains"] and len(argv) == 3:
        return run_contains(argv[1], argv[2])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
