# Sprint 10 结构稿（给 PO 看，点头后再写全文）

> 中间文件，Review 时删除。英文是将来插件里的标题和短名，后面是中文说明。每条约定写成：短名（来源标签）：写什么（出处）。出处里的编号指产品日志的小节；「CLAUDE.md」「GlobalMemory」指作者那边现有的规矩，这次转成约定。
> 来源标签沿用 design-log.md 的三种：Author's practice、Supplement、Decide on the spot。下面没写标签的，都是 Author's practice。
> **第二版（2026-11-08）改了什么**：带进 PO 新定的三条——① How 是方案、不是步骤（冲刺日志约定第 7 条、冲刺日志模板 3.1、总览汇总表）；② 目标不变、其余可调（总览第 16 条、冲刺日志约定第 3 条、产品日志约定第 18 条、design-log.md 第 22 条）；③ 约定里不写 Claude Code 的具体机制（plan 模式、fork、权限模式），这些做法容易变：删掉总览原第 13 条「A fork follows its parent」，原第 14～17 条前移为 13～16；冲刺日志约定第 13 条只留原则；第 16 条改成工具中性的说法；subagent 照旧用。另照 Master 的补充：冲刺日志约定开头加一张流程图；总览第 13 条（Working conventions）补三处分工、短名；冲刺日志约定第 20 条补「tag 写成果」。
> **第三版（2026-11-08）改了什么**：PO 定不要修订记录，历史交给 git——产品日志模板去掉 Revision record 一节，产品日志约定第 17、18 条和冲刺日志约定第 18 条清掉修订记录的说法；PO 把结构和全文的审阅交给 Master，冲刺日志约定第 12 条写明 PO 可以这样交。

## 文件

放在 `plugins/ideo-scrum/skills/scrum-kernel/conventions/`，命名照 design-kernel：约定叫 `xxx-log.md`，模板叫 `xxx-backlog-template.md`。

| 文件 | 是什么 | PBI |
| --- | --- | --- |
| `overview.md` | 总览：三层结构、文件、文档文件夹、角色、会话分工、约定本身、与官方故意不同之处 | 39 |
| `product-log.md` | 产品日志约定 | 31 |
| `product-backlog-template.md` | 产品日志模板，用它建出来的文件叫 `ProductBacklog.md` | 31 |
| `sprint-log.md` | 冲刺日志约定 | 23 |
| `sprint-backlog-template.md` | 冲刺日志模板，用它建出来的文件叫 `SprintBacklog.md` | 23 |

另外还改三处，不新建文件：design-kernel 的约定和模板（37）；四个命令（32）；scrum-kernel 的 SKILL.md 加一张短表，描述不动。具体见文末附录。

## 1. `overview.md` — How the Pieces Fit (v1)

文件头：身份声明；三个来源标签；本文件夹的文件一览。

**The map**（总图）：Mermaid flowchart TD，由产品日志 2.2.1 的 Map 改写。

**Where things live**（东西放在哪）

1. **One product log**：新项目、老项目都从一份产品日志开始（2.2.2）。
2. **Sprints and designs side by side**：产品日志之下，冲刺和设计平级。故意和 Scrum Guide 不同，引原句并写理由（2.2.2、2.2.8）。
3. **Three layers**：一张表，列出层、文件、承诺、负责、主持（2.2.2）。
4. **Folders**：`scrum/` 只放现状，即产品日志、`sprint-NN-<后缀>/`、`design-<后缀>/`；附一张目录树（2.2.2）。
5. **The document folder**：日志写不下的东西，放进项目的文档文件夹，日志里引用；根目录有 `docs/` 就用它，没有就建一个，比如 `scrum/docs/`（PO 2026-11-08）。
6. **File names**：用模板建出来的文件，叫 `ProductBacklog.md`、`SprintBacklog.md`、`DesignBacklog.md`（2.2.7）。

**Who does what**（谁做什么）

7. **Roles**：角色表，列出主场、负责什么、加载哪些内核；简单项目没有 Developer 时，Master 和 PO 直接走完（2.2.3）。
8. **Only the PO must be human**：故意和 SGEP 不同，写理由（2.2.8）。
9. **Ask the PO**：拿不准就问 PO，除非 PO 说过某类事改问别人（2.2.3）。
10. **PO as Developer**：PO 动手施工时，以 Developer 身份参与，引 Scrum Guide 原句；这时 How 要和 PO 商量（2.2.3）。

**Sessions**（会话分工，来自 GlobalMemory 两条）

11. **One Master per project**：每个项目一个 Master 会话，带本项目的 Developer、Designer、Stakeholder；同时做几个项目时，另有一个总的会话来汇总（GlobalMemory：会话角色分层）。
12. **Who gets which work**：一张表，列出审阅、长期维护、小改、施工各交给谁，以及为什么；施工那一行写成工具中性的说法：一段话交代得清的交给新的 Developer，要用大量讨论内容的交给和 Master 共享上下文的 Developer，后者不能审自己的活（GlobalMemory：派活分工）。

**About these conventions**（关于约定本身）

13. **Working conventions**：身份声明的意思，即参考用、可以越过、越过时写明为什么；三个来源标签；三处分工：模板为主，参考为辅，命令里只放一句指路；每条约定起一个短名，方便口头引用（2.2.7）。约定里不写 plan 模式、fork、权限模式这类具体工具的机制，这些做法容易变；subagent 照旧用（PO 2026-11-08）。
14. **Revise them weekly**：用着不顺先记下，大约每周集中改一次，下个冲刺照新的用，冲刺进行中不改（2.2.7）。
15. **Templates record outputs**：章按流程分，节只放产出，做法写在约定里（2.2.7、Sprint 09）。

**What stays fixed**（什么不变）

16. **Goal fixed, plan flexible**：三份日志各有一个不变的承诺，分别是 Product Goal、Sprint Goal、设计目标；DoD 也不降低。承诺下面的东西，包括 PBI、精化点、验收标准、How 方案、设计方案，都可以随着了解调整，改了什么、为什么都记下来。承诺本身只有 PO 能改；Sprint Goal 保不住时，由 PO 取消冲刺。引原句：SGEP 用 scrum-kernel SKILL.md 里那段（Product Goal is fixed… / DoD is not weakened… / So what could be changed instead?）；Scrum Guide 用「No changes are made that would endanger the Sprint Goal」「Scope may be clarified and renegotiated with the Product Owner as more is learned」（PO 2026-11-08）。

**Where we depart from the official guides**（与官方故意不同之处汇总表）：列出不同之处、官方怎么说、理由、见哪条约定；How 那一行写「How 是方案，不是步骤」（2.2.8，PO 2026-11-08 改）。

## 2. `product-backlog-template.md`

```
# Product Backlog — <product>
> Product Owner | Started | Documents: <文档文件夹在哪>
## 1. Product
### 1.1 Product            （是什么、边界）
### 1.2 Product Goal       （远景一句、当前目标、之后的方向）
### 1.3 Definition of Done （Outcome Done、Output Done 两张表）
## 2. Architecture
### 2.1 Stakeholders       （小表：谁、要什么、何时召唤）
### 2.2 Map                （先一张 Map；要细说的步骤再开小节）
## 3. Product Backlog Items
### 3.1 Current items      （七列表）
### 3.2 Done and closed    （一行一条，附出处）
```

不设修订记录，历史交给 git（PO 2026-11-08）。

## 3. `product-log.md` — Product Log Conventions (v1)

**Starting**（起步）

1. **One product log**：新项目、老项目都先照模板写一份（2.2.4）。
2. **Blank page**：第一章不清楚时，用 IDEO 的方法弄清（ideo-kernel）（2.2.4）。
3. **Facts first, then questions**（Supplement）：事实由 Master 自己查；要 PO 定的事，在一条消息里编号问完，每条附上推荐（2.2.4）。

**Each part**（各部分怎么写）

4. **Product and Product Goal**：远景一句、当前目标、之后的方向；引 SGEP 原句：没有反证时，Product Goal 保持不变（2.2.4）。
5. **Two kinds of Done**：Outcome Done 与 Output Done，用 SGEP 的说法；冲刺从中挑相关的条目，整份 DoD 照样适用（2.2.4、2.2.5）。
6. **Stakeholders in a short table**：用一张小表列出利益相关者，不写长卡；派子代理时拿表里的一行当身份，细节由 AI 当场写；表里没人时，先问 PO（PO 2026-11-08）。
7. **Architecture as a map**：照 Make a Map 画：上面是人（AI 角色也算），下面是结局，中间 5～15 步，用 Mermaid 的 flowchart TD；要细说的步骤再开小节（2.2.4）。
8. **No TBD**：不明白的地方登记成 PBI，交给冲刺或设计去研究（2.2.4）。
9. **Technical design stays out**：模块、接口这类技术架构归 Developer，写在增量里（2.2.4）。

**Items**（PBI）

10. **Seven columns**：七列各写什么；用户故事的句式；规模分 S、M、L（2.2.4）。
11. **Numbers, not ranks**：编号只是枚举的顺序，不设排序列，需要时再排。故意和「Product Backlog 是有序的」不同，写理由（2.2.4）。
12. **PBIs with the Master**：PBI 由 PO 和 Master 一起定，Master 是 PO 的秘书。故意和官方不同，写理由（2.2.8）。
13. **Status lives here**：PBI 的状态只写在产品日志里，冲刺日志只引用编号（CLAUDE.md）。

**Refinement**（精化）

14. **Refine any time, finish in the Sprint**：引 Scrum Guide 原句「This is an ongoing activity」；在产品日志里只是先放细，最终在冲刺日志的 2.2 里做（2.2.4）。
15. **Seven steps**：精化七步。冲刺日志约定的 Planning 阶段 2 指到这里（2.2.5）。
16. **Where refined content goes**：切出的小条成为新的一行；长的设计内容进架构；短的写进备注；大材料放进文档文件夹，在备注里引用（2.2.4）。

**Keeping it fresh**（保鲜）

17. **Fresh at every Review**：做完的 PBI 移入 3.2，只留一行加出处；删掉过时的架构文字和已解决的开放点；没做完的回 3.1；不设修订记录，历史交给 git（2.2.5 单元 9，PO 2026-11-08 改）。

**What stays fixed**（什么不变）

18. **Goal fixed, plan flexible**：PBI 和验收标准随时可以精化；Product Goal 没有相反的证据就不改，要改只有 PO 能改；改了什么、为什么写在提交说明里，历史交给 git。指向总览第 16 条（PO 2026-11-08）。

## 4. `sprint-backlog-template.md`

```
# Sprint Backlog — Sprint <NN> (<name>)
> Started <date> | Closes when the Sprint Goal is met or the PO stops it | Branch | Product Owner | Scrum Master | Developer
## 1. Why
### 1.1 Sprint Goal
### 1.2 Definition of Done
## 2. What
### 2.1 Product Backlog Items
### 2.2 Refinement          （定下的各点和谁定的；验收标准；测试的方法与判定标准）
## 3. How
### 3.1 How                 （方案，不是步骤：工作项按顺序排，每项一个会话以内，写明产出和怎么算做完；关键选择和理由；已知风险和拿不准的地方；最后一行写放行）
### 3.2 Notes               （只往后加：日期、做了什么、决定与理由、证据、下一步）
## 4. Review                （收官时写：增量、DoD 与验收标准的结果、审阅、外部视角、产品日志的调整）
```

## 5. `sprint-log.md` — Sprint Log Conventions (v1)

**The flow**（流程图）：放在开头，Mermaid flowchart TD，由产品日志 2.2.5 那张改写：Planning 三个阶段 → 放行 → 施工与检查点 → 审阅 → 验收 → Review → Retro → 收官；精化碰到难点时开成设计。

**Opening**（开冲刺）

1. **One branch, one folder**：一个冲刺一个分支，worktree 可开可不开；文件夹叫 `scrum/sprint-NN-<后缀>/`，里面一定有 `SprintBacklog.md`（2.2.5）。
2. **No end date**：收官点是 Sprint Goal 达成，或 PO 叫停。故意和定长冲刺不同，写理由和代价（2.2.5、2.2.8）。
3. **Goal fixed, plan flexible**（原名 The log is not final）：Sprint Goal 和 DoD 守住，引 Scrum Guide「No changes are made that would endanger the Sprint Goal」和 SGEP 原句；How 方案随时可改；精化点、验收标准可以和 PO 重新商量（Scrum Guide「Scope may be clarified and renegotiated with the Product Owner as more is learned」）；一到三章随时可以改，改了什么、为什么记进 3.2；3.2 只往后加；Sprint Goal 保不住时，由 PO 取消冲刺。指向总览第 16 条（2.2.5，PO 2026-11-08）。
4. **Small work, small Sprint**：半小时到一个会话就能做完的活，也开冲刺，每一步缩到一两行；放行、审阅、收官照做（Sprint 09）。

**Planning**（三个阶段）

5. **Stage 1: Why and what**：PO 主导，和 Master 一起定 Sprint Goal、PBI 和 DoD；Sprint Goal 照 PO 以前写过的风格起草；选不出时用 IDEO 的方法；定完给 Developer 看（2.2.5 单元 1）。
6. **Stage 2: Refinement**：Master 主导，用精化七步（指向 product-log 第 15 条）；碰到难点开成设计；最后由 Developer 确认没有不明白的点（2.2.5 单元 2）。
7. **How is a plan, not steps**（原名 Stage 3: How gives direction only）：Developer 主导。How 写三样：① 工作项清单，按顺序排，每项一个会话以内做得完，写明产出和怎么算做完；② 关键选择和理由；③ 已知风险和拿不准的地方。不写每份文件里具体写什么，不写操作步骤，也不打磨计划本身。依据：Scrum Guide「decomposing Product Backlog items into smaller work items of one day or less」「enough detail that they can inspect their progress in the Daily Scrum」，SGEP「do enough planning to get started with the work」；这里把「一天」换成「一个会话」，把站会换成检查点（第 10 条）。Master 和 PO 看方案对不对。Master 和 PO 要看过、放行才施工，这一点故意和官方不同，写理由（2.2.5 单元 3、2.2.8，PO 2026-11-08 改）。
8. **Go-ahead**：How 定了、PO 放行了才施工；放行写成一行，写明授权到哪一步；PO 可以把审 How 交给 Master（2.2.5 单元 4、Sprint 10）。

**Building**（施工）

9. **Notes as you go**：3.2 是全程记录，每行写日期、做了什么、决定与理由、证据、下一步；接手的会话以笔记为准（2.2.5 单元 5）。
10. **Checkpoints, not stand-ups**：不定时，AI 停下来问 PO，或者 PO 来问进度。故意和每日站会不同，写理由（2.2.5 单元 6、2.2.8）。
11. **New work gets registered**：冲刺中冒出来的新活，先登记成 PBI，再由 PO 定进不进当前冲刺；Sprint Goal 不变（CLAUDE.md）。
12. **Structure before full text**：新模板、新结构，先把章节清单单独给 PO 看，PO 点头再写全文；PO 可以把结构和全文的审阅交给 Master，Master 认可就继续（Sprint 09 Retro；Sprint 10，PO 2026-11-08）。
13. **Full text for review**：新的长期文档，先把全文放到 PO 能逐段批注的地方，批准后才改源文件；盘上的版本优先（GlobalMemory：plan 视图审阅；只留原则，不写具体工具，PO 2026-11-08）。
14. **Hand off by compacting**：不写交接文档；压缩前先把该写的写进文件、提交，停在一个完整的点上；压缩时写明要保留什么（GlobalMemory：压缩代替交接）。
15. **Tests: criteria first**：判定标准先写、单独提交，再跑；出了结果不改标准；判错的逐条人工看，写明理由（CLAUDE.md）。

**Review and acceptance**（审阅与验收）

16. **A reviewer is required**：默认由 Master 审；PO 可以指定 Stakeholder 或全新子代理；Master 兼 Developer，或 Developer shares the Master's context（和 Master 共享上下文）时，交给全新子代理，只核对做得对不对；派审阅子代理时，写全任务、项目规矩和已经发出的决定。故意和官方不同，写理由（2.2.5 单元 7、CLAUDE.md、GlobalMemory：派活分工）。
17. **PO acceptance when written**：DoD 或验收标准里写了才做，有时 PO 看一眼就过（2.2.5 单元 8）。

**Closing**（收官）

18. **Review**：依次是备料、删掉中间文件、压缩冲刺日志并补上第四章、改名移进文档文件夹、照 product-log 第 17 条给产品日志保鲜（不写修订记录）；召唤产品日志表里的利益相关者看增量（2.2.5 单元 9、GlobalMemory：Sprint 收尾做法）。
19. **Retro**：不设 Retro 章；教训写进项目的记忆或说明文件，写成原则：坏了什么、为什么、得出什么规则；特别好的改进经 PO 同意写进 DoD；问一句 PO 在哪里卡住了 AI（2.2.5 单元 10）。
20. **One closing commit**：Review 和 Retro 只出一个提交；tag 与冲刺文件夹同名，同名分支随即删除；tag 的说明写这次做成了什么；改名、移动后全仓查旧路径；推送这类对外动作要经 PO 同意（2.2.5 单元 11、GlobalMemory：Sprint 收尾做法）。

**When things change**（特殊情况）

21. **Special cases**：一张表，覆盖审阅或验收不过、外部阻碍、精化碰到难点、中途发版、收官时没做完、Sprint Goal 作废（2.2.5）。

## 附录：另外三处改动（不新建文件）

- **37，design-kernel**。约定条号 1～20 不变，免得 SKILL.md 和模板里的引用跟着改：
  - design-log.md 第 4 条 **Where** 改成 **Open a design**：起后缀、建文件夹、照模板建出 `DesignBacklog.md`、填好文件头（分支见第 5 条）。
  - 第 3 条 **Who** 加上只有一个会话时的署名写法。
  - 开头的两个术语：**Role card** 改成「产品日志利益相关者表里的一行」，表里没人时先问 PO；**Folders** 改成指向总览里的文档文件夹。
  - 末尾新加第 21 条 **Resume from the header**：文件头的 Now 一行随时更新，接手的会话先读它。
  - 末尾再加第 22 条 **Goal fixed, plan flexible**：设计目标在共情阶段边学边改，定下以后只有 PO 能改；方案可以照测试结果改；改了什么、为什么写进日志。指向总览第 16 条（PO 2026-11-08）。
  - 第 13、17 条各加一句：子代理开几个、用什么模型、原型做到多真，都当场定（Decide on the spot）。
  - 模板的文件头加上 Now 一行。
- **32，四个命令**：照精化表改；每个命令加一句指路，指向 `conventions/overview.md`。
- **scrum-kernel 的 SKILL.md**：加一节 Conventions，用一张短表列出五份文件和各自什么时候读；描述不动。
