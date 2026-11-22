"""Sprint 26 (Master 2026-11-23): the old relay wording must be found nowhere in what is delivered.

    python -X utf8 -I scripts/check_old_relay.py              scan plugins/, dsh/, docs/, README* (the deliverables)
    python -X utf8 -I scripts/check_old_relay.py --draft      scan the draft Memory (memory-draft/) instead
    python -X utf8 -I scripts/check_old_relay.py --selftest

The PO decided (2026-11-23) that a Supporter the PO has authorized may relay tool permissions and settings, CLAUDE.md or
AGENTS.md, a push or a release as the PO's own word. A text that still says a relay does not stand in for the PO's own
confirmation contradicts it, and a script cannot see a contradiction of meaning: the old sentences have to be found by their
words and brought to zero. Searched:

  anywhere:        "a relay does not stand in", "own confirmation", "亲口确认"
  relay context:   "own word", "in person" -- only on a line that also says relay, Supporter or 转达 (the Scrum Guide
                   Expansion Pack's own "in person" is no relay text; assets/ is not scanned)

Not searched: scrum/ (the logs, the archives, the review records are history). One sentence is kept on purpose: the host's own
check ("it accepts only what the user confirms in the session that acts"); it matches none of the words above, and the
verification table lists it on a row of its own.
"""
from __future__ import annotations

import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SPRINT = HERE.parent
ROOT = SPRINT.parents[1]
SUFFIXES = {".md", ".js", ".mjs", ".json", ".html", ".py", ".sh", ".yml", ".yaml", ".txt"}
SKIP_DIRS = {"assets", "node_modules", ".git"}
ANYWHERE = [re.compile(p, re.I) for p in (r"a relay does not stand in", r"own confirmation", r"亲口确认")]
IN_RELAY = [re.compile(p, re.I) for p in (r"\bown word\b", r"in person")]  # "own words" (a Supporter relaying the PO's words) is no old sentence
RELAY_WORDS = re.compile(r"relay|supporter|转达", re.I)


def hits_in(text: str) -> list[tuple[int, str, str]]:
    out = []
    for n, line in enumerate(text.splitlines(), start=1):
        for pat in ANYWHERE:
            if pat.search(line):
                out.append((n, pat.pattern, line.strip()[:160]))
        if RELAY_WORDS.search(line):
            for pat in IN_RELAY:
                if pat.search(line):
                    out.append((n, pat.pattern, line.strip()[:160]))
    return out


def files(draft: bool) -> list[pathlib.Path]:
    if draft:
        roots = [SPRINT / "memory-draft"]
    else:
        roots = [ROOT / "plugins", ROOT / "dsh", ROOT / "docs"] + sorted(ROOT.glob("README*"))
    out: list[pathlib.Path] = []
    for r in roots:
        if r.is_file():
            out.append(r)
        elif r.is_dir():
            out += [p for p in sorted(r.rglob("*")) if p.is_file() and p.suffix in SUFFIXES and not (set(p.relative_to(r).parts) & SKIP_DIRS)]
    return out


def scan(draft: bool) -> list[str]:
    found = []
    for p in files(draft):
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for n, pat, line in hits_in(text):
            found.append(f"{p.relative_to(ROOT).as_posix()}:{n}: [{pat}] {line}")
    return found


def selftest() -> int:
    ok = True
    for what, cond in (
        ("the old supporter sentence is found", bool(hits_in("those need the Product Owner's own confirmation, and a relay does not stand in for it."))),
        ("'in person' on a relay line is found", bool(hits_in("a relay of what needs the Product Owner in person"))),
        ("'in person' with no relay word is not", not hits_in("They meet in person at the workshop.")),
        ("'own word' on a Supporter line is found", bool(hits_in("the Supporter keeps the PO's own word"))),
        ("'own words' (relaying their words) is no old sentence", not hits_in("the Supporter relays the PO's own words")),
        ("the host sentence is not a hit", not hits_in("The host keeps its own check: it accepts only what the user confirms in the session that acts.")),
        ("the Chinese wording is found", bool(hits_in("这类事要 PO 亲口确认"))),
    ):
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    found = scan("--draft" in sys.argv)
    for f in found:
        print(f)
    where = "the draft Memory" if "--draft" in sys.argv else "plugins/, dsh/, docs/, README*"
    print(f"{len(found)} old relay sentences in {where}" if found else f"the old relay wording is nowhere in {where}")
    sys.exit(1 if found else 0)
