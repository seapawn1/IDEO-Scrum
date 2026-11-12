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
| PBI-56 | 设计冲刺与 IDEO 五阶段法分清 | 作为熟手，我想要插件分清设计冲刺和 IDEO 五阶段法：小问题就地用五阶段法，大问题才开设计冲刺，由 PO 指定，以便不为小问题兴师动众 | 插件：ideo-kernel（新 `conventions/`）、design-kernel（design-log 第 1、26 条） | M |
| PBI-53 | 约定写明 Developer 在别的工具里时怎么协作 | 作为熟手，我想要约定写明 Developer 在别的工具（如 Codex）里干活时，它和 Master 怎么协作，以便不用口述 Sprint 13 的做法，换工具也能照着走 | Map ③～⑧ | S |
| PBI-46 | Codex 版后续小修 | 作为熟手，我想要 Codex 包的同步和说明再顺一点，以便以后每次发版重跑同步都不用多想，陌生人在 Codex 里也能起步 | Map ①（装插件，开会话） | S |

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

**验收**

1. 收进的每一点都写进了约定：一张对照表，PBI-54 ①–④、PBI-58 ①–⑧、PBI-56、PBI-53、PBI-46 ③，每点对到约定文件和条。
2. 一条规矩只写一处：同一条规矩的其他说法都改了或删了；对抗审查的必改项清零。
3. 引用：每处「convention N」和路径都指得到，并且指对（脚本核对，再逐处读）。
4. 停点 ②：PO 整份读审阅稿，说行。
5. 最后一轮流程测试过线（见下）。
6. `claude plugin validate --strict plugins/ideo-scrum` 通过；结构或 frontmatter 改了，再派 `plugin-dev:plugin-validator`（`model: haiku`）；Codex 同步与核对通过。
7. 停点 ③：PO 亲手试一次。

**测试**（跑之前写定，跑后不改；Master 定，PO 委托）

- 判定标准和题目先写、Master 审过、单独提交，再跑；跑后不改标准、不改判；脚本判错的逐条人工看，改判写明理由。
- 测法同 Sprint 16（无头、Haiku、只开 Read、Grep、Glob、Skill、连 PowerShell 一起禁、空项目、每次一个全新会话、先冒烟），跑在搬进插件后的版本上。
- 题目：Sprint 14 流程测试的题 1–5（见 `git show a87bd1c:scrum/sprint-14-conventions-tuning/SprintBacklog.md` 的 2.2），加上覆盖本冲刺改动的题：断线后接手一个冲刺（54 ①）、什么时候算卡住（54 ②）、选条目写 2.1（54 ④）、一个小问题该用五阶段法还是开设计冲刺（56）、设计的地图和设计目标怎么写（58 ①②）、Developer 在 Codex 里时怎么协作（53）。用自然的说法，不带引导词。
- 一次回答算过：读到该读的约定、必答项全中、没有「不能」项（Sprint 14 的判定）。每题 3 次，过线：每题至少 2 次过。
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

## 4. Increment notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (sprint-log.md, conventions 9 and 20). A session that picks up the Sprint reads these first. The chapter ends with the Product Owner's decision that the Increment can go into testing (sprint-log.md, convention 24). -->

| Date | What was done | Decision and reason | Evidence | Next |
| --- | --- | --- | --- | --- |
| 2026-11-12 | 接手 Sprint 17：在 Developer 的原生 worktree 切到 `sprint-17-conventions-rewrite`（路径 `S:\IDEO-Scrum\.claude\worktrees\awesome-pare-fb64d7`，分支自带开冲刺提交 `5f4dc72`），删掉自动分支 `claude/awesome-pare-fb64d7`；读日志、反馈文件（54、56、58 各行与原文）、Sprint 14 Review、Sprint 16 日志；精化复述；写 How | 2.2 没有疑问；54 的「两份都改」按 54 ④ 落成 sprint-log 第 5 条写、product-log 第 12 条收成指向 | 本日志 2.2、3 章 | 交 Master 审 How；等停点 ① 放行后做第 1 项 |
| 2026-11-12 | Master 审 How（`9cea676`）：整体可以，两处必补、两条建议、三件事 | 必补 1：ideo-kernel 的 `SKILL.md` 加一行指向新约定，写进第 3 项产出。必补 2：58 ⑦、46 ③ 先查依据——Claude Code 文档（code.claude.com/docs/en/sub-agents 的 What loads at startup）：非 fork 子代理带着 CLAUDE.md 各级和 git 状态快照，Explore、Plan 两样都不带，`omitClaudeMd` 只去掉用户/项目/本地 CLAUDE.md（受管策略仍加载），git 状态只有 Explore、Plan 能不带，fork 继承父会话；`codex-cli 0.167.0` 的 help：没有子代理，`agents` 只浏览和切换会话，`exec` 是非交互运行、`exec fork` 复制已有会话。建议：53 写成角色和步骤、工具做法只当例子（overview 15）；54 ③ 与 product-log 第 17 条的定义只写一处、大纲里定。三件事：`sync_codex.py` 用 rglob 整个复制，ideo-kernel 的 `conventions/` 自动带上、脚本不用改；收官时 Master 删全局记忆 Feedback 已落地的行与文件；停点 ② 的中文译文由 Master 安排，我只交英文原文 | 文档 en/sub-agents 的 What loads at startup 与 frontmatter 表（`omitClaudeMd`）；本机 `codex --version`、`codex --help`、`codex exec --help`、`codex agents --help` | 交 Master 再审；等放行 |
| 2026-11-12 | 放行后做第 1、2 项：改动点清单与新路径表（照 Sprint 16 的清单，`d9a1123`）、八份文件的大纲 | 五处待 Master 定：58 ④ 三个环放图下导读、不编号；58 ③ 主对话并进第 11 条；54 ③ 的「过时」定义写 sprint-log 第 17 条；53 放 sprint-log 第 26 条加 overview 第 14 条指向；56 两处描述各改一句（改了就把触发测试排进第 10 项） | `checklist.md`、`outline.md` | Master 同意大纲后写设计侧全文（第 3 项） |
| 2026-11-12 | Master 审大纲（`a1bae9b`）：五处定了、补三处 | 58 ④ 导读里加一句「PO 可把原型与测试之间的阶段决定交给 Scrum Master（overview 第 12 条）」，关卡不删，差别列进问题与建议给停点 ②；58 ③ 并进第 11 条但要整条重写、太长就拆——拆成新第 12 条（我的判断），改号单独提交；54 ③ 定义放 sprint-log 17；53 放 sprint-log 26 + overview 14；56 不改描述（P1 旁测三次都只加载 ideo-kernel，缺的是分界；流程测试行为栏不过再议）。补：56 的连带五处（scrum-kernel SKILL.md 加进稿件、sprint-log 6 第 4 步、overview 2、ideo-kernel Use Protocol 6、product-log 2）；46 ③ 的定义放 overview 第 7 条（全新子代理：只从简报起步，fork、复制都不算；没有子代理的工具开只给简报的新会话），工具版本与依据不进约定、记笔记、收官写进 PBI-46；58 ⑦ 只写目标与通用局限，Claude Code 的细节记笔记。建议：54 ② 加两种卡住（同一做法试两次不行、照 How 看不出怎么达成 Sprint Goal）；模板注释只加几个字和条号 | `outline.md`、`checklist.md` | 写第 3 项：设计侧全文 |

## 5. Test

<!-- Record here the Developer's tests, the reviewer's check (by default the Scrum Master), the Product Owner's end-to-end test, and the result of each Definition of Done item and acceptance criterion. Fix a problem on the spot and test again (sprint-log.md, convention 16). The chapter ends with the Product Owner's decision: close, or go back (sprint-log.md, convention 24). -->
