# SeaPawn 在 IDEO-Scrum 的审阅记录

PO 逐份读插件里的英文约定，把不顺、不清楚、觉得不该在插件里的地方记在这里；定稿后由 IDEO-Scrum 开冲刺，照这些点把原文改掉。

## 目录

| 文件 | 是什么 |
|---|---|
| `conventions-overview-zh.md` | `scrum-kernel/conventions/overview.md` 的中文直译 |
| `conventions-product-log-zh.md` | `scrum-kernel/conventions/product-log.md` 的中文直译 |
| `conventions-sprint-log-zh.md` | `scrum-kernel/conventions/sprint-log.md` 的中文直译 |
| `conventions-design-log-zh.md` | `design-kernel/conventions/design-log.md` 与 `design-backlog-template.md` 的中文直译 |

## 进度

| 文档 | 状态 |
|---|---|
| `scrum-kernel/conventions/overview.md` | 审过一轮；Sprint 11 已改（第 2 处后半不改） |
| `scrum-kernel/conventions/product-log.md` | 审过一轮；Sprint 11 已改 |
| `scrum-kernel/conventions/sprint-log.md` | 审过一轮；Sprint 11 已改 |
| `design-kernel/conventions/design-log.md` | 审过一轮；Sprint 11 已改，原约定 2–22 改号为 1–21 |
| `design-kernel/conventions/design-backlog-template.md` | 随 design-log 一起审；Sprint 11 已改（地图重画那一句、条号） |

五份都审完了；Sprint 11（2026-11-09，PBI-41）照这份记录改了原文，各条状态见下面每张表的最后一列。

---

## overview.md —— 2026-11-09 凌晨

原文 109 行，逐段批注后定了四处改动，另有一处提了但没有改。

### 待改

| # | 位置 | 改什么 | 为什么 | 状态 |
|---|---|---|---|---|
| 1 | 开头「其余文件」那句 | 括号里补「设计那两份属于 design-kernel 技能，开设计时才去读」 | 原文只解释了 `../` 是相对路径，读者可能误以为 design-kernel 是 scrum-kernel 的一部分 | 已改（「开设计时」加了接手：read them when you open or resume a design，与 design-kernel SKILL.md 一致） |
| 2 | 约定 2 | 「产品日志下面平级放两样」→「产品日志之下，冲刺和设计平级并列」；「某一项」→「某个条目」 | 原文 `Below the product log sit two peers` 是倒装，直译后中文别扭；`item` 指 PBI 的一行，译成「某一项」太泛 | 前半已改（Under the product log, Sprints and designs are peers）；后半不改：英文原文就是 item，含糊的是译文「某一项」 |
| 3 | 约定 5 短名 | 「documents 文件夹」→「文件放哪」 | 这一条不只讲 documents，也讲只服务单个冲刺或设计的文件放哪、何时删。不能用「各个文件夹」，会和约定 4 的「文件夹」撞名 | 已改（Where files go） |
| 4 | 约定 14 | 短名「每周修订一次」→「修订何时生效」，正文删掉「大约每周改一次约定」，只留「从下一个冲刺起生效，绝不在冲刺中途改」 | 「每周改一次」是插件作者维护插件的节奏，不是使用者要遵守的规矩，不该写进插件。那半句挪去 IDEO-Scrum 自己的 PBI 或 CLAUDE.md | 已改（When a revision applies）；删掉的半句写进 CLAUDE.md「Sprint 节律」 |

### 提了但没改：官方没说「Developer 全权负责会议」

PO 认为 Planning 上我们跟官方不同，想在「对官方指南的偏离」表里加一行。核了原文，**不建议加**。

`references/scrum-guide-expanded-2025.6.md` 第 660–684 行讲 Sprint Planning 时说的是三件事，没有一句讲会议归谁：

1. `the Product Developers create the Sprint Backlog`
2. `Through collaboration with the Product Owner, the Product Developers select items from the Product Backlog`
3. `The How for the What: How the work is done is at the sole discretion of the Product Developers.`

其中第 2、3 条我方确实偏离，但**偏离表里已经有了**，对应的两行是「Product Owner 与 Scrum Master 一起定条目」和「How 是一份方案，构建要等放行」。再加一行会重复。

「SM 主持 Planning」不是偏离：同一份文件第 631 行说 `Skilled facilitation improves effectiveness`；第 425 行把 `chairperson` 列进 SM **不该**当的那串角色里——主持流程受鼓励，拍板的主席不行。第 587 行说精化 `often supported or facilitated by the Product Owner`，是「常常」，不是规矩。

---

## product-log.md —— 2026-11-09

| # | 位置 | 改什么 | 状态 |
|---|---|---|---|
| 1 | 约定 2 白纸 | 「第一章不清楚」→「产品和架构都弄不清楚」；不说用 IDEO 弄清楚，改成做一次设计：IDEO 方法加设计冲刺、做原型、测原型。落到日志上：产品降级成挑战、验收标准变问题、架构变待定的路线图 | 已改；「待定的路线图」写成 provisional roadmap，不写 TBD，免得和约定 8 冲突 |
| 2 | 约定 5 两种 Done | 补「写完成定义要精准，不是碰到一个就往里写；拿不准的留到验收标准」 | 已改 |
| 3 | 约定 11 编号不是排名 | 删掉「故意偏离 Scrum Guide」整段，改成编号必须唯一、排名即往上提 | 已改；连带删了 overview 偏离表里「Items are numbered, not ranked」一行 |
| 4 | 约定 12 一起定条目 | 补「挑进来的条目要和冲刺目标吻合；差的条目该加就加」 | 已改 |
| 5 | 约定 17 每次 Review 都刷新 | 补「不只是更新 PBI，是整个 `scrum/` 都要保持新鲜」 | 已改，写成指路：「整个 scrum/ 保鲜」只写在 sprint-log 约定 18 |

约定 2 的理由（PO 原话大意）：IDEO 方法论单独弄不清楚产品和架构，还是要走设计冲刺、做原型、测原型；产品和架构都可以先降级——产品降级成挑战、架构降级成待定路线图。

---

## sprint-log.md —— 2026-11-09

| # | 位置 | 改什么 | 状态 |
|---|---|---|---|
| 1 | 约定 3 | 「与 Product Owner 重新谈」→「与 Product Owner 或 Scrum Master」；删掉「笔记只增不减」 | 已改；写明 Scrum Master 是 Product Owner 的秘书（Scrum Guide 写的是与 PO 重谈）；冲刺日志模板 3.2 连带去掉表格和「只增不减」 |
| 2 | 约定 5 | 「什么都挑不出来」→「目标都定不出来」；补 IDEO 是所有的基础、遇到难点也能用；结果要与 Master 和 Developer 同步 | 已改；「IDEO 是基础」只带一句，指向 overview 约定 7 |
| 3 | 约定 9 | 删掉「每行给日期、做了什么、决定及理由、证据、下一步」这条格式规定；改成 3.2 就是写笔记，想写什么写什么；How（3.1）本身也是笔记，3.2 可以是 How 的细化 | 已改；冲刺日志模板 3.2 同步 |
| 4 | 约定 16 | 分清两种情形：Master 自己参与构建 → 全新子代理审；Developer 与 Master 共享上下文（fork）→ 仍由这个 Master 审，当独立的 Master 看待。也可以委任子代理，不影响 | 已改；没写「fork」（工具机制不进约定）；「也可以委任子代理」并进原有那句；scrum-master、developer 两个命令同步 |
| 5 | 约定 18 | 补「把整个 `scrum/` 过一遍」；调整删文件与移日志的顺序；「第 4 章」注明是 Review 章 | 已改 |
| 6 | 约定 20 | 「主要是产品日志」→ 直接说看 `scrum/` 就够 | 已改；没列看板（约定里还没定看板放哪，PBI-35 未做），改为指向 overview 约定 4 |

约定 21「冲刺目标过时 → 只有 Product Owner 能取消冲刺」按原文保留，PO 确认原意没写错。

「小冲刺可以不建那么多角色」不新增：`overview.md` 约定 7 末句已经写了「没有 Developer 时，Product Owner 与 Scrum Master 两人跑这个冲刺」。

---

## design-log.md 与 design-backlog-template.md —— 2026-11-09

PO 的整体判断：这一份**最拿不准**，后面还要调很多，先落盘，交给冲刺去改。

| # | 位置 | 改什么 | 状态 |
|---|---|---|---|
| 1 | 开头「角色卡」单列条 | 删掉。它跟设计日志无关，只是「角色卡」这个词的出处；等约定 18 用到时再就地引 `../scrum-kernel/conventions/overview.md` 约定 6 | 已改；引用放在「角色卡」第一次出现的原约定 10（现 9），不放 18：Designer 只加载 ideo、design 两个内核 |
| 2 | 约定 1 设计与冲刺并排 | 保留，但建议把规则提到 `design-kernel/SKILL.md` 开头——那才是渐进披露的入口。提上去之后这条可从约定里删掉 | 已改：原句提到 SKILL.md 第一段，删原约定 1，2–22 改号为 1–21，引用跟着改 |
| 3 | 约定 4 开一个设计 | 文件夹装的不止日志和原型，还有这一步的工作材料（草图、收集的点子、反应网格） | 已改（现约定 3） |
| 4 | 约定 10 需要时才问专家 | 补：专家和深度研究做完之后，挑战、设计目标、设计问题、**尤其是地图**，要再精化一遍查缺补漏，照 make-a-map 重画；这一步也可以理解为精化。模板 2.1 的注释同步补了这句 | 已改（现约定 9）；「也可以理解为精化」并进动词 refine；模板 2.1 同步 |

PO 判过、不算问题、不改的四条：约定 3 的兼任与 sprint-log 约定 16 的审阅；约定 17 的 *补充* 标签；约定 19 与 sprint-log 约定 18 的做法不同；约定 11 取消 Pick a target。（Sprint 11 原样保留，只随改号变成约定 2、16、18、10。）

---

## 下一步

五份约定都审完；Sprint 11 已照这份记录改完原文（2026-11-09）。
