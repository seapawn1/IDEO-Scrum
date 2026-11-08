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
| `scrum-kernel/conventions/overview.md` | 审过一轮，四处待改 |
| `scrum-kernel/conventions/product-log.md` | 审过一轮，五处待改 |
| `scrum-kernel/conventions/sprint-log.md` | 审过一轮，六处待改 |
| `design-kernel/conventions/design-log.md` | 审过一轮，四处待改 |
| `design-kernel/conventions/design-backlog-template.md` | 随 design-log 一起审，模板里同步了地图重画那一句 |

五份都审完了，可以开冲刺去改原文。

---

## overview.md —— 2026-11-09 凌晨

原文 109 行，逐段批注后定了四处改动，另有一处提了但没有改。

### 待改

| # | 位置 | 改什么 | 为什么 |
|---|---|---|---|
| 1 | 开头「其余文件」那句 | 括号里补「设计那两份属于 design-kernel 技能，开设计时才去读」 | 原文只解释了 `../` 是相对路径，读者可能误以为 design-kernel 是 scrum-kernel 的一部分 |
| 2 | 约定 2 | 「产品日志下面平级放两样」→「产品日志之下，冲刺和设计平级并列」；「某一项」→「某个条目」 | 原文 `Below the product log sit two peers` 是倒装，直译后中文别扭；`item` 指 PBI 的一行，译成「某一项」太泛 |
| 3 | 约定 5 短名 | 「documents 文件夹」→「文件放哪」 | 这一条不只讲 documents，也讲只服务单个冲刺或设计的文件放哪、何时删。不能用「各个文件夹」，会和约定 4 的「文件夹」撞名 |
| 4 | 约定 14 | 短名「每周修订一次」→「修订何时生效」，正文删掉「大约每周改一次约定」，只留「从下一个冲刺起生效，绝不在冲刺中途改」 | 「每周改一次」是插件作者维护插件的节奏，不是使用者要遵守的规矩，不该写进插件。那半句挪去 IDEO-Scrum 自己的 PBI 或 CLAUDE.md |

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

| # | 位置 | 改什么 |
|---|---|---|
| 1 | 约定 2 白纸 | 「第一章不清楚」→「产品和架构都弄不清楚」；不说用 IDEO 弄清楚，改成做一次设计：IDEO 方法加设计冲刺、做原型、测原型。落到日志上：产品降级成挑战、验收标准变问题、架构变待定的路线图 |
| 2 | 约定 5 两种 Done | 补「写完成定义要精准，不是碰到一个就往里写；拿不准的留到验收标准」 |
| 3 | 约定 11 编号不是排名 | 删掉「故意偏离 Scrum Guide」整段，改成编号必须唯一、排名即往上提 |
| 4 | 约定 12 一起定条目 | 补「挑进来的条目要和冲刺目标吻合；差的条目该加就加」 |
| 5 | 约定 17 每次 Review 都刷新 | 补「不只是更新 PBI，是整个 `scrum/` 都要保持新鲜」 |

约定 2 的理由（PO 原话大意）：IDEO 方法论单独弄不清楚产品和架构，还是要走设计冲刺、做原型、测原型；产品和架构都可以先降级——产品降级成挑战、架构降级成待定路线图。

---

## sprint-log.md —— 2026-11-09

| # | 位置 | 改什么 |
|---|---|---|
| 1 | 约定 3 | 「与 Product Owner 重新谈」→「与 Product Owner 或 Scrum Master」；删掉「笔记只增不减」 |
| 2 | 约定 5 | 「什么都挑不出来」→「目标都定不出来」；补 IDEO 是所有的基础、遇到难点也能用；结果要与 Master 和 Developer 同步 |
| 3 | 约定 9 | 删掉「每行给日期、做了什么、决定及理由、证据、下一步」这条格式规定；改成 3.2 就是写笔记，想写什么写什么；How（3.1）本身也是笔记，3.2 可以是 How 的细化 |
| 4 | 约定 16 | 分清两种情形：Master 自己参与构建 → 全新子代理审；Developer 与 Master 共享上下文（fork）→ 仍由这个 Master 审，当独立的 Master 看待。也可以委任子代理，不影响 |
| 5 | 约定 18 | 补「把整个 `scrum/` 过一遍」；调整删文件与移日志的顺序；「第 4 章」注明是 Review 章 |
| 6 | 约定 20 | 「主要是产品日志」→ 直接说看 `scrum/` 就够 |

约定 21「冲刺目标过时 → 只有 Product Owner 能取消冲刺」按原文保留，PO 确认原意没写错。

「小冲刺可以不建那么多角色」不新增：`overview.md` 约定 7 末句已经写了「没有 Developer 时，Product Owner 与 Scrum Master 两人跑这个冲刺」。

---

## design-log.md 与 design-backlog-template.md —— 2026-11-09

PO 的整体判断：这一份**最拿不准**，后面还要调很多，先落盘，交给冲刺去改。

| # | 位置 | 改什么 |
|---|---|---|
| 1 | 开头「角色卡」单列条 | 删掉。它跟设计日志无关，只是「角色卡」这个词的出处；等约定 18 用到时再就地引 `../scrum-kernel/conventions/overview.md` 约定 6 |
| 2 | 约定 1 设计与冲刺并排 | 保留，但建议把规则提到 `design-kernel/SKILL.md` 开头——那才是渐进披露的入口。提上去之后这条可从约定里删掉 |
| 3 | 约定 4 开一个设计 | 文件夹装的不止日志和原型，还有这一步的工作材料（草图、收集的点子、反应网格） |
| 4 | 约定 10 需要时才问专家 | 补：专家和深度研究做完之后，挑战、设计目标、设计问题、**尤其是地图**，要再精化一遍查缺补漏，照 make-a-map 重画；这一步也可以理解为精化。模板 2.1 的注释同步补了这句 |

PO 判过、不算问题、不改的四条：约定 3 的兼任与 sprint-log 约定 16 的审阅；约定 17 的 *补充* 标签；约定 19 与 sprint-log 约定 18 的做法不同；约定 11 取消 Pick a target。

---

## 下一步

五份约定都审完，可以照这份记录开一个 IDEO-Scrum 的冲刺，逐条改原文。
