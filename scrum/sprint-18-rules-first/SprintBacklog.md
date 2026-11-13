# Sprint Backlog — Sprint 18 (rules-first)

> Started: 2026-11-13 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: claude/youthful-payne-b1e139 | Product Owner: SeaPawn | Scrum Master: 会话 IDEO # [master]-[main]-[support sprint] | Developer: Claude Code（会话 IDEO # [developer]-[sprint-18]-[do sprint 18]，youthful-payne-b1e139）
> Now: How：Developer 起草施工方案 · Master 2026-11-13 定精化结束（PO 授权，见第 4 章）
> Waiting for PO: None
> How to write this log: `sprint-log.md` in the sprint-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled later; add none — remarks go in chapter 4, Increment notes (`overview.md` in the scrum-kernel skill folder, convention 16).

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 规矩先顺：日志头部统一，scrum、sprint、design 召唤才来，角色说明写清；看板和 hook 照着就能读，文档照着就能写。（PO 2026-11-13 定） |
| --- | --- |

### 1.2 Definition of Done

| 维度 | 标准 |
| --- | --- |
| 内容忠实 | 忠于源材料（SGEP / d.school / Sprint）；方法论设计部分（融合、solo+AI）标注来源与依据 |
| 可导航 | 从 SKILL.md 入口 ≤2 跳到达任意 reference |
| 无死链 | 所有 markdown 内部链接可解析，无 404 |
| 插件校验 | `claude plugin validate --strict plugins/ideo-scrum` 通过 |
| 描述长度 | 每个技能的 description 不超过 1024 字符 |
| Codex 包 | 改了插件就跑 `scripts/sync_codex.py`，`scripts/check_codex.py` 通过 |

PO 2026-11-13 定 Sprint Goal

## 2. What

### 2.1 Product Backlog Items

| 编号 | 标题 | 用户故事 | 架构定位 | 规模 |
| --- | --- | --- | --- | --- |
| PBI-66 | 日志头部——承诺、Now、等 PO 的事，决定前引用目标 | 作为熟手（也是 PO），我想要每份日志的头部有固定的一块——承诺一行小表、Now 行、等 PO 的事——阶段决定前先引用目标原文，以便 hook 和看板读得到，AI 做决定时不丢目标 | Map ④ | M |
| PBI-65 | 加载边界——ideo 放开，其余召唤才来 | 作为熟手（也是 PO），我想要 ideo-kernel 在发散、定义问题、做原型、做测试这类请求时就加载，scrum、sprint、design 三个内核只在召唤时加载（用了角色命令，或明说要用），以便平时不被打扰、要用时可控 | Map ② | M |
| PBI-60 | 角色说明——PO 助手是谁，Master 能替你做到哪 | 作为熟手（也是 PO），我想要 stakeholder 命令写明它可以当我的助手——整理产品日志、汇总进度、照我的话派活、维护看板——Master 写明「服务 PO；经书面授权在范围内代行，问责仍在 PO」，以便我一眼找到对的角色，也不让 AI 自己拍板 | Map ② | S |

### 2.2 Refinement

> 精化由 Master 主持并定案（PO 2026-11-13 授权，原话见第 4 章）。Developer 先写的 66 头部提案见提交 `2561224`；下面的定案在它的基础上改了一处：承诺不挪到文件头。

**PBI-66 日志头部**——观点：照抄 2.1。

| # | 点 | 定案（谁定） |
| --- | --- | --- |
| 66-1 | 承诺放哪 | 留在各自的节里，不挪到文件头：产品日志 1.1 Product、1.2 Product Goal；冲刺日志 1.1 Sprint Goal；设计日志 1.2 Design goal。每处一张一行小表，只存一份；种类由小表所在的节标题定，不加 `Product:` 一类标签。理由：这几节本来就在文件最上面；挪到头部要改四份模板的结构，原节还得变成指引，PO 不要大改内核；产品日志和 Sprint 18、19 的日志已经是这个样子，不用迁移。（Master） |
| 66-2 | 小表的键 | 模板写 `\| Commitment \| <原文> \|`，插件是英文的；中文日志写 `\| 承诺 \| <原文> \|`，两者是同一个键。右格逐字放原文，不加粗。（Master） |
| 66-3 | 头部两行 | 冲刺、设计、IDEO 三种日志的头部各有 `> Now: …` 和 `> Waiting for PO: …` 两行，后者紧跟 Now。Now 沿用各模板原来的写法；IDEO 模板把 Now 从第一行里拆出来，单独成行。产品日志不加这两行：它没有阶段，等 PO 的事由看板从各日志汇总。（Master） |
| 66-4 | IDEO 日志的承诺 | 不另设承诺，读取方沿 For 找它服务的日志（同意 Developer 的建议）。（Master） |
| 66-5 | 决定前引用 | 冲刺的阶段决定引本 Sprint Goal，设计的阶段决定引本设计目标，涉及产品方向时另引 Product Goal；IDEO 的模式之间不加关卡；引不出原文就先补读，不编造，这时的决定不算数。写进 sprint-log 第 24 条、design-log 第 26 条。（Master） |
| 66-6 | 什么时候更新 | Now、Waiting for PO 跟引起变化的那次日志提交一起更新；Waiting for PO 写编号加短句，多项用「；」隔开，没有就写 None。（Master） |
| 66-7 | 旧日志 | 已归档的日志不回改；Sprint 18、19 的日志现在就加上 Waiting for PO 一行，由 Master 在精化时加。（Master） |

**读取规则（给 Sprint 19 的看板和 hook，也是接口验收的依据）**
- 开着的日志：`scrum/sprint-*/SprintBacklog.md`、`scrum/design-*/DesignBacklog.md`、`scrum/ideo-*/IdeoBacklog.md`，不含 `scrum/documents/`；产品日志是 `scrum/ProductBacklog.md`。
- 承诺：表头行的首格是 `Commitment` 或 `承诺`，第二格就是原文；它是哪种承诺，看上方最近的节标题。
- 现状：以 `> Now:` 开头的行。等 PO 的事：以 `> Waiting for PO:` 开头的行，`None` 表示没有。

**验收标准（66）**
1. 四份模板照 66-1～66-3 改好：产品日志的 1.1、1.2，冲刺日志的 1.1，设计日志的 1.2 各留一个承诺小表的占位；冲刺、设计、IDEO 三份模板的头部各有 Now 与 Waiting for PO 两行；产品日志模板不加这两行。
2. 约定里讲到头部、Now 行、目标所在节的地方都跟着改，例如 sprint-log 第 22 条、design-log 的 Now 一条、ideo-log、product-log 第 4 条、overview 第 17 条。全仓 grep「Now」「Commitment」「goal」，凡是说法冲突的都改掉（CLAUDE.md：改规矩先找它的其他说法）。
3. 66-5 写进 sprint-log 第 24 条和 design-log 第 26 条；IDEO 不加关卡。
4. 静态核对：用四份模板各填一份样本日志，照上面的读取规则用脚本读，每个承诺、Now、Waiting for PO 都读得到，读出的原文与填入的一致（4/4）。脚本只用来核对，不进插件。
5. 已归档的日志一行没动（git diff `scrum/documents/` 为空）。

**PBI-65 加载边界**——观点：照抄 2.1。

| # | 点 | 定案（谁定） |
| --- | --- | --- |
| 65-1 | 用什么办法 | 只改描述。`disable-model-invocation: true` 会把技能从模型的上下文里整个拿掉，角色命令和子代理就没法用 Skill 工具加载内核（claude-code-docs：skills#restrict-claudes-skill-access）；`user-invocable: false` 挡的是用户，挡不住模型，与本条无关。（Master 查文档定，2026-11-13） |
| 65-2 | 什么算召唤 | 三种：① 用了 ideo-scrum 的角色命令，命令里叫它加载；② 用户点名本插件或某个内核；③ 用户要建、改本插件的日志——ProductBacklog.md、SprintBacklog.md、DesignBacklog.md，或说「产品日志、冲刺日志、设计日志」。除此以外，泛问 Scrum、Sprint、设计冲刺都不加载，照常回答。（Master） |
| 65-3 | ideo 放开到哪 | 发散、定义问题、做原型、做测试、用户研究这类请求，没说 IDEO 或设计思维这些词也加载；现有的触发保留：五模式、方法名、没有现成答案的问题。（Master，照 PO 2026-11-13） |
| 65-4 | 描述怎么写 | 描述仍是触发条件（CLAUDE.md 描述规约）。三个内核写成「只在召唤时加载」，并列出 65-2 的三种召唤；删掉「Load it before answering, even for a quick outline」这类强触发句；四个内核之间保持区分度；每条不超过 1024 字符。（Master） |
| 65-5 | 连带改动 | CLAUDE.md「组件描述规约」里与新方向相反的两句要改：「模型自以为懂的通用词……写明要照技能答」「Scrum 的通用词也要写进描述，并写明什么时候先加载」。改成新方向，注明「PO 2026-11-13 改方向」，和描述放在同一个提交。SKILL.md 正文只有加载以后才读得到，不影响触发，不改。（Master） |
| 65-6 | Codex | 描述由脚本同步进 Codex 包；不在 Codex 里测，Codex 不是核心。（Master，照 PO 2026-11-13） |

**PBI-60 角色说明**——观点：照抄 2.1。

| # | 点 | 定案（谁定） |
| --- | --- | --- |
| 60-1 | PO 助手 | stakeholder 命令的描述已经写了「常驻会话……例如维护看板」；描述和正文再补上「PO 助手」这个身份，写明负责：整理产品日志、汇总进度、照 PO 或 Master 已定的事派活、维护看板；不负责：排序、拍板、审阅、改插件文件。描述仍以触发句开头。（Master） |
| 60-2 | 派活边界 | PO 助手只转达 PO 或 Master 已经定下的事；凡是改范围、改条目、要放行的，都经 Master。派给哪个会话，由 Master 定。（Master，按产品日志 PBI-60 备注由 Master 定） |
| 60-3 | Master 的说法 | 插件里所有「secretary」都换掉，共 5 处：scrum-master 命令的描述和正文、overview 第 8 条的表、product-log 第 12 条、sprint-log 第 20 条。改成「serves the Product Owner; acts for them within a written handover, and the accountability stays with the Product Owner; decisions made under it are recorded」，不写「替身」。overview 第 12 条已有「unless the Product Owner has handed this to the Scrum Master」，留着并与新说法对上。（Master） |
| 60-4 | 看板放哪 | 原定由 60 在 overview 第 4 条写一句看板放哪，改由 Sprint 19（PBI-35）来写：那一句由看板的定案决定；第 4 条和 60 要改的第 8、12、14 条不相邻，合并时不会冲突。（Master） |

**验收标准（65、60）**
1. 插件里 grep「secretary」为 0；scrum-master、stakeholder 两个命令的描述与正文写明 60-1～60-3。
2. 三个内核的描述写明 65-2 的三种召唤，不再有强触发句；ideo 的描述写明 65-3；每条不超过 1024 字符（DoD「描述长度」）。
3. CLAUDE.md 那两句照 65-5 改好，和描述在同一个提交。
4. 触发测试过线（见下）。
5. DoD 全部通过：插件校验、无死链、可导航、Codex 同步并核对通过。

**测试（65、60 同一轮；标准先写、单独提交，再跑；看到结果后不改）**
- 通道照 CLAUDE.md「回归测试」：Haiku，`claude -p --plugin-dir <本分支插件的 Windows 路径>`，去掉网关与宿主认证变量；工具只给 Read、Grep、Glob、Skill；每次调用用全新的空 TEMP 和空工作目录；比对技能名时去掉 `ideo-scrum:` 前缀；Windows 上连 PowerShell 一起禁；正式跑之前先冒烟一次。
- 基线：同一天、同一条通道，先用 main 上的插件跑一遍。
- 题组，每题 3 次；题目不带「按插件的约定」这类引导词：
  - **A 泛问**：3 题，例如「Product Backlog 是什么」「Sprint Review 一般怎么开」「设计冲刺一般几天」，在空目录里问。scrum、sprint、design 三个内核都不该加载。
  - **B 召唤**：3 题，三种召唤各一题——角色命令；点名「用 ideo-scrum……」；在有产品日志的样本项目里说「改一下 Product Goal」。该加载对应的内核。
  - **C ideo 放开**：3 题，发散、定义问题、做原型测反应各一题。ideo-kernel 该加载。
  - **D 角色**：2 题，「我想要一个助手帮我整理产品日志、汇总进度」应选 stakeholder；「帮我主持 Sprint Planning」应选 scrum-master。
- 过线：A 九次里三个内核加载不超过 1 次；B 对的内核不少于 8/9；C ideo 不少于 7/9，且不比基线少；D 每题不比基线少。汇总把行为（加载了哪个技能、读没读约定）和内容（答得对不对）分两栏列。

精化结束：Master 2026-11-13 定（PO 授权，见第 4 章）。Developer 起草 How 时如有不清楚的点，先问 Master；没有疑问，就在第 4 章写一行「Developer 复述无疑问」。

## 3. How

待 Developer 起草。

| # | Work item | Output | Done when |
| --- | --- | --- | --- |

**Key choices**

**Risks and open points**

Go-ahead: 尚未放行。

## 4. Increment notes

- 分支名没照约定 1，因为是原生 worktree 生成的名字；收官时 tag 用文件夹名 `sprint-18-rules-first`。
- **PO 授权（2026-11-13，原话）**：「其实精化我一般让你做的，你的上下文最多，其实你可以详细的告诉他们得，怎么写精化啥得对不对，我把整个权限全放开了，也就是告诉你，后面你的权限拉满，除非必要，我来做决定，否则你都可以直接决定」。所以本冲刺的精化定案、精化结束、How 的审阅和放行都由 Master 做（overview 第 12 条：PO 可以把阶段决定交给 Master）。下面这些仍回到 PO：改 Product Goal；推送、发布等对外动作；取消冲刺；推翻 PO 已经说过的话。
- 精化由 Master 接手：Developer 的 65、60 草稿没有写完，就停下了；66 的提案以提交 `2561224` 为准。
