"""Sprint 26, work item 2: turn the verifiers' files into a first set of decisions, and list what needs my own eyes.

    python -X utf8 -I scripts/auto_decisions.py [--dir DIR] --out DECISIONS.json --manual MANUAL.txt

Policy (written before reading the verifiers' findings in full):
- a rule whose verifiers both said ok: nothing changes;
- a rule with one fix, or two fixes that agree on a field: that field is accepted (`accept`);
- a rule where the two lenses propose different values for the same field, or where a verifier said doubt, or where a
  fix touches `recommend`/`home` against the current annotation in the direction of losing content (a keep turned into a
  delete): goes to the manual list, with both proposals side by side. Nothing there is applied until I decide.
The decisions file is read by apply_verification.py apply. The manual list is for me, one rule at a time.
"""
from __future__ import annotations

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import apply_verification as av  # noqa: E402


def main(argv: list[str]) -> int:
    d = av.DEFAULT_DIR
    if "--dir" in argv:
        d = pathlib.Path(argv[argv.index("--dir") + 1])
    out = pathlib.Path(argv[argv.index("--out") + 1])
    manual = pathlib.Path(argv[argv.index("--manual") + 1])
    got, problems = av.load(d)
    if problems:
        print("file problems:", *problems, sep="\n  ")
        return 1
    ann, _ = av.annotations()
    decisions: dict[str, dict] = {}
    manual_lines: list[str] = []
    n_ok = n_auto = n_man = 0
    order = sorted(got, key=lambda s: (s.rsplit("#", 1)[0], int(s.rsplit("#", 1)[1])))
    for i in order:
        by = got[i]
        if all(o["verdict"] == "ok" for o in by.values()):
            n_ok += 1
            continue
        fixes = {lens: (o.get("fix") or {}) for lens, o in by.items() if o["verdict"] == "fix"}
        doubts = [lens for lens, o in by.items() if o["verdict"] == "doubt"]
        accept, conflicts = [], []
        for field in av.FIX_FIELDS:
            vals = {lens: fx[field] for lens, fx in fixes.items() if field in fx}
            if not vals:
                continue
            if len({json.dumps(v, ensure_ascii=False) for v in vals.values()}) == 1:
                accept.append(field)
            elif len(vals) == 1 and not (field == "recommend" and ann[i]["recommend"] in ("留", "改") and next(iter(vals.values())) in ("删", "并")):
                accept.append(field)
            else:
                conflicts.append(field)
        if conflicts or doubts:
            n_man += 1
            cur = ann[i]
            manual_lines.append(f"\n=== {i} | now: {cur['recommend']}{('→' + cur['merge_into']) if cur.get('merge_into') else ''} · {cur['home']} · {cur['kind']} · {cur['source']} · {cur['confidence']}")
            manual_lines.append("    reason now: " + cur["reason"])
            for lens, o in by.items():
                if o["verdict"] == "ok":
                    continue
                manual_lines.append(f"  [{lens}] {o['verdict']}: " + " / ".join(o["issues"]))
                if o.get("fix"):
                    manual_lines.append("    fix: " + json.dumps(o["fix"], ensure_ascii=False))
            manual_lines.append(f"    auto-accepted fields: {accept or '-'}; conflicts: {conflicts or '-'}; doubts: {doubts or '-'}")
            if accept:
                decisions[i] = {"accept": accept, "_manual": True}
        else:
            n_auto += 1
            decisions[i] = {"accept": accept} if accept else {"keep": "verifier flagged, no field to change"}
    out.write_text(json.dumps(decisions, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    manual.write_text("\n".join(manual_lines) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(order)} rules: {n_ok} ok in both lenses, {n_auto} auto, {n_man} manual (details in {manual.name})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
