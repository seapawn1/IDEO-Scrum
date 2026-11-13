# Sprint Backlog — Sprint 19 (board-hook)

> Started: 2026-11-13 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: worktree-golden-orbiting-bachman | Product Owner: SeaPawn | Scrum Master: 会话 IDEO # [master]-[main]-[support sprint] | Developer: Claude Code（会话 IDEO # [developer]-[sprint-19]-[do sprint 19]，golden-orbiting-bachman）
> Now: Test：Master 审过，等收官 · Master 2026-11-13 放行 How（PO 授权，见第 4 章）
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
| 1 | 产品卡两版原型（35-1、35-2） | 冲刺文件夹 `prototype/` 下手做两个文件：`Board.md`（带 Mermaid 架构图）、`Board.html`（单文件网页）；数据取 main 最新的产品日志和 Sprint 18、19 日志的 Now、Waiting for PO；标「原型，用完即弃」 | ✓ 2026-11-13　两版都能打开，卡上每个事实对得到日志里的一行；Waiting for PO 写上 35-2；Master 转 PO，PO 挑定后记进第 4 章 |
| 2 | hook 小研究（61-2～61-6） | 第 4 章一段研究记录，每条带出处：SessionStart 的 source、UserPromptSubmit 怎么注入、插件里 hook 怎么声明、Windows 下用什么 shell 跑、环境变量与开关、Codex 支不支持 hook（用 hookify、plugin-dev:hook-development 和 claude-code-docs 查） | ✓ 2026-11-13　61-2～61-6 的每个未知都有答案，没有凭记忆写的；答案推翻 2.2 的哪一点，当天报 Master |
| 3 | 频率测试的标准 | `tests/frequency-test.md`：臂、场景、探针、判定、过线、夹具（做法见 Key choices）；先写、单独提交 | ✓ 2026-11-13　单独提交（`4e26b73`）在正式运行之前；Master 看过（通过，三处都同意） |
| 4 | hook 脚本与直接运行测试 | `plugins/ideo-scrum/hooks/` 下的声明和 POSIX sh 脚本（读承诺、开关、出错静默，暂留测试用的模式开关）；样本项目夹具和比对脚本（直接喂输入，不起会话） | ✓ 2026-11-13　验收 61-1～3 通过；本机 Windows 实测通过；macOS、Linux 写明依据（见第 4 章「块 4」） |
| 5 | 频率测试的跑法与冒烟 | 无头长会话的造法；判定脚本（先拿两份已知结果自测）；一次冒烟，估出单次成本 | ✓ 2026-11-13　冒烟通过，成本记进第 4 章；太贵先报 Master，不自己降规模（成本见第 4 章「块 5」，已报 Master） |
| 6 | 频率测试正式跑与选定 | 按块 3 各臂 3 次 Haiku；汇总（行为、内容分两栏，每轮注入多少 token）进第 4 章；原始输出放 `S:\IDEO-Scrum-Archives\sprint-19-board-hook\` | ✓ 2026-11-13　按过线选出频率（测不出差别选最省的）并改进 hook，删掉测试用的模式开关，61-1～3 重过（选定 A4；汇总见第 5 章；最终 hook 在真实会话里整场跑一次：注入 3 次、压缩发生、P1 P2 都引用当前目标） |
| 7 | 看板约定与模板 | scrum-kernel `conventions/` 下的 `board.md`（英文，自带给子代理的简报）和 PO 挑的那一版的卡片模板；先给大纲，再给全文审阅（sprint-log 第 11、12 条） | ✓ 2026-11-13　Master 审过（`1c2cdb2`，通过）；自足——别人的环境里，一个便宜模型的子代理拿着它就能生成——在块 9 验证 |
| 8 | 看板夹具与核对脚本 | 夹具构造脚本（临时仓库：main 加两个开着的冲刺分支，其中一个带设计）；核对脚本：事实对日志、链接、Waiting for PO 汇总、删掉重建一致 | ✓ 2026-11-13　核对脚本先自测：一份对的样本过，一份故意弄坏的被抓住（48 条全过：两个场景各一份对的页过、18 种改坏的页都被抓到） |
| 9 | 看板生成与汇总 | Haiku 子代理对夹具生成 3 次，再对本仓库现状生成一次；汇总进第 4 章 | ✓ 2026-11-14　验收 35-1～5 通过（35-6 在块 1）：夹具 A、B 各 3/3，本仓库现状批 4 为 2/2，事实集合相同；汇总在第 5 章；生成用的是 magpie 的便宜模型（非 Haiku），手抄丢字的限制见第 4 章 |
| 10 | 接入插件并交测试 | overview 第 4 条加一句；scrum-kernel `SKILL.md` 的文件表加一行；`.gitignore`；README 文件地图加两行；`sync_codex.py`、`check_codex.py` 照 61-5；第 4 章对照验收标准写完成情况 | ✓ 2026-11-14　`claude plugin validate --strict` 通过（新增 `hooks/` 属结构变化，再派 `plugin-dev:plugin-validator`，`model: haiku`）；无死链；Codex 同步并核对通过；Master 说可以进测试——前三项都做完了（`--strict` 通过、validator 无必改项、`check_codex.py` 内容/链接/导航 0 错，见第 4 章「块 10」），Master 2026-11-14 审过块 8～10、说可以进测试（PO 授权） |

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

Go-ahead: Master 2026-11-13 放行（PO 授权，见第 4 章）：本分支上提交；合并、打 tag、发版在 Review 决定；不推送。

## 4. Increment notes

- 分支名没照约定 1，因为是原生 worktree 生成的名字；收官时 tag 用文件夹名 `sprint-19-board-hook`。
- **PO 授权（2026-11-13，原话）**：「其实精化我一般让你做的，你的上下文最多，其实你可以详细的告诉他们得，怎么写精化啥得对不对，我把整个权限全放开了，也就是告诉你，后面你的权限拉满，除非必要，我来做决定，否则你都可以直接决定」。所以本冲刺的精化定案、精化结束、How 的审阅和放行都由 Master 做（overview 第 12 条：PO 可以把阶段决定交给 Master）。下面这些仍回到 PO：改 Product Goal；推送、发布等对外动作；取消冲刺；推翻 PO 已经说过的话；看板的形式（35-2）。
- 日志由 Master 开：Developer 正要开时，PO 交代精化由 Master 做，Master 就把开日志和精化一起写了。
- **Developer 复述无疑问**（2026-11-13）：其中「冲刺卡的完成情况读哪里」一处先问了 Master，答复（✓ 标记、路线图只放产品日志里的状态）已补进 2.2 的接口和 35-3。
- 第 5 章标题：开日志时漏了（模板要求每个标题都留着），Developer 2026-11-13 补上；Sprint 18 的日志同样没有这一章。
- **块 1 进展**（2026-11-13）：两版产品卡原型已做好，在 `prototype/`（`Board.md`、`Board.html`）。版式手排，数据由一次性脚本（不入库）从真实日志填入：产品日志取 `main` @ 74b929b，Sprint 18 取分支 `claude/youthful-payne-b1e139` 已提交的 df88e67，Sprint 19 取工作区；产品卡的内容和顺序照 35-3，另放了两张冲刺卡的摘要（承诺、Now、等 PO），让链接有去处。网页版用 Edge 无头渲染核对过：联网时 Mermaid 出图，架构图占一屏，网页里可折叠。Waiting for PO 已写上 35-2，等 Master 转 PO 挑；PO 挑定后记在这里并给块 1 标 ✓。
- **35-2 定了：网页版（B）**（Master 2026-11-13；PO 把形式和版式都交给 Master 定，原话：「可以，这些你可以来决定」）。理由：看板不提交，Markdown 能进 git、能看差异的长处用不上；网页更接近 PO 要的卡片化。版式：块的顺序不动，照 PO 的卡片设计——承诺在上，架构图在中，条目在下；「等 PO 拍板」仍放最上面；**架构图默认收起、点一下展开**，条目不被挤到下面；离线时显示 Mermaid 源码（退路）。网页生成时容易走样，由块 7 的模板和块 8 的核对脚本兜。给块 7 的两条：模板里架构图用 `<details>` 且默认不加 `open`；原型里的 `Board.md` 和默认展开的写法都不带进模板。块 1 标 ✓，Waiting for PO 改回 None。
- **读法上的发现，记给块 7**：条目分组靠产品日志状态列里「（主线）」「（副线）」这样的字，别的项目未必有这种写法——看板约定要写明「照状态列原文分组，没有括号标注的归其他」，状态链到冲刺卡靠「在 Sprint NN」。
- **块 2：hook 小研究**（2026-11-13，Developer）。用了 plugin-dev:hook-development、查了 claude-code-docs（页名写在括号里），另在本机做了三次一次性探针（探针插件在仓库外；Claude Code 2.1.323，Windows 10，经 claude-magpie）。
  - **注入口（61-1）**：SessionStart、UserPromptSubmit 的纯文本 stdout，或 `hookSpecificOutput.additionalContext`，都进模型上下文；模型看到的是一行「`SessionStart:startup hook success: <原文>`」（探针实测，中文原样过去、没有乱码）。官方建议写成事实、不写指令；超过一万字符会被转成文件，我们只有几句，碰不到（hooks 页「Add context for Claude」）。
  - **什么时候注（61-2）**：SessionStart 的来源有 `startup`、`resume`、`clear`、`compact`、`fork`；resume、fork 会重新跑；compact 时重新跑，输出加进压缩后的上下文，而早先注入的内容会随对话一起被压缩（hooks 页「SessionStart」；context-window 页「What survives compaction」）。所以 SessionStart 不写 matcher、五种来源都注，「只在开会话与压缩后」这一档不用另写逻辑。UserPromptSubmit **不只在用户打字时触发**：定时任务、后台子代理回报、别的会话发来的跨会话消息也触发（hooks 页「UserPromptSubmit」）——「每轮」在 Master 与 Developer 来回发消息的会话里会很勤；它默认 30 秒超时，超时只丢弃本次输出、不挡提示。
  - **声明与环境（61-3）**：插件用 `hooks/hooks.json`，顶层 `"hooks"` 键，形状同 settings；hook 进程拿得到 `CLAUDE_PLUGIN_ROOT`、`CLAUDE_PLUGIN_DATA`、`CLAUDE_PROJECT_DIR`；hooks 在会话开始时加载，改了要重开（plugins 页「Hooks」）。没有单条 hook 的开关，只有 `disableAllHooks`（全关）（hooks 页「Disable or remove hooks」）；所以脚本自己读一个环境变量当开关，用户在 settings 的 `env` 或 shell 里设（环境变量会传进 hook，探针实测）。不用 `userConfig`：它在安装时弹配置对话框（plugins 页「When the configuration dialog appears」）。工作目录：hook 在会话当前目录跑，`$PWD` 就是它，stdin 的 `cwd` 同值，`CLAUDE_PROJECT_DIR` 是会话起点（探针实测，worktree 会话里都是 worktree 根）；脚本从 `$PWD` 往上找 `scrum/ProductBacklog.md`，找不到再试 `CLAUDE_PROJECT_DIR`。本 worktree 的日志是 LF（0 行带 `\r`），别的 Windows 检出可能是 CRLF，脚本照旧去掉 `\r`，块 4 用 CRLF 样本测。
  - **跨平台（61-4）——推翻了 2.2 的线索**：2.2 写「Claude Code 在 Windows 上要求装 Git Bash」，已过时：Git for Windows 现在是可选的，没有它时 hook 默认走 PowerShell，写给 bash 的命令会失败（setup 页；hooks 页「Failed hooks on Windows without Git Bash」）。探针实测三种情形：① 设了 `CLAUDE_CODE_GIT_BASH_PATH`、Git Bash 找得到：`sh "…"; exit 0` 在 Git Bash 里正常跑；② 找不到（本机 Git for Windows 装在 `E:\GIT\Git`，无头子进程默认找不到）：Claude Code 改在 PowerShell 里跑同一条命令，`sh` 在 PATH 上就照样跑，另给一条提示「Git Bash wasn't found…」；③ PowerShell 下根本没有 `sh`：命令报错，但 `; exit 0` 让退出码为 0，hook 静默无效（PowerShell 一行直测）。**定案（Developer）**：声明写成 shell 形式 `sh "${CLAUDE_PLUGIN_ROOT}/hooks/<脚本>"; exit 0`——用 `sh` 调、不靠可执行位（Windows 上提交的文件没有 x 位）；脚本只用 POSIX sh 与 sed、grep、tr、printf、head、ls，这些 macOS（BSD 工具）、Linux（dash）都有；Windows 没装 Git for Windows 的用户，hook 不生效，记成已知限制（Claude Code 自己会提示装 Git for Windows）。macOS 没法实测，写依据；Linux 用本机 WSL（Ubuntu-24.04，`/bin/sh` 是 dash）跑一遍。
  - **Codex（61-5）——支持**（Codex 的 hooks 文档页，经 WebFetch 读取；本机 codex-cli 0.167.2 的 `codex features list` 里 `hooks` 为 stable、已开，二进制里有 `hooks/hooks.json`、`CLAUDE_PLUGIN_ROOT` 字样，互相印证）：插件根目录的 `hooks/hooks.json` 默认被找到；Codex 同时设 `PLUGIN_ROOT`、`CLAUDE_PLUGIN_ROOT`、`CLAUDE_PLUGIN_DATA`；SessionStart 的来源同样含 `compact`；纯文本 stdout 作为开发者上下文加入；**用户要先在 `/hooks` 里审阅并信任插件的 hook 才会跑，插件更新改了脚本要重新审阅**；Windows 上用哪个 shell，文档没写。**定案**：同步。`scripts/sync_codex.py` 现在只复制四个内核和角色命令，要加一段复制 `hooks/`，`check_codex.py` 同样核对；块 10 在本机 Codex 里试一次，试不成就记成未实测。
  - **Master 同意**（2026-11-13）：上面的 61-4 定案（shell 形式加 POSIX sh，没装 Git for Windows 的 Windows 用户不生效、记成已知限制，README 里怎么写交 PBI-62）、61-5 定案（Codex 同步 `hooks/`；Codex 要用户先在 `/hooks` 信任才会跑，交 62、64 写进说明）、测试通道（用 magpie 的便宜模型，汇总里写「magpie 的便宜模型，非 Haiku」，不写模型名和提供方；结果落在边界上才补真 Haiku，补之前先报 Master，由它问 PO）。`CLAUDE_CODE_GIT_BASH_PATH`、`--resume` 两条无头测法，Retro 时挑进 CLAUDE.md。
  - **给块 3、5 的发现（测法）**：① 无头多轮要用 `--input-format stream-json` 在同一进程里发多条消息，且要等上一条的 `result` 事件再发下一条——一次发三条，后两条并成一轮（实测：3 条消息、2 轮、UserPromptSubmit 触发 2 次）。② 同一进程里 SessionStart 只触发一次；若用 `--resume` 接力，每个新进程都触发一次 SessionStart（resume），「只 SessionStart」一档就变成每轮都注，测不出差别，所以不用 `--resume`。③ `--include-hook-events` 在流里给出每个 hook 的 `output`、`exit_code`，注入了什么可以直接核对，不靠模型复述。④ claude-magpie：Git Bash 里要写 `claude-magpie.cmd`；认 `--plugin-dir`、`--input-format stream-json`、`--tools ""`；但 `--model haiku` 实际跑的是 magpie 自己配的另一个便宜模型（流里的 `modelUsage` 与 init 事件可查；stderr 有 unrecognized_model 提示），不是 Haiku；模型名是提供方的设置值，不写进仓库。⑤ 无头子进程要设 `CLAUDE_CODE_GIT_BASH_PATH`（指向本机 Git 的 `usr\bin\bash.exe`），否则 hook 走 PowerShell，和多数用户的路径不同。⑥ `/compact` 在无头流里可当一条用户消息发：流里出现 `compact_boundary` 事件，SessionStart 以来源 `compact` 再触发一次，压缩后上下文里只剩那次 compact 的注入，早先 startup 的注入只在摘要里被提到（实测）；`/compact` 不触发 UserPromptSubmit。所以块 3 的场景里能确定地压缩一次，不必凑出 10 万 token 的会话（`--autocompact` 最小 100K，触不及）。
- **块 3 通过**（Master 2026-11-13）：两个探针加一次 `/compact`、过线与选定规则、开着工具，三处都同意，标准不改。Master 补一层：真实使用里 Sprint Goal 很少中途改（目标固定），P1 主要用来比 A1 与 A4 谁更划算，照规则「过线臂里注入最少」已能分出；各臂结果差不多就如实记「测不出」并照规则选最省——这也是有用的结论：约定（66-5）是主力，hook 只补位；各臂查了几次日志一起报。
- **宿主变量与测试通道**（2026-11-13，Master 同意，留给 Retro）：无头子进程不能继承宿主的环境。本机宿主环境里有 `CLAUDE_CODE_AUTO_COMPACT_WINDOW`（盖过 `--autocompact`，改变压缩时机）、`CLAUDE_CODE_MESSAGING_SOCKET`、`CLAUDE_CODE_MESSAGING_TOKEN`（跨会话消息）、`CLAUDE_CODE_SESSION_ID` 等；Sprint 18 又发现宿主会设模型重映射（`ANTHROPIC_DEFAULT_*_MODEL`）和模型目录。两个冲刺统一用白名单环境：只带 `SystemRoot`、`PATH`、`USERPROFILE`、`APPDATA`、`LOCALAPPDATA`、`HOMEDRIVE`、`HOMEPATH`、`ComSpec`、`PATHEXT`，加 `TEMP`、`TMP`（每次全新的空目录）、`CLAUDE_CODE_GIT_BASH_PATH`、`MSYS_NO_PATHCONV`；hook 的开关这类额外变量只靠驱动脚本的 `--env` 明着给。核对：我这条通道里没有重映射变量；白名单下 `--model haiku`、`--model sonnet`、不写 `--model` 三次报告的是同一个模型，且与块 2 探针（继承环境）的相同——所以那个模型是 magpie 自己固定的映射，不是宿主造成的。
- **块 4：hook 脚本与直接运行测试**（2026-11-13，Developer）。产出：`plugins/ideo-scrum/hooks/hooks.json`、`commitments.sh`；`.gitattributes`（`*.sh` 强制 LF——Windows 上 `core.autocrlf=true` 会把脚本写成 CRLF，sh 遇到 CR 是语法错误）；`tests/hook_cases.py`（直接喂输入、不起会话）。
  - **脚本**：读取规则照 66（overview 第 17 条）：首格 `Commitment` 或 `承诺` 的一行小表，节标题认种类；从 `$PWD` 往上找 `scrum/ProductBacklog.md`，找不到再试 `CLAUDE_PROJECT_DIR`（反斜杠先转成斜杠）；开着的冲刺、设计 = `scrum/sprint-*/SprintBacklog.md`、`scrum/design-*/DesignBacklog.md`；只有一个冲刺（设计）时注它的承诺，两个以上时只注一行「有 N 个冲刺开着，见看板」；模板没填的占位（`<…>`）跳过；标签语言跟日志的首格走（`承诺` 用中文标签，`Commitment` 用英文）。输出是三到四行纯文本，Claude Code 把它包成「`SessionStart:startup hook success: …`」放进上下文。开关 `IDEO_SCRUM_COMMITMENTS=off`；出错、缺文件、缺工具一律什么都不输出、退出码 0。测试期还留着模式开关 `IDEO_SCRUM_COMMITMENTS_MODE`（`start`、`every`、`every-n`、`changed`）与 `_N`，状态文件放 `CLAUDE_PLUGIN_DATA` 下、按会话号命名；块 6 选定频率后连同这一段一起删掉。声明（shell 形式）：`sh "${CLAUDE_PLUGIN_ROOT}/hooks/commitments.sh"; exit 0`，超时 10 秒。
  - **结果**：本机 Windows（Git Bash 的 sh）28/28；WSL Ubuntu 24.04 的 dash，awk 分别用 gawk 5.2、mawk，各 26/26（少的两条只在 Windows 上有意义：反斜杠路径、清空 PATH）。变异检查：六种改坏的脚本，五种被本机测试抓到；「不去 CR」一种本机抓不到——MSYS 的 awk 自己吃掉 `\r`——但 WSL 抓到，所以去 CR 这一步在 Linux 上必需。`claude plugin validate --strict plugins/ideo-scrum` 通过（hooks.json 能加载）。真实会话（块 5 冒烟）里，startup 的第一次注入逐字等于样本项目的三句承诺，压缩后那次注入是换过的目标。
  - **macOS：没法实测**。依据：只用 POSIX sh 和 awk、sed、tr、cksum、dirname、basename、mkdir，用法限在 POSIX 的子集；Linux 上 dash 配 gawk、mawk 两种 awk 都过；BSD awk 没试，记成「未在 macOS 上实测」。已知限制：Windows 没装 Git for Windows 的用户 hook 不生效（61-4 的定案）。
- **块 5：频率测试的驱动与冒烟**（2026-11-13，Developer）。驱动与判定都在 `tests/frequency_test.py`（`selftest`、`smoke`、`run`、`judge`、`tokens`）；判定脚本先拿 16 条已知结果自测，全过（完整引用算引用、Markdown 引用的标点不同仍算、旧目标算过期、改写不算引用、读过日志与没读过分得开、对照臂真的没有注入、其他插件的 hook 不算我们的）。冒烟：A2 整场一次，15 个提示加一次压缩，status ok，注入 16 次（预期 16），压缩发生；P1、P2 都逐字引用了当前目标（P1 另读了一次日志，P2 没读）。成本：228 秒；输入约 21 万 token（其中缓存读约 20 万）、输出约 4 千；Claude Code 自己估的费用是 0.40 美元，但模型不被识别，这个估算不可信。照此推：正式跑 15 次，串行约 1 小时、输入约 340 万 token；并行 3 个约 20 分钟。每次注入 172 个字符。
- **块 7：看板约定与模板**（2026-11-13，Developer；大纲 Master 通过，三点补充已照改，全文直接在分支上交 Master 审 diff）。产出：`plugins/ideo-scrum/skills/scrum-kernel/conventions/board.md`（16 条，英文，自带给子代理的简报）与 `board-template.html`。
  - 照 Master 的意见：① 分组——项目自己有分组（状态格里的括号词）就照它分，没有就按 product-log 第 10 条的状态值（在冲刺里、在设计里、待选），其余归 Other，不写死本仓库的词；② 空状态——「等 PO」条、冲刺、设计各一行；③ 第 5 条把 Now、Waiting for PO、承诺、完成标记各自写在哪一条列全（overview 第 17 条、sprint-log 第 9、22 条、design-log 第 24 条、ideo-log 第 4 条），只指过去不重写；④ 「生成物不必进版本控制，进不进由项目定」，本仓库自己在 `.gitignore` 加了 `/scrum/Board.html`；⑤ 步骤只写角色和步骤，不写工具用法，「用 git 读别的分支上已提交的日志」只作说明。这些条号是 66 交付之后的；Sprint 18 合进 main 之前，本分支上的旧文可能对不上，合并后再核（块 10）。
  - 模板：一份可直接复制的 HTML，槽位写成 `{{…}}`，重复的块标 REPEAT；每个事实带 `data-fact` 标记（13 种，列在模板顶部注释里），块 8 的核对脚本按它逐项对日志；地图用 `<details>` 默认收起，第一次打开才画——藏着的元素量不出尺寸，开页就画会画坏；Mermaid 源码另放在 `details.src` 里，离线或画失败就自动展开；事实里的 `<`、`>`、`&` 要转义（Mermaid 标签里常有 `<br/>`），模板与第 13 条都写了。
  - 随手先做了块 10 的三项：scrum-kernel `SKILL.md` 文件表加两行（导航入口）、overview 第 4 条加看板一句、`.gitignore`；块 10 剩下 README、Codex 同步与核对、校验。
  - 还没验的：模板自足、Haiku 级子代理拿着它就能生成——块 9。
- **块 6 选定 A4**（Master 2026-11-13 确认读法：「仍带 SessionStart」已经排除 A0；带 SessionStart 的 A1～A4 里过线的只有 A2 与 A4，最省的是 A4，A1 没过线选不上）。结论三件：① 选定 A4——SessionStart（startup、resume、clear、compact、fork）一律注，UserPromptSubmit 只在承诺和本会话上次注入的不同时才注；目标没变时它和 A1 一样省（一次开会话、每次压缩各一次），目标变了也不留过期的；② **约定是主力，hook 补位**：A0 不注也过线，模型有「决定前引用 Sprint Goal 原文」这条规矩时自己会去读日志，压缩摘要又带着原文；③ **每次注入约 96 token**（样本三句承诺 172 字符）。hook 已改成 A4，测试期的模式开关（`IDEO_SCRUM_COMMITMENTS_MODE`、`_N`）已删，只剩用户的开关 `IDEO_SCRUM_COMMITMENTS=off`；状态是会话号命名的小文件（只存上次注入文本的校验和），放在 `CLAUDE_PLUGIN_DATA` 下，开会话时只留最新的 200 个；写不了状态就照注（几行字，不挡事）。61-1～3 的直接运行测试重跑：本机 31/31，WSL 的 dash 配 gawk、mawk 各 29/29；九种改坏的脚本全被抓到（「不去 CR」那种在 WSL 里抓到）。
- **magpie 通道的两条（进 Retro）**：① 默认是 `bypassPermissions`，`--allowedTools` 的白名单不生效，`--tools` 也管不住 MCP 工具（文档与图片 MCP 的工具仍在）；② 加了 `--permission-mode dontAsk` 也不够——用户 settings 里有宽泛的 allow 规则，照样放行（块 9 第二批里模型自己写了 Python 生成脚本，没被拦）；要让白名单真生效，得再加 `--setting-sources project,local` 把用户 settings 挡在外面（块 9 第三批起这样跑）。Sprint 18 核对过它那边的 init（工具只有四项、用了 `--strict-mcp-config`），结果不受影响。
- **块 7 通过**（Master 2026-11-13，审的是 `1c2cdb2` 的 diff）：16 条都照大纲，细节也认可（同一份日志在几个分支上以最新提交为准；别的分支上的日志不给链接、改写分支名和提交号；设计日志的 2.1 Map、3.1 Solution 节号对过模板）；两个设计选择（`data-fact` 标记、地图首次打开才画加离线展开源码）同意；条号等 Sprint 18 合入后再核。
- **块 8：看板夹具与核对脚本**（2026-11-13，Developer）。`tests/board_check.py`（`selftest`、`fixture`、`check`、`compare`、`facts`）。
  - **夹具**：临时 git 仓库，中文产品日志（承诺、带 `<br/>` 的地图、五条 PBI 带括号词状态、一条已完成的 PBI）、一份已收官的冲刺日志放在 `scrum/documents/`（页面上不许出现）；两个开着的冲刺各在自己的分支上（Sprint 01 中文、Sprint 02 英文，一个等 PO、一个 `None`），设计日志与 IDEO 日志在 Sprint 02 的分支上。场景 A：工作区在 main，所有开着的日志只在分支上；场景 B：工作区在 Sprint 01 的分支上，Now 行有一处没提交的改动——该冲刺要读工作区。
  - **核对**：脚本自带一份独立的日志读法，把每份开着的日志读成「事实」，再对页面：① 每个 `data-fact` 标记里的文字，都要是日志里的原文（承诺、Now、等 PO、阶段、工作块与它的 ✓、地图、方案标题、来源的分支与提交号、条目的标题状态规模）——日志没有的事实不许出现；② 该有的都在：每份开着的日志一张卡、IDEO 日志在它服务的卡上占一行、每个阶段与工作块的完成标记对；③ 顶部「等 PO」条里恰好是各日志的 Waiting for PO，不多不少，`None` 的不列；④ 条目分组与项目自己的分组一致（括号词分组、其余归 Other），已完成和已收官的不许出现；⑤ 链接都打得开（页内 id、工作区里的文件），工作区里有的日志卡上要有链接；⑥ `compare`：同一状态下做的两页，事实集合相同（不算生成时间）。
  - **自测**：两个场景各一份写对的参考页（只在自测里用）要过；各 18 种改坏的页要被抓到（改一个字的承诺、改写 Sprint Goal、删掉一条等 PO、改写 Now、翻转完成标记、死链、页内死链、改状态、露出已完成条目、改地图、地图里的 `<br/>` 没转义、来源提交号不对、卡片的 id 不对、两个分组并成一个、少了 IDEO 一行、编造一个事实、阶段标记挪错、给 `None` 的日志编一条等 PO）；还有 `compare` 的两条。共 48 条，全过。
  - **给块 9 的约束**：生成要读别的分支上已提交的日志，模型得能跑 git 的只读命令；测试通道里给 `Bash`，但只放行 `git show`、`git branch`、`git for-each-ref`、`git ls-tree`、`git rev-parse`、`git log` 这几类前缀，加 `Read`、`Grep`、`Glob`、`Write`；工作目录是全新的临时夹具仓库，写文件也只落在里面。这一条偏离了 CLAUDE.md 的「工具限 Read、Grep、Glob、Skill」，理由是看板的活本来就要读分支。
- **66 接口已交付**（Master 2026-11-13，Sprint 18 分支提交 `1e347b4`）：和 2.2 的读取规则一致；细节：承诺的格式只在 overview 第 17 条写定（首格 `Commitment`，中文日志写 `承诺`，第二格原文不加粗，只存一份，靠节标题认种类）；冲刺、设计、IDEO 三种日志头部 `> Now:` 后紧跟 `> Waiting for PO:`，没有写 `None`，产品日志没有这两行；IDEO 日志的 `For` 写它服务的日志的相对路径；工作块完成标记写在 sprint-log 第 9 条。Sprint 18 合进 main 以后，先把 main 合进本分支，再按合并后的原文核一遍。块 4 的 hook 脚本和块 8 的核对脚本都照这套读。
- **块 10：接入插件与交测试**（2026-11-13～14，Developer）。① **合并 main**（Sprint 18 收官 `e1fa560`）进本分支：无冲突。**条号复核**：board.md 第 5、6 条引用的 overview 第 17 条（承诺格式）、sprint-log 第 9 条（✓）与第 22 条（Now、Waiting for PO）、design-log 第 24 条、ideo-log 第 4 条、product-log 第 10 条，都和合并后的原文对上；hook 读的节标题（1.1 Product、1.2 Product Goal、1.1 Sprint Goal、1.2 Design goal）与 overview 第 17 条一致。② **Codex**：`scripts/sync_codex.py` 加了复制 `hooks/`，`check_codex.py` 核对同样的文件，自测里加了「hook 脚本被改、被删都抓得到」；同步后包里 99 个文件，内容、链接、导航 0 错。包能装进隔离的 Codex 目录，`hooks/hooks.json` 到了插件缓存；**hook 的触发没法不调模型验证**（`codex debug prompt-input` 渲出的提示里有技能、没有 hook 的输出，它不跑 hook），Codex 又要用户先在 `/hooks` 里信任——记成「触发未在 Codex 里实测」，交 62、64 写进说明。③ **校验**：`claude plugin validate --strict plugins/ideo-scrum` 通过；结构变了（多了 `hooks/`），派了 `plugin-dev:plugin-validator`（`model: haiku`）：无必改项（hooks.json 格式、脚本 `sh -n` 与引号、SKILL.md 表里的引用与条号都对，四个描述都在 1024 字符以内，ideo-kernel 1023，贴着线）。④ README 文件地图加了 hooks、`.gitattributes`、看板约定与模板、Codex 包的 `hooks/`；版本号没动（发不发版在 Review 定）。
- **给 Retro 的素材**（Developer，原则形式，进不进 CLAUDE.md 与记忆由 Master 与 PO 定）：
  1. **测试通道**：magpie 默认 `bypassPermissions`，`--allowedTools` 白名单不生效；加 `--permission-mode dontAsk` 仍被用户 settings 里宽泛的 allow 规则放行；要真限制，得再加 `--setting-sources project,local`；`--tools` 管不住 MCP 工具。子进程用白名单环境，不继承宿主变量——`CLAUDE_CODE_AUTO_COMPACT_WINDOW` 会盖过压缩设置，`CLAUDE_CODE_MESSAGING_*` 与 `CLAUDE_CODE_SESSION_ID` 是会话通道，模型重映射是 Sprint 18 的发现；Git Bash 装在非默认位置时，要设 `CLAUDE_CODE_GIT_BASH_PATH`，否则 hook 走 PowerShell 回退。
  2. **测多轮与压缩**：同一进程里用 `--input-format stream-json` 一条一条发，等上一条的 `result` 再发下一条（一次发多条会并成一轮）；`--resume` 接力会让每个新进程都触发 SessionStart，「只在 SessionStart 注入」的臂就变成每轮注入；`/compact` 可当用户消息定点压缩一次；`--include-hook-events` 的流里有每个 hook 的输出，核对臂用它，不靠模型复述。
  3. **量 token 要配对**：文档 MCP 服务开场是否连上，会让同一个提示的输入差约 1300 token；同一提示的两个臂要拿连接状态相同的一对来减。
  4. **标准的选定规则要把限定词写清**：「选最省的过线臂」，要写成「在带 SessionStart 的过线臂里」；字面读法含 A0 就会选出一个自己没过线的配置（Master 一句话解开）。判定「过期」时，看明细比看计数重要：模型其实是发现了不一致并按日志做了对的决定，计数里它算「过期」。
  5. **hook 的做法**：声明用 shell 形式 `sh "…"; exit 0`（不靠可执行位，PowerShell 回退下找不到 `sh` 也静默）；`.gitattributes` 让 `*.sh` 保 LF；MSYS 的 awk 自己吃掉 `\r`、Linux 的不吃，去 CR 要在 Linux（WSL）里测才抓得到；不要用 `find`（Windows 自带一个同名的 `find.exe`）；注入的文字会留在上下文里，承诺改了就成噪音，所以只在变了时再注；没有注入的好处可测时，约定（66-5）才是主力。
  6. **检查脚本**：独立读日志的脚本，路径要锚定在顶层（用后缀匹配，会把测试夹具目录里的假日志当成开着的），也别假定编号的写法（Sprint 18 的工作块编号是 `H1`）；夹具要放真仓库里才有的形状（嵌套的假日志、非数字编号、没有等 PO 时的空状态），并先拿真仓库的状态过一遍。
  7. **便宜模型逐字抄长文会丢字**：地图里一个 `-` 没了，`<br/>` 被删——逐字规矩要配核对脚本；约定里写「长文机械拷贝、写完读回对照」；权限放宽时模型会自己写脚本拷贝，没丢字，收紧时只能手抄。
  8. **验证用的子进程要先核对它真被限制**：看 init 事件的 `permissionMode`，也要看 `permission_denials` 有没有出现过——一次都没有，多半是限制没生效，不是模型守规矩。
- **已知限制**（Master 2026-11-14 定，收官时进产品日志）：① **看板生成后没有自动核对**：检查脚本是仓库里的测试工具，不在插件里；插件只在约定里写「长文机械拷贝、写完把每张地图读回对照」和第 12 条第 5 步「对着日志查一遍」，不写某个工具的用法（overview 第 15 条）；靠模型自查，手抄长文仍可能丢字——真实状态的一次生成里地图丢了一个 `-`，检查脚本抓到了。收官时 Master 登记后续「看板生成后的自动核对」。② **hook**：Windows 上没装 Git for Windows 的用户不生效；macOS 未实测；Codex 里的触发未实测，且要用户先在 `/hooks` 里信任。③ **频率测试**：模型是 magpie 的便宜模型、不是 Haiku；一场只有 14 个提示加一次压缩，不够「很长」，注意力衰减测不出；三次一档，只分得出大差别。④ **看板**：地图靠 Mermaid 的 CDN 画，离线时展开的是源码；本仓库现状的一次生成要 15 到 25 分钟（条目和日志多、模型手抄）。
- **块 8～10 通过，进 Test**（Master 2026-11-14，PO 授权；审的是 `1c2cdb2..HEAD` 的提交）：块 10 标 ✓，Now 改成「Test：Master 审过，等收官」；审阅的记录在第 5 章。已知限制四条照上面留着。

## 5. Test

**频率测试**（61-5，块 6）。标准 `tests/frequency-test.md`（`4e26b73`，第 9 节补充 `5be345d`，都在跑之前）；驱动与判定 `tests/frequency_test.py`（`c3e338b`）。通道：`claude-magpie.cmd -p`、白名单环境、magpie 的便宜模型（**非 Haiku**）；工具 Read、Grep、Glob（15 次里有一次调了文档 MCP 的只读查询——`--tools` 管不住 MCP 工具——不影响结果）。原始流在 `S:\IDEO-Scrum-Archives\sprint-19-board-hook\formal\`。

- **运行**：15 次全部 `ok`，0 次重跑，0 次权限拒绝；臂核对全过（注入次数 A0 0、A1 2、A2 16、A3 4、A4 3，与预期逐个相同）；15 次都发生了压缩。仪器有效：A2 的 P1、P2 的「引用当前」各 3/3。
- **行为栏**（每格 x/3；P1 在换目标之后、压缩之前，P2 在压缩之后）：

  | 臂 | P1 引用当前 | P1 过期 | P1 查日志 | P2 引用当前 | P2 过期 | P2 查日志 | 注入次数 | 过线 |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | A0 对照（不注） | 3 | 0 | 3 | 3 | 0 | 0 | 0 | 是 |
  | A1 只 SessionStart | 3 | **2** | 3 | 3 | 0 | 1 | 2 | 否 |
  | A2 再加每轮 | 3 | 1 | 3 | 3 | 0 | 0 | 16 | 是 |
  | A3 再加每 5 轮 | 3 | **2** | 3 | 3 | 0 | 0 | 4 | 否 |
  | A4 再加变了才注 | 3 | 1 | 3 | 3 | 0 | 0 | 3 | 是 |

- **内容栏**（人工复核全部 30 条）：P1 应当不选入，15/15 不选入；P2 应当选入，15/15 选入。脚本初判多数是 `unclear`（关键词不够），改判都是 `unclear`→对；脚本判错一条：A2-3 的 P2 判成 `wrong`，人工看决定行是「选进本冲刺」、是对的，脚本是被回答别处的「不」字带偏了。
- **人工看「过期」的 6 次（A1×2、A2×1、A3×2、A4×1）**：形态都一样——模型发现「会话启动时 hook 给的 Sprint Goal（旧的）和日志 1.1 里的不一致」，按日志原文做了决定，并提醒用户去查（A1-2 还问「哪句才是真实承诺」）。决定没被带偏，但旧的注入成了噪音，按标准字面算过期。A0 一次都没有——它没见过旧文，只在 P1 读了日志。
- **查日志**：P1 各臂都读了日志（夹具里那条规矩起作用）；P2 只有 A1 的一次读了，其余没读也逐字引用了当前目标——压缩摘要带着 P1 读来的原文。
- **每次注入多少 token**：样本三句承诺 172 个字符。脚本取的 A0 对 A2 单轮输入 token 之差是 1052，除以 2 次注入得 526，但这个数被一个干扰带偏了：A2 三次里有两次，文档 MCP 服务在开场时已连上，多带了约 1290 token 的工具定义。用同样没连上的一对算（A0 六千五百零四、A2 的第 2 次六千六百九十七），两次注入共多 193 token，**每次约 96 token**。
- **选定**：按标准，过线的臂是 A0、A2、A4（A1、A3 因 P1 过期 2/3 不过线）。A0 也过线，**如实记「测不出」**：模型有「决定前引用 Sprint Goal 原文」这条规矩时自己会去读日志，压缩摘要又带着原文，所以 hook 在这个测试里没有可测的好处——这也印证了 Master 的判断：约定（66-5）是主力，hook 只补位；而且会话里的目标改了以后，早先注入的旧文留在上下文里，反成噪音（A1、A3 最明显）。标准里「A0 也过线——仍照 PO 的决定带 SessionStart，UserPromptSubmit 选最省的过线臂」，字面读法里「最省」包含 A0（不注），那会得到 A1 的配置，而 A1 自己没过线；按本意（PO 要带 hook），在带 hook 的过线臂里选最省的，是 **A4**（3 次注入对 A2 的 16 次）。这一处读法请 Master 确认。（Master 2026-11-13 确认选 A4，见第 4 章。）

**看板生成与核对**（35-1～5，块 8、9）。检查脚本 `tests/board_check.py`（自测 54 条全过：两个场景各一份写对的参考页过，各 18 种改坏的页都被抓到，再加空状态与重建一致的几条）；驱动 `tests/board_generate.py`。通道同上，工具 Bash、Read、Grep、Glob、Write、Skill；简报是一句话——读 scrum-kernel 的 `conventions/board.md` 与 `board-template.html`、照着写 `scrum/Board.html`；每次都从没有 `Board.html` 的副本做起。原始流与页面在 `S:\IDEO-Scrum-Archives\sprint-19-board-hook\board`、`board2`、`board3`、`board4`。

- **各批结果**（夹具 A：工作区在 main，开着的日志只在分支上；夹具 B：工作区在 Sprint 01 的分支上，Now 行有未提交的改动；本仓库现状）：

  | 批 | 条件 | 夹具 A | 夹具 B | 本仓库现状 |
  | --- | --- | --- | --- | --- |
  | 1 | 权限宽松 | 2/3，一页链接写成 `../ProductBacklog.md`（死链） | — | — |
  | 2 | 宽松；模板补了链接写法 | 2/3，一页删了地图里的 `<br/>` | 3/3 | 2 页各 9 处不过，全是检查脚本自己读错；修脚本后按当时的状态重核，2/2 过 |
  | 3 | 严格（`--setting-sources project,local`）；模板补了 `<br/>` 的写法 | 3/3 | 3/3 | 1/2：一页过但超时被杀（页面已写好）；一页地图丢了一个字符（`K -.-> U` 写成 `K .-> U`） |
  | 4 | 严格；合并 Sprint 18 后；board.md 补「长文机械拷贝、把每张地图读回对照」 | — | — | 2/2 |

  每批里同一状态下的页，事实集合相同（`compare`：same facts）；批 2 夹具 A、批 3 本仓库各有一页因上面的丢字不同。严格权限下模型常写 `cd … && git …` 被拒、也试过跑 Python 被拒，它改用不带 `cd` 的写法，没有一次因此失败。
- **验收**：35-1 本仓库现状（main 加 Sprint 19 的分支；Sprint 18 已收官）出一张产品卡、一张冲刺卡、没有设计时一行「No design is open.」；夹具里是两张冲刺卡、一张设计卡、IDEO 日志一行；链接都打得开。35-2「抽查 10 个事实」改成全查：检查脚本逐项对日志（承诺、Now、等 PO、阶段、工作块与完成标记、条目的标题状态规模、地图、方案标题、来源的分支与提交号），批 3、批 4 的每一页都是 0 处不符。35-3 顶部「等 PO」条恰好是各日志的 Waiting for PO：夹具 A、B 各 3 页都过；本仓库现状两份日志都是 `None`，页面写了一行「Nothing is waiting for the Product Owner.」。35-4 同一状态生成 3 次、事实对：夹具 A、B 各 3/3，本仓库现状批 4 为 2/2。35-5 删掉再生成内容一样：每次都从没有看板的副本做起，同状态的页事实集合相同。35-6 形式：Master 定网页版（块 1）。
- **成本**：夹具每次约 2 到 6 分钟（输入约 2 万到 6 万 token，另有缓存读 16 万到 68 万，输出约 0.6 万到 1.5 万 token）；本仓库现状每次约 4 到 25 分钟。
- **手抄丢字的已知限制**见第 4 章。

**审阅**（sprint-log 第 16 条的审阅者；Master）：Master 2026-11-14 审过块 1～10 的提交，复核了 strict、Codex、hook 实跑（PO 授权）。它自己核的几项：`claude plugin validate --strict` 通过；`check_codex.py` 各项都是空列表；在本仓库直接跑 hook，输出就是三句承诺原文，exit 0，照日志的语言出中文或英文的标签；`hooks.json` 带开关说明；`sync_codex.py` 不收符号链接；README 的文件地图已同步，也写了 Codex 要先在 `/hooks` 信任。

**Definition of Done（本冲刺选的三项）**：无死链——`check_codex.py` 的链接检查 0 错，`plugin-dev:plugin-validator` 核对过插件里新文件的引用都解析得到；插件校验——`claude plugin validate --strict plugins/ideo-scrum` 通过；Codex 包——同步并核对通过，hook 一并同步。Outcome Done（一次会话走通方法论环节、用户不反复追问）：待 PO 的端到端试用。

**还没做**：PO 的端到端试用；Review 与 Retro 由 Master 做。
