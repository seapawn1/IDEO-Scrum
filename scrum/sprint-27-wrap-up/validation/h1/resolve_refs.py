"""H1 evidence: resolve the relative paths written inside the six moved files against the base each file declares.

board-log.md declares the scrum-kernel skill folder as the base of its paths; design-backlog-template.md says its
excerpt paths are relative to the design-kernel skill folder. The other three templates name files in prose together
with their skill's folder, so there is little to resolve. Two reports are expected and are not defects: a token that is
an example in the text (`sprint-01-alpha/SprintBacklog.md` in board-log.md) and `overview.md` in the sprint log
template, which the template itself places "in the scrum-kernel skill folder".

    python -X utf8 -I resolve_refs.py
"""
import pathlib
import re
import sys

PLUGIN = pathlib.Path(__file__).resolve().parents[4] / "plugins" / "ideo-scrum"
CHECKS = [
    (PLUGIN / "board" / "board-log.md", PLUGIN / "skills" / "scrum-kernel"),
    (PLUGIN / "template" / "design-backlog-template.md", PLUGIN / "skills" / "design-kernel"),
    (PLUGIN / "template" / "sprint-backlog-template.md", PLUGIN / "skills" / "sprint-kernel"),
    (PLUGIN / "template" / "product-backlog-template.md", PLUGIN / "skills" / "scrum-kernel"),
    (PLUGIN / "template" / "ideo-backlog-template.md", PLUGIN / "skills" / "ideo-kernel"),
]
TOKEN = re.compile(r"`([^`\s]+\.(?:md|html|json))`")
unresolved_total = 0
for file, base in CHECKS:
    text = file.read_text(encoding="utf-8")
    seen, unresolved, skipped = [], [], []
    for token in TOKEN.findall(text):
        if token in seen:
            continue
        seen.append(token)
        if "<" in token or "*" in token or token.startswith(("scrum/", "http")):
            skipped.append(token)  # a placeholder or a path inside the user's project
            continue
        if not ("/" in token or token in ("overview.md", "SKILL.md")):
            skipped.append(token)  # a bare name used in prose together with its skill's folder
            continue
        if not (base / token).resolve().exists():
            unresolved.append(token)
    print("%-36s base=%-14s paths=%-2d unresolved=%s | prose names or placeholders: %s" % (
        file.relative_to(PLUGIN), base.name, len(seen) - len(skipped), unresolved or "none", skipped))
    unresolved_total += len(unresolved)
print("unresolved in total:", unresolved_total, "(2 expected: the example path and the prose overview.md, see the docstring)")
sys.exit(0)
