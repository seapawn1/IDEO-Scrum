"""Sprint 26 row 13, by hand: the references that migrate_refs.py has no rule for (the kernels' sections, the five entries, the
template headers, the board brief, the Chinese "第 N 条" lines, the docs, README, AGENTS.md lines 44 and 56, check_docs.py,
check_dsh.mjs, the hook comment). Every replacement must match exactly once, or nothing is written.

A record: it ran once (2026-11-23), and the old sentences it matches are gone, so a second run stops at the first one.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
texts: dict[str, str] = {}
bad: list[tuple] = []


def get(p: str) -> str:
    if p not in texts:
        texts[p] = (ROOT / p).read_text(encoding="utf-8")
    return texts[p]


def sub(p: str, old: str, new: str, count: int = 1) -> None:
    t = get(p)
    n = t.count(old)
    if n != count:
        bad.append((p, n, old[:90]))
        return
    texts[p] = t.replace(old, new)


SK = "plugins/ideo-scrum/skills/"
CMD = "plugins/ideo-scrum/commands/"
TPL = "plugins/ideo-scrum/template/"

# ---------------------------------------------------------------- scrum-kernel
p = SK + "scrum-kernel/SKILL.md"
sub(p, "before using the product log template and conventions.", "before using the product log template and the Memory.")
sub(p, "## Conventions\n\nHow a solo + AI team keeps its product log and runs its Sprints is in `overview.md`, beside this file, and in the conventions: `conventions/` here for the product log, and the sprint-kernel skill's `conventions/` for running a Sprint. Start with the overview. When you write the product log or answer a question about how to do it, read the matching convention first, even for a rough answer. The references below are the official texts; the conventions depart from them on purpose in a few places — no Sprint end date, checkpoints instead of the Daily Scrum, a go-ahead before building — and the overview lists them all. Running a Sprint is the sprint-kernel skill's work: `../sprint-kernel/conventions/sprint-log.md` has the five stages and the close, and its `events/` holds the five Scrum events.",
    "## The Memory\n\nHow a solo + AI team keeps its product log and runs its Sprints is in the memory skill (`../memory/SKILL.md`): one list of rules, a line each, with a details file in `../memory/details/` behind the longer ones. The role commands load it after the kernels; if it is not loaded yet, invoke `ideo-scrum:memory` first. A line that ends in `Read details/<file>.md first.` needs that file read before you act on it. When you write the product log or answer a question about how to do it, read the Memory's *The product log* section first, even for a rough answer. The references below are the official texts; the Memory departs from them on purpose in a few places — no Sprint end date, checkpoints instead of the Daily Scrum, a go-ahead before building — and `../memory/details/departures.md` lists them all. Running a Sprint is the sprint-kernel skill's work: the Memory's *Running a Sprint* section has the five stages and the close, and the sprint-kernel skill's `events/` holds the five Scrum events.")
sub(p, "read all of `overview.md`, `references/scrum-artifact-product-backlog.md`, and `conventions/product-log.md`, plus the full §1.2 comment in",
    "read the whole Memory list (`../memory/SKILL.md`) and, in full, `../memory/details/goal-fixed.md`, `../memory/details/product-log.md`, and `references/scrum-artifact-product-backlog.md`, plus the full §1.2 comment in")
sub(p, "reread the `Commitment: Product Goal` passage and the applicable conventions and template comment before redrafting.",
    "reread the `Commitment: Product Goal` passage and the applicable Memory lines, details files, and template comment before redrafting.")
sub(p, "| `overview.md` | How the product log, Sprints, and designs fit together; folders, including `scrum/documents/`; roles; what stays fixed | Starting a project, or unsure who does what or where a file goes |\n| `conventions/product-log.md` | Writing the product log and refining its items | Writing, refining, or refreshing the product log |",
    "| `../memory/SKILL.md` | The Memory: how the product log, Sprints, and designs fit together; folders, including `scrum/documents/`; roles; what stays fixed; writing the product log and refining its items. A details file in `../memory/details/` stands behind the longer rules | Starting a project, unsure who does what or where a file goes, or writing, refining, or refreshing the product log |")

# ---------------------------------------------------------------- sprint-kernel
p = SK + "sprint-kernel/SKILL.md"
sub(p, "Once summoned, read the sprint log conventions before planning or writing the log;", "Once summoned, read the Memory's Sprint rules before planning or writing the log;")
sub(p, "This kernel holds what running one takes: the sprint log conventions in `conventions/`, and the five Scrum events in `events/`. The product log, the roles, and the rest of Scrum stay in the scrum-kernel skill (`../scrum-kernel/SKILL.md`, `../scrum-kernel/overview.md`); read it first if it is not loaded yet.",
    "This kernel holds what running one takes: the five Scrum events in `events/`, and the pointers to the Sprint rules in the Memory (`../memory/SKILL.md`). The product log, the roles, and the rest of Scrum stay in the scrum-kernel skill (`../scrum-kernel/SKILL.md`); read it first if it is not loaded yet.")
sub(p, "## Conventions\n\nHow a solo + AI team runs a Sprint — the five stages, the sprint log, who decides — is in `conventions/sprint-log.md`; the sprint log template is `../../template/sprint-backlog-template.md`. These are working conventions, not source text: follow what fits, override what doesn't, and note why. When you open, run, or close a Sprint, write a log, or answer a question about how to do any of these, read the matching convention first, even for a rough answer.",
    "## The Memory\n\nHow a solo + AI team runs a Sprint — the five stages, the sprint log, who decides — is in the memory skill (`../memory/SKILL.md`), its *Running a Sprint* section, with the longer rules in `../memory/details/` (`sprint.md`, `gates.md`, `refinement.md`, `closing.md`, `handoff.md`); the sprint log template is `../../template/sprint-backlog-template.md`. The role commands load the Memory after the kernels; if it is not loaded yet, invoke `ideo-scrum:memory` first. These are working conventions, not source text: follow what fits, depart from what doesn't, and note why. When you open, run, or close a Sprint, write a log, or answer a question about how to do any of these, read the matching Memory lines first, even for a rough answer.")
sub(p, "| `conventions/sprint-log.md` | The five stages of a Sprint — Why, What, How, Increment, Test — and its close | Opening, running, or closing a Sprint |",
    "| `../memory/SKILL.md`, `../memory/details/sprint.md` | The Memory's Sprint rules: the five stages of a Sprint — Why, What, How, Increment, Test — and its close | Opening, running, or closing a Sprint |")
sub(p, "read `../scrum-kernel/overview.md`, `conventions/sprint-log.md`, and `events/scrum-event-sprint-planning.md` in full.",
    "read the whole Memory list (`../memory/SKILL.md`) and, in full, `../memory/details/sprint.md`, `../memory/details/goal-fixed.md`, `../memory/details/gates.md`, `../memory/details/refinement.md`, and `events/scrum-event-sprint-planning.md`.")
sub(p, "`../scrum-kernel/conventions/product-log.md`", "`../memory/details/product-log.md`")
sub(p, "follow the decisions in the sprint log conventions.", "follow the Memory's stage-gate rules (`stage-gates`).")

# ---------------------------------------------------------------- design-kernel
p = SK + "design-kernel/SKILL.md"
sub(p, "Once summoned, read the design log conventions; this research module", "Once summoned, read the Memory's design rules; this research module")
sub(p, "with their own log (`../ideo-kernel/conventions/ideo-log.md`); if you loaded", "with their own log (Memory `open-ideo-log`, `ideo-log-ends`); if you loaded")
sub(p, "## Conventions\n\nHow a solo + AI team runs a design — where the design log lives, who decides, how each stage works with subagents and role cards, and how a design ends — is in `conventions/design-log.md`. The design log template is `../../template/design-backlog-template.md`. These are working conventions, not source text: follow what fits, override what doesn't, and note why.",
    "## The Memory\n\nHow a solo + AI team runs a design — where the design log lives, who decides, how each stage works with subagents and role cards, and how a design ends — is in the memory skill (`../memory/SKILL.md`), its *Running a design sprint* section, with `../memory/details/design.md` for the stages and `../memory/details/design-ending.md` for the end. The design log template is `../../template/design-backlog-template.md`. The role commands load the Memory after the kernels; if it is not loaded yet, invoke `ideo-scrum:memory` first. These are working conventions, not source text: follow what fits, depart from what doesn't, and note why.")
sub(p, "Also read `../scrum-kernel/overview.md`, `../ideo-kernel/conventions/ideo-log.md`, `conventions/design-log.md`, and all the comments in",
    "Also read the whole Memory list (`../memory/SKILL.md`), `../memory/details/design.md`, `../memory/details/gates.md`, `../memory/details/roles.md`, and all the comments in")
sub(p, "Read the conventions whenever you open, run, or resume a design,", "Read the Memory's *Running a design sprint* lines, and the details file a line names, whenever you open, run, or resume a design,")
sub(p, "the conventions say how a solo + AI team does that step, and the conventions apply.", "the Memory (`../memory/details/design.md`) says how a solo + AI team does that step, and its rules apply.")

# ---------------------------------------------------------------- ideo-kernel
p = SK + "ideo-kernel/SKILL.md"
sub(p, "Read `conventions/ideo-log.md` for the boundary between a design sprint and the five modes.", "The Memory skill has the boundary between a design sprint and the five modes.")
sub(p, "## Conventions\n\nWhether a question needs a design sprint or the five modes, how the two relate, when to open an IDEO log, and how one ends are in `conventions/ideo-log.md`; the log template is `../../template/ideo-backlog-template.md`.",
    "## The Memory\n\nWhether a question needs a design sprint or the five modes, how the two relate, when to open an IDEO log, and how one ends are in the memory skill (`../memory/SKILL.md`), its *The five modes and the IDEO log* section, with `../memory/details/ideo-ending.md` for the end; the role commands load it last, and if it is not loaded yet, invoke `ideo-scrum:memory`. The log template is `../../template/ideo-backlog-template.md`.")
sub(p, "preserve the original as Memory `design-ends`, `design-conclusions`, says.", "preserve the original, as Memory `design-ends` says (`../memory/details/design-ending.md`).")

# ---------------------------------------------------------------- the five entries
ENTRY_OLD = "**Conventions**: how the product log, Sprints, and designs fit together, and who does what, is in `overview.md` in the scrum-kernel skill's folder; it points to the templates and the other conventions."
ENTRY_NEW = "**Memory**: how the product log, Sprints, and designs fit together, and who does what, is in the memory skill, loaded last above: one list of rules, a line each, with a details file behind the longer ones."
for name in ("developer", "scrum-master", "stakeholder", "supporter"):
    sub(CMD + name + ".md", ENTRY_OLD, ENTRY_NEW)
sub(CMD + "designer.md", ENTRY_OLD + " How a design runs with AI is in the design-kernel skill's `conventions/design-log.md`.",
    ENTRY_NEW + " How a design runs with AI is in the Memory's *Running a design sprint* section.")
sub(CMD + "designer.md", "from the design-kernel skill's conventions)", "from the design log template; the rules are in the Memory)")
sub(CMD + "developer.md", "goes where Memory `reviewer-required` says (`../skills/scrum-kernel/overview.md`).", "goes where Memory `ask-the-po` says.")
sub(CMD + "scrum-master.md", "(Memory `sprint-or-modes`, in the ideo-kernel skill's `conventions/` folder)", "(Memory `sprint-or-modes`)")
sub(CMD + "stakeholder.md", "(Memory `stakeholder-table`, relative to the scrum-kernel skill's folder)", "(Memory `stakeholder-table`)")
sub(CMD + "supporter.md", "following the board conventions in the scrum-kernel skill.", "following the Memory's board rules (`board-rules`, which points to `board/board-log.md`).")
sub(CMD + "supporter.md", "explain it from `overview.md` and the conventions it points to, and say where each rule comes from.", "explain it from the Memory and the details files it points to, and say where each rule comes from.")
sub(CMD + "supporter.md", "(the contact-point bullet above; Memory `who-gets-which-work`, `answers-back`, `po-word-relayed`, `relay-limits`, *The answers back*)", "(the contact-point bullet above; Memory `answers-back`)")

# ---------------------------------------------------------------- templates
sub(TPL + "product-backlog-template.md", "> How to write this log: `product-log.md` in the scrum-kernel skill's `conventions/` folder. How it fits with sprint and design logs: `overview.md`, beside the skill's `SKILL.md`.",
    "> How to write this log: the Memory's *The product log* section (the memory skill's `SKILL.md`). How it fits with sprint and design logs: `details/flow-maps.md` in the same skill.")
sub(TPL + "sprint-backlog-template.md", "> How to write this log: `sprint-log.md` in the sprint-kernel skill's `conventions/` folder.", "> How to write this log: the Memory's *Running a Sprint* section (the memory skill's `SKILL.md`).")
sub(TPL + "sprint-backlog-template.md", "(Memory `dod-in-product-log`, `dod-standards`; Memory `sprint-goal`, `share-goal-and-checks`)", "(Memory `dod-in-product-log`, `dod-standards`, `sprint-goal`, `share-goal-and-checks`)")
sub(TPL + "design-backlog-template.md", "> How to write this log: `design-log.md` in the design-kernel skill's `conventions/` folder.", "> How to write this log: the Memory's *Running a design sprint* section (the memory skill's `SKILL.md`).")
sub(TPL + "design-backlog-template.md", "not every step taken to get there (Memory `?`).", "not every step taken to get there.")
sub(TPL + "design-backlog-template.md", "(Memory `review-at-close`, `disputed-points`, in the sprint-kernel skill's `conventions/` folder)", "(Memory `review-at-close`, `disputed-points`)")
sub(TPL + "ideo-backlog-template.md", "> How to write this log: `ideo-log.md` in the ideo-kernel skill's `conventions/` folder.", "> How to write this log: the Memory's *The five modes and the IDEO log* section (the memory skill's `SKILL.md`).")
sub(TPL + "ideo-backlog-template.md", "how the two differ is Memory `sprint-or-modes`, in the ideo-kernel skill's `conventions/` folder.", "how the two differ is Memory `sprint-or-modes`.")

# ---------------------------------------------------------------- the board brief
p = "plugins/ideo-scrum/board/board-log.md"
sub(p, "follow what fits, override what doesn't, note why. Source labels and short names are explained in Memory `rule-labels`, in the scrum-kernel skill folder, beside its `SKILL.md`.",
    "follow what fits, depart from what doesn't, note why. Source labels and short names are explained in Memory `rule-labels` (`details/names.md` in the memory skill).")
sub(p, " Paths in this file, such as `overview.md`, `conventions/product-log.md` and those starting with `../`, are relative to the scrum-kernel skill folder, not to `board/`.", "")
sub(p, "- `> Now:` in a Sprint log (Memory `log-is-the-handoff`), a design log (Memory `log-is-the-handoff`), and an IDEO log (Memory `ideo-log-ends`); the product log has none;",
    "- `> Now:` in a Sprint log, a design log, and an IDEO log (Memory `log-is-the-handoff`); the product log has none;")

# ---------------------------------------------------------------- the hook comment
sub("plugins/ideo-scrum/hooks/commitments.sh", "(the rules are in convention 17 of `overview.md` in the scrum-kernel skill):", "(the rules are Memory `goal-fixed` and `commitment-table`):")

# ---------------------------------------------------------------- AGENTS.md (PO: 「可以修改agents.md」, 2026-11-22; lines 44 and 56 only)
sub("AGENTS.md", "不是原文的写法进 `conventions/`，标为约定建议。", "不是原文的写法进 Memory（`plugins/ideo-scrum/skills/memory/`），标为约定建议。")
sub("AGENTS.md", "流程见插件 sprint-kernel 的 `conventions/sprint-log.md`。", "流程见插件 Memory 的 `review-at-close`、`retro-in-memory`（细则在 `skills/memory/details/closing.md`）。")

# ---------------------------------------------------------------- docs
g = "docs/glossary.md"
M = "[Memory](../plugins/ideo-scrum/skills/memory/SKILL.md)"
sub(g, "[design-log](../plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md), [Memory](../plugins/ideo-scrum/skills/memory/SKILL.md) `sprint-or-modes`", M + " `designs-beside-sprints`, `sprint-or-modes`")
sub(g, "| [product-log](../plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md) |", "| " + M + " `one-product-log`, `write-product-log` |")
sub(g, "| [sprint-log](../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md) |", "| " + M + " `sprint-folder`, `templates-record-outputs` |")
sub(g, "| [design-log](../plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md) |", "| " + M + " `design-folder`, `design-stages` |")
sub(g, "One of the plugin's four skills holding conventions and source material: ideo, scrum, sprint, design. Claude Code role commands call their kernels in order; DSH role entries preload ideo and scrum, then load sprint and design as needed.",
    "One of the plugin's four skills holding methods and source material: ideo, scrum, sprint, design. The rules every role follows are in a fifth skill, the Memory. Claude Code role commands call their kernels in order, then the Memory; DSH role entries preload ideo, scrum and the Memory, then load sprint and design as needed.")
sub(g, "插件的四个技能之一：ideo、scrum、sprint、design，各自装着约定和原文。Claude Code 角色命令依次调用该角色的内核；DSH 的角色入口预载 ideo 和 scrum，sprint 和 design 按需加载。",
    "插件的四个技能之一：ideo、scrum、sprint、design，各自装着方法和原文。各角色共用的规矩在第五个技能 Memory 里。Claude Code 角色命令依次调用该角色的内核，再调用 Memory；DSH 的角色入口预载 ideo、scrum 和 Memory，sprint 和 design 按需加载。")
sub(g, "\n| commitments hook |",
    "\n| Memory | Memory | The plugin's one short list of working rules, a line each, with a details file behind the longer ones. Every role command loads it after the kernels, so the same rules hold without being told each time; where a rule does not fit, depart from it and say why in the log. | 插件的那份短规矩清单：一条一行，长的另有细则文件。每个角色命令在内核之后加载它，同一套规矩不用每次手动说明就能守；某条不合用时可以不照做，在日志里写明原因。 | " + M + " |\n| commitments hook |")

sub("docs/maintaining.md", "[`overview.md`](../plugins/ideo-scrum/skills/scrum-kernel/overview.md) (process overview and departures)",
    M + " (the rules every role follows; the departures from the official guides are in its `details/departures.md`)")
sub("docs/maintaining.zh-CN.md", "[`overview.md`](../plugins/ideo-scrum/skills/scrum-kernel/overview.md)（流程总览与官方指南差异）",
    M + "（各角色共用的规矩；与官方指南的差异在它的 `details/departures.md`）")
sub("docs/maintaining.zh-CN.md", "（[`overview.md`](../plugins/ideo-scrum/skills/scrum-kernel/overview.md) 第 17 条）", "（" + M + " 的 `goal-fixed`、`commitment-table`）")

sub("docs/quick-start.md", "This Claude Code command calls the IDEO, Scrum, Sprint, and Design kernels in that order before starting work; you don't need to call them yourself. See the [role convention](../plugins/ideo-scrum/skills/scrum-kernel/overview.md#who-does-what) for the other roles.",
    "This Claude Code command calls the IDEO, Scrum, Sprint, and Design kernels, then the Memory, in that order before starting work; you don't need to call them yourself. See the [role rules](../plugins/ideo-scrum/skills/memory/details/roles.md) for the other roles.")
sub("docs/quick-start.zh-CN.md", "这个 Claude Code 命令先依次调用 IDEO、Scrum、Sprint 和 Design 内核，再开始工作；不用你逐个调用。其他角色的顺序见[角色约定](../plugins/ideo-scrum/skills/scrum-kernel/overview.md#who-does-what)。",
    "这个 Claude Code 命令先依次调用 IDEO、Scrum、Sprint 和 Design 内核，再调用 Memory，然后开始工作；不用你逐个调用。其他角色的顺序见[角色规矩](../plugins/ideo-scrum/skills/memory/details/roles.md)。")
sub("docs/quick-start.zh-CN.md", "（[overview](../plugins/ideo-scrum/skills/scrum-kernel/overview.md)，第 12 条）", "（" + M + " 的 `stage-gates`）")
sub("docs/quick-start.zh-CN.md", "（[冲刺日志约定](../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md)，第 8 条）", "（" + M + " 的 `go-ahead`、`review-handover`）")
sub("docs/quick-start.zh-CN.md", "（overview，第 17 条）", "（Memory 的 `goal-fixed`、`commitment-table`）")
sub("docs/quick-start.zh-CN.md", "（冲刺日志约定，第 14 条）", "（Memory 的 `reviewer-required`）")
sub("docs/quick-start.zh-CN.md", "（冲刺日志约定，第 22 条）", "（Memory 的 `log-is-the-handoff`）")

# ---------------------------------------------------------------- READMEs (what loads, the pointers, the departures link, the file map)
R = "plugins/ideo-scrum/skills/memory/"
sub("README.md", "Each Claude Code role command calls its required kernels in order before starting work (see the [role convention](plugins/ideo-scrum/skills/scrum-kernel/overview.md#who-does-what)).",
    "Each Claude Code role command calls its required kernels, then the Memory, in order before starting work (see the [role rules](" + R + "details/roles.md)).")
sub("README.zh-CN.md", "每个 Claude Code 角色命令都会先按顺序调用所需内核，再开始工作（见[角色约定](plugins/ideo-scrum/skills/scrum-kernel/overview.md#who-does-what)）。",
    "每个 Claude Code 角色命令都会先按顺序调用所需内核和 Memory，再开始工作（见[角色规矩](" + R + "details/roles.md)）。")
sub("README.md", "In DSH, the role brings in IDEO and Scrum in order; Sprint and Design load only as needed.", "In DSH, the role brings in IDEO, Scrum and the Memory in order; Sprint and Design load only as needed.")
sub("README.zh-CN.md", "在 DSH 中，角色按顺序带入 IDEO 内核和 Scrum 内核，Sprint 和 Design 按需加载。", "在 DSH 中，角色按顺序带入 IDEO 内核、Scrum 内核和 Memory，Sprint 和 Design 按需加载。")
sub("README.md", "the Scrum, Sprint and design-sprint material comes only when summoned, by a role, by naming ideo-scrum or one of its kernels, or by asking to create or change its logs;",
    "the Scrum, Sprint and design-sprint material, and the Memory, come only when summoned, by a role, by naming ideo-scrum, one of its kernels or the Memory, or by asking to create or change its logs;")
sub("README.zh-CN.md", "Scrum、冲刺、设计冲刺的材料只有召唤才来——叫出角色，点名 ideo-scrum 或它的某个内核，或者要求建改它的日志；",
    "Scrum、冲刺、设计冲刺的材料和 Memory 只有召唤才来——叫出角色，点名 ideo-scrum、它的某个内核或 Memory，或者要求建改它的日志；")
sub("README.md", "in [`overview.md`](plugins/ideo-scrum/skills/scrum-kernel/overview.md#departures-from-the-official-guides); this is the short version.",
    "in [`departures.md`](" + R + "details/departures.md#departures-from-the-official-guides); this is the short version.")
sub("README.zh-CN.md", "在 [`overview.md`](plugins/ideo-scrum/skills/scrum-kernel/overview.md#departures-from-the-official-guides) 里只写一次",
    "在 [`departures.md`](" + R + "details/departures.md#departures-from-the-official-guides) 里只写一次")
sub("README.md", "- [`overview.md`](plugins/ideo-scrum/skills/scrum-kernel/overview.md): how the pieces fit, and every departure from the official guides",
    "- [Memory](" + R + "SKILL.md): the rules every role follows, one line each; every departure from the official guides is in its `details/departures.md`")
sub("README.zh-CN.md", "- [`overview.md`](plugins/ideo-scrum/skills/scrum-kernel/overview.md)：各部分怎么配合，以及和官方指南的每一处不同（英文）",
    "- [Memory](" + R + "SKILL.md)：各角色共用的规矩，一条一行；和官方指南的每一处不同在它的 `details/departures.md`（英文）")
sub("README.md", "the shared source for the five roles and the four kernels (ideo, scrum, sprint, design), with the four log templates",
    "the shared source for the five roles, the four kernels (ideo, scrum, sprint, design) and the Memory (`skills/memory/`), with the four log templates")
sub("README.zh-CN.md", "五个角色和四个内核（ideo、scrum、sprint、design）的共用源；", "五个角色、四个内核（ideo、scrum、sprint、design）和 Memory（`skills/memory/`）的共用源；")

# ---------------------------------------------------------------- scripts
c = "scripts/check_docs.py"
sub(c, "table repeats the Departures table of overview.md word for word", "table repeats the Departures table of details/departures.md word for word")
sub(c, 'OVERVIEW = "plugins/ideo-scrum/skills/scrum-kernel/overview.md"', 'DEPARTURES_FILE = "plugins/ideo-scrum/skills/memory/details/departures.md"')
sub(c, "# the \"How it differs\" table repeats the Departures table of overview.md", "# the \"How it differs\" table repeats the Departures table of details/departures.md")
sub(c, 'for sec in parse(read(root / OVERVIEW))["sections"]:', 'for sec in parse(read(root / DEPARTURES_FILE))["sections"]:')
sub(c, 'errors.append(f"{OVERVIEW}: no Departures table found")', 'errors.append(f"{DEPARTURES_FILE}: no Departures table found")')
sub(c, "the real documents (a stub for one that is not written yet), overview.md\n    and plugin.json,", "the real documents (a stub for one that is not written yet), details/departures.md\n    and plugin.json,")
sub(c, "for name in names + [OVERVIEW, PLUGIN_JSON]:", "for name in names + [DEPARTURES_FILE, PLUGIN_JSON]:")
sub(c, '("a missing heading", "README.md", "overview.md#departures-from-the-official-guides",\n         "overview.md#no-such-heading", "no heading for #no-such-heading"),',
    '("a missing heading", "README.md", "departures.md#departures-from-the-official-guides",\n         "departures.md#no-such-heading", "no heading for #no-such-heading"),')

d = "scripts/check_dsh.mjs"
sub(d, """  // A skill folder is the base of the paths in its SKILL.md and in the files beside it: a kernel's conventions/ (if it still has
  // any), the memory skill's details/.
  const skills = join(plugin, 'skills')
  const written = []
  for (const kernel of [...kernels, 'memory']) {
    const base = join(skills, kernel)
    const folders = ['conventions', 'details'].map(name => join(base, name)).filter(dir => existsSync(dir))
    const files = [join(base, 'SKILL.md'), ...folders.flatMap(dir => readdirSync(dir).map(name => join(dir, name)))]
    if (kernel === 'scrum-kernel' && existsSync(join(base, 'overview.md'))) files.push(join(base, 'overview.md'))
    for (const file of files.filter(f => f.endsWith('.md'))) {
      const text = readFileSync(file, 'utf8')
      // the old places: a template or a board file named under a kernel's conventions/ folder
      assert.doesNotMatch(
        text,
        /conventions\\/(?:(?:product|sprint|design|ideo)-backlog-template\\.md|board-log\\.md|scrum-board-template\\.html)/,
        `${file} still names a file at its old place`,
      )
""", """  // A skill folder is the base of the paths in its SKILL.md and, for the memory skill, in the files of its details/.
  const skills = join(plugin, 'skills')
  const written = []
  for (const kernel of [...kernels, 'memory']) {
    const base = join(skills, kernel)
    const details = join(base, 'details')
    const files = [join(base, 'SKILL.md'), ...(existsSync(details) ? readdirSync(details).map(name => join(details, name)) : [])]
    for (const file of files.filter(f => f.endsWith('.md'))) {
      const text = readFileSync(file, 'utf8')
      // the old places: the kernels' conventions/ folders and overview.md are gone, their rules moved to the memory skill
      assert.doesNotMatch(text, /conventions\\/|overview\\.md/, `${file} still names a file at an old place`)
""")

if bad:
    for b in bad:
        print("NOT EXACTLY ONCE:", b)
    sys.exit(1)
for p, t in texts.items():
    (ROOT / p).write_text(t, encoding="utf-8", newline="\n")
print(f"{len(texts)} files written")
