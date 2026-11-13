# Sprint Backlog — Sprint 19 (board-hook)

> Started: 2026-11-13 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: worktree-golden-orbiting-bachman | Product Owner: SeaPawn | Scrum Master: 会话 IDEO # [master]-[main]-[support sprint] | Developer: Claude Code（会话 IDEO # [developer]-[sprint-19]-[do sprint 19]，golden-orbiting-bachman）
> Now: How：Developer 已写完草稿，待 Master 审、给放行 · Master 2026-11-13 定精化结束（PO 授权，见第 4 章）
> Waiting for PO: None
> How to write this log: `sprint-log.md` in the sprint-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled later; add none — remarks go in chapter 4, Increment notes (`overview.md` in the scrum-kernel skill folder, convention 16).

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 看得见：看板把产品日志和开着的冲刺、设计浓缩成卡片，hook 把承诺放进上下文；PO 照着就能一眼看清进度，AI 照着就不忘目标。（PO 2026-11-13 定） |
| --- | --- |

### 1.2 Definition of Done

**Outcome Done**

| 度量 | 目标信号 |
| --- | --- |
| 一次会话走通方法论环节：完整引导（结构化、忠于原文） | 用户不反复追问 |

**Output Done**

| 维度 | 标准 |
| --- | --- |
| 无死链 | 所有 markdown 内部链接可解析，无 404 |
| 插件校验 | `claude plugin validate --strict plugins/ideo-scrum` 通过 |
| Codex 包 | 改了插件就跑 `scripts/sync_codex.py`，`scripts/check_codex.py` 通过（hook 能同步就一起同步） |

PO 2026-11-13 定 Sprint Goal

## 2. What

### 2.1 Product Backlog Items

| 编号 | 标题 | 用户故事 | 架构定位 | 规模 |
| --- | --- | --- | --- | --- |
| PBI-35 | 看板——卡片化，一眼看清进度 | 作为熟手（也是 PO），我想要一块项目级的看板，把产品日志、开着的冲刺和设计各浓缩成一张卡，以便不翻日志就知道全局和等我拍板的事 | Map「看进度」 | M |
| PBI-61 | 目标常驻——hook 把承诺放进上下文 | 作为熟手（也是 PO），我想要 hook 把当前的几句承诺放进上下文，以便长会话、压缩、换会话之后 AI 仍照同一个目标做事，不用我反复提醒 | Map「看进度」 | M |

### 2.2 Refinement

> 精化由 Master 主持并定案（PO 2026-11-13 授权，原话见第 4 章）。看板和 hook 读的是日志头部，接口由 Sprint 18 的 PBI-66 定（Sprint 18 日志 2.2，提交 `df88e67`），这里照抄读取规则，不另定格式。

**接口：日志的读取规则（照抄 Sprint 18 的 66 定案）**
- 开着的日志：`scrum/sprint-*/SprintBacklog.md`、`scrum/design-*/DesignBacklog.md`、`scrum/ideo-*/IdeoBacklog.md`，不含 `scrum/documents/`；产品日志是 `scrum/ProductBacklog.md`。
- 承诺：表头行的首格是 `Commitment` 或 `承诺`，第二格就是原文；它是哪种承诺，看上方最近的节标题：产品日志 1.1 Product、1.2 Product Goal；冲刺日志 1.1 Sprint Goal；设计日志 1.2 Design goal。IDEO 日志没有承诺，沿 For 找它服务的日志。
- 现状：以 `> Now:` 开头的行。等 PO 的事：以 `> Waiting for PO:` 开头的行，`None` 表示没有。产品日志没有这两行。
- 在 66 的模板合进 main 之前，旧日志里可能没有 Waiting for PO 行：读不到就当 None，不报错。
- 工作块完成：冲刺日志第 3 章表里，Done when 格以 `✓` 开头的行算完成；Developer 做完一块，就在该格最前面写「✓ 日期」。这条规矩由 Sprint 18 写进 sprint-log（66-8），主线不改 sprint-log。（Master 2026-11-13 定）

**PBI-35 看板**——观点：照抄 2.1。

| # | 点 | 定案（谁定） |
| --- | --- | --- |
| 35-1 | 先开设计还是直接做原型 | 不另开设计。卡片的构想 PO 已经给了（2026-11-13）：本冲刺的第一块工作，就是拿真实数据做产品卡的粗原型。（Master） |
| 35-2 | 做成什么形式 | 原型的产品卡做两版：一个 Markdown 文件（需要时带 Mermaid），一个打开就能看的单文件网页。PO 看一眼，挑一种，后面就照它做。这是 PO 的口味，留给 PO 定；他挑之前，Waiting for PO 写上这一项。（Master 定做法，PO 定形式） |
| 35-3 | 卡上放什么（PO 的设计） | 产品卡：两句承诺 · 架构图（产品日志 2.2）· 未完成的条目（3.1，按主线、副线、以后分组，每条的状态链到对应的冲刺卡或设计卡）。冲刺卡：承诺 · PBI 路线图（只放 2.1 的条目，加上它们在产品日志里的状态；不从工作块推算 PBI 完成了多少，PBI 算不算完成以产品日志为准，Review 时才改。Master 定）· How 进度（五个阶段标出当前，Now 行，第 3 章的工作块列表，Done when 格以 ✓ 开头的标完成。Master 定）。设计卡：承诺 · 地图 · 进行中的方案。IDEO 日志不单独成卡，在它服务的那张卡下面占一行。每张卡都显示自己的 Waiting for PO；产品卡顶部汇总所有等 PO 拍板的事。产品卡链到开着的冲刺卡、设计卡，冲刺卡链到它开的设计卡，每张卡都链回日志原文。（PO 定设计，Master 定细节） |
| 35-4 | 数据从哪来 | 只照上面的读取规则读日志，不另存状态。开在别的分支、还没合进来的冲刺，用 git 读它已提交的日志，卡上注明「截至提交 <hash>」；看板顶部写生成时间和读了哪些分支。（Master） |
| 35-5 | 文件放哪、进不进版本控制 | `scrum/` 下一个生成出来的文件（Markdown 叫 `Board.md`，网页另起名，由 35-2 定），看的时候重新生成，本项目不提交，加进 `.gitignore`。它不拥有任何东西，删了也随时能重建。overview 第 4 条加一句看板文件（原定由 Sprint 18 的 60 写，改到本冲刺，Sprint 18 不改第 4 条）。（Master） |
| 35-6 | 谁来生成 | 便宜的模型（Haiku）照插件里的一份说明加卡片模板生成，例如 PO 助手会话或一个子代理；做成技能、约定还是命令，由 Developer 在 How 里定。插件内容要自足：模板用英文，读中文日志也行。（PO 定便宜模型；Master） |
| 35-7 | 不做的 | 交互、存状态、在看板上改日志、Codex 专用的部分。（Master） |

**验收标准（35）**
1. 拿本仓库现在的状态（main 加 Sprint 18、19 两个分支）生成出看板：一张产品卡、两张冲刺卡，有设计时还有设计卡，内容照 35-3；链接都打得开（DoD「无死链」）。
2. 抽查 10 个事实——承诺、状态、阶段、等 PO 的事——每个都能对到日志里的一行（10/10）。
3. 每份开着的日志里的 Waiting for PO 都出现在产品卡顶部，一项不漏。
4. 同一状态下用 Haiku 生成 3 次：结构一样，抽查的事实都对（3/3）。
5. 删掉看板文件再生成，内容一样：它不拥有任何东西。
6. PO 看过原型，挑定了形式（35-2），记进第 4 章。

**PBI-61 目标常驻（hook）**——观点：照抄 2.1。

| # | 点 | 定案（谁定） |
| --- | --- | --- |
| 61-1 | 注什么 | 只注承诺原文：产品、Product Goal，加上当前目录看得到的那份开着的冲刺或设计的承诺，三到四句，照上面的读取规则读。写成事实，不写指令。当前目录有两个以上开着的冲刺（或设计）时，不注冲刺那句，只注一行事实「有 N 个冲刺开着，见看板」。（PO 2026-11-13 定内容，Master 定兜底） |
| 61-2 | 什么时候注 | SessionStart（startup、resume、compact）一定注；UserPromptSubmit 注入的频率由测试来定：每轮、每 N 轮、只在承诺变了时。测不出差别，就选最省的那种。（PO 2026-11-13：怕中途遗忘，先测再定） |
| 61-3 | 什么时候不注 | 没有 `scrum/ProductBacklog.md`；脚本出错（静默跳过，exit 0，不挡用户）；用户关掉了它（开关做成环境变量还是设置，由 Developer 定）；冲刺收官、日志归档以后，自然就读不到了。（Master） |
| 61-4 | 跨平台 | 不能要求用户另装 Python 等东西。线索：Claude Code 在 Windows 上要求装 Git Bash，所以 POSIX sh 脚本也许三个平台都能跑——先查文档核实，由 Developer 定。（Master 给线索） |
| 61-5 | Codex | 先查 Codex 插件支不支持 hook：支持，就扩写 `scripts/sync_codex.py` 和 `check_codex.py` 一起同步；不支持，就记一句，Codex 包不带这一层。（PO 2026-11-13：能同步就同步） |
| 61-6 | 写之前 | 先用官方插件（hookify、plugin-dev:hook-development），并查 claude-code-docs MCP，不凭记忆写格式（全局规矩）。（Master） |
| 61-7 | 不做的 | sessionTitle 自动设会话标题，以后再说。（Master） |

**验收标准（61）**
1. 样本项目（产品日志加一份开着的冲刺）里开新会话，注入的内容逐字等于那三句承诺；直接运行 hook 脚本，喂样本输入，比对它的输出。
2. 两个冲刺都开着时，只注产品、Product Goal 两句，加一行「有 2 个冲刺开着，见看板」。
3. 没有产品日志、脚本出错、开关关掉，这三种情况都什么也不注入，exit 0。
4. 在本机 Windows 上实测通过；macOS、Linux 能不能跑，写明依据。没法实测的，记成已知限制。
5. 频率测试：标准先写、单独提交。造一个长会话，最后做一次阶段决定，比较 61-2 的几种频率，每种 Haiku 3 次，看决定里有没有引用目标原文。按结果选定频率，记进第 4 章，并报每轮注入多少 token。
6. 加了 hook 之后，`claude plugin validate --strict` 照样通过；Codex 同步并核对通过（带不带 hook，照 61-5）。

精化结束：Master 2026-11-13 定（PO 授权，见第 4 章）。Developer 起草 How 时如有不清楚的点，先问 Master；没有疑问，就在第 4 章写一行「Developer 复述无疑问」。

## 3. How

先发块 1 给 PO；等他挑的时候做块 2～6（和他的挑选互不依赖）；他挑定后接块 7～9；块 10 最后。做完一块，在该行 Done when 格最前面写「✓ 日期」（读取规则见 2.2）。放行之前不改 `plugins/`、`scripts/`、`.gitignore`、README；块 1、3 的产物在冲刺文件夹里。

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | 产品卡两版原型（35-1、35-2） | 冲刺文件夹 `prototype/` 下手做两个文件：`Board.md`（带 Mermaid 架构图）、`Board.html`（单文件网页）；数据取 main 最新的产品日志和 Sprint 18、19 日志的 Now、Waiting for PO；标「原型，用完即弃」 | 两版都能打开，卡上每个事实对得到日志里的一行；Waiting for PO 写上 35-2；Master 转 PO，PO 挑定后记进第 4 章 |
| 2 | hook 小研究（61-2～61-6） | 第 4 章一段研究记录，每条带出处：SessionStart 的 source、UserPromptSubmit 怎么注入、插件里 hook 怎么声明、Windows 下用什么 shell 跑、环境变量与开关、Codex 支不支持 hook（用 hookify、plugin-dev:hook-development 和 claude-code-docs 查） | 61-2～61-6 的每个未知都有答案，没有凭记忆写的；答案推翻 2.2 的哪一点，当天报 Master |
| 3 | 频率测试的标准 | `tests/frequency-test.md`：臂、场景、探针、判定、过线、夹具（做法见 Key choices）；先写、单独提交 | 单独提交在正式运行之前；Master 看过 |
| 4 | hook 脚本与直接运行测试 | `plugins/ideo-scrum/hooks/` 下的声明和 POSIX sh 脚本（读承诺、开关、出错静默，暂留测试用的模式开关）；样本项目夹具和比对脚本（直接喂输入，不起会话） | 验收 61-1～3 通过；本机 Windows 实测通过；macOS、Linux 写明依据 |
| 5 | 频率测试的跑法与冒烟 | 无头长会话的造法；判定脚本（先拿两份已知结果自测）；一次冒烟，估出单次成本 | 冒烟通过，成本记进第 4 章；太贵先报 Master，不自己降规模 |
| 6 | 频率测试正式跑与选定 | 按块 3 各臂 3 次 Haiku；汇总（行为、内容分两栏，每轮注入多少 token）进第 4 章；原始输出放 `S:\IDEO-Scrum-Archives\sprint-19-board-hook\` | 按过线选出频率（测不出差别选最省的）并改进 hook，删掉测试用的模式开关，61-1～3 重过 |
| 7 | 看板约定与模板 | scrum-kernel `conventions/` 下的 `board.md`（英文，自带给子代理的简报）和 PO 挑的那一版的卡片模板；先给大纲，再给全文审阅（sprint-log 第 11、12 条） | Master 审过；自足：别人的环境里，一个 Haiku 子代理拿着它就能生成 |
| 8 | 看板夹具与核对脚本 | 夹具构造脚本（临时仓库：main 加两个开着的冲刺分支，其中一个带设计）；核对脚本：事实对日志、链接、Waiting for PO 汇总、删掉重建一致 | 核对脚本先自测：一份对的样本过，一份故意弄坏的被抓住 |
| 9 | 看板生成与汇总 | Haiku 子代理对夹具生成 3 次，再对本仓库现状生成一次；汇总进第 4 章 | 验收 35-1～5 通过（35-6 在块 1） |
| 10 | 接入插件并交测试 | overview 第 4 条加一句；scrum-kernel `SKILL.md` 的文件表加一行；`.gitignore`；README 文件地图加两行；`sync_codex.py`、`check_codex.py` 照 61-5；第 4 章对照验收标准写完成情况 | `claude plugin validate --strict` 通过（新增 `hooks/` 属结构变化，再派 `plugin-dev:plugin-validator`，`model: haiku`）；无死链；Codex 同步并核对通过；Master 说可以进测试 |

**Key choices**

- **原型手做、两版并排**：要学的是形式，不是生成；手做最快，两版并排 PO 才有得比（Prototype to Decide：只做一版不算比较）。PO 挑定前不写约定和模板。
- **看板的生成说明做成约定加模板，放 scrum-kernel 的 `conventions/`，不新增技能或命令**（35-6）：PO 助手「维护看板」的入口在 Sprint 18 的 60；新技能或命令要写新描述、重跑触发测试、改 Codex 的适配，而本冲刺一个描述也不改。约定自带简报，Haiku 子代理拿着它就能生成；PO 要一句话命令，另开 PBI。
- **hook 用 POSIX sh、开关用环境变量**：都是 2.2 的线索，块 2 查文档核实后才定，核实不了就停下问 Master。`sync_codex.py` 只复制四个内核和角色命令，`hooks/` 不在内，所以内核里的文件不链接到 `hooks/`。
- **读取规则只写一处**：写在看板约定里，hook 脚本的头注释指向它、照同一规则实现；66 的格式再动，两处一起改。
- **频率测试**：五臂各 3 次 Haiku——不装 hook（对照）、只 SessionStart、再加每轮、再加每 N 轮、再加只在承诺变了时。一个场景：长会话中途由脚本把 Sprint Goal 改一次，结尾做一次阶段决定，判定决定里有没有逐字引用当前的目标。这样「忘了」和「过期」都测得到，「只在变了时」才和「只在开会话与压缩后」分得开。「决定前先引用目标原文」用夹具里的一行代替（66-5 的条文不一定已合进来），让各臂的差别只来自 hook。
- **看板验收用固定夹具**，真实状态另做一次演示：Sprint 18 可能在我测之前就收官合入，「main 加两个分支」就没有了。
- **合并顺序与模型通道**：只改自己的行；Sprint 18 先合入 main 后，先把 main 合进本分支，再跑块 10 的校验，66 的读取规则（含 66-8 的措辞）以合并后的为准再核一遍。子代理、测试显式写 `model: haiku`，报告太浅或有错才升一档并告诉 Master；无头测试用 `claude-magpie -p`（PO 2026-11-13 用户级规定），冒烟时核实。

**Risks and open points**

- **66 的格式还可能动**：Sprint 18 没收官前不算最终，合并后重核（见合并顺序）。
- **hook 平台细节没法全测**：本机只有 Windows；macOS 自带 bash 3.2 和 BSD 工具。本机实测，其余写依据，记成已知限制。
- **长会话测试的成本和造法没把握**：块 5 先冒烟；太贵先报 Master。
- **「每 N 轮」「承诺变了才注」要在 hook 里存一点状态**（轮数、上次的指纹）：放系统临时目录、按会话编号命名，读写失败也静默；hook 里只有这一处状态，看板不存状态；选定的若不需要，就不带。
- **Haiku 生成看板可能逐字不稳**：模板填空、简报写死「承诺逐字照抄」，核对脚本兜底；3 次都不稳，先升一档再回头报 Master。
- **网页版的 Mermaid 要联网加载**（若 PO 选网页）：离线时架构图出不来；退路是同页放 Mermaid 源码；正式版是否内嵌另议。

Go-ahead: 尚未放行。（拟：本分支上提交；合并、打 tag、发版在 Review 决定；不推送。）

## 4. Increment notes

- 分支名没照约定 1，因为是原生 worktree 生成的名字；收官时 tag 用文件夹名 `sprint-19-board-hook`。
- **PO 授权（2026-11-13，原话）**：「其实精化我一般让你做的，你的上下文最多，其实你可以详细的告诉他们得，怎么写精化啥得对不对，我把整个权限全放开了，也就是告诉你，后面你的权限拉满，除非必要，我来做决定，否则你都可以直接决定」。所以本冲刺的精化定案、精化结束、How 的审阅和放行都由 Master 做（overview 第 12 条：PO 可以把阶段决定交给 Master）。下面这些仍回到 PO：改 Product Goal；推送、发布等对外动作；取消冲刺；推翻 PO 已经说过的话；看板的形式（35-2）。
- 日志由 Master 开：Developer 正要开时，PO 交代精化由 Master 做，Master 就把开日志和精化一起写了。
- **Developer 复述无疑问**（2026-11-13）：其中「冲刺卡的完成情况读哪里」一处先问了 Master，答复（✓ 标记、路线图只放产品日志里的状态）已补进 2.2 的接口和 35-3。
- 第 5 章标题：开日志时漏了（模板要求每个标题都留着），Developer 2026-11-13 补上；Sprint 18 的日志同样没有这一章。

## 5. Test
