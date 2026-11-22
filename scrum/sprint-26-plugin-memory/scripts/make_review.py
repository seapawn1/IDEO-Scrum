"""Sprint 26 row 9: write the review documents the PO reads, one per old convention file.

    python -X utf8 -I scripts/make_review.py [--draft DIR] [--out DIR]
    python -X utf8 -I scripts/make_review.py --selftest

For each old rule: its text word for word, its source and basis, what the checks said and what I recommend, and the new
line (or where it went). Reads review/ledger.json, review/annotations/*.json and review/draft/*.json; writes
review/review-<file>.md. Nothing here is judged: it only puts what is already recorded side by side, so the PO can read
a rule, its reason and its new line in one place.
"""
from __future__ import annotations

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_drafts as cd  # noqa: E402

SPRINT = HERE.parent
LEDGER = SPRINT / "review" / "ledger.json"
OUT = SPRINT / "review"
FILE_TITLES = {
    "overview": "overview.md（scrum-kernel）",
    "product-log": "product-log.md（scrum-kernel）",
    "board-log": "board-log.md（scrum-kernel）",
    "sprint-log": "sprint-log.md（sprint-kernel）",
    "design-log": "design-log.md（design-kernel）",
    "ideo-log": "ideo-log.md（ideo-kernel）",
}
HOME = {"清单": "清单（一行）", "长文件": "长文件", "不进 Memory": "不进 Memory"}


def quote(text: str) -> list[str]:
    return ["> " + ln if ln.strip() else ">" for ln in text.split("\n")]


def new_part(o: dict | None) -> list[str]:
    if not o:
        return ["**新**：（还没起草）"]
    lines = [o["line"]] if o.get("line") else (o.get("lines") or [])
    out: list[str] = []
    if lines:
        out += ["**新行**" + (f"（长文件 `{o['long_file']}`）" if o.get("long_file") else ""), "", "```text", *lines, "```"]
    elif o.get("via"):
        out += [f"**新**：只在长文件 `{o.get('long_file')}`，清单里由 `{o['via']}` 一行索引。"]
    elif o.get("merged_into"):
        out += [f"**新**：并入 `{o['merged_into']}`。这条独有、要带过去的内容：{o.get('adds_to_target') or '（未写）'}"]
    else:
        out += [f"**新**：不进清单。去处或不要的理由：{o.get('where_else') or '（未写）'}"]
    if o.get("where_else") and (lines or o.get("via") or o.get("merged_into")):
        out += ["", f"**别处已有**：{o['where_else']}"]
    if o.get("note"):
        out += ["", f"**备注**：{o['note']}"]
    return out


def rule_block(f: dict, r: dict, a: dict | None, o: dict | None) -> list[str]:
    out = [f"### {r['id']} · {r['name']}", "", f"`{f['path']}` 第 {r['line_start']}–{r['line_end']} 行" + (f" · 标记：{'、'.join(r['flags'])}" if r["flags"] else ""), "", "**旧规矩原文**", "", *quote(r["text"]), ""]
    if a:
        out += [f"**出处与依据**：{a['source']}（把握：{a['confidence']}）；种类：{a['kind']}"]
        out += [f"- {b}" for b in a.get("basis") or []]
        merge = f" → {a['merge_into']}" if a.get("merge_into") else ""
        out += ["", f"**建议**：{a['recommend']}{merge}；去处：{HOME.get(a['home'], a['home'])}", "", f"**理由**：{a['reason']}"]
        if a.get("dups"):
            out += ["", "**与它重复或相邻**：" + "、".join(a["dups"])]
    out += ["", *new_part(o), "", "---", ""]
    return out


def build(f: dict, ann: dict, rows: dict) -> str:
    recs = {}
    for r in f["rules"]:
        recs[ann[r["id"]]["recommend"]] = recs.get(ann[r["id"]]["recommend"], 0) + 1
    out = [f"# 审阅：{FILE_TITLES[f['short']]}", "",
           "每条旧规矩一节：先是原文（逐字），再是出处与依据、核验后的建议与理由，最后是它现在的样子（清单里的一行，或并到哪、删在哪）。",
           "读法：只看「旧规矩原文」和「新行」两块就能审；出处、理由是我和核验员写的依据，供你判断「留不留、改得对不对」。",
           "", f"本文件 {len(f['rules'])} 条：" + "、".join(f"{k} {v}" for k, v in sorted(recs.items())) + f"；另有 {len(f['blocks'])} 个非编号块（文末）。", "", "---", ""]
    for r in f["rules"]:
        out += rule_block(f, r, ann.get(r["id"]), rows.get(r["id"]))
    out += ["## 非编号块（引言、署名、图、表）", ""]
    for k, b in enumerate(f["blocks"], start=1):
        o = rows.get(f"{f['short']}@{k}")
        out += [f"### {f['short']}@{k} · {b['kind']}（第 {b['line_start']}–{b['line_end']} 行）", "", *quote(b["text"]), "", *new_part(o), "", "---", ""]
    return "\n".join(out)


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    d = cd.DEFAULT_DIR
    out = OUT
    if "--draft" in argv:
        d = pathlib.Path(argv[argv.index("--draft") + 1])
    if "--out" in argv:
        out = pathlib.Path(argv[argv.index("--out") + 1])
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    ann = cd.annotations()
    rows, problems = cd.load(d)
    if problems:
        print("draft file problems:", *problems, sep="\n  ")
        return 1
    out.mkdir(parents=True, exist_ok=True)
    for f in ledger["files"]:
        dest = out / f"review-{f['short']}.md"
        dest.write_text(build(f, ann, rows), encoding="utf-8", newline="\n")
        print(f"{dest.name}: {len(f['rules'])} rules, {len(f['blocks'])} blocks")
    return 0


def selftest() -> int:
    ok = True

    def check(cond: bool, what: str):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    f = {"short": "overview", "path": "p/overview.md", "blocks": [], "rules": [{"id": "overview#1", "name": "N", "text": "1. **N** — Do it.\n   - a", "line_start": 3, "line_end": 4, "flags": ["quote"]}]}
    ann = {"overview#1": {"source": "作者", "confidence": "中", "kind": "规矩", "basis": ["commit abc"], "recommend": "留", "merge_into": None, "home": "清单", "reason": "r", "dups": []}}
    rows = {"overview#1": {"line": "- **do-it** Do it.", "lines": None, "long_file": None, "note": "n", "where_else": None}}
    text = build(f, ann, rows)
    check("> 1. **N** — Do it." in text and "> " in text.split("\n")[text.split("\n").index("> 1. **N** — Do it.") + 1], "the old text is quoted line by line")
    check("- **do-it** Do it." in text and "**备注**：n" in text, "the new line and the note are there")
    check("**出处与依据**：作者（把握：中）" in text and "- commit abc" in text, "the source and basis are there")
    check("只在长文件" in "\n".join(new_part({"line": None, "lines": None, "via": "v", "long_file": "l", "note": "", "where_else": None})), "a rule kept only in a long file says so")
    check("并入 `x#1`" in "\n".join(new_part({"line": None, "lines": None, "merged_into": "x#1", "adds_to_target": "y", "where_else": None, "note": ""})), "a merge names its target")
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
