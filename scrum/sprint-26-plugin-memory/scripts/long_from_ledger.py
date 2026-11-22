"""Sprint 26 row 6: start a long Memory file from the ledger's verbatim text.

    python -X utf8 -I scripts/long_from_ledger.py NAME [--force]    write review/draft/long/NAME.md from SPEC[NAME]
    python -X utf8 -I scripts/long_from_ledger.py --selftest

A long file holds the old rules that a list line points at, word for word where the rule is the author's own and
nothing is gained by rewording. This script copies each rule's body from review/ledger.json (so nothing is retyped),
drops the "N. **Name** —" prefix, dedents the continuation lines, and turns the old cross-references ("convention 24",
"`../sprint-kernel/conventions/sprint-log.md`, convention 24") into placeholders like ‹sprint-log#24›, which
assemble_memory.py replaces with the handle(s) of that rule. The file is then edited by hand (it never overwrites an
edited one without --force). A reference to a rule that was deleted or not drafted stays a placeholder and is reported.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
import textwrap

HERE = pathlib.Path(__file__).resolve().parent
SPRINT = HERE.parent
LEDGER = SPRINT / "review" / "ledger.json"
OUT = SPRINT / "review" / "draft" / "long"

# name -> title, intro, sections [(heading, [refs]) ...]; a ref is "sprint-log#17" (a rule) or "overview@7" (a block, 1-based)
SPEC: dict[str, dict] = {
    "stage-gates": {
        "title": "Stage gates: the Product Owner decides between stages",
        "intro": "Read this file before you start a stage, return to one, or record a stage decision, in a Sprint or in a design. The list lines that point here are `stage-gates`, `sprint-stage-decisions`, `read-the-goal`, `design-gates` and `ideate-arrangement`.",
        "sections": [
            ("The rule, for both (`stage-gates`)", ["overview#12"]),
            ("In a Sprint (`sprint-stage-decisions`, `read-the-goal`)", ["sprint-log#24"]),
            ("In a design (`design-gates`, `ideate-arrangement`)", ["design-log#26"]),
        ],
    },
    "design-ending": {
        "title": "When a design ends",
        "intro": "Read this file when you end a design, decide what happens to its material, or hand its conclusions to a Sprint. The list lines that point here are `design-ends` and `design-conclusions`.",
        "sections": [("The rule", ["design-log#19"])],
    },
    "board-writing": {
        "title": "Writing the Scrum board",
        "intro": "This file is the brief for whoever writes the board page: what the board is, what it reads from the logs, the data it holds, what it leaves out, the steps to write it, and the check. Read it in full before you write or refresh `scrum/ScrumBoard.html`. The list lines that point here are `board-writer` and `board-rules`.",
        "sections": [
            ("What the board is and who writes it", ["board-log@2", "board-log#1", "board-log#2", "board-log#19", "board-log#3"]),
            ("What it reads", ["board-log#4", "board-log#5", "board-log#6"]),
            ("The data", ["board-log#11", "board-log#12", "board-log#13"]),
            ("What the page works out itself, and how cards link", ["board-log#9", "board-log#10", "board-log#8"]),
            ("What the board leaves out", ["board-log#16"]),
            ("How to write it", ["board-log#17", "board-log#18"]),
        ],
    },
    "sprint-stages": {
        "title": "The stages of a Sprint: the details",
        "intro": "The detail behind the Sprint lines that point here: opening, the How, the go-ahead, checkpoints, and the Test. Read it when you plan, build or test a Sprint. The list lines that point here are `sprint-folder`, `how-is-a-plan`, `go-ahead`, `checkpoints`, `reviewer-required` and `record-the-tests`.",
        "sections": [
            ("Opening a Sprint (`sprint-folder`)", ["sprint-log#1"]),
            ("How: a plan, not steps (`how-is-a-plan`, `no-steps`)", ["sprint-log#7"]),
            ("The go-ahead (`go-ahead`, `review-handover`)", ["sprint-log#8"]),
            ("Checkpoints (`checkpoints`)", ["sprint-log#10"]),
            ("Tests: criteria first (`tests-criteria-first`, `check-script-misses`)", ["sprint-log#13"]),
            ("A reviewer is required (`reviewer-required`)", ["sprint-log#14"]),
            ("Record the tests (`record-the-tests`)", ["sprint-log#16"]),
        ],
    },
    "design-stages": {
        "title": "The stages of a design: the details",
        "intro": "The detail behind the design lines that point here, stage by stage. Read it when you run a design sprint, together with the design-kernel skill's step files. The list lines that point here are `design-stages` and `isolated-sketches`.",
        "sections": [
            ("How these rules sit beside the book", ["design-log@2", "design-log@6"]),
            ("The three loops", ["design-log@4"]),
            ("Empathize: start from the people", ["design-log#6", "design-log#7"]),
            ("Define: map and questions in the log", ["design-log#8"]),
            ("Ideate: Lightning Demos (optional)", ["design-log#9"]),
            ("Ideate: isolated solutions (optional)", ["design-log#11"]),
            ("Prototype: just enough", ["design-log#16"]),
            ("Test: role cards", ["design-log#17"]),
        ],
    },
    "flow-maps": {
        "title": "The process maps",
        "intro": "The process maps of the six old convention files, with the lines (handles) that apply at each step written into the boxes, so each map is also an index. Read it to see where a rule sits in the flow.",
        "sections": [
            ("The whole flow", ["overview@5"]),
            ("The product log", ["product-log@4"]),
            ("A Sprint", ["sprint-log@4"]),
            ("A design", ["design-log@3"]),
            ("The five modes and the IDEO log", ["ideo-log@3"]),
            ("The board", ["board-log@3"]),
        ],
    },
    "sprint-closing": {
        "title": "Closing a Sprint",
        "intro": "Read this file when you close a Sprint: the Review, the Retrospective and the closing commit. The list lines that point here are `review-at-close`, `retro-in-memory` and `one-closing-commit`.",
        "sections": [
            ("Review (`review-at-close`)", ["sprint-log#17"]),
            ("Retrospective (`retro-in-memory`)", ["sprint-log#18"]),
            ("One closing commit (`one-closing-commit`)", ["sprint-log#19"]),
        ],
    },
}

NUMS = r"\d+(?:\s*[–-]\s*\d+)?(?:(?:\s*,\s*and\s+|\s*,\s*|\s+and\s+)\d+(?:\s*[–-]\s*\d+)?)*"
REF_FILE = re.compile(r"`(?:\.\./)?(?:[a-z-]+/)*([a-z-]+)\.md`,\s*conventions?\s+(" + NUMS + ")")
REF_NAMED = re.compile(r"\b(overview|product-log|sprint-log|design-log|ideo-log|board-log)\s+conventions?\s+(" + NUMS + ")")
REF_BARE = re.compile(r"\bconventions?\s+(" + NUMS + ")")
PREFIX = re.compile(r"^\d+\.\s+\*\*[^*]+\*\*\s*(?:—\s*)?")


def numbers(s: str) -> list[int]:
    out: list[int] = []
    for part in re.split(r",|\band\b", s):
        part = part.strip()
        m = re.fullmatch(r"(\d+)\s*[–-]\s*(\d+)", part)
        if m:
            out += list(range(int(m.group(1)), int(m.group(2)) + 1))
        elif part.isdigit():
            out.append(int(part))
    return out


def placeholders(short: str, nums: list[int]) -> str:
    return ", ".join(f"‹{short}#{n}›" for n in nums)


def convert(text: str, own: str) -> str:
    """Old cross-references -> ‹file#N› placeholders. A reference with no file is to the rule's own file."""
    text = REF_FILE.sub(lambda m: placeholders(m.group(1), numbers(m.group(2))), text)
    text = REF_NAMED.sub(lambda m: placeholders(m.group(1), numbers(m.group(2))), text)
    text = REF_BARE.sub(lambda m: placeholders(own, numbers(m.group(1))) if numbers(m.group(1)) else m.group(0), text)
    return text.replace("`steps/", "`design-kernel/steps/")


def body(rule: dict, own: str) -> str:
    lines = rule["text"].split("\n")
    first = PREFIX.sub("", lines[0]).strip()
    rest = lines[1:]
    ind = [len(x) - len(x.lstrip()) for x in rest if x.strip()]
    cut = min(ind) if ind else 0
    rest = [x[cut:] if x.strip() else "" for x in rest]
    txt = "\n".join(([first] if first else []) + rest).strip("\n")
    return convert(txt, own)


def build(name: str, ledger: dict) -> str:
    spec = SPEC[name]
    by_id = {r["id"]: (f["short"], r) for f in ledger["files"] for r in f["rules"]}
    out = [f"# {spec['title']}", "", spec["intro"], ""]
    for heading, refs in spec["sections"]:
        out += [f"## {heading}", ""]
        for ref in refs:
            if "@" in ref:
                short, n = ref.split("@")
                blk = next(f for f in ledger["files"] if f["short"] == short)["blocks"][int(n) - 1]
                out += [convert(blk["text"], short), ""]
            else:
                short, r = by_id[ref]
                out += [body(r, short), ""]
    out += ["## Open points for the Product Owner", "", "- (none yet)", ""]
    return "\n".join(out)


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    if not argv or argv[0] not in SPEC:
        print(__doc__)
        print("names:", sorted(SPEC))
        return 2
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    dest = OUT / f"{argv[0]}.md"
    if dest.exists() and "--force" not in argv:
        print(f"{dest.name} exists; use --force to replace it")
        return 1
    OUT.mkdir(parents=True, exist_ok=True)
    dest.write_text(build(argv[0], ledger), encoding="utf-8", newline="\n")
    print(f"wrote {dest}")
    return 0


def selftest() -> int:
    ok = True

    def check(cond: bool, what: str):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    check(numbers("13–14") == [13, 14] and numbers("19, 24, and 26") == [19, 24, 26] and numbers("7 and 8") == [7, 8], "number lists and ranges")
    check(convert("(`../sprint-kernel/conventions/sprint-log.md`, convention 24)", "overview") == "(‹sprint-log#24›)", "a reference with a path")
    check(convert("as convention 12 says", "overview") == "as ‹overview#12› says", "a bare reference is to the rule's own file")
    check(convert("(sprint-log convention 17)", "design-log") == "(‹sprint-log#17›)", "a named reference")
    check(convert("see `steps/3-3-decide.md`", "design-log") == "see `design-kernel/steps/3-3-decide.md`", "a steps path gets its skill")
    r = {"text": "3. **Three layers**\n\n   | A | B |\n   | - | - |\n   | 1 | 2 |"}
    check(body(r, "overview") == "| A | B |\n| - | - |\n| 1 | 2 |", "the prefix goes and the table is dedented")
    r = {"text": "9. **Name** — First sentence.\n    - a bullet\n    - another"}
    check(body(r, "x") == "First sentence.\n- a bullet\n- another", "the first line loses its prefix and bullets are dedented")
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
