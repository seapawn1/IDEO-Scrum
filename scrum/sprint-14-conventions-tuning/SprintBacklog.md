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
- 做法（2026-11-10 改）：Developer 照已定的方向起草修订，Master 审，最后 PO 强审，PO 指出的问题 Developer 直接改；不走 plan 视图审阅。原做法是 PO 对着全文逐条说哪条不对、怎么改，Master 和 PO 商量，定了就改。PO 用中文说，译文由 PO 的 Stakeholder 会话做；每条意见先分清是英文原文的问题还是译文的问题，Developer 只改英文原文（CLAUDE.md「对着译文审阅」）。
- 顺序：先做设计这块——design-log、设计日志模板，连同 47、48、50；scrum 这边（overview、product-log、sprint-log 与两份模板）随后，慢慢做。
- 结构方向：每份约定先一张架构图，再一批约定；overview 多一节（第 3 节），写与官方指南不同的地方和理由。细节见下面的结构建议。
- 分工：Master 管理、顶层设计；开分支、写日志、改文件都由 Developer 做。Developer 是从 Master 会话 fork 出的 Claude 会话，在 worktree 里干活；它带着 Master 的上下文，审阅仍由 Master 做（sprint-log 约定 16）。通道是本日志，加跨会话消息：Master 直接给 Developer 发消息，不经 PO 转；长的审阅仍写在 plan 文件里，消息给路径；Developer 交活时也直接发消息给 Master（PO 2026-11-10 定，Master 转述）。
- 只做 Claude 版：冲刺中不同步 Codex；全部改完后一次跑 `scripts/sync_codex.py` 和 `scripts/check_codex.py`。
- 现在就开（距上次集中修订 Sprint 11 一天；CLAUDE.md「约定大约每周集中改一次」）。
- 做插件，不改成全局记忆；约定不改成 index，照本节的结构建议做；其余交 Master 定（PO 2026-11-10，Master 转述）。
- 样板：PO 接受样板的结构（PO：「之前提的那几个点确实都改了，没问题，很好。」）；三道题没过线，PO 让继续往下走，不重跑，不改标准（Master 第四轮转述）。
- 阶段之间由 PO 决定：设计的五个阶段之间、冲刺的各阶段之间，每个阶段结束时由 PO 拍板——定下这一段的结果，决定进不进下一段；除非 PO 明确把这件事交给 Master。这是做决定，不是审阅或验收：检查做得对不对是 Master 的事（PO 2026-11-10 补充）。只管到阶段这一层，不细到阶段里的每一步（挑战、目标、问题、地图、HMW 等）。PO 说冲刺有 4 个阶段，确认点具体放在哪里，改 sprint-log 时再定。
- 冲刺日志改成五章，五个阶段，和设计日志同一个样子（PO 2026-11-10 定，后一次说法为准）：第 1 章 Why、第 2 章 What、第 3 章 How 不变；现在的 3.2 Notes 改名为 Increment notes（增量笔记），单独成为第 4 章；第 5 章是 Test，不是 Review：Developer 的测试、Master 的审阅、PO 的端到端测试，以及 DoD 和验收标准逐项的结果，都记在这一章，测试里发现的问题当场改，改完再测。Review 和 Retro 不设章，是收官时的动作：Review 是压缩日志、归档、保鲜产品日志，利益相关者的看法落到产品日志；Retro 是把教训写进记忆或说明文件。设计日志同理：五章就是五个阶段，收官是动作。冲刺五个阶段结束时 PO 各拍一次板：Why 定 Sprint Goal；What 定精化到此为止；How 放行；Increment 定可以进入测试；Test 定收官（做 Review、Retro）还是回去改。
- How 写成「类似方案」的一节：不要写太细；模板里直接这样说，不必注明出处。
- 收官前 PO 强审：PO 逐份审四份约定（overview、product-log、sprint-log、design-log）和三份模板，审出的问题由 Developer 直接改。
- 登记 PBI-51：把技能做成由 index 引领的记忆系统。PO 想以后这样做，但还不确定；本冲刺不做。
- 两个入口，同一份产品日志（PO 2026-11-10 定方向，Master 转述）：看情况替换——能定义出来的，直接写产品日志；定义不出来的，用设计里对应的那一项替换，交给设计去回答。连产品和 Product Goal 都写不出时，就从设计开始（白纸）。对照表：

  | 设计（共情、定义两章） | 产品日志 |
  | --- | --- |
  | 挑战 | 1.1 产品 |
  | 设计目标 | 1.2 Product Goal |
  | 设计问题（测试后答出来的） | 1.3 完成标准（成效的度量）；没答出来的变成 PBI |
  | 地图最上面的人 | 2.1 利益相关者 |
  | 地图 | 2.2 架构 |
  | 地图上的步骤 | 3 PBI（每条放在地图的某一步上） |

  落到哪里（做法 Developer 定，PO 强审时看）：
  - overview 的图：加上「白纸」这个入口，从一开始就可以先进设计；现在的图里只有「某条 PBI 需要设计」才进设计。
  - product-log 约定 2「白纸」：对照表只写在这一处，总览和设计日志的收官约定都指向它。被替换的那一节，写明由哪份设计在回答，并链过去，不把设计日志的内容抄一遍；利益相关者那张表可以先写，因为设计一开始就要用角色卡。
  - design-log 的收官约定（18）：结论按对照表写进产品日志；白纸设计收官时，地图上的步骤拆成 PBI，先做哪些由 PO 排。不加「选目标点」这一步（约定 10 的拆分已经覆盖）。
  - 判断走哪个入口：凭现有的了解写不出产品和 Product Goal，就先开设计。这和 PBI-50「没有现成答案的问题先走设计」是同一个判断，写在一起。
- 设计模板的结构（PO 2026-11-10，Master 转述）：去掉单列的发现一节，发现附在挑战、目标、问题三节里并注明来源（约定 23 照留，改指这三节）；去掉点子池一节，点子由每个子代理在自己内部消化、不落盘（约定 24 改成给每个出隔离草图的子代理下任务时，要它先发散——至少两种方法，先求量、不评判——再收敛成自己那一份草图，点子是工作材料、不进日志；约定 12 跟着改）；原型一章只留「各部分」一张表，不分小节，试跑并到测试一章（约定 16 跟着改）；测试一章不分小节，自由写，保留一句注释：对 1.3 的每个设计问题给出答案和证据，写明结论回流到哪里；约定 25（测前写判据）照留，写在这一章里；门表（约定 26）的「日志里有什么」一栏照各章重写。冲刺模板的 Test 一章同样不分小节，注释写明这一章记什么：Developer 的测试、审阅人的检查（默认 Scrum Master）、PO 的端到端测试，以及 DoD 和验收标准逐项的结果；测出的问题当场改，改完再测。
- POV 整条去掉（PO 2026-11-10，Master 转述）：书里的设计冲刺不要 POV；第 1 章的挑战、目标、问题加上地图，合起来就是 POV，不用再单写用户、需要、洞察。定义一章就是地图和 HMW：HMW 对着地图写，同时参考第 1 章的挑战、目标、问题（约定 10、模板定义一章的注释、五阶段表的定义一行、门表的定义一行都照这个）。映射：共情＝挑战、目标、问题；定义＝地图、HMW；构思＝先发散（必须有）、再收敛成方案；原型就是原型；测试就是测试。
- IDEO 一定要融合进设计冲刺（PO 2026-11-10，Master 转述；后一次说法为准）：这里的设计冲刺只是骨架——阶段和书的步骤；每个阶段需要的详细方法论，到 ideo-kernel 里找：阶段前读这一阶段对应的 IDEO 模式文件、照它的重心做，从那里挑合适的方法，用前读方法文件；语气是必须。书的步骤和这一阶段的 IDEO 模式两样一起做，不是二选一。不给每个阶段指定方法名：五阶段表每行写 IDEO 这一模式的重心和书的步骤；模板各章注释不列方法名；门表用 IDEO 的重心做检查。规矩只写在 SKILL.md，约定 7 指向它。
- 冲刺里的 How 用 plan，不用 solution（PO 2026-11-10，Master 转述）：PO 担心以后的 AI 把冲刺的 How 和设计的方案搞混（中文都叫「方案」）。冲刺模板第 3 章和 sprint-log 约定 7 一律用 plan，不用 solution，并写明一次区别：How 是 Developer 怎么做出选中条目的计划，写到做法这一层，不写步骤；它不是设计里选出的方案——设计若给了方案，How 计划的是怎么把它做出来。
- overview 补一句（PO 2026-11-10，Master 转述；写 overview 时做）：工作材料不进日志；真正关键的内容可以存进项目的记忆或说明文件，大份重要的文件放进 `scrum/documents/`；照约定的写法，不写具体工具。

**结构建议**（Master 提；PO 先说「Master 的这些修正都不错，你可以考虑」，后定：照本节的结构建议做）
1. 图画流程，每个节点标出适用的条号；约定按图的顺序排，小标题和节点同名。图放在约定文件里，不放进模板，所以不与 overview 约定 15「模板只记产出」冲突。设计这块：「构思」画成两个节点——发散、收敛（PBI-47），每段的重心写进对应节点（PBI-48）。
2. 一条规矩只写在一处：跨文件的规矩只留在 overview，其他文件不再重复。例：「目标固定、计划可变」现在写了四遍（overview 16、product-log 18、sprint-log 3、design-log 21）；sprint-log 21 的特殊情况表大半在重复别的条。
3. 每条第一句就是规矩，一句祈使句；理由不明显时才加一句；和官方不同的理由搬到 overview 第 3 节，条里只留一个指向。
4. 来源标签只标例外：文件开头写一次「以下都是作者的做法」，只在 Supplement、Decide on the spot 和引文处单独标。（与同名文件的「每条标明」不完全一样。）
5. 样板先行，不单开设计：先用 design-log 当样板——只调结构（挪位置、加图，一个字不改），PO 看形状；再派一个全新的 Haiku 子代理，只给这一份文件，问三道「你在某一步，先做什么」，题目和过线标准事先定好；答对了，再套到其余几份。

**Master 定**
- 没有依据的文字不动（2026-11-10 改，原为「PO 没提的文字一字不动」）：每处改动都要能对到清单里一条已定的依据。依据有四种：PO 的决定；PBI-40、47、48、50 的输入；结构建议第 2 到 4 条；Master 的提议。清单的「结论」栏写清改了什么、依据是哪一条。插件文件里不做任何标记：PO 强审时一视同仁地看（PO 2026-11-10）。新写的文字（如架构图）仍在清单里单独列出，方便 PO 圈阅。
- 样板的发现进 design-log 的修订：定分支排在填表头之前（或并进「开设计」那一条）；依据记为「样板发现」。
- 「阶段之间由 PO 决定」是跨文件的规矩：正文只写在一处（overview）；design-log 和 sprint-log 的图上标出 PO 拍板的点，并指向 overview 那一条。
- 本冲刺自己的冲刺日志不改成五章：约定的改动从下一个冲刺起生效（overview 约定 14），这次只把决定记下来。
- 改一条规矩，就全仓找它在模板、四个命令、两份 SKILL.md、CLAUDE.md、README 里的其他说法，列成连带改动一起改；删、合并约定要改号，用脚本把每处「convention N」重新对到短名。
- 本冲刺照 5.1.2 的约定走；改动从下一个冲刺起生效（overview 约定 14）。
- 不推送、不合入、不打 tag，收官时 PO 定。

**Master 对设计日志的提议**（写进 design-log 的修订，文件里不标记）
1. 每个阶段设一道门：离开这个阶段前，日志里必须有哪些产出；标准取 IDEO 各模式的重心。门上由 PO 拍板，这一点是 PO 已定的。
2. 共情先找当事人；每条发现都标明来源。
3. 模板补格子：共情发现、POV、点子池，以及原型的每一部分测哪个问题。
4. 小设计。
5. 测试前先写判据；写明角色卡测试的局限。
6. 测完由 PO 决定收官还是回到前面的阶段。
7. ~~设计收官时的 Review 章~~（撤回：PO 定 Review 是动作、不设章）。设计收官时，归档就是压缩后的日志本身，五章不变，不另加 Review 章；这也回答 PBI-40 ①（设计收官没有 Review 模板）。约定 18 里列的 Review 内容，对到各章去（例如存着原型的提交写进原型一章）。

**验收标准**
1. 清单（`checklist.md`）每行都有结论——改、不改、挪到别的 PBI——并写明依据；在 PO 强审时全部打勾。
2. 定了要改的都已改；Master 对照结论逐条核 diff。
3. diff 只落在有依据的改动和登记的连带改动上。
4. 改过的规矩，全仓旧说法 0 残留；「convention N」引用脚本核对 0 错。
5. 无死链、可导航；plugin-validator 通过。
6. Goal 末句：收官前派全新子代理（Haiku），只给改后的插件，答几道流程题；题目与过线标准先提交、后跑，测法由 Master 定（PO 授权，2026-11-10），见下面「流程测试」。
7. 收官前 Codex 同步与核对：0 不一致。
8. 收官前 PO 强审四份约定（overview、product-log、sprint-log、design-log）和三份模板；PO 指出的问题全部改完后，PO 再看一遍，说行才算过。

**测试**：4、7 用脚本，脚本先拿一两份已知结果自测；6 照上面。

**样板的三道题**（2026-11-10 起草，Master 审定；本次提交即定稿，先提交、后跑，跑后不改标准。三道题只用 design-log 里现有的内容）
- 方法：被测文件两份——改前基线（提交 `89406bf` 里的 `design-log.md`）和改后（样板）；三道题都只给 `design-log.md` 这一份。每份 × 三道题 × 5 次，用 Haiku，同日同环境。提示 = 一句交代（「下面是一份文件的全文，你手上只有它。读完回答问题；文件里没写的，就说没写。」）+ 文件全文 + 题目；关掉所有工具，所以只能凭这一份文件答。题目里不提约定名和条号，不带引导词。正式测之前先冒烟：一次最简单的调用，确认 Haiku 可用、关工具的调用方式有效。原始输出放仓库外，仓库里只留判定汇总，提交前扫一遍提供方地址、凭据和设置值。
- 测法：不用 index（PO 2026-11-10 定），所以用上面这套——只给 `design-log.md` 全文、关掉工具（Master 定）。
- 判定：脚本按关键词和出现先后打分，先拿一两份已知结果自测；判错的逐条人工看，改判写明理由。一次回答算过：题 1、题 3 的六条「必答」至少答出五条（题 3 另要求 Review 内容至少三项）；题 2 的第 ⑦ 条必须答出，其余六条至少答出五条；顺序对；没有「不能」项。
- 过线：改后每道题 5 次里至少 4 次过，并且三道题合计的通过次数不少于改前基线的合计。
- 用途：题 1、题 3 主要防样板把事情改坏；题 2 看结构有没有用——现行文字把构思的步骤（约定 11–15）和 IDEO 的构思方法（约定 7）分在两处，没规定先发散后收敛（PBI-47），基线里 ⑦ 可能常被漏掉；图上把构思拆成「发散、收敛」两个节点之后，看它能不能带出来。
- **题 1 开设计**
  - 题目：冲刺精化时，团队碰到一个靠现有资料答不了的难点：新用户第一次打开这个产品，会卡在哪一步。PO 同意为它开一个设计。你这一个会话同时担任这个设计的 Designer 和 Scrum Master。从现在起，到可以开始第一个阶段为止，你要做哪些事？按先后顺序说。
  - 必答（六条）：① 只把这个难点取出来做设计，冲刺的其余部分照常进行；② 建文件夹 `scrum/design-<后缀>/`，后缀写这个设计讲什么、不带编号；③ 把模板复制进去，命名为 `DesignBacklog.md`；④ 填文件头：来自哪里、分支、PO、Designer、Scrum Master、Now 一行；⑤ 一人兼两个角色，Designer 和 Scrum Master 两栏写同一个名字；⑥ 开设计时定分支：从冲刺分支还是从 main 分出，不能叫 `<冲刺分支>/<名字>`。
  - 顺序：① 在最前；② → ③ → ④；⑥ 在 ④ 之前或之中。
  - 不能：给文件夹加编号；把冲刺的其余工作也搬进设计。
- **题 2 构思到选定**
  - 题目：设计走到了构思阶段：前面两个阶段的产出——挑战、设计目标、设计问题、地图，以及 PO 选出的要解决的问题——都已写进日志。目标是让 PO 选定一个方案，再往下做原型。从现在起，到开始做原型为止，要做哪些事？每一步谁做、产出放在哪里？按先后顺序说。
  - 必答（七条）：① 先找现有的点子：子代理并行搜，清单是工作材料，不写进日志；② 几个互相看不见的全新子代理，各出一份完整的方案草图（文字或 Mermaid）；③ Scrum Master 在对话里主持选择，PO 做最终决定，不找共识；④ 只有选中的方案写进日志 3.1；⑤ 能合的方案合并，两个冲突就都做原型、让测试决定，合还是比由 PO 决定；⑥ 故事板可选，需要时由 Designer 写在 3.2；⑦ 构思时也用 ideo-kernel 的构思方法（如 How Might We、Brainstorming、Analogous Empathy），与书的步骤并用或替代。第 ⑦ 条必须答出，其余六条至少答出五条。
  - 顺序：① → ② → ③ → ④；⑤ 在 ③ 之后；⑦ 不设先后要求（现行文字没规定它的顺序）。
  - 不能：由子代理或 Scrum Master 替 PO 选定；把没选中的方案也写进 3.1；先选后找点子。
  - 说明：题面不点名 How Might We，以免提示 ⑦ 的答案；Master 同意这个改法（2026-11-10）。
- **题 3 收官**
  - 题目：设计问题都有了答案，PO 说可以收官。这个设计该怎么收？日志、文件、分支、产品日志各怎么处理，按先后顺序说；教训记在哪里？
  - 必答（六条）：① 把设计日志改写成一份 Review 文档；② 改名 `design-<后缀>.md`，移到 `scrum/documents/`；③ 删掉原型和其他文件（git 留着）；④ 分支：先合并、再删除（做法见冲刺日志约定 20，文件里没有细节，要如实说没有）；⑤ 更新产品日志；⑥ 不设 Retro 一章，教训的写法见冲刺日志约定 19（同样如实说文件里没有细节）。另：Review 里要有的内容，至少答出三项——挑战与设计问题、选中的方案、每个设计问题的测试结论、结论流回了哪里、存着原型的提交。
  - 顺序：① → ② → ③。
  - 不能：把原型留在仓库里；先删文件再写 Review；留一章 Retro。

**流程测试**（验收 6，第 8 项；2026-11-10 起草，测法 Master 定、PO 授权；本次提交即定稿，先提交、后跑，跑后不改标准）
- 被测：提交 `87bd0db` 上的 `plugins/ideo-scrum/`。跑之前核对工作区里的插件文件与它一致；跑的过程中不改插件，改了就整轮重跑。
- 方法：无头 `claude -p --model haiku --plugin-dir <worktree 里的插件>`，只开 Read、Grep、Glob、Skill，Bash、PowerShell 和其他工具都关掉；加 `--strict-mcp-config --no-session-persistence`，用 `--output-format stream-json --verbose` 留下每次调用读了哪些文件；工作目录是系统临时目录里新建的空项目；每次调用是一个全新会话。题目用自然的说法，不带引导词（不说「按插件的约定」「照流程」），题里没有限制行动的话；每题 3 次，共 15 次。不比基线（新内容没有改前版本可比）。
- 冒烟（已做，2026-11-10）：一次最简单的调用，确认模型 `claude-haiku-5-5` 在提供方可用，插件从 worktree 加载，Skill 和读插件目录里的文件都正常，工具只剩 Read、Grep、Glob、Skill 四个。
- 判定：一次回答算过，要同时满足：① 读到了该题对应的约定文件（用 Read 读，或用 Grep 的输出读到文件内容，都算）；② 必答项全中（写了「至少几条」的按写的算）；③ 没有「不能」项。机械的部分（读了哪些文件、五个阶段名的先后）用脚本；语义的部分我逐条读回答来判，每条写下依据的原话。脚本先拿已知结果自测（冒烟那份输出里读过 `sprint-log.md`、没读 `design-log.md`，应各判对；把读的文件换掉的副本应判不同）。判错或拿不准的逐条人工看，改判写明理由，验收时摆给 PO。
- 过线：每题 3 次里至少 2 次过。
- 原始输出放仓库外（系统临时目录 `ideo-s14-flow\out`），仓库里只留判定汇总；提交前扫一遍提供方地址、凭据值、令牌形态和设置值。
- **题 1 开冲刺**
  - 题目：我在做一个帮人整理读书笔记的命令行小工具，产品日志已经写好了。现在要开一个新的 Sprint，把它往前推一步。这个 Sprint 从头到尾会怎么走？每一段做完以后，由谁来决定能不能往下走？
  - 要读：scrum-kernel 的 `conventions/sprint-log.md` 或 `overview.md`。
  - 必答（三条）：① 五个阶段按先后说全：Why、What、How、Increment、Test（回答里按这个先后出现这五个名字，可以加中文说明）；② 每个阶段结束时由 PO 决定能不能往下走（拍板），不是 Scrum Master 或 Developer 自己定，也不只是「审阅」「验收」；③ 至少说出三处具体的决定：Why 结束定 Sprint Goal；What 结束定精化到此为止；How 的放行（go-ahead）；Increment 结束定可以进入测试；Test 结束定收官还是回去。
  - 不能：用 Scrum Guide 的事件（Planning、Daily Scrum、Review、Retrospective）代替这五个阶段来组织回答；说 Sprint 有固定时长（如两周）。收官时把 Review、Retro 当作动作提到，不算违规。
- **题 2 精化碰到没有现成答案的问题**
  - 题目：Sprint 里精化做到一半，碰到一个问题：这个读书笔记工具的用户到底是谁，对他们来说怎样才算好用，我们自己说不清，手上的资料里也没有现成的答案。这时候该怎么办？这个 Sprint 接下来怎么走？
  - 要读：scrum-kernel 的 `conventions/sprint-log.md`，或 design-kernel 的 `conventions/design-log.md`。
  - 必答（三条）：① 为这个问题开一个设计，而不是自己拍脑袋定下答案或直接开始做；② 只把这个难点取出来做设计，Sprint 的其余部分照常进行；③ 设计从共情（Empathize）起：先找当事人、用户，问具体的经历，而不是先出方案。
  - 不能：不做设计、直接定一个用户画像或功能就往下做；让整个 Sprint 停下来等设计。
- **题 3 白纸项目**
  - 题目：我有个想法：给一家社区图书馆做一个帮读者找书的工具。现在手上只有这一句话，没有产品日志，也不知道读者具体要什么。我想把这件事正式做起来，第一步该做什么？
  - 要读：scrum-kernel 的 `conventions/product-log.md` 或 `overview.md`，或 design-kernel 的 `conventions/design-log.md`。
  - 必答（三条）：① 从设计开始，产品和 Product Goal 交给设计去回答；可以先写能写的部分（如利益相关者表，或一条指向这个设计的 PBI），但不先把产品日志写完；② 说明原因：现在写不出产品和 Product Goal，要靠设计去回答；③ 设计的结论会流回产品日志（让设计去填产品日志），之后再用 Sprint 去做。
  - 不能：先把产品日志写完再开始（能写的部分可以先写，见必答 ①）；先出方案或直接做。
- **题 4 设计的构思**
  - 题目：设计走到构思这一步了：挑战、设计目标、设计问题和地图都写进日志了，PO 也选出了要解决的那个问题。接下来怎么得到方案？谁来做，各自怎么做，最后怎么选？
  - 要读：design-kernel 的 `conventions/design-log.md`。
  - 必答（四条，①② 必须答出，③④ 至少答出一条）：① 每个草图先发散再收敛：先用至少两种方法大量出点子（求量、先不评判），再收成自己那一份方案；② 用 ideo-kernel 的构思方法（IDEO），与书的步骤一起用，是必须用，不是可选（判法：回答把 IDEO 方法当作流程里的一步来用，与书的步骤一起，就算过；说成「需要时再用」「也可以用」才算不过；不要求回答里出现「必须」两个字）；③ 几个互相看不见的全新子代理，各出一份完整的方案草图；④ 最后由 PO 做出选择（Scrum Master 主持，不找共识）。
  - 不能：每个草图直接收敛，没有发散这一步；把 IDEO 方法说成可选、需要时再用；由 Scrum Master 或子代理替 PO 选定。
- **题 5 收官**
  - 题目：这个 Sprint 的 Sprint Goal 已经达成，PO 说可以收官了。收官要做哪些事？冲刺日志怎么处理？这个 Sprint 学到的教训记在哪里？
  - 要读：scrum-kernel 的 `conventions/sprint-log.md`。
  - 必答（三条）：① Review 是收官时的动作：把日志压缩成关键决定，改名 `sprint-NN-<后缀>.md`，移进 `scrum/documents/`，删掉其余中间文件；② 要更新产品日志（做完的移走，没做完的回待办，或说「保鲜」）；③ Retro 也是动作：教训以原则的形式写进项目的记忆文件或说明文件（没有就新建一个）。
  - 不能：在冲刺日志里加 Review 章或 Retro 章（或说日志有这两章）。

## 3. How

### 3.1 How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | design-log 样板：只做结构建议第 1 条（图加按图排序） | design-log 加一张 `flowchart TD`（节点是步骤，标现有条号；构思拆成「发散」「收敛」两个节点；贯穿全程的几条写在图下一行）；约定按图的顺序排，保留原编号、不改号，小标题改成和节点同名；每条正文一个字不动；图、新小标题、图下一行单列，可被单独圈阅或撤掉 | PO 接受结构；三道题 14 对 15 没过线，PO 让往下走（见 3.2） |
| 2 | design-log 修订 | Developer 照已定的方向起草的修订稿：新增和改写的约定、改后的图；每处改动在清单「结论」栏写明依据；Master 的七条提议也写进来（文件里不标记） | 清单里 design-log 的行都有结论和依据，状态「已改」；Master 审过（核 diff 对依据），状态「已核」；PO 强审在第 8 项 |
| 3 | 设计日志模板；design-kernel `SKILL.md` 的五阶段表 | 同 2 的做法起草的修订稿；模板的章节清单单独摆出，给 PO 看结构 | 同 2；模板的结构 PO 看过 |
| 4 | overview（含新的第 3 节、「阶段之间由 PO 决定」、图上的「白纸」入口）；scrum-kernel `SKILL.md` 的分工一节 | 同 2 的做法起草的修订稿 | 同 2 |
| 5 | product-log（含约定 2「白纸」的对照表）；产品日志模板 | 同 2 的做法起草的修订稿 | 同 2 |
| 6 | sprint-log（含冲刺日志五章、How 写成「类似方案」、PO 拍板的点）；冲刺日志模板 | 同 2 的做法起草的修订稿；冲刺日志模板的章节清单单独摆出，给 PO 看结构 | 同 2；模板的结构 PO 看过 |
| 7 | 连带改动与改号 | 改过的规矩在模板、四个命令、两份 `SKILL.md`、CLAUDE.md、README 里的其他说法一起改；删、合并造成的改号，每处「convention N」对到短名 | 旧说法 0 残留；引用脚本核对 0 错（脚本先拿已知结果自测）；连带改动登记在 `checklist.md` 的第二张表 |
| 8 | 审阅与校验；PO 强审 | `plugin-validator` 和 Haiku 测试由 Developer 跑；审阅由 Master 做，或由 Master 派全新子代理（sprint-log 约定 16）；PO 逐份强审四份约定和三份模板，指出的问题 Developer 直接改，改完 PO 再看一遍 | 无必改项；验收 5、6 过线；PO 说行（验收 8） |
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

- 结构细节：PO 已接受样板的结构，结构建议第 2 到 4 条作为依据（第 4 条与同名文件的「每条标明」不完全一样，以 PO 的决定为准）；overview 现有的「The map」与新 §1 架构图是同一张还是新画、现有的 Departures 表与新 §3 的关系，做 overview 时定，PO 强审时看。
- 中间提交里 Codex 包落后于 Claude 侧：PO 定收官前一次同步，与 CLAUDE.md「同一提交里跑同步」不同；`check_codex.py` 在中间会报不一致，收官前必须清零。
- 连带改动面广：删、合并约定会改号，牵到模板、四个命令、两份 `SKILL.md`、CLAUDE.md、README；`scrum/documents/` 的归档是历史，不改；`codex/` 是生成物，同步时随之更新（「全仓」的范围见 3.2 的问题 b）；仓库外还有两条全局记忆引用「sprint-log 约定 13、14」（plan-view-review、compact-instead-of-handoff），不归 Developer 改，收官 Retro 时由 Master 经 PO 同意处理。
- 发版与版本号：改的是措辞与结构、行为不变，要不要升版本、升到几，收官时 PO 定；发版则 `plugin.json` 与 README 两处版本号同步。
- 测试：样板的三道题已跑，没过线（14 < 15），PO 让往下走。Retro 输入：改前版本可能满分时，「不少于改前」这条过线要留余量或加次数，而且要在跑之前定。收官的流程题与过线标准收官前再定，测法由 PO 定；题目与过线标准都要先提交、后跑。
- 技能描述：这次不动（1.2）；某条意见若牵出描述的改动，先停下问 Master。

Go-ahead: 2026-11-10，Master 放行，PO 授权（「让他继续往下走」）——3.1 第 2 到 7 项：在冲刺分支上提交；不推送，不合入，不打 tag，不同步 Codex。停点：① 设计这块（design-log、设计日志模板、design-kernel `SKILL.md` 的五阶段表）改完，发消息给 Master 审，审过再做 scrum 这边；② scrum 这边和连带改动做完后交 Master 审，审过再做第 8 项（`plugin-validator`、测试），然后交 PO 强审。第 1 项的放行见 3.2。

### 3.2 Notes

| Date | What was done | Decision and reason | Evidence | Next |
| --- | --- | --- | --- | --- |
| 2026-11-10 | Planning：PO 定 Sprint Goal、选 PBI，开冲刺；Master 写 1.1–2.2，Developer 开 worktree、落盘 | 同名文件的四条登记为 PBI-47～50（PO：都可以列成 PBI）；49 是主 PBI，47、48、50 是设计这块，40 是熟手的意见；PBI-44（SKILL.md 可读性）、45（流程命令）不是约定本身，不选 | 产品日志 PBI-40、47～50 | Developer 复述验收、写 How；Master 审，PO 放行 |
| 2026-11-10 | Developer（fork 出的会话）：开 worktree，分支改名为 `sprint-14-conventions-tuning`；产品日志登记 PBI-47～50、PBI-40 状态改为 Sprint 14、1.2 改三处；建 `checklist.md`（87 行，待 PO 逐行看）；同名文件标 PBI 编号（该文件不入库）；复述验收，写 3.1 | PO 看了 Master 的结构建议，说「都不错，你可以考虑」：写进 2.2，3.1 的第 1 项按「样板先行」排；清单的「输入」栏照 plan 附录 D，另加四处：design-log §1 一行标 PBI-47、48（按 Master 对话里的说明）；overview §1、§3 和 sprint-log §1 三行标现有内容的位置（The map；Departures 表与各条里的 Departs 句；文件开头的流程图），都只标位置，不是意见 | `checklist.md`；产品日志 3.1、1.2 | Master 审开冲刺与 How；PO 放行；放行后做 3.1 第 1 项 |
| 2026-11-10 | Master 审开冲刺与 How | 开冲刺通过；How 通过，一处必改（「fork 的限制」写错：Developer 是 `/fork` 复制出的独立会话，能派子代理，不受主会话 plan 模式影响）；a 连带改动登记在清单的第二张表；b 范围同意，仓库外的两条记忆由 Master 收官时处理；c 样板的三道题现在起草；第 1 项暂不放行：index 方案与「插件还是全局记忆」待 PO 定；通道改为 Master 直接发消息，不经 PO 转（PO） | 本审阅（plan 文件） | Developer 改必改项、起草三道题，提交后停下；PO 定结构后放行第 1 项 |
| 2026-11-10 | Developer 按 Master 审改：删掉 3.1 里写错的「fork 的限制」，第 8 项改写；清单加第二张表「连带改动」；样板的三道题起草进 2.2「测试」；3.1 风险补 index 方案与「插件还是全局记忆」两条待 PO 定，Go-ahead 行写明现状；2.2「分工」的通道改为直接发消息；a、b、c 的答复记在上面的「不清楚的地方」 | Developer 是 `/fork` 复制出的独立会话，能派子代理，不受主会话 plan 模式影响（Master 指出；我原先照 CLAUDE.md 里子代理式 fork 的说法写错了）；通道改为 Master 与 Developer 直接发消息（Master 转述 PO 的决定）；三道题取开设计、构思到选定、收官三段，只用 design-log 现有内容，不受 index 方案影响；第 1 项仍不放行 | 2.2 样板的三道题；`checklist.md` 第二张表 | PO 定 index 方案与「插件还是全局记忆」；PO 与 Master 看三道题；放行第 1 项 |
| 2026-11-10 | Master 第二轮审（消息）：必改项、通道、a/b/c、风险、3.2 通过；Developer 按它改三道题的草稿（没跑过，不算改标准） | Master 要三处改：题 2 加必答 ⑦（用 ideo-kernel 的构思方法），⑦ 必须答出、其余六条至少五条、不设先后——现在的必答清单奖励的正是 PBI-47 要改的只收敛不发散，加上后题 2 才看得出图上拆成「发散、收敛」两个节点有没有用；次数改每份每题 5 次、过线改每题 4/5 且合计不少于基线，3 次太少，一次失误就翻结论；测法跟着结构走，不用 index 才是关工具读全文，用 index 改无头 `claude -p --plugin-dir`；另写明用途。我多改一处：题 2 题面原写「How Might We 问题已写进日志」，会提示 ⑦ 的答案，改成「PO 选出的要解决的问题」（已告知 Master，不同意就改回）；3.1 第 1 项的 Done when 改为「样板的三道题过线」，风险里的测试条同步 | 2.2 样板的三道题 | PO 与 Master 看三道题；PO 定 index 方案与「插件还是全局记忆」；放行第 1 项 |
| 2026-11-10 | Master 第三轮通过，转述 PO 的决定并放行 3.1 第 1 项；Developer 把这几句抄进日志，先提交，再动手 | PO 定：做插件，不改成全局记忆；约定不改成 index，照 2.2 的结构建议做；其余交 Master 定。据此：3.1 风险里 index 方案、「插件还是全局记忆」两条删去；样板测法定为不用 index 的那套；Go-ahead 行写明范围；Master 同意题 2 题面的改法 | Master 消息；3.1 的 Go-ahead 行 | 做 3.1 第 1 项，做完提交、跑样板三道题，交 Master 审 |
| 2026-11-10 | Developer 做 3.1 第 1 项：design-log 样板（提交 `72e64fc`）——加一张 `flowchart TD`，约定按图排序，小标题改成和节点同名，条号不变；脚本核对条文逐字不变；再跑样板三道题（改前基线对改后，3 题 × 5 次，Haiku，关工具，30 次都一次成功），判定汇总在 `sample-test-summary.md` | 结构只做结构建议第 1 条：贯穿全程的 5、6、8、20、21 写在图下一行，另成一组放最后；条号不连续的相邻条之间加隐藏注释 `<!-- -->`，让 Markdown 预览不把列表重排编号（第 7 项统一改号后去掉）；图里没画「推翻前面的答案就回头」的回路，那条在 SKILL.md 的 Use Protocol 里，design-log 里没有对应的约定。**测试没过线**：每题都至少 4/5，但三题合计改后 14、改前 15，少 1 次（题 1 改后第 5 次，分支排在填表头之后）；改前基线 15/15，没有余量，测不出结构的好处；两处边缘判定见汇总，Master 若改判，结论会变 | `sample-test-summary.md`；核对脚本先拿 2 个应过、6 个应不过的样本自测（第一次暴露脚本只认每行一个节点，修好后重测全对） | Master 审；Master 先把结构单独给 PO 看，PO 说行再进第 2 项；测试没过线怎么处理，请 Master 与 PO 定（标准不能改；要不要重跑也由你们定，我不自己加跑） |
| 2026-11-10 | Master 第四轮：样板的结论与 PO 的新决定 | PO 接受样板的结构；三道题没过线（14 < 15），两处判定维持，失败原因在约定 3、4 的顺序，与结构无关，PO 让往下走；PO 新定：阶段之间由 PO 决定（是拍板，不是验收）、冲刺日志改成五章、How 写成类似方案、收官前 PO 强审、登记 PBI-51；做法改为 Developer 起草、Master 审、PO 强审，每处改动都要有依据 | 本审阅（plan 文件） | Developer 改日志，做设计这块，做完交 Master 审 |
| 2026-11-10 | Developer 抄入第四轮：产品日志登记 PBI-51；2.2 加 PO 的新决定、做法变化和 Master 对设计日志的七条提议，改「Master 定」那条规矩，验收改第 1、3 条并加第 8 条；3.1 重写第 2–8 项的产出与怎么算完、风险、Go-ahead；3.2 抄入 Master 的一行与样板的结论 | 验收第 3 条的「定了的点」顺带改成「有依据的改动」，与「没有依据的文字不动」一致（我多改的一处，请 Master 看）；本冲刺自己的日志不改成五章 | 产品日志 PBI-51；本日志 | 做设计这块：design-log、设计日志模板、`SKILL.md` 五阶段表，做完发消息给 Master 审 |
| 2026-11-10 | Developer 做完设计这块的修订稿（提交 `7e3e5b6`）：design-log、设计日志模板、design-kernel `SKILL.md` 的五阶段表；清单里设计这块各行写明改了什么和依据；PO 补的几点（插件文件不做标记、阶段之间是 PO 拍板、Review 和 Retro 不设章）和「两个入口」都按新写法落进去了 | design-log：新增 22–29，原编号未动；首句改祈使的 11 条（2、4、6、7、11、12、13、15、18、19、21），去「Author's practice」标签的 19 条；约定 5 补触发清单；约定 18 改成压缩日志归档、按产品日志约定 2 回流；图上标出 PO 拍板的点。模板：补 1.4 Findings、2.2 Point of View、3.1 Idea pool、4.1 Parts、5.1 Criteria，不加 Review 章，节号顺延。五阶段表各加一句重心。我自己拿主意的几处请 Master 看：29「小设计」对话里的表只有三个字，我照 sprint-log 约定 4 类推；25 的「发散够」取「池里有做法不同的点子」；28 的「检查」一栏取 PBI-48 的重心；约定 5 的触发清单取自本文件已有的「PO 决定」处；`SKILL.md` 的 Use Protocol 第 6 步没动（记在清单第二张表，待定） | `checklist.md` 设计这块各行与第二张表；脚本核对：没动的条逐字不变，改了的条都有依据，插件文件里没有标记 | 停点 1：Master 审设计这块；审过再做 scrum 这边（overview → product-log → sprint-log → 两份模板 → scrum-kernel `SKILL.md` 的分工一节）；模板的章节清单请 Master 先单独给 PO 看 |
| 2026-11-10 | Developer 照 Master 转述的 PO 决定改设计这块：设计日志模板去掉发现、POV、点子池三节，原型和测试两章不分小节，节号回到改前；约定 24（POV）整条去掉，新增条改号为 22–27；约定 24（原 25）改成给子代理下任务时要它先发散；约定 10、门表、五阶段表的定义一行不再提 POV；IDEO 写成必须（SKILL.md 序言段改成「IDEO is required in every stage」，五阶段表改成「IDEO 模式和重心｜书的步骤」，不列方法名，约定 7 指向 SKILL.md）；冲刺日志模板第 3 章用 plan、Test 一章不分小节 | 先要列方法名、后改为只写原则，以后一次为准；POV 去掉后，约定 10 补一句「HMW 对着地图写、参考第 1 章」；约定 12 的草图依据去掉「或」（IDEO 与书两样一起用）；模板各章注释不列方法名 | 清单设计这块各行；冲刺日志模板 | 做 scrum 这边：overview → product-log → sprint-log → `SKILL.md` 分工一节，再连带改动与改号；做完交 Master 审（停点 2） |
| 2026-11-10 | Developer 做完 scrum 这边和连带改动（提交 `46bdccf`、`a8095ef`、`c861574` 和本次）：overview（图重画：加「白纸」入口、冲刺五个阶段；新条 Product Owner decides between stages；Departures 表加「Why」列）、product-log（图；约定 1 加老项目；约定 2 加对照表；七步挪到 sprint-log）、sprint-log（五阶段图；七步并入 6；How 用 plan；新增 Test 与阶段结束 PO 拍板；特殊情况表删五行）、冲刺日志模板（五章）、scrum `SKILL.md` 的分工一段；四份约定按文件里的顺序重排条号，131 处引用逐处对到短名，0 错；`commands/developer.md` 一行；清单加「现号」栏，scrum 各行写了结论，连带改动、改号对照、核对写在清单末 | 每处改动的依据在清单「结论」栏。起草时做了几个判断，请 Master 看，见下面「停点 2 的不清楚的地方」。核对时发现并改了一处：product-log 17 起草时误改成指向 overview 5（那里只写了 documents/），改回指向 sprint-log 的 Review，Review 里写全「把整个 scrum/ 过一遍」；改号脚本只保证改前改后一致，不保证指针指对，这条记为 Retro 输入 | `checklist.md`（96 行：95 已改、1 已核；连带改动；改号对照；核对）；脚本核对：条号连续、引用 131 处 0 错、图的范围与小标题逐项对上、插件里没有标记；敏感信息扫描全过 | 停点 2：Master 审 scrum 这边与连带改动，并核停点 1 的三项必改；审过再做第 8 项（`plugin-validator`、Haiku 流程题，题目与过线标准先提交），然后交 PO 强审 |
| 2026-11-10 | Master 审停点 2：通过；停点 1 的三处必改核过都对，PO 后来定的几条都落对了；七处必改，Developer 照改（本次提交）：设计模板头部 Methods 一行与 ideo-kernel `SKILL.md` 第 10 行改成「设计里每个阶段都要用」；design-log 9 删五个方法名；Departures 表删「Closed logs」一行；sprint-log 4、5、6、16 的短名去掉「Stage N:」；sprint-log Throughout 加 25「Ask the PO」（只列指向，另加取消 Sprint 一项）；overview 1 写规矩、product-log 1 只写做法 | 其余答复（d–m）记在上面「停点 2 的不清楚的地方」；PBI-40 ⑧ 这次不做，收官时拆成新 PBI，先记在清单第二张表。第 8 项的测法 Master 定（PO 授权）：无头 `claude -p --plugin-dir`，Haiku，开读文件的工具，关 Bash 和 PowerShell，系统临时目录里的空项目，约五题，每题 3 次、至少 2 次过，不比基线；先冒烟；题目与过线标准先提交，发消息给 Master 看过再跑；原始输出放仓库外 | `checklist.md`（现 97 行；第二张表加三行；核对加第二轮）；脚本核对：条号连续、引用 142 处都解析到存在的条、短名变化只有预期的五处、结构检查全过 | 写第 8 项的题目与过线标准（进 2.2），提交，发消息给 Master；Master 看过再冒烟、再跑；跑完连同 `plugin-validator` 的结果交 Master |
| 2026-11-10 | Developer 跑第 8 项的流程测试：冒烟后 5 题 × 3 次共 15 次，Haiku（`claude-haiku-5-5`），被测插件取提交 `87bd0db`；判定标准先提交（`1b07623`、`a87bd1c`，含 Master 改的三处判定说法），跑后没改；15 次都在第一次调用成功；判定汇总在 `flow-test-summary.md` | 结果：题 1、4、5 各 3/3，过线；**题 2 为 1/3，题 3 为 0/3，没过线**（线是每题 ≥2/3）。题 2 的内容三次都对，没过是因为两次只加载了技能、没读约定文件；题 3 三次都没加载 scrum-kernel，「白纸项目先从设计开始」一次也没碰到，内容也没说出来。照规矩不改判、不改标准、不加跑；怎么处理（给 design-kernel 的 SKILL.md 加一句、改技能描述，或不改）交 Master 和 PO 定，改插件就要整轮重跑 | `flow-test-summary.md`；原始输出在仓库外 | 交 Master：判定汇总和 `plugin-validator` 的结果；Master 派全新子代理对整份改动挑错，然后交 PO 强审 |
| 2026-11-10 | Master 派全新子代理对 `2aad30f..87bd0db` 的插件改动做对抗审查，清单在 plan 文件 | 7 处必改（构思的发散必含 IDEO 方法、删 design-log 9、sprint-log 4 指向错误、阶段拍板与 scrum/ 保鲜与白纸判断各只留一处、冲刺模板第 1 章补决定）、6 处小改，overview 4 一处不改（那是做法的说明，不是标签残留）；题 2、题 3 没过线，Master 选 (a)：design-kernel 的 `SKILL.md` 加一句指向 product-log 2，两份 `SKILL.md` 都写明「回答怎么做的问题之前也要先读对应的约定」，不改技能描述；改完把流程测试原样重跑一轮，两轮结果都留 | Master 的清单（plan 文件，第 1–17 条） | Developer 改，重跑测试，交 Master，再交 PO 强审 |
| 2026-11-10 | Developer 照清单改插件：内容改动提交 `94a6758`，重排条号提交 `c35c4df`（design-log 26 条、overview 18 条，引用 140 处对到短名，0 错）；清单补上这一轮的结论、「现号」栏重算、改号对照改成旧→现一张；`plugin-validator` 第一次（跑在 `87bd0db` 上）回来：PASS，无必改，建议 5 条 | 每处改动的依据在清单「结论」栏。我定的几处：overview 的工作材料那句单列一条（Master 让我在单列和挪到段首里选，因为一条只讲一件事）；plugin-validator 的建议采纳 2 条（sprint-log 开头写明 `../` 路径从技能文件夹算起；product-log 对照表里 2.2 改称 Map，与模板标题一致），其余不动：product-log 开头「引文标在出处」是无害的残留，版本号和 `plugin.json` 的可选字段留到收官。它还查出仓库外和 CLAUDE.md 里按旧号引的地方，已记进清单第二张表 | `checklist.md`（98 行：97 已改、1 已核；第二张表 13 行）；脚本核对：条号连续、引用 0 错、图的范围与 Throughout 对上 | 第二轮流程测试和第二次 `plugin-validator` |
| 2026-11-10 | 流程测试第二轮：原样重跑在 `c35c4df` 上（脚本先核对了插件文件与提交一致、2.2「流程测试」那一块与第一轮提交逐字相同），15 次都在第一次调用成功 | 题 1、4、5 各 3/3；题 2 为 2/3，过线（第一轮 1/3）；**题 3 仍是 0/3，不过线**：记成已知缺口，留给 PO 强审时看，PO 要做就登记成新 PBI。两轮六次都没加载 scrum-kernel；design-kernel 的 `SKILL.md` 新加的那一句让 3-1 说出「设计的结论会成为项目的第一份产品日志」，但它没读约定，也没讲为什么现在写不出产品和 Product Goal；3-3 读了 design-log，没有顺着指向去读 product-log 2。第一轮的结果不改，两轮并列写在汇总里 | `flow-test-summary.md` | 交 Master：汇总、`plugin-validator` 第二次的结果；Master 再交 PO 强审 |
| 2026-11-10 | Master 转述 PO 看过设计约定后又定的两点（plan 文件 A、B 两节，必改第 2 条同时改了）；Developer 照改，提交 `f495298` | A. 设计不做 Review 和 Retro（设计是整个 Scrum 工作里的一个子集，不单独收尾）：design-log 原 19 删，原 18 改名 When the design ends，只留结论流回产品日志和提出它的冲刺、白纸时拆 PBI、删原型和设计文件夹里除日志以外的文件、分支合并后删除；设计日志由它服务的冲刺在 Review 时归档，教训进那个冲刺的 Retro；图上的 Closing 改 Ending；设计模板头部、两处 close 的说法、design-kernel 的 `SKILL.md`、overview 的大图与第 5 条、README 里设计日志约定一行跟着改。B. 贯穿全程加一条 IDEO in every stage（原 9 挪来改写，不列方法名，指向 `SKILL.md`），放在 Throughout 开头，条号仍是 26 条、没有动。CLAUDE.md「设计收官」一段和产品日志 PBI-40 ① 与 A 冲突，我没动，记进清单第二张表，收官时由 Master 和 PO 处理 | 清单（98 行；第二张表 14 行）；脚本核对：条号连续、引用 139 处都解析到存在的条、短名变化只有预期的两处、结构检查全过 | 第三轮流程测试和第三次 `plugin-validator` |
| 2026-11-10 | 流程测试第三轮：原样重跑在 `f495298` 上（脚本先核对插件文件与提交一致、2.2「流程测试」那一块与第一轮提交逐字相同），15 次都在第一次调用成功；`plugin-validator` 第二次（跑在 `c35c4df`）：PASS，无必改，5 条小建议我都没采纳（都不影响读懂，多数是本冲刺之前就有的：design-kernel 的 `SKILL.md` 与设计模板里的裸条号默认指 design-log；`overview.md` 路径的写法；设计摘录文件头的 ATTRIBUTION.md 在插件外；两处引用与句子贴合得宽松）；第三次（跑在 `f495298`，另用官方的 `claude plugin validate` 加 `--strict` 核了插件、skills、commands 和 marketplace 清单，也过）：PASS，无必改；建议 5 条，其中两条与上面的问题 n、o 是同一件事——sprint-log 17 没提设计日志的归档、归档后叫什么没有规定，「它服务的冲刺」在白纸设计和服务多个冲刺时没有对象——不改，等 Master 定；另三条是老问题（设计摘录文件头的 ATTRIBUTION.md 在插件外；三处引用与条名贴合得宽松；可选的元数据警告），不采纳。它还查出 CLAUDE.md 第 15、55、57 行仍写着旧的设计收官，已记进清单第二张表 | 第三轮：题 1、4、5 各 3/3；题 2 为 2/3，过线；**题 3 仍是 0/3**，三轮共 9 次一次没过，记成已知缺口，留给 PO 强审时看，PO 要做就登记成新 PBI。9 次里 4 次没加载任何技能，5 次加载了 design-kernel，scrum-kernel 一次也没加载，product-log 一次也没读。题 5 的两次回答还主动指出这台机器全局记忆索引里的「sprint-log 约定 14」已过时，正是清单第二张表记着的外部引用。三轮并列写在汇总里 | `flow-test-summary.md` | 交 Master：汇总和两次 `plugin-validator` 的结果；Master 再交 PO 强审 |
| 2026-11-10 | Master 答复 n、o，Developer 照改（提交 `63ee408`） | 一、sprint-log 17 加一句：Review 时把已经结束、还在自己文件夹里的设计的日志，照冲刺日志的做法压缩，改名 `design-<后缀>.md`，移进 `scrum/documents/`；归档动作只写在这里，design-log 18、overview 5、设计模板头部改成指向它（我上次把「只在设计这边写明」理解成不碰 sprint-log 17，Master 说是他没说清楚，意思是不另立一条规矩）。二、「它服务的冲刺」统一改成「设计结束后的第一个冲刺 Review」，白纸设计和服务多个冲刺的设计都适用。这一轮不重跑流程测试：接下来是 PO 强审，PO 的意见改完后，收官前整轮再跑最后一次；题 3（白纸项目）的已知缺口交 PO 定 | 清单更新；脚本核对：条号没动、引用都解析到存在的条、结构检查全过，插件里没有「it served」的残留 | 交 PO 强审（四份约定、三份模板）；PO 的意见改完后，收官前整轮再跑一次流程测试 |
| 2026-11-10 | PO 强审第一批意见（Master 转述），Developer 照改（提交 `c1ee678`，重排条号 `ec5d30a`） | 一、删 overview 的「When a revision applies」：这条讲维护本插件约定的节奏，是这个项目自己的事，CLAUDE.md「Sprint 节律」里已有同样的话；PO 说的「15」是改号前的号，Master 按内容判断是这一条，向 PO 确认过；删后 overview 17 条，5 处引用对到短名。二、product-log 2 对照表末行的设计一栏改成 the target（指向 pick-a-target.md），对应 PBI；连带 design-log 18（白纸设计结束时选 target 再拆成 PBI）、design-log 8（设计进行中不设选靶，白纸设计在结束时选 target），以及 design-kernel `SKILL.md` Define 行里同样的「No target step」（我顺手对齐，Master 没列）。三、去掉约定的版本标记：四份约定标题和开头一行里的 v1，README 里四处的约定 v1；来源的版本不动 | 改号后 143 处引用逐处对到短名，0 错；结构检查全过；清单相应行写了结论，第二张表加三行 | 本轮不重跑流程测试；等 PO 下一批意见 |
| 2026-11-10 | PO 强审结束（「别的就没什么问题了」，其余交 Master 定）；第一阶段：sprint-log 11 改 Outline before full text；设计结束时在第 5 章末尾记一两句教训；最后一轮（第四轮）流程测试 | 提交 `aa473c6`。sprint-log 11：写新的长期文档或新模板之前先给大纲（各级标题，每部分一句话），同意了再写全文，新模板的大纲就是章节清单；12 不动。设计结束时的教训：设计不单做 Retro，教训要等冲刺的 Retro 才整理，中间隔得久会忘，所以在第 5 章末尾、PO 的决定旁写一两句，不另开一节。第四轮（脚本核对插件文件与提交一致、判定标准那一块与第一轮提交逐字相同，15 次都一次成功）：题 1、4、5 各 3/3，题 2 为 2/3 过线，题 3 为 0/3。这一轮题 3 三次都加载了 design-kernel，3-2、3-3 的内容三条必答都答对了，只差判定标准里的「读到约定文件」（三次都没读），所以字面上仍是 0/3，记为已知缺口（PBI-52）；标准是不是该只看内容，不由我定，没改标准、没改判。四轮并列写在汇总里。子智能体：Master 定这一轮不再派 plugin-validator（只改了文字，结构没变，前两次都是 PASS），收官改完版本号后跑一次官方 `claude plugin validate --strict`，报问题或结构有变才派；第四次是 Master 改口前派出的，让它跑完，结果到了再记。PO 嫌子智能体费 token，要求用 Haiku：已写进用户级 CLAUDE.md，今后派子代理一律显式写 `model: haiku`；已完成的三个 validator 没写 model，各用了 22 到 27 万 token，是 Retro 的输入 | `flow-test-summary.md`（四轮对比）；清单第七轮 | 交 Master；等 Master 说「收官」再做第二阶段 |
| 2026-11-10 | 流程测试题 3（白纸项目）的已知缺口：Master 定，PO 授权，登记成新 PBI-52（产品日志 3.1） | 三轮 9 次 0 次过线，记成已知缺口；改法实现前定，多半要改 scrum-kernel 或 design-kernel 的描述，改描述要重跑触发测试、结果不能比改前差；本冲刺不做（1.2 DoD：技能描述这次不动） | 产品日志 3.1 的 PBI-52 | 收官时产品日志保鲜带上 |

**样板的结论（Master 第四轮，2026-11-10）**
- PO 接受样板的结构（PO：「之前提的那几个点确实都改了，没问题，很好。」）。
- 三道题没过线（改后 14 次，改前 15 次）。Master 看过两份边缘回答，维持两处判定，用同一个标准：按开设计的动作看顺序。改后那次确实是先填表头、后定分支；改前那次第一步是去读文件里指向的另一条约定，这不算开设计的动作。
- 失败原因与结构无关：出在约定 3（填表头，表头里有分支一栏）排在约定 4（定分支）前面，改前改后都一样。PO 让继续往下走，不重跑，不改标准。
- 这个发现进 design-log 的修订：定分支要排在填表头之前，或者把定分支并进「开设计」那一条。
- Retro 输入：改前版本可能满分时，「不少于改前」这条过线要留余量或加次数，而且要在跑之前定。

**Developer 复述验收（2026-11-10）**

1. 清单每行都有 PO 的结论（改 / 不改 / 挪到别的 PBI），全部打勾（状态「已核」），Goal 才算达成。
2. 定了要改的都改到位；Master 拿结论逐条对 diff。
3. diff 里除了定了的点，只有登记过的连带改动；PO 没提的字不动。
4. 改过的规矩，全仓里的旧说法 0 残留；「convention N」引用用脚本核，0 错。
5. 无死链，从入口两跳可达；`plugin-validator` 通过。
6. Goal 末句：收官前，一个全新 Haiku 子代理只拿改后的插件，答几道流程题；题目与过线标准先提交、后跑；测法 PO 收官前定。
7. Codex：全部改完后一次同步，`check_codex.py` 0 不一致。

**清单怎么记**：PO 的意见经 Master 转来（plan 文件），我抄进清单的「PO 的意见」「结论」，并改状态：待看 → 已定（结论已抄入）→ 已改（我改完）→ 已核（Master 核过 diff）。

**不清楚的地方（Master 已答，2026-11-10）**
- a. 「登记的连带改动」登记在哪：我打算记在本 3.2 里（每项写：哪条规矩、哪些文件），收官时据此核 diff；想放进清单另开一张表的话，请说。**答**：登记在 `checklist.md` 的第二张表，栏目「规矩｜涉及的文件｜状态」，收官时和第一张表一样逐行核对；3.2 只指向它。
- b. 「全仓」的范围：我按 `plugins/ideo-scrum/`、README、CLAUDE.md、`scrum/` 现行文件算；`scrum/documents/` 的归档是历史，不改（与 Sprint 12 一致）；`codex/` 是生成物，同步时随之更新。是否这样。**答**：同意；仓库外两条全局记忆（plan-view-review、compact-instead-of-handoff）引用「sprint-log 约定 13、14」，不归 Developer 改，收官 Retro 时由 Master 经 PO 同意处理。
- c. 验收 6 与样板那三道题：题目与过线标准我这轮不写，等 PO 定测法（sprint-log 约定 15：先提交、后跑）。**答**：样板的三道题现在起草，写进 2.2 的「测试」，每题写清题目、给哪份文件、过线标准，不带引导词；收官用的流程题（验收 6）收官前再定。

**停点 2 的不清楚的地方（Developer 提给 Master，Master 已答，2026-11-10；编号用改号前的号，对照表在 `checklist.md` 末）**
- d. PBI-40 ②（「拿不准就问 PO」的触发清单）：设计这边有一份（design-log 5，现 21）；Scrum 这边没另列——overview 9 只去了标签，PO 要决定的事分写在 overview 7 的 PO 一行、新条（阶段结束的决定）和 sprint-log 24。要不要在 overview 9 或 sprint-log 24 汇成一份？**答**：在 sprint-log 的 Throughout 加一条「Ask the PO」，和 design-log 21 对称，只列指向（已做，现 25）。
- e. PBI-40 ⑧（Developer 在别的工具里，如 Codex）：本冲刺没动（PO 定这次只做 Claude 版）。留在 PBI-40 的备注里，还是挪到新 PBI？**答**：这次不做，收官时从 PBI-40 拆成一条新 PBI；先记在清单第二张表。
- f. overview 1 与 product-log 1 重叠：「Every project … starts from one product log」和「Start every project … by writing one product log from the template」。我两条都留了（前者是总规矩，后者带怎么写和老项目）；合并的话删 product-log 1 的前半句。**答**：只留一处：overview 1 写规矩，product-log 1 只写做法并指向 overview 1（已做）。
- g. sprint-log 4（小 Sprint）里「PO 仍在每个阶段结束时拍板」，是照 design-log 27（Master 提议 4）类推的，冲刺这边没有直接依据；留不留？**答**：留着，依据改写成 overview 11（每个冲刺都适用），不是从设计类推（清单已改）。
- h. 短名里的「Stage N」：sprint-log 的 Why、选条目、Refinement、Test 带阶段号（Stage 1、2、2、5），How 和 Increment 两组不带，「Stage 2」还出现了两次。要不要改成都不带（小标题已经是阶段名）？**答**：去掉前缀，换成说这一步做什么的短名（已做：Set the Sprint Goal、Select the items、Refine in seven steps、Record the tests）。
- i. Departures 表里「Closed logs are kept in scrum/documents/」一行，官方没有对应说法，两栏都是「—」；它不是「与官方不同」，留在表里还是挪出去？**答**：删掉那一行（已做）。
- j. overview 的图画整个流程，节点不标条号（另三份的图标了）；要标吗？**答**：不标，它跨好几份文件，条号由各文件自己的图标。
- k. sprint-log 23（特殊情况）我删去五行，因为各有别的条覆盖（见清单该行）；同意删吗？**答**：同意。
- l. `commands/developer.md` 一行改了（阶段结束请 PO「拍板并决定进不进下一段」，原为「看一眼结果」），这是连带改动里唯一动命令的地方，请核。**答**：对。
- m. 仓库外和 CLAUDE.md 的引用（全局记忆的「sprint-log 约定 13、14」现为 12 和 22；CLAUDE.md 的「约定 16」现为 14；「冲刺收官与归档」里的「补上 Review 章」与新结构冲突）我没动，收官时由你们处理，清单第二张表有明细。**答**：同意；CLAUDE.md 收官时在收官提交里改；仓库外的全局记忆由 Master 收官时经 PO 同意处理。

**Retro 输入（续）**：改号脚本只保证改前改后一致，不保证指针指对；把规矩挪到别处之后，要逐处读指针所指的条是不是真有那句话（本冲刺核出 product-log 17 一处）。

**对抗审查之后的不清楚的地方（Developer 提给 Master，2026-11-10）**
- n. 设计日志由「它服务的冲刺」在 Review 时归档（design-log 18）：白纸设计没有提出它的冲刺，由哪一个冲刺归档？我写成「the Sprint it served」，没有往下规定；要不要写明（例如：接着用它的结论的第一个冲刺）？**答**：统一改成「设计结束后的第一个冲刺 Review」，白纸设计和服务多个冲刺的设计都适用（已做）。
- o. 设计模板头部原来写「压缩、归档」，现在改成「Ends … the Review of the Sprint it served archives this file」，归档的责任放在冲刺那边；sprint-log 17 我没动（它本来就要把整个 `scrum/` 过一遍），overview 5 的归档清单写成了「冲刺日志，和这个冲刺服务过的设计的日志」。要不要在 sprint-log 17 里也点一句设计日志？**答**：要；归档动作只写在 sprint-log 17，design-log 18、overview 5、设计模板头部改成指向它（已做）。

## 4. Review

<!-- Written at close by the Product Owner, the Scrum Master, and the Developer: the Increment; the Definition of Done and the acceptance criteria, item by item; what the review found; the stakeholders' view; changes to the product log and the Product Goal (sprint-log.md, convention 18). -->
