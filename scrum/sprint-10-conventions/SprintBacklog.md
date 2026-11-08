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

从产品日志原样摘抄五列：编号、标题、用户故事、架构定位、规模（PO 2026-11-08，2.2.1 第 19 点）。当前状态只写在产品日志里；备注是精化的点，本冲刺已在 2.2 处理。

| 编号 | 标题 | 用户故事 | 架构定位 | 规模 |
| --- | --- | --- | --- | --- |
| PBI-39 | 总览约定——三层、文件与 docs | 作为陌生人，我想要插件里有一份总览，讲清产品日志、冲刺、设计怎么连起来，`scrum/` 和文档文件夹各放什么，谁负责什么，以便第一次用就知道每份日志在哪、写不下的东西放哪 | 2.2.1 Map、2.2.2 主线与分层；另含 2.2.3 的角色表、2.2.7 讲约定本身的几条、2.2.8 的汇总 | M |
| PBI-31 | 产品日志约定 v1——模板与精化 | 作为熟手，我想要开新项目时插件自带产品日志模板和精化约定，以便新老项目都从一份产品日志开始，白纸也知道先写什么、PBI 怎么写 | 2.2.4 产品日志（Map ②） | M |
| PBI-23 | 冲刺日志约定 v1——模板与各单元约定 | 作为熟手，我想要插件自带冲刺日志模板和各单元的约定，以便每个冲刺都照同一套流程开会、记录、收官，不用我每次口述规矩 | 2.2.5 一个 Sprint（Map ③～⑧） | L |
| PBI-32 | 角色命令接上约定 | 作为熟手，我想要每个角色一进入就加载该加载的内核、知道该读哪份约定、清楚自己负责什么不负责什么，以便不用我提醒，角色就按约定办事 | 2.2.3 角色与主场 | M |
| PBI-37 | 开设计与接手——设计日志第一次就跑得起来 | 作为熟手，我想要说一句「这条 PBI 要设计」就能开出一份设计（文件夹、分支、文件头、角色卡都有着落），会话断了也能从日志看出停在哪，以便第一次用就不用我补规矩 | 2.2.6 设计日志 | S |

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
| 14 | **How 是方案，不是步骤**（改约定）：How 写三样——① 工作项清单，按顺序排，每项一个会话以内做得完，写明产出和怎么算做完；② 关键选择和理由；③ 已知风险和拿不准的地方。不写每份文件里具体写什么，不写操作步骤，也不打磨计划本身。依据：Scrum Guide「decomposing Product Backlog items into smaller work items of one day or less」「enough detail that they can inspect their progress in the Daily Scrum」（SGEP 那句「do enough planning to get started with the work」只见于 references/，v2026.1 原文里没有，约定和产品日志都不引，见 3.2）；「一天」换成「一个会话」，站会换成检查点。取代产品日志 2.2.5 单元 3 的「只写大致方向」和 2.2.8 那一行（已同步改）。本冲刺的 How 也照办 | PO（2026-11-08，Master 转达） |
| 15 | **Goal fixed, plan flexible**（目标不变，其余可调）：三份日志各有一个不变的承诺——Product Goal、Sprint Goal、设计目标，DoD 也不降低；承诺下面的 PBI、精化点、验收标准、How 方案、设计方案，都可以随着了解调整，改了什么、为什么都记下来；承诺只有 PO 能改，Sprint Goal 保不住时由 PO 取消冲刺。写成一条约定，分四处落：总览、冲刺日志约定、产品日志约定、设计日志约定（design-log.md，归 PBI-37）。引原句：SGEP 原定用 scrum-kernel SKILL.md 里那段（Product Goal is fixed… / DoD is not weakened… / So what could be changed instead?），但 v2026.1 原文里没有这段，约定里改引 Scrum Guide 的句子（见 3.2）；Scrum Guide 用「No changes are made that would endanger the Sprint Goal」「Scope may be clarified and renegotiated with the Product Owner as more is learned」 | PO（2026-11-08，Master 转达） |
| 16 | **约定里不写 Claude Code 的具体机制**：plan 模式、fork、权限模式这类做法容易变，一律不写进约定；subagent 照旧用（插件里一直在用的通用说法）。因此：删掉总览原第 13 条「A fork follows its parent」；冲刺日志约定第 13 条「Full text for review」只留原则（新的长期文档先把全文放到 PO 能逐段批注的地方，批准后才改源文件；盘上的版本优先）；第 16 条「Developer 是 Master 的 fork」改成工具中性的说法（Developer shares the Master's context）；Master 先前提的「插件的运行环境就是 Claude Code」这句不加 | PO（2026-11-08，Master 转达） |
| 17 | **不要修订记录**：产品日志模板不设 Revision record 一节，历史交给 git；产品日志约定、总览、冲刺日志约定里提到修订记录的地方都清掉，Review 时「给产品日志保鲜」也不再写修订记录。我们自己的产品日志，到 Review 精简时照新模板，同样去掉修订记录一节 | PO（2026-11-08，Master 转达） |
| 18 | **PBI 编号写成 PBI- 加三位数**，往下接着编，例如 PBI-001、PBI-002：改产品日志约定第 10 条七列说明表的「#」一行、两份模板的表头或注释、冲刺日志里讲到编号的地方；测试夹具和 D 组题目里的 PBI-02 改成 PBI-002。我们自己的产品日志不重新编号：归档的冲刺日志和 git 历史都在引用 PBI-12 这种旧编号 | PO（2026-11-08，Master 转达） |
| 19 | **冲刺日志 2.1 直接摘抄产品日志原文**，五列：编号、标题、用户故事、架构定位、规模。当前状态不抄，只写在产品日志里；备注不抄，那是精化的点，放到 2.2 处理。改模板 2.1、冲刺日志约定的「Who writes each section」表和第 5 条；本冲刺日志的 2.1 也照这个改 | PO（2026-11-08，Master 转达） |
| 20 | **stakeholder 命令的描述**：「(not a fork of the conversation)」改成「(not a copy of the current conversation)」，其余一字不动；R 组本来就要重跑 | PO（2026-11-08，Master 转达） |
| 21 | **PO 指定 Stakeholder 审阅时，它对照 DoD 和验收标准逐条核对**：加在 stakeholder 命令、冲刺日志约定第 16 条、scrum-master 命令「Review the work」那条；产品日志 PBI-32 的这个开放点改成已定 | PO（2026-11-08，Master 转达） |
| 22 | **约定要短**（取代产品日志 2.2.7「约定文件长度不限」）：砍字，不砍规矩；对照表每一项砍完都还在，不加新内容。方向：① 一条规矩只写一处，别处用短名指过去——「目标不变，其余可调」的完整写法和引文只放总览第 16 条；故意和官方不同的理由写在那条规矩里，一句话加原文关键的半句，总览的汇总表改成索引；design-log 第 1、6 条指向总览；审阅、文档文件夹、文件名各只在一处写全。② 每条先写规矩本身，一到三句；只在故意和官方不同、或不说清楚 AI 会做错时写理由。③ 引文只标故意不同之处，只引关键的半句；和官方一致的不引（sprint-log 第 7 条可留「decomposing … one day or less」）；引文砍光的文件去掉 Source、License 两行。④ 不复述原书和模板：design-log 第 10～18 条只写人机协作和原书不同的地方；sprint-log 的「Who writes each section」表删掉，挪进冲刺日志模板各节的注释。⑤ 文件头：总览保留完整身份声明和来源标签说明，其余三份只留一句身份声明并指向总览第 13 条。⑥ 条号不动，只缩写不合并。⑦ 软目标：总览约 95 行、product-log 约 50、sprint-log 约 75、design-log 约 50，合计约 270 | PO 同意精简，具体方向由 Master 与 Developer 商定（PO 2026-11-08） |

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
  - D（目录里预先放好夹具）：「PBI-002 要先做设计。开一份设计：建好文件夹和设计日志，填好文件头，停在开头，不往下做。」
  - 冷启动三组的题目不提插件和约定，用用户自然会说的话（Scrum 词）；「按插件的约定」等于直接叫模型去加载插件，留着它 S 组的「直接说」就验不了 PBI-23 验收 ②，P、D 作为 Outcome 的证据也弱（Master 审 How 时改，2026-11-08，跑之前）。
- **夹具**：一份用新模板写的样例产品日志 `scrum/ProductBacklog.md`（社区图书馆借阅小程序，三条 PBI，其中 PBI-002 写明要先做设计），照新模板写，不带修订记录。施工时和模板一起写好，放在任务临时目录、不入库；跑测试前不再改；验收时连同结果一起给 Master 看。

| 组 | 怎么问 | 跑几次 | 判对（任一条不满足判错） |
| --- | --- | --- | --- |
| C 直接说 | Sprint 08 原题 | 新、旧各 5 | 加载了 scrum-kernel |
| R 角色命令 | Sprint 08 原题，四个命令 | 新版各 2 | 加载的内核与产品日志 2.2.3 一致：designer = ideo + design；developer = ideo + scrum；scrum-master = ideo + scrum + design；stakeholder = ideo |
| P 冷启动：产品日志 | 空目录 | 新版 5 | ① 加载了 scrum-kernel；② 读了产品日志的模板或约定；③ 建出名为 `ProductBacklog.md` 的文件；④ 标题按模板排：Product、Product Goal、DoD；Stakeholders、架构（Map）；当前的 PBI、已完成（中文或英文都算）；⑤ Stakeholders 一节是一张表，不是逐人的长卡 |
| S 冷启动：冲刺日志 | 夹具；直接说 5 次，从 scrum-master、developer 命令进入各 2 次 | 新版 9 | ① 加载了 scrum-kernel；② 读了冲刺日志的模板或约定；③ 建出 `scrum/sprint-01-<后缀>/SprintBacklog.md`（后缀不限）；④ 标题按模板排：Why（Sprint Goal、DoD）；What（PBI、精化）；How（How、笔记）；Review；⑤ 没改产品日志 |
| D 冷启动：开设计 | 夹具 | 新版 5 | ① 加载了 design-kernel；② 读了设计日志的模板或约定；③ 建出 `scrum/design-<后缀>/DesignBacklog.md`（后缀不限）；④ 文件头写了来源（PBI-002）和「Now」一行；⑤ 五章标题按模板排 |

- **通过线**：C 新版 ≥4/5，且不低于旧版；R 全部 2/2；P ≥4/5；S 直接说 ≥4/5，从命令进入的 4 次全过；D ≥4/5。
- **判定**：脚本先按工具调用和写出的文件判；判错的逐条人工看，改判写明理由，验收时摆给 Master 和 PO（CLAUDE.md「回归测试」）。
- **局限**：每组次数少，模型输出有随机性；用户级 CLAUDE.md 照常加载（作者的环境）；冷启动组在作者机器上跑，不等于陌生人的环境（体验测试归 PBI-30）。

**补测（2026-11-08，三份审查之后由 Master 定，跑之前写定，单独提交）**：在照审查改完的最终版本上跑；C 组原来的结果不动，已经跑过的标准不改。

| 组 | 怎么问 | 跑几次 | 判对（任一条不满足判错） | 通过线 |
| --- | --- | --- | --- | --- |
| C2 | C 组原题，直接说 | 新版 5 | ① 加载了 scrum-kernel；② 读了 `scrum-kernel/conventions/` 下的文件 | ≥4/5 |
| X-designer | 「/ideo-scrum:designer 这个项目还没有专门放文档的文件夹。设计收官后，Review 文档该放到哪里？只回答，不要写文件。」 | 新版 3 | ① 读了 scrum-kernel 的 `conventions/overview.md`；② 答对关键事实：没有文档文件夹时建一个，例如 `scrum/docs/`（回答里出现 `scrum/docs`）。答案只在总览第 5 条里 | ≥2/3 |
| X-stakeholder | 「/ideo-scrum:stakeholder 先别看东西。照这个插件的约定，利益相关者写在产品日志的第几节？只回答，不要写文件。」 | 新版 3 | ① 读了 scrum-kernel 的 `conventions/product-log.md` 或 `conventions/product-backlog-template.md`；② 答对关键事实：第 2.1 节（回答里出现 `2.1`）。答案只在产品日志约定第 6 条和模板里 | ≥2/3 |
| R、P、S、D | 原题 | 同上 | 原标准不变 | 原通过线 |

X 组是跨技能读取：designer 只加载 ideo、design，stakeholder 只加载 ideo，两题的答案都只在没加载的 scrum-kernel 的约定里，要顺着命令里 `../scrum-kernel/...` 的指路去读。

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
| 8 | 精简四份约定（2.2.1 第 22 点） | 总览、产品日志约定、冲刺日志约定、design-log.md 砍字不砍规矩；冲刺日志模板各节注释写明谁写 | 照对照表逐项重核、结果记进 3.2；全仓条号引用都对得上；留下的引文脚本逐句核过原文；没有新增内容 |
| 9 | 夹具与测试 | 样例产品日志（任务临时目录）；C、R、P、S、D 五组的结果记进 3.2 | 全部过线（2.2.4）；判错的逐条人工看、写明理由 |
| 10 | 自检，交审 | 3.2 记下对照表逐项落在哪；全仓 grep 与路径核对 | 无死链；插件里没有本仓库的路径、作者的记忆和配置；停下等 Master 派对抗审查，不做 Review、不合入 main |

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
| 2026-11-08 | 测试判定标准补一句（Master 审结构第二版时提出） | 夹具照新模板写，不带修订记录。P 组第 ④ 条去掉「修订记录」那处，已在 `2c28566` 改过、理由已记，但那次和结构稿第三版放在了同一个提交里，没有单独提交；这次补的夹具说明单独提交。至今没跑过任何一次测试 | `19609aa` | 补结构稿其余六处 |
| 2026-11-08 | 结构稿第四版：补完 Master 审第二版提出的其余六处，结构通过 | 总览第 2 条补产品日志 2.2.2 的三点（Review 时产品日志要删掉它们，插件里不能缺）；产品日志约定第 18 条写明改动记在哪（PBI 备注列、1.2 写日期和理由、其余交给 git）；冲刺日志约定第 8 条写成通用说法：PO 可以把审阅交给 Master，交了记进日志；第 14 条改成工具中性的「The log is the handoff」；role card 统一成新定义（design-log.md 第 10、18 条，design-kernel SKILL.md 测试那一行，施工 37 时照着对）；四个命令的指路写明是 scrum-kernel 技能下的 `conventions/overview.md`。Master：补完即通过，直接写全文，每份提交后停下报 Master | `9a4e950` | 写全文第一份：总览 |
| 2026-11-08 | 全文第一份：`scrum-kernel/conventions/overview.md`（PBI-39） | 对照表里归 39 的各项落点：2.2.1 Map → The map；2.2.2 主线与分层 → 第 1～4 条（第 2 条含三点：以 PBI 为单位判断要不要设计、设计结论照样开冲刺落地、增量是什么由 DoD 定；第 3 条三层表与第三层的说明）；文档文件夹（PO 2026-11-08）→ 第 5 条；生成的文件名 → 第 6 条；2.2.3 角色与主场 → 第 7 条角色表（含加载的内核、三方一起做冲刺日志、没有 Developer 时 PO 与 Master 直接走完）、第 9 条拿不准就问 PO、第 10 条 PO 兼 Developer；GlobalMemory 会话角色分层 → 第 11 条，派活分工 → 第 12 条（施工一行写成工具中性的说法）；2.2.7 讲约定本身的几条 → 第 13 条（身份声明、来源标签、短名、三处分工、不写工具机制）、第 14 条（每周集中改）、第 15 条（模板只记产出）；目标不变其余可调 → 第 16 条（SGEP 那段与 Scrum Guide 三句，原文都在仓库源文件里核对过）；2.2.8 → 文末汇总表九行（2.2.8 的八行，加产品日志「编号不排序」一行），各行注明见哪条约定。文件头按 CLAUDE.md 加了 Source、License 两行（文中有 SGEP 的整段引文）；ATTRIBUTION.md 第 1、2 节「本仓库位置」登记了 `scrum-kernel/conventions/`。自查：没有本仓库的路径、作者的记忆和配置，没有工具机制的说法；Mermaid 只有一张，flowchart TD | `9c9bd67` | 停下报 Master；认可后写产品日志约定与模板 |
| 2026-11-08 | Master 认可总览，删一处；全文第二、三份：`product-log.md`、`product-backlog-template.md`（PBI-31） | 总览汇总表「numbered, not ranked」一行删去「at Planning at the latest」（PO 原话只是「人需要时再调」，这半句没有依据）。Master 定：模板和约定写完一起停下报，冲刺日志两份也照办。对照表里归 31 的各项落点：2.1 Stakeholders → 模板 2.1 小表、约定第 6 条（派子代理拿一行当身份，表里没人先问 PO）；2.2.4 → 第 1 条只有一份、第 2 条白纸起步用 IDEO、第 3 条事实先查再编号问（Supplement）、第 4 条 Product 与 Product Goal（引 SGEP「stepping stone toward a long-term Product Vision」）、第 5 条两种 Done、第 7 条照 Make a Map 画架构、第 8 条不写 TBD、第 9 条技术架构不进、第 10 条七列（规模 S、M、L）、第 11 条编号不排序（故意不同，引 Scrum Guide）、第 12 条 PBI 与 Master 一起定（故意不同，引 Scrum Guide 两处）、第 14 条随时精化最终在冲刺日志、第 16 条精化内容放哪；精化七步（2.2.5 单元 2）→ 第 15 条；保鲜（单元 9）→ 第 17 条，不设修订记录；PBI 状态只写产品日志（CLAUDE.md）→ 第 13 条；目标不变其余可调 → 第 18 条；模板三章，节只放产出，不设修订记录。第 12 条短名由结构稿的「PBIs with the Master」改为「Items with the Scrum Master」，与全文的角色名一致。精化七步第 5 步原文是「几天能做完」，照 PO 定的「一个会话」改成「each done in a few sessions at most」 | `0122f8e` | 停下报 Master；认可后写冲刺日志约定与模板 |
| 2026-11-08 | Master 认可产品日志两份，改两处；自查引文出处 | 产品日志约定第 4 条的 SGEP 引文换成 v2026.1 第 209 行原句「The Product Goal often supports the Product strategy and Product Vision.」（原句只见于 references/）；第 11 条理由照 PO 原话写，删去没有依据的半句。按「引 SGEP 一律以 assets 里的 v2026.1 原文为准」逐句自查已写的引文：总览第 16 条和产品日志约定第 18 条引的 SGEP 那段（出自 scrum-kernel SKILL.md「The Scrum Artifacts in the Expansion Pack」）在 v2026.1 原文里没有，改引 Scrum Guide 原句（Product Goal「They must fulfill (or abandon) one objective before taking on the next.」，冲刺中「No changes are made that would endanger the Sprint Goal」「Quality does not decrease」「Scope may be clarified and renegotiated…」，取消冲刺「Only the Product Owner has the authority to cancel the Sprint.」）；产品日志 2.2.5 单元 3 去掉 SGEP「do enough planning to get started with the work」（同样只见于 references/）。现在三份文件里的引文，Scrum Guide 的都在 scrum-guide-2020.md 里，SGEP 的（两句「must be human」、第 209 行那句、Outcome/Output Done 两个名词）都在 v2026.1 原文里，脚本逐句核过。另：scrum-kernel 的 SKILL.md 和 references/ 注明出自「Scrum Guide Expanded v2026.1」的 Artifacts、Events 两章，在仓库的 v2026.1 原文里找不到，属于插件原有的出处问题，不在本冲刺范围，报 Master | `4870a40` | 写冲刺日志约定与模板 |
| 2026-11-08 | 全文第四、五份：`sprint-log.md`、`sprint-backlog-template.md`（PBI-23） | 对照表里归 23 的各项落点：2.2.5 工作区 → 第 1 条；收官点 → 第 2 条（故意不同，引 Scrum Guide）；冲刺日志结构表 → 模板与开头「Who writes each section」表；冲刺日志不是定稿 → 第 3 条；流程图 → 开头「The flow」；单元 1～11 → 第 5、6、7、8、9、10、16、17、18、19、20 条；特殊情况 → 第 21 条，小冲刺 → 第 4 条；不设 Retro 章 → 第 19 条。2.2.8 的四处故意不同（How、检查点、审阅方、不写截止日）→ 第 7、10、16、2 条，各引 Scrum Guide 原句写理由。GlobalMemory：Sprint 收尾做法 → 第 18、20 条（删过程件、压缩归档、单提交、tag 写成果、保鲜）；压缩代替交接 → 第 14 条（工具中性的写法）；plan 视图审阅 → 第 13 条（只留原则，附自审问题与建议）。CLAUDE.md 的流程教训：审阅交全新子代理、派审阅子代理写全已发出的决定 → 第 16 条；Review 召唤利益相关者 → 第 18 条；新模板先看结构 → 第 12 条；计划外工作先登记 → 第 11 条；判定标准先写 → 第 15 条；迁移后全仓查旧路径 → 第 20 条；没做完的回产品日志 → 第 21 条。PO 新定：How 是方案 → 第 7 条与模板 3.1；目标不变其余可调 → 第 3 条；审阅可以交给 Master → 第 8 条（第 12 条指过去）；不写工具机制 → 第 13、14、16 条；不要修订记录 → 第 18 条指向产品日志约定第 17 条。Sprint Goal 照 PO 的行文风格起草 → 第 5 条。引文十句全出自 scrum-guide-2020.md，脚本逐句核过，本文件没引 SGEP，文件头 Source、License 只列 Scrum Guide。README 文件地图加了 `scrum-kernel/conventions/` 一行（不写作者侧的状态） | `be44889` | 停下报 Master；认可后改 design-kernel（37） |
| 2026-11-08 | Master 认可冲刺日志两份；PBI-25 加 ⑥ | Master 查明：SKILL.md 与 references/ 里那段 SGEP（Artifacts、Events 两章）出自 2025.6 版，却标成 v2026.1，插件里的 v2026.1 原文没有这两章。这是插件原有的问题，不进本冲刺，照 Master 给的原文登记为 PBI-25 ⑥ | 本提交 | 写设计那侧（37） |
| 2026-11-08 | 全文第六份：design-kernel 的设计那侧（PBI-37） | 落点：① 2.1 里没人先问 PO → design-log.md 开头术语「Role card」（新定义：产品日志利益相关者表里的一行；派子代理拿一行当身份，细节由 AI 当场写；表里没人先问 PO）；② 开设计的步骤 → 第 4 条改名「Open a design」（后缀、文件夹、照模板建 DesignBacklog.md、填文件头）；③ 停在哪 → 模板文件头加 Now 一行，末尾新加第 21 条「Resume from the header」；只有一个会话时的署名 → 第 3 条；子代理开几个、用什么模型 → 第 13 条，非界面产品的原型做到多真 → 第 17 条，都标 Decide on the spot；role card 说法统一 → 术语、第 10、18 条、design-kernel SKILL.md 测试那一行；目标不变其余可调 → 末尾新加第 22 条，指向总览第 16 条。顺带对齐已定的规矩：术语「Folders」与第 19 条的 `docs/` 改成项目的文档文件夹（总览第 4、5 条）；第 20 条的 CLAUDE.md 改成「instructions file」（约定里不写具体工具）。原有条号 1～20 没挪。SKILL.md 的 Use Protocol 第 2 步指到第 4、21 条。ATTRIBUTION 第 1 节登记 design-log.md 第 1 条引的 Scrum Guide 原句 | `ccd8257` | 停下报 Master；认可后改四个命令与 scrum-kernel SKILL.md 短表，一起写完再停 |
| 2026-11-08 | Master 认可 37；补两处：design-kernel 里指这份日志的「product backlog」改成「product log」（「product backlog item(s)」照旧）；design-log.md 文件头加 Source、License 两行，只列 Scrum Guide | 和 scrum-kernel 的约定、总览的分法一致：日志叫 product log，条目叫 product backlog item | 本提交 | — |
| 2026-11-08 | 全文第七、八份：四个命令（PBI-32）与 scrum-kernel SKILL.md 短表 | 四个命令各加一行 Conventions 指路，写明是 scrum-kernel 技能下的 `conventions/overview.md`（designer 另指 design-kernel 的 design-log.md）；scrum-master 改「冲刺或设计之外」、审阅默认 Master、放行与检查点，加「Facilitate Sprints and designs」「Ask the Product Owner」；developer 加「Own the Sprint and its log」「The How is a plan, not steps」，改证据交审、放行经谁、拿不准问 PO 与 PO 兼 Developer、节奏一条（一个会话、检查点、Retro 写原则）；designer 写明对设计负责、产出是原型和结论，加「Ask the Product Owner」；stakeholder 的身份改成从产品日志利益相关者表里读一行。四个描述一字没动。SKILL.md 加「Conventions」一节和一张五行短表，描述没动 | 本提交 | — |
| 2026-11-08 | PO 又定两条（2.2.1 第 18、19 点）：PBI 编号 PBI-001 起；冲刺日志 2.1 摘抄五列 | 改了产品日志约定第 10 条、两份模板、冲刺日志约定的表与第 5 条；本冲刺 2.1 照新写法从产品日志原样摘抄五列。测试判定标准里的 PBI-02（夹具说明、D 组题目、D 组第 ④ 条）改成 PBI-002：测试还没跑过，不违反「出结果后不改标准」 | `63d7c82` | 停下报 Master；认可后写夹具、跑测试 |
| 2026-11-08 | Master 认可命令与 SKILL.md 这一批；测试暂缓；写好测试夹具 | Master：PO 嫌约定冗长，Master 已提精简方向、等 PO 点头；PO 同意的话先把四份约定精简一遍，测的才是最终文字，所以先不跑测试。模板不在精简范围里，先写夹具。夹具：样例产品日志，照新的产品日志模板写，社区图书馆借阅小程序，三条 PBI（PBI-001 查书、PBI-002 预约取书流程（备注写明要先做设计）、PBI-003 续借提醒），不带修订记录，标题与模板逐行一致；放在任务临时目录 `trig/fixture_s10/scrum/ProductBacklog.md`，不入库，sha256 前 12 位 `7b3dcc980550`，跑测试前不再改。Master 转给 PO 定的两处：stakeholder 描述里的「fork」；Stakeholder 被指定审阅时要不要对照 DoD 核验 | `944100e`、`b881f35` | 停下，等 PO 定精简方向 |
| 2026-11-08 | PO 定三件（2.2.1 第 20～22 点）；做 A：stakeholder 描述与审阅核对 | stakeholder 描述只把「fork of the conversation」换成「copy of the current conversation」；stakeholder 命令加「Reviewing when named」一条；scrum-master「Review the work」加半句；冲刺日志约定第 16 条在精简时一并写进；产品日志 PBI-32 的开放点改成已定。3.1 加工作项 8「精简四份约定」，原 8、9 顺延为 9、10 | `664bf46` | 精简 |
| 2026-11-08 | 做 B：精简四份约定 | 行数，砍前 → 砍后：总览 146 → 106，产品日志约定 79 → 63，冲刺日志约定 111 → 75，design-log.md 74 → 53，合计 410 → 297（软目标约 270；总览多出的主要是 Map、三张表和故意不同之处索引，都是对照表里的项）。对照表逐项重核，都还在：2.1 → 产品日志约定第 6 条与模板；2.2.1 Map → 总览的图；2.2.2 → 总览第 1～5 条（第 2 条的三点在）；2.2.3 → 总览第 7、9、10 条与四个命令；2.2.4 → 产品日志约定第 1～16 条；2.2.5 → 冲刺日志约定第 1～21 条与流程图，「谁写」挪进冲刺日志模板各节注释；2.2.6 → design-log.md；2.2.7 → 总览第 6、13～15 条；2.2.8 → 各条里的一句理由加总览的索引表；GlobalMemory 五条 → 总览第 11、12 条，冲刺日志约定第 13、14、16、18、20 条；CLAUDE.md 的教训 → 冲刺日志约定第 4、11、12、15、16、18、20、21 条；PO 新定各条 → 总览第 5、16 条，产品日志约定第 6、10、17、18 条，冲刺日志约定第 3、5、7、8、13、14、16 条，design-log.md 第 4、21、22 条。条号：四份文件依次是 16、18、21、22 条，连续，没有合并；插件里 44 处「convention N」引用用脚本逐个对到短名，全部对得上。引文：总览七句、产品日志约定两句、冲刺日志约定五句，脚本逐句核过 scrum-guide-2020.md 和 v2026.1 原文；design-log.md 的引文砍光（第 1 条的理由挪到总览第 2 条，第 18 条原书那句改成转述），去掉 Source、License 两行，ATTRIBUTION 里 design-log.md 那一行也删掉。没有新增内容；为了不砍规矩，design-log.md 第 13、17、19 条在初稿砍过头后补回四处（子代理出方案可用 Mermaid、子代理分做原型部件、Review 文档的内容仍标 Supplement、问专家前先画草图地图） | `664bf46` | 提交后照 2.2.4 跑 C、R、P、S、D |
| 2026-11-08 | 照 2.2.4 跑五组测试（Haiku，`claude -p --plugin-dir`，本分支 `664bf46` 的插件；C 组旧版用 `git archive v5.0.1` 导出） | 结果全部过线：C 新 5/5、旧 5/5（不低于旧版）；R 四个命令各 2/2（designer 加载 ideo + design，developer 加载 ideo + scrum，scrum-master 三个都加载，stakeholder 只加载 ideo）；P 5/5（都建出 `scrum/ProductBacklog.md`，标题按模板排，2.1 是一张表）；S 直接说 5/5、从 scrum-master 和 developer 命令进入 4/4（都建出 `scrum/sprint-01-<后缀>/SprintBacklog.md`，四章按模板排，2.1 是五列，产品日志没动）；D 5/5（都建出 `scrum/design-<后缀>/DesignBacklog.md`，文件头有 PBI-002 和 Now 一行，五章按模板排）。脚本判定后人工抽看了 P、S、D 各几份，没有判错，不改判。和判定标准的出入一处：冷启动组的临时目录不在任务临时目录里——先用一句无关的话试写，`~/.claude` 下的路径被权限系统当成敏感路径拦下，所以冷启动组改在系统临时目录 `%LOCALAPPDATA%\Temp\ideo-s10-a7aa9ffe\work` 下逐次新建；夹具仍从任务临时目录复制，内容没动。原始输出在任务临时目录 `trig/out_s10/`，判定结果 `trig/judge_s10_result.txt`，都随任务清掉，以本条为准 | `d6d09a9` | 停下报 Master，等对抗审查 |
| 2026-11-08 | 三份审查回来（插件校验 PASS；对抗审查基本通过；技能审阅必改 5 条、建议 10 条），照 Master 合并的 21 项清单改 | 一、scrum-kernel SKILL.md：Conventions 一节加一句（先读对应约定；references 是官方原文；约定在没有截止日、检查点、放行几处故意不同，总览列全）——证据是 C 组新版第 2、3 次只读了 references；第 18 行 Daily Scrum 改成 checkpoint；「只有 PO 必须是人」那段改成一句指向总览第 8 条，SGEP「At least one Product Developer should be human」并进总览第 8 条（脚本核过 v2026.1 第 371 行）。描述没动。二、总览：来源标签定义并进第 13 条，删掉第 13 条里命令那半句，文件头改成一句指向第 13 条；第 6 条补术语（product log、sprint log、design log 与文件名，PBI 写全一次，role card），短名由 File names 改为 Names；第 3 条补回「第三层不规定方法」；第 1 条删掉重复的半句。三、产品日志约定：第 6 条「not long cards」改成「not a long profile per person」，补「问过 PO 后把行补进表里」；第 4 条删掉复述模板的半句；第 5 条的规矩留在约定，冲刺日志模板 1.2 注释改成指路。四、冲刺日志约定：第 9 条补回「接手以笔记为准，不重新推导」，每行写什么拆出来标 Supplement；第 13 条改成交给审阅人（第 8 条），补「逐字全文，不写提纲」；第 19 条补回「写成原则，让不在场的人也能用」，「问 PO 在哪里卡住 AI」拆出来标 Supplement；第 20 条按六步的顺序重写；流程图改成「when written」。五、design-log.md：和 SKILL.md 重复的四处（开头第二句、第 3 条 PO 定什么、第 8 条第一句、第 9 条）改成指向 SKILL.md；删掉术语 Folders；role card 指向总览第 6 条，补「问过 PO 后把行补进表里」，正文统一用 role card；第 19 条补「分支照 sprint-log 第 20 条处理」。条号没动。六、模板：产品日志、冲刺日志模板的注释只留形状、谁写和短名指路，删掉召唤子代理、问 PO、「先加进产品日志」、「committed before anything runs」和 3.1 的长注释；保留「接手的会话先读这些」和文件头的指路；设计日志模板只加一行「How to write this log」，Sprint 09 PO 批过的原句一字没动。七、跨技能路径：design-log.md 指向总览、sprint-log 的各处，产品日志约定指向 make-a-map，总览指向 design-kernel 的两份文件，designer、stakeholder 命令的指路，都改成 `../` 开头的相对路径，并写明相对哪个技能的目录；脚本核过每个路径都存在。核对：60 处条号引用全部对到短名；引文脚本逐句核过；四个命令和三个 SKILL.md 的描述 diff 为 0。行数：总览 109、产品日志约定 63、冲刺日志约定 85（第 20 条拆成六步、两处 Supplement 拆行）、design-log.md 52。产品日志约定规模 M、L 的定义没动，等 PO 定 | `72e08a2` | 写 C2、X 两组的判定标准，单独提交，再在这个版本上跑 C2、X、R、P、S、D |
| 2026-11-08 | 补测判定标准（2.2.4「补测」） | C2 验「先读约定」那句有没有用；X 验跨技能的相对路径读不读得到；R、P、S、D 在最终版本上重跑，标准不变。X 两题的答案都只在 scrum-kernel 的约定里：designer 题的关键事实是 `scrum/docs/`（总览第 5 条），stakeholder 题是「2.1」（产品日志约定第 6 条与模板） | `fcc4876` | 在 `72e08a2` 的插件上跑 |
| 2026-11-08 | 补测：在 `72e08a2` 的插件上跑 C2、X、R、P、S、D（Haiku，`claude -p --plugin-dir`；冷启动组在系统临时目录 `ideo-s10-a7aa9ffe\work2` 下） | 过线的：C2 5/5（五次都读了 `scrum-kernel/conventions/` 下的文件，sprint-log.md 每次都读，四次还读了总览）；X-designer 3/3（三次都顺着 `../scrum-kernel/...` 读了总览，答出 `scrum/docs/`）；R 四个命令各 2/2；S 直接说 5/5、从命令进入 4/4；D 5/5。没过线的两组，照规矩不改判、不改标准：① **P 3/5**（线是 ≥4/5；第一轮是 5/5）：第 2、4 次根本没加载 scrum-kernel，凭常识在根目录写了 `PRODUCT_BACKLOG.md`；题目去掉「按插件的约定」以后，只说「把 Product Backlog 建起来」，而 scrum-kernel 的描述里没有 Product Backlog 这个词，Haiku 有时不触发。要修就得改描述，和 PBI-23 验收 ③「技能描述不变」冲突，留给 Master 和 PO 定。② **X-stakeholder 0/3**：三次都没加载技能、没读文件。原因在我出的题：题里「先别看东西」被它当成「别读任何文件」，第 0 次明说「按你的要求也没去读」，第 1 次只凭命令里的指路答了「第 6 条」。这组测不到跨技能读取，题目出错是我的问题；要不要改题重跑，由 Master 定（改题要先写新标准、单独提交）。另：P 第 4 次用了 PowerShell 工具列目录（只读）——禁用名单只写了 Bash，Windows 上还有 PowerShell 工具，下次一起禁。原始输出 `trig/out_s10b/`，判定结果 `trig/judge_s10b_result.txt` | 本提交 | 停下报 Master |
