"""Sprint 26, Codex review follow-up: every file path the draft Memory names must resolve from the memory skill's folder.

    python -X utf8 -I scripts/check_paths.py [--plugin [DIR]]     --plugin: the files that landed in plugins/ideo-scrum/skills/memory/

The memory skill will live at plugins/ideo-scrum/skills/memory/; its list line says `Read details/x.md first.` and the details
files name other files by paths written from that same folder (`../design-kernel/steps/2-1-make-a-map.md`,
`../../template/design-backlog-template.md`, `../../board/board-log.md`). `details/...` resolves against the draft
(memory-draft/details/); everything else is resolved on disk from where the skill folder will be. A bare `design-kernel/...`,
`steps/...` or `conventions/...` path is reported as one that cannot resolve from there. Paths that name the project's own
places (`scrum/documents/`) are not plugin files and are not checked.
"""
from __future__ import annotations

import glob
import os
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SPRINT = HERE.parent
ROOT = SPRINT.parents[1]
SKILL_DIR = ROOT / "plugins" / "ideo-scrum" / "skills" / "memory"
if "--plugin" in sys.argv:  # the files that landed: details/ and the list (SKILL.md) in the plugin's memory skill
    _i = sys.argv.index("--plugin")
    MEM = pathlib.Path(sys.argv[_i + 1]) if _i + 1 < len(sys.argv) and not sys.argv[_i + 1].startswith("--") else SKILL_DIR
    LISTFILE = MEM / "SKILL.md" if (MEM / "SKILL.md").exists() else MEM / "MEMORY.md"
else:
    MEM = SPRINT / "memory-draft"
    LISTFILE = MEM / "MEMORY.md"

TOKEN = re.compile(r"`([^`\n]+)`|(?<![\w/.-])((?:\.\./)+[\w./-]+|details/[\w-]+\.md)")


def paths_in(text: str) -> list[str]:
    out = []
    for m in TOKEN.finditer(text):
        tok = (m.group(1) or m.group(2) or "").strip()
        if "…" in tok or " " in tok or "<" in tok:
            continue
        if re.match(r"^(\.\./)+[\w./-]+$", tok) or re.match(r"^details/[\w-]+\.md$", tok) or re.match(r"^(design-kernel|ideo-kernel|scrum-kernel|sprint-kernel|steps|conventions|template)/[\w./-]+$", tok):
            out.append(tok.rstrip("."))
    return out


def resolves(tok: str) -> tuple[bool, str]:
    if tok.startswith("details/"):
        return (MEM / tok).exists(), "memory-draft/" + tok
    if not tok.startswith("../"):
        return False, "a bare path does not resolve from the memory skill's folder"
    target = pathlib.Path(os.path.normpath(SKILL_DIR / tok))
    return target.exists(), str(target.relative_to(ROOT)).replace("\\", "/") if target.is_relative_to(ROOT) else str(target)


def check() -> list[str]:
    problems = []
    files = [LISTFILE] + sorted(pathlib.Path(p) for p in glob.glob(str(MEM / "details" / "*.md")))
    for f in files:
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), start=1):
            for tok in paths_in(line):
                ok, where = resolves(tok)
                if not ok:
                    problems.append(f"{f.name}:{n}: `{tok}` -> {where}")
    return problems


def selftest() -> int:
    ok = True
    for what, cond in (
        ("a bare design-kernel path is reported", not resolves("design-kernel/steps/2-1-make-a-map.md")[0]),
        ("a path from the skill's folder resolves", resolves("../design-kernel/steps/2-1-make-a-map.md")[0]),
        ("the template resolves", resolves("../../template/design-backlog-template.md")[0]),
        ("the board file stays resolvable", resolves("../../board/board-log.md")[0]),
        ("paths are found in backticks", paths_in("see `../x/y.md` and `details/roles.md`") == ["../x/y.md", "details/roles.md"]),
    ):
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    probs = check()
    for p in probs:
        print(p)
    print(f"{len(probs)} unresolved paths" if probs else "all file paths resolve from the memory skill's folder")
    sys.exit(1 if probs else 0)
