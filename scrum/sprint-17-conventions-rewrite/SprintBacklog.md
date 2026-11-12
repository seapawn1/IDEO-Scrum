# Sprint Backlog — Sprint 17 (conventions-rewrite)

> Started: 2026-11-12 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `sprint-17-conventions-rewrite`（Developer 的原生 worktree） | Product Owner: SeaPawn | Scrum Master: IDEO # [master]-[main]-[start sprint] | Developer: IDEO # [developer]-[sprint-17]-[执行冲刺]
> How to write this log: `sprint-log.md` in the scrum-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled later; add none — remarks go in chapter 4, Increment notes (`overview.md`, convention 16).

**委托**（sprint-log 第 8 条）：PO 2026-11-12 把 Sprint 16、17 全权交给 Master：审 How、审新结构、审全文，以及各阶段结束时的决定，都由 Master 做；只在三处停下等 PO——① 两个冲刺的 How 都审过后，PO 一起放行（放行范围可以到推送和更新本机插件，PO 已同意）；② PO 整份读本冲刺的约定审阅稿，排在最后一轮流程测试之前；③ 最后 PO 亲手试一次，之后 Master 发版 v6.0.0、推送、更新本机插件。改 Sprint Goal 或 Product Goal、取消冲刺，仍由 PO 定。平时只在卡住时报告 PO。

**两个冲刺并行**：Sprint 16（`sprint-16-kernel-structure`）改结构和加载，本冲刺改约定内容，各有一个 Developer 会话。Sprint 16 先合入 main；本冲刺先在本文件夹里按新布局写全文审阅稿、不碰 `plugins/`，等 Sprint 16 合入后从新的 main 搬进插件，再跑最后一轮流程测试。两个冲刺各自收官、打 tag；v6.0.0 在本冲刺收官时发。Master 与 Developer 用跨会话消息联系，长的审阅写在 plan 文件里、消息里只给路径；派子代理一律显式写 `model: haiku`。

## 1. Why

### 1.1 Sprint Goal

**约定改顺**：攒下的反馈都改进约定；设计冲刺和五阶段法分清；熟手照着就能走。

（Master 照 PO 的写法代拟；PO 2026-11-12 看过拆分表里的这句草稿，说没问题。开冲刺前核对了 Product Goal「优化现有插件」：在目标之内——只改约定，不加新功能。）

### 1.2 Definition of Done

- 内容忠实：PO 的原话、已批准的命令 Identity 和原书摘录逐字不变；约定是作者的写法，可以大改，不在原文上打补丁（PO 2026-11-12）。
- 可导航：从每个技能的 SKILL.md 入口 ≤2 跳到达它的任意文件。
- 无死链：所有内部链接、路径和「convention N」都解析得到，并且指对。

Master 2026-11-12（PO 委托）：Sprint Goal 定。

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-54 | 产品日志与冲刺约定修订 | 作为熟手，我想要产品日志和冲刺的约定用过一轮后再集中修一次，补上用起来卡手的地方 | 插件：scrum-kernel 的 `conventions/` | S |
| PBI-58 | 设计约定修订——PO 用设计时攒下的点 | 作为熟手，我想要设计约定补上用过一轮后攒下的点，以便下一个设计照着走更顺 | 插件：design-kernel 的 `conventions/` | M |
| PBI-56 | 设计冲刺与 IDEO 五阶段法分清（＋IDEO 日志与模板） | 作为熟手，我想要插件分清设计冲刺和 IDEO 五阶段法：小问题就地用五阶段法，大问题才开设计冲刺，由 PO 指定，以便不为小问题兴师动众 | 插件：ideo-kernel（新 `conventions/`）、design-kernel（design-log 第 1、26 条） | M |
| PBI-53 | 约定写明 Developer 在别的工具里时怎么协作 | 作为熟手，我想要约定写明 Developer 在别的工具（如 Codex）里干活时，它和 Master 怎么协作，以便不用口述 Sprint 13 的做法，换工具也能照着走 | Map ③～⑧ | S |
| PBI-46 | Codex 版后续小修 | 作为熟手，我想要 Codex 包的同步和说明再顺一点，以便以后每次发版重跑同步都不用多想，陌生人在 Codex 里也能起步 | Map ①（装插件，开会话） | S |
| PBI-52 | 白纸入口——新想法、还没有产品日志时带到设计 | 作为陌生人，我想要说出「我有个想法、还没有产品日志」时，插件就把我带到先开设计、由设计结论去填产品日志这条路上，以便不会一上来就硬写产品日志或直接出方案 | Map ①（装插件，开会话） | S～M |

### 2.2 Refinement

**选入**（照抄产品日志 3.1，对照 Sprint Goal 查过够不够——PO 2026-11-12，PBI-54 ④）：54、58 是攒下的反馈；56 是目标第二句；53 和 46 ③ 让换了工具也照着走；46 只带 ③，①④ 在 Sprint 16，②⑤⑥ 留在产品日志。产品日志与冲刺的约定在 Sprint 16 之后分在两个技能里（product-log 留在 scrum-kernel，sprint-log 挪到 sprint-kernel），54 两份都改。

**定案**

- PBI-54（PO 2026-11-12 收进）：① 冲刺日志模板头部加一行 Now，断线后一眼看到最后一个 PO 的决定；② Checkpoints 写明什么算卡住；③ Review 写明怎么判过时；④ sprint-log 第 5 条写明：照抄进 2.1 时对照 Sprint Goal 查够不够，缺就增、多就减。「Why 不写 PBI」不用改，也不另加一句：插件里本来就没有 Why 写 PBI 的说法（PO）。
- PBI-58（PO 2026-11-12 收进）：①–⑧ 照产品日志的备注；「测试前 PO 先看原型」不进插件，原型和测试之间不加 PO 关卡；Designer 和 Master 兼不兼由 PO 定（PO）。
- PBI-56（PO 2026-11-12）：用设计冲刺还是 IDEO 五阶段法由 PO 指定；PO 没指定时，要先做原型、拿角色卡测过才敢动手的，开设计冲刺，其余就地用五阶段法，按方法记录；设计冲刺重，五阶段法是基础、规矩少，所以 ideo-kernel 的约定写得轻；从聊天里开的设计，聊天算作共情材料。写进 ideo-kernel 新的 `conventions/`（一份简短约定）；design-log 第 1、26 条改成指向它。
- PBI-53：写明 Developer 在别的工具（如 Codex）里时怎么和 Master 协作（Sprint 13 的做法见产品日志的备注），连同 `/fork` 出的独立会话用跨会话消息直接通讯（Sprint 14）。
- PBI-46 ③：核对「派全新子代理」在 Codex 里怎么做，结果写进约定或 Codex 包的说法。
- 约定可以大改（PO 2026-11-12）：重写，不在原文上打补丁；PO 的原话、已批准的命令 Identity、原书摘录逐字不动。
- 来源：PO 的原话在全局记忆 Feedback（`S:\SeaPawn-Memory\memory\FeedBack\MEMORY.md` 里标了 PBI-54、56、58 的行，和各自的文件）；Sprint 14 Review 的熟手意见在 `scrum/documents/sprint-14-conventions-tuning.md`。
- 先写稿、后搬（Master 定，PO 同意的拆分）：先在本文件夹里按新布局写全文审阅稿，不碰 `plugins/`；文件的新路径照 Sprint 16 How 里的文件清单。Sprint 16 合入 main 后，从新的 main 出发搬进插件；搬之前对照 Sprint 16 对这几份文件的改动（应当只有路径），并进定稿。
- 改规矩先找它的其他说法（CLAUDE.md）：模板、命令、四个 SKILL.md、overview、CLAUDE.md、README 里同一条规矩的说法，列成连带改动，一起写进审阅稿。
- 审阅顺序（CLAUDE.md「大改约定的审阅顺序」）：每份新写或重写的约定，先给 Master 看大纲（图和每条一行，sprint-log 第 11 条），同意了再写全文，全文附找到的问题和每处的建议（第 12 条）→ Master 审 → 对抗审查（全新子代理，Haiku）→ 停点 ②：PO 整份读——结构清单单独摆在前面，再给全文；PO 读完说行，不逐行勾 → 搬进插件 → 最后一轮流程测试 → 停点 ③：PO 亲手试 → 收官、发 v6.0.0。
- 改号：内容改动与改号分开提交；每处「convention N」用脚本对到短名，再逐处读所指的条是不是真有那句话。
- 改了技能或命令的描述，就照 Sprint 16 的触发测试重跑：基线是 Sprint 16 合入后的 main，同日同环境，过线同 Sprint 16。
- 发版（PO 同意）：v6.0.0 在本冲刺收官时发——`plugin.json` 的版本号、README 两处、Codex 包同步；推送 main、tag 和 SeaPawn-Memory；更新本机 Claude Code 的插件。

**PBI-52 并入**（Master 2026-11-12，PO 委托；范围调整，Sprint Goal 不变）：Sprint 16 改了描述之后，题 3 两条路径的行为栏都到了 3/3，触发问题解决了；剩下的缺口在内容上——从 `/ideo-scrum:scrum-master` 进的那条路径，3 次里有 2 次没说「设计的结论会流回产品日志」。这是约定写法的事，归本冲刺；草稿先不动，看最后一轮流程测试的结果，要改措辞再和 PO 的意见同批改。

**IDEO 日志与模板并入 PBI-56**（PO 2026-11-12 停点 ②，Master 转；范围调整，Sprint Goal 不变）。PO 原话：

> OK，相当好，但是差了一件事情，我不知道有没有补充完毕，什么呢，就是说ideo-kernel，没有出现模板，我希望可以出一个文件IdeoBacklog.md，虽然我觉得基本不会用到，然后里面就是标准得五节，没有什么拆分（这时候一般是不上design-kernel得，所以一般不会读哪个kernel，所以要注意区分，是ideo方法论还是design sprint），然后conventions得log，你看着稍微写一写就好，我估计很少，主要是区分一下就可以，对然后就可以了，也就是说差一个文件夹conventios，里面得log和模板。你看sprint17好不好补充，这样最好，，思考一下这个问题。应该如何更好的处理

**架构与关系**（PO 2026-11-13，Master 定）。PO 原话：

> 是的，冲刺16没问题，其余你都自己决定住就可以了。是的，但是这个log也需要一个架构也要补充上去。其余的我觉得没啥问题了，但是还是那句话，要说明ideo五阶段法和设计冲刺之间得关系，不能乱，这个东西很容易乱得。其余得我觉得都没啥问题。

定案：
- ideo-kernel 的 `conventions/` 照另三个内核放两份：`ideo-log.md`（分界第 1 条、关系第 2 条、什么时候开 IDEO 日志第 3 条、放哪与结束第 4 条）和 `ideo-backlog-template.md`（做出 `IdeoBacklog.md`，五章、不分节）。
- 8 处指向改成 `ideo-log.md`；改名同一提交全仓 grep 旧名到零。
- overview 的图加一个分界节点，两支：设计冲刺（design-log）与五模式（就地用或开 IDEO 日志）；`ideo-log.md` 的图画清五模式的三种用法；两边的结论都流回。
- 关系只写 `ideo-log.md` 第 2 条；design-kernel `SKILL.md` 的「five IDEO stages」与 design-log 第 20 条的「Run the design sprint as the IDEO five-stage method」改掉。
- overview 第 4、5、7 条与 sprint-log 第 17 条带上 IDEO 日志；README 加 ideo-kernel `conventions/` 一行。
- 不改任何 description；Codex 同步；引用核对、check_codex、validate 照跑。

**停点 ③ 取消**（PO 2026-11-13，Master 转）。PO 原话：

> OK，最后全部完成即可，我就不进行审阅了，全部完成，推送更新先不做，到时候我给辅助对话去做。你只需要监督全部完成，做完review retro，然后你直接相关得活全部完成即可。最后我审阅后没问题，我会推送更新，不会找你，会直接归档掉你，如果有问题，我再会找你。ok，权限全部交给你

定案：停点 ③ 取消；收官（Review、Retro）与 v6.0.0 的本地发版（版本号、README、Codex 包、tag）由 Master 做；main、tag、记忆库都不推送；推送和更新本机插件交 PO 的辅助会话。

**验收**

1. 收进的每一点都写进了约定：一张对照表，PBI-54 ①–④、PBI-58 ①–⑧、PBI-56、PBI-53、PBI-46 ③，每点对到约定文件和条。
2. 一条规矩只写一处：同一条规矩的其他说法都改了或删了；对抗审查的必改项清零。
3. 引用：每处「convention N」和路径都指得到，并且指对（脚本核对，再逐处读）。
4. 停点 ②：PO 整份读审阅稿，说行。
5. 最后一轮流程测试过线（见下）。
6. `claude plugin validate --strict plugins/ideo-scrum` 通过；结构或 frontmatter 改了，再派 `plugin-dev:plugin-validator`（`model: haiku`）；Codex 同步与核对通过。
7. 停点 ③：PO 2026-11-13 取消，改为收官后 PO 自己看。推送和更新本机插件交 PO 的辅助会话。
8. PBI-52：最后一轮流程测试里，题 3 两条路径各至少 2/3 过。
9. IDEO 日志：ideo-kernel 的 `conventions/` 有 `ideo-log.md` 和模板，分界并入第 1 条；最后一轮流程测试里的五模式题过线。

**测试**（跑之前写定，跑后不改；Master 定，PO 委托）

- 判定标准和题目先写、Master 审过、单独提交，再跑；跑后不改标准、不改判；脚本判错的逐条人工看，改判写明理由。
- 测法同 Sprint 16（无头、Haiku、只开 Read、Grep、Glob、Skill、连 PowerShell 一起禁、空项目、每次一个全新会话、先冒烟），跑在搬进插件后的版本上。
- 题目：Sprint 14 流程测试的题 1–5（见 `git show a87bd1c:scrum/sprint-14-conventions-tuning/SprintBacklog.md` 的 2.2；题 3 是白纸，PBI-52），加上覆盖本冲刺改动的题：断线后接手一个冲刺（54 ①）、什么时候算卡住（54 ②）、选条目写 2.1（54 ④）、一个小问题该用五阶段法还是开设计冲刺（56）、设计的地图和设计目标怎么写（58 ①②）、Developer 在 Codex 里时怎么协作（53）。用自然的说法，不带引导词。
- 路径：所有题走直接说；题 2、题 3 另外再走一遍角色命令（`/ideo-scrum:scrum-master`）。每条路径 3 次，各自都要过线（每题至少 2/3）。
- 一次回答算过：读到该读的约定、必答项全中、没有「不能」项（Sprint 14 的判定，不放宽）。
- 汇总分两栏：行为（加载了哪些技能、读没读该读的约定）、内容（必答项中没中）。
- 原始输出放 `S:\IDEO-Scrum-Archives\sprint-17-conventions-rewrite\`，仓库里只留汇总；提交前按提供方地址、凭据值、令牌形态扫一遍。

Master 2026-11-12（PO 委托）：精化到此（Developer 复述，没有疑问）。

## 3. How

<!-- The Developer writes this chapter as a plan for making the selected items, short and not in detail (sprint-log.md, convention 7): the work items in order, each with its output and how to tell it is done; the key choices and why; the risks and open points. The last line is the go-ahead (sprint-log.md, convention 8). -->

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | 改动点清单与新路径表 | 本文件夹 `checklist.md`：① 现行文件 → 新布局路径（照 Sprint 16 的 How 文件清单；它未提交时照它 2.2 的布局四条，标「待核」）；② 改动点表：54 ①–④、58 ①–⑧、56、53、46 ③ 每点对到文件与条；③ 连带改动的扫描范围（三份模板、四个命令、四个 `SKILL.md`、overview、CLAUDE.md、README、`scripts/codex_readme.md`） | 每点都有落点；路径表与 Sprint 16 的清单核对过或标明待核；随大纲交 Master |
| 2 | 大纲 | 每份要改的文件：一张 `flowchart TD`（节点标条号）+ 一条一行；两份模板另给章节清单；ideo-kernel 的新约定给短清单；overview、product-log 只列要动的那条 | Master 同意大纲（不同意的改到同意） |
| 3 | 设计侧全文审阅稿 | `drafts/` 里 design-log（58 ①–⑧、56 的第 1、26 条改指向）、设计日志模板（58 ①② 的注释）、ideo-kernel 的新约定（56）；ideo-kernel 的 `SKILL.md` 加一行指向新约定（可导航：从入口 ≤2 跳）；附找到的问题和每处的建议 | 全文逐字可读；问题清单齐；自查「convention N」与路径 0 缺 |
| 4 | 冲刺侧全文审阅稿 | `drafts/` 里 sprint-log（54 ②③④、53、46 ③）、冲刺日志模板（54 ①）、product-log 第 12 条收成指向、overview 第 14 条的指向（若大纲定了），附问题与建议 | 同 3 |
| 5 | 连带改动与引用核对 | 同一条规矩在模板、命令、四个 `SKILL.md`、overview、CLAUDE.md、README、`codex_readme.md` 里的其他说法改齐；每处「convention N」对到短名并逐处读所指的条；路径逐条查 | 旧说法 0 残留；引用 0 错（脚本先拿已知结果自测） |
| 6 | Master 审与对抗审查 | Master 的必改改完；全新子代理（`model: haiku`，只核对做得对不对）对抗审查，必改清零 | 必改 0；Master 说交 PO |
| 7 | 停点 ②：PO 整份读审阅稿 | 结构清单在前、全文在后，交 PO | PO 说行 |
| 8 | 搬运（Sprint 16 合入 main 之后） | 从新的 main 更新冲刺分支；`drafts/` 按新路径搬进 `plugins/ideo-scrum/`；对照 Sprint 16 对这几份文件的改动（应当只有路径）并进定稿；跑 `sync_codex.py`、`check_codex.py` | 插件里是新文本；Codex 0 不一致；diff 只剩预期 |
| 9 | 题目与过线标准先写、单独提交 | 2.2 的题与判定落成文件：题面、必答项、不能项、每题该读的约定；Master 审过 | 单独提交在跑之前 |
| 10 | 最后一轮流程测试（描述改了则加触发测试） | 2.2 的题各 3 次；汇总进仓库，原始输出放 `S:\IDEO-Scrum-Archives\sprint-17-conventions-rewrite\`；判错的逐条人工看并写明理由。描述若改，照 Sprint 16 的触发测试跑基线对照 | 每题至少 2/3 过；触发测试过线同 Sprint 16 |
| 11 | 校验 | `claude plugin validate --strict plugins/ideo-scrum`；结构或 frontmatter 变了派 `plugin-dev:plugin-validator`（`model: haiku`）；Codex 同步与核对 | 通过；无必改；0 不一致 |
| 12 | 停点 ③：PO 亲手试 | PO 试一次 | PO 说行 |
| 13 | 收官准备交 Master | Review（压缩日志、归档 `scrum/documents/`、产品日志保鲜）、Retro（教训进记忆或 CLAUDE.md）、一个提交；v6.0.0、tag、合入、推送、更新本机插件由 Master 做 | Master 接受 |
| 14 | 补 IDEO 日志与模板（PBI-56 补充，停点 ② 之后） | `ideo-kernel/conventions/ideo-log.md`（4 条）与 `ideo-backlog-template.md`；8 处指向改名；overview 的图与第 4、5、7 条；sprint-log 第 17 条；README；Codex 同步 | 旧名 0 残留；引用核对 0 缺；check_codex 0 不一致；validate 通过 |

**Key choices**

- **先写稿、后搬**：正文全部先在 `drafts/` 里写、审、PO 读，`plugins/` 在 Sprint 16 合入 main 之前不动；搬家从新的 main 出发，对照 Sprint 16 的改动（应当只有路径）并进定稿。
- **路径不等清单**：Sprint 16 的 How 未提交前，照它 2.2 的布局四条推出新路径（scrum-kernel：`SKILL.md`、`overview.md` 在根，`assets/`、`conventions/`、`references/`；sprint-kernel：`conventions/`、`events/`；ideo-kernel：`conventions/`、`IDEO-modes/`、`methods/`；design-kernel：`conventions/`、`steps/`）；它的清单提交后逐条核对，以它的为准，差异只改路径表。
- **54 两份都改**：54 的正文落在 sprint-log 与冲刺模板；「照抄进 2.1 时查够不够」写进 sprint-log 第 5 条，product-log 第 12 条的同一条规矩收成指向——一条规矩只写一处。
- **53 写成角色和步骤**：写明谁在什么时候做什么；跨会话消息、`/fork`、plan 文件这些工具做法只当例子，不作规矩（overview 第 15 条：约定不写任何工具的具体操作）。落点拟为 sprint-log 新增一条，overview 第 14 条加一句指向，大纲里定。
- **46 ③ 照实查过再写**：`codex-cli 0.167.0` 没有子代理——`codex agents` 只是浏览和切换会话，`codex exec` 是非交互运行、`codex exec fork` 复制已有会话；等价做法是开一个新的 `codex exec` 会话、只给简报，fork 出来的会带着原会话、不算全新。结论只写进约定，不动 Codex 包的说法（那属 46 ⑤）。
- **58 ⑦ 照 Claude Code 文档写，并写明局限**：非 fork 的子代理默认带着 CLAUDE.md 各级文件和 git 状态快照；Explore、Plan 两样都不带；`omitClaudeMd` 只去掉用户、项目、本地 CLAUDE.md（受管策略仍加载），git 状态只有 Explore、Plan 能不带；fork 会继承父会话。所以约定写「用全新、非 fork 的子代理，简报只给第 1、2 章和收集的点子，不给现状」，并在约定里写清做不到的地方（受管策略、子目录 CLAUDE.md、git 状态）。依据记进第 4 章。
- **54 ③ 与 product-log 第 17 条挨得近**：「怎么判过时」的定义只写一处，大纲里定放哪份、另一份指向。
- **描述改不改在大纲里定**：56 的分界若进 ideo-kernel 或 design-kernel 的 `description`，触发测试排进第 10 项，基线是 Sprint 16 合入后的 main，同日同环境。
- **一份文件定完再改**（Sprint 14 的做法）：大纲一次给全；全文分设计侧、冲刺侧两批，Master 每批审一次。
- **测试先写后跑**：题目与判定标准单独提交，跑后不改；原始输出不进仓库。
- **改号与内容分开提交**（若有改号）：每处「convention N」脚本对到短名，再逐处读所指的条。

**Risks and open points**

- Sprint 16 的清单可能和路径表不同（`steps/`、`events/` 的文件名）；以它的为准，搬时再核，返工只在路径。
- 冲刺分支现在落后于 Sprint 16 的路径改动；搬家用 rebase 或 merge，冲突应集中在路径行。
- 描述若改，触发测试是整轮（Sprint 16 的 7 题 × 2 路径 × 3 次 × 两版），成本高；大纲时就要定，避免跑第二轮。
- 58 ⑦ 只能做到一半：CLAUDE.md 可用 Explore/Plan 或 `omitClaudeMd` 去掉，git 状态只有 Explore/Plan 能不带；受管策略和子目录 CLAUDE.md 去不掉。约定写目标与局限，不写工具操作。
- 46 ③ 已查过 help（0.167.0），没有实测；约定里标明这一点。
- 流程测试题多（Sprint 14 的 5 题加覆盖本冲刺的 6 题，33 次），先冒烟；判定脚本先自测。
- 新规矩容易在别处重复（56 的分界、58 的三个环、53 的协作）：各归一处，其余只指向，对抗审查专查这一项。

Go-ahead: 2026-11-12，PO（停点 ①，两个冲刺一起放行，原话「全部放行」）；范围：在冲刺分支上提交；Sprint 16 合入 main 后，从新的 main 搬进插件；停点 ②（PO 整份读审阅稿）和停点 ③（PO 亲手试）仍然要停；③ 之后由 Master 收官——打 tag、合入 main、发 v6.0.0（版本号、README、Codex 包）、推送 main、tag 和 SeaPawn-Memory、更新本机 Claude Code 的插件。
2026-11-13 变更（PO 原话见 2.2）：停点 ③ 取消，改为收官后 PO 自己看；收官与 v6.0.0 的本地发版由 Master 做；main、tag、记忆库都不推送；推送和更新本机插件交 PO 的辅助会话。

## 4. Increment notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (sprint-log.md, conventions 9 and 20). A session that picks up the Sprint reads these first. The chapter ends with the Product Owner's decision that the Increment can go into testing (sprint-log.md, convention 24). -->

| Date | What was done | Decision and reason | Evidence | Next |
| --- | --- | --- | --- | --- |
| 2026-11-12 | 接手 Sprint 17：在 Developer 的原生 worktree 切到 `sprint-17-conventions-rewrite`（路径 `S:\IDEO-Scrum\.claude\worktrees\awesome-pare-fb64d7`，分支自带开冲刺提交 `5f4dc72`），删掉自动分支 `claude/awesome-pare-fb64d7`；读日志、反馈文件（54、56、58 各行与原文）、Sprint 14 Review、Sprint 16 日志；精化复述；写 How | 2.2 没有疑问；54 的「两份都改」按 54 ④ 落成 sprint-log 第 5 条写、product-log 第 12 条收成指向 | 本日志 2.2、3 章 | 交 Master 审 How；等停点 ① 放行后做第 1 项 |
| 2026-11-12 | Master 审 How（`9cea676`）：整体可以，两处必补、两条建议、三件事 | 必补 1：ideo-kernel 的 `SKILL.md` 加一行指向新约定，写进第 3 项产出。必补 2：58 ⑦、46 ③ 先查依据——Claude Code 文档（code.claude.com/docs/en/sub-agents 的 What loads at startup）：非 fork 子代理带着 CLAUDE.md 各级和 git 状态快照，Explore、Plan 两样都不带，`omitClaudeMd` 只去掉用户/项目/本地 CLAUDE.md（受管策略仍加载），git 状态只有 Explore、Plan 能不带，fork 继承父会话；`codex-cli 0.167.0` 的 help：没有子代理，`agents` 只浏览和切换会话，`exec` 是非交互运行、`exec fork` 复制已有会话。建议：53 写成角色和步骤、工具做法只当例子（overview 15）；54 ③ 与 product-log 第 17 条的定义只写一处、大纲里定。三件事：`sync_codex.py` 用 rglob 整个复制，ideo-kernel 的 `conventions/` 自动带上、脚本不用改；收官时 Master 删全局记忆 Feedback 已落地的行与文件；停点 ② 的中文译文由 Master 安排，我只交英文原文 | 文档 en/sub-agents 的 What loads at startup 与 frontmatter 表（`omitClaudeMd`）；本机 `codex --version`、`codex --help`、`codex exec --help`、`codex agents --help` | 交 Master 再审；等放行 |
| 2026-11-12 | 放行后做第 1、2 项：改动点清单与新路径表（照 Sprint 16 的清单，`d9a1123`）、八份文件的大纲 | 五处待 Master 定：58 ④ 三个环放图下导读、不编号；58 ③ 主对话并进第 11 条；54 ③ 的「过时」定义写 sprint-log 第 17 条；53 放 sprint-log 第 26 条加 overview 第 14 条指向；56 两处描述各改一句（改了就把触发测试排进第 10 项） | `checklist.md`、`outline.md` | Master 同意大纲后写设计侧全文（第 3 项） |
| 2026-11-12 | Master 审大纲（`a1bae9b`）：五处定了、补三处 | 58 ④ 导读里加一句「PO 可把原型与测试之间的阶段决定交给 Scrum Master（overview 第 12 条）」，关卡不删，差别列进问题与建议给停点 ②；58 ③ 并进第 11 条但要整条重写、太长就拆——拆成新第 12 条（我的判断），改号单独提交；54 ③ 定义放 sprint-log 17；53 放 sprint-log 26 + overview 14；56 不改描述（P1 旁测三次都只加载 ideo-kernel，缺的是分界；流程测试行为栏不过再议）。补：56 的连带五处（scrum-kernel SKILL.md 加进稿件、sprint-log 6 第 4 步、overview 2、ideo-kernel Use Protocol 6、product-log 2）；46 ③ 的定义放 overview 第 7 条（全新子代理：只从简报起步，fork、复制都不算；没有子代理的工具开只给简报的新会话），工具版本与依据不进约定、记笔记、收官写进 PBI-46；58 ⑦ 只写目标与通用局限，Claude Code 的细节记笔记。建议：54 ② 加两种卡住（同一做法试两次不行、照 How 看不出怎么达成 Sprint Goal）；模板注释只加几个字和条号 | `outline.md`、`checklist.md` | 写第 3 项：设计侧全文 |
| 2026-11-12 | 第 3 项：设计侧全文审阅稿——design-log（27 条，新增第 12 条、原 12–26 顺延）、设计日志模板、ideo-kernel 新约定一份、ideo-kernel `SKILL.md` 两处、scrum-kernel `SKILL.md` 一段；附问题与建议 | 三个环与原型到测试之间的门有差别，列进问题 2、停点 ② 请 PO 看；新第 12 条造成顺延，搬运时内容与改号分开提交；`scrum-kernel/SKILL.md` 草稿基于现行文件，搬运时只套用我改的那段。测试通道备忘（Master 转）：reclaude 现在不可用；桌面会话直接跑 `claude -p` 报 Not logged in，起子进程时去掉 `CLAUDE_CODE_HOST_AUTH_ENV_VAR` 就能用；跑前先冒烟，同一轮只用一条通道 | `drafts/`（五个文件）、`drafts/problems-design-side.md` | 交 Master 审全文 |
| 2026-11-12 | Master 审设计侧全文（`8e6dc95`）：8 处必改、3 条建议（`C:\Users\seapawn\.claude\plans\sprint-17-review-design-side.md`） | 全照改：第 10 条引用回 11；58 ⑧ 的改法落到第 11 条、第 9 条只留一句；第 11 条整条重写；第 1 条补回「没有现成答案」；第 3 条贴 PO 的话；第 27 条只指向；ideo 第 1 条两处（聊天算共情材料、record by method 写明记在哪）；scrum-kernel 最后一句改成「never gets a solution first」。建议：ideo 的两处指向留工具箱一处；题 2 的判定按新分界；改号牵到的草稿外引用（design-kernel `SKILL.md` 五阶段表与 Use Protocol、overview 第 12 条、模板与命令）放进改号提交。ideo 第 1 条 (b) 的举例拿不准，停点 ② 请 PO 看 | `drafts/`、`problems-design-side.md` | 写第 4 项：冲刺侧全文 |
| 2026-11-12 | 第 4 项：冲刺侧全文审阅稿——sprint-log（改 5、6、10、17、22，新增 26）、冲刺日志模板（Now 行）、product-log（2、12、17）、overview（2、7、12、14）；附问题与建议 | 54 ④ 写 sprint-log 5、product-log 12 收成指向；54 ③ 写 sprint-log 17、product-log 17 指向；54 ① Now 行写模板与第 22 条；53 写第 26 条、overview 14 指向；46 ③ 定义放 overview 7；56 连带三处指向 ideo 约定；搬家后的跨技能路径全部写 `../scrum-kernel/…`、`../ideo-kernel/SKILL.md` | `drafts/sprint-kernel/`、`drafts/scrum-kernel/`、`drafts/problems-sprint-side.md` | 交 Master 审冲刺侧；设计侧的复核一起做 |
| 2026-11-12 | Master 审设计侧复核与冲刺侧全文（`4c16ab2`、`cb2e6be`）：4 处必改（`C:\Users\seapawn\.claude\plans\sprint-17-review-sprint-side.md`） | 全照改：product-log 的 `../overview.md` 改回 `overview.md`（5 处）；两份模板的 `../` 改成文字说明（写明哪个技能的哪个文件夹）；sprint-log 第 26 条拆成两种情况（能直接通话的、只能靠日志的），标题改 Developer in another session or tool，overview 第 14 条跟着改；design-log 第 11 条用 Master 给的合并写法 | `drafts/` | 第 5 项：连带改动与引用核对 |
| 2026-11-12 | 第 5 项：连带改动与引用核对——`check_refs.py`（先拿 4 条已知结果自测）171 处引用 0 缺，跨文件逐处读；路径核对 | 查出并改两处：product-log 第 7 条的地图路径还是旧的 `../design-kernel/define/make-a-map.md`（改 `steps/2-1-…`）；overview 的 Departures 表里裸写的 `product-log.md`（改 `conventions/product-log.md`）。搬运时要做的：design-kernel `SKILL.md` 五阶段表的条号（6–7、8、9 and 11–15、16、17–18、19、21，及 Use Protocol 的 5、24、21、19）；`commands/scrum-master.md` 第 48 行「open a design」改成指向 ideo 约定（在 Sprint 16 的版本上加一行）；README 的 ideo-kernel 文件表加 `conventions/` 一行；CLAUDE.md 收官时更新 | `checks.md`、`check_refs.py` | 交 Master，派对抗审查（第 6 项） |
| 2026-11-12 | 对抗审查已派出（审 `7426b3d` 的快照）；等结果期间不改 `drafts/`。备好停点 ② 的材料 | Master 同意改 scrum-master 命令那一行：只改正文、不动描述、不用跑触发测试，搬运时在 Sprint 16 的版本上加；停点 ② 的材料：结构清单在前、全文在后，两处请 PO 看（三个环与关卡、ideo 约定 (b) 的举例） | `checks.md`（命令一行改成「已同意」）、`stop2.md` | 等对抗审查结果；之后搬运 |
| 2026-11-12 | 对抗审查（`7426b3d` 快照，Haiku 全新子代理；Master 逐条核过）：收下 5 处、其余不改 | 改：sprint-log 5 补回「every item serves it」「never one just to fill the Sprint」；design-log 11 改成「不给今天怎么解——现有设计、规则、代码」（不和第 2 章的地图读混）；design-log 19 改成「merge it into its base (convention 4), then delete it」；sprint-log 的图节点改成「Settle it: a design sprint or the five modes (ideo-kernel)」；sprint-log 26 末尾改「(These are examples, not rules.)」。checklist 同步：58 ⑧ 落在第 9 条一句、改法在第 11 条；ideo `SKILL.md` 只留工具箱一处指向。不改的：design-kernel `SKILL.md` 的旧条号在搬运时做（checks.md 已列）；scrum-kernel `SKILL.md` 取 Sprint 16 版本；白纸开设计冲刺不冲突（PBI-52 的路）；overview 2 各管各的；design-log 10 的 at least two methods 是 Sprint 14 PO 强审定下的；模板 1.1 注释、overview 7 的例外、19 的指向不改 | `drafts/`、`checklist.md`、`stop2.md`；复查 172 处引用 0 缺 | 提交后进停点 ② |
| 2026-11-12 | Master 备忘：Sprint 16 在搬运前改了冲刺模板 1.1、1.2 的注释（validator 说 1.1 的引用太松），以及 overview 第 8 条和四个命令的加载说法 | 搬运时先取 Sprint 16 的版本，保留它改过的地方，别被我的稿覆盖；我的 overview 稿只套用第 2、7、12、14 条与路径，第 8 条用它的 | `checks.md` 的「搬运时要做的」 | 停点 ② 等 PO |
| 2026-11-12 | Master 转：PBI-52（白纸入口）并入本冲刺——范围调整，Sprint Goal 不变（Master，PO 委托） | 来由：Sprint 16 改描述后，题 3 两条路径的行为栏都到 3/3，触发问题解决了；剩下的缺口在内容——从 `/ideo-scrum:scrum-master` 进的路径，3 次里有 2 次没说「设计的结论会流回产品日志」。2.1 加 PBI-52 一行；2.2 记并入理由与决定；验收加第 8 项（题 3 两条路径各至少 2/3 过）；测试改成所有题走直接说、题 2 与题 3 另走角色命令、每条路径 3 次各自过线；草稿先不动，等 PO 停点 ② 的意见和测试结果 | 本日志 2.1、2.2、验收、测试；`checklist.md` | 等 PO 意见与 Sprint 16 合入 |
| 2026-11-12 | 第 8 项搬运：main（`72d398f`）合入（`18f9202`）；内容提交 `9ffb765`、改号提交 `d5c0e6a`、Codex 包 `4212a2a` | Sprint 16 改过的地方都保留（冲刺模板 1.1 的「conventions 4 and 20」、1.2 的文字定位、overview 第 8 条、四个命令的加载说法、scrum-kernel `SKILL.md` 的约定表与描述）；scrum-master 第 48 行照同意改；design-kernel `SKILL.md` 的条号跟上；内容与改号分两个提交（内容版 design-log 新条暂排 27） | 引用核对 189 处 0 缺；`sync_codex.py` 写 11 个文件、`check_codex.py` 0 不一致；`claude plugin validate --strict` 通过（只有图标警告，PBI-25 ⑦）；`checks.md` 第五节 | 等 PO 停点 ② 意见；第 9 项写测试题交 Master 审 |
| 2026-11-13 | Master 转：PO 停点 ② 说行；补 IDEO 日志与模板并入 PBI-56（范围调整，Sprint Goal 不变）；PO 取消停点 ③、权限全交 Master | 定案见 2.2；批次提交 `3d823bd`（ideo-log 四条、IdeoBacklog 模板、8 处指向、overview 的图与第 4/5/7 条、sprint-log 第 17 条、README、Codex 同步）；必改 `3a69305`（设计模板第 7 行补回 in design-log.md）；停点 ③ 改为收官后 PO 自己看；推送与更新本机插件交 PO 的辅助会话 | 本日志 2.2、验收、How 第 14 项；`check_refs.py` 改为插件版（196 处 0 缺） | 交 Master 审这一批；之后第 9 项测试题 |
| 2026-11-13 | Master 审 IDEO 日志批次（`3d823bd`）：8 处必改、6 条建议 | 全照改：`in sequence` 改「a run of its own」（3 处）；分界 6 处去掉 `on the spot`；第 3 条与第 2 条重复的并进第 2 条；第 4 条归档只指向 sprint-log 第 17 条；模板第 3 行指的句子写进第 3 条；overview 图里 Designer 与 Stakeholders 连回设计冲刺节点；sprint-log 第 17 条两句并一句；overview 的「other files」补 ideo 两份。建议全取：ideo 图加一条到设计冲刺的虚线；「modes, not stages」；ideo `SKILL.md` 两处指向并进 Conventions 一节；模板标题改 IDEO Backlog；模板加「五个标题都留着」一句；overview 第 5 条带上 IDEO 日志 | 引用 197 处 0 缺；Codex 0 不一致；validate 通过 | 交 Master，派对抗审查 |
| 2026-11-13 | 对抗审查（`d9533bf` 快照）：9 条收 3 条、驳 6 条（Master 逐条核过） | 收：overview 图 X0→X2 的线与 X2 节点改成整支五模式（一两个方法或开 IDEO 日志）；第 3 条分层表与第 60 行带上 IDEO 日志；模板头部补「章号只是编号，不是做的先后（ideo-log 第 2 条）」。驳（理由照记）：图里 IDEO 日志的结论只流回产品日志，与设计冲刺那支同一种简化，完整规矩在 ideo-log 第 4 条；「每个阶段站在一个模式上」是设计冲刺自身的结构，写在讲设计冲刺的地方不算重复，关系只在 ideo-log 第 2 条；图上「a run of its own」就是第 3 条定义的词，两种情况都包括；role cards 有 overview 第 7 条定义，map、Lightning Demos、storyboard 只是举例，不影响照着走；scrum-kernel `SKILL.md` 第 21 行与 overview 第 2 条已指向 ideo-log 第 1 条，IDEO 日志由谁跑在模板头部由人填 | 引用 198 处 0 缺；Codex 0 不一致；validate 通过 | 交测试题给 Master |
| 2026-11-13 | 第 9 项：最后一轮流程测试 42 次（12 题直接 + 题 2、3 的命令路径），冒烟核对加载的是 worktree 版本（base directory 指向 worktree、读得到 ideo-log） | **没有全部过线**：9 题过；题 2 直接 0/3（都没答出「PO 指定或默认分界」）、题 3 两条路径 1/3 与 1/3（空白页原因与结论回流没答全）、题 9 0/3（一个技能都没加载、没读 ideo-log）、题 10 0/3（都把「IDEO 五阶段法」当成设计冲刺）。缺口在触发与读约定（行为栏）和分界措辞（内容栏）两处；标准与判定没改，不重跑、不改判。改法（改描述、点明「五阶段法指五模式」、加强白纸回流）由 PO 与 Master 定 | `test-summary.md`；原始输出在 `S:\IDEO-Scrum-Archives\sprint-17-conventions-rewrite\`；`parse_results.py` | 交 Master |
| 2026-11-13 | 第 1 轮不过，Master 定：改一轮、整轮重跑；题目与标准不动，第 1 轮的行为栏当改前基线（同一天、同一条通道，第 2 轮每题行为不能比第 1 轮差） | 四处改动：① 三份描述——ideo-kernel 写明「IDEO 五阶段法」就是五模式、成段跑记进 IDEO 日志，并加「没有现成答案」的触发；design-kernel 写明它不是五阶段法、「Five stages」改「Five design-sprint stages」；scrum-kernel 的「open a design first」改成先照分界定。② design-kernel `SKILL.md` 开头加一句指向 ideo-kernel。③ 白纸：overview 图 BP 连回设计冲刺、X→A 写明白纸的设计填产品日志；design-log 第 1 条与设计模板头部带上「写不出产品」与「结论去填产品日志」的要旨。④ sprint-log 第 6 条第 4 步写明由 PO 照分界定 | 引用 198 处 0 缺；Codex 0 不一致；validate 通过；`plugin-dev:plugin-validator`（Haiku）已派 | 等 validator 与 Master 审；审过整轮重跑 |

## 5. Test

<!-- Record here the Developer's tests, the reviewer's check (by default the Scrum Master), the Product Owner's end-to-end test, and the result of each Definition of Done item and acceptance criterion. Fix a problem on the spot and test again (sprint-log.md, convention 16). The chapter ends with the Product Owner's decision: close, or go back (sprint-log.md, convention 24). -->
