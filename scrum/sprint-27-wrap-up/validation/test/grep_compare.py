"""Sprint 27 Test: run the two frozen grep commands (chapter 2.2, "搜索命令") over a commit and compare the hits with the
table of released hits in 2.2. A hit that is not in the table, or a listed hit that is gone, fails.

    python -X utf8 -I grep_compare.py [TREE-ISH]        default HEAD

The two patterns are those of 2.2; the only addition is the tree-ish, which makes git read the commit and not the
working copy.
"""
import subprocess
import sys

import pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
PATHS_CMD = ["-E", "conventions/(board-log|scrum-board-template|(product|sprint|design|ideo)-backlog-template)"]
# The seven old wordings are split in the source on purpose: written whole, this file would be the 15th hit of the very
# grep it runs once it is committed. Joined with "|" they are the 2.2 pattern letter for letter.
WORDS = ["PO assis" "tant", "PO 助" "手", "standing assis" "tant", "standing hel" "per", r"\bstanding Stake" "holder",
         "常驻的助" "手", "助手会" "话"]
WORDS_CMD = ["-i", "-E", "|".join(WORDS)]
LOG = "scrum/sprint-27-wrap-up/SprintBacklog.md"
# copied from chapter 2.2, "放行的命中，逐处列出"
RELEASED_PATHS = {
    "scrum/documents/sprint/sprint-09-design-template.md:60",
    "scrum/documents/conventions-review-log.md:24",
}
RELEASED_WORDS = {
    "scrum/documents/sprint/sprint-18-rules-first.md:35",
    "scrum/documents/sprint/sprint-22-project-agents.md:81",
    "scrum/ProductBacklog.md:57", "scrum/ProductBacklog.md:77", "scrum/ProductBacklog.md:117", "scrum/ProductBacklog.md:145",
    "scrum/documents/sprint-roadmap.md:66",
    "CHANGELOG.md:11",
} | {"%s:%d" % (LOG, n) for n in (60, 61, 65, 77, 119, 123)}


def hits(tree, pattern_args):
    out = subprocess.run(["git", "-C", str(REPO), "grep", "-n", *pattern_args, tree], capture_output=True, text=True,
                         encoding="utf-8").stdout
    found = set()
    for line in out.splitlines():
        rest = line[len(tree) + 1:] if line.startswith(tree + ":") else line  # "<tree>:<path>:<line>:<text>"
        path, number, _ = rest.split(":", 2)
        found.add("%s:%s" % (path, number))
    return found


def main():
    tree = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    rc = 0
    for label, args, released in (("old paths", PATHS_CMD, RELEASED_PATHS), ("old wording", WORDS_CMD, RELEASED_WORDS)):
        found = hits(tree, args)
        extra, gone = sorted(found - released), sorted(released - found)
        ok = not extra and not gone
        rc |= not ok
        print("%s %s: %d hit(s), %d released in 2.2%s%s" % ("PASS" if ok else "FAIL", label, len(found), len(released),
                                                         "; NOT released: %s" % extra if extra else "",
                                                         "; released but gone: %s" % gone if gone else ""))
    return rc


if __name__ == "__main__":
    sys.exit(main())
