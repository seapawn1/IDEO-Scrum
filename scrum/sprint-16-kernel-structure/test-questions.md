# Sprint 16 测试题与判定

> 2.2「测试」一节的执行稿。先经 Master 审，单独一个提交，再跑；跑后不改题目、不改判定、不改判。
> 基线固定在 `9769bd6`：用 `git archive 9769bd6 plugins/ideo-scrum` 解到仓库外的临时目录（如 `%TEMP%\ideo-s16-baseline\plugins\ideo-scrum`），从那里跑，不指向主检出。新版：本分支的插件（`S:\IDEO-Scrum\.claude\worktrees\wizardly-almeida-5485e1\plugins\ideo-scrum`）。两轮同日、连着跑。

## 测法

- 无头：`reclaude -p --plugin-dir <插件的 Windows 路径>`（`reclaude` 不可用时用 `claude -p`，参数相同）；模型 Haiku。
- 只开 Read、Grep、Glob、Skill；Bash、PowerShell 与其他工具全关；加 `--strict-mcp-config --no-session-persistence`，用 `--output-format stream-json --verbose` 留下每次调用读了哪些文件。
- 工作目录：系统临时目录里新建的空项目；每次调用是一个全新会话。
- 路径一（直接说）：题目原样作为提示。
- 路径二（角色命令）：提示 = `/ideo-scrum:<role>` 加空格再加同一题。进入方式以第 2 项冒烟为准；若 `-p` 不认斜杠命令，就在跑任何正式测试之前把测法定下来写进第 4 章，题目与判定不变。
- 每题每条路径 3 次：7 题 × 2 路径 × 3 = 42 次；另加加载冒烟 8 次（见下）。
- 原始输出放 `S:\IDEO-Scrum-Archives\sprint-16-kernel-structure\` 下（`baseline\`、`new\`）；仓库里只留汇总；提交前扫一遍提供方地址、凭据值、令牌形态。

## 判定

一次回答算过，要同时满足：

1. 读到该题对应的约定文件（用 Read 读，或用 Grep 的输出读到文件内容，都算）；基线按基线的路径判，新版按新版的路径判（见每题「要读」）。
2. 必答项全中（写「至少几条」的按写的算）。
3. 没有「不能」项。

机械部分（读了哪些文件、五个阶段名的先后）用脚本；语义部分逐条读回答来判，每条写下依据的原话。脚本先拿已知结果自测（一份读过 sprint-log 的、一份只读了 SKILL.md 的，应各判对）；判错或拿不准的逐条人工看，改判写明理由。

汇总分两栏：行为（加载了哪些技能、读没读该读的约定）、内容（必答项中没中）。

## 过线（同 2.2）

1. 每条路径的行为栏合计，新版不少于基线减 1。
2. 没有一题从过线（3 次里至少 2 次过）跌到不过线。
3. 白纸题（题 3）：新版两条路径各至少 2/3 过。
4. 加载冒烟（新版）：四个命令各 2 次，都加载了 ideo-kernel 和 scrum-kernel；不开设计、不开冲刺时不加载 design-kernel、sprint-kernel。

## 题目

### 题 1 开冲刺

- 题目：我在做一个帮人整理读书笔记的命令行小工具，产品日志已经写好了。现在要开一个新的 Sprint，把它往前推一步。这个 Sprint 从头到尾会怎么走？每一段做完以后，由谁来决定能不能往下走？
- 角色命令：`/ideo-scrum:scrum-master`
- 要读：基线 `scrum-kernel/conventions/sprint-log.md` 或 `scrum-kernel/overview.md`；新版 `sprint-kernel/conventions/sprint-log.md` 或 `scrum-kernel/overview.md`。
- 必答（三条）：① 五个阶段按先后说全：Why、What、How、Increment、Test（回答里按这个先后出现这五个名字，可以加中文说明）；② 每个阶段结束时由 PO 决定能不能往下走（拍板），不是 Scrum Master 或 Developer 自己定，也不只是「审阅」「验收」；③ 至少说出三处具体的决定：Why 结束定 Sprint Goal；What 结束定精化到此为止；How 的放行（go-ahead）；Increment 结束定可以进入测试；Test 结束定收官还是回去。
- 不能：用 Scrum Guide 的事件（Planning、Daily Scrum、Review、Retrospective）代替这五个阶段来组织回答；说 Sprint 有固定时长（如两周）。收官时把 Review、Retro 当作动作提到，不算违规。

### 题 2 精化碰到没有现成答案的问题

- 题目：Sprint 里精化做到一半，碰到一个问题：这个读书笔记工具的用户到底是谁，对他们来说怎样才算好用，我们自己说不清，手上的资料里也没有现成的答案。这时候该怎么办？这个 Sprint 接下来怎么走？
- 角色命令：`/ideo-scrum:scrum-master`
- 要读：基线 `scrum-kernel/conventions/sprint-log.md` 或 `design-kernel/conventions/design-log.md`；新版 `sprint-kernel/conventions/sprint-log.md` 或 `design-kernel/conventions/design-log.md`。
- 必答（三条）：① 为这个问题开一个设计，而不是自己拍脑袋定下答案或直接开始做；② 只把这个难点取出来做设计，Sprint 的其余部分照常进行；③ 设计从共情（Empathize）起：先找当事人、用户，问具体的经历，而不是先出方案。
- 不能：不做设计、直接定一个用户画像或功能就往下做；让整个 Sprint 停下来等设计。

### 题 3 白纸项目

- 题目：我有个想法：给一家社区图书馆做一个帮读者找书的工具。现在手上只有这一句话，没有产品日志，也不知道读者具体要什么。我想把这件事正式做起来，第一步该做什么？
- 角色命令：`/ideo-scrum:scrum-master`
- 要读：两版相同——`scrum-kernel/conventions/product-log.md` 或 `scrum-kernel/overview.md`，或 `design-kernel/conventions/design-log.md`。
- 必答（三条）：① 从设计开始，产品和 Product Goal 交给设计去回答；可以先写能写的部分（如利益相关者表，或一条指向这个设计的 PBI），但不先把产品日志写完；② 说明原因：现在写不出产品和 Product Goal，要靠设计去回答；③ 设计的结论会流回产品日志（让设计去填产品日志），之后再用 Sprint 去做。
- 不能：先把产品日志写完再开始（能写的部分可以先写，见必答 ①）；先出方案或直接做。

### 题 4 设计的构思

- 题目：设计走到构思这一步了：挑战、设计目标、设计问题和地图都写进日志了，PO 也选出了要解决的那个问题。接下来怎么得到方案？谁来做，各自怎么做，最后怎么选？
- 角色命令：`/ideo-scrum:designer`
- 要读：两版相同——`design-kernel/conventions/design-log.md`。
- 必答（四条，①② 必须答出，③④ 至少答出一条）：① 每个草图先发散再收敛：先用至少两种方法大量出点子（求量、先不评判），再收成自己那一份方案；② 用 ideo-kernel 的构思方法（IDEO），与书的步骤一起用，是必须用，不是可选（判法：回答把 IDEO 方法当作流程里的一步来用，与书的步骤一起，就算过；说成「需要时再用」「也可以用」才算不过；不要求回答里出现「必须」两个字）；③ 几个互相看不见的全新子代理，各出一份完整的方案草图；④ 最后由 PO 做出选择（Scrum Master 主持，不找共识）。
- 不能：每个草图直接收敛，没有发散这一步；把 IDEO 方法说成可选、需要时再用；由 Scrum Master 或子代理替 PO 选定。

### 题 5 收官

- 题目：这个 Sprint 的 Sprint Goal 已经达成，PO 说可以收官了。收官要做哪些事？冲刺日志怎么处理？这个 Sprint 学到的教训记在哪里？
- 角色命令：`/ideo-scrum:developer`
- 要读：基线 `scrum-kernel/conventions/sprint-log.md`；新版 `sprint-kernel/conventions/sprint-log.md`。
- 必答（三条）：① Review 是收官时的动作：把日志压缩成关键决定，改名 `sprint-NN-<后缀>.md`，移进 `scrum/documents/`，删掉其余中间文件；② 要更新产品日志（做完的移走，没做完的回待办，或说「保鲜」）；③ Retro 也是动作：教训以原则的形式写进项目的记忆文件或说明文件（没有就新建一个）。
- 不能：在冲刺日志里加 Review 章或 Retro 章（或说日志有这两章）。

### 题 6 产品日志

- 题目：我们项目的产品日志要重写一遍：产品是什么、Product Goal 怎么写、待办事项怎么列，还有这些该由谁来决定。这份日志应该写成什么样？
- 角色命令：`/ideo-scrum:scrum-master`
- 要读：两版相同——`scrum-kernel/conventions/product-log.md` 或 `scrum-kernel/overview.md`。
- 必答（三条）：① 从模板建一份产品日志（文件 `ProductBacklog.md`），分 Product、架构、PBI 三块；② PBI 用七列写，至少说出五列；编号只用来计数，不是优先级；③ PBI 由 PO 与 Master 一起定；Product Goal 只有 PO 能改。
- 不能：把技术设计（模块、接口）写进产品日志。

### 题 7 冲刺日志

- 题目：项目要开下一个 Sprint 了，我们准备把冲刺日志建起来。这个日志放在哪里、叫什么名字？里面要有哪几章？开头要写些什么？
- 角色命令：`/ideo-scrum:developer`
- 要读：基线 `scrum-kernel/conventions/sprint-log.md` 或 `scrum-kernel/conventions/sprint-backlog-template.md`；新版 `sprint-kernel/conventions/sprint-log.md` 或 `sprint-kernel/conventions/sprint-backlog-template.md`。
- 必答（三条）：① 一个冲刺一个文件夹 `scrum/sprint-NN-<后缀>/`（编号是上一个冲刺加一），和分支同名，收官时也是 tag 名；② 从模板建，文件名 `SprintBacklog.md`，表头至少说出三项（开始日期、分支、PO、Scrum Master、Developer）；③ 五章按先后说全：Why、What、How、Increment、Test。
- 不能：给冲刺写截止日；在日志里另加章。

## 加载冒烟（新版，验收 ④）

- 四条角色命令各 2 次；提示用中性的一句话，如「跟我说说你能帮我做什么。」，不开设计、不开冲刺。
- 判：每次调用都加载了 ideo-kernel 和 scrum-kernel；没有加载 design-kernel、sprint-kernel。8 次全中算过。
