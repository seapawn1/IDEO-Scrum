# Sprint Backlog — Sprint 10（流程全部进插件）

> 开工 2026-11-08 | 不写截止日：Sprint Goal 达成或 PO 叫停时收官（产品日志 2.2.5） | 分支：`sprint-10-conventions`（不开 worktree，PO 定） | PO：SeaPawn | Master：Claude（主会话） | Developer：Claude，从 Master 会话 fork 出来，继承上下文（PO 2026-11-08 定）
> 审阅：Developer 是 Master 的 fork，等于 Master 兼 Developer，对抗审查交全新子代理（CLAUDE.md）。plugin-validator、skill-reviewer，以及 Review 时召唤的 2.1 角色，都由 Master 派（fork 不派子代理）。拿不准的点报 Master，由 Master 问 PO（产品日志 2.2.3）。
> Developer 跟着主会话的权限模式走：主会话进 plan 模式时，Developer 写不了文件，停下等。
> PBI 状态只写在产品日志，本文件只引用编号；流程见产品日志 2.2.5。

# 一、Why

## 1.1 Sprint Goal

**流程全部进插件**：精化定下的内容都写进 scrum-kernel 的约定，产品日志、冲刺日志有了模板，从 Planning 到收官每一步都有约定，docs 是 Scrum 的文档库；角色命令跟上约定；产品日志只留产品本身，新项目照着插件就能走完一个冲刺。

## 1.2 DoD

产品日志 1.3 全部选入（PO 2026-11-08）：

| 项 | 本冲刺怎么核 |
| --- | --- |
| Outcome：一次会话走通方法论环节，完整引导（结构化、忠于原文），用户不反复追问 | 冷启动测试 P、S、D 三组（2.2.4） |
| Output：内容忠实 | Scrum Guide、SGEP 有原句的引原句；不是原文的写成约定，每条标来源标签，故意和官方不同的写明理由 |
| Output：可导航 | 从 scrum-kernel 的 SKILL.md 入口 ≤2 跳到任意约定和模板 |
| Output：无死链 | 所有 markdown 内部链接可解析 |

# 二、What

## 2.1 PBI

| 编号 | 标题 | 规模 | 本冲刺做什么 |
| --- | --- | --- | --- |
| PBI-39 | 总览约定——三层、文件与 docs（新登记） | M | 一份总览，讲清产品日志、冲刺、设计怎么连起来，文件放哪，谁负责什么 |
| PBI-31 | 产品日志约定 v1——模板与精化 | M | 产品日志模板与约定，精化七步 |
| PBI-23 | 冲刺日志约定 v1——模板与各单元约定 | L | 冲刺日志模板与各单元的约定 |
| PBI-32 | 角色命令接上约定 | M | 四个命令改掉过时的说法，跟上约定 |
| PBI-37 | 开设计与接手 | S | design-kernel 补开设计的步骤和「停在哪」 |

- 原定的 Sprint 11（PBI-32、25）并进本冲刺，路线上不再有 11；冲刺大没关系（PO 2026-11-08）。
- 不在范围：PBI-25（①② 是发布前的署名问题，随 PBI-30；③ 到时一并改；Master 定，PO 授权）；PBI-30、12、33、35（PO 定，这次不做）。

## 2.2 精化

PO 2026-11-08 宣布精化结束。

### 2.2.1 定下的各点

| # | 内容 | 谁定 |
| --- | --- | --- |
| 1 | Sprint Goal 照 Master 的草稿 | PO |
| 2 | PBI-23、31、32 放进同一个冲刺；冲刺大没关系 | PO |
| 3 | 精化定下的内容全部写进插件约定；Review 时照对照表（2.2.3）精简产品日志，2.2 只留 Map 和一句「流程见插件 scrum-kernel 的 conventions/」，删掉的原文 git 可查；修订记录一节也删掉（第 17 点）。PO：「之前想所有都写到产品日志里面，现在想想不太好。」 | PO |
| 4 | docs 的地位：日志写不下的东西（Review 归档、精化内容、背景材料、参考资料、专家访谈、深度研究、设计文档）放进项目的文档文件夹，日志里引用，被引用的文件就算 Scrum 的一部分；`scrum/` 只放现状，保持干净。根目录有 `docs/` 就用它；没有就建一个，比如 `scrum/docs/`；约定里不写死位置 | PO |
| 5 | 产品日志 2.1 用一张小表列出利益相关者，不写长的角色卡模板；派子代理时拿表里的一行当身份，细节由 AI 当场写 | PO |
| 6 | 总览单列成 PBI-39，放 scrum-kernel 的 `conventions/`；总览里有一张角色表（PO、Master、Developer、Designer、Stakeholder） | PO 同意 Master 的提议 |
| 7 | GlobalMemory 里五条流程规矩转成约定：Sprint 收尾做法、压缩代替交接、plan 视图审阅、会话角色分层、派活分工（PO：Review、Retro 的方式这些还是很重要的）；删哪些全局记忆，Review 时列给 PO | PO |
| 8 | Developer 用 fork；不开 worktree；文件夹和分支叫 `sprint-10-conventions` | PO |
| 9 | How、结构和全文的审阅都交给 Master：Master 认可就继续，不用再等 PO（PO 先把审 How 交给 Master，后来又把结构和全文的审阅也交给 Master） | PO（2026-11-08，后一半由 Master 转达） |
| 10 | PBI-37 进本冲刺，和 31 一起做 | Master（PO 授权 25、37、32 的细节由 Master 定） |
| 11 | PBI-25 不进：①② 随 PBI-30，③ 到时一并改 | Master（同上） |
| 12 | PBI-32 不把四个命令改成 Owns / Does not own / Needs approval 三栏卡（命令里已写了边界，产品日志 2.2.3 也定好了主场）；只按 2.2.3 保持新鲜，stakeholder 的身份从产品日志 2.1 读 | Master（同上） |
| 13 | PBI-37：构思开几个子代理、用什么模型、非界面产品的原型做到多真，都当场定，不写死 | Master（同上） |
| 14 | **How 是方案，不是步骤**（改约定）：How 写三样——① 工作项清单，按顺序排，每项一个会话以内做得完，写明产出和怎么算做完；② 关键选择和理由；③ 已知风险和拿不准的地方。不写每份文件里具体写什么，不写操作步骤，也不打磨计划本身。依据：Scrum Guide「decomposing Product Backlog items into smaller work items of one day or less」「enough detail that they can inspect their progress in the Daily Scrum」，SGEP「do enough planning to get started with the work」；「一天」换成「一个会话」，站会换成检查点。取代产品日志 2.2.5 单元 3 的「只写大致方向」和 2.2.8 那一行（已同步改）。本冲刺的 How 也照办 | PO（2026-11-08，Master 转达） |
| 15 | **Goal fixed, plan flexible**（目标不变，其余可调）：三份日志各有一个不变的承诺——Product Goal、Sprint Goal、设计目标，DoD 也不降低；承诺下面的 PBI、精化点、验收标准、How 方案、设计方案，都可以随着了解调整，改了什么、为什么都记下来；承诺只有 PO 能改，Sprint Goal 保不住时由 PO 取消冲刺。写成一条约定，分四处落：总览、冲刺日志约定、产品日志约定、设计日志约定（design-log.md，归 PBI-37）。引原句：SGEP 用 scrum-kernel SKILL.md 里那段（Product Goal is fixed… / DoD is not weakened… / So what could be changed instead?），Scrum Guide 用「No changes are made that would endanger the Sprint Goal」「Scope may be clarified and renegotiated with the Product Owner as more is learned」 | PO（2026-11-08，Master 转达） |
| 16 | **约定里不写 Claude Code 的具体机制**：plan 模式、fork、权限模式这类做法容易变，一律不写进约定；subagent 照旧用（插件里一直在用的通用说法）。因此：删掉总览原第 13 条「A fork follows its parent」；冲刺日志约定第 13 条「Full text for review」只留原则（新的长期文档先把全文放到 PO 能逐段批注的地方，批准后才改源文件；盘上的版本优先）；第 16 条「Developer 是 Master 的 fork」改成工具中性的说法（Developer shares the Master's context）；Master 先前提的「插件的运行环境就是 Claude Code」这句不加 | PO（2026-11-08，Master 转达） |
| 17 | **不要修订记录**：产品日志模板不设 Revision record 一节，历史交给 git；产品日志约定、总览、冲刺日志约定里提到修订记录的地方都清掉，Review 时「给产品日志保鲜」也不再写修订记录。我们自己的产品日志，到 Review 精简时照新模板，同样去掉修订记录一节 | PO（2026-11-08，Master 转达） |

### 2.2.2 各 PBI 写什么与验收

| PBI | 写什么 | 验收 |
| --- | --- | --- |
| 39 总览 | 总图；三层结构与文件布局，含文档文件夹（第 4 点）；角色表：主场、负责什么、加载哪些内核、拿不准就问 PO；约定本身的规矩：身份声明、来源标签、每周集中改一次、模板只记产出、用模板建出来的文件叫 `ProductBacklog.md`、`SprintBacklog.md`、`DesignBacklog.md`；与官方故意不同之处汇总；会话分工：一个项目一个 Master，审阅默认 Master，施工交给新的 Developer，或交给和 Master 共享上下文的 Developer（后者不能审自己的活）；不写具体工具的机制（2.2.1 第 16 点） | ① Master 派一个「陌生人」子代理只读总览，能说出每份日志在哪、写不下的放哪、谁负责什么；② 对照表里归 39 的每一项都在 |
| 31 产品日志 | 模板：三章，不设修订记录（第 17 点），节只放产出，2.1 是一张小表；约定：产品日志 2.2.4 的全部内容；精化七步写在这里，冲刺日志约定指过来；保鲜规则 | ① 冷启动 P 组过线；② 对照表里归 31 的每一项都在 |
| 23 冲刺日志 | 模板：四章；约定：产品日志 2.2.5 的全部单元（含小冲刺）；GlobalMemory 的收尾做法、压缩代替交接、plan 视图审阅；CLAUDE.md 里关于审阅和 Review 的教训 | ① 冷启动 S 组过线：空目录（只有一份产品日志）能开 Planning、建出冲刺日志骨架；② 从角色命令进入和直接说，两条路都找得到约定（S 组两种问法）；③ 技能描述不变，SKILL.md 只多一张短表；④ 全英文、不依赖本仓库，故意和官方不同的地方写明理由；⑤ 对抗审查通过 |
| 32 命令 | 改掉过时的说法：「冲刺之外不干活」改成「冲刺或设计之外」；审阅默认 Master，Master 兼 Developer、或 Developer 和 Master 共享上下文时交全新子代理；补「拿不准就问 PO」、放行、检查点；scrum-master 提到设计与设计日志；designer 的产出说法对齐设计日志约定第 1 条；stakeholder 的身份从产品日志 2.1 读；每个命令一句指路 | ① 四个命令和总览的角色表一致，没有和约定冲突的句子；② R 组每个命令 2/2；C 组不低于改前 |
| 37 开设计 | 2.1 里没人时先问 PO，补进小表；开一份设计的步骤：起后缀、建文件夹、开分支、填文件头；文件头加一行「Now」，写停在哪、下一步；只有一个会话时 Designer 与 Scrum Master 的署名写法 | ① 冷启动 D 组过线：新会话只看 design-kernel 就能开出一份设计；② 接手的会话读文件头就知道停在哪 |

### 2.2.3 「全部加进来」对照表（验收依据，也是 Review 时精简产品日志的依据）

| 产品日志里的内容 | 写到插件哪里 | PBI |
| --- | --- | --- |
| 2.1 Stakeholders | 产品日志模板的 2.1 小表；派子代理拿表里一行当身份；stakeholder 命令指过去 | 31、37、32 |
| 2.2.1 Map、2.2.2 主线与分层 | 总览，加文档文件夹 | 39 |
| 2.2.3 角色与主场 | 四个命令；总览的角色表 | 32、39 |
| 2.2.4 产品日志 | 产品日志模板与约定 | 31 |
| 2.2.5 一个 Sprint | 冲刺日志模板与各单元约定，含小冲刺 | 23 |
| 2.2.6 设计日志 | 已在 design-kernel；只补开设计与接手 | 37 |
| 2.2.7 在插件里的载体 | 讲约定本身的几条（身份声明、来源标签、迭代、模板只记产出）进总览；作者写插件的规矩（原文优先、写法）CLAUDE.md 已有，不进插件 | 39 |
| 2.2.8 与官方故意不同之处 | 分散写进各条约定，总览再列一张汇总表 | 23、31、39 |
| GlobalMemory 五条 | 收尾做法、压缩代替交接、plan 视图审阅进冲刺日志约定；会话角色分层、派活分工进总览 | 23、39 |
| CLAUDE.md 的流程教训 | 审阅交全新子代理；Review 时召唤 2.1 的角色；新模板先给 PO 看结构；小冲刺 | 23 |
| PO 2026-11-08 新定三条（2.2.1 第 14～16 点） | How 是方案：冲刺日志约定第 7 条、冲刺日志模板 3.1、总览的汇总表。目标不变，其余可调：总览第 16 条、冲刺日志约定第 3 条、产品日志约定第 18 条、design-log.md 第 22 条。不写工具机制：总览第 13 条（Working conventions）写明这条规矩，冲刺日志约定第 13、16 条照办 | 23、31、37、39 |

### 2.2.4 测试：方法与判定标准（2026-11-08，跑之前写定，单独提交）

- **方法**：`claude -p --plugin-dir <本分支插件的 Windows 路径> --model haiku --output-format stream-json --verbose`（与 Sprint 08 相同；reclaude 可用时也可以用它，参数相同）。每次跑都用一个新的临时目录，从工具调用记录里看加载了哪些技能、读了哪些文件，跑完看目录里写出了什么。用 Haiku（PO：测试用便宜的模型）。
  - 只读的组（C、R）：禁用 Write、Edit、Bash、NotebookEdit，与 Sprint 08 相同。
  - 冷启动组（P、S、D）：允许写文件（`--permission-mode acceptEdits`），禁用 Bash、NotebookEdit，只在临时目录里写。
- **对照**：C 组同一天跑改前版本（main 上的 v5.0.1，用 `git archive` 导出）当基线。冷启动组改前没有模板，只判新版。
- **题目**：沿用社区图书馆。
  - C：Sprint 08 原题「帮我开 Sprint Planning：这个冲刺要让社区图书馆的借阅小程序上线预约功能。先给我 Sprint Goal 的草稿和 Planning 的步骤大纲，不要写文件。」
  - R：Sprint 08 的四道原题。
  - P（空目录）：「我要开一个新项目：社区图书馆的借阅小程序。先把 Product Backlog 建起来：不清楚的地方留空，最后把要我定的问题编号列出来。」
  - S（目录里预先放好夹具）：直接说「开 Sprint 01 的 Planning：建出 Sprint Backlog，Sprint Goal 和选哪些 PBI 先写你的建议，How 先空着；不要改 Product Backlog。」从命令进入：同一句话前面加 `/ideo-scrum:scrum-master`，或加 `/ideo-scrum:developer`。
  - D（目录里预先放好夹具）：「PBI-02 要先做设计。开一份设计：建好文件夹和设计日志，填好文件头，停在开头，不往下做。」
  - 冷启动三组的题目不提插件和约定，用用户自然会说的话（Scrum 词）；「按插件的约定」等于直接叫模型去加载插件，留着它 S 组的「直接说」就验不了 PBI-23 验收 ②，P、D 作为 Outcome 的证据也弱（Master 审 How 时改，2026-11-08，跑之前）。
- **夹具**：一份用新模板写的样例产品日志 `scrum/ProductBacklog.md`（社区图书馆借阅小程序，三条 PBI，其中 PBI-02 写明要先做设计）。施工时和模板一起写好，放在任务临时目录、不入库；跑测试前不再改；验收时连同结果一起给 Master 看。

| 组 | 怎么问 | 跑几次 | 判对（任一条不满足判错） |
| --- | --- | --- | --- |
| C 直接说 | Sprint 08 原题 | 新、旧各 5 | 加载了 scrum-kernel |
| R 角色命令 | Sprint 08 原题，四个命令 | 新版各 2 | 加载的内核与产品日志 2.2.3 一致：designer = ideo + design；developer = ideo + scrum；scrum-master = ideo + scrum + design；stakeholder = ideo |
| P 冷启动：产品日志 | 空目录 | 新版 5 | ① 加载了 scrum-kernel；② 读了产品日志的模板或约定；③ 建出名为 `ProductBacklog.md` 的文件；④ 标题按模板排：Product、Product Goal、DoD；Stakeholders、架构（Map）；当前的 PBI、已完成（中文或英文都算）；⑤ Stakeholders 一节是一张表，不是逐人的长卡 |
| S 冷启动：冲刺日志 | 夹具；直接说 5 次，从 scrum-master、developer 命令进入各 2 次 | 新版 9 | ① 加载了 scrum-kernel；② 读了冲刺日志的模板或约定；③ 建出 `scrum/sprint-01-<后缀>/SprintBacklog.md`（后缀不限）；④ 标题按模板排：Why（Sprint Goal、DoD）；What（PBI、精化）；How（How、笔记）；Review；⑤ 没改产品日志 |
| D 冷启动：开设计 | 夹具 | 新版 5 | ① 加载了 design-kernel；② 读了设计日志的模板或约定；③ 建出 `scrum/design-<后缀>/DesignBacklog.md`（后缀不限）；④ 文件头写了来源（PBI-02）和「Now」一行；⑤ 五章标题按模板排 |

- **通过线**：C 新版 ≥4/5，且不低于旧版；R 全部 2/2；P ≥4/5；S 直接说 ≥4/5，从命令进入的 4 次全过；D ≥4/5。
- **判定**：脚本先按工具调用和写出的文件判；判错的逐条人工看，改判写明理由，验收时摆给 Master 和 PO（CLAUDE.md「回归测试」）。
- **局限**：每组次数少，模型输出有随机性；用户级 CLAUDE.md 照常加载（作者的环境）；冷启动组在作者机器上跑，不等于陌生人的环境（体验测试归 PBI-30）。

# 三、How

## 3.1 How

How 是方案，不是步骤（PO 2026-11-08，2.2.1 第 14 点）：工作项按顺序排，每项一个会话以内做得完；不写每份文件里具体写什么，不写操作步骤。2026-11-08 起照这个写法重排（原来是七条方向，内容不变，补上「怎么算做完」和风险）。

**工作项**

| # | 工作项 | 产出 | 怎么算做完 |
| --- | --- | --- | --- |
| 1 | 结构稿 | `scrum/sprint-10-conventions/structure.md`：五份文件的章节与约定短名，附 37、32、SKILL.md 的改动点 | Master 认可（PO 2026-11-08 把审阅交给 Master） |
| 2 | 总览（39） | `scrum-kernel/conventions/overview.md` | 对照表里归 39 的每一项都在；停下报 Master，Master 认可 |
| 3 | 产品日志（31） | `product-log.md`、`product-backlog-template.md` | 对照表里归 31 的每一项都在；Master 认可 |
| 4 | 冲刺日志（23） | `sprint-log.md`、`sprint-backlog-template.md` | 对照表里归 23 的每一项都在，GlobalMemory 三条有落点；Master 认可 |
| 5 | 设计那侧（37） | 改 design-kernel 的 `design-log.md` 和模板 | 结构稿附录列的各点都改了，原有条号 1～20 不变；Master 认可 |
| 6 | 四个命令（32） | 改 `commands/` 下四个文件 | 和总览的角色表一致，没有和约定冲突的句子；Master 认可 |
| 7 | SKILL.md 短表 | scrum-kernel 的 SKILL.md 加一节 Conventions | 描述一字不动；从 SKILL.md 一跳到每份约定和模板 |
| 8 | 夹具与测试 | 样例产品日志（任务临时目录）；C、R、P、S、D 五组的结果记进 3.2 | 全部过线（2.2.4）；判错的逐条人工看、写明理由 |
| 9 | 自检，交审 | 3.2 记下对照表逐项落在哪；全仓 grep 与路径核对 | 无死链；插件里没有本仓库的路径、作者的记忆和配置；停下等 Master 派对抗审查，不做 Review、不合入 main |

**关键选择和理由**

- 文件照 design-kernel 的样子拆，约定和模板分开放：两个内核用同一种布局，读的人认一次就会。共用的单元（检查点、审阅、文档文件夹）只写一份，别处指过去，免得两处说法走样。
- 设计那侧不新建文件，design-log.md 原有条号 1～20 不变，新条接在末尾：SKILL.md 和模板里都引用了这些条号，改号就得跟着改。
- 按依赖排：总览先写，后面各份照它的说法；四个命令最后改，指路才能指向已经定下的文件名。
- 先结构、后全文，全文每写完一份停一次，由 Master 审，Master 认可再写下一份（PO 2026-11-08 把审阅交给 Master；CLAUDE.md「模板规约」）。
- 内容照对照表逐项落，对照表就是验收清单；原文优先，Scrum Guide、SGEP 有原句的引原句并在句中写明出处，整段摘录的文件加 Source、License 两行；不是原文的写成约定，标来源标签；全英文、自足；模板只记产出。

**已知风险和拿不准的地方**

- 冲刺日志约定有 21 条，篇幅大，审的量也大：每写完一份就停，不攒着一起交。
- 把作者的做法写成通用说法时，容易漏出本仓库的路径、名字或作者的配置：工作项 9 专门 grep 一遍。
- 三份约定之间互相引用条号（如冲刺日志约定指向产品日志约定的「精化七步」）：结构定稿后条号不再动，改动时同步查引用。
- 冷启动测试受 Haiku 输出的随机性和作者环境影响（用户级 CLAUDE.md 照常加载），过线不等于陌生人环境里也行（体验测试归 PBI-30）。
- Developer 是 fork，跟着主会话的权限模式：主会话一进 plan 模式就写不了文件，只能停下等。

PO 放行：How 由 Master 审，Master 认可即放行（PO 2026-11-08 授权）；授权：冲刺分支上提交；合入 main、打 tag、发版到 Review 时定；不推送。

## 3.2 笔记

> 只往后加。每行：日期 · 做了什么 · 决定与理由 · 证据或提交号 · 下一步。

| 日期 | 做了什么 | 决定与理由 | 证据 | 下一步 |
| --- | --- | --- | --- | --- |
| 2026-11-08 | Planning 阶段 1、2（主会话） | PO 定：Sprint Goal、选入 PBI、DoD 全选、精化的各点（2.2.1）；原定 Sprint 11 并进来；Developer 用 fork，不开 worktree；How 交 Master 审即放行。阶段 2 的精化表和对照表 PO 认可，精化由 PO 宣布结束 | 主会话对话 | Developer 开工 |
| 2026-11-08 | 开工：开分支，建本日志一到三章；产品日志登记 PBI-39，改 1.2 路线与各 PBI 状态，改 PBI-31、37 的 2.1 写法，PBI-32 记下不做三栏卡 | Developer 由 Master fork 出来（16:18 开工） | `65f49ad` | 写测试判定标准，单独提交 |
| 2026-11-08 | 测试判定标准（2.2.4） | C、R 沿用 Sprint 08 的题目与判法；新加冷启动 P、S、D 三组，S 组同时验「从角色命令进入、直接说」两条路（PBI-23 验收 ②）；冷启动组允许写文件、禁用 Bash，只在临时目录里写；夹具施工时和模板一起写好，跑之前不再改 | `d85f6e5` | 停下，把 How 和判定标准报给 Master 审 |
| 2026-11-08 | Master 审 How 通过，放行，附两处调整 | ① 冷启动三组（P、S、D）的题目去掉「按插件的约定」，改成用户自然会说的话、用 Scrum 词（Product Backlog、Sprint Backlog、开一份设计）：这几个字等于直接叫模型去加载插件，留着它 S 组的「直接说」验不了 PBI-23 验收 ②，P、D 作为 Outcome 的证据也弱；判对的五条不变；在跑任何测试之前改，不违反「出结果后不改标准」。② CLAUDE.md「当前状态」照 Sprint 08 的先例加「Sprint 10 立项」一条，删去 2026-11-07 那条，保持三条；收官时换成收官那条，Sprint 09 那条不改。另：约定里引 Scrum Guide、SGEP 原句时在句中写明出处；放了整段摘录的文件，文件头加 Source、License 两行 | `9da5e94` | 照 How 施工：先交五份文件的结构 |
| 2026-11-08 | 结构稿：`structure.md`（中间文件，Review 时删） | 五份文件放 scrum-kernel 的 `conventions/`，命名照 design-kernel（约定 `xxx-log.md`，模板 `xxx-backlog-template.md`）：总览 16 条加汇总表、产品日志约定 17 条、冲刺日志约定 21 条、两份模板只列章节。每条标出处，对照表（2.2.3）各项都有落点。37 不改 design-log.md 的条号 1～20，新条接在末尾，免得 SKILL.md 和模板里的引用跟着改 | `6017ae0` | 停下，交 Master 转 PO；PO 点头后写全文，从总览开始 |
| 2026-11-08 | 带进 PO 新定的两条（2.2.1 第 14、15 点），照 Master 的补充改结构稿 | How 是方案、不是步骤：冲刺日志约定第 7 条、模板 3.1，本冲刺 3.1 也照这个写法重排（补「怎么算做完」和风险），产品日志 2.2.5 单元 3、2.2.8 那一行，以及 2.2.1 Map、2.2.5 的表与流程图、2.2.7 的短名示例，同步改成「How 是方案」。目标不变、其余可调：总览、冲刺日志约定、产品日志约定、design-log.md 各落一处，新条接在各自末尾，原有条号不挪。补充：冲刺日志约定开头加流程图；总览「Working conventions」补三处分工和短名；冲刺日志约定第 20 条补「tag 写成果」。2.2.3 对照表加一行 | 本提交 | — |
| 2026-11-08 | PO 定：约定里不写 Claude Code 的具体机制（2.2.1 第 16 点） | 结构稿删掉总览原第 13 条，原第 14～17 条前移为 13～16，引用「总览第 17 条」的几处同步改成第 16 条；冲刺日志约定第 13 条只留原则，第 16 条改成工具中性的说法；总览第 12 条「施工交给谁」也写成工具中性的说法。冲刺日志 2.2.2 的 39、32 两行和产品日志 PBI-39 的备注同步去掉 fork、权限模式的说法。冲刺日志开头关于本冲刺 Developer 是 fork 的记录照留，那是本冲刺的事实，不是约定 | 本提交 | 停下，等 PO 看结构稿 |
| 2026-11-08 | PO 又定两件（2.2.1 第 9、17 点）：不要修订记录；结构和全文的审阅交给 Master | 结构稿第三版：产品日志模板去掉 Revision record 一节，产品日志约定第 17、18 条、冲刺日志约定第 18 条清掉修订记录，冲刺日志约定第 12 条写明 PO 可以把审阅交给 Master。测试判定标准 P 组第 ④ 条的标题清单去掉「修订记录」：模板已经没有这一节，留着会把照新模板建出的文件判错；还没有跑任何测试，不违反「出结果后不改标准」。3.1 工作项「怎么算做完」里的「PO 看过」改成「Master 认可」 | 本提交 | 停下报 Master，等 Master 审结构 |
