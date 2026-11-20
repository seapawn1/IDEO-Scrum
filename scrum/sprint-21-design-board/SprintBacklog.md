# Sprint Backlog — Sprint 21 (design-board)

> Started: 2026-11-19 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `claude/sprint-21-design-board-2a4e5b` | Product Owner: SeaPawn | Scrum Master: IDEO # [master]-[main]-[manage sprint] | Developer: Sprint 21 Developer
> Now: Test · 2026-11-20，Master 依 PO 的书面委托放行 H6，并复核两条 PBI 过线。五模式底本已追到官方存档维基页与空间级 CC BY-NC-SA 3.0 声明，尚待 Master／PO 裁定能否闭环及与现注 4.0 之落差；整体 Test 未判通过，不进 Review。
> Waiting for PO: None
> 日志约定：[sprint-log.md](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md)。

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 设计方案看得懂：打开设计冲刺卡，一眼看清这次设计的目标、路线和选定的方案；即使没画故事板，也能知道选了什么、方案怎么用。 |
| --- | --- |

**依据：** 承接 [Product Goal](../ProductBacklog.md#12-product-goal) 的「看板一眼看清进度」。按[六期总表](../documents/sprint-roadmap.md)，PBI-74 聚焦设计卡，产品卡和普通 Sprint 卡不变；PBI-71 独立核验 IDEO 日志归属，让看板约定和检查说同一件事。

### 1.2 Definition of Done

[产品日志 §1.3 的完整 DoD](../ProductBacklog.md#13-definition-of-done) 仍生效，本期重点核验以下三组。它们是要达到的标准，尚未验证。

| 维度 | 本期核验重点 |
| --- | --- |
| 内容忠实 | 看板约定保留“方案”和“故事板”的区别：方案一旦选定就能展示，故事板是可选的；尚未选定时，不编造方案。 |
| 可导航、无死链 | 从技能入口到参考材料仍不超过两跳；看板到设计日志的链接、改动涉及的文档链接都能打开。 |
| 插件与分发校验 | Claude 插件严格校验、DSH 自动检查均通过。若没有改分发方式，不把重新安装列为本期专项。 |

署名、技能描述长度等未列为重点的标准不豁免。

PO 2026-11-19（Master 转达）：「目标和 DoD 就这么定，让 Developer 写进日志，进入 What。」目标原文：「设计方案看得懂：打开设计冲刺卡，一眼看清这次设计的目标、路线和选定的方案；即使没画故事板，也能知道选了什么、方案怎么用。」

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-74 | 看板：重做设计冲刺卡 | 作为熟手，我想一眼看见设计目标、地图主线和选定方案，以便不用翻完整日志就能理解这次设计 | Map「设计冲刺」、看板 | 待估 |
| PBI-71 | 看板：服务产品日志的 IDEO 日志怎么处理 | 作为用插件做设计的人，我想要看板约定写清「服务产品日志、或已经收尾的 IDEO 日志页面怎么处理」，以便模型和检查脚本对同一件事有同一个答案 | Map「设计冲刺」 | S |

### 2.2 Refinement

PO 指定 Master 主导精化，Developer 复述、估量和落盘。下列行为由 Master 提出，PO 认可的范围见章末。核验方法与 Developer 估量是工作口径，不记作 PO 对做法的决定；此处记录的是待执行的口径。

**PBI-74 · 先精化设计卡**

**视角（产品日志原文）：** 作为熟手，我想一眼看见设计目标、地图主线和选定方案，以便不用翻完整日志就能理解这次设计

**精化问题：** 没有故事板，读者怎样仍能看懂选了什么、怎么用？以设计日志为准，不凭字段非空判断是否已选定。

**PO 已定范围：** 只重做设计卡。第一块只展示本设计 §1.2 的设计目标原文，不堆 PBI 或其他承诺；第二块取本设计 §2.1 的地图主线，借用产品卡的简略路线表达，不复制产品路径、不改顺序或发明节点；第三块是独立、始终在场的方案区。产品卡与普通 Sprint 卡不改版。

| 场景 | Master 提议的预期 |
| --- | --- |
| A · 已选定，有故事板 | 展示 §3.1 的选定方案，与可选的 §3.2 互相核对；故事板可辅助理解，不替代方案。 |
| B · 已选定，无单独故事板 | 方案区仍可见。评阅者只看卡、不听讲解，能说出选了什么、怎样使用，再与 §3.1 原文核对。以[反馈闭环设计 §3.1](../documents/design/design-feedback-loop.md#31-方案)为只读内容样本，不补故事板、不改归档，不把此设计列为在办。 |
| C · 尚未选定 | 方案区仍在，并让读者看得出尚未选定。候选草图和推测都不能当成定案。 |

**测试与通过线草案：** 分别验 A、B、C；逐字比目标，沿源图核主线，用日志明示内容核方案，不捏造、不串源。改前后用同一份数据对照产品卡和普通 Sprint 卡，既有外观、内容与交互无回归，保留原有离线、宽中窄、深浅色约束。选定理由不必填，具体布局、帧数和空态措辞不是通过线。

**Developer 初估：M（3–5 个会话）。** 技术上可做，不只改样式：当前页面以 `story` 是否非空决定方案区显隐，后续需让取材约定、卡片和验收一致。源文只写了选定事实时，不视作未选定，也不补造用法；读者是否真能读懂仍要看卡核对，不能只靠结构检查。具体做法留待 How。

**PBI-71 · 独立精化 IDEO 日志归属**

**视角（产品日志原文）：** 作为用插件做设计的人，我想要看板约定写清「服务产品日志、或已经收尾的 IDEO 日志页面怎么处理」，以便模型和检查脚本对同一件事有同一个答案

**精化问题：** 怎样让约定、页面和检查脚本对哪些 IDEO 日志应挂卡给出同一个答案？依据是 [Sprint 20 判错记录](../documents/sprint/sprint-20-presentable.md#5-test)和[看板约定](../../plugins/ideo-scrum/skills/scrum-kernel/conventions/board-log.md)的现有关联；不改两类卡的外观，不删除或改写日志，不扩张 IDEO 日志的合法归属。

| 独立样本 | Master 提议的预期 |
| --- | --- |
| 1 · 未收尾，`For` 指向开放的 Sprint 或设计 | 只挂在所服务的已有宿主卡下，`Now` 与原文一致，不另建卡。错挂、漏挂不能通过。 |
| 2 · 未收尾，`For` 只指向产品日志 | 不上板。即使仍在活动，也不能挂到任何卡。 |
| 3 · 明确已收尾，`For` 仍指向开放宿主 | 不上板，即使文件尚未归档。建议各覆盖中文明确写「已收尾」与英文明确结束的有效样本，不新增必填字段。 |

**测试与通过线草案：** 三种输入分别核对约定、可见页面和检查判定，三者给出同一答案；误挂两类负样本要能查出，合规省略不报错。[现有检查脚本](../../scripts/board_check/check.py)的旧例同时把 2、3 置真，不能各自作证；收尾检测目前只匹配 `concluded`、`closed`。

**Developer 初估：S（1–2 个会话）。** 已有宿主关联和漏挂、错挂检查，可在现有规则上补齐。中英文明确收尾与「待收尾」要区分；不把解析实现当新的日志要求。两条 PBI 暂无需 PO 补定的价值取舍。

**并行安排（PO 澄清，Master 转达）：** 「我的意思是同步准备好吗？」「我们都是并行的」。Sprint 22 的 Why 与本期 Planning 并行；本期不等 Sprint 22 的结果，只等 PO 明确放行 How。

**H6 测法与通过线 · 2026-11-20 冻结。** 以下把两条 PBI 已定范围和完整 DoD 落为可复核的测法，不重开 What。首次测试前，以仅含本日志的本地提交冻结；被测实现起点 `f030513`，旧模板基线 `00c224b`。后续修正保留首次结果，并对同一判据复测；脚本误判逐项列出原判、人工核对结论和理由，不改通过线。

| 验收项 | 测法与通过线 | 证据 |
| --- | --- | --- |
| 74-A／B／C · 真实设计卡 | 用 `prepare_review.py` 生成同数据的当前／基线页，在本机浏览器离线打开，点总览节点并核可见卡。A、B、C 都是三块：本设计 §1.2 目标逐字相同且不混入关联条目；§2.1 主线各站沿源图顺序且不串源；方案区总存在。A 显示 §3.1 的选定方案，不展开故事板也能读方案，展开后帧与 §3.2 相符。B 无故事板但仍能读方案和用法。C 明示未选，不能把候选当定案。对照源夹具及独立期待，布局、帧数、空态原句和选定理由不作判据。 | `pages/`：当前卡截图、可见摘录和源文对账；§5 按 A／B／C 记结果 |
| 74-B · 独立盲读 | Master 召唤未参与施工的评阅者。仅给实际渲染的 B 卡可见图和无答案任务，不给整页源码、归档、其他卡、作者清单或期待。先保存原答，再对 §3.1 核对：能辨认全局说明指路、反馈按产品进全局记忆，PO 一句话即可、不报位置，反馈可在会话中使用，更新时取回由 PO 决定。按意思核，不能代答或事后讲解。 | `blind/`：B 卡图、任务和独立原答；§5 记逐项对账 |
| 74-R · 其他卡与显示回归 | 确认新旧页的 `board-data` 完全相同；在 1440／900／375 CSS 像素、浅／深色各组合打开两页，分别核产品卡与普通 Sprint 卡的可见内容、外观和交互不变；同一条件观察新版三种设计卡未被遮挡或截断。核实浏览器实际使用该主题、离线仍能加载、点条目高亮、点产品／Sprint／设计开卡、窄屏返回总览；展开 `Now` 与日志原文核对。宽度为取样，不规定新断点；截图差异须解释，不机械以逐像素相等为通过线。 | `pages/`：两页同数据校验、宽度／主题矩阵、截图、真实点击及控制台记录；§5 记录差异 |
| 71-1／2／3 · 归属独立取证 | 每例复制同一套夹具，只改 `For` 或 `Now` 所指的一项条件，明确预期后分别生成并打开实际页，查看所有宿主卡脚；用 `check.py check` 判同一页。开放 Sprint／设计宿主例仅正确卡出现一次且 `Now` 逐字相同；仅服务产品、或有开放宿主但 IDEO 明确结束（中英文分别）均不显示，正确省略不报错。保留待收尾／提到旧事项、宿主缺失、宿主结束未归档但卡仍在、宿主只结束一阶段、完整头部 `Question` 提到 `For:` 的对照。 | `ideo/`：各例源码输入、实际卡脚摘录与判卷；§5 分项记结果 |
| 71-N · 负对照 | 在同一数据副本分别加入误挂、错挂、漏挂、改写 `Now`，以及同时挂正确和错误宿主后的两种卡遍历顺序。`check.py selftest` 和负对照须检查到相应错误；重复挂载两种顺序均被拒。脚本用于证结构与归属，不替代正常页的实际打开和对照。 | `ideo/`：独立预期与判卷；`checks/`：自测原始输出；§5 记录结果 |

| DoD（产品日志 §1.3） | 测法与通过线 | 证据 |
| --- | --- | --- |
| 内容忠实 | 对照设计日志约定、板子第 5、6、8、11、12、16 条和源夹具核验上表；工作约定属于作者做法，不冒称第三方原文。核对差异未改动方法论摘录、已定承诺或归档样本。 | §5 源文对账和差异范围 |
| 署名 | 对照 `ATTRIBUTION.md` 和插件第三方摘录的 `Source`／`License` 行核查许可一致；命令按项目既有登记办法。没有新增第三方摘录；历史欠项如实列出，不用改动未覆盖作为通过理由。 | `checks/` 署名核对与例外；§5 结论 |
| 可导航／无死链 | 从相应 `SKILL.md` 用其显式文件路径逐跳到已改约定和模板，并核插件各技能到 `references/` 的入口；可达 ≤2 跳。解析仓库内 Markdown 相对链接和片段（区分外链、代码示例）；至少改动涉及的入口、两份 README 和本日志链接均打开，基线遗留如实列出，不把未核计作通过。实际点工作区卡脚链接，必须读到同一夹具的日志；另建仅在分支上的隔离夹具实开卡片，只见分支和提交，不生成本地死链。 | `checks/` 链接及两跳对账；`pages/` 实际导航与分支来源；§5 结论 |
| 插件校验／描述长度／DSH | 在本期分支运行 `claude plugin validate --strict plugins/ideo-scrum` 和 `node --test scripts/check_dsh.mjs`，均退出 0。测每个 `SKILL.md` 的实际 `description` 字符数，须 ≤1024；同基线比对描述未改，不增触发专项。分发方式未改，不做安装或角色入口专项。 | `checks/` 命令、退出码、计数和输出；§5 结论 |
| Outcome 两条信号 | 分开对账「一次会话走通、不反复追问」与「熟手陌生人不问作者走完第一冲刺（PBI-63）」。引用已有有效体验证据并注明版本；本次 B 盲读只提供不用讲解理解设计卡的局部信号，不拿它代替全流程。没有在本次覆盖的信号记「未重测」，不声称达到产品 Outcome。 | §5 分开记录产品 Outcome 与本轮 Output |

原始运行材料按运行编号保留在仓库外本会话的 `sprint21-h6/`（`pages/`、`blind/`、`ideo/`、`checks/`）；逐项结果、错误解释和去除本机隐私信息后的必要汇总落入 §5。先给 Master 盲读输入路径，收原答后再作结论；正式 Test 完成后也停在 Review 前。

PO 2026-11-19（Master 转达）：「可以的，没问题，下面准备22吧」。认可 PBI-74 的有故事板、无故事板、尚未选定三种场景和两类其他卡无回归，以及 PBI-71 的三种独立 IDEO 日志归属行为。Developer 已复述，无新增实质分歧，两项精化收口。目标原文：「设计方案看得懂：打开设计冲刺卡，一眼看清这次设计的目标、路线和选定的方案；即使没画故事板，也能知道选了什么、方案怎么用。」本次不放行 How、施工或测试。

## 3. How

**How 入口决定（2026-11-19）：** Master 问「是否同时放行 Sprint 21 进入 How、Sprint 22 进入 What？」PO 答「两期同时放行」（Master 转达）。Sprint 21 进入 How，不等 Sprint 22；PO 在本会话明确「Sprint 21 进 How，先不施工」。核对 §1.1 目标原文：「设计方案看得懂：打开设计冲刺卡，一眼看清这次设计的目标、路线和选定的方案；即使没画故事板，也能知道选了什么、方案怎么用。」

Master 已审阅原计划，Developer 按意见补齐 H5 的反例，PO 随后放行施工。按表中顺序，每块至多一个会话。H1–H5 为施工范围；H6 等 PO 明确放行 Test，测法和通过线按 §2.2 先定稿，经授权单独提交后再测。

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| H1 | PBI-74 · 对齐设计卡的取材约定 | 看板约定中的设计卡数据约定，以及直接受影响的中英文说明 | ✓ 2026-11-20 §1.2 的目标、§2.1 的地图主线、§3.1 的选定方案与可选 §3.2 各有清楚的来源和缺项规则。README 中英不再把设计卡写成展示已完成工作块。 |
| H2 | PBI-74 · 做成三块设计卡 | 更新后的看板模板 | ✓ 2026-11-20 设计卡只在第一块放设计目标，第二块用本设计的简略路线，第三块独立展示方案或明确的未选定状态。产品卡、普通 Sprint 卡及既有导航不改版。 |
| H3 | PBI-74 · 备齐独立样本和判据 | A、B、C 的隔离样本、与约定一致的参考生成和自动检查、读卡对照材料 | ✓ 2026-11-20 A、B 的源日志均明示定案，B 只借用归档 §3.1 的内容，C 明确尚未选定。能用同一数据核其他卡及离线、宽中窄、深浅色表现，读卡任务不透露答案。 |
| H4 | PBI-71 · 对齐 IDEO 日志归属 | 同一归属规则下的看板约定、参考生成与检查判定 | ✓ 2026-11-20 只显示指向实际开放宿主的在办日志；无开放宿主不另建卡，也不判漏挂。仅服务产品日志或已明确收尾的不上板。用既有 `For` 和 `Now`，不增加日志必填字段，不改变合法归属。 |
| H5 | PBI-71 · 拆开归属核验样本 | 三类独立样本及误挂、错挂、漏挂、跨卡重复挂载和改写 `Now` 的检查对照 | ✓ 2026-11-20 每条规则都有独立证据，收尾有中英文代表；不靠一个同时满足两条排除条件的样本。应显示的 IDEO 日志只挂正确宿主才通过；同一条日志同时挂在正确和错误宿主下，无论遍历顺序都必须判错。约定、页面和检查能按 §2.2 逐项对账。 |
| H6 | 本期验收与 DoD 核对 | 两条 PBI 分列的测试证据、DoD 对账和 Master 审阅材料 | 按 §2.2 留下页面与判卷证据；无故事板场景有独立读卡结果。工作区日志链接能打开，仅在别的分支的日志按现行规则只标来源。核对导航和受影响链接、Claude 严格校验与 DSH 自动检查，完整 DoD 逐项说明；结果记入第 5 章，未改分发方式不加重装专项。 |

**Key choices**

- 保留「固定页面 + 一份日志数据」。让 §3.1 的选定方案有独立的数据表达，故事板只补充，不用旧 `story` 反推是否已选。沿用产品卡的路线画法，但只给设计卡使用，避免改动其他卡。
- 按 PBI-74、PBI-71 顺序处理共享的看板约定和检查，证据分开。PBI-71 沿用宿主卡展示，不为排除规则加卡或改日志结构。
- 自动检查只核能从日志或页面查实的要求；「读者能说清怎样使用」由独立评阅者只看卡后与源文核对。保留本工作树内的隔离样本，不回改已归档日志。

**Risks and open points**

- 现模板以 `story` 非空决定方案区显隐，旧数据不一定能证明已有选定方案。旧静态页仍可照旧打开；要看新版，从日志重新生成，不从故事板猜定案。已选但用法没写全，只呈现已知事实。
- 归属判定要区分明确已收尾与尚待收尾；既有判卷对中文收尾不足。只按约定查，避免把符合约定的省略判错。
- Sprint 23 若改动设计日志约定，合入时核对四个章节的取材约定；本期无需等待该 Sprint。未发现需要重开 What 的取舍。

Go-ahead: 2026-11-19，PO：「可以，放行吧，随后你受到master得监督和审阅，出现重大问题可以向我和它询问」。放行本工作树 H1–H5 施工；Master 监督并审阅，重大问题回 Master／PO。Test、提交、合并、打 tag、推送和发布未放行。目标原文：「设计方案看得懂：打开设计冲刺卡，一眼看清这次设计的目标、路线和选定的方案；即使没画故事板，也能知道选了什么、方案怎么用。」

## 4. Increment notes

**2026-11-20 · 施工交审。** H1–H5 的产物在本 Sprint 工作树，未提交。H1 的来源、缺项规则和中英说明已静态核对；H2–H5 的实现和用例已落盘，待实际核验的完成条件尚未打勾。目标和 §2.2 通过线未改。

| 范围 | 产物与取舍 | 待核 |
| --- | --- | --- |
| H1–H3 · PBI-74 | [看板约定](../../plugins/ideo-scrum/skills/scrum-kernel/conventions/board-log.md)与[模板](../../plugins/ideo-scrum/skills/scrum-kernel/conventions/scrum-board-template.html)将目标、路线、方案分开；故事板只作补充。不从旧 `story` 推断定案；旧静态页面无需迁移，要看新卡就从日志重生成。A／B／C 有独立[源夹具](../../scripts/board_check/fixtures/acme/scrum/)和[预期](../../scripts/board_check/fixtures/review-expectations.json)。[准备脚本](../../scripts/board_check/prepare_review.py)以同一数据生成新旧模板对照页，另备 B 卡无答案读卡任务。 | 获准后用 `00c224b` 作旧模板基线，核实际页面、B 卡独立读卡与产品／普通 Sprint 卡无回归。地图顺序、选定语义和可读性对照源文；有 §3.1 正文却填 `null` 只提示复核，不据此判定已选。 |
| H4–H5 · PBI-71 | 看板约定第 11、16 条与[检查器](../../scripts/board_check/check.py)按 `For` 的实际宿主及 `Now` 的收尾状态取材。参考生成和判卷共用归属规则；记录所有挂载，后出现的正确宿主不能掩盖错挂。自测分开覆盖仅服务产品、明确收尾、无开放宿主和应展示的日志，含中英文收尾、待收尾、错挂／漏挂／改写 `Now` 和两个顺序的跨卡重复。 | 获准后跑各独立样本，对照约定、页面与判卷。看板保留识别已有设计宿主的原有展示口径，不修改 IDEO 日志约定对开日志和归属的限制。 |

**静态核对：** `git diff --check`、Python AST、模板 JavaScript 语法和独立预期 JSON 解析通过。沿用「阶段原文没读就产出」反馈所定的先读原文、约定与模板注释；按「看板检查只查约定要求的」项目记忆，不以字段有字替代方案或读卡判断。未生成或打开验收页，未跑自测、独立读卡、插件严格校验或 DSH 检查；未审定 DoD。

**2026-11-20 · 本地检查点。** Master 转达 PO 的决定：只在本 Sprint 分支提交 H1–H5 施工产物及本日志，供 Master 审阅。不改实现或通过线，不进入 Test，不合并、不打 tag、不推送、不发布。

**2026-11-20 · H4／H5 静态审阅修订。** Master 复核 `7453a50`：PBI-74 未见静态阻塞；PBI-71 三处退回当前 Increment 修订，准在本期分支做本地修订提交，仍不放行 Test。目标原文：「设计方案看得懂：打开设计冲刺卡，一眼看清这次设计的目标、路线和选定的方案；即使没画故事板，也能知道选了什么、方案怎么用。」

| 审阅点 | 修订与依据 | 已备对照，尚未执行 |
| --- | --- | --- |
| 明确结束的 IDEO 仍被判应挂 | 收尾只读状态开头的完整表述，支持明确主语与中英文结束动词；不在后文搜关键词。看板约定第 16 条补例，不增加日志字段。 | `Test: The IDEO run has concluded; awaiting archive.` 与 `测试：本轮五模式已收尾，待归档` 应省略且误挂应报错；保留「待收尾」和 `review closed cases` 应挂的对照。 |
| 宿主文件在，宿主已结束 | 依据看板约定第 11、16 条的开放宿主限制，及设计日志约定第 19 条「先结束、后由 Sprint Review 归档」的区别，只在嵌套 IDEO 归属时读取宿主自身的 `Now`。不改 `discover`、宿主卡生成、产品／普通 Sprint 卡或 IDEO 合法宿主范围。 | Sprint 的 `Test: Sprint 01 has ended; awaiting Review archive.` 与设计的 `测试：设计已结束（待 Review 归档）`：保留宿主卡，但在办 IDEO 不挂它，误挂报错。另有宿主文件不存在、仅一轮测试结束而宿主仍在办的独立对照。 |
| `Question` 中的 `For:` 抢字段 | 按模板头部引用行的字段起点或竖线分隔边界取 `For`；冒号后的提问内容不是字段名。不要求新增字段。 | 完整模板头部把问题里的 `For: ../sprint-02-beta/SprintBacklog.md` 放在真正的 `For: ../sprint-01-alpha/SprintBacklog.md` 前；应只挂 Sprint 01。原先不含 `Question` 的简短头部继续保留。 |

自测仍保留「正确宿主先出现」「正确宿主后出现」两种跨卡重复负例。改动仅为看板约定、检查器及本日志；H2–H5 继续待核。此次仅 Python AST 与 `git diff --check` 通过，未导入或执行检查器，未跑任何自测、实测或验收页。宿主恢复时原工作树处于分离 HEAD；确认 HEAD 和本期分支同为 `7453a50`、工作树干净后，重新关联原分支，未动主检出。

**2026-11-20 · Master 复审。** `f030513` 中明确收尾、宿主已结束但未归档、`Question` 内的 `For:` 三处均按已定范围修齐；两个遍历顺序的跨卡重复挂载反例仍在。Master 未发现静态阻塞，将请 PO 决定是否进入 Test。此结论不是验收结果：H2–H5 不勾选；自测、页面、独立读卡、插件严格校验及 DSH 检查均未运行。

**2026-11-20 · PO 委托（Master 转达，逐字）。**「嗯，这样子对于21来说，呃，其他所有的都由你来决定。嗯，关键是到了最后 review 之前，让我来通知我就可以了，其他的在此之前的所有事情你来决定就可以，对于21来讲。」

范围仅 Sprint 21：Master 决定 Review 前的阶段门、测试、修正与复测及本期分支本地提交；到 Review 之前停下，由 Master 通知 PO。仍交回 PO：改 Product Goal、取消冲刺、推翻 PO 已定事项、PO 点名的品味、推送发布。不启动 Review、Retro，不合并、不打 tag、不推送、不发布，不改 CLAUDE.md。B 卡独立盲读由 Master 召唤；Developer 不兼独立评阅。

**2026-11-20（UTC+8）· PO 追加书面委托（Master 在 Test 中转达，逐字）。**「现在他们全部都开跑了，这样子我跟你讲。嗯，每一个对话，我现在给你权限，每一个对话，等到他们 review 之前向我报告就可以了。不意是每一个对话哦。因为他们现在都已经开始跑了。」

覆盖已开的 Sprint 21–25。各期正式 Sprint Review 前的阶段门与常规决定由 Master 处理，到各期 Review 前由 Master 向 PO 报告。仍回 PO：改 Product Goal、取消 Sprint、推翻 PO 已定决定、PO 点名的品味、正式 Review／Retro／收官、推送发布；不代批 CLAUDE.md。本期只续做 Test 内的出处核验，不改变以下入口决定、已冻结判据或当前阶段。

**阶段决定 · 2026-11-20，Master 依上述委托代 PO：Increment → Test（H6）。** 静态复审 `f030513` 未见阻塞，先冻结 §2.2 具体测法与通过线并只提交该日志，再执行本机验证。允许本期分支的判据、范围内修正和证据本地提交；失败保留原证据并按冻结判据复测，需回 Increment 或改验收边界先交 Master。§1.1 当时的目标原文快照：「设计方案看得懂：打开设计冲刺卡，一眼看清这次设计的目标、路线和选定的方案；即使没画故事板，也能知道选了什么、方案怎么用。」Test 完成也不自动 Review／收官。

## 5. Test

**2026-11-20 · Developer 验收。** 按先行本地提交 `9558a0a` 冻结的口径执行；被测插件与检查器仍为 `f030513` 所载实现，旧模板基线 `00c224b`。PBI-74、PBI-71 各自过线，H2–H5 勾选；Master 复核及完整 Test 停点见本章末。原始运行、首轮误判与复测留在仓库外 `S:/IDEO-Scrum-Archives/sprint-21-design-board/h6-9558a0a/`，下表证据路径相对于它。

| 验收项 | 结果 | 证据 |
| --- | --- | --- |
| 74-A | 过。目标逐字相同，只含设计目标；主线五站按源图顺序，独立方案写明仅重试失败批次。故事板折起时可读方案，点开后两帧与 §3.2 的题、文相符。 | `pages/matrix-corrected.json`、`pages/captures-corrected/story-A.png` |
| 74-B | 过。三块可见、目标和地图与源文一致；未生成故事板。独立评阅者仅看渲染截图和三问，答出选了什么、怎样用及后续动作，见下方原答。 | `pages/captures-corrected/`；`blind/card-B.png`、`blind/answer-original.md`、`blind/source-check.md` |
| 74-C | 过。目标逐字相同、本设计路线与源图一致；方案区仍在，显示尚未选定，不把两种退款候选写成已选。 | `pages/matrix-corrected.json`、`pages/captures-corrected/1440-light-current-design-choosing.png` |
| 74-R | 过。实际 Edge 取 1440／900／375 × 浅／深六种环境，共 42 卡次，均核实离线。两页 `board-data` SHA-256 相同；产品、普通 Sprint 共 12 组对照可见内容、截图与交互一致。当前三设计卡未见遮挡、截断或横向溢出。26 组条目高亮／取消、窄屏返回检查通过；产品圈和各节点实际开卡；`Now` 初见折叠、展开与源文相同。控制台错误和 HTTP 请求均 0。 | `checks/board-summary.json`、`pages/matrix-corrected.json`、`pages/captures-corrected/` |
| 71-1／2／3 | 过。13 份独立夹具离线实开并逐一看卡脚、与约定和判卷对账。开放 Sprint／设计只在正确卡出现一次，`Now` 原样。仅服务产品、中英文明确结束、缺宿主、Sprint／设计宿主各自结束未归档共 6 例省略且误挂各被拒；结束未归档不删宿主卡。待收尾、提及旧事项或宿主只结束一轮仍应挂；`Question` 里的词不抢实际 `For`。 | `ideo/fixtures.json`、`ideo/browser-corrected.json`、`ideo/captures-corrected/` |
| 71-N | 过。5 个负例分别报错挂、漏挂、改写 `Now`、正确宿主先／后两种重复；均退出 1 且命中对应错误，不以技术失败充数。当前页检查无告警；自测 79 项均通过。 | `ideo/fixtures.json`、`checks/current-page-check.json`、`checks/board-selftest.json` |

**首轮判错及复测。** 首轮浏览器驱动置了网络条件但没有核实 `navigator.onLine`，不能拿该轮作为严格离线证据；折叠判定取隐藏段落的 `innerText` 得到空串，误报 `Now` 未折叠。原始 `pages/matrix-first.json`、`pages/matrix-summary-first.json` 和截图全部保留。核过可见截图与原始 `Now` 后，仅修仓库外驱动：导航前禁 HTTP(S)，明确模拟断网并核实浏览器报告离线；折叠用原文 `textContent` 对照可见卡文字。重新走完全部 42 卡次和 13 归属页，沿用原判据，未改插件或样本。首次盲读图边缘截到卡型徽标，三块内容完整；复测另保留整张卡，未提示评阅者改答。

**B 卡独立原答（Master 转达）。** Master 召唤的独立 Sonnet 评阅者只收到 B 卡截图和任务，未看源文、预期、其他卡或作者解释：

| 问题 | 我的回答 |
| --- | --- |
| 这次设计选了什么？ | 选的是「记一下就够」：用全局说明告诉 AI 怎么处理反馈，把反馈按产品记进全局记忆。卡上说清了反馈去哪一类地方，看不出具体存在哪儿。 |
| 如果要使用它，你会怎么做？ | 用产品时发现问题，我就把问题告诉手边的 AI，说一句「记一下」，不用告诉它记在哪里。要是我没说产品名、AI 也认不出来，卡上看不出要怎么处理。 |
| 按卡片这样使用之后，接下来会发生什么？ | AI 会按产品存下这条反馈；反馈在会话里马上生效，等更新产品时再集中取回，由 PO 决定改什么。卡上看不出「马上生效」具体会改变什么，也看不出更新时是谁、怎么发起取回。 |

**按冻结语义逐项核对：** 第一问对上标题与步骤 3（全局说明指路、按产品进全局记忆），第二问对上步骤 2、3（一句话、不报位置），第三问对上步骤 4、5（会话里立即用，更新时取回由 PO 决定）。具体路径、拿不准归属的处理、生效细节及发起取回的角色／方式未在卡上交代，原样保留读者观察，不补讲、不改判据。

**完整 DoD 对账（产品日志 §1.3）。**

| Output Done | 结论及证据 |
| --- | --- |
| 内容忠实 | 本期通过。设计日志约定给出 §1.2、§2.1、§3.1 与可选 §3.2 的来源；看板约定第 5、6、8、11、12、16 条属作者工作约定。三种设计卡与各自源文相符；只借归档设计 §3.1，不改归档；两条承诺及第三方原文摘录与基线相比未改。 |
| 署名 | 未判通过。独立核查确认现有许可标注与 `ATTRIBUTION.md` 表面一致、命令按既有登记，本期无新增第三方摘录。Master 复核指出，现有标注相同不能证明五份 `IDEO-modes/` 的具体底本与旧版补料均已对上出处和许可；见下方复核及原件链接。SGEP 资产的原文粗体标签已给出处与许可，不是缺署名。 |
| 可导航 | 过。沿用 Sprint 16／17 的同一口径，从各技能入口到其自有材料 ≤2 跳；本期 `scrum-kernel/SKILL.md` 到看板约定、模板和四份 `references/` 各 1 跳。`sprint-kernel` 经 scrum 入口到四份引用 2 跳。`checks/doc-audit/nav-own.txt`、`nav-all.txt` 记录实测；设计、IDEO 入口不是这些 Scrum 引用的使用入口。 |
| 无死链 | 过。提交前扫描 132 份文件，139 条相对链接、17 个锚点，0 断；基线 124 条、12 个锚点，亦 0 断。两份 README、相应入口和本日志可解析。实点六个工作区卡脚链接，均打开对应 Markdown、内容逐字一致；仅在分支的 `sprint-02-beta` 只列分支与提交，不生成本地链接。见 `checks/doc-audit/current-links-submission.json` 与 `pages/matrix-corrected.json`。 |
| 插件严格校验 | 过，`claude plugin validate --strict plugins/ideo-scrum` 退出 0，`Validation passed`；`checks/claude-strict.stdout`。本次不发布，不把本地校验写成外部目录审核。 |
| 技能描述长度 | 过。按字符计：ideo 1023、design 1007、scrum 968、sprint 943，均 ≤1024，与基线逐字相同。`checks/doc-audit/desc-current.txt`、`desc-base.txt`。 |
| DSH 分发 | 过，`node --test scripts/check_dsh.mjs` 6/6、退出 0；`checks/dsh.stdout`。分发方式与版本未改，无需重装或另验角色入口，不把这次自动检查写成安装验收。 |

| Outcome Done | 证据与界限 |
| --- | --- |
| 一次会话完整引导，不反复追问 | 本期未重测新会话的全环节。B 盲读是局部证据：未讲解也理解卡片，不能代替完整方法论引导。 |
| 熟手陌生人走完第一冲刺，不问作者、不卡死 | [Sprint 20／v6.0.3 的 PBI-63 记录](../documents/sprint/sprint-20-presentable.md#5-test)：冻结口径下一组 3 次中的 2 次走完，问作者 0 次，无文档卡点；另一轮是技术失败。本期未重跑全流程，不把旧版或 B 盲读作当前整产品 Outcome 已达成。 |

**基线遗留。** 除署名口径待核外，Sprint 与设计日志模板共三处用裸文件名加文字定位其他内核（Sprint 模板行 7、20，设计模板行 6）；能按文字找到，不是 Markdown 死链，但未达到 CLAUDE.md 的跨内核显式相对路径规约。与基线一致，未在本期顺手改。

**跨期合流待核（Master 交接，不属本轮判据）。** Sprint 23 设计结束时在既有 `Now` 写 `Concluded — awaiting archive` 或等价语义，首个 Review 才迁出活动路径。合流后分别核「开放」「结束待归档」「已迁出活动路径（含分支残留）」的宿主发现、来源标注与 PBI-71 嵌套归属；本期只排除已结束宿主下的 IDEO，不改变宿主卡发现，不提前合流。

**2026-11-20 · Master 复核 `7ae87ff`。** PBI-74／PBI-71 均按 `9558a0a` 过线。认可首轮仅修取证驱动，保留原判，按原口径复测；不重跑已通过项。SGEP 资产的粗体标签不缺出处或许可，三处基线裸路径另记，不计为 Markdown 断链。

**五模式署名缺口。** Master 核对 `89eb3dd` 的 Stanford 底本、`0d2629f` 从早期内核提取的补料及 `832092c` 的合并，确认有两路材料。`6c1017c` 改注现版 d.school 的 4.0 标注，但未逐项对上具体底本和旧版补料。[HPI 留存的 Stanford Bootcamp Bootleg 2010 原件](https://hpi.de/fileadmin/user_upload/fachgebiete/d-school/documents/01_GDTW-Files/bootcampbootleg2010.pdf)第 2 页明载 `CC BY-NC-SA 3.0 Unported`；[Stanford d.school 现版 Design Thinking Bootleg 页面](https://dschool.stanford.edu/tools/design-thinking-bootleg)标注 `CC BY-NC-SA 4.0`。这只证明两版原件的标注不同，不据此推定本仓库任何段落适用哪一版许可，不认定 IDEO 是另一个出版者，也不作侵权判断。待核的是具体内容、原件版本、出处与许可的逐项对应。

**2026-11-20 · 五模式出处续核（Master 已核）。** `0d2629f` 的 38 个补料文本块逐词对应 Stanford 官方 2018 版 *Design Thinking Bootleg* PDF 第 3–12 页；4.0 标注出自链接该 PDF 的 Stanford 资源页，不据此反推历史下载记录或整份正文的许可。`89eb3dd` 的底本可追到本地 *An Introduction to Design Thinking — Process Guide* 的 DOCX／MD；仍缺与该底本对应、能确认具体版本和出处的官方原件，以及针对该版本的许可声明或权利方授权。2010／2018 年版 Bootleg 的许可不能替代这份证据。逐模式行号、页码和原件见仓外归档 `checks/attribution-audit/five-modes-evidence.md`；没有新的官方原件或权利方依据，不再重复查同一镜像。

**2026-11-20 · Process Guide 副本与官方出版维基取证（待 Master 裁定）。**
1. **第三方副本对账（Master 所交）：** `checks/attribution-audit/process-guide-license-check.md` 与 `process-guide-alnap.pdf`（SHA-256 `72bb9da7b55f39e39cff440ca2a7a8a5924ff90d75d385674b17e0da7efdb196`，6 页，ALNAP 目录列 HPI of Design 2010）第 2–6 页分别对应 Empathize／Define／Ideate／Prototype／Test；目录页、PDF 文本、渲染页、批注与 XML 均未见许可。
2. **官方原页与字节相同原件：** 沿 Wayback 存档核实 Stanford d.school 官方 `Design Resources` 维基页 [`Design Process Mini-Guide`](https://dschool.stanford.edu/groups/designresources/wiki/36873/Design_Process_MiniGuide.html)（建于 `2011-06-16`，`2012-08-02` 由 Thomas Both 编辑；同维基 [`The Wallet Project`](https://dschool.stanford.edu/groups/designresources/wiki/4dbb2/The_Wallet_Project.html) 亦直接指向它）同时挂载屏显 6 页 `ModeGuideBOOTCAMP2010L.pdf`（`2016-01-18`／`04-06` 及 `dschool-old` `2017-11-09` 捕获，与 `process-guide-alnap.pdf` **逐字节相同**，`2010-09-29` InDesign CS3 建档；正文 3,156 词与本地 `references/IDEO-StanfordDesignGuides.md` 去图片标记后 3,145 词除排布引语、封面与连字外全对得上）与小册子 11 页 `ModeGuideBOOTCAMP2010.pdf`（`2014-10-22` 捕获，SHA-256 `7ee2e054...`，封面＋五双页模式）。两份 PDF 及 `wiki/36873` 本页（含 `revisions/36873/2–4` 与 `2013–2023` 存档）自身均无版权或 CC 文本；APA 目录指向的教师个人目录 `509554.pdf`（Wayback `2026-11-11`，SHA-256 `a2bc58a4...`，`2010-11-08` Quartz 重印）系个人转载，非官方原件，亦无许可。
3. **同维基首页授权与现行站状态：** `wiki/36873` 所属的官方维基首页 [`https://dschool.stanford.edu/groups/designresources/`](https://dschool.stanford.edu/groups/designresources/) 自 `revisions/welcome/14`（`2011-06-19`，`36873` 建页三日后）起至 `2013-01-30`、`2016-03-15`、`dschool-old` `2019-10-06`、`2023-01-30` 捕获均明载 `"The resources in this wiki by Hasso Plattner Institute of Design at Stanford are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. Permissions beyond the scope of this license may be available at info@dschool.stanford.edu."`（带 `rel="license"` 指向 `by-nc-sa/3.0/`）。现行 `dschool.stanford.edu` 站点（506 URL 站图、`/innovate/tools`、`/innovate/tools/from-the-d-school-archive`、`/connect/faq`）及 2017–2021 `/resources/` 存档均未列名或托管本文件，原维基路径已 404／`dschool-old` 不可达；现行页脚标 `© 2026 ... All Rights Reserved.`，`/connect/faq` 仅泛称遵循 CC 非商业相同方式共享原则，Stanford 网站条款限个人非商业下载。详见仓外归档 `checks/attribution-audit/publisher-wiki/publisher-wiki-evidence.md`。
4. **未闭环缺口（本次不改原文与现有署名）：**（a）授权声明位于维基首页（空间级），不在 `wiki/36873` 单页或 PDF 内；（b）官方维基已下线，仅有存档证据、未发函取得权利方书面回执；（c）该官方空间级声明为 `CC BY-NC-SA 3.0 Unported` 且来源为 *Design Process Mini-Guide*（*Process Guide*），而本仓库 `ATTRIBUTION.md` 第 3 节与 `IDEO-modes/*.md` 现仅标注 2018 *Design Thinking Bootleg*（`CC BY-NC-SA 4.0`），尚未登记该底本与 3.0 许可。

**Test 停点：** H6 不勾，整体 Test 未判通过，两条 PBI 过线不变。只补记证据与缺口，不重测，不改旧署名、原文、CLAUDE.md 或冻结标准，不回 Increment，不进 Review 或 Retro，不收官；不合并、不打 tag、不推送、不发布。
