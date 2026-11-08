# Sprint Backlog — Sprint 11 (conventions-review)

> Started: 2026-11-09 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `sprint-11-conventions-review` | Product Owner: SeaPawn | Scrum Master: Claude（主会话）| Developer: Claude（Master 兼任，PO 2026-11-09 定）
> How to write this log: `sprint-log.md` in the scrum-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled at close; add none — remarks go in 3.2 Notes (`overview.md`, convention 15).
> 归档：2026-11-09 开工、当天收官（小冲刺），发版 v5.1.1（未推送）。日志本来就短，没有再压缩；改动的英文全文以提交为准。

## 1. Why

### 1.1 Sprint Goal

**约定照审阅改定**：PO 审出的 19 处逐条核过，成立的改进原文，不成立的写明理由；一条规矩只写一处，英文语感不变；照着改后的约定，就能开、跑、收一个冲刺和一份设计。

### 1.2 Definition of Done

Output Done 三条：内容忠实、可导航、无死链。插件描述一个字不动，不重跑触发测试。

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-41 | 约定 v1 按 PO 审阅修订 | 作为熟手，我想要约定照 PO 逐段审出的意见改过一遍，以便读起来顺、一条规矩只写一处、不该在插件里的不在插件里 | 插件 scrum-kernel、design-kernel 的 `conventions/` | S |

### 2.2 Refinement

清单：`scrum/documents/conventions-review-log.md`（19 处）；理由见同目录四份中文译文。Master 逐条核过，PO 2026-11-09 全部同意（英文全文在放行前的对话里给 PO 看过，以提交为准）。

| 文件 | 处 | 结论 |
| --- | --- | --- |
| overview | 1 | 成立：括号里补设计两份属于 design-kernel，开设计或接手时读（「开设计时」加了 resume，与 design-kernel SKILL.md 一致） |
| overview | 2 | 前半成立，倒装改顺；后半不改：英文原文就是 item，含糊的是译文「某一项」 |
| overview | 3 | 成立：短名 Where files go |
| overview | 4 | 成立：短名 When a revision applies，删「大约每周改一次」，那半句挪进 CLAUDE.md「Sprint 节律」（是本仓库的规矩，不是一件活，不登记 PBI） |
| product-log | 1 | 成立：IDEO 方法单独弄不清，要做一次设计；设计结论回流前，产品日志写挑战、问题、provisional roadmap（不写 TBD，免得和约定 8 冲突） |
| product-log | 2 | 成立：完成定义要写准，拿不准的放验收标准 |
| product-log | 3 | 成立：编号唯一，排名是往上挪；连带删 overview 偏离表里对应的一行 |
| product-log | 4 | 成立：以 Sprint Goal 为准，缺的补，不凑数 |
| product-log | 5 | 成立，写成指路：「整个 `scrum/` 保鲜」只写在 sprint-log 18 |
| sprint-log | 1 | 成立：可与 SM 重谈，写明 SM 是 PO 的秘书（不算新偏离）；删「只增不减」 |
| sprint-log | 2 | 成立：目标定不出来时用 IDEO；「IDEO 是基础」只带一句、指向 overview 7；结果同步给 SM 和 Developer |
| sprint-log | 3 | 成立：删行格式，笔记形式不限，How 也是笔记，3.2 可细化 How |
| sprint-log | 4 | 成立：SM 自己构建 → 全新子代理审；只共享上下文 → SM 照常审；不写 fork（工具机制）；「也可委任子代理」并进原有那句 |
| sprint-log | 5 | 成立：先压缩、写第 4 章 Review、移走，再删其余工作文件；加「整个 `scrum/` 过一遍」 |
| sprint-log | 6 | 成立：看 `scrum/` 就够，指向 overview 4；不列看板（约定里还没定看板放哪，PBI-35 未做） |
| design-log | 1 | 成立：删单列的角色卡；引用放在第一次出现处（原约定 10），不放 18——Designer 只加载 ideo、design 两个内核 |
| design-log | 2 | 可行，做：原句提到 design-kernel SKILL.md 第一段，删约定 1，原 2–22 改为 1–21，引用跟着改 |
| design-log | 3 | 成立：文件夹也装工作材料（草图、收集的点子、反应网格），都不进增量 |
| design-log | 4 | 成立：问过专家或做过研究后再精化一遍、重画地图；「也可理解为精化」并进动词 refine；模板 2.1 同步 |

PO 判过不改的四条（design-log 原约定 3、17、19、11 及对应处）原样。

**清单外的连带改动**（PO 2026-11-09 同意）：overview 偏离表删一行；冲刺日志模板 3.2 删五列表格、改注释；commands 的 scrum-master、developer 两处审阅说法跟 sprint-log 16；design-kernel SKILL.md 与模板条号跟着改；CLAUDE.md 加每周节律、fork 那条的审阅说法、收官顺序与「看 `scrum/` 就够」。

**验收标准**：① 19 处都改了，不改的在审阅记录里写明理由；② 连带改动做完，全仓没有自相矛盾的说法；③ 脚本核过：每处「convention N」都指向正确的条目，路径都存在；④ 约定里没有 fork 这类工具机制；⑤ PO 判过不改的四条原样。

**测试**：不跑触发测试（描述不动）。用脚本核条号引用与路径，判定标准即验收 ③。

## 3. How

### 3.1 How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | 开冲刺 | 分支、本日志一至三章、登记 PBI-41 | 放行行在本节末尾；提交 |
| 2 | 改 scrum-kernel | overview、product-log、sprint-log、冲刺日志模板 | 与放行前给 PO 的英文一致；提交 |
| 3 | 改 design-kernel | design-log（删约定 1、改号）、模板、SKILL.md | 同上；新旧条号对照写进 3.2；提交 |
| 4 | 改命令和 CLAUDE.md | 两个命令、CLAUDE.md | 同上；提交 |
| 5 | 自查 | 脚本核条号和路径；grep 工具机制词；四条不改的原样；审阅记录逐条标 | 脚本 0 错；提交 |
| 6 | 审阅 | 全新子代理对照本节和 2.2 核 diff；plugin-validator | 必改项改完 |
| 7 | 收官 | Review 章（含 design-log 别扭处）、归档、产品日志、README、版本号、tag、合入 | git status 干净 |

**Key choices**

- PO 定：不另开 Developer，Master 兼任。Master 自己构建，审阅交全新子代理，只核做得对不对（v5.1.0 的 sprint-log 16；本冲刺的修订从 Sprint 12 起生效）。
- 一条规矩只写一处：「整个 `scrum/` 保鲜」放 sprint-log 18，product-log 17 与 sprint-log 20 指过去。
- 本冲刺的日志仍照 v5.1.0 的模板写（3.2 用表格）。

**Risks and open points**

- 改号漏改某处引用：脚本逐条核。
- 四份中文译文在英文改完后就对不上了：Review 时定留不留（Master 倾向删，git 留着；审阅记录标完后保留）。
- README 的文件地图没列五份审阅文件，收官时一并改。

Go-ahead: 2026-11-09，PO（「其他的我就都同意，现在开始干活吧」）——冲刺分支上可以提交；收官时合入 main，打 tag `v5.1.1` 与 `sprint-11-conventions-review`；不推送。

### 3.2 Notes

<!-- Whoever did the thing writes the row; append only (sprint-log.md, convention 9). A session that picks up the Sprint reads these first. -->

| Date | What was done | Decision and reason | Evidence | Next |
| --- | --- | --- | --- | --- |
| 2026-11-09 | Planning、精化、How 在对话里给 PO 看过 | PO：不开 Developer，Master 兼任；其余全部同意，放行 | 本日志 2.2、3.1 | 工作项 1 |
| 2026-11-09 | 工作项 1～4：开冲刺；scrum-kernel 四份；design-kernel 三份；两个命令与 CLAUDE.md | 照放行前的英文改；design-log 新旧条号：原 2–22 → 现 1–21（原 n 现 n−1）；CLAUDE.md 另把收官顺序与「看 `scrum/` 就够」跟上新约定 | `ce313f6`、`33db205`、`b265ca2`、`f3339fe` | 工作项 5 |
| 2026-11-09 | 工作项 5：自查；审阅记录逐条标状态 | 条号引用 64 处全部对到正确短名；路径 93 处都在；约定与 design-kernel SKILL.md 里没有 fork、plan mode、permission mode、worktree；PO 判过不改的四条（现约定 2、10、16、18）除条号外逐字未变 | 脚本 `refs.py`、`paths.py`（任务临时目录，结果以此为准） | 工作项 6：全新子代理审阅、plugin-validator |
| 2026-11-09 | 工作项 6：全新子代理（Sonnet）对照 2.2 审 diff | 19 处与连带改动全部核过，没有必改项，没有遗留矛盾。六条建议采纳两条，意思不变、只改清楚：product-log 2 改成 "which adds the design sprint, a prototype, and a test to those methods"；sprint-log 5 的 "guide the choice" 改成 "help set it"。不采纳：「by `scrum/` alone」是 PO 要的「就够」；「may send a subagent to do the review」与前句不冲突（Master 自己构建时本来就要全新子代理）；句子拆分与 CLAUDE.md 加指路不必要 | 审阅报告（对话里） | plugin-validator 结果 |
| 2026-11-09 | 工作项 6：plugin-validator | PASS。提醒两条：版本号收官时改；overview 4 说设计文件夹只装日志和原型，与 design-log 3 新加的工作材料不一致——照冲刺文件夹的说法补 "and working files"（design-log 3 的连带改动） | validator 报告（对话里） | 收官 |

## 4. Review

**增量**（PBI-41，v5.1.1）：

- scrum-kernel：overview 改 4 处，并删去偏离表「Items are numbered, not ranked」一行、约定 4 补设计文件夹的工作文件；product-log 改 5 处；sprint-log 改 6 处；冲刺日志模板 3.2 去掉五列表格与「只增不减」。
- design-kernel：「设计与冲刺并排」提到 SKILL.md 第一段；design-log 删原约定 1 与单列的角色卡，原 2–22 改号为 1–21，补文件夹的工作材料、问过专家后再精化与重画地图；模板与 SKILL.md 的条号跟着改，模板 2.1 补重画一句。
- 命令：scrum-master、developer 的审阅说法跟上 sprint-log 16。
- 本仓库：CLAUDE.md 加「约定大约每周集中改一次」（原总览约定 14 的前半句）、fork 那条的审阅说法、收官顺序；审阅记录 19 处逐条标了状态。

**DoD 与验收标准**：

| 项 | 结果 |
| --- | --- |
| 内容忠实 | 19 处照 2.2 的结论改；没有新引文 |
| 可导航 | 路径 93 处都在；design-kernel SKILL.md 一跳到 design-log |
| 无死链 | 条号引用 64 处都对到正确短名（脚本）；plugin-validator PASS |
| ① 19 处都改了，不改的写明理由 | 过：18 处改，overview 第 2 处后半不改，理由写在审阅记录 |
| ② 连带改动做完，没有自相矛盾 | 过：审阅子代理与 validator 都没找到遗留矛盾；validator 指出的 overview 4 已补 |
| ③ 脚本核条号与路径 | 过 |
| ④ 约定里没有工具机制 | 过：无 fork、plan mode、permission mode、worktree |
| ⑤ PO 判过不改的四条原样 | 过：现约定 2、10、16、18 除条号外逐字未变 |

**审阅**：Master 兼 Developer，审阅交全新子代理（Sonnet）：没有必改项，六条建议采纳两条（见 3.2）。外部视角这次没召唤 Stakeholder（PO：小冲刺，别的不需要）。

**design-log 读着别扭的地方**（PO 要求记下，不硬改）：

1. 约定 5（Ask the PO）和 8（Renamed terms）只是指路，与这次提到 SKILL.md 的原约定 1 是同一类；约定 7 前半也只是指路。下次可以照原约定 1 的办法处理。
2. 「Where a design sits」这个小标题原本贴着原约定 1；它移走后，这一节从 Hard point 开始，讲的是开设计前后的事，小标题不太对得上。
3. 约定 9（Experts when needed）现在最长：什么时候问、专家是谁、先画草图、日志记什么、问完再精化，一条装了五件事。
4. 冲刺 Review 现在要把整个 `scrum/` 过一遍，设计收官（约定 18）仍只写「刷新产品日志」，两边差得比以前大（PO 判过两边做法可以不同）。
5. 模板文件头有六行引用块，接手时要读的 Now 夹在中间。

**产品日志调整**：PBI-41 移入 3.2；1.2 路线补上 11；PBI-40（熟手的七条意见）照旧排着，标题里的「第一次」已不准确，留给下次精化。Product Goal 不动。

**scrum/ 保鲜**：四份中文译文按英文改完就对不上了（条号也变了），删掉，git 留着（`git show 6a2fd5e:scrum/documents/conventions-overview-zh.md` 等）；审阅记录标完状态后留着。

**Retro**（教训写进 CLAUDE.md）：一条规矩改了，牵出的其他说法要一起改（这次一处审阅意见牵出五组连带改动），精化时就全仓 grep；对着译文审阅的意见，先判是改原文还是只是译文的措辞。*Supplement*：PO 这次没有卡住 AI，Planning 一次放行。
