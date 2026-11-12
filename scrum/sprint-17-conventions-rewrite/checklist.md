# Sprint 17 改动点清单与新路径表

> 用途：本冲刺的收官条件之一（2.2 验收 1、3）。路径以 Sprint 16 的 How 为准（`sprint-16-kernel-structure` 的 `SprintBacklog.md`，提交 `d9a1123`）。
> 2026-11-12 按 Master 的定案改过：56 不改描述；46 ③ 的定义放 overview 第 7 条；58 ③ 拆成新条；58 ④ 放导读；54 ③ 定义放 sprint-log 第 17 条；53 放 sprint-log 第 26 条。

## 一、新布局路径表

本冲刺要写稿的文件（`drafts/` 镜像插件的新布局，搬运时整棵挪进去）：

| 现在（`plugins/ideo-scrum/skills/`） | 之后 | 本冲刺的稿 | 我改什么 |
| --- | --- | --- | --- |
| `scrum-kernel/conventions/sprint-log.md` | `sprint-kernel/conventions/sprint-log.md` | `drafts/sprint-kernel/conventions/sprint-log.md` | 第 5、6（56 连带）、10、17、22 条；新增第 26 条（53） |
| `scrum-kernel/conventions/sprint-backlog-template.md` | `sprint-kernel/conventions/sprint-backlog-template.md` | `drafts/sprint-kernel/conventions/sprint-backlog-template.md` | 头部 Now 行（54 ①） |
| `scrum-kernel/conventions/product-log.md` | 原位 | `drafts/scrum-kernel/conventions/product-log.md` | 第 2（56 连带）、12、17 条 |
| `scrum-kernel/overview.md` | 原位 | `drafts/scrum-kernel/overview.md` | 第 2（56 连带）、7（46 ③）、14（53）条 |
| `scrum-kernel/SKILL.md` | 原位 | `drafts/scrum-kernel/SKILL.md` | 56 连带：把「always goes to a design first」等改成指向（Master 补） |
| `ideo-kernel/SKILL.md` | 原位 | `drafts/ideo-kernel/SKILL.md` | 加一行指向新约定（只这一处，Use Protocol 不动） |
| —（新建） | `ideo-kernel/conventions/design-sprint-or-five-modes.md` | `drafts/ideo-kernel/conventions/design-sprint-or-five-modes.md` | 56 |
| `design-kernel/conventions/design-log.md` | 原位 | `drafts/design-kernel/conventions/design-log.md` | 第 1、3、4、6、8、9、11（重写）、26 条；新增第 12 条；导读；改号后顺延 |
| `design-kernel/conventions/design-backlog-template.md` | 原位 | `drafts/design-kernel/conventions/design-backlog-template.md` | 1.2、2.1 注释各加几个字和条号 |

不写稿、只核对的：

| 文件 | 谁改 | 我核什么 |
| --- | --- | --- |
| `scrum-kernel/conventions/product-backlog-template.md` | Sprint 16（查路径） | 我的条文改动不牵它 |
| `sprint-kernel/SKILL.md` | Sprint 16（新写） | 它的约定表与我的文件对得上（文件名、条数） |
| `design-kernel/SKILL.md` | Sprint 16 | 56 不改描述；它的摘录路径由 16 改 |
| 四个 `commands/*.md` | Sprint 16 | 53、56 不另写进命令；「全新子代理」用 overview 第 7 条的定义 |
| `scripts/codex_readme.md` | 不动 | 46 ③ 只写进 overview 与笔记 |

## 二、改动点表

| 点 | 落点（文件 · 条） | 怎么落 |
| --- | --- | --- |
| 54 ① | `sprint-backlog-template.md` 头部；`sprint-log.md` 第 22 条 | 头部加 Now 行：当前阶段 + 最后一个 PO 的决定；接手先读它 |
| 54 ② | `sprint-log.md` 第 10 条 | 什么算卡住：等一个只有 PO 能给的决定、缺一个只有 PO 能给的信息、外部阻塞、同一个做法试了两次都不行、照现在的 How 看不出怎么达成 Sprint Goal；其余算计划内的调整 |
| 54 ③ | `sprint-log.md` 第 17 条（定义写这里）；`product-log.md` 第 17 条指向 | 过时 = 现在不真了，或现在没人要读（历史在 git，删了不丢） |
| 54 ④ | `sprint-log.md` 第 5 条（写这里）；`product-log.md` 第 12 条收成指向 | 照抄进 2.1 时对照 Sprint Goal 查够不够：缺就增、多就减 |
| 58 ① | `design-log.md` 第 8 条；设计模板 2.1 注释 | 地图只画现在发生的事：五六个框、一个环；分支和方案不进地图 |
| 58 ② | `design-log.md` 第 6 条；设计模板 1.2 注释 | 设计目标写愿景（为什么做、想到哪），不写怎么做 |
| 58 ③ | `design-log.md` 新第 12 条 | 主对话问 PO、聊着不急着收敛；PO 没想法就替他画一份；所有线合并后再收敛 |
| 58 ④ | `design-log.md` 图下导读（不编号） | 三个环；PO 可把原型与测试之间的阶段决定交给 Master（overview 第 12 条）；差别列进问题与建议，停点 ② 请 PO 看 |
| 58 ⑤ | `design-log.md` 第 3 条 | 一个 Designer 常常就够；兼不兼 Master 由 PO 定 |
| 58 ⑥ | `design-log.md` 第 4 条 | 设计一开就开分支；现场定的只是从哪里开 |
| 58 ⑦ | `design-log.md` 第 11 条（整条重写） | 全新、非 fork 的子代理；简报只给第 1、2 章和收集的点子，叫它不要读项目里的文件；局限用通用说法 |
| 58 ⑧ | `design-log.md` 第 9 条一句、改法在第 11 条 | 点子清单之后分给各份草图：每份拿不同的一部分，或先画后看 |
| 56 | `ideo-kernel/conventions/design-sprint-or-five-modes.md`（新，第 1 条，分界只写这里）；`design-log.md` 第 1、26 条指向；`ideo-kernel/SKILL.md` 一行（工具箱）；`scrum-kernel/SKILL.md` 两处；`sprint-log.md` 第 6 条第 4 步；`overview.md` 第 2 条；`product-log.md` 第 2 条 | 分界写一次，其余只指向，不重复、不冲突；聊天算共情材料的原话保留 |
| 53 | `sprint-log.md` 第 26 条（新）；`overview.md` 第 14 条指向 | 写成角色和步骤；工具做法只当例子（overview 第 15 条） |
| 46 ③ | `overview.md` 第 7 条（Names） | 定义「全新子代理」：只从简报起步；fork 出来的、复制出来的都不算；工具没有子代理时，开一个只给简报的新会话。工具版本与依据不进约定，记笔记，收官写进 PBI-46 |
| PBI-52（并入） | 题 3 的缺口：设计的结论流回产品日志 | 现有三处已写：`product-log.md` 第 2 条、`design-log.md` 第 19 条、design-kernel `SKILL.md` 开头；草稿先不动，看最后一轮流程测试；要改措辞再和 PO 的意见同批改 |

## 三、连带改动扫描范围

同一条规矩的其他说法，在下面各处找（「改规矩先找它的其他说法」）：

- **「什么时候开设计」现在写在五处**（56 之后都要指向新的 ideo 约定或至少不冲突）：`scrum-kernel/SKILL.md` 的「always goes to a design first」与「open a design first」、`sprint-log.md` 第 6 条第 4 步、`overview.md` 第 2 条、`ideo-kernel/SKILL.md` Use Protocol 第 6 条、`product-log.md` 第 2 条（白纸）。
- **「全新子代理」出现在**：`sprint-log.md` 第 14 条、`overview.md` 第 7 条（定义）、四个命令的描述与正文——定义只放 overview 第 7 条，其余用词不改。
- 三份模板：`product-backlog-template.md`、`sprint-backlog-template.md`、`design-backlog-template.md`
- 四个命令：`commands/*.md`
- 四个 `SKILL.md`：scrum-kernel、sprint-kernel、ideo-kernel、design-kernel
- `scrum-kernel/overview.md`（含第 2、7、12、14、15 条）
- `CLAUDE.md`（含「当前状态」与「下一次集中修订」两处，收官时更新）
- `README.md`（文件地图；Sprint 16 主改，我只核我的条文没有别的说法）
- `scripts/codex_readme.md`（Sprint 16 改文件表；我核 53、56 没有别的说法）
- 每份约定文件之间：`convention N` 与路径（脚本 + 逐处读）

要搜的说法（短名与特征句）：「stuck」「outdated」「Now」「The measure is the Sprint Goal」「Open a design for a question」「small design」「Branch」「Lightning Demos」「Isolated solutions」「Who」「fresh subagent」「another tool」「five modes」「design sprint」「When the design ends」「always goes to a design」。

不动的历史：`scrum/documents/` 的归档、产品日志 3.2、本日志之外的历史提交。
