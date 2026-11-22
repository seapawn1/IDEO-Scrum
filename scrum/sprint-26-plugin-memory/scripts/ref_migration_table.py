"""Sprint 26 row 13 (prep): for every reference to the old conventions outside the six files, the Memory handle(s) that replace it.

    python -X utf8 -I scripts/ref_migration_table.py [--out FILE]
    python -X utf8 -I scripts/ref_migration_table.py --selftest

Reads the draft (review/draft/*.json, as assemble_memory.py does) and scans the live files the way refs_inventory.py does.
A reference to a rule that has a line, or was merged into one, or is kept only in a long file, gets its handle(s); a rule that
was deleted, a path, a heading and a number that resolves to nothing are listed for a person. Nothing is rewritten here:
the table is what the migration (row 13) works from, and it is run again after Sprint 27 has merged, when the files have moved.
"""
from __future__ import annotations

import pathlib
import sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import assemble_memory as am  # noqa: E402
import check_drafts as cd  # noqa: E402
import refs_inventory as ri  # noqa: E402

SPRINT = HERE.parent
DEFAULT_OUT = SPRINT / "review" / "refs-migration.md"


def classify(ref: dict, rows: dict[str, dict]) -> tuple[str, str]:
    """(proposed new reference, who does it): 'auto' when the handles are known, 'person' when someone has to read it."""
    kind, target = ref["kind"], ref["target"]
    if kind == "heading":
        return "Memory `departures` (long file `long/departures.md`)", "person"
    if kind == "path":
        return "the Memory (`ideo-scrum:memory`) — name the handle the sentence is about", "person"
    if not target:
        return "?", "person"
    hs = am.handles_for(rows, target)
    if hs:
        return "Memory " + ", ".join(f"`{h}`" for h in hs), "auto"
    o = rows.get(target)
    if o is None:
        return f"{target} is not in the draft", "person"
    return "deleted: " + (o.get("where_else") or "no replacement written")[:120], "person"


def collect() -> list[dict]:
    out = []
    for p in ri.files():
        rel = p.relative_to(ri.REPO).as_posix()
        if ri.host_short(rel):
            continue  # inside the six files: they are deleted with the old conventions
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for no, line in enumerate(text.split("\n"), 1):
            out += ri.scan_line(rel, no, line)
    return out


def table(refs: list[dict], rows: dict[str, dict]) -> tuple[str, Counter]:
    counts: Counter = Counter()
    lines = ["# 旧约定引用迁移表（Sprint 26 行 13 的底稿）", "",
             "由 `scripts/ref_migration_table.py` 生成：六份旧约定文件之外的每处引用，和替它的 Memory handle。`auto` 是 handle 已知，仍要人读一遍上下文再改；`person` 是路径、标题、解析不出的编号、已删的规矩，要人写。27 合入后文件会动，要重新生成。", "",
             "| 位置 | 种类 | 旧目标 | 改成 | 谁做 |", "| --- | --- | --- | --- | --- |"]
    for r in sorted(refs, key=lambda r: (r["file"], r["line"], r["kind"], str(r["target"]))):
        new, who = classify(r, rows)
        counts[(r["kind"], who)] += 1
        lines.append(f"| `{r['file']}:{r['line']}` | {r['kind']} | {r['target'] or '?'} | {new} | {who} |")
    return "\n".join(lines) + "\n", counts


def selftest() -> int:
    ok = True

    def check(cond: bool, what: str) -> None:
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    rows = {"a#1": {"id": "a#1", "line": "- **one-handle** Do it."}, "a#2": {"id": "a#2", "merged_into": "a#1"},
            "a#3": {"id": "a#3", "where_else": "in the template"}, "a#4": {"id": "a#4", "via": "idx"}}
    check(classify({"kind": "number", "target": "a#1"}, rows) == ("Memory `one-handle`", "auto"), "a rule with a line gets its handle")
    check(classify({"kind": "number", "target": "a#2"}, rows) == ("Memory `one-handle`", "auto"), "a merged rule gets its target's handle")
    check(classify({"kind": "number", "target": "a#4"}, rows) == ("Memory `idx`", "auto"), "a rule kept in a long file gets the index line's handle")
    check(classify({"kind": "number", "target": "a#3"}, rows)[1] == "person", "a deleted rule goes to a person")
    check(classify({"kind": "number", "target": None}, rows)[1] == "person", "an unresolved number goes to a person")
    check(classify({"kind": "number", "target": "z#9"}, rows)[1] == "person", "a rule that is not in the draft goes to a person")
    check(classify({"kind": "heading", "target": "overview:Departures"}, rows)[1] == "person", "a heading goes to a person")
    check(classify({"kind": "path", "target": "overview"}, rows)[1] == "person", "a path goes to a person")
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    out = pathlib.Path(argv[argv.index("--out") + 1]) if "--out" in argv else DEFAULT_OUT
    rows, problems = cd.load(cd.DEFAULT_DIR)
    if problems:
        print("draft file problems:", *problems, sep="\n  ")
        return 1
    refs = collect()
    text, counts = table(refs, rows)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8", newline="\n")
    total = sum(counts.values())
    auto = sum(n for (_, w), n in counts.items() if w == "auto")
    print(f"{total} references outside the six files: {auto} with known handles ('auto'), {total - auto} for a person")
    print({f"{k}/{w}": n for (k, w), n in sorted(counts.items())})
    print("written to", out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
