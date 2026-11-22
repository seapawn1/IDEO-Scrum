"""Sprint 27 Test: an independent re-read of the trigger test, round 1. It does not use run_trigger.py: it opens every raw
stream, collects the Skill calls itself, and compares them with the judge's row of that trial and with the tally in
chapter 5. Read-only.

    python -X utf8 -I trigger_crosscheck.py ROUND_DIR

ROUND_DIR is the folder of the round (results.jsonl and raw/), kept outside the repository. A raw stream is data from a
model run: it is parsed as JSON and never run.
"""
import collections
import json
import pathlib
import sys

ROLES = {"scrum-master", "developer", "designer", "stakeholder", "supporter"}
# group -> (the role that counts as a hit, the role that counts as mixing)
TARGET = {"A": ("supporter", "stakeholder"), "B": ("stakeholder", "supporter"), "C": ("scrum-master", None)}


def skill_calls(stream):
    calls = []
    for line in stream.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if event.get("type") != "assistant":
            continue
        for block in (event.get("message") or {}).get("content") or []:
            if isinstance(block, dict) and block.get("type") == "tool_use" and block.get("name") == "Skill":
                calls.append((block.get("input") or {}).get("skill"))
    return calls


def main():
    round_dir = pathlib.Path(sys.argv[1])
    rows = [json.loads(l) for l in (round_dir / "results.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    wrong, tally = [], collections.defaultdict(lambda: [0, 0, 0])  # (arm, group) -> [n, hits, mixing]
    for row in rows:
        mine = [s for s in skill_calls(round_dir / "raw" / (row["trial"] + ".session.jsonl")) if s]
        roles = sorted({s.split(":", 1)[1] for s in mine if s.startswith("ideo-scrum:") and s.split(":", 1)[1] in ROLES})
        if roles != sorted(row["roles"]):
            wrong.append((row["trial"], "roles: judge %s, raw %s" % (sorted(row["roles"]), roles)))
        if sorted(set(mine)) != sorted(set(row["skills"])):
            wrong.append((row["trial"], "skills: judge %s, raw %s" % (sorted(set(row["skills"])), sorted(set(mine)))))
        hit_role, mix_role = TARGET[row["group"]]
        cell = tally[(row["arm"], row["group"])]
        cell[0] += 1
        cell[1] += hit_role in roles
        cell[2] += bool(mix_role) and mix_role in roles
    print("%d trials re-read from raw; %d disagree with the judge's row" % (len(rows), len(wrong)))
    for trial, why in wrong:
        print("  DISAGREE %s: %s" % (trial, why))
    for (arm, group), (n, hits, mixing) in sorted(tally.items()):
        print("%-9s group %s: n=%d  hits=%d  mixing=%s" % (arm, group, n, hits, mixing if TARGET[group][1] else "-"))
    return 1 if wrong else 0


if __name__ == "__main__":
    sys.exit(main())
