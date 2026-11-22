"""Sprint 27 Test evidence: content fidelity and attribution (PBI-84 and the quotations of H2), commit scopes of H3 and
H6, and the length of every description. Read-only; it prints PASS or FAIL lines and exits 1 if any check fails.

    python -X utf8 -I evidence.py [--base REV]

The base is the Sprint's baseline commit (1145382). The commits named below are this Sprint's own work commits.
"""
import argparse
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[4]
PLUGIN = "plugins/ideo-scrum"
H3_COMMIT, H4_COMMIT, H6_COMMIT = "e3fce9e", "2fb4881", "27cdaa3"
MODES = ["empathize", "define", "ideate", "prototype", "test"]
EXCERPT_DIRS = [
    PLUGIN + "/skills/scrum-kernel/assets", PLUGIN + "/skills/scrum-kernel/references",
    PLUGIN + "/skills/sprint-kernel/events", PLUGIN + "/skills/design-kernel/steps",
    PLUGIN + "/skills/ideo-kernel/methods",
]
failures = []


def git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True, encoding="utf-8").stdout


def show(rev, path):
    return subprocess.run(["git", "-C", str(REPO), "show", "%s:%s" % (rev, path)], capture_output=True).stdout.decode("utf-8")


def read(path):
    return (REPO / path).read_bytes().decode("utf-8").replace("\r\n", "\n")


def squash(text):
    return re.sub(r"\s+", " ", text).strip()


def check(name, ok, detail=""):
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, " — " + detail if detail else ""))
    if not ok:
        failures.append(name)


def description(text):
    m = re.search(r"^description:[ \t]*(.*)$", text.replace("\r\n", "\n"), re.M)
    return m.group(1).strip() if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="1145382")
    ap.add_argument("--candidate", default="52b42fa", help="the commit the trigger test (round 1) ran on")
    args = ap.parse_args()
    base, candidate = args.base, args.candidate

    # --- H2: the quotations in the new role entry and in convention 14 are verbatim
    sgep = squash(read(PLUGIN + "/skills/scrum-kernel/assets/scrum-guide-expansion-pack-2026.1.md"))
    guide = squash(read(PLUGIN + "/skills/scrum-kernel/assets/scrum-guide-2020.md"))
    supporter = read(PLUGIN + "/commands/supporter.md")
    body = supporter.split("\n---\n", 1)[1]  # the quotations are in the body; the front matter is only the description
    quoted = sorted(set(re.findall(r'"([^"\n]+)"', body)))
    missing = [q for q in quoted if squash(q) not in sgep]
    check("supporter.md: every double-quoted phrase is verbatim in the SGEP", bool(quoted) and not missing,
          "%d distinct phrases: %s%s" % (len(quoted), quoted, "; not found: %s" % missing if missing else ""))
    overview = read(PLUGIN + "/skills/scrum-kernel/overview.md")
    sentence = re.search(r'"(The Product Owner may do the above work[^"]+)"', overview)
    check("overview.md convention 14: the Scrum Guide 2020 sentence is verbatim",
          bool(sentence) and squash(sentence.group(1)) in guide, sentence.group(1) if sentence else "sentence not found")
    check("supporter.md: the author's choice is marked in italics",
          bool(re.search(r"^\*\(Author's choice for solo \+ AI teams", supporter, re.M)))

    # --- H2, H3, H6, H1: the excerpts are untouched
    changed = git("diff", "--name-only", base, "HEAD", "--", *EXCERPT_DIRS).split()
    check("excerpt folders (assets, references, events, steps, methods): no change against the baseline", not changed,
          "changed: %s" % changed if changed else "git diff --name-only is empty")

    # --- H4 (PBI-84): the bodies of the five mode files are verbatim, only the three quotation lines differ
    header = re.compile(r"^> (Merged from|Source|License):")
    for mode in MODES:
        path = "%s/skills/ideo-kernel/IDEO-modes/%s.md" % (PLUGIN, mode)
        old, new = show(base, path).replace("\r\n", "\n").splitlines(), read(path).splitlines()
        old_body, new_body = [l for l in old if not header.match(l)], [l for l in new if not header.match(l)]
        n_old, n_new = len(old) - len(old_body), len(new) - len(new_body)
        check("IDEO-modes/%s.md: body verbatim against the baseline" % mode,
              old_body == new_body and n_old == 3 and n_new == 3,
              "%d lines each side outside the three header lines; %d header lines before, %d now" % (len(new_body), n_old, n_new))
        head = "\n".join(new[:8])
        wanted = ["Design Process Mini-Guide", "Design Thinking Bootleg", "CC BY-NC-SA 3.0 Unported", "CC BY-NC-SA 4.0",
                  "creativecommons.org/licenses/by-nc-sa/3.0/legalcode", "creativecommons.org/licenses/by-nc-sa/4.0/legalcode",
                  "web.archive.org/web/20160118010517/", "dschool.stanford.edu/tools/design-thinking-bootleg"]
        absent = [w for w in wanted if w not in head]
        check("IDEO-modes/%s.md: the header names both sources, both licenses and their links" % mode, not absent,
              "missing: %s" % absent if absent else "8 of 8 present")
    attribution = read("ATTRIBUTION.md")
    section3 = attribution[attribution.index("## 3. "):attribution.index("## 4. ")]
    for label, needles in (("3.1 (2010 Mini-Guide)", ["### 3.1", "CC BY-NC-SA 3.0 Unported", "Design_Process_MiniGuide", "web.archive.org"]),
                           ("3.2 (2018 Bootleg)", ["### 3.2", "CC BY-NC-SA 4.0", "design-thinking-bootleg"])):
        absent = [n for n in needles if n not in section3]
        check("ATTRIBUTION.md section %s is complete" % label, not absent, "missing: %s" % absent if absent else "%d of %d present" % (len(needles), len(needles)))
    for readme in ("README.md", "README.zh-CN.md"):
        rows = [l for l in read(readme).splitlines() if "Design Process Mini-Guide" in l and "Bootleg" in l]
        check("%s: the d.school licence row names both editions and both licences" % readme,
              len(rows) == 1 and "3.0 Unported" in rows[0] and "4.0" in rows[0], rows[0][:110] if rows else "row not found")
    scope = set(git("show", "--name-only", "--format=", H4_COMMIT).split())
    expected = {"%s/skills/ideo-kernel/IDEO-modes/%s.md" % (PLUGIN, m) for m in MODES} | {
        "ATTRIBUTION.md", "README.md", "README.zh-CN.md", "scrum/sprint-27-wrap-up/SprintBacklog.md"}
    check("PBI-84 commit %s touches only the headers, ATTRIBUTION, the two README rows and the log" % H4_COMMIT,
          scope == expected, "%d files" % len(scope) if scope == expected else "unexpected: %s; absent: %s" % (sorted(scope - expected), sorted(expected - scope)))

    # --- H3 and H6: commit scopes
    h3 = git("show", "--name-only", "--format=", H3_COMMIT).split()
    check("H3 commit %s touches no methodology text under skills/" % H3_COMMIT,
          bool(h3) and not [f for f in h3 if f.startswith(PLUGIN + "/skills/")], "%d files: %s" % (len(h3), ", ".join(h3)))
    h6 = git("show", "--name-only", "--format=", H6_COMMIT).split()
    check("H6 commit %s touches docs, entry texts and the advisor only (no excerpt)" % H6_COMMIT,
          bool(h6) and all(f.startswith(("docs/", PLUGIN + "/claude-skills/", PLUGIN + "/agents/", "scrum/")) for f in h6),
          "%d files: %s" % (len(h6), ", ".join(h6)))

    # --- every changed or new description is within 1024 characters (without the quotes)
    files = [PLUGIN + "/commands/%s.md" % n for n in ("scrum-master", "developer", "designer", "stakeholder", "supporter")]
    files += [PLUGIN + "/skills/%s/SKILL.md" % k for k in ("ideo-kernel", "scrum-kernel", "sprint-kernel", "design-kernel")]
    files += [PLUGIN + "/claude-skills/project-stakeholder/SKILL.md", PLUGIN + "/claude-skills/second-opinion/SKILL.md",
              PLUGIN + "/agents/advisor.md"]
    lengths = {f.rsplit("/", 2)[-2] + "/" + f.rsplit("/", 1)[-1] if f.endswith("SKILL.md") else f.rsplit("/", 1)[-1]:
               len((description(read(f)) or "").strip('"')) for f in files}
    check("every description is a single line of at most 1024 characters", all(0 < v <= 1024 for v in lengths.values()),
          ", ".join("%s %d" % kv for kv in lengths.items()))

    # --- the trigger result of round 1 stays valid only if the descriptions are the ones that were tested
    drift = [f for f in files if description(show(candidate, f)) != description(read(f))]
    check("the %d descriptions are byte-identical to the trigger candidate %s" % (len(files), candidate), not drift,
          "differs: %s" % drift if drift else "0 of %d differ" % len(files))

    # --- the right to summon an outside view at Sprint Review, and the builder boundary, are unchanged
    stakeholder, master = PLUGIN + "/commands/stakeholder.md", PLUGIN + "/commands/scrum-master.md"
    sprint_log = PLUGIN + "/skills/sprint-kernel/conventions/sprint-log.md"
    kept = [
        (stakeholder, "Any role may summon an outside view; at Sprint Review only the PO or Scrum Master does, never the builder."),
        (stakeholder, "A session already at work delegates independent feedback to a fresh subagent rather than claiming fresh eyes."),
        (stakeholder, "Say so if the builder summons you at Sprint Review"),
        (stakeholder, "Take no build work"),
        (master, "At Sprint Review the Scrum Master or PO summons a fresh Stakeholder subagent for an outside view."),
        (sprint_log, "the Product Owner or the Scrum Master — never the builder — summons Stakeholders from the product log"),
    ]
    lost = [(f.rsplit("/", 1)[-1], s[:50]) for f, s in kept if s not in show(base, f).replace("\r\n", "\n") or s not in read(f)]
    check("Review summoning right and builder boundary: %d sentences present at the baseline and still present" % len(kept),
          not lost, "missing: %s" % lost if lost else "6 of 6 present in both")
    new = "At Sprint Review only the Product Owner or the Scrum Master summons it, never the builder."
    check("supporter.md carries the same boundary", new in read(PLUGIN + "/commands/supporter.md"))

    # --- the fixes of the Codex review (Test): present in the body of the entry and in convention 14, and only there
    supporter_text = read(PLUGIN + "/commands/supporter.md")
    in_body = supporter_text.split("\n---\n", 1)[1]
    in_convention = read(PLUGIN + "/skills/scrum-kernel/overview.md")
    wanted = [
        ("a relayed word is traceable, not verified (supporter.md body)", in_body, "they do not prove who sent it"),
        ("a relayed word is traceable, not verified (convention 14)", in_convention, "they do not verify who sent it"),
        ("a relay is trusted because the PO set up this Supporter (supporter.md body)", in_body, "trusted because the Product Owner set up this Supporter"),
        ("a relay is trusted because the PO set up this Supporter (convention 14)", in_convention, "trusted because the Product Owner set up this Supporter"),
        ("the host's session name is noted (supporter.md body)", in_body, "which session sent a message"),
        ("the host's session name is noted (convention 14)", in_convention, "which session sent a message"),
        ("a question still waiting for the PO, a go-ahead no handover covers included, is the Supporter's (supporter.md body)", in_body, "a go-ahead no handover covers included"),
        ("a question still waiting for the PO, a go-ahead no handover covers included, is the Supporter's (convention 14)", in_convention, "a go-ahead no handover covers included"),
        ("what the PO has decided about scope, items or a go-ahead goes to the Scrum Master (supporter.md body)", in_body, "decided or answered something about scope, items or a go-ahead, hand it to the Scrum Master"),
        ("what the PO has decided about scope, items or a go-ahead goes to the Scrum Master (convention 14)", in_convention, "decided or answered something about scope, items or a go-ahead, the Supporter hands it to the Scrum Master"),
    ]
    absent = [name for name, text, needle in wanted if needle not in text]
    check("Codex review fixes 2 and 3: the %d sentences are in" % len(wanted), not absent, "missing: %s" % absent if absent else "%d of %d present" % (len(wanted), len(wanted)))
    stale = "go to the Scrum Master, who chooses the receiving session and records them"
    check("the old ambiguous routing sentence is gone from supporter.md and convention 14",
          stale not in supporter_text and "Scope or item changes, go-aheads and the Product Owner's answers about them" not in in_convention)

    # --- the five small fixes after the Review (the Increment was returned): the sentences are in
    quick = [read("docs/quick-start.md"), read("docs/quick-start.zh-CN.md")]
    convention12 = re.search(r"^12\. \*\*Product Owner decides between stages\*\*.*$", in_convention, re.M)
    after_review = [
        ("1 a relay about scope, items or a go-ahead has the Scrum Master as its receiver (supporter.md body)", in_body,
         "for what the Product Owner has decided or answered about scope, items or a go-ahead it is the Scrum Master"),
        ("1 the same (convention 14)", in_convention,
         "for what the Product Owner has decided or answered about scope, items or a go-ahead it is the Scrum Master"),
        ("1 supporter.md points at convention 14, The answers back (no double quotes: in this file they mark SGEP phrases)", in_body, "*The answers back*"),
        ("1 convention 14 points at the supporter entry", in_convention, "the `supporter` entry says the same"),
        ("2 the relay says where the Product Owner said it (supporter.md body)", in_body, "where they said it (the session's name and the time)"),
        ("2 the relay says where the Product Owner said it (convention 14)", in_convention, "where the Product Owner said it (the session's name and the time)"),
        ("3 convention 12 says it is not a tool permission", in_convention, "wait for explicit stage permission (not a tool permission) for that stage and scope"),
        ("4 with no Scrum Master session the second step goes to the Product Owner (convention 14)", in_convention,
         "with no Scrum Master session, this step goes straight to the Product Owner"),
        ("5 quick start (English) hands the board to the supporter", quick[0], "Hand it to the supporter: `/ideo-scrum:supporter` in Claude Code, `/supporter` in DSH."),
        ("5 quick start (Chinese) hands the board to the supporter", quick[1], "交给 supporter（秘书）：Claude Code 用 `/ideo-scrum:supporter`，DSH 用 `/supporter`。"),
    ]
    absent = [name for name, text, needle in after_review if needle not in text]
    check("the Review fixes 1–5: the %d sentences are in" % len(after_review), not absent,
          "missing: %s" % absent if absent else "%d of %d present" % (len(after_review), len(after_review)))
    check("convention 12 writes stage permission five times and no bare 'explicit permission'",
          bool(convention12) and convention12.group(0).count("stage permission") == 5 and "explicit permission" not in convention12.group(0),
          "%d times" % convention12.group(0).count("stage permission") if convention12 else "convention 12 not found")
    print("\n%d check(s) failed" % len(failures) if failures else "\nall checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
