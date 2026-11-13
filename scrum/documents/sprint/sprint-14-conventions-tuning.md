# Sprint Backlog — Sprint 14 (conventions-tuning)

> Started: 2026-11-10 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `sprint-14-conventions-tuning`（worktree `.claude/worktrees/sprint-14-conventions-tuning`）| Product Owner: SeaPawn | Scrum Master: Claude（Claude Code 主会话）| Developer: Claude（从 Master 会话 `/fork` 出的独立会话）
> How to write this log: `sprint-log.md` in the scrum-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled at close; add none — remarks go in 3.2 Notes (`overview.md`, convention 15).
> 归档：2026-11-10 开工并收官，发版 5.2.0。本日志照 5.1.2 的约定写（四章，第 4 章是 Review）；文中约定号凡写「现」的是 5.2.0 的号，其余是 5.1.2 的号（上一行的 convention 15，现为 16）。日志已压缩成关键决定，逐条笔记原文见 `git show 1c1473c:scrum/sprint-14-conventions-tuning/SprintBacklog.md`；98 行审定清单（含连带改动与改号对照）和两份测试汇总已删，要点在下面和第 4 章，原文见 `git show 1c1473c:scrum/sprint-14-conventions-tuning/checklist.md`（同目录还有 `flow-test-summary.md`、`sample-test-summary.md`）；测试的原始输出在仓库外，不入库。

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
- 选 PBI-49（主），连同 47、48、50（都是调设计，和重写约定同一类）和 40（熟手对同一批约定的意见）；本冲刺在当前 Product Goal 之内。
- 做法：Developer 照已定的方向起草修订，Master 审，最后 PO 强审，PO 指出的问题 Developer 直接改；不走 plan 视图审阅（原做法是 PO 逐条说哪条不对）。PO 用中文说，译文由 PO 的 Stakeholder 会话做；每条意见先分清是英文原文的问题还是译文的问题，Developer 只改英文原文。顺序：先设计这块（design-log、设计日志模板，连同 47、48、50），scrum 这边随后。只做 Claude 版，Codex 全部改完后一次同步。
- 做插件，不改成全局记忆；约定不做成 index，照「一张图加一批约定」做（index 登记为 PBI-51，以后可能做）。
- 结构：每份约定先一张架构图，再一批约定；overview 多一节（第 3 节），写与官方指南不同的地方和理由。
- 阶段之间由 PO 决定：设计的五个阶段之间、冲刺的各阶段之间，每个阶段结束时由 PO 拍板——定下这一段的结果，决定进不进下一段（除非 PO 明确交给 Master）。这是做决定，不是审阅或验收，检查做得对不对是 Master 的事；只管到阶段这一层。冲刺：Why 定 Sprint Goal；What 定精化到此为止；How 放行；Increment 定可以进入测试；Test 定收官还是回去。
- 冲刺日志改成五章，和设计日志同一个样子：Why、What、How、Increment notes、Test。Review 和 Retro 不设章，是收官动作：Review 是压缩日志、归档、保鲜产品日志，利益相关者的看法落到产品日志；Retro 是把教训写进记忆或说明文件。设计日志同理，五章就是五个阶段。
- How 写成「类似方案」的一节，不要写太细；一律用 plan，不用 solution（PO 担心以后的 AI 把冲刺的 How 和设计选出的方案搞混，中文都叫「方案」）。
- 两个入口，同一份产品日志：能定义出来的直接写产品日志，定义不出来的用设计里对应的一项替换；连产品和 Product Goal 都写不出时，从设计开始（白纸）。设计的挑战对 1.1 产品，设计目标对 Product Goal，设计问题对完成标准，地图对架构，地图上的步骤对 PBI；对照表只写在 product-log 的 Blank page 一条。判断走哪个入口，和 PBI-50「没有现成答案的问题先走设计」是同一个判断。
- 设计模板：去掉单列的发现一节和点子池一节（点子是工作材料，由子代理自己消化，不落盘），原型一章只留「各部分」一张表，测试一章不分小节；POV 整条去掉（书里的设计冲刺不要 POV；第 1 章的挑战、目标、问题加地图，合起来就是 POV）。
- IDEO 一定要融合进设计冲刺：设计冲刺只是骨架（阶段和书的步骤），每个阶段需要的方法到 ideo-kernel 里找；必须用，与书的步骤两样一起做，不是二选一；不给每个阶段指定方法名，规矩只写在 design-kernel 的 `SKILL.md`。
- overview 补一句：工作材料不进日志，真正关键的内容进项目的记忆或说明文件，大份重要的文件进 `scrum/documents/`。
- 收官前 PO 强审四份约定和三份模板；本冲刺不推送、不合入、不打 tag，收官时 PO 定。
- 分工：Master 管理、顶层设计；开分支、写日志、改文件都由 Developer 做。通道是本日志加跨会话消息：Master 与 Developer 直接发消息，不经 PO 转；长的审阅写在 plan 文件里，消息给路径。

**结构建议**（Master 提；PO：「都不错，你可以考虑」）
1. 图画流程，每个节点标出适用的条号；约定按图的顺序排，小标题和节点同名。构思画成「发散」「收敛」两个节点。
2. 一条规矩只写在一处：跨文件的规矩只留在 overview。
3. 每条第一句就是规矩，一句祈使句；理由不明显才加一句；和官方不同的理由搬到 overview 第 3 节。
4. 来源标签只标例外：文件开头写一次「没有标签的就是作者的做法」，只在 Supplement、Decide on the spot 和引文处单独标。
5. 样板先行，不单开设计：先用 design-log 当样板，只调结构；再派全新 Haiku 子代理，只给这一份文件，问三道题；答对了再套到其余几份。

**Master 定**
- 没有依据的文字不动：每处改动都要对到清单里一条已定的依据——PO 的决定；PBI-40、47、48、50 的输入；结构建议第 2 到 4 条；Master 的提议。清单的「结论」栏写清改了什么、依据是哪一条。插件文件里不做标记，PO 强审时一视同仁地看；新写的文字（如架构图）在清单里单独列出，方便圈阅。
- 「阶段之间由 PO 决定」正文只写在 overview 一处；design-log 和 sprint-log 的图上标出 PO 拍板的点，并指向它。
- 改一条规矩，就全仓找它在模板、四个命令、两份 `SKILL.md`、CLAUDE.md、README 里的其他说法，列成连带改动一起改；删、合并约定造成的改号，用脚本把每处「convention N」重新对到短名。
- 本冲刺自己的日志不改成五章，照 5.1.2 的约定走；约定的改动从下一个冲刺起生效。
- 样板的发现进 design-log 的修订：定分支排在填表头之前（或并进「开设计」那一条）。

**Master 对设计日志的提议**（写进 design-log，文件里不标记）：① 每个阶段设一道门——离开前日志里必须有哪些产出，标准取 IDEO 各模式的重心，门上由 PO 拍板；② 共情先找当事人，每条发现标明来源；③ 模板补格子（共情发现、POV、点子池、原型每一部分测哪个问题）——后来 PO 定去掉发现、POV、点子池，只留原型每一部分测哪个问题；④ 小设计；⑤ 测试前先写判据，写明角色卡测试的局限；⑥ 测完由 PO 决定收官还是回到前面的阶段；⑦ 设计收官不加 Review 章（后来 PO 定设计整个不做 Review 和 Retro）。

**验收标准**
1. 清单（`checklist.md`）每行都有结论——改、不改、挪到别的 PBI——并写明依据；在 PO 强审时全部打勾。
2. 定了要改的都已改；Master 对照结论逐条核 diff。
3. diff 只落在有依据的改动和登记的连带改动上。
4. 改过的规矩，全仓旧说法 0 残留；「convention N」引用脚本核对 0 错。
5. 无死链、可导航；plugin-validator 通过。
6. 收官前派全新子代理（Haiku），只给改后的插件，答几道流程题；题目与过线标准先提交、后跑，测法由 Master 定（PO 授权）。
7. 收官前 Codex 同步与核对：0 不一致。
8. 收官前 PO 强审四份约定（overview、product-log、sprint-log、design-log）和三份模板；PO 指出的问题全部改完后，PO 再看一遍，说行才算过。

**测试**：4、7 用脚本，脚本先拿一两份已知结果自测；5、6 如下。
- **样板的三道题**（design-log 的结构）：只给 `design-log.md` 全文、关掉所有工具；被测是改前（提交 `89406bf`）和改后各一份，每份三题（开设计、构思到选定、收官）各 5 次，Haiku，同日同环境。过线：改后每题 5 次里至少 4 次过，并且三题合计不少于改前。
- **流程测试**（验收 6；题目与过线标准在提交 `1b07623`、`a87bd1c`，先提交、后跑，跑后不改）：无头 `claude -p --model haiku --plugin-dir <worktree 里的插件>`，只开 Read、Grep、Glob、Skill，工作目录是系统临时目录里新建的空项目，每次一个全新会话；题目用自然的说法，不带引导词；5 题 × 3 次，不比基线。一次回答算过，要同时满足：读到了该题对应的约定文件；必答项全中；没有「不能」项。过线：每题 3 次里至少 2 次过。五题：1 开冲刺（五个阶段按先后说全，每段结束由 PO 拍板）；2 精化碰到没有现成答案的问题（为它开设计、只取出这个难点、从共情起）；3 白纸项目（从设计开始，设计的结论流回产品日志）；4 设计的构思（先发散再收敛，IDEO 方法必须用，隔离的子代理，PO 选定）；5 收官（Review、Retro 是动作，日志压缩归档，教训进记忆或说明文件）。

## 3. How

### 3.1 How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | design-log 样板：只做结构建议第 1 条 | design-log 加一张 `flowchart TD`（节点是步骤，标现有条号；构思拆成「发散」「收敛」；贯穿全程的几条写在图下一行）；约定按图的顺序排，保留原编号，小标题和节点同名；每条正文一个字不动 | PO 接受结构；三道题 14 对 15 没过线，PO 让往下走（见 3.2） |
| 2 | design-log 修订 | 照已定的方向起草：新增和改写的约定、改后的图；每处改动在清单「结论」栏写明依据；Master 的七条提议也写进来 | 清单里 design-log 的行都有结论和依据；Master 审过；PO 强审在第 8 项 |
| 3 | 设计日志模板；design-kernel `SKILL.md` 的五阶段表 | 同 2；模板的章节清单单独摆出，给 PO 看结构 | 同 2；PO 看过模板的结构 |
| 4 | overview（含新的第 3 节、「阶段之间由 PO 决定」、图上的「白纸」入口）；scrum-kernel `SKILL.md` 的分工一节 | 同 2 | 同 2 |
| 5 | product-log（含 Blank page 的对照表）；产品日志模板 | 同 2 | 同 2 |
| 6 | sprint-log（含冲刺日志五章、How 写成 plan、PO 拍板的点）；冲刺日志模板 | 同 2；冲刺日志模板的章节清单单独摆出，给 PO 看结构 | 同 2；模板的结构 PO 看过 |
| 7 | 连带改动与改号 | 改过的规矩在模板、四个命令、两份 `SKILL.md`、CLAUDE.md、README 里的其他说法一起改；删、合并造成的改号，每处「convention N」对到短名 | 旧说法 0 残留；引用脚本核对 0 错（脚本先拿已知结果自测）；连带改动登记在清单第二张表 |
| 8 | 审阅与校验；PO 强审 | `plugin-validator` 和 Haiku 流程测试由 Developer 跑；审阅由 Master 做，或由 Master 派全新子代理；PO 逐份强审，指出的问题 Developer 直接改，改完 PO 再看一遍 | 无必改项；验收 5、6 过线；PO 说行（验收 8） |
| 9 | 收官前同步 Codex | `scripts/sync_codex.py`、`scripts/check_codex.py` | 0 不一致（验收 7） |

**Key choices**

- **worktree**：PO 建议开 worktree；Developer 在 `.claude/worktrees/` 里改，主目录不动；分支与文件夹同名，不带 `worktree-` 前缀。
- **清单是收官条件**：98 行，每行一条约定、一份模板或一处 `SKILL.md`；每行写 PO 的意见、结论（改 / 不改 / 挪到别的 PBI）和依据，状态走 待看 → 已定 → 已改 → 已核。
- **一份文件定完再改**：意见定下后一次改完，Master 审，PO 看结果；比一条一改来回少，也比攒到最后更早看到效果。
- **样板先行，不单开设计**：结构是品味题，反馈链太长，所以先用 design-log 当样板看形状，再套到其余几份。
- **按日志分三块，各一份约定**：不按步骤拆文件，也不合成一个文件（每走一步要整份重读）。
- **只改有依据的点**：原定 PO 没提的文字一字不动，后改成「没有依据的文字不动」；结构调整只挪不改；新文字单列，可被单独圈阅或撤掉。
- **只改英文原文**：中文译文由 PO 的 Stakeholder 会话做，不进仓库。

**Risks and open points**

- 中间提交里 Codex 包落后于 Claude 侧：PO 定收官前一次同步，与 CLAUDE.md「同一提交里跑同步」不同；收官时已同步，0 不一致。
- 连带改动面广：删、合并约定会改号（共改三次），牵到模板、四个命令、两份 `SKILL.md`、CLAUDE.md、README；`scrum/documents/` 的归档是历史，不改；仓库外的全局记忆引用「sprint-log 约定 13、14」，不归 Developer 改，由 Master 收官时经 PO 同意处理。
- 版本号：PO 把版本交给 Master，定 5.2.0（模板和约定的结构都变了，但已有项目的日志照旧能用）。
- 技能描述：这次没动。

Go-ahead: 2026-11-10，Master 放行，PO 授权（「让他继续往下走」）——3.1 第 2 到 7 项：在冲刺分支上提交；不推送，不合入，不打 tag，不同步 Codex。停点：① 设计这块改完，发消息给 Master 审，审过再做 scrum 这边；② scrum 这边和连带改动做完后交 Master 审，审过再做第 8 项，然后交 PO 强审。第 1 项由 PO 定结构后放行。

### 3.2 Notes

| Date | What was done | Decision and reason | Evidence | Next |
| --- | --- | --- | --- | --- |
| 2026-11-10 | Planning：PO 定 Sprint Goal、选 PBI，开冲刺；Developer 开 worktree，登记 PBI-47～50，建 98 行审定清单，复述验收、写 How | 同名文件的四条登记为 PBI-47～50（PO：都可以列成 PBI）；Master 审开冲刺与 How：通过，一处必改——Developer 是 `/fork` 出的独立会话，能派子代理，不受主会话 plan 模式影响（我原先照 CLAUDE.md 里 Agent 工具式 fork 的说法写错了）；通道改为 Master 与 Developer 直接发消息 | 产品日志 PBI-40、47～51；清单 | 样板 |
| 2026-11-10 | 样板（3.1 第 1 项，`72e64fc`）：design-log 加流程图并按图排序，条文逐字不动；样板三道题改前对改后各 5 次，30 次都一次成功 | PO 定：做插件，不做 index，照结构建议做。**测试没过线**：每题至少 4/5，合计改后 14、改前 15；改前基线满分，没有余量；两处边缘判定 Master 维持；失败原因在约定 3（填表头，表头里有分支一栏）排在约定 4（定分支）前面，改前改后一样，与结构无关。PO 接受结构，让往下走，不重跑、不改标准 | `sample-test-summary.md`（已删） | 设计这块 |
| 2026-11-10 | PO 新定（Master 转述）：阶段之间由 PO 决定、冲刺日志改五章、How 写成 plan、收官前 PO 强审；登记 PBI-51；做法改为 Developer 起草、Master 审、PO 强审 | 每处改动要有依据（见 2.2「Master 定」）；本冲刺自己的日志不改成五章 | 2.2 | 设计这块 |
| 2026-11-10 | 设计这块修订稿（`7e3e5b6`，停点 1）；Master 审后三处必改（`9ff405d`）；PO 补定设计模板结构（`46bdccf`） | 必改：共情的顺序理成一个（先找当事人，据此写挑战、目标、问题，还不清楚再问专家、改地图），「PO 决定什么」只留一份清单，小设计一个阶段也不跳、测完的决定并进阶段之间的门；PO 补定：设计模板去掉发现、POV、点子池，POV 整条去掉，IDEO 写成必须——先要列方法名、后改成只写原则，以后一次为准 | 清单设计这块各行 | scrum 这边 |
| 2026-11-10 | scrum 这边和连带改动（`a8095ef`、`c861574`、`17b46d9`）：overview、product-log、sprint-log、冲刺日志模板、`SKILL.md` 分工一段；四份约定重排条号 | 131 处「convention N」引用逐处对到短名，0 错。核对中发现并改了一处：product-log 17 起草时误指向 overview 5。改号脚本只保证改前改后一致，不保证指针指对，所以要逐处读所指的条是不是真有那句话（Retro） | 清单（现号栏、改号对照、核对） | Master 审停点 2 |
| 2026-11-10 | Master 审停点 2：通过，七处必改（`87bd0db`）：IDEO 在设计里每个阶段都要用、Departures 表删一行、短名去掉「Stage N」、sprint-log 加 Ask the PO、overview 1 与 product-log 1 并成一处等；流程测试的测法定下 | 测法 Master 定（PO 授权）：无头 `claude -p`，Haiku，空项目，约五题，每题 3 次至少 2 次过；先冒烟；题目与过线标准先提交（`1b07623`、`a87bd1c`，含 Master 改的三处判定说法） | 2.2「测试」 | 流程测试第一轮 |
| 2026-11-10 | 流程测试第一轮（`87bd0db`）：冒烟后 5 题 × 3 次，15 次都在第一次调用成功 | 题 1、4、5 各 3/3；**题 2 为 1/3、题 3 为 0/3，没过线**。题 2 内容三次都对，两次只加载了技能、没读约定文件；题 3 三次都没加载 scrum-kernel，白纸项目先从设计开始一次也没碰到。照规矩不改判、不改标准、不加跑 | `flow-test-summary.md`（已删）；原始输出在仓库外 | 对抗审查 |
| 2026-11-10 | 对抗审查：Master 派全新子代理对 `2aad30f..87bd0db` 挑错；Developer 照改（`94a6758`，重排条号 `c35c4df`）；流程测试第二轮（`c35c4df`） | 七处必改、六处小改、一处不改：构思的发散必含 IDEO 方法、删 design-log 一条、sprint-log 4 指向错误、阶段拍板与 `scrum/` 保鲜与白纸判断各只留一处、冲刺模板第 1 章补决定。题 2、3 没过线，Master 选 (a)：design-kernel `SKILL.md` 加一句指向 product-log 2，两份 `SKILL.md` 写明回答怎么做的问题之前也要先读约定，不改技能描述。第二轮：题 2 升到 2/3 过线，题 3 仍 0/3 | 清单；`flow-test-summary.md` | PO 的意见 |
| 2026-11-10 | PO 的两点（Master 转述，`f495298`）：设计不做 Review 和 Retro；贯穿全程加 IDEO in every stage。流程测试第三轮；`plugin-validator` 第二、三次 | 设计是整个 Scrum 工作里的一个子集，不单独收尾：design-log 原 19 删，原 18 改成 When the design ends，设计日志由它服务的冲刺在 Review 时归档，教训进那个冲刺的 Retro。第三轮：题 1、4、5 各 3/3，题 2 为 2/3，题 3 仍 0/3；validator 两次 PASS | 清单；`flow-test-summary.md` | PO 强审 |
| 2026-11-10 | Master 答 n、o（`63ee408`）：设计日志的归档动作只写在 sprint-log 的 Review（现 17）：已结束、还在自己文件夹里的设计的日志，压缩、改名 `design-<后缀>.md`、移进 `scrum/documents/` | 「它服务的冲刺」统一改成「设计结束后的第一个冲刺 Review」，白纸设计和服务多个冲刺的设计都适用；design-log 18、overview 5、设计模板头部改成指向它 | 清单 | PO 强审 |
| 2026-11-10 | PO 强审第一批（`c1ee678`，重排条号 `ec5d30a`） | 一、删 overview 的「When a revision applies」：讲维护本插件约定的节奏，是作者自己的事，CLAUDE.md「Sprint 节律」已有；二、product-log 2 对照表末行的设计一栏改成 the target，白纸设计结束时选 target 再拆 PBI；三、去掉约定的版本标记（PO：以后更新都是重构，不要版本这种标志）。改号后 143 处引用逐处对到短名，0 错 | 清单第六轮 | PO 强审收尾 |
| 2026-11-10 | PO 强审结束（「别的就没什么问题了」，其余交 Master 定）；第一阶段（`aa473c6`）：sprint-log 11 改 Outline before full text；设计结束时记一两句教训；最后一轮（第四轮）流程测试 | sprint-log 11：写新的长期文档或新模板之前先给大纲（各级标题，每部分一句话），同意了再写全文，新模板的大纲就是章节清单。设计结束时在第 5 章末尾、PO 的决定旁写一两句做法上的教训，留给那个冲刺的 Retro（设计不单做 Retro，隔得久会忘）。第四轮：题 1、4、5 各 3/3，题 2 为 2/3，题 3 为 0/3——3-2、3-3 的内容三条必答都答对了，只差「读到约定文件」，字面上仍不过，记为已知缺口，登记 PBI-52；标准没改、没改判 | `flow-test-summary.md`（四轮对比） | 收官 |
| 2026-11-10 | 子代理的开销：四次 `plugin-validator` 都没写 `model`，继承了主会话的 Sonnet，每次约 22 到 27 万 token | PO 嫌费，要求用 Haiku：写进用户级 CLAUDE.md，此后派子代理一律显式写 `model`；Master 定此后收官时先跑一次官方 `claude plugin validate --strict`，它报问题或结构有变才派子代理（Retro） | 用户级 CLAUDE.md | — |
| 2026-11-10 | 收官：Review、产品日志保鲜、Retro、版本 5.2.0、同步 Codex | 见第 4 章。Retro 的教训写进了 CLAUDE.md（回归测试、Sprint 节律、插件验证、模板规约、冲刺收官与归档）和项目记忆 `po-reads-whole-documents`（SeaPawn-Memory 提交 `c28d03b`） | 第 4 章 | 交 Master |
| 2026-11-10 | Master 审收官提交：通过，四处并进收官提交 | 验收 8 改为通过（最后两处改动 PO 交 Master 定，Master 核过），验收 1 照旧写「部分」；设计模板头部的路径改成写明基准目录，重跑 sync、check、validate；`scrum/documents/` 两件都留；PBI-25 加 marketplace.json 缺 description 一项 | 第 4 章 | 2b：合入 main、推送、更新本机插件 |

**Developer 提给 Master 的问题与答复（摘要）**
- 范围：连带改动登记在清单第二张表；「全仓」不含 `scrum/documents/` 的归档（历史），`codex/` 是生成物、随同步更新；CLAUDE.md 在收官提交里改；仓库外的全局记忆由 Master 收官时经 PO 同意处理。
- sprint-log 的 Throughout 加一条 Ask the PO（现 25），与 design-log 的对称，只列指向；overview 1 写规矩、product-log 1 只写做法，只留一处；小 Sprint 一条里「PO 仍在每个阶段结束时拍板」的依据改成 overview 的 Product Owner decides between stages；短名去掉「Stage N」前缀；Departures 表删「Closed logs…」一行（官方没有对应说法，不是偏离）；overview 的图不标条号（它跨好几份文件）；sprint-log 特殊情况表删五行（各有别的条覆盖）。
- PBI-40 ⑧（Developer 在别的工具里）这次不做，收官时拆成新 PBI。

## 4. Review

**增量**（PBI-49、47、48、50 和 PBI-40 的大部分；发版 5.2.0）：四份约定（overview 17 条、product-log 18 条、sprint-log 25 条、design-log 26 条）、冲刺日志模板和设计日志模板（产品日志模板核过，不改）、两份 `SKILL.md`（design-kernel 的五阶段表与几处说法，scrum-kernel 的分工一段）、`ideo-kernel/SKILL.md` 一行、`developer` 命令一行，经 PO 逐份强审改定；插件 diff 共 10 个文件（`2aad30f..aa473c6`，+276 −205；收官提交在插件里只再改 `plugin.json` 的版本号和设计模板头部一处注释），技能描述没动。用户会看到的变化：
- **形状**：每份约定先一张 `flowchart TD`（节点标条号），条按图排序，小标题与节点同名；每条第一句是祈使句；一条规矩只写一处；来源标签只标例外；约定不带版本标记。
- **overview**：图画整个流程，含「白纸」入口和冲刺五个阶段；新增 Product Owner decides between stages 与 Working material 两条；删「When a revision applies」；Departures 表加 Why 列，只留七行真偏离。
- **sprint-log 与冲刺日志模板**：冲刺五个阶段 Why、What、How、Increment、Test，日志五章；How 写成 plan；新增 Record the tests、The Product Owner decides at the end of each stage、Ask the PO，Structure before full text 改成 Outline before full text；Review 和 Retro 是收官动作，不设章；七步精化并入 Refine in seven steps；特殊情况表删去重复的五行。
- **product-log**：One product log 加老项目怎么写；Blank page 加对照表（设计的挑战、目标、问题、地图 ↔ 产品日志的产品、Product Goal、完成标准、架构），白纸时从设计开始。
- **design-log 与设计日志模板**：构思拆成发散、收敛（PBI-47：每个草图至少两种方法发散，至少一种来自 ideo-kernel 的构思方法）；Start from the people；每个阶段一道门，按 IDEO 各模式的重心检查（PBI-48）；Write the criteria before the test；小设计也是设计；IDEO in every stage；设计不做 Review 和 Retro（When the design ends，日志由设计结束后的第一个冲刺 Review 归档）；Open a design for a question with no ready answer 写明什么时候必须开设计（PBI-50）。模板去掉发现、POV、点子池，原型、测试不分小节。
- **两份 `SKILL.md`**：design-kernel 的五阶段表改成「IDEO 模式和重心｜书的步骤」，加白纸指向；两份都写明回答怎么做的问题之前也要先读对应的约定。

**DoD 与验收**：

| 项 | 结果 |
| --- | --- |
| DoD 内容忠实 | 通过：改动只在上面 10 个文件里，每处在清单有结论和依据；design-kernel 的书摘、ideo-kernel 的方法库、Scrum Guide 与 SGEP 原文没动 |
| DoD 可导航；无死链 | 通过：Codex 包同步后 `check_codex.py` 本地链接 10、资源 77，内容、链接、导航错误各 0；四次 `plugin-validator` 都 PASS，第四次逐个解析了 145 处「convention N」引用和约 266 个路径，都解析得到，只有几处写法上的小问题（列在审阅发现）；官方 `claude plugin validate --strict` 对插件目录通过 |
| DoD 只改 Claude 侧；Codex 收官时一次同步 | 通过：冲刺里 `codex/` 没动；收官前同步一次，`sync_codex.py` 写了 17 个文件（10 个是插件改动的镜像，2 个是版本号，5 个只是换行差异），改设计模板头部那处注释后重跑，又写了那一个镜像；`check_codex.py` 0 不一致 |
| DoD 不改技能描述 | 通过：插件 diff 里 `description` 行 0 处改动，没有重跑触发测试的需要 |
| 验收 1 清单每行有结论和依据 | 部分：98 行都有结论和依据——97 行改，1 行不改（产品日志模板，章节与注释和新约定不冲突）。但状态没有全部走到「已核」：97 行停在「已改」。PO 强审是整份读的，不是逐行勾；Master 的核对在停点 1、停点 2 和对抗审查上，清单里也没有逐行记。「PO 强审时全部打勾」没有按字面做到，实际由两次 Master 审、对抗审查和 PO 的整份强审替代 |
| 验收 2 定了的都改了；Master 核 diff | 通过：停点 1 三处必改、停点 2 七处必改，Master 核过都对；对抗审查七处必改、六处小改，已改；PO 的意见（设计模板结构、POV、IDEO 必须、设计不做 Review 和 Retro、强审两批共五处）都已改 |
| 验收 3 diff 只落在有依据的改动上 | 通过：插件 diff 的 10 个文件全在清单里；我自己拿主意的几处（如 design-kernel `SKILL.md` 的 Define 行顺手对齐「No target step」）都在 3.2 或交审时向 Master 报告过 |
| 验收 4 旧说法 0 残留；引用 0 错 | 通过：脚本把「convention N」引用对到短名，三次改号（131、140、143 处）都是 0 错，最后一次核对 144 处全部解析到存在的条；第四次 `plugin-validator` 独立核了 145 处匹配，全部指到对的文件和存在的条号。旧说法：收官前全仓 grep（插件、README、CLAUDE.md、`scrum/` 现行文件、`codex/`；`scrum/documents/` 的归档是历史，不查）旧路径与旧说法，0 残留（产品日志 3.2 里已完成条目的旧名字，如「约定 v1」「conventions/overview.md」，是历史记录，不改） |
| 验收 5 无死链；plugin-validator 通过 | 通过：四次 PASS（`87bd0db`、`c35c4df`、`f495298`、`aa473c6`），无必改项，每次 5 到 8 条建议，多数是冲刺之前就有的小问题（见审阅发现） |
| 验收 6 流程题 | **没有全部过线**：四轮（跑在 `87bd0db`、`c35c4df`、`f495298`、`aa473c6`，每轮 5 题 × 3 次，Haiku，题目与判定标准先提交、没改）——题 1、4、5 每轮 3/3；题 2：1/3 → 2/3 → 2/3 → 2/3，第二轮起过线；**题 3（白纸项目）四轮都是 0/3**，登记为 PBI-52。原因出在触发和读约定，不在内容：四轮 12 次一次也没读 product-log；前三轮 9 次里 4 次一个技能都没加载，scrum-kernel 一次也没加载；第四轮三次都加载了 design-kernel，其中两次内容三条必答都答对，只是没读约定文件，按判定标准仍判不过。标准没改，也没改判 |
| 验收 7 Codex 同步 | 通过：见上，`check_codex.py` 0 不一致 |
| 验收 8 PO 强审 | 通过：PO 强审了四份约定和三份模板，两批意见已改；最后两处（sprint-log 11 改名、设计结束时记教训）PO 交 Master 定（2026-11-10「你决定即可」），Master 核过 |

**审阅发现**：停点 1 三处必改、停点 2 七处必改、对抗审查七处必改，都改了（见 3.2）。`plugin-validator` 四次 PASS；第四次的建议里有一条是本冲刺改出来的：设计模板头部指向 sprint-log 的路径没写基准目录。Master 审收官提交时定改，已改成写明是 scrum-kernel 技能的 `conventions/sprint-log.md`，重跑了 `sync_codex.py`、`check_codex.py` 和 `claude plugin validate --strict`，都过；所以发布版与跑流程测试的 `aa473c6` 相比，插件里只差这一处模板注释，加 `plugin.json` 的版本号。其余建议多数是冲刺之前就有的小问题，登记进 PBI-25 ⑦：product-log 与 sprint-log 开头「`overview.md` (…), convention 15」的括号插在路径和号之间；overview 里裸写的 `sprint-log.md`、`product-log.md`；三处引用与条名贴合得宽松；插件没有图标。`marketplace.json` 缺顶层 description，官方校验加 `--strict` 时退出 1（不加则只是警告），旧问题，登记为 PBI-25 ⑧。摘录文件头的 ATTRIBUTION.md 在插件外、装好的缓存里没有，是 PBI-25 ① 已有的问题。Developer 没越过放行：全部提交在冲刺分支上，没推送、没合入、没打 tag，Codex 到收官才同步。

**利益相关者的看法**（「熟手」卡，Haiku，全新子代理，只读；Master 召唤）：愿意照新版走下一个冲刺。顺手的三处：overview 分组清楚，偏离官方的地方集中在一张表里并带理由；冲刺模板每章注释标了约定号和 PO 在这章定什么；design-kernel 五阶段表先写 IDEO 的重心，能判断这一段做没做到位。缺口（Master 核过原文都属实）：① 冲刺模板头部没有设计模板那样的 Now 行，断线后要翻五章才找到最后一个 PO 的决定，sprint-log 的 The log is the handoff 只说日志是交接，没说接手从哪看起；② design-log 的 When the design ends：设计日志的归档和教训都要等设计结束后的第一个冲刺 Review，熟手会卡住——这是 PO 定的（设计是整个 Scrum 工作里的子集，不单独收尾），照记为看法，不改；③ sprint-log 的 Checkpoints, not stand-ups 写「whenever the AI is stuck」，没说什么算卡住（PBI-40 ③ 只解决了一半，阶段结束这个触发点有了）；④ sprint-log 的 Review 写「delete what is outdated」，没说怎么判过时。另一条「sprint-log 的 The Product Owner decides at the end of each stage 要跳到 overview 才看得全 PO 的决定」是一条规矩只写一处的代价，接受。①③④ 与 ② 的看法登记为 PBI-54，作为约定下一次集中修订的输入。

**产品日志**：
- PBI-49、47、48、50 移入 3.2，出处是本归档。
- PBI-40 移入 3.2：① 不再需要（设计不做 Review，没有设计 Review 模板的需要）；② 做了（Ask the PO：sprint-log 25、design-log 20）；③ 做了一半（阶段结束、AI 卡住、PO 问进展三个触发点写明，「卡住」没说清，进 PBI-54）；④ 做了（overview 15：越过约定时把做了什么、为什么写进日志的笔记）；⑤ 做了（每份约定先一张图；一条规矩只写一处；七步精化并入 sprint-log）；⑥ 做了（sprint-log 18：没有记忆文件也没有说明文件，就新建一个说明文件）；⑦ 做了（product-log 1：老项目怎么写）；⑧ 没做，拆成新 PBI-53。
- 新增 PBI-53（约定写明 Developer 在别的工具里时怎么协作）、PBI-54（熟手的意见：约定第二次集中修订）。
- PBI-51、52 留在 3.1（PBI-52 备注补第四轮的观察）；PBI-25 补 ⑦、⑧；PBI-12 备注补一句（ExpertNotes 的附录图 `five-stage-mapping.svg` 里冲刺还是旧的三段，用前要改成五个阶段）；PBI-30、44、45、46 的过时备注改掉；2.2 架构图加白纸入口，How 的「方案」改「计划」，⑥ 改成 Test，⑦ 把已结束的设计日志也算进归档；1.2「之后的方向」补上 Sprint 14 的结果。
- **Product Goal** 不变（Master 核过，没有反证）。
- `scrum/documents/` 过了一遍，拿不准的两件都留（Master 定）：`conventions-review-log.md` 是 Sprint 11 的审阅记录，属历史；`five-stage-mapping.svg` 是 ExpertNotes 的素材，见上面 PBI-12。

**发布**：版本 5.2.0（PO 把版本交给 Master：模板和约定的结构都变了，但已有项目的日志照旧能用）；tag `sprint-14-conventions-tuning` 与 `v5.2.0`。PO 2026-11-10 同意收官后推送 main 与两个 tag，并把本机 Claude Code 的插件更新到 5.2.0；本机 Codex 的安装不动（这次只做 Claude 版，Codex 包已同步到 5.2.0）。
