# Sprint Backlog — Sprint 15 (feedback-loop)

> Started: 2026-11-12 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `sprint-15-feedback-loop`（worktree `.claude/worktrees/sprint-15-feedback-loop`）| Product Owner: SeaPawn | Scrum Master: IDEO # [master]-[main]-[研究反馈机制] | Developer: IDEO # [designer]-[main]-[辅助设计]
> How to write this log: `sprint-log.md` in the scrum-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled later; add none — remarks go in chapter 4, Increment notes (`overview.md`, convention 16).

小冲刺（sprint-log 的 Small work, small Sprint），每一步一两行。PO 2026-11-11 把这次的事全部交给 Master，各阶段由 Master 定，到 PO 检查为止。增量不在本仓库，在 `S:\SeaPawn-Memory`。

## 1. Why

### 1.1 Sprint Goal

**反馈落地**：自我反馈的办法装进全局说明和全局记忆；攒下的修正点迁进去；用任何产品时说一句「记一下」就落到对的地方，照着就能用。

（Master 照 PO 的写法代拟，PO 检查时认。开冲刺前核对了 Product Goal：Master 认为在现在的目标之内，插件靠这条回路一轮轮改进；PO 检查时认，不认就先定新目标。）

### 1.2 Definition of Done

- 内容忠实：装进去的「Feedback」一节与测过的原型第三版逐字一致；迁进去的点引 PO 的原话。
- 无死链：全局记忆 Feedback 一节的每个链接都指得到文件。

Master 2026-11-12（PO 全部放权）：Sprint Goal 定。

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-55 | 自我反馈——用自己的产品时冒出的想法，更新时都用得上 | 作为熟手，我想要用自己的产品时冒出的想法，随口一句就能交给手边的 AI 记下，以便更新产品时都用得上，产品照我的用法一轮轮改进 | S:\SeaPawn-Memory：SEAPAWN.md 的 Feedback 一节与全局记忆的 Feedback 一节 | S |

### 2.2 Refinement

- 装什么：设计日志 3.1 的方案，文字用原型第三版（`git show c072d8e:scrum/design-feedback-loop/prototype/feedback-section.md`）；另有两句衔接：SEAPAWN.md「Global memory」一条说明 MEMORY.md 末尾有 Feedback 一节，「Where to write」那句把 Feedback 一节算进本文件（Master 定）。
- 迁哪些点：F1–F8；同名文件里的点不迁（PO 2026-11-11）；两份修正记录 `design-map-rough.md`、`design-goal-vision.md` 的内容进 F1、F2，Review 时从 `scrum/documents/` 删掉。F5 已登记 PBI-56，它那一行末尾标 `→ PBI-56`。
- 验收（跑之前写定，不改）：① SEAPAWN.md 的 Feedback 一节与原型第三版逐字一致；② MEMORY.md 末尾 Feedback 一节 8 行，链接都通；③ 冒烟：F3–F6 用装好的办法交（无头 Haiku，在本仓库里说「记一下」，各 1 次），4 次都落进 IDEO-Scrum，文件五项齐，回执一行；④ 审阅：全新子代理没有必改项。

Master 2026-11-12（PO 全部放权）：精化到此。

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | SEAPAWN.md 加 Feedback 一节，改两句衔接 | `S:\SeaPawn-Memory\SEAPAWN.md` | 验收 ① |
| 2 | MEMORY.md 末尾加 Feedback 一节；写 F1、F2、F7、F8 | `GlobalMemory/MEMORY.md`、`GlobalMemory/feedback/IDEO-Scrum/` | 4 个文件、4 行，链接通 |
| 3 | 用装好的办法交 F3–F6 | 4 个文件、4 行 | 验收 ③ |
| 4 | F5 那一行标 `→ PBI-56`；SeaPawn-Memory 提交 | 一个提交 | 不推送 |
| 5 | 审阅 | 审阅意见 | 验收 ④ |

**Key choices**：F3–F6 用装好的办法交，就是在真环境里冒烟；F1、F2 带两份修正记录的内容，F7、F8 是 Master 在设计里发现的，这四个直接写。

**Risks and open points**：装上就对所有项目新开的会话生效；不满意就在 SeaPawn-Memory 回滚这个提交。推不推送，收官时问 PO。

Go-ahead: 2026-11-12，Master（PO 全部放权）；范围：改 `S:\SeaPawn-Memory` 并提交、不推送；在冲刺分支上提交；合入、tag、推送收官时定。

## 4. Increment notes

- 冲刺 worktree `sprint-15-feedback-loop`（`.claude/worktrees/sprint-15-feedback-loop`）从 main（ccc1278）开；本日志照 plan 逐字建。
- 装进 `S:\SeaPawn-Memory`（提交 8c52e57，未推送）：SEAPAWN.md 加「## Feedback」一节（与原型第三版逐字一致，审阅核对过 sha），并改两句衔接；`memory/GlobalMemory/MEMORY.md` 末尾加「## Feedback」一节，先 4 行（F1、F2、F7、F8）；`memory/GlobalMemory/feedback/IDEO-Scrum/` 下 4 个文件。
- 冒烟（用装好的办法交 F3–F6）：`claude -p --model haiku`，禁 Bash 和 PowerShell，守卫只许写 `memory/GlobalMemory/`；四次各 1 次，全部落进 `feedback/IDEO-Scrum/` 并各加一行；回执都只有一行；五项都齐。没有手工改。原始输出在 `S:\IDEO-Scrum-Archives\sprint-15-feedback-loop\`。
- F5 那一行末尾加 ` → PBI-56`。
- 审阅（全新子代理，Haiku）：逐条核对；必改 1 项——F7、F8 没有 PO 原话，与 1.2 的 DoD「迁进去的点引 PO 的原话」冲突。处理：两行标题后加「（设计中发现）」，SeaPawn-Memory 再提交 e4bb8d1；DoD 的措辞（或这两条要不要移作普通全局记忆）报 Master 定。
- 审阅必改的处理（Master 2026-11-12 定，替换上一条的临时处理）：Feedback 只放 PO 自己的点——机制本来就是「用户说记一下」；F7、F8 是 Master 在设计里的发现，移到产品日志 PBI-54 的 ⑦⑧，SeaPawn-Memory 删掉这两个文件和两行（提交 11757c1），e4bb8d1 加的「（设计中发现）」随之没了。DoD 不改；验收 ② 从 8 行改为 6 行（sprint-log 的 Goal fixed, plan flexible）。F3 文件里提到 F7、F8 的半句改成泛指；MEMORY.md、SEAPAWN.md 末尾补了换行（审阅建议 5）。其余建议不改：待认领目录要用时由机制建；name 和五项标签的写法不统一，不影响用。
- F3–F6 的「原话」是 Master 照 PO 在设计会话里的语音整理的：意思不变，去掉了口头语和识别错误。

## 5. Test

冒烟（验收 ③）：

| 条 | 回执 | 写到哪 | Feedback 行 | 五项 |
| --- | --- | --- | --- | --- |
| F3 | 记下了 · IDEO-Scrum · 可改 | `feedback/IDEO-Scrum/2026-11-11-diverge-main-talks-to-po.md` | 有 | 齐 |
| F4 | 记下了 · IDEO-Scrum · 可改 | `feedback/IDEO-Scrum/2026-11-11-design-three-loops.md` | 有 | 齐 |
| F5 | 记下了 · IDEO-Scrum · 可改 | `feedback/IDEO-Scrum/2026-11-11-small-issue-no-design-sprint.md` | 有（末尾标 `→ PBI-56`） | 齐 |
| F6 | 记下了 · IDEO-Scrum · 可改 | `feedback/IDEO-Scrum/2026-11-12-design-single-designer.md` | 有 | 齐 |

审阅（验收 ④）：第 1–4 条对；第 5 条的例外是 F7、F8 没有 PO 原话（记在必改 1）。必改 1 项已按上面的办法处理；DoD 的措辞或这两条的归属要 Master（和 PO）定。其余 5 条建议没有改：`待认领/` 目录未建；`name` 前缀不统一；五项标签写法不统一；Explore/Plan 的「不加载 CLAUDE.md」可补半句说明；文件不以换行结尾。
