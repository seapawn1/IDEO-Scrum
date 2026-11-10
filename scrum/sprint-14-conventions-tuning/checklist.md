# Sprint 14 审定清单

PO 逐行看；结论填「改 / 不改 / 挪到 PBI-xx」；状态填「待看 / 已定 / 已改 / 已核」。

「条」栏是改号前的号：scrum 这边是 5.1.2 文件里的号，design-log 是起草时的号（1–21 沿用 5.1.2，22–27 是新增）；「现号」栏是第 7 项重排之后文件里现在的号；结论里写的条号也是改号前的号，加了「现」字的是现在的号。对照表在本文件末。

路径都在 `plugins/ideo-scrum/skills/` 下：`scrum-kernel/`（`overview.md`、`SKILL.md`、`conventions/` 里的 product-log、sprint-log 和两份模板）、`design-kernel/`（`SKILL.md`、`conventions/` 里的 design-log 和模板）。「输入」栏里的 PBI-40 ①～⑧，见产品日志 3.1 里 PBI-40 的备注。

| 文件 | 条 | 现号 | 短名 | 输入 | PO 的意见 | 结论 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| design-log.md | §1 | — | 架构图（新） | PBI-47、48 |  | 改：图加「PO decides」的边（阶段之间）和测完回到前面阶段的虚线（back to an earlier stage）；节点标号补上新增的 22–25，26、27 写在图下一行；构思拆成发散、收敛；图下一行指向 26。依据：PO 决定（阶段之间由 PO 决定）；PBI-47；样板发现；Master 审停点 1（虚线的写法）。 | 已改 |
| design-log.md | 1 | 2 | Hard point, not the whole item | PBI-50 |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| design-log.md | 2 | 3 | Who | — |  | 改：去来源标签；「PO 决定什么」的指向从 SKILL.md 第 6 步改成约定 5（只留一份清单）；首句保持陈述句（给角色下定义）。依据：结构建议 4；Master 审停点 1（必改 2、建议 3）。 | 已改 |
| design-log.md | 3 | 5 | Open a design | PBI-50 |  | 改：去来源标签；排在 4（定分支）之后。依据：结构建议 4；样板发现（先定分支再填表头）。 | 已改 |
| design-log.md | 4 | 4 | Branch | — |  | 改：首句改祈使（Decide when the design opens…）；排到 3 之前；保留「Decide on the spot」标签。依据：结构建议 3；样板发现。 | 已改 |
| design-log.md | 5 | 21 | Ask the PO | PBI-40 ②；可能与 overview 9 重复 |  | 改：把「看 overview 9」扩成 PO 要决定的各处（触发清单），是「PO 决定什么」的唯一一份：每个阶段结束和测完收官或回头（26）、设计目标、挑出的 HMW 问题、选方案与合或比、原型多真、设计做完；去来源标签。依据：PBI-40 ②；PO 决定（阶段之间由 PO 决定）；结构建议 4；Master 审停点 1（必改 2）。清单取自本文件已有的「PO 决定」处，除阶段结束和测完之后两项外没有新规矩。 | 已改 |
| design-log.md | 6 | 22 | Five chapters, not five days | PBI-48；可能与 overview 15 重复 |  | 改：首句改祈使（Write one chapter per stage）；去来源标签。依据：结构建议 3、4。五章不变，不加 Review 章（PO 定）。 | 已改 |
| design-log.md | 7 | 9 | IDEO always in play | PBI-47 |  | 改：首句改成「每个阶段都把书的步骤和这一阶段的 IDEO 模式一起做，规矩见 SKILL.md」，规矩只写在 SKILL.md 一处；去掉「或代替」（不是二选一）；去来源标签。依据：PO 决定（IDEO 一定要融合进设计冲刺，两样一起做）；结构建议 3、4。 | 已改 |
| design-log.md | 8 | 23 | Renamed terms | — |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| design-log.md | 9 | 7 | Experts when needed | PBI-48（共情） |  | 改：首句改成「听过当事人（23）之后写挑战、目标、问题」，不再是「先写」；去来源标签。依据：Master 审停点 1（必改 1：理顺 9 和 23 的先后）；结构建议 4。 | 已改 |
| design-log.md | 10 | 8 | Map and questions in the log | PBI-48（定义） |  | 改：加一句「HMW 对着地图写，同时参考第 1 章的挑战、目标、问题」；去来源标签。依据：PO 决定（去掉 POV：挑战、目标、问题加地图合起来就是 POV，定义一章就是地图和 HMW）；结构建议 4。 | 已改 |
| design-log.md | 11 | 10 | Lightning Demos | PBI-47 |  | 改：首句改祈使；去来源标签。依据：结构建议 3、4。 | 已改 |
| design-log.md | 12 | 12 | Isolated solutions | PBI-47、48 |  | 改：首句改祈使，写成「各自先发散（24）再出草图」；草图的依据去掉「或」，改成第 1、2 章、已收集的点子、sketch.md 和 ideo-kernel 的构思方法，两样一起用；去来源标签；保留行内「Decide on the spot」。依据：结构建议 3、4；PBI-47；PO 决定（点子由各子代理自己消化、不落盘；IDEO 与书的步骤两样一起做）。 | 已改 |
| design-log.md | 13 | 13 | Choosing is the key step | PBI-47 |  | 改：首句改祈使并拆成四句；去来源标签。依据：结构建议 3、4。节号仍是 3.1，模板没加小节。 | 已改 |
| design-log.md | 14 | 14 | Combine or rumble | PBI-47 |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| design-log.md | 15 | 15 | Storyboard | PBI-47 |  | 改：改成「只在需要时写」的祈使句；去来源标签。依据：结构建议 3、4。节号仍是 3.2。 | 已改 |
| design-log.md | 16 | 16 | Just enough prototype | PBI-48（原型） |  | 改：试跑的发现写进测试一章；原型各部分列在原型一章，各写明测哪个设计问题；保留「Supplement」标签。依据：Master 提议 3（原型每一部分测哪个问题）；PO 决定（原型一章只留各部分一张表，试跑并到测试一章）。 | 已改 |
| design-log.md | 17 | 17 | Role-card test | PBI-48（测试） |  | 改：去来源标签。依据：结构建议 4。测前写判据、角色卡的局限另见 26。 | 已改 |
| design-log.md | 18 | 19 | Close as a Review | PBI-40 ①；两个入口（见 2.2）：结论按对照表回流产品日志，白纸设计收官时地图上的步骤拆成 PBI |  | 改：首句改祈使；「重写成一份 Review 文档」改成「压缩日志」，归档就是压缩后的日志，原 Supplement 段列的 Review 内容对到各章（挑战和设计问题→第 1 章，选中的方案→第 3 章，存着原型的提交→第 4 章，各问题的测试结论和回流去处→第 5 章）；结论按产品日志约定 2 的对照表回流，白纸设计收官时地图上的步骤拆成 PBI、先做哪些由 PO 排；去来源标签。依据：PO 决定（Review 和 Retro 是收官动作、不设章；两个入口）；PBI-40 ①；Master 提议 7（已按 PO 撤回）；结构建议 2、3、4。 | 已改 |
| design-log.md | 19 | 20 | Retro as in a Sprint | 可能与 sprint-log 19 重复 |  | 改：首句改祈使；去来源标签。依据：结构建议 3、4。 | 已改 |
| design-log.md | 20 | 24 | Resume from the header | — |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| design-log.md | 21 | 25 | Goal fixed, plan flexible | 可能与 overview 16 重复 |  | 改：首句改祈使；去来源标签。依据：结构建议 3、4。与 overview 16 并存的部分留作指向，没删。 | 已改 |
| design-log.md | 22 | 1 | Open a design for a question with no ready answer | PBI-50；两个入口（见 2.2） |  | 新：问题问的是「人要什么」「怎么才算好」又没有现成答案，就开设计、从共情起，不先出方案；写不出产品和 Product Goal 时，先开设计，让它去填产品日志。依据：PBI-50；PO 决定（两个入口）。 | 已改 |
| design-log.md | 23 | 6 | Start from the people | Master 提议 2 |  | 新（排在 9 之前）：共情先找当事人；PO 自己是当事人时先问具体经历，再请 PO 拍板，否则从 PO 能找来的用户起；之后才是文件和角色卡；发现写进挑战、目标、问题三节并注明来源（第一手 / 第二手）。依据：Master 提议 2；Master 审停点 1（必改 1）；PO 决定（去掉单列的发现一节，发现附在 1.1–1.3）；PBI-48；PBI-50。 | 已改 |
| design-log.md | 24 | 11 | Diverge before you converge | PBI-47 |  | 新：给每个出隔离草图的子代理下任务时，要它先发散（至少两种方法，先求量、不评判）再收敛成自己那一份草图；点子是工作材料，不进日志。依据：PBI-47（至少选两样、产出量优先，顺序写死；不让四版同质）；PO 决定（点子由各子代理自己消化，去掉点子池一节）。 | 已改 |
| design-log.md | 25 | 18 | Write the criteria before the test | Master 提议 5 |  | 新：测试前先在第 5 章写每个设计问题的是、否、还没答的判据，并写明角色卡不能证明什么。依据：Master 提议 5；PO 决定（测试一章不分小节，判据写在这一章里）。 | 已改 |
| design-log.md | 26 | 26 | Gates between stages | Master 提议 1、6；PO 决定 |  | 新：每个阶段结束，对着「日志里要有什么」和「检查」一栏看过；Master 查做得对不对，PO 拍板这一段的结果和进不进下一段；决定写在本章最后一行；测完的决定就是收官或回到答错的那一段；「日志里有什么」一栏照模板各章写（共情：挑战、目标、问题和发现的来源；定义：地图和 HMW；构思：选中的方案和故事板；原型：各部分和各自测的问题；测试：判据、试跑、测试、答案和回流）；检查栏取 IDEO 各模式的重心（定义一行改成「HMW 是对着地图和第 1 章写出来的」），另带「换一个没学过设计的人做，会不会做得一模一样」。依据：PO 决定（阶段之间由 PO 决定：拍板，不是验收；模板各章的结构；去掉 POV）；Master 提议 1、6；PBI-48；Master 审停点 1（建议：测完的决定并进门）。规矩正文在 overview（短名 Product Owner decides between stages），这里只留门和指向。 | 已改 |
| design-log.md | 27 | 27 | A small design is still a design | Master 提议 4 |  | 新：设计很小（约一个会话）也留日志，每个阶段缩到一两行，阶段结束 PO 照样拍板；一个阶段也不跳，尤其是共情和发散（24）。依据：Master 提议 4；Master 审停点 1（必改 3：意思对，补不跳阶段）。 | 已改 |
| design-backlog-template.md | 模板 | — | Design log template | PBI-40 ①（设计 Review 的规格）；PBI-48 |  | 改（章节清单：1 Empathize：1.1 Challenge、1.2 Design goal、1.3 Design questions；2 Define：2.1 Map、2.2 How Might We；3 Ideate：3.1 Solution、3.2 Storyboard；4 Prototype：不分小节，只一张表（部分｜测哪个设计问题｜在哪里）；5 Test：不分小节，一条注释）。节和节号与改前相同；改的是：头部 From 加「白纸」，Closes 行改成「压缩后归档」；第 4 章原来的一条注释换成「各部分」那张表；第 5 章注释加「试跑的发现」，章注释写明判据先写在这一章；每个阶段章的注释末加一句「本章以 PO 的决定收尾」；第 1 章注释写明先找当事人、据此写挑战、目标、问题，发现附在这三节里并注明来源；第 2 章注释写明 HMW 对着地图写、参考第 1 章；第 3 章注释加「各草图先发散再收敛（24）」；不加 Review 章。依据：PO 决定（模板结构：不单列发现、POV、点子池，原型只留各部分表，测试一章不分小节；去掉 POV；Review 是动作、不设章；阶段之间由 PO 决定；IDEO 融合进每个阶段；两个入口）；Master 提议 3、5；PBI-47、48；PBI-40 ①；Master 审停点 1（必改 1、建议 2）。 | 已改 |
| design-kernel/SKILL.md | 表 | — | Five Stages | PBI-47、48 |  | 改：五阶段表第二列写 IDEO 模式文件和它的重心（共情：理解人，先从当事人起；定义：框定问题，HMW 对着地图和第 1 章写；构思：先发散再收敛；原型：为学不为交；测试：真实反应，「我错了」也是答案），第三列「书的步骤」是原来的字句；表里不指定方法名；「IDEO methods are always in play」改成「IDEO is required in every stage」：这里的设计冲刺只是骨架，每个阶段需要的详细方法论到 ideo-kernel 里找，阶段前读这一阶段的模式文件、照它的重心做、从那里挑方法、用前读方法文件，书的步骤和 IDEO 两样一起做；去掉原来的两个方法名例子；序言里「when you need them」改成「before the stage begins」；Use Protocol 第 5 步改成每个阶段都用，第 6 步改成「PO 在每个阶段结束时拍板，还要定约定 5 列的那些事」（只留一份清单）。依据：PO 决定（IDEO 一定要融合进设计冲刺、写成必须；不给每个阶段指定方法名；去掉 POV）；PBI-47、48；Master 审停点 1（必改 1、2）。 | 已改 |
| overview.md | §1 | — | 架构图（新） | 现有「The map」；两个入口（见 2.2）：图加「白纸」入口 |  | 改：「The map」重画——加「白纸」入口（产品写不出时直接进设计）；冲刺一侧由 Planning、Go-ahead、Build、Review、Sprint Review、Retro 七个节点改成五个阶段（Why、What、How、Increment、Test），阶段之间标「PO decides」，Test 之后可回 Increment（虚线），收官画成一个节点（Review 和 Retro 是动作，不是阶段）。依据：PO 决定（两个入口，同一份产品日志；阶段之间由 PO 决定；冲刺五个阶段，Review 和 Retro 不设章）；结构方向（每份约定先一张图）。这张图画整个流程，节点不标条号，和另三份约定里标条号的图不同。 | 已改 |
| overview.md | 1 | 1 | One product log | 可能与 product-log 1 重复 |  | 改：去来源标签。依据：结构建议 4。与 product-log 1 说的是同一件事的两面（这里是总规矩，那里是怎么写），见 3.2「不清楚的地方」。 | 已改 |
| overview.md | 2 | 2 | Sprints and designs side by side | — |  | 改：首句改祈使（Treat Sprints and designs as peers under the product log）；去来源标签；开设计的情形加第三种：产品和 Product Goal 还写不出（白纸，指向 product-log 2）；整句「Departs from the Scrum Guide on purpose …」的理由搬进 Departures 表，这里只留指向。依据：结构建议 3、4；PO 决定（两个入口；overview 多一节写与官方不同的地方和理由）。 | 已改 |
| overview.md | 3 | 3 | Three layers | — |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| overview.md | 4 | 4 | Folders | — |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| overview.md | 5 | 5 | Where files go | 可能与 product-log 17、sprint-log 18 重复 |  | 改：去来源标签；设计的归档由「Reviews」改成「compressed design logs」（设计收官归档的就是压缩后的日志）；末尾加一句：工作材料不进日志，真正关键的内容可存进项目的记忆或说明文件，大份重要的文件放进 scrum/documents/（不写具体工具）。依据：结构建议 4；PO 决定（设计收官压缩日志、不设 Review 章；overview 补一句）。与 product-log 17、sprint-log 18 的重复：「整个 scrum/ 保鲜」的规矩只写在 sprint-log 的 Review（原 18，现 17），product-log 17 指向它，documents/ 的一句留在本条。 | 已改 |
| overview.md | 6 | 6 | Names | — |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| overview.md | 7 | 7 | Roles | — |  | 改：去来源标签；角色表 PO 一行的「决定」栏加「每个阶段结束时的决定」，并指向新条（现 11）。依据：结构建议 4；PO 决定（阶段之间由 PO 决定）。 | 已改 |
| overview.md | 8 | 8 | Only the Product Owner must be human | — |  | 改：去来源标签；整句「Departs from the SGEP on purpose …」的理由搬进 Departures 表，这里只留指向。依据：结构建议 3、4；PO 决定（overview 多一节写与官方不同的地方和理由）。 | 已改 |
| overview.md | 9 | 9 | Ask the Product Owner | PBI-40 ② |  | 改：去来源标签。PBI-40 ②（「拿不准就问 PO」的触发清单）：设计这边的清单在 design-log 5（现 21）；Scrum 这边没有另列，PO 要决定的事分写在角色表 PO 一行、新条（阶段结束的决定）和 sprint-log 24，要不要也汇成一份清单，请 Master 或 PO 定（见 3.2「不清楚的地方」）。依据：结构建议 4；PBI-40 ②。 | 已改 |
| overview.md | 10 | 10 | Product Owner as Developer | — |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| overview.md | 新 | 11 | Product Owner decides between stages | PO 决定（阶段之间由 PO 决定） |  | 新：这条规矩的正文只写在这里：每个阶段结束，PO 拍板——定下这一段的结果，决定进不进下一段；是做决定，不是审阅或验收，检查做得对不对是 Scrum Master 的事；只到阶段这一层，不细到阶段里的每一步；PO 可明确交给 Scrum Master；点明冲刺有五个阶段（指向 sprint-log 24）、设计有五个（指向 design-log 26）。依据：PO 决定（阶段之间由 PO 决定，2026-11-10 补充）；Master 定（跨文件的规矩正文只写在 overview 一处）。 | 已改 |
| overview.md | 11 | 12 | One Scrum Master per project | PBI-40 ⑧ |  | 改：去来源标签。PBI-40 ⑧（Developer 在别的工具里）：本冲刺没做，见 3.2「不清楚的地方」。依据：结构建议 4。 | 已改 |
| overview.md | 12 | 13 | Who gets which work | PBI-40 ⑧ |  | 改：去来源标签；指向 sprint-log 的「A reviewer is required」的条号随改号更新（16→14）。PBI-40 ⑧ 同上。依据：结构建议 4。 | 已改 |
| overview.md | 13 | 14 | Working conventions | PBI-40 ④ |  | 改：来源标签的说明改成「只有例外带标签：没有标签的就是作者的做法；Supplement、Decide on the spot 单独标」，删掉「Author's practice」这个标签；加一句：越过一条约定时，把做了什么、为什么写进日志的笔记（冲刺日志的 Increment notes，或设计日志里相关的那一章）。依据：结构建议 4；PBI-40 ④。 | 已改 |
| overview.md | 14 | 15 | When a revision applies | — |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| overview.md | 15 | 16 | Templates record outputs | — |  | 改：去来源标签；末句「remarks go in the notes」改成「冲刺日志的 Increment notes，或设计日志里相关的那一章」（冲刺日志的笔记现在是第 4 章，设计日志没有笔记节）。依据：结构建议 4；PO 决定（冲刺日志五章，3.2 Notes 改名 Increment notes 单独成章）。 | 已改 |
| overview.md | 16 | 17 | Goal fixed, plan flexible | 可能与 product-log 18、sprint-log 3、design-log 21 重复 |  | 改：去来源标签；正文不动，这条规矩只写在这里。product-log 18、sprint-log 3（现 20）、design-log 21（现 25）各留本日志特有的做法（改什么、记在哪），通用部分指向本条。依据：结构建议 2、4。 | 已改 |
| overview.md | 表 | — | Departures from the official guides | — |  | 改：三列（Here / The official guide / See）改成四列，加「Why」一列；官方原话加引号。依据：PO 决定（overview 多一节写与官方不同的地方和理由）。其余见下一行。 | 已改 |
| overview.md | §3 | — | 与官方不同（新） | 现有 Departures 表；各条里的 Departs 句（overview 2、8；product-log 12；sprint-log 2、7、10、16） |  | 改：这一节就是现有的 Departures 表，不另写一节：理由从各条里搬来，每条原来的「Departs … on purpose, where …」整句换成一句指向（overview 2、8；product-log 12；sprint-log 2、7、10、16）；导语改成「每一条在这里写一次，附理由」；文件开头的说明加一句指向这一节；「Closed logs are kept in scrum/documents/」一行官方没有对应说法，Why 栏写「—」，见 3.2「不清楚的地方」。依据：PO 决定（overview 多一节，写与官方不同的地方和理由）；结构建议 3。 | 已改 |
| product-log.md | §1 | — | 架构图（新） | — |  | 新：流程图——Starting（1–3）、Each part（4–9）、Items（10–13）、Refinement（14–16）、Keeping it fresh（17）五个节点，18 写在图下一行；「产品写不出」这条边通向设计，结论流回；节点名和下面的小标题同名，约定按图的顺序排，条号没动。开头的说明加一句：没有标签的约定就是作者的做法。依据：PO 决定（每份约定先一张图）；结构建议 1、4。 | 已改 |
| product-log.md | 1 | 1 | One product log | PBI-40 ⑦ |  | 改：首句改祈使（Start every project, new or old, by writing one product log from the template）；去来源标签；加老项目怎么写：照已有的 README、未关的 issue、旧计划写，历史留在版本控制里，写不出的部分按 2 处理。依据：结构建议 3、4；PBI-40 ⑦。「Start every project, new or old」与 overview 1 的说法有重叠，见 3.2「不清楚的地方」。 | 已改 |
| product-log.md | 2 | 2 | Blank page | PBI-50；两个入口（见 2.2）：对照表只写在这一条 |  | 改：首句改祈使（Write into the product log what you can define; replace what you cannot with the matching item of a design）；去来源标签；加对照表（设计的挑战→1.1 产品，设计目标→1.2 Product Goal，设计问题测试后答出来的→1.3 完成标准、没答出来的变成 PBI，地图最上面的人→2.1 利益相关者，地图→2.2 架构，地图上的步骤→3 PBI 并各放在地图的一步上），对照表只写在这一条；被替换的那一节写明由哪份设计在回答并链过去，不抄设计日志；利益相关者表可以先写（设计一开始就用角色卡）；什么时候从设计开始，指向 design-log 1（现 1）。依据：PO 决定（两个入口，同一份产品日志）；PBI-50。 | 已改 |
| product-log.md | 3 | 3 | Facts first, then questions | — |  | 改：首句改祈使（Have the Scrum Master look up the facts itself）；保留 Supplement 标签。依据：结构建议 3。 | 已改 |
| product-log.md | 4 | 4 | Product and Product Goal | — |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| product-log.md | 5 | 5 | Two kinds of Done | — |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| product-log.md | 6 | 6 | Stakeholders in a short table | — |  | 改：首句改祈使（List the stakeholders in section 2.1 in a short table）；去来源标签。依据：结构建议 3、4。 | 已改 |
| product-log.md | 7 | 7 | Architecture as a map | — |  | 改：首句改祈使（Start section 2.2 with one map）；去来源标签。依据：结构建议 3、4。 | 已改 |
| product-log.md | 8 | 8 | No TBD | — |  | 改：首句改祈使（Turn an unclear point into an item）；去来源标签。依据：结构建议 3、4。 | 已改 |
| product-log.md | 9 | 9 | Technical design stays out | — |  | 改：首句改祈使（Keep technical design out）；去来源标签。依据：结构建议 3、4。 | 已改 |
| product-log.md | 10 | 10 | Seven columns | — |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| product-log.md | 11 | 11 | Numbers, not ranks | — |  | 改：首句改祈使（Number items to count them, and keep every number unique）；去来源标签。依据：结构建议 3、4。 | 已改 |
| product-log.md | 12 | 12 | Items with the Scrum Master | — |  | 改：首句改祈使（Let the Product Owner decide the items together with the Scrum Master）；去来源标签；整句「Departs … on purpose, where …」的理由搬进 overview 的 Departures 表，这里只留指向。依据：结构建议 3、4；PO 决定（理由搬到 overview 第 3 节）。 | 已改 |
| product-log.md | 13 | 13 | Status lives here | — |  | 改：首句改祈使（Write an item's status in the product log only）；去来源标签。依据：结构建议 3、4。 | 已改 |
| product-log.md | 14 | 14 | Refine any time, finish in the Sprint | — |  | 改：首句改祈使（Refine in the product log only to add detail）；去来源标签。依据：结构建议 3、4。 | 已改 |
| product-log.md | 15 | 15 | Seven steps | PBI-50（第 4 步）；PBI-40 ⑤（在冲刺 Planning 里执行） |  | 改：七步挪到 sprint-log 6（精化是冲刺 Planning 里做的事，在那里一次读完，不用同时开两份约定）；这里只留「按 sprint-log 6 的七步一条一条精化」和「已在这里写全的验收标准，冲刺日志里不重抄」两句；七步里第 4 步加「没有现成答案的问题（人要什么、怎么才算好）开设计」并指向 design-log 1（现 1）。依据：PBI-40 ⑤；PBI-50；结构建议 2（一条规矩只写一处）。 | 已改 |
| product-log.md | 16 | 16 | Where refined content goes | — |  | 改：首句改祈使（Put refined content where it belongs）；去来源标签。依据：结构建议 3、4。 | 已改 |
| product-log.md | 17 | 17 | Fresh at every Review | — |  | 改：首句改祈使（At every Review, move done items to section 3.2）；去来源标签；末句「整个 scrum/ 过一遍」仍指向 sprint-log 的 Review（原 18，现 17），措辞没动。依据：结构建议 3、4。 | 已改 |
| product-log.md | 18 | 18 | Goal fixed, plan flexible | 可能与 overview 16 重复 |  | 改：首句改祈使（Refine items and acceptance criteria at any time; let only the Product Owner change the Product Goal）；去来源标签；仍指向 overview 的通用规矩（原 16，现 17）。依据：结构建议 2、3、4。 | 已改 |
| product-backlog-template.md | 模板 | — | Product log template | — |  | 不改（已核）：模板的章节与注释和新约定不冲突，里面指向 product-log 条号的地方（4、6、10–13、18）改号后仍对得上，因为产品日志约定没改号。依据：核对，无新依据。 | 已核 |
| sprint-log.md | §1 | — | 架构图（新） | 现有流程图（文件开头） |  | 改：现有流程图重画成五个阶段——Opening（1–3）、Why（4）、What（5–6）、How（7–8）、Increment（9–12）、Test（13–16）、Closing（17–19）七个节点，阶段之间标「PO decides」（Why→What 定 Sprint Goal；What→How 定精化到此为止；How→Increment 是放行；Increment→Test 定可以测；Test 之后定收官或回去），「难点开设计」和「学到的东西流回」两条边保留；Throughout（20–24）写在图下一行。依据：PO 决定（冲刺五个阶段；阶段之间由 PO 决定；冲刺日志五章）；结构建议 1。 | 已改 |
| sprint-log.md | 1 | 1 | One branch, one folder | — |  | 改：首句改祈使（Give each Sprint one branch …）；去来源标签。依据：结构建议 3、4。 | 已改 |
| sprint-log.md | 2 | 2 | No end date | — |  | 改：首句改祈使（Close a Sprint when its goal is met or the Product Owner stops it）；去来源标签；整句「Departs from the Scrum Guide on purpose …」的理由搬进 overview 的 Departures 表，这里只留指向。依据：结构建议 3、4；PO 决定（理由搬到 overview 第 3 节）。 | 已改 |
| sprint-log.md | 3 | 20 | Goal fixed, plan flexible | 可能与 overview 16 重复 |  | 改：首句改成「Hold the Sprint Goal and the Definition of Done」并指向 overview 的通用规矩（原 16，现 17），后面留本日志特有的做法（怎么重谈、变更记在第 4 章 Increment notes）；挪到 Throughout。依据：结构建议 1、2；PO 决定（3.2 Notes 改名 Increment notes 单独成章）。 | 已改 |
| sprint-log.md | 4 | 3 | Small work, small Sprint | — |  | 改：首句改祈使（Open a Sprint even for work of half an hour to one session）；去来源标签；加「PO 仍在每个阶段结束时拍板」。依据：结构建议 3、4；PO 决定（阶段之间由 PO 决定）。「小 Sprint 也一样」是照设计日志小设计（Master 提议 4）类推的，没有直接依据，见 3.2「不清楚的地方」。 | 已改 |
| sprint-log.md | 5 | 4、5 | Stage 1: Why and what → Stage 1: Why；Stage 2: What — select the items | PBI-40 ⑤ |  | 拆成两条：现 4（Stage 1: Why）留定 Sprint Goal、挑 Definition of Done 的项、卡住时用 IDEO 方法；现 5（Stage 2: What — select the items）接选条目（逐字抄进 2.1、五列、缺的先进产品日志）；去来源标签。依据：PO 决定（冲刺五个阶段：Why、What、How、Increment、Test）；结构建议 1（按图的顺序排）。 | 已改 |
| sprint-log.md | 6 | 6 | Stage 2: Refinement | PBI-40 ⑤；PBI-50 |  | 改：七步从 product-log 15 搬进来，列成一个有序清单（一次读完，不再同时开两份约定）；首句改祈使（Refine the items one at a time）；第 4 步加「没有现成答案的问题（人要什么、怎么才算好）开设计」并指向 design-log 1（现 1）；原来单列的「A point that needs research becomes a design」「Last, the Developer confirms that nothing is unclear」与七步的第 4、6 步重复，删去；去来源标签。依据：PBI-40 ⑤；PBI-50；结构建议 2、3、4。 | 已改 |
| sprint-log.md | 7 | 7 | How is a plan, not steps | PBI-40 ⑤ |  | 改：首句改祈使（The Developer writes chapter 3 as a plan …）；写明区别一次：plan 是计划怎么做出选中条目，写到做法这一层、不写步骤，不是设计里选出的方案——设计若给了方案，plan 是怎么把它做出来；「section 3.1」改「chapter 3」；去来源标签；整句「Departs … on purpose …」的理由搬进 Departures 表。依据：PO 决定（How 写成类似方案，用 plan 不用 solution 并写明区别；冲刺日志五章）；结构建议 3、4。PBI-40 ⑤ 这里没有要改的：这一条本来就在 sprint-log 里。 | 已改 |
| sprint-log.md | 8 | 8 | Go-ahead | PBI-40 ⑤ |  | 改：首句改祈使（Start building only after the Product Owner's go-ahead）；去来源标签；「section 3.1」改「chapter 3」。依据：结构建议 3、4；PO 决定（冲刺日志五章）。 | 已改 |
| sprint-log.md | 9 | 9 | Notes as you go | — |  | 改：「section 3.2」改「chapter 4, Increment notes」，「section 3.1」改「chapter 3」；去来源标签。依据：PO 决定（3.2 Notes 改名 Increment notes 单独成章）；结构建议 4。 | 已改 |
| sprint-log.md | 10 | 10 | Checkpoints, not stand-ups | PBI-40 ③ |  | 改：首句改祈使并写明触发时机：每个阶段结束时、AI 卡住时、PO 问进展时；去来源标签；整句「Departs … Daily Scrum …」的理由搬进 Departures 表。依据：PBI-40 ③；PO 决定（阶段之间由 PO 决定）；结构建议 3、4。 | 已改 |
| sprint-log.md | 11 | 21 | New work gets registered | — |  | 改：去来源标签；挪到 Throughout（贯穿全程）。依据：结构建议 1、4。 | 已改 |
| sprint-log.md | 12 | 11 | Structure before full text | — |  | 改：去来源标签；编入 Increment 一组。依据：结构建议 1、4。 | 已改 |
| sprint-log.md | 13 | 12 | Full text for review | — |  | 改：去来源标签；编入 Increment 一组。依据：结构建议 1、4。 | 已改 |
| sprint-log.md | 14 | 22 | The log is the handoff | — |  | 改：首句改祈使（Write no separate handoff documents）；去来源标签；挪到 Throughout。依据：结构建议 1、3、4。 | 已改 |
| sprint-log.md | 15 | 13 | Tests: criteria first | — |  | 改：去来源标签；编入 Test 一组。依据：结构建议 1、4。 | 已改 |
| sprint-log.md | 16 | 14 | A reviewer is required | 可能与 overview 12 重复 |  | 改：首句改祈使（Have someone other than the builder review）；去来源标签；整句「Departs … Instilling quality …」的理由搬进 Departures 表；编入 Test 一组。依据：结构建议 1、3、4。 | 已改 |
| sprint-log.md | 17 | 15 | Product Owner acceptance when written | — |  | 改：首句改祈使（Ask for formal acceptance only when …）；去来源标签；编入 Test 一组。依据：结构建议 1、3、4。 | 已改 |
| sprint-log.md | 新 | 16 | Stage 5: Test | PO 决定（冲刺日志五章） |  | 新：第 5 章 Test 记什么：Developer 的测试、审阅人的检查（默认 Scrum Master）、PO 的端到端测试，以及 Definition of Done 和验收标准逐项的结果；问题当场改，改完再测。依据：PO 决定（冲刺日志第 5 章是 Test；Developer 的测试、审阅、PO 的端到端测试都记在这一章）。 | 已改 |
| sprint-log.md | 18 | 17 | Review | — |  | 改：首句改祈使（Close with a Review）；去掉「补上 Review 章」（Review 不设章）和备料那一串（Increment、Definition of Done、验收标准逐项已记在第 5 章 Test）；加「利益相关者的看法和对产品日志、Product Goal 的改动写进产品日志」；「翻一遍 scrum/documents/ 删过时的」并进「把整个 scrum/ 过一遍」，指向 overview 5；去来源标签。依据：PO 决定（Review 是压缩日志、归档、保鲜产品日志，利益相关者的看法落到产品日志；不设 Review 章）；结构建议 3、4。 | 已改 |
| sprint-log.md | 19 | 18 | Retrospective | PBI-40 ⑥ |  | 改：首句改祈使（Hold the Retrospective as an action at close, with no chapter in the log）；去来源标签；加「没有记忆文件也没有说明文件时，就新建一个说明文件」。依据：PO 决定（Retro 是收官动作，不设章）；PBI-40 ⑥；结构建议 3、4。 | 已改 |
| sprint-log.md | 20 | 19 | One closing commit | — |  | 改：去来源标签。依据：结构建议 4。 | 已改 |
| sprint-log.md | 21 | 23 | Special cases | 可能与 sprint-log 4、6，product-log 17，overview 16 重复 |  | 改：首句改成「Two cases need a rule of their own」；去来源标签；表里删去已有条覆盖的五行：审阅或验收没过（现在是 Test 一章的「当场改、改完再测」和 PO 的「回去」）、精化遇到难点（sprint-log 6 第 4 步）、收官时没做完的条目（product-log 17）、Sprint Goal 过时（overview 17）、活很小（sprint-log 小 Sprint 一条），只留两行。依据：结构建议 2（大半在重复别的条）。 | 已改 |
| sprint-log.md | 新 | 24 | The Product Owner decides at the end of each stage | PO 决定（阶段之间由 PO 决定） |  | 新：写明每个阶段 PO 决定什么：Why 定 Sprint Goal；What 定精化到此为止；How 放行；Increment 定可以进入测试；Test 定收官（做 Review、Retro）还是回去；决定写在该阶段章节的最后一行；规矩正文指向 overview 的短名，这里不重写。依据：PO 决定（冲刺五个阶段结束时各拍一次板，内容如此）；Master 定（规矩正文只写在 overview 一处）。 | 已改 |
| sprint-backlog-template.md | 模板 | — | Sprint log template | — |  | 改（章节清单：1 Why：1.1 Sprint Goal、1.2 Definition of Done；2 What：2.1 Product Backlog Items、2.2 Refinement；3 How：不分节；4 Increment notes：不分节；5 Test：不分节；Review、Retro 不设章）。改的是：原 3.1 How 的小标题去掉，第 3 章就是一份 plan（注释用 plan，不用 solution，区别写在冲刺约定 7）；原 3.2 Notes 改名 Increment notes，单独成第 4 章；原第 4 章 Review 删掉，换成第 5 章 Test（注释写明记 Developer 的测试、审阅人的检查、PO 的端到端测试、DoD 和验收标准逐项的结果，问题当场改、改完再测）；头部「Keep every heading」那行改指第 4 章；各章注释末写明 PO 的决定（冲刺约定 24）；2.1 的指向改到约定 22（现 5）。依据：PO 决定（冲刺日志五章，五个阶段；第 5 章叫 Test；Review 和 Retro 不设章；How 写成类似方案；How 用 plan 不用 solution；Test 一章不分小节）。 | 已改 |
| scrum-kernel/SKILL.md | 节 | — | Working with the Design and IDEO Kernels | PBI-50 |  | 改：分工那一段加两句：写产品日志之前也这样判断——凭现有的了解写不出产品和 Product Goal，就从设计开始，让它去填产品日志（指向 product-log 2）；「人要什么、怎么才算好」又没有现成答案的问题，一律先走设计（指向 design-log 1，现 1）；约定表里 sprint-log 一行的描述改成「The five stages of a Sprint — Why, What, How, Increment, Test — and its close」（原：Planning, building, reviewing, and closing a Sprint）。依据：PBI-50；PO 决定（两个入口；冲刺五个阶段）。 | 已改 |

## 连带改动

改一条规矩时，这条规矩在别处的说法（模板、命令、两份 SKILL.md、CLAUDE.md、README）一起改，每项登记在这里。状态填「待改 / 已改 / 已核」。

| 规矩 | 涉及的文件 | 状态 |
| --- | --- | --- |
| 来源标签只标例外（没有标签的就是作者的做法） | 四份约定各条的标签都去掉了，只留 Supplement 和 Decide on the spot；overview 14（原 13）的说明改了；两份模板、两份 SKILL.md、四个命令里没有提到标签的地方（grep 核对：插件里「Author's practice」只剩四份约定开头对「没有标签」的说明） | 已改 |
| 阶段之间由 PO 决定（overview 新增一条，短名 Product Owner decides between stages） | overview.md（新条，现 11）、sprint-log.md（图、24、各阶段指向）、design-log.md（图、3、21、26）、两份日志模板（各章注释末写明 PO 的决定）；commands/developer.md「Report to the Scrum Master」一行：原「ask the Product Owner, or the reviewer the Product Owner named, to look at the result」改成「ask the Product Owner, or the Scrum Master when the Product Owner has handed it over, to settle the result and decide whether to move on」，并指向该短名；其余三个命令没有阶段结束的说法 | 已改 |
| 两个入口，同一份产品日志（对照表只写在 product-log 2） | product-log.md（2）、overview.md（图加「白纸」入口、2）、scrum-kernel/SKILL.md（分工一段）、design-log.md（1、19 指向 product-log 2） | 已改 |
| Review 和 Retro 是收官动作、不设章；冲刺日志改成五章 | sprint-log.md（图、4–19、24）、冲刺日志模板（五章）、design-log.md 与设计日志模板（五章不变，收官是压缩日志）、scrum-kernel/SKILL.md（约定表一行）、overview.md（图、15、16）；四个命令和 README 里没有章号或 Review 章的说法（grep 核对），不用改；CLAUDE.md「冲刺收官与归档」里「补上 Review 章」与此冲突：本冲刺自己的日志仍按旧做法收官（约定从下一个冲刺起生效），CLAUDE.md 怎么改，由 Master 和 PO 在收官时定 | 插件已改；CLAUDE.md 待收官时定 |
| 约定统一改号（第 7 项） | 四份约定按文件里的顺序重排，对照表见本文件末；131 处「convention N」引用逐处对到短名，0 错；指向约定号的地方（四份约定、两份模板、两份 SKILL.md）一并更新；commands/stakeholder.md 指向 product-log 6，product-log 没改号，不用改。仓库外和 CLAUDE.md 里的引用：全局记忆 plan-view-review、compact-instead-of-handoff 里的「sprint-log 约定 13」「sprint-log 约定 14」现在应为 12 和 22；CLAUDE.md「Sprint 节律」里「插件 sprint-log 约定 16」现在应为 14（「原插件总览约定 14」是历史说法，不动） | 插件已改；仓库外与 CLAUDE.md 的引用待收官时由 Master 处理 |
| 「PO 决定什么」只留一份清单（design-log 5，现 21） | design-kernel/SKILL.md 的 Use Protocol 第 6 步和 design-log 2（现 3）已改成指向 design-log 5（现 21）；scrum 这边 overview 7 的 PO 行是角色表，不是第二份清单，不动 | 已改 |
| 「整个 scrum/ 过一遍」只写在 sprint-log 的 Review（Sprint 11 定） | sprint-log 17 写全；product-log 17 指向它；overview 5 只留 documents/ 一句。起草时 product-log 17 误改成指向 overview 5，核对时改回 | 已改 |
| 一条规矩只写一处（结构建议 2）：跨文件重复的 | 已合并：七步（product-log 15 → sprint-log 6）、「Departs」句（各条 → overview 第 3 节）、PO 决定什么（design-log 一份）、「目标固定、计划可变」（overview 17 为正文，三份各留本日志做法）、sprint-log 特殊情况表（删去重复的五行）。仍有重叠，待 Master 或 PO 定：overview 1 与 product-log 1；sprint-log 小 Sprint 里「PO 仍拍板」是照 design-log 27 类推的 | 部分已改；余下见 3.2 |

## 改号对照（旧→现）

旧号即「条」栏的号。没写的不变。

| 文件 | 对照 |
| --- | --- |
| overview.md | 11→12，12→13，13→14，14→15，15→16，16→17；新增「Product Owner decides between stages」为 11 |
| product-log.md | 不变（1–18） |
| sprint-log.md | 3→20，4→3，5→4（Why）和 5（What — select the items，从原 5 拆出），11→21，12→11，13→12，14→22，15→13，16→14，17→15，18→17，19→18，20→19，21→23；新增「Stage 5: Test」为 16、「The Product Owner decides at the end of each stage」为 24；1、2、6–10 不变 |
| design-log.md | 22→1，1→2，2→3，3→5，23→6，9→7，10→8，7→9，11→10，24→11，25→18，18→19，19→20，5→21，6→22，8→23，20→24，21→25；4、12–17、26、27 不变 |

## 核对（第 7 项之后，停点 2）

- **改号**：四份约定的条号连续；每处引用改号前后指向同一条（按短名）；把引用换成短名、去掉条号后，改号前后的文字逐行相同。131 处，0 错。
- **结构**：图的节点范围与小标题下的条逐项对上（product-log、sprint-log、design-log）；图下一行的「贯穿全程」各条就是 Throughout 一组；图的节点加 Throughout 恰好盖住全部条、各一次；约定里没有隐藏注释分隔符。
- **内容**：scrum 三份约定对照 5.1.2 的版本，未改的条逐字相同，改了的条都列在上面（改号前跑过，全过）。
- **引用的意思**：每一处「convention N」引用都列出所指条的短名，逐处读过，意思对得上；发现并改了一处（product-log 17）。
- **残留**：插件里「Author's practice」只剩四份约定开头的说明；「Departs」整句只剩指向；旧的冲刺日志节号（3.1、3.2、第 4 章 Review）没有残留。
- **敏感信息**：扫描全过（两处命中是文件名 ask-the-experts 里的 sk-the-experts，误报）。
