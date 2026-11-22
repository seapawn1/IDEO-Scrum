"""H1 evidence: dead relative links in the tracked markdown, and which of them a change newly breaks.

    python -X utf8 -I dead_links.py               every dead relative link in the tracked markdown, now
    python -X utf8 -I dead_links.py --base REV    only the links that worked at REV and are dead now

Sprint 27 (PBI-85) moved the log templates and the board files; the baseline 1145382 had no dead link at all.
"""
import argparse
import pathlib
import posixpath
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[4]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s#]+)(?:#[^)]*)?\)")


def git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True, encoding="utf-8").stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base")
    args = ap.parse_args()
    base_paths = set(git("ls-tree", "-r", "--name-only", args.base).splitlines()) if args.base else set()
    base_dirs = {posixpath.dirname(p) for p in base_paths}
    dead, files, links = [], 0, 0
    for rel in git("ls-files").splitlines():
        if not rel.endswith(".md"):
            continue
        files += 1
        text = (REPO / rel).read_text(encoding="utf-8", errors="replace")
        for target in LINK.findall(text):
            if re.match(r"^[a-z]+:", target) or target.startswith(("#", "/", "<")):
                continue
            links += 1
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(rel), target))
            if (REPO / resolved).exists():
                continue
            if args.base and resolved not in base_paths and resolved not in base_dirs:
                continue  # it did not work at the base either
            dead.append((rel, target))
    print("scanned %d tracked markdown files, %d relative links" % (files, links))
    print("dead relative links%s: %d" % (" that worked at " + args.base if args.base else "", len(dead)))
    for rel, target in dead:
        print("  %s -> %s" % (rel, target))
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
