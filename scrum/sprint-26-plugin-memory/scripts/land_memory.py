"""Sprint 26 row 12: land the Memory in the plugin. A dry run unless told to apply.

    python -X utf8 -I scripts/land_memory.py              dry run: check every precondition and say what would change
    python -X utf8 -I scripts/land_memory.py --apply      do it (the working tree only; nothing is committed); writes review/landing-changes.md
    python -X utf8 -I scripts/land_memory.py --stage DIR  write only the memory skill (SKILL.md and details/) to DIR, so
                                                          clause_coverage.py --plugin DIR and check_paths.py --plugin DIR can run first
    python -X utf8 -I scripts/land_memory.py --selftest

What it does, in this order:
  1. plugins/ideo-scrum/skills/memory/SKILL.md   frontmatter (name, one quoted description line, the shape the DSH adapter's
                                                 readEntry accepts) + the assembled list (memory-draft/MEMORY.md), unchanged
  2. plugins/ideo-scrum/skills/memory/details/   the 15 details files from memory-draft/details/, each without its
                                                 "Open points for the Product Owner" section, without the drafting note that says
                                                 the text is "the old rules word for word", and with the few sentences that
                                                 told the history of the old convention files said plainly (FIXES)
  3. git rm of the five old convention files (the board conventions stay in board/)
  4. the five role entries (commands/*.md): `ideo-scrum:memory` is called last; the subagent sentence names memory; the
     Supporter's relay wording follows the PO's decision of 2026-11-23 (an authorized Supporter's relay counts)
  5. dsh/index.js and scripts/check_dsh.mjs: the DSH adapter registers and preloads memory (the change tested on the copy,
     review/memory-outline.md section 10); the hint to call `memory` again after a compaction is a named context that DSH
     replays every turn (Master 2026-11-23, "writing B": the role text, where the routing sentence lives, is replaced by a
     summary when the conversation is compacted), with a check_dsh assertion
  6. ATTRIBUTION.md: the quotation sites move from scrum-kernel/conventions/ to skills/memory/details/
It touches nothing else: the references in the kernels' SKILL.md, the templates, docs, README (row 13) are not edited here.
Every replacement must match exactly once, or the run stops before it writes anything.
"""
from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
SPRINT = HERE.parent
ROOT = SPRINT.parents[1]
PLUG = ROOT / "plugins" / "ideo-scrum"
MEM = PLUG / "skills" / "memory"
DRAFT = SPRINT / "memory-draft"
CHANGES = SPRINT / "review" / "landing-changes.md"

DESC = ("Use only when summoned: an ideo-scrum role command tells you to load it, or the user asks for the plugin's Memory "
        "(the shared rules every role follows). When summoned, invoke this skill before answering, even for a short request. "
        "General questions about Scrum or design that do not name this plugin are not a summons: answer normally without loading it.")
OLD_FILES = [
    "plugins/ideo-scrum/skills/scrum-kernel/overview.md",
    "plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md",
    "plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md",
    "plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md",
    "plugins/ideo-scrum/skills/ideo-kernel/conventions/ideo-log.md",
]
ROLES = ["developer", "designer", "scrum-master", "stakeholder", "supporter"]
PROVENANCE = re.compile(r" The text is the old rules? word for word, cut into bullets(?:; the old pointers to convention numbers became handles)?\.")
OPEN_POINTS = re.compile(r"\n## Open points for the Product Owner\n.*?(?=\n## |\Z)", re.S)
FIXES = {  # sentences that told the history of the old files, said plainly now that the old files are gone
    "gates.md": [("Sprint 27 changed convention 12 in two ways, both here: it says *stage* permission (not a tool permission), and the Product Owner's own words relayed by the Supporter count as theirs.",
                  "Here *stage* permission means the Product Owner's permission to enter or return to a stage (not a tool permission), and the Product Owner's own words relayed by the Supporter count as theirs.")],
    "flow-maps.md": [("The process maps of the six old convention files, with the lines (handles)", "The process maps of the whole flow and of each log, with the lines (handles)")],
}


def skill_md() -> str:
    body = (DRAFT / "MEMORY.md").read_text(encoding="utf-8")
    assert "\n" not in DESC and '"' not in DESC
    return f'---\nname: memory\ndescription: {json.dumps(DESC, ensure_ascii=False)}\n---\n\n{body}'


def detail(name: str, text: str) -> tuple[str, list[str]]:
    """One details file as it lands, and what was done to it (for the change list)."""
    notes = []
    new = OPEN_POINTS.sub("", text).rstrip("\n") + "\n"
    if new != text:
        notes.append("the Open points for the Product Owner section removed")
    out = PROVENANCE.sub("", new)
    if out != new:
        notes.append("the drafting note \"the text is the old rules word for word\" removed")
    for old, repl in FIXES.get(name, []):
        if out.count(old) != 1:
            raise SystemExit(f"{name}: expected exactly one match for {old[:60]!r}, found {out.count(old)}")
        out = out.replace(old, repl)
        notes.append(f"said plainly: {old[:70]}…")
    return out, notes


def sub_once(text: str, pat: str, repl: str, what: str, regex: bool = False) -> str:
    n = len(re.findall(pat, text)) if regex else text.count(pat)
    if n != 1:
        raise SystemExit(f"{what}: expected exactly one match, found {n}")
    return re.sub(pat, repl, text, count=1) if regex else text.replace(pat, repl)


def entry(name: str, text: str) -> str:
    text = sub_once(text, r"(call the Skill tool in this order: (?:`[^`]+`(?: → )?)+)\.", r"\1 → `ideo-scrum:memory`.", f"{name}: the loading sentence", regex=True)
    text = sub_once(text, "Subagents you dispatch load the ideo-kernel and scrum-kernel skills too.",
                    "Subagents you dispatch load the ideo-kernel, scrum-kernel and memory skills too.", f"{name}: the subagent sentence")
    if name == "supporter":
        text = sub_once(text, ", with the date and where they said it. Tool permissions and settings, changes to `CLAUDE.md` or `AGENTS.md`, and outward actions such as a push or a release are not covered: those need the Product Owner's own confirmation, and a relay does not stand in for it.",
                        ", with the date and where they said it. That includes tool permissions and settings, changes to `CLAUDE.md` or `AGENTS.md`, and outward actions such as a push or a release, once the Product Owner has authorized you to relay them: say in the relay when and where they authorized you. The host keeps its own check: where it asks (a permission prompt, a setting, `CLAUDE.md`), the Product Owner confirms in the session that acts.",
                        "supporter: the relay limit")
        text = sub_once(text, "the rule, and what it does not cover, is in `overview.md`, convention 14.",
                        "the rule is in the Memory (`po-word-relayed`, `relay-limits`); for tool permissions and settings, `CLAUDE.md` or `AGENTS.md`, a push or a release, the relay also says when and where the Product Owner authorized you.",
                        "supporter: the relay bullet")
    return text


MEMORY_CONTEXT = """  // DSH replays a named runtime context every turn, also after a compaction has replaced the role text with a summary;
  // the hint to call `memory` again lives here and not in the role routing, which the summary would swallow.
  ctx.effect(() => ctx.systemPrompt.context({
    name: 'ideo-scrum:memory',
    order: 120,
    interpolate: false,
    text: ({ agent }) => agent
      ? 'ideo-scrum Memory: if you are working as an ideo-scrum role and the text of the `memory` skill is no longer in this conversation, for example because the conversation was compacted, call the `skill` tool with `{"name":"memory"}` before going on.'
      : '',
  }))
"""

CHECK_TEST = """test('replay the Memory reload hint as a named context, only for an agent', () => {
  const { contexts, dispose } = mount()
  const section = contexts.get('ideo-scrum:memory')
  assert.equal(section.interpolate, false)
  assert.equal(section.text({}), '')
  const text = section.text({ agent: { session: { cwd: tmpdir() } } })
  assert.match(text, /`memory`/)
  assert.match(text, /compacted/)
  dispose()
  assert.equal(contexts.size, 0)
})
"""


def dsh_index(text: str) -> str:
    text = sub_once(text, "const kernels = ['ideo-kernel', 'scrum-kernel', 'sprint-kernel', 'design-kernel']",
                    "const kernels = ['ideo-kernel', 'scrum-kernel', 'sprint-kernel', 'design-kernel', 'memory']", "dsh/index.js: the kernels list")
    text = sub_once(text, "The IDEO and Scrum kernels are already loaded below, in that order; do not call `skill` again for those. Load",
                    "The IDEO and Scrum kernels and the Memory are already loaded below, in that order; do not call `skill` again for those. Load",
                    "dsh/index.js: the routing sentence")
    text = sub_once(text, "return entries.slice(0, 2).map(entry => [",
                    "return ['ideo-kernel', 'scrum-kernel', 'memory'].map(name => entries.find(entry => entry.name === name)).map(entry => [", "dsh/index.js: the prelude")
    return sub_once(text, "      return readCommitments(ctx.workingDirectory.get(agent.session))\n    },\n  }))\n}",
                    "      return readCommitments(ctx.workingDirectory.get(agent.session))\n    },\n  }))\n" + MEMORY_CONTEXT + "}", "dsh/index.js: the named context")


def dsh_check(text: str) -> str:
    text = sub_once(text, "assert.deepEqual([...skills.keys()], [...kernels, ...roles])", "assert.deepEqual([...skills.keys()], [...kernels, 'memory', ...roles])", "check_dsh.mjs: the registered names")
    text = sub_once(text, "      const scrum = canonical(join(plugin, 'skills', 'scrum-kernel', 'SKILL.md')).content\n",
                    "      const scrum = canonical(join(plugin, 'skills', 'scrum-kernel', 'SKILL.md')).content\n      const memory = canonical(join(plugin, 'skills', 'memory', 'SKILL.md')).content\n", "check_dsh.mjs: the memory body")
    text = sub_once(text, "      assert.ok(i >= 0 && s > i, `${name} must preload the two verbatim bodies in order`)",
                    "      const m = entry.content.indexOf(memory)\n      assert.ok(i >= 0 && s > i && m > s, `${name} must preload the ideo and scrum bodies and the Memory, in that order`)", "check_dsh.mjs: the preload assertion")
    return text.rstrip("\n") + "\n\n" + CHECK_TEST


QUOTES = "`plugins/ideo-scrum/skills/scrum-kernel/conventions/`（约定里的嵌入引用，句中注明出处）"


def attribution(text: str) -> str:
    head, sep, tail = text.partition("## 2. Scrum Guide Expansion Pack (2026.1)")
    if not sep:
        raise SystemExit("ATTRIBUTION.md: section 2 not found")
    head = sub_once(head, QUOTES, "`plugins/ideo-scrum/skills/memory/details/`（`roles.md`、`goal-fixed.md`、`sprint.md`、`departures.md` 里的嵌入引用，文件头与句中注明出处）", "ATTRIBUTION.md section 1")
    tail = sub_once(tail, QUOTES, "`plugins/ideo-scrum/skills/memory/details/`（`departures.md` 里的嵌入引用，文件头与句中注明出处）", "ATTRIBUTION.md section 2")
    return head + sep + tail


def plan() -> tuple[dict[pathlib.Path, str], dict[str, list[str]]]:
    """Every file to write, with its new text, and what was done to each details file; raises before anything is written when a precondition fails."""
    out: dict[pathlib.Path, str] = {}
    notes: dict[str, list[str]] = {}
    out[MEM / "SKILL.md"] = skill_md()
    for p in sorted((DRAFT / "details").glob("*.md")):
        out[MEM / "details" / p.name], notes[p.name] = detail(p.name, p.read_text(encoding="utf-8"))
    for r in ROLES:
        p = PLUG / "commands" / f"{r}.md"
        out[p] = entry(r, p.read_text(encoding="utf-8"))
    for rel, fn in (("dsh/index.js", dsh_index), ("scripts/check_dsh.mjs", dsh_check), ("ATTRIBUTION.md", attribution)):
        p = ROOT / rel
        out[p] = fn(p.read_text(encoding="utf-8"))
    for rel in OLD_FILES:
        if not (ROOT / rel).exists():
            raise SystemExit(f"{rel}: the old convention file is not there")
    return out, notes


def checks(files: dict[pathlib.Path, str]) -> list[str]:
    errs = []
    skill = files[MEM / "SKILL.md"]
    m = re.match(r'^---\nname: memory\ndescription: ("[^\n]*")\n---\n', skill)
    if not m:
        errs.append("SKILL.md: the frontmatter is not name + one quoted description line")
    elif len(json.loads(m.group(1))) > 1024:
        errs.append("SKILL.md: the description is over 1024 characters")
    body = skill[m.end():] if m else skill
    if len(body) > 16000:
        errs.append(f"SKILL.md: the list is {len(body)} characters (cap 16,000)")
    for ln in body.splitlines():
        if ln.startswith("- **") and len(ln) > 150:
            errs.append(f"SKILL.md: a line of {len(ln)} characters: {ln[:60]}")
    for p, t in files.items():
        if p.parent == MEM / "details":
            if "Open points for the Product Owner" in t:
                errs.append(f"{p.name}: the Open points section is still there")
            if "word for word, cut into bullets" in t:
                errs.append(f"{p.name}: the drafting note is still there")
            if re.search(r"\bconventions? \d", t):
                errs.append(f"{p.name}: still names an old convention number")
    return errs


def write_changes(files: dict[pathlib.Path, str], notes: dict[str, list[str]]) -> None:
    lines = ["# 落盘后与审定的草稿不同的地方（Sprint 26 行 12）", "",
             "由 `scripts/land_memory.py --apply` 生成。清单（`SKILL.md` 的正文）与草稿 `memory-draft/MEMORY.md` 逐字相同，没有差异；下面是细则文件与别处落盘时做的事。", "",
             "## 细则文件（`skills/memory/details/`）与草稿的差别", "", "| 文件 | 做了什么 |", "| --- | --- |"]
    for name, ns in notes.items():
        lines.append(f"| `{name}` | {'；'.join(ns) if ns else '没有差别'} |")
    lines += ["", "## 别处", "",
              "- `skills/memory/SKILL.md`：新建，frontmatter（`name: memory`、一行带引号的描述，不超过 1024 字符）加上面说的清单正文。",
              "- `commands/{developer,designer,scrum-master,stakeholder,supporter}.md`：加载序列最后加 `ideo-scrum:memory`；「Subagents you dispatch load…」那句加上 memory；`supporter.md` 的转达限制按 PO 2026-11-23 的决定改（经授权的 Supporter 转达也算，写明何时何地授权；宿主自己的确认照宿主来）。",
              "- `dsh/index.js`、`scripts/check_dsh.mjs`：DSH 适配器注册并预载 memory；压缩后重新调用 memory 的提示放在每轮回放的命名上下文 `ideo-scrum:memory` 里（Master 2026-11-23：写法 B），`check_dsh` 加了一项断言。",
              "- `ATTRIBUTION.md`：引用位置由 `scrum-kernel/conventions/` 改为 `skills/memory/details/`。",
              "- 删除（`git rm`）：" + "、".join(f"`{p.split('plugins/ideo-scrum/')[1]}`" for p in OLD_FILES) + "。`board/board-log.md` 留在原处。", ""]
    CHANGES.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def apply(files: dict[pathlib.Path, str], notes: dict[str, list[str]]) -> None:
    for p, t in files.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(t, encoding="utf-8", newline="\n")
    subprocess.run(["git", "rm", "-q", "--", *OLD_FILES], cwd=ROOT, check=True)
    write_changes(files, notes)


def stage(dest: pathlib.Path, files: dict[pathlib.Path, str]) -> None:
    for p, t in files.items():
        if p == MEM / "SKILL.md" or p.parent == MEM / "details":
            q = dest / p.relative_to(MEM)
            q.parent.mkdir(parents=True, exist_ok=True)
            q.write_text(t, encoding="utf-8", newline="\n")


def selftest() -> int:
    ok = True

    def check(cond: bool, what: str) -> None:
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    t = "# T\n\nIntro. The text is the old rules word for word, cut into bullets; the old pointers to convention numbers became handles. More.\n\n## A\n\n- x\n\n## Open points for the Product Owner\n\n- None.\n\n## B\n\n- y\n"
    d, n = detail("x.md", t)
    check("Open points" not in d and "## B" in d and "- y" in d and "- x" in d, "the Open points section goes, the sections around it stay")
    check("word for word, cut" not in d and "Intro. More." in d and len(n) == 2, "the drafting note goes and the sentence closes up")
    check(detail("x.md", "## A\n\n- x\n\n## Open points for the Product Owner\n\n- None.\n")[0].rstrip().endswith("- x"), "an Open points section at the end of the file goes too")
    check("old rule word" not in detail("x.md", "Intro. The text is the old rule word for word, cut into bullets. More.\n")[0], "the shorter variant of the drafting note goes too")
    e = entry("developer", "x call the Skill tool in this order: `ideo-scrum:ideo-kernel` → `ideo-scrum:scrum-kernel` → `ideo-scrum:sprint-kernel`. Wait. Subagents you dispatch load the ideo-kernel and scrum-kernel skills too.")
    check("→ `ideo-scrum:sprint-kernel` → `ideo-scrum:memory`." in e and "scrum-kernel and memory skills too" in e, "an entry calls memory last and its subagents load it")
    try:
        entry("developer", "no loading sentence here")
        check(False, "an entry without the loading sentence stops the run")
    except SystemExit:
        check(True, "an entry without the loading sentence stops the run")
    fm = skill_md()
    check(fm.startswith("---\nname: memory\ndescription: \"") and json.loads(re.match(r'^---\nname: memory\ndescription: ("[^\n]*")\n---\n', fm).group(1)) == DESC, "the SKILL.md frontmatter is the shape the DSH adapter reads")
    check(len(DESC) <= 1024, f"the description is {len(DESC)} characters")
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    files, notes = plan()
    if "--stage" in argv:
        dest = pathlib.Path(argv[argv.index("--stage") + 1])
        stage(dest, files)
        print(f"the memory skill is staged in {dest}")
        return 0
    errs = checks(files)
    new = [p for p in files if not p.exists()]
    changed = [p for p in files if p.exists() and p.read_text(encoding="utf-8") != files[p]]
    print(f"{len(new)} files to create, {len(changed)} to change, {len(OLD_FILES)} to remove (git rm)")
    for p in new + changed:
        print(("  new     " if p in new else "  changed ") + p.relative_to(ROOT).as_posix())
    for rel in OLD_FILES:
        print("  remove  " + rel)
    for e in errs:
        print("  PROBLEM " + e)
    if errs:
        return 1
    if "--apply" not in argv:
        print("dry run: nothing written (use --apply)")
        return 0
    apply(files, notes)
    print("applied: the working tree is changed, nothing is committed; the change list is review/landing-changes.md")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
