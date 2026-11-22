"""Sprint 26, work item 1: pull every numbered convention out of the six convention files into a ledger.

    python -X utf8 -I scripts/extract_rules.py              write review/ledger.json and review/ledger.md
    python -X utf8 -I scripts/extract_rules.py --selftest   run the extractor on a small known sample and on planted defects

Run it from anywhere; the repository root is found from this file's place
(scrum/sprint-26-plugin-memory/scripts/). The six files are read as they are in the working copy; the ledger
records the commit and the blob of each file, so the old text stays pinned after the files are deleted (P3).

A "rule" is a line starting `N. **Name**` and everything after it that is blank or indented by three spaces or more.
Everything else that is not a heading is a "block" (quote, fenced diagram, table, paragraph). The coverage check
proves that every non-blank line of a file is a heading, part of one rule, or part of one block: no line lost or doubled.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPRINT = HERE.parent
REPO = SPRINT.parents[1]
REVIEW = SPRINT / "review"
SKILLS = "plugins/ideo-scrum/skills"

FILES = [
    ("overview", f"{SKILLS}/scrum-kernel/overview.md"),
    ("product-log", f"{SKILLS}/scrum-kernel/conventions/product-log.md"),
    ("board-log", f"{SKILLS}/scrum-kernel/conventions/board-log.md"),
    ("sprint-log", f"{SKILLS}/sprint-kernel/conventions/sprint-log.md"),
    ("design-log", f"{SKILLS}/design-kernel/conventions/design-log.md"),
    ("ideo-log", f"{SKILLS}/ideo-kernel/conventions/ideo-log.md"),
]
# The count is the independent check: `grep -c '^[0-9]*\. \*\*'` on each file gave these (sprint-26 How, row 1).
EXPECTED = {"overview": 17, "product-log": 18, "board-log": 19, "sprint-log": 26, "design-log": 27, "ideo-log": 4}

RULE = re.compile(r"^(\d+)\. \*\*(.+?)\*\*")
XREF = re.compile(r"conventions? \d+(?:[–-]\d+)?(?: and \d+)?")
QUOTED = re.compile(r'"[^"\n]{20,}"')
CJK = re.compile(r"[㐀-鿿]")


def indented(line: str) -> bool:
    return line.startswith("   ")  # three spaces or more: overview uses three, the others four


def parse(lines: list[str]) -> dict:
    """Split a file into headings, rules and blocks. Line numbers are 1-based and inclusive."""
    headings: list[dict] = []
    rules: list[dict] = []
    blocks: list[dict] = []
    h2 = h3 = ""
    rule: dict | None = None
    block: dict | None = None
    in_fence = False

    def close_rule():
        nonlocal rule
        if rule is not None:
            end = rule["line_end"]
            while end > rule["line_start"] and lines[end - 1].strip() == "":
                end -= 1
            rule["line_end"] = end
            rule["text"] = "\n".join(lines[rule["line_start"] - 1 : end])
            rules.append(rule)
            rule = None

    def close_block():
        nonlocal block
        if block is not None:
            block["text"] = "\n".join(lines[block["line_start"] - 1 : block["line_end"]])
            first = lines[block["line_start"] - 1]
            if first.startswith(">"):
                block["kind"] = "quote"
            elif first.startswith("```"):
                block["kind"] = "fence:" + (first[3:].strip() or "plain")
            elif first.startswith("|"):
                block["kind"] = "table"
            else:
                block["kind"] = "paragraph"
            block["heading"] = block.pop("_heading")
            blocks.append(block)
            block = None

    for no, line in enumerate(lines, 1):
        if in_fence:
            block["line_end"] = no
            if line.strip().startswith("```"):
                in_fence = False
                close_block()
            continue
        if line.startswith("```"):
            close_rule()
            close_block()
            block = {"line_start": no, "line_end": no, "_heading": f"{h2} / {h3}".strip(" /")}
            in_fence = True
            continue
        if line.startswith("#"):
            close_rule()
            close_block()
            if line.startswith("### "):
                h3 = line[4:].strip()
            elif line.startswith("## "):
                h2, h3 = line[3:].strip(), ""
            headings.append({"line": no, "text": line})
            continue
        m = RULE.match(line)
        if m:
            close_rule()
            close_block()
            rule = {
                "number": int(m.group(1)),
                "name": m.group(2),
                "heading": f"{h2} / {h3}".strip(" /"),
                "line_start": no,
                "line_end": no,
            }
            continue
        if rule is not None and (line.strip() == "" or indented(line)):
            rule["line_end"] = no
            continue
        if line.strip() == "":
            close_block()
            continue
        # a non-blank, non-indented line that is neither a heading nor a rule
        close_rule()
        if block is None:
            block = {"line_start": no, "line_end": no, "_heading": f"{h2} / {h3}".strip(" /")}
        else:
            block["line_end"] = no
    close_rule()
    close_block()
    return {"headings": headings, "rules": rules, "blocks": blocks}


def coverage_errors(lines: list[str], parsed: dict) -> list[str]:
    """Every non-blank line must be a heading, in one rule, or in one block: exactly once."""
    seen: dict[int, str] = {}
    errors: list[str] = []

    def mark(no: int, what: str):
        if no in seen:
            errors.append(f"line {no} is in both {seen[no]} and {what}")
        seen[no] = what

    for h in parsed["headings"]:
        mark(h["line"], "heading")
    for r in parsed["rules"]:
        for no in range(r["line_start"], r["line_end"] + 1):
            mark(no, f"rule {r['number']}")
    for b in parsed["blocks"]:
        for no in range(b["line_start"], b["line_end"] + 1):
            mark(no, f"block@{b['line_start']}")
    for no, line in enumerate(lines, 1):
        if line.strip() and no not in seen:
            errors.append(f"line {no} is in nothing: {line[:50]!r}")
    return errors


def number_errors(parsed: dict) -> list[str]:
    nums = [r["number"] for r in parsed["rules"]]
    return [] if nums == list(range(1, len(nums) + 1)) else [f"numbers are not 1..n: {nums}"]


def flags(text: str) -> list[str]:
    out = []
    if "*Supplement" in text:
        out.append("Supplement")
    if "*Decide on the spot" in text:
        out.append("Decide on the spot")
    if "*Departs from the book" in text or "This departs from" in text:
        out.append("Departs")
    if QUOTED.search(text):
        out.append("quote")
    if CJK.search(text):
        out.append("CJK")
    return out


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True, check=True).stdout.strip()


def build() -> dict:
    ledger = {"baseline_commit": git("rev-parse", "HEAD"), "files": []}
    for short, rel in FILES:
        raw = (REPO / rel).read_bytes()
        text = raw.decode("utf-8").replace("\r\n", "\n")
        lines = text.split("\n")
        if lines and lines[-1] == "":
            lines.pop()
        parsed = parse(lines)
        problems = coverage_errors(lines, parsed) + number_errors(parsed)
        if len(parsed["rules"]) != EXPECTED[short]:
            problems.append(f"{len(parsed['rules'])} rules, expected {EXPECTED[short]}")
        if problems:
            raise SystemExit(f"{rel}:\n  " + "\n  ".join(problems))
        for r in parsed["rules"]:
            r["id"] = f"{short}#{r['number']}"
            r["chars"] = len(r["text"])
            r["flags"] = flags(r["text"])
            r["xrefs"] = XREF.findall(r["text"])
        ledger["files"].append(
            {
                "short": short,
                "path": rel,
                "blob": git("rev-parse", f"HEAD:{rel}"),
                "sha1_text": hashlib.sha1(text.encode("utf-8")).hexdigest(),
                "lines": len(lines),
                "chars": len(text),
                **parsed,
            }
        )
    return ledger


def render_md(ledger: dict) -> str:
    n_rules = sum(len(f["rules"]) for f in ledger["files"])
    n_blocks = sum(len(f["blocks"]) for f in ledger["files"])
    out = [
        "# 台账：六份约定文件的编号规矩（Sprint 26 行 1）",
        "",
        f"由 `scripts/extract_rules.py` 生成；基线提交 `{ledger['baseline_commit'][:7]}`。合计 **{n_rules}** 条编号规矩、**{n_blocks}** 个非编号块。",
        "覆盖检查：每个文件的每个非空行恰属于「标题」「一条规矩」「一个非编号块」之一，没有丢行、没有重复；编号连续；条数与 `grep` 一致。",
        "旧条的完整原文在 `ledger.json`（逐字），不抄进这里。",
        "",
        "| 文件 | 条数 | 非编号块 | 行数 | 字符 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for f in ledger["files"]:
        out.append(f"| `{f['path'].split('skills/')[1]}` | {len(f['rules'])} | {len(f['blocks'])} | {f['lines']} | {f['chars']:,} |")
    for f in ledger["files"]:
        out += ["", f"## {f['short']}（{len(f['rules'])} 条）", "", f"`{f['path']}` · blob `{f['blob'][:10]}`", ""]
        out += ["| id | 名称 | 所在节 | 行 | 字符 | 标记 | 引用其他约定 |", "| --- | --- | --- | --- | --- | --- | --- |"]
        for r in f["rules"]:
            name = r["name"].replace("|", "\\|")
            out.append(
                f"| {r['id']} | {name} | {r['heading']} | {r['line_start']}–{r['line_end']} | {r['chars']} | "
                f"{'、'.join(r['flags']) or '—'} | {len(r['xrefs'])} |"
            )
        out += ["", f"非编号块（{len(f['blocks'])} 个）：", "", "| 种类 | 行 | 所在节 | 首行 |", "| --- | --- | --- | --- |"]
        for b in f["blocks"]:
            first = b["text"].split("\n")[0].replace("|", "\\|")[:70]
            out.append(f"| {b['kind']} | {b['line_start']}–{b['line_end']} | {b['heading'] or '（文件头）'} | {first} |")
    return "\n".join(out) + "\n"


SAMPLE = """# Title

> note

Intro paragraph.

```mermaid
flowchart TD
    A --> B
```

## Part

1. **First** — Text one.
2. **Second** — Text two.

    | a | b |
    | --- | --- |
    | 1 | 2 |

    More of rule two.
3. **Third** — "A quoted passage that is long enough to count".

## Other

Loose paragraph.
"""


def selftest() -> int:
    lines = SAMPLE.split("\n")[:-1]
    parsed = parse(lines)
    ok = True

    def check(cond: bool, what: str):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    check([r["number"] for r in parsed["rules"]] == [1, 2, 3], "three rules, numbered 1..3")
    check(coverage_errors(lines, parsed) == [], "known sample: coverage clean")
    two = parsed["rules"][1]
    check(two["text"].count("\n") == 6 and two["text"].endswith("More of rule two."), "rule 2 keeps its indented table and paragraph, drops the trailing blank")
    check([b["kind"] for b in parsed["blocks"]] == ["quote", "paragraph", "fence:mermaid", "paragraph"], "blocks: quote, paragraph, diagram, paragraph")
    check("quote" in flags(parsed["rules"][2]["text"]), "a long quoted passage is flagged")
    check(flags(parsed["rules"][0]["text"]) == [], "a plain rule has no flag")
    # planted defects: the coverage check must catch each one
    broken = {k: (list(v) if isinstance(v, list) else v) for k, v in parsed.items()}
    broken["rules"] = [dict(r) for r in parsed["rules"]]
    broken["rules"][1]["line_end"] -= 2  # cut two lines off rule 2
    check(any("in nothing" in e for e in coverage_errors(lines, broken)), "planted defect: a line cut off a rule is reported")
    broken2 = {k: (list(v) if isinstance(v, list) else v) for k, v in parsed.items()}
    broken2["rules"] = [dict(r) for r in parsed["rules"]]
    broken2["rules"][0]["line_end"] += 1  # rule 1 reaches into rule 2
    check(any("in both" in e for e in coverage_errors(lines, broken2)), "planted defect: a line in two rules is reported")
    skipped = parse([l for l in lines if "Second" not in l])
    check(number_errors(skipped) != [], "planted defect: a missing number is reported")
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    ledger = build()
    REVIEW.mkdir(exist_ok=True)
    (REVIEW / "ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    (REVIEW / "ledger.md").write_text(render_md(ledger), encoding="utf-8", newline="\n")
    print("rules:", {f["short"]: len(f["rules"]) for f in ledger["files"]}, "total", sum(len(f["rules"]) for f in ledger["files"]))
    print("blocks:", {f["short"]: len(f["blocks"]) for f in ledger["files"]})
    return 0


if __name__ == "__main__":
    sys.exit(main())
