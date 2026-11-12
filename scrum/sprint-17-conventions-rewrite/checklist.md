# Sprint 17 改动点清单与新路径表

> 用途：本冲刺的收官条件之一（2.2 验收 1、3）。路径以 Sprint 16 的 How 为准（`sprint-16-kernel-structure` 的 `SprintBacklog.md`，提交 `d9a1123`）。
> 状态：落点已定 → 大纲 → 全文 → 已核。Master 审大纲时看「落点」一栏。

## 一、新布局路径表

本冲刺要写稿的文件（`drafts/` 镜像插件的新布局，搬运时整棵挪进去）：

| 现在（`plugins/ideo-scrum/skills/`） | 之后 | 本冲刺的稿 | 我改什么 |
| --- | --- | --- | --- |
| `scrum-kernel/conventions/sprint-log.md` | `sprint-kernel/conventions/sprint-log.md` | `drafts/sprint-kernel/conventions/sprint-log.md` | 54 ②③④、53、46 ③ |
| `scrum-kernel/conventions/sprint-backlog-template.md` | `sprint-kernel/conventions/sprint-backlog-template.md` | `drafts/sprint-kernel/conventions/sprint-backlog-template.md` | 54 ① |
| `scrum-kernel/conventions/product-log.md` | 原位 | `drafts/scrum-kernel/conventions/product-log.md` | 第 12 条收成指向、第 17 条指向过时定义 |
| `scrum-kernel/overview.md` | 原位 | `drafts/scrum-kernel/overview.md` | 第 14 条加一句指向（大纲定） |
| `ideo-kernel/SKILL.md` | 原位 | `drafts/ideo-kernel/SKILL.md` | 加一行指向新约定（Master 必补） |
| —（新建） | `ideo-kernel/conventions/design-sprint-or-five-modes.md` | `drafts/ideo-kernel/conventions/design-sprint-or-five-modes.md` | 56 |
| `design-kernel/conventions/design-log.md` | 原位 | `drafts/design-kernel/conventions/design-log.md` | 58 ①–⑧、56 |
| `design-kernel/conventions/design-backlog-template.md` | 原位 | `drafts/design-kernel/conventions/design-backlog-template.md` | 58 ①② 的注释 |

不写稿、只核对的：

| 文件 | 谁改 | 我核什么 |
| --- | --- | --- |
| `scrum-kernel/conventions/product-backlog-template.md` | Sprint 16（查路径） | 我的条文改动不牵它 |
| `scrum-kernel/SKILL.md`、`sprint-kernel/SKILL.md` | Sprint 16 | 它们的约定表与我的文件对得上（文件名、条数） |
| `design-kernel/SKILL.md` | Sprint 16 | 56 若改描述，由我加（大纲定） |
| 四个 `commands/*.md` | Sprint 16 | 53、56 不另写进命令（大纲定） |
| `scripts/codex_readme.md` | 不动 | 46 ③ 只写进约定 |

## 二、改动点表

| 点 | 落点（文件 · 条） | 怎么落 |
| --- | --- | --- |
| 54 ① | `sprint-backlog-template.md` 头部；`sprint-log.md` 第 22 条 | 头部加 Now 行：当前阶段 + 最后一个 PO 的决定；接手先读它 |
| 54 ② | `sprint-log.md` 第 10 条 | 写明什么算卡住：等一个只有 PO 能给的决定、缺一个只有 PO 能给的信息、外部阻塞；其余算计划内的调整 |
| 54 ③ | `sprint-log.md` 第 17 条（定义写这里）；`product-log.md` 第 17 条指向 | 过时 = 现在不真了，或现在没人要读（历史在 git，删了不丢） |
| 54 ④ | `sprint-log.md` 第 5 条（写这里）；`product-log.md` 第 12 条收成指向 | 照抄进 2.1 时对照 Sprint Goal 查够不够：缺就增、多就减 |
| 58 ① | `design-log.md` 第 8 条；设计模板 2.1 注释 | 地图只画现在发生的事：五六个框、一个环；分支和方案不进地图 |
| 58 ② | `design-log.md` 第 6 条；设计模板 1.2 注释 | 设计目标写愿景（为什么做、想到哪），不写怎么做 |
| 58 ③ | `design-log.md` 第 11 条（主对话那一段） | 子代理发散时主对话陪 PO 聊；PO 没想法就替他画一份；全部合并后再收敛 |
| 58 ④ | `design-log.md` 图下的导读（不编号，大纲定） | 三个环：共情定义人进 AI 出；发散收敛 AI 做、人选；原型测试可自动跑 |
| 58 ⑤ | `design-log.md` 第 3 条 | 一个 Designer 常常就够；兼不兼 Master 由 PO 定 |
| 58 ⑥ | `design-log.md` 第 4 条 | 设计一开就开分支；现场定的只是从哪里开 |
| 58 ⑦ | `design-log.md` 第 11 条 | 全新、非 fork 的子代理；简报只给第 1、2 章和收集的点子；局限写明（受管策略、子目录 CLAUDE.md、git 状态） |
| 58 ⑧ | `design-log.md` 第 9 条 | 每份草图给不同的一部分，或先画再看 |
| 56 | `ideo-kernel/conventions/design-sprint-or-five-modes.md`（新，第 1 条）；`design-log.md` 第 1、26 条指向；`ideo-kernel/SKILL.md` 一行 | PO 指定；没指定时：要先做原型、拿角色卡测过才敢动手的开设计冲刺，其余就地用五阶段法、按方法记录；聊天算共情材料 |
| 53 | `sprint-log.md` 第 26 条（新）；`overview.md` 第 14 条指向 | 写成角色和步骤；工具做法只当例子（overview 15） |
| 46 ③ | `sprint-log.md` 第 14 条 | 工具没有子代理时，新的会话只给简报＝全新子代理；fork 不算；标明只查过 `codex-cli 0.167.0` 的 help |

## 三、连带改动扫描范围

同一条规矩的其他说法，在下面各处找（「改规矩先找它的其他说法」）：

- 三份模板：`product-backlog-template.md`、`sprint-backlog-template.md`、`design-backlog-template.md`
- 四个命令：`commands/*.md`
- 四个 `SKILL.md`：scrum-kernel、sprint-kernel、ideo-kernel、design-kernel
- `scrum-kernel/overview.md`（含第 14、15 条）
- `CLAUDE.md`（含「当前状态」与「下一次集中修订」两处，收官时更新）
- `README.md`（文件地图；Sprint 16 主改，我只核我的条文没有别的说法）
- `scripts/codex_readme.md`（Sprint 16 改文件表；我核 53、56 没有别的说法）
- 每份约定文件之间：`convention N` 与路径（脚本 + 逐处读）

要搜的说法（短名与特征句）：「stuck」「outdated」「Now」「The measure is the Sprint Goal」「Open a design for a question」「small design」「Branch」「Lightning Demos」「Isolated solutions」「Who」「fresh subagent」「another tool」「five modes」「design sprint」「When the design ends」。

不动的历史：`scrum/documents/` 的归档、产品日志 3.2、本日志之外的历史提交。
