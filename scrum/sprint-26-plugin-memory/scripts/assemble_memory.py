"""Sprint 26 rows 6-9: put the drafted lines and long files together, and write the cross tables.

    python -X utf8 -I scripts/assemble_memory.py [--draft DIR] [--out DIR]
    python -X utf8 -I scripts/assemble_memory.py --selftest

Reads the drafters' files (DIR/*.json, checked by check_drafts.py) and the long files (DIR/long/*.md); writes
memory-draft/MEMORY.md (the list), memory-draft/long/*.md, and review/map-old-new.md (every old rule to its new line,
merge or deletion, and every new handle back to its old rules). It prints the sizes that matter for how Memory is
carried: the whole list, and the slice each role would get from a hook.
"""
from __future__ import annotations

import json
import pathlib
import re
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_drafts as cd  # noqa: E402

SPRINT = HERE.parent
DEFAULT_OUT = SPRINT / "memory-draft"
MAP_FILE = SPRINT / "review" / "map-old-new.md"
FILE_ORDER = ["overview", "product-log", "sprint-log", "design-log", "ideo-log", "board-log"]
TITLES = {
    "roles": "Who does what, and who decides",
    "product-log": "The product log",
    "sprint": "Running a Sprint",
    "design": "Running a design sprint",
    "ideo": "The five modes and the IDEO log",
    "board": "The Scrum board",
    "meta": "About these rules",
}
HEADER = """# IDEO-Scrum Memory

> The rules every role follows, one line each. A line marked `[dev,sm]` binds those roles; a line with no mark binds every role. `→ long/<file>.md` says where the detail is: read that file before you do what the line is about. These are working conventions: follow what fits, override what doesn't, and say why in the log's notes.
"""


def rank(i: str) -> tuple[int, int]:
    f, n = i.rsplit("#", 1)
    return FILE_ORDER.index(f), int(n)


def lines_of(o: dict) -> list[str]:
    return [o["line"]] if o.get("line") else (o.get("lines") or [])


def role_slices(entries: list[tuple[str, str]]) -> dict[str, int]:
    out = {}
    for role in sorted(cd.ROLES):
        n = 0
        for _, ln in entries:
            m = cd.LINE.match(ln)
            tags = set(m.group(2).split(",")) if m and m.group(2) else None
            if tags is None or role in tags:
                n += len(ln) + 1
        out[role] = n
    return out


def build(rows: dict[str, dict]) -> tuple[str, list[tuple[str, str]]]:
    by_section: dict[str, list[tuple[tuple[int, int], str, str]]] = {s: [] for s in cd.SECTIONS}
    for i, o in rows.items():
        for ln in lines_of(o):
            by_section.setdefault(o.get("section") or "meta", []).append((rank(i), i, ln))
    out, flat = [HEADER], []
    for s in cd.SECTIONS:
        items = sorted(by_section.get(s, []))
        if not items:
            continue
        out.append(f"\n## {TITLES[s]}\n")
        for _, i, ln in items:
            out.append(ln)
            flat.append((i, ln))
    return "\n".join(out) + "\n", flat


PLACEHOLDER = re.compile(r"‹([a-z-]+#\d+)›")


def handles_for(rows: dict[str, dict], i: str) -> list[str]:
    """The handles an old rule lives under now: its own lines, or its merge target's."""
    o = rows.get(i)
    if not o:
        return []
    hs = [m.group(1) for ln in lines_of(o) for m in [cd.LINE.match(ln)] if m]
    if hs:
        return hs
    return handles_for(rows, o["merged_into"]) if o.get("merged_into") else []


def resolve(text: str, rows: dict[str, dict]) -> tuple[str, list[str]]:
    """A long file may name an old rule as ‹sprint-log#10›; the finished file names its handle(s) instead. A rule
    with no line and no merge target (a deletion, or one not drafted yet) stays as written and is reported."""
    bad: list[str] = []

    def sub(m: re.Match) -> str:
        hs = handles_for(rows, m.group(1))
        if not hs:
            bad.append(m.group(1))
            return m.group(0)
        return ", ".join(f"`{h}`" for h in hs)

    return PLACEHOLDER.sub(sub, text), bad


def map_tables(rows: dict[str, dict], ann: dict[str, dict]) -> str:
    handle_of: dict[str, list[str]] = {}
    new_to_old: dict[str, list[str]] = {}
    for i, o in rows.items():
        for ln in lines_of(o):
            m = cd.LINE.match(ln)
            if m:
                handle_of.setdefault(i, []).append(m.group(1))
                new_to_old.setdefault(m.group(1), []).append(i)
    for i, o in rows.items():
        t = o.get("merged_into")
        if t:
            for h in handle_of.get(t, []):
                if i not in new_to_old[h]:
                    new_to_old[h].append(i)
    out = ["# 旧规矩 ↔ Memory 对照表", "", "由 `scripts/assemble_memory.py` 生成。每条旧规矩一行：它去了哪一行（handle）、并入了谁、或删在哪里；再反过来，每个 handle 来自哪几条旧规矩。", "",
           "## 旧 → 新", "", "| 旧规矩 | 处理 | 去向 |", "| --- | --- | --- |"]
    for i in sorted(rows, key=rank):
        o, a = rows[i], ann[i]
        if lines_of(o):
            out.append(f"| {i} | {a['recommend']} | " + "、".join(f"`{h}`" for h in handle_of.get(i, [])) + (f"（长文件 `{o['long_file']}`）" if o.get("long_file") else "") + " |")
        elif o.get("merged_into"):
            hs = "、".join(f"`{h}`" for h in handle_of.get(o["merged_into"], []))
            out.append(f"| {i} | 并 | 并入 {o['merged_into']} {hs} |")
        else:
            out.append(f"| {i} | 删 | {o.get('where_else') or '无'} |")
    out += ["", "## 新 → 旧", "", "| handle | 来自的旧规矩 |", "| --- | --- |"]
    for h in sorted(new_to_old):
        out.append(f"| `{h}` | " + "、".join(sorted(new_to_old[h], key=rank)) + " |")
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    d = cd.DEFAULT_DIR
    out = DEFAULT_OUT
    if "--draft" in argv:
        d = pathlib.Path(argv[argv.index("--draft") + 1])
    if "--out" in argv:
        out = pathlib.Path(argv[argv.index("--out") + 1])
    rows, problems = cd.load(d)
    if problems:
        print("draft file problems:", *problems, sep="\n  ")
        return 1
    ann = cd.annotations()
    text, flat = build(rows)
    out.mkdir(parents=True, exist_ok=True)
    (out / "MEMORY.md").write_text(text, encoding="utf-8", newline="\n")
    long_src = d / "long"
    (out / "long").mkdir(exist_ok=True)
    have, unresolved = set(), {}
    if long_src.is_dir():
        for p in sorted(long_src.glob("*.md")):
            body, bad = resolve(p.read_text(encoding="utf-8"), rows)
            (out / "long" / p.name).write_text(body, encoding="utf-8", newline="\n")
            have.add(p.stem)
            if bad:
                unresolved[p.name] = sorted(set(bad))
    referenced = set(re.findall(r"long/([A-Za-z0-9_-]+)\.md", text))
    MAP_FILE.write_text(map_tables(rows, ann), encoding="utf-8", newline="\n")
    total = len(text)
    print(f"MEMORY.md: {len(flat)} lines, {total} characters; slices a hook would carry per role: {role_slices(flat)}")
    print("long files referenced but not written:", sorted(referenced - have) or "none")
    print("long files written but not referenced:", sorted(have - referenced) or "none")
    print("rule placeholders left unresolved in long files:", unresolved or "none")
    return 0


def selftest() -> int:
    ok = True

    def check(cond: bool, what: str):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    rows = {
        "sprint-log#8": {"id": "sprint-log#8", "line": "- **go-ahead** [dev,sm] Build after the go-ahead.", "lines": None, "section": "sprint", "long_file": None, "merged_into": None, "absorbed": []},
        "overview#10": {"id": "overview#10", "line": "- **ask-the-po** Ask the PO.", "lines": None, "section": "roles", "long_file": None, "merged_into": None, "absorbed": ["sprint-log#25"]},
        "sprint-log#25": {"id": "sprint-log#25", "line": None, "lines": None, "section": "roles", "long_file": None, "merged_into": "overview#10", "absorbed": [], "adds_to_target": "x"},
        "design-log#4": {"id": "design-log#4", "line": None, "lines": None, "section": "design", "long_file": None, "merged_into": None, "absorbed": [], "where_else": "design template"},
    }
    ann = {i: {"recommend": "留"} for i in rows}
    text, flat = build(rows)
    check(text.index("## Who does what") < text.index("## Running a Sprint"), "sections come in the fixed order")
    check([i for i, _ in flat] == ["overview#10", "sprint-log#8"], "a line sits in its section, in old-file order")
    sl = role_slices(flat)
    check(sl["dev"] > sl["des"] and sl["des"] == len("- **ask-the-po** Ask the PO.") + 1, "a role slice has the untagged lines and its own tagged lines")
    mp = map_tables(rows, ann)
    check("| sprint-log#25 | 并 | 并入 overview#10 `ask-the-po` |" in mp, "the map shows a merge with the target's handle")
    check("| `ask-the-po` | overview#10、sprint-log#25 |" in mp, "the map shows a handle with the rules that fed it")
    check("| design-log#4 | 删 | design template |" in mp, "the map shows where a deleted rule went")
    body, bad = resolve("See ‹sprint-log#8›, ‹sprint-log#25› and ‹design-log#4›.", rows)
    check(body == "See `go-ahead`, `ask-the-po` and ‹design-log#4›." and bad == ["design-log#4"],
          "a placeholder becomes its handle, a merged rule its target's handle, a deleted rule stays and is reported")
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main(sys.argv[1:]))
