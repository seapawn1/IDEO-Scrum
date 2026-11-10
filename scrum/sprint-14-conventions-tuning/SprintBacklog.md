# Sprint Backlog — Sprint 14 (conventions-tuning)

> Started: 2026-11-10 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `sprint-14-conventions-tuning`（worktree `.claude/worktrees/sprint-14-conventions-tuning`）| Product Owner: SeaPawn | Scrum Master: Claude（Claude Code 主会话）| Developer: Claude（从 Master 会话 fork 出的会话）
> How to write this log: `sprint-log.md` in the scrum-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled at close; add none — remarks go in 3.2 Notes (`overview.md`, convention 15).

## 1. Why

### 1.1 Sprint Goal

**约定精调**：约定与模板逐条经 PO 审定，每一条 PO 都同意；重复的合并，说不清的写清楚；新会话照着就能把流程走对。

### 1.2 Definition of Done

Output Done 三条：内容忠实、可导航、无死链（产品日志 1.3）。只改 Claude 侧；Codex 包等全部改完一次同步并核对（PO 2026-11-10）。不改技能描述；若改了，重跑触发测试。

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-49 | 约定精调——PO 逐条审定 | 作为熟手，我想要约定与模板经 PO 逐条过一遍、每一条都同意，写得简洁、明确、准确，以便新项目照着就能把流程走对 | 插件：scrum-kernel 的 `overview.md` 与 `conventions/`，design-kernel 的 `conventions/` | M |
| PBI-47 | 设计的构思——先发散后收敛 | 作为熟手，我想要设计的构思阶段先发散、再收敛，写明发散用哪些方法、做到什么程度才算够，以便不会跳过发散直接出方案 | 插件 design-kernel：SKILL.md 五阶段表的构思一行，`conventions/design-log.md` 的构思各条（7、11–15） | S |
| PBI-48 | 设计各阶段的重心对上 IDEO 五模式 | 作为熟手，我想要设计的每个阶段把注意力放在对应 IDEO 模式的重心上，以便每一段的产出不是走过场 | 插件 design-kernel：SKILL.md 的五阶段表，`conventions/design-log.md` | M |
| PBI-50 | 什么时候必须开设计 | 作为熟手，我想要约定写明哪类问题必须先开设计，以便遇到「他想要什么」「怎么才算好」这类没有现成答案的问题时先进共情，不先出方案 | 插件：scrum-kernel 的 SKILL.md（与设计内核的分工）、`conventions/product-log.md`（2、15）、`conventions/sprint-log.md`（6），design-kernel 的 `conventions/design-log.md`（1、3） | S |
| PBI-40 | 约定 v1 第一次集中修订 | 作为熟手，我想要约定 v1 用过一轮后集中修一次，补上用起来卡手的地方，以便下一个冲刺照着走更顺 | 插件 scrum-kernel、design-kernel 的 `conventions/` | S～M |

### 2.2 Refinement

**PO 定（2026-11-10）**
- 选 PBI-49（主），连同 47、48、50（PO：都是调设计，和重写约定同一类）和 40（熟手对同一批约定的意见）；本冲刺在当前 Product Goal 之内；Sprint Goal 如 1.1。
- 做法：PO 对着全文逐条说哪条不对、怎么改；Master 和 PO 商量，定了就改；不走 plan 视图审阅。PO 用中文说，译文由 PO 的 Stakeholder 会话做；每条意见先分清是英文原文的问题还是译文的问题，Developer 只改英文原文（CLAUDE.md「对着译文审阅」）。
- 顺序：先做设计这块——design-log、设计日志模板，连同 47、48、50；scrum 这边（overview、product-log、sprint-log 与两份模板）随后，慢慢做。
- 结构方向：每份约定先一张架构图，再一批约定；overview 多一节（第 3 节），写与官方指南不同的地方和理由。细节见下面的结构建议。
- 分工：Master 管理、顶层设计；开分支、写日志、改文件都由 Developer 做。Developer 是从 Master 会话 fork 出的 Claude 会话，在 worktree 里干活；它带着 Master 的上下文，审阅仍由 Master 做（sprint-log 约定 16）。通道是本日志：Master 的审阅写在 plan 文件里，PO 转给 Developer，由它抄进日志。
- 只做 Claude 版：冲刺中不同步 Codex；全部改完后一次跑 `scripts/sync_codex.py` 和 `scripts/check_codex.py`。
- 现在就开（距上次集中修订 Sprint 11 一天；CLAUDE.md「约定大约每周集中改一次」）。

**结构建议**（Master 提；PO 对 Developer 说：「Master 的这些修正都不错，你可以考虑」）
1. 图画流程，每个节点标出适用的条号；约定按图的顺序排，小标题和节点同名。图放在约定文件里，不放进模板，所以不与 overview 约定 15「模板只记产出」冲突。设计这块：「构思」画成两个节点——发散、收敛（PBI-47），每段的重心写进对应节点（PBI-48）。
2. 一条规矩只写在一处：跨文件的规矩只留在 overview，其他文件不再重复。例：「目标固定、计划可变」现在写了四遍（overview 16、product-log 18、sprint-log 3、design-log 21）；sprint-log 21 的特殊情况表大半在重复别的条。
3. 每条第一句就是规矩，一句祈使句；理由不明显时才加一句；和官方不同的理由搬到 overview 第 3 节，条里只留一个指向。
4. 来源标签只标例外：文件开头写一次「以下都是作者的做法」，只在 Supplement、Decide on the spot 和引文处单独标。（与同名文件的「每条标明」不完全一样。）
5. 样板先行，不单开设计：先用 design-log 当样板——只调结构（挪位置、加图，一个字不改），PO 看形状；再派一个全新的 Haiku 子代理，只给这一份文件，问三道「你在某一步，先做什么」，题目和过线标准事先定好；答对了，再套到其余几份。

**Master 定**
- PO 没提的文字一字不动；结构调整只挪不改；新写的文字（如架构图）单独给 PO 看。
- 改一条规矩，就全仓找它在模板、四个命令、两份 SKILL.md、CLAUDE.md、README 里的其他说法，列成连带改动一起改；删、合并约定要改号，用脚本把每处「convention N」重新对到短名。
- 本冲刺照 5.1.2 的约定走；改动从下一个冲刺起生效（overview 约定 14）。
- 不推送、不合入、不打 tag，收官时 PO 定。

**验收标准**
1. 清单（`checklist.md`）每行都有 PO 的结论——改、不改、挪到别的 PBI——全部打勾。
2. 定了要改的都已改；Master 对照结论逐条核 diff。
3. diff 只落在定了的点和登记的连带改动上。
4. 改过的规矩，全仓旧说法 0 残留；「convention N」引用脚本核对 0 错。
5. 无死链、可导航；plugin-validator 通过。
6. Goal 末句：收官前派全新子代理（Haiku），只给改后的插件，答几道流程题；题目与过线标准先提交、后跑，测法收官前由 PO 定。
7. 收官前 Codex 同步与核对：0 不一致。

**测试**：4、7 用脚本，脚本先拿一两份已知结果自测；6 照上面。

## 3. How

### 3.1 How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | design-log 样板：只调结构 | design-log 加流程图（节点标条号），条按图的顺序排；一个字不改，图单列，可被单独圈阅或撤掉 | PO 看过形状并说行；一个全新 Haiku 子代理只读这一份，答三道「你在某一步，先做什么」，题目与过线标准先提交、后跑 |
| 2 | design-log 逐条过 | PO 对 21 条的意见与结论进清单；按结论改后的 design-log（PBI-47、48、50 的内容在此） | 清单里 design-log 的行都是「已改」；Master 对照结论核 diff，核过改「已核」 |
| 3 | 设计日志模板；design-kernel `SKILL.md` 的五阶段表 | 按清单结论改后的模板与五阶段表 | 同 2 |
| 4 | overview（含新的第 3 节）；scrum-kernel `SKILL.md` 的分工一节 | 按清单结论改后的 overview 与分工一节 | 同 2 |
| 5 | product-log；产品日志模板 | 按清单结论改后的两份文件 | 同 2 |
| 6 | sprint-log；冲刺日志模板 | 按清单结论改后的两份文件 | 同 2 |
| 7 | 连带改动与改号 | 改过的规矩在模板、四个命令、两份 `SKILL.md`、CLAUDE.md、README 里的其他说法一起改；删、合并造成的改号，每处「convention N」对到短名 | 旧说法 0 残留；引用脚本核对 0 错（脚本先拿已知结果自测）；连带改动登记在 3.2 |
| 8 | 审阅与校验 | 全新子代理审 diff；`plugin-dev:plugin-validator`；新会话流程题（Haiku） | 无必改项；验收 5、6 过线（这三项由 Master 派） |
| 9 | 收官前同步 Codex | `scripts/sync_codex.py`、`scripts/check_codex.py` | 0 不一致（验收 7） |

**Key choices**

- **worktree**：PO 建议开 worktree；Developer 在 `.claude/worktrees/` 里改，主目录不动；分支改成与文件夹同名（sprint-log 约定 1），不带 `worktree-` 前缀。
- **清单是收官条件**：87 行，每行一条约定、一份模板或一处 `SKILL.md`；PO 逐行给结论，全部打勾就是 Goal 达成，一条不漏。「输入」栏只标位置，不加意见。
- **一份文件定完再改**：这份的意见都定下后，Developer 一次改完，Master 审，PO 看结果；比一条一改来回少，也比攒到最后更早看到效果。
- **样板先行，不单开设计**：结构是品味题，反馈链太长（PO），所以先用 design-log 当样板看形状，再套到其余几份。
- **按日志分三块，各一份约定**：不按步骤拆文件（Planning 要同时开几份约定的问题，交给 PBI-45 的流程命令），也不合成一个文件（每走一步要整份重读）（Master 的建议）。
- **只改定了的点**：PO 没提的文字一字不动，结构调整只挪不改；新文字（图、第 3 节）单列，可被单独圈阅或撤掉。
- **只改英文原文**：中文译文由 PO 的 Stakeholder 会话做，不进仓库；PO 的每条意见先判是原文的问题还是译文的问题。

**Risks and open points**

- 结构细节待 PO 看形状后定：结构建议第 4 条与同名文件的「每条标明」不完全一样，PO 的回话没单独说这条；overview 现有的「The map」与新 §1 架构图是同一张还是新画、现有的 Departures 表与新 §3 的关系，都还没定。
- 中间提交里 Codex 包落后于 Claude 侧：PO 定收官前一次同步，与 CLAUDE.md「同一提交里跑同步」不同；`check_codex.py` 在中间会报不一致，收官前必须清零。
- fork 的限制：Developer 不能派子代理，审阅、`plugin-validator`、Haiku 测试都由 Master 派；主会话进 plan 模式时 Developer 会停下，写不了文件。
- 连带改动面广：删、合并约定会改号，牵到模板、四个命令、两份 `SKILL.md`、CLAUDE.md、README；`scrum/documents/` 的归档是历史，不改；`codex/` 是生成物，同步时随之更新（「全仓」的范围见 3.2 的问题 b）。
- 发版与版本号：改的是措辞与结构、行为不变，要不要升版本、升到几，收官时 PO 定；发版则 `plugin.json` 与 README 两处版本号同步。
- 测试待定：样板的三道题、收官的流程题，题目与过线标准都要先提交、后跑，测法收官前由 PO 定。
- 技能描述：这次不动（1.2）；某条意见若牵出描述的改动，先停下问 Master。

Go-ahead: 待 PO（Master 审开冲刺与 How 之后）

### 3.2 Notes

| Date | What was done | Decision and reason | Evidence | Next |
| --- | --- | --- | --- | --- |
| 2026-11-10 | Planning：PO 定 Sprint Goal、选 PBI，开冲刺；Master 写 1.1–2.2，Developer 开 worktree、落盘 | 同名文件的四条登记为 PBI-47～50（PO：都可以列成 PBI）；49 是主 PBI，47、48、50 是设计这块，40 是熟手的意见；PBI-44（SKILL.md 可读性）、45（流程命令）不是约定本身，不选 | 产品日志 PBI-40、47～50 | Developer 复述验收、写 How；Master 审，PO 放行 |
| 2026-11-10 | Developer（fork 出的会话）：开 worktree，分支改名为 `sprint-14-conventions-tuning`；产品日志登记 PBI-47～50、PBI-40 状态改为 Sprint 14、1.2 改三处；建 `checklist.md`（87 行，待 PO 逐行看）；同名文件标 PBI 编号（该文件不入库）；复述验收，写 3.1 | PO 看了 Master 的结构建议，说「都不错，你可以考虑」：写进 2.2，3.1 的第 1 项按「样板先行」排；清单的「输入」栏照 plan 附录 D，另加四处：design-log §1 一行标 PBI-47、48（按 Master 对话里的说明）；overview §1、§3 和 sprint-log §1 三行标现有内容的位置（The map；Departures 表与各条里的 Departs 句；文件开头的流程图），都只标位置，不是意见 | `checklist.md`；产品日志 3.1、1.2 | Master 审开冲刺与 How；PO 放行；放行后做 3.1 第 1 项 |

**Developer 复述验收（2026-11-10）**

1. 清单每行都有 PO 的结论（改 / 不改 / 挪到别的 PBI），全部打勾（状态「已核」），Goal 才算达成。
2. 定了要改的都改到位；Master 拿结论逐条对 diff。
3. diff 里除了定了的点，只有登记过的连带改动；PO 没提的字不动。
4. 改过的规矩，全仓里的旧说法 0 残留；「convention N」引用用脚本核，0 错。
5. 无死链，从入口两跳可达；`plugin-validator` 通过。
6. Goal 末句：收官前，一个全新 Haiku 子代理只拿改后的插件，答几道流程题；题目与过线标准先提交、后跑；测法 PO 收官前定。
7. Codex：全部改完后一次同步，`check_codex.py` 0 不一致。

**清单怎么记**：PO 的意见经 Master 转来（plan 文件），我抄进清单的「PO 的意见」「结论」，并改状态：待看 → 已定（结论已抄入）→ 已改（我改完）→ 已核（Master 核过 diff）。

**不清楚的地方（请 Master 定）**
- a. 「登记的连带改动」登记在哪：我打算记在本 3.2 里（每项写：哪条规矩、哪些文件），收官时据此核 diff；想放进清单另开一张表的话，请说。
- b. 「全仓」的范围：我按 `plugins/ideo-scrum/`、README、CLAUDE.md、`scrum/` 现行文件算；`scrum/documents/` 的归档是历史，不改（与 Sprint 12 一致）；`codex/` 是生成物，同步时随之更新。是否这样。
- c. 验收 6 与样板那三道题：题目与过线标准我这轮不写，等 PO 定测法（sprint-log 约定 15：先提交、后跑）。

## 4. Review

<!-- Written at close by the Product Owner, the Scrum Master, and the Developer: the Increment; the Definition of Done and the acceptance criteria, item by item; what the review found; the stakeholders' view; changes to the product log and the Product Goal (sprint-log.md, convention 18). -->
