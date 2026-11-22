"""Sprint 26, work item 2: read the verifiers' files, report what needs a decision, apply the decisions.

    python -X utf8 -I scripts/apply_verification.py check [--dir DIR]       are all 26 files there, valid, one object per rule?
    python -X utf8 -I scripts/apply_verification.py report [--dir DIR]      the rules where any verifier said fix or doubt
    python -X utf8 -I scripts/apply_verification.py apply DECISIONS.json    apply my decisions to review/annotations/*.json

The verifiers (a workflow run outside the session, scripts/verify_annotations.wf.js) write to
S:/IDEO-Scrum-Archives/sprint-26-plugin-memory/verify/<chunk>.<lens>.json. A verifier's `fix` is a suggestion: nothing is
applied until DECISIONS.json says so. DECISIONS.json is {"<id>": {"accept": ["reason", "recommend", ...]} |
{"set": {...fields...}} | {"keep": "why the annotation stays"}}; `accept` takes those fields from the verifiers' fixes
(the first fix that has the field), `set` writes the given values, `keep` changes nothing. After `apply`, the annotation
checker (check_annotations.py check --complete) runs on the result.
"""
from __future__ import annotations

import glob
import json
import pathlib
import subprocess
import sys
from collections import defaultdict

HERE = pathlib.Path(__file__).resolve().parent
SPRINT = HERE.parent
ANN = SPRINT / "review" / "annotations"
LEDGER = SPRINT / "review" / "ledger.json"
DEFAULT_DIR = pathlib.Path("S:/IDEO-Scrum-Archives/sprint-26-plugin-memory/verify")
VERDICTS = ["ok", "fix", "doubt"]
FIX_FIELDS = ["reason", "recommend", "merge_into", "home", "kind", "source", "confidence"]
LENSES = ["facts", "loss"]


def ledger_ids() -> dict[str, list[str]]:
    """chunk key -> the ids it should hold, from the workflow script's own chunk table (ids like sprint-log#1-9)."""
    text = (HERE / "verify_annotations.wf.js").read_text(encoding="utf-8")
    import re

    chunks = {}
    for m in re.finditer(r"key: '([^']+)',\s*ids: '([^#']+)#(\d+)-(\d+)'", text):
        key, f, a, b = m.group(1), m.group(2), int(m.group(3)), int(m.group(4))
        chunks[key] = [f"{f}#{n}" for n in range(a, b + 1)]
    return chunks


def load(dirpath: pathlib.Path) -> tuple[dict, list[str]]:
    problems: list[str] = []
    got: dict[str, dict[str, dict]] = defaultdict(dict)  # id -> lens -> object
    for key, ids in ledger_ids().items():
        for lens in LENSES:
            p = dirpath / f"{key}.{lens}.json"
            if not p.exists():
                problems.append(f"{p.name}: missing")
                continue
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
            except ValueError as e:
                problems.append(f"{p.name}: not valid JSON ({e})")
                continue
            if not isinstance(data, list):
                problems.append(f"{p.name}: top level is not a list")
                continue
            seen = [o.get("id") for o in data if isinstance(o, dict)]
            for i in ids:
                if seen.count(i) != 1:
                    problems.append(f"{p.name}: {i} appears {seen.count(i)} times")
            for o in data:
                if not isinstance(o, dict):
                    problems.append(f"{p.name}: an item is not an object")
                    continue
                if o.get("id") not in ids:
                    problems.append(f"{p.name}: {o.get('id')} is not in this chunk")
                    continue
                if o.get("verdict") not in VERDICTS:
                    problems.append(f"{p.name}: {o['id']} verdict {o.get('verdict')!r}")
                if not isinstance(o.get("issues"), list):
                    problems.append(f"{p.name}: {o['id']} issues is not a list")
                fx = o.get("fix")
                if fx is not None and (not isinstance(fx, dict) or set(fx) - set(FIX_FIELDS)):
                    problems.append(f"{p.name}: {o['id']} fix has fields outside {FIX_FIELDS}")
                if o.get("verdict") == "fix" and not fx:
                    problems.append(f"{p.name}: {o['id']} says fix but gives no fix")
                got[o["id"]][lens] = o
    return got, problems


def annotations() -> tuple[dict[str, dict], dict[str, pathlib.Path]]:
    by_id, where = {}, {}
    for p in sorted(ANN.glob("*.json")):
        for o in json.loads(p.read_text(encoding="utf-8")):
            by_id[o["id"]] = o
            where[o["id"]] = p
    return by_id, where


def cmd_check(d: pathlib.Path) -> int:
    got, problems = load(d)
    n_ok = sum(1 for v in got.values() if all(x.get("verdict") == "ok" for x in v.values()) and len(v) == 2)
    print(f"{len(got)} rules read; {n_ok} ok in both lenses; {len(problems)} problems")
    for p in problems:
        print("  " + p)
    return 1 if problems else 0


def cmd_report(d: pathlib.Path) -> int:
    got, problems = load(d)
    ann, _ = annotations()
    flagged = [i for i in sorted(got, key=lambda s: (s.rsplit("#", 1)[0], int(s.rsplit("#", 1)[1]))) if any(x.get("verdict") != "ok" for x in got[i].values())]
    print(f"{len(flagged)} of {len(got)} rules have a fix or a doubt ({len(problems)} file problems)")
    for i in flagged:
        a = ann[i]
        print(f"\n=== {i} | now: {a['recommend']}{('→' + a['merge_into']) if a.get('merge_into') else ''} · {a['home']} · {a['kind']} · {a['source']} · {a['confidence']}")
        print("    reason now: " + a["reason"][:220])
        for lens in LENSES:
            o = got[i].get(lens)
            if not o or o["verdict"] == "ok":
                continue
            print(f"  [{lens}] {o['verdict']}: " + " / ".join(x[:260] for x in o["issues"]))
            if o.get("fix"):
                print("    fix: " + json.dumps(o["fix"], ensure_ascii=False)[:360])
    return 0


def cmd_apply(decisions_path: str, d: pathlib.Path) -> int:
    decisions = json.loads(pathlib.Path(decisions_path).read_text(encoding="utf-8"))
    got, _ = load(d)
    ann, where = annotations()
    files: dict[pathlib.Path, list] = {}
    for p in set(where.values()):
        files[p] = json.loads(p.read_text(encoding="utf-8"))
    changed = 0
    for i, dec in decisions.items():
        if i not in ann:
            print("unknown id", i)
            return 2
        target = next(o for o in files[where[i]] if o["id"] == i)
        if "keep" in dec:
            target.setdefault("checked", []).append("keep: " + dec["keep"])
            continue
        updates = {}
        if "accept" in dec:
            for field in dec["accept"]:
                for lens in LENSES:
                    fx = (got.get(i, {}).get(lens) or {}).get("fix") or {}
                    if field in fx:
                        updates[field] = fx[field]
                        break
                else:
                    print(f"{i}: no verifier fix has the field {field}")
                    return 2
        updates.update(dec.get("set") or {})
        bad = set(updates) - set(FIX_FIELDS)
        if bad:
            print(f"{i}: fields outside {FIX_FIELDS}: {bad}")
            return 2
        if updates:
            target.update(updates)
            target.setdefault("checked", []).append("verified: " + ", ".join(sorted(updates)))
            changed += 1
    for p, data in files.items():
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"applied to {changed} rules")
    r = subprocess.run([sys.executable, "-X", "utf8", "-I", str(HERE / "check_annotations.py"), "check", "--complete"], capture_output=True, text=True)
    print(r.stdout.strip())
    return r.returncode


def main(argv: list[str]) -> int:
    d = DEFAULT_DIR
    if "--dir" in argv:
        i = argv.index("--dir")
        d = pathlib.Path(argv[i + 1])
        argv = argv[:i] + argv[i + 2 :]
    if argv[:1] == ["check"]:
        return cmd_check(d)
    if argv[:1] == ["report"]:
        return cmd_report(d)
    if argv[:1] == ["apply"] and len(argv) == 2:
        return cmd_apply(argv[1], d)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
