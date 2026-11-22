"""Print one or more rules from the ledger, word for word, with where they sit. Read-only.

    python -X utf8 -I scrum/sprint-26-plugin-memory/scripts/show_rule.py sprint-log#7
    python -X utf8 -I scrum/sprint-26-plugin-memory/scripts/show_rule.py overview#1 overview#2 overview#3
    python -X utf8 -I scrum/sprint-26-plugin-memory/scripts/show_rule.py overview#1-9        (a range of numbers in one file)
    python -X utf8 -I scrum/sprint-26-plugin-memory/scripts/show_rule.py --blocks sprint-log  (the non-numbered blocks of a file)
"""
import json
import re
import sys
from pathlib import Path

LEDGER = Path(__file__).resolve().parent.parent / "review" / "ledger.json"


def main(argv: list[str]) -> int:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    files = {f["short"]: f for f in ledger["files"]}
    if argv[:1] == ["--blocks"] and len(argv) == 2 and argv[1] in files:
        for b in files[argv[1]]["blocks"]:
            print(f"--- {argv[1]} block, {b['kind']}, lines {b['line_start']}-{b['line_end']}, under: {b['heading'] or '(file head)'}")
            print(b["text"])
        return 0
    if not argv:
        print(__doc__)
        return 2
    wanted: list[str] = []
    for a in argv:
        m = re.fullmatch(r"([a-z-]+)#(\d+)-(\d+)", a)
        if m:
            wanted += [f"{m.group(1)}#{n}" for n in range(int(m.group(2)), int(m.group(3)) + 1)]
        else:
            wanted.append(a)
    by_id = {r["id"]: (f, r) for f in ledger["files"] for r in f["rules"]}
    code = 0
    for w in wanted:
        if w not in by_id:
            print(f"--- {w}: not in the ledger")
            code = 1
            continue
        f, r = by_id[w]
        print(f"--- {r['id']} | {r['name']} | {f['path']} lines {r['line_start']}-{r['line_end']} | under: {r['heading']} | flags: {', '.join(r['flags']) or '-'}")
        print(r["text"])
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
