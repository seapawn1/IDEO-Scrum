# Sprint 14 审定清单

PO 逐行看；结论填「改 / 不改 / 挪到 PBI-xx」；状态填「待看 / 已定 / 已改 / 已核」。

路径都在 `plugins/ideo-scrum/skills/` 下：`scrum-kernel/`（`overview.md`、`SKILL.md`、`conventions/` 里的 product-log、sprint-log 和两份模板）、`design-kernel/`（`SKILL.md`、`conventions/` 里的 design-log 和模板）。「输入」栏里的 PBI-40 ①～⑧，见产品日志 3.1 里 PBI-40 的备注。

| 文件 | 条 | 短名 | 输入 | PO 的意见 | 结论 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| design-log.md | §1 | 架构图（新） | PBI-47、48 |  | 改：图加「PO decides」的边（阶段之间）和测完回到前面阶段的虚线（back to an earlier stage）；节点标号补上新增的 22–26，27、28 写在图下一行；构思拆成发散、收敛；图下一行指向 27。依据：PO 决定（阶段之间由 PO 决定）；PBI-47；样板发现；Master 审停点 1（虚线的写法）。 | 已改 |
| design-log.md | 1 | Hard point, not the whole item | PBI-50 |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| design-log.md | 2 | Who | — |  | 改：去来源标签；「PO 决定什么」的指向从 SKILL.md 第 6 步改成约定 5（只留一份清单）；首句保持陈述句（给角色下定义）。依据：结构建议 4；Master 审停点 1（必改 2、建议 3）。 | 已改 |
| design-log.md | 3 | Open a design | PBI-50 |  | 改：去来源标签；排在 4（定分支）之后。依据：结构建议 4；样板发现（先定分支再填表头）。 | 已改 |
| design-log.md | 4 | Branch | — |  | 改：首句改祈使（Decide when the design opens…）；排到 3 之前；保留「Decide on the spot」标签。依据：结构建议 3；样板发现。 | 已改 |
| design-log.md | 5 | Ask the PO | PBI-40 ②；可能与 overview 9 重复 |  | 改：把「看 overview 9」扩成 PO 要决定的各处（触发清单），是「PO 决定什么」的唯一一份：每个阶段结束和测完收官或回头（27）、设计目标、挑出的 HMW 问题、选方案与合或比、原型多真、设计做完；去来源标签。依据：PBI-40 ②；PO 决定（阶段之间由 PO 决定）；结构建议 4；Master 审停点 1（必改 2）。清单取自本文件已有的「PO 决定」处，除阶段结束和测完之后两项外没有新规矩。 | 已改 |
| design-log.md | 6 | Five chapters, not five days | PBI-48；可能与 overview 15 重复 |  | 改：首句改祈使（Write one chapter per stage）；去来源标签。依据：结构建议 3、4。五章不变，不加 Review 章（PO 定）。 | 已改 |
| design-log.md | 7 | IDEO always in play | PBI-47 |  | 改：首句改成规矩（任何阶段按需用 ideo-kernel 的方法），「规矩在 SKILL.md」挪进括号；去来源标签。依据：结构建议 3、4。构思的发散要求另见 25。 | 已改 |
| design-log.md | 8 | Renamed terms | — |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| design-log.md | 9 | Experts when needed | PBI-48（共情） |  | 改：首句改成「听过当事人（23）之后写挑战、目标、问题」，不再是「先写」；去来源标签。依据：Master 审停点 1（必改 1：理顺 9 和 23 的先后）；结构建议 4。 | 已改 |
| design-log.md | 10 | Map and questions in the log | PBI-48（定义） |  | 改：去来源标签。依据：结构建议 4。POV 另见 24。 | 已改 |
| design-log.md | 11 | Lightning Demos | PBI-47 |  | 改：首句改祈使；去来源标签。依据：结构建议 3、4。 | 已改 |
| design-log.md | 12 | Isolated solutions | PBI-47、48 |  | 改：首句改祈使，开头加「点子池备齐之后（25）」；去来源标签；保留行内「Decide on the spot」。依据：结构建议 3、4；PBI-47。 | 已改 |
| design-log.md | 13 | Choosing is the key step | PBI-47 |  | 改：首句改祈使并拆成四句；「section 3.1」改「3.2」（模板加了点子池）；去来源标签。依据：结构建议 3、4；Master 提议 3（模板补格子）。 | 已改 |
| design-log.md | 14 | Combine or rumble | PBI-47 |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| design-log.md | 15 | Storyboard | PBI-47 |  | 改：改成「只在需要时写」的祈使句；「section 3.2」改「3.3」；去来源标签。依据：结构建议 3、4；Master 提议 3（模板补格子）。 | 已改 |
| design-log.md | 16 | Just enough prototype | PBI-48（原型） |  | 改：加一句「写明原型每一部分测哪个设计问题」；保留「Supplement」标签。依据：Master 提议 3。 | 已改 |
| design-log.md | 17 | Role-card test | PBI-48（测试） |  | 改：去来源标签。依据：结构建议 4。测前写判据、角色卡的局限另见 26。 | 已改 |
| design-log.md | 18 | Close as a Review | PBI-40 ①；两个入口（见 2.2）：结论按对照表回流产品日志，白纸设计收官时地图上的步骤拆成 PBI |  | 改：首句改祈使；「重写成一份 Review 文档」改成「压缩日志」，归档就是压缩后的日志，原 Supplement 段列的 Review 内容对到各章（挑战和设计问题→第 1 章，选中的方案→第 3 章，存着原型的提交→第 4 章，各问题的测试结论和回流去处→第 5 章）；结论按产品日志约定 2 的对照表回流，白纸设计收官时地图上的步骤拆成 PBI、先做哪些由 PO 排；去来源标签。依据：PO 决定（Review 和 Retro 是收官动作、不设章；两个入口）；PBI-40 ①；Master 提议 7（已按 PO 撤回）；结构建议 2、3、4。 | 已改 |
| design-log.md | 19 | Retro as in a Sprint | 可能与 sprint-log 19 重复 |  | 改：首句改祈使；去来源标签。依据：结构建议 3、4。 | 已改 |
| design-log.md | 20 | Resume from the header | — |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| design-log.md | 21 | Goal fixed, plan flexible | 可能与 overview 16 重复 |  | 改：首句改祈使；去来源标签。依据：结构建议 3、4。与 overview 16 并存的部分留作指向，没删。 | 已改 |
| design-log.md | 22 | Open a design for a question with no ready answer | PBI-50；两个入口（见 2.2） |  | 新：问题问的是「人要什么」「怎么才算好」又没有现成答案，就开设计、从共情起，不先出方案；写不出产品和 Product Goal 时，先开设计，让它去填产品日志。依据：PBI-50；PO 决定（两个入口）。 | 已改 |
| design-log.md | 23 | Start from the people | Master 提议 2 |  | 新（排在 9 之前）：共情先找当事人；PO 自己是当事人时先问具体经历，再请 PO 拍板，否则从 PO 能找来的用户起；之后才是文件和角色卡；每条发现标明来源（第一手 / 第二手）。依据：Master 提议 2；Master 审停点 1（必改 1：PO 是当事人的写法）；PBI-48（共情的重心）；PBI-50（二手材料当一手材料的教训）。模板 1.1 Findings 是对应的格子。 | 已改 |
| design-log.md | 24 | Say it as a Point of View | PBI-48；Master 提议 3 |  | 新：从共情的发现写出 POV（用户、需求、洞察），再由它写 HMW 问题；地图画流程，替代不了 POV。依据：PBI-48（定义的重心：POV 不是流程图）；Master 提议 3（模板补 POV 格子）。模板 2.2 Point of View 是对应的格子。 | 已改 |
| design-log.md | 25 | Diverge before you converge | PBI-47 |  | 新：先攒点子池再出隔离草图；至少两种方法，量优先、判断延后；池里有做法不同的点子（不只是细节不同）才算发散够。依据：PBI-47（至少选两样、产出量优先，顺序写死；「发散够」取同名文件说的「四版同质」的反面）。模板 3.1 Idea pool 是对应的格子。 | 已改 |
| design-log.md | 26 | Write the criteria before the test | Master 提议 5 |  | 新：测试前先写每个设计问题的是、否、还没答的判据，并写明角色卡不能证明什么。依据：Master 提议 5。模板 5.1 Criteria 是对应的格子。 | 已改 |
| design-log.md | 27 | Gates between stages | Master 提议 1、6；PO 决定 |  | 新：每个阶段结束，对着「日志里要有什么」和「检查」一栏看过；Master 查做得对不对，PO 拍板这一段的结果和进不进下一段；决定写在本章最后一行；测完的决定就是收官或回到答错的那一段（并入原 27）；检查栏取 IDEO 各模式的重心，另带「换一个没学过设计的人做，会不会做得一模一样」。依据：PO 决定（阶段之间由 PO 决定：拍板，不是验收）；Master 提议 1、6；PBI-48；Master 审停点 1（建议：27 并进 28）。规矩正文在 overview（短名 Product Owner decides between stages），这里只留门和指向。 | 已改 |
| design-log.md | 28 | A small design is still a design | Master 提议 4 |  | 新：设计很小（约一个会话）也留日志，每个阶段缩到一两行，阶段结束 PO 照样拍板；一个阶段也不跳，尤其是共情和发散（25）。依据：Master 提议 4；Master 审停点 1（必改 3：意思对，补不跳阶段）。 | 已改 |
| design-backlog-template.md | 模板 | Design log template | PBI-40 ①（设计 Review 的规格）；PBI-48 |  | 改（章节清单：1 Empathize：1.1 Findings、1.2 Challenge、1.3 Design goal、1.4 Design questions；2 Define：2.1 Map、2.2 Point of View、2.3 How Might We；3 Ideate：3.1 Idea pool、3.2 Solution、3.3 Storyboard；4 Prototype：4.1 Parts、4.2 Trial run；5 Test：5.1 Criteria、5.2 What showed up、5.3 Answers）。新增 1.1、2.2、3.1、4.1、5.1，原 1.1–1.3、2.2、3.1、3.2 顺延，原第 4、5 章只有一条注释、现各拆成小节（字句不变，只拆开）；头部 From 加「白纸」，Closes 行改成「压缩后归档」；每个阶段章的注释末加一句「本章以 PO 的决定收尾」；第 1 章注释写明先找当事人、据此写挑战、目标、问题；第 3 章注释加「先发散后收敛（25）」；不加 Review 章。依据：Master 提议 2、3、5；PBI-47、48；PO 决定（Review 是动作、不设章；阶段之间由 PO 决定；两个入口）；PBI-40 ①；Master 审停点 1（必改 1、建议 2）。 | 已改 |
| design-kernel/SKILL.md | 表 | Five Stages | PBI-47、48 |  | 改：五行「What happens」各加一句重心（共情改成「先从当事人起、每条发现带来源，据此写挑战、目标、问题」；定义：POV，不只画流程；构思：先发散后收敛、点子池；原型：为学不为交；测试：真实反应，「我错了」也是答案），条号引用补上 23–27；Use Protocol 第 6 步改成「PO 在每个阶段结束时拍板，还要定约定 5 列的那些事」（只留一份清单）。依据：PBI-47、48；Master 审停点 1（必改 1、2）。 | 已改 |
| overview.md | §1 | 架构图（新） | 现有「The map」；两个入口（见 2.2）：图加「白纸」入口 |  |  | 待看 |
| overview.md | 1 | One product log | 可能与 product-log 1 重复 |  |  | 待看 |
| overview.md | 2 | Sprints and designs side by side | — |  |  | 待看 |
| overview.md | 3 | Three layers | — |  |  | 待看 |
| overview.md | 4 | Folders | — |  |  | 待看 |
| overview.md | 5 | Where files go | 可能与 product-log 17、sprint-log 18 重复 |  |  | 待看 |
| overview.md | 6 | Names | — |  |  | 待看 |
| overview.md | 7 | Roles | — |  |  | 待看 |
| overview.md | 8 | Only the Product Owner must be human | — |  |  | 待看 |
| overview.md | 9 | Ask the Product Owner | PBI-40 ② |  |  | 待看 |
| overview.md | 10 | Product Owner as Developer | — |  |  | 待看 |
| overview.md | 11 | One Scrum Master per project | PBI-40 ⑧ |  |  | 待看 |
| overview.md | 12 | Who gets which work | PBI-40 ⑧ |  |  | 待看 |
| overview.md | 13 | Working conventions | PBI-40 ④ |  |  | 待看 |
| overview.md | 14 | When a revision applies | — |  |  | 待看 |
| overview.md | 15 | Templates record outputs | — |  |  | 待看 |
| overview.md | 16 | Goal fixed, plan flexible | 可能与 product-log 18、sprint-log 3、design-log 21 重复 |  |  | 待看 |
| overview.md | 表 | Departures from the official guides | — |  |  | 待看 |
| overview.md | §3 | 与官方不同（新） | 现有 Departures 表；各条里的 Departs 句（overview 2、8；product-log 12；sprint-log 2、7、10、16） |  |  | 待看 |
| product-log.md | §1 | 架构图（新） | — |  |  | 待看 |
| product-log.md | 1 | One product log | PBI-40 ⑦ |  |  | 待看 |
| product-log.md | 2 | Blank page | PBI-50；两个入口（见 2.2）：对照表只写在这一条 |  |  | 待看 |
| product-log.md | 3 | Facts first, then questions | — |  |  | 待看 |
| product-log.md | 4 | Product and Product Goal | — |  |  | 待看 |
| product-log.md | 5 | Two kinds of Done | — |  |  | 待看 |
| product-log.md | 6 | Stakeholders in a short table | — |  |  | 待看 |
| product-log.md | 7 | Architecture as a map | — |  |  | 待看 |
| product-log.md | 8 | No TBD | — |  |  | 待看 |
| product-log.md | 9 | Technical design stays out | — |  |  | 待看 |
| product-log.md | 10 | Seven columns | — |  |  | 待看 |
| product-log.md | 11 | Numbers, not ranks | — |  |  | 待看 |
| product-log.md | 12 | Items with the Scrum Master | — |  |  | 待看 |
| product-log.md | 13 | Status lives here | — |  |  | 待看 |
| product-log.md | 14 | Refine any time, finish in the Sprint | — |  |  | 待看 |
| product-log.md | 15 | Seven steps | PBI-50（第 4 步）；PBI-40 ⑤（在冲刺 Planning 里执行） |  |  | 待看 |
| product-log.md | 16 | Where refined content goes | — |  |  | 待看 |
| product-log.md | 17 | Fresh at every Review | — |  |  | 待看 |
| product-log.md | 18 | Goal fixed, plan flexible | 可能与 overview 16 重复 |  |  | 待看 |
| product-backlog-template.md | 模板 | Product log template | — |  |  | 待看 |
| sprint-log.md | §1 | 架构图（新） | 现有流程图（文件开头） |  |  | 待看 |
| sprint-log.md | 1 | One branch, one folder | — |  |  | 待看 |
| sprint-log.md | 2 | No end date | — |  |  | 待看 |
| sprint-log.md | 3 | Goal fixed, plan flexible | 可能与 overview 16 重复 |  |  | 待看 |
| sprint-log.md | 4 | Small work, small Sprint | — |  |  | 待看 |
| sprint-log.md | 5 | Stage 1: Why and what | PBI-40 ⑤ |  |  | 待看 |
| sprint-log.md | 6 | Stage 2: Refinement | PBI-40 ⑤；PBI-50 |  |  | 待看 |
| sprint-log.md | 7 | How is a plan, not steps | PBI-40 ⑤ |  |  | 待看 |
| sprint-log.md | 8 | Go-ahead | PBI-40 ⑤ |  |  | 待看 |
| sprint-log.md | 9 | Notes as you go | — |  |  | 待看 |
| sprint-log.md | 10 | Checkpoints, not stand-ups | PBI-40 ③ |  |  | 待看 |
| sprint-log.md | 11 | New work gets registered | — |  |  | 待看 |
| sprint-log.md | 12 | Structure before full text | — |  |  | 待看 |
| sprint-log.md | 13 | Full text for review | — |  |  | 待看 |
| sprint-log.md | 14 | The log is the handoff | — |  |  | 待看 |
| sprint-log.md | 15 | Tests: criteria first | — |  |  | 待看 |
| sprint-log.md | 16 | A reviewer is required | 可能与 overview 12 重复 |  |  | 待看 |
| sprint-log.md | 17 | Product Owner acceptance when written | — |  |  | 待看 |
| sprint-log.md | 18 | Review | — |  |  | 待看 |
| sprint-log.md | 19 | Retrospective | PBI-40 ⑥ |  |  | 待看 |
| sprint-log.md | 20 | One closing commit | — |  |  | 待看 |
| sprint-log.md | 21 | Special cases | 可能与 sprint-log 4、6，product-log 17，overview 16 重复 |  |  | 待看 |
| sprint-backlog-template.md | 模板 | Sprint log template | — |  |  | 待看 |
| scrum-kernel/SKILL.md | 节 | Working with the Design and IDEO Kernels | PBI-50 |  |  | 待看 |

## 连带改动

改一条规矩时，这条规矩在别处的说法（模板、命令、两份 SKILL.md、CLAUDE.md、README）一起改，每项登记在这里。状态填「待改 / 已改 / 已核」。

| 规矩 | 涉及的文件 | 状态 |
| --- | --- | --- |
| 来源标签只标例外（没有标签的就是作者的做法） | overview.md（13 的标签说明）、product-log.md 与 sprint-log.md 各条的标签、两份模板与 SKILL.md 里提到标签的地方 | design-log 已改；其余待改 |
| 阶段之间由 PO 决定（overview 新增一条，短名 Product Owner decides between stages） | overview.md（新条）、sprint-log.md（图与指向）；design-log.md 的图、5、27 已指向该短名 | design-log 已改；overview、sprint-log 待改 |
| 两个入口，同一份产品日志（对照表只写在 product-log 约定 2） | product-log.md（约定 2）、overview.md（图加「白纸」入口）；design-log.md 的 18、22 已指向 product-log 约定 2 | design-log 已改；其余待改 |
| Review 和 Retro 是收官动作、不设章；冲刺日志改成五章 | sprint-log.md、冲刺日志模板（第 4 章 Review 改成第 5 章 Test，3.2 Notes 改名 Increment notes）、scrum-kernel/SKILL.md、四个命令、CLAUDE.md「冲刺收官与归档」、README；design-log.md 的 18、19 已按此写 | design-log 已改；其余待改 |
| design-log 新增 22–28，原编号未动 | 第 7 项统一改号时：design-log.md、设计日志模板、design-kernel/SKILL.md、overview.md、sprint-log.md 里所有指向设计日志约定号的地方；全局记忆 plan-view-review、compact-instead-of-handoff 里的「sprint-log 约定 13、14」收官 Retro 时由 Master 处理 | 待改（第 7 项） |
| 设计日志模板的节号变了：第 1 章 Findings 排最前（1.1 Findings、1.2 Challenge、1.3 Design goal、1.4 Design questions），2.2 HMW→2.3，3.1 Solution→3.2，3.2 Storyboard→3.3 | design-log.md 的 13、15 与模板已改；已有的设计日志不受影响（本仓库当前没有进行中的设计） | 已改 |
| 「PO 决定什么」只留一份清单（design-log 5） | design-kernel/SKILL.md 的 Use Protocol 第 6 步和 design-log 2 已改成指向 design-log 5；scrum 这边 overview 7 的 PO 行是角色表，不是第二份清单，不动 | 已改 |
