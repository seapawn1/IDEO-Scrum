# Sprint Backlog · Sprint 24（加载可靠性）

> Started: 2026-11-19 | 达成 Sprint Goal 或 PO 停止时收官 | Branch: `claude/sprint-24-loading-reliability-012ded` | Product Owner: SeaPawn | Scrum Master: IDEO-Scrum Master | Developer: Sprint 24 Developer
> Now: Increment，H6 基线复核与瓶颈拆解已完成，交 Master 审阅并申请 H7 施工（依 2026-11-20 书面委托）；H7–H11、冒烟、可选预载与支出仍未放行。
> Waiting for PO: None
> 日志写法见 [sprint-log.md](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md)。

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 先读原文再动笔：叫出角色就能调齐该用的内核；定目标、写设计问题或精化条目前，AI 先读并用上对应的原文、约定和模板注释，不用 PO 反复提醒；承诺照常提示，发消息时不再为检查未变的承诺等上几秒。 |
| --- | --- |

<!-- The Product Owner decides it: this Sprint's one commitment (sprint-log.md, conventions 4 and 20). -->

本期让使用者不必反复提醒 AI 才能按方法走下去，让[产品化目标](../ProductBacklog.md#12-product-goal)里的「懂 Scrum 的人照着就能走完第一个冲刺」更可达。依据是[六期总表的 Sprint 24 与反馈对账](../documents/sprint-roadmap.md#六期分工)（F03、F04、F06、F07、F14、F15）。

### 1.2 Definition of Done

<!-- The Product Owner picks them: the Definition of Done items that matter to this Sprint (convention 5 in `product-log.md`, in the scrum-kernel skill's `conventions/` folder). The chapter ends with the Product Owner's decision on the Sprint Goal (sprint-log.md, convention 24). -->

完整产品 DoD 继续生效。本期重点核验方法原文忠实、署名正确、参考材料从技能入口两跳可达、内部链接有效，以及 Claude 插件严格校验和 DSH 既有回归通过。若没有改分发方式，不把重新安装列为本期专项。

完整标准见[产品日志 §1.3](../ProductBacklog.md#13-definition-of-done)。这里记录质量要求，不是测试结果；角色调用、原文读取与运用、承诺行为和耗时分别留 PBI 专项证据。

**PO 决定（2026-11-19，Master 转达）：**「定案并放行 What」。已按 [§1.1 承诺表](#11-sprint-goal) 核对目标原文，定案范围为 Sprint Goal 与本期 DoD 核验重点；只放行 What。

## 2. What

### 2.1 Product Backlog Items

<!-- The Product Owner leads the selection; the Scrum Master and the Developer say when it is too much or too little. The selected items, copied word for word from the product log (sprint-log.md, convention 5). -->

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-80 | 起草产物前真正读到阶段原文 | 作为 PO，我想在 AI 定目标、写挑战与问题或精化条目前，让它读对应的原文、约定及模板注释，以免反复纠正没有依据的草稿 | Map ③、④、设计阶段 | 待估 |
| PBI-81 | 角色入口按顺序调齐内核 | 作为熟手，我想召唤角色后不必再提醒它加载对应内核，以便不同角色遵守相同的入口规则 | Map ② | 待估 |
| PBI-82 | 内核加载时带入需要的方法原文 | 作为熟手，我想在加载 sprint-kernel 时就得到 Sprint Backlog 与 Sprint Goal 的原文，以便 Planning 有依据，而不必预载所有阶段材料 | Map ②、④、设计阶段 | 待估 |
| PBI-83 | 承诺 hook 的响应时间 | 作为熟手，我想继续得到正确的承诺原文，又不用每发一条消息就多等两秒，以便会话不被重复开销打断 | 看板与承诺注入 | 待估 |

### 2.2 Refinement

<!-- The Scrum Master leads. What refinement settled, each point with who decided it; the acceptance criteria; the tests' method and pass lines (sprint-log.md, conventions 6 and 13). The chapter ends with the Product Owner's decision that refinement is over (sprint-log.md, convention 24). -->

**PBI-80（Master 提议的验收口径；下列样本与门槛由 Developer 草拟；经 Master 复审）**：以上表用户故事为 POV。我们怎样让 AI 在交首稿前读全当前阶段指定的原文、约定和模板注释，并在草稿里用对，不等 PO 追问？PO 指出不合方法时，先回查对应依据再重拟。

| 证据 | 单次判定 |
| --- | --- |
| A · 先读全 | 对照事件顺序，指定正文和注释须完整到达起草者的上下文，早于首份实质草稿（聊天或落盘，以先发生的为准）。分段读完、实际带入等价全文都算；只有路径、Skill 调用、无有效结果、只读片段、读写同批尚未返回内容或先写后补读均不算。Skill 调用顺序由 PBI-81 另验。 |
| B · 用对 | 判卷者按下表对照首稿和原文，逐项都有文本证据才通过；不按关键词、文件名或模型自报给分。A、B 必须在同一试次都通过，不能相互替代。 |

**必读清单与内容判据**：路径相对 `plugins/ideo-scrum/skills/`。四题共读 `scrum-kernel/overview.md`；原文及约定读全表列文件，模板读表列部分的完整注释。另用了某个阶段方法就须先读该方法全文；不因读到可选操作就强制执行该操作。

| 样本 | 原文 | 约定与模板注释 | B · 产物要做到 |
| --- | --- | --- | --- |
| G1 · Product Goal | `scrum-kernel/references/scrum-artifact-product-backlog.md` | `scrum-kernel/conventions/product-log.md`；`scrum-kernel/conventions/product-backlog-template.md` §1.2 | 单一、中期的价值目标；不把下周一次交付当成目标，也不是无限期愿景。 |
| G2 · Sprint Goal | `sprint-kernel/events/scrum-event-sprint-planning.md`；`scrum-kernel/references/scrum-artifact-sprint-backlog.md` | `sprint-kernel/conventions/sprint-log.md`；`sprint-kernel/conventions/sprint-backlog-template.md` §1.1–1.2；读取本题产品日志 §1.2 | 一个本期使用者价值，推进已有 Product Goal；短信、入口等不是并列目标，不替 What 选条目。 |
| D1 · 设计挑战／目标／问题 | `design-kernel/steps/1-1-define-the-challenge.md`；`design-kernel/steps/1-2-start-at-the-end.md`；`design-kernel/steps/1-3-ask-the-experts.md`；`ideo-kernel/IDEO-modes/empathize.md` | `ideo-kernel/conventions/ideo-log.md`；`design-kernel/conventions/design-log.md`；`design-kernel/conventions/design-backlog-template.md` §1 及 §1.1–1.3 | 挑战交代为何现在、以谁的经历为据，保留第一手／第二手区别；目标写愿景不写解法；把失败假设改成这个设计能回答的问题；不虚构访谈。 |
| R1 · 精化条目 | `sprint-kernel/events/scrum-event-sprint-planning.md`；`scrum-kernel/references/scrum-artifact-product-backlog.md`；`ideo-kernel/IDEO-modes/define.md`；`ideo-kernel/methods/how-might-we-questions.md` | `scrum-kernel/conventions/product-log.md`；`sprint-kernel/conventions/sprint-log.md`；`sprint-kernel/conventions/sprint-backlog-template.md` §2.2 | 从已有条目或目标逐字立 POV；HMW 留出多种解法；区分 PO 决定、Developer 可提方案、待研究问题；给可核对的验收草案，不替 PO 定案或进入 How。 |

**固定样本输入（合成借阅服务，不取真实项目资料）**：每次从相同的最小项目副本起步。`scrum/ProductBacklog.md` 取 `00c224b` 的产品日志模板，名称为「小馆借阅」，§1.1 第二格为「小馆借阅：让社区图书馆读者查阅和管理自己的借阅。」；G1 的 §1.2 留模板占位，其他三题填「读者不必跑柜台，也能自主处理借阅，不因弄不清到期日或续借结果而逾期。」。R1 额外有一个冲刺日志，从同基线的模板起稿，头部 `Now: What`，§1.1 第二格为「读者到期前能办续借，并知道是否成功。」；产品日志和冲刺 §2.1 都有下表 R1 的 PBI，编号 `PBI-001`，标题「续借被拒后知道怎么办」，定位「线上续借」，规模 S，产品日志状态为「Sprint 01」。其他字段保持模板占位，无其他历史承诺或隐含指令。先真实调用 `/ideo-scrum:scrum-master`，等该回合结束再原样发题；题面不列路径或提示先读。

| 样本 | 发给被测会话的原话 |
| --- | --- |
| G1 | 「我就是产品负责人。小馆已经能查借到什么书；每周都有读者因为不清楚到期日或续借结果白跑柜台，也有读者只能在闭馆后处理。下一周能做一条短信提醒。产品日志 1.2 还空着，给我拟一个 Product Goal，先在对话里给首稿。」 |
| G2 | 「可以启动这个冲刺的 Planning，先只做 Why。现状是读者知道哪天到期，但还看不出能不能续、有没有续上；柜台最近收到了这些求助。手上的想法是短信提醒、续借入口和回执。结合产品日志，给我拟一条本期 Sprint Goal，先在对话里说。」 |
| D1 | 「准许做这个设计冲刺的共情，暂不进定义。我是来续借的读者：上周五 19 点我赶到柜台，门已经关了；手机上点了两次续借，只看到『处理中』，我第二天又跑了一趟。馆长说旧的线上入口下月要关。基于这些材料，先在对话里拟设计挑战、设计目标和设计问题。」 |
| R1 | 「这个冲刺已进入 What，先用 HMW 精化 PBI-001：『作为读者，我想在续借被拒时知道接下来还能怎么办，以便在到期前作决定。』甲说想马上知道能否借到另一本，乙只想知道必须何时归还。先在对话里给精化草案，不进 How。」 |
| G1 · 纠偏续轮 | 每个 G1 首稿后的同一进程、同一会话原样发：「上一稿不合方法论，我要的是 Product Goal。请重拟。」额外验 A：反馈之后、重拟之前确实回查 `scrum-artifact-product-backlog.md` 的 `Commitment: Product Goal` 原文（能查到正文，不是只报路径）；B：重拟仍满足 G1 判据。与首稿分栏，不拿第二稿替换首稿。 |

| 测试口径 | Developer 建议（未运行） |
| --- | --- |
| 环境及对照 | 同日同一 Windows 机器、同一 Claude Code 版本、Git Bash、同一路由下实际相同的 magpie 便宜模型；以 `00c224b` 的插件目录对照评审后锁定的候选快照，同一题及权限，只有插件快照不同。按 [无头回归手册](../documents/headless-testing.md) 隔离设置、记忆、MCP 和测试目录，只保留插件与题目所需的 `Skill`／只读工具，不给写文件或启动代理的能力；不加载作者的临时规矩兜底。开跑前记录宿主版本、两臂快照、题面与夹具版本；冒烟每臂一回，确认实际权限与模型匹配、原生角色入口可用、事件流足以复原正文和首稿顺序。遥测留仓外，记录不带认证值。 |
| 样本与通过线 | 每题三对有效样本，共 24 个独立会话；题号和重复号预先固定，交替先跑基线／候选；每个 G1 在本进程里加一轮纠偏。每题候选须至少 2/3 同次通过 A 和 B，且每题的 A 通过数、B 通过数、A 与 B 同次通过数分别不低于基线；G1 纠偏另用同一规则。一题不过不得平均抵消；基线已满分、候选同分只报持平，不说改善。逐试次列 A、B 和证据，Master 审内容与边界误判。 |
| 失败与停止 | 漏读、迟读、内容不合、或无技术错误但未在有效回合交稿均算行为失败，不补跑。API／宿主报错、限流、超时等有记录才列技术失败，整对补测，同一对最多补一次、整轮最多补两对；可归因插件的错误不按环境排除。权限未隔离、两臂模型不同、该取的事件缺失或仍凑不齐样本，停并标证据不足，不改判据。每条消息等上一条 `result` 后再发，单回合上限 150 秒，超时杀整棵进程树。 |
| 试次与授权 | G1 的三对首轮角色调用同时作为 PBI-81 的 Master 冷启动样本；仍等该回合结束再发 G1 题面。四个场景共 24 次有效启动，G1 纠偏增加 6 个同进程回合，不增加启动数。冒烟、补测、费用与放行归本节末的跨 PBI 总表，不分项重复请款。 |

**Developer 初估仍为 M（3–5 个会话）**：包括四类样本、纠偏与可审证据；扩大宿主或场景覆盖再估。§2.1 的原文不变。尚未实施或运行测试；精化决定见本节末。

**PBI-81（Developer 草案；经 Master 复审）**：以上表用户故事为 POV。我们怎样让四种角色一进门就调齐对应内核，不等 PO 补一句？按 F07，Claude Code 角色入口的承诺是**实际调用**，不是把正文放进上下文就算调用。下表省略 `ideo-scrum:` 前缀。

| 冷启动：唯一用户输入 | 依次成功的内核 `Skill` 调用 |
| --- | --- |
| `/ideo-scrum:scrum-master` | `ideo-kernel` → `scrum-kernel` → `sprint-kernel` → `design-kernel` |
| `/ideo-scrum:developer` | `ideo-kernel` → `scrum-kernel` → `sprint-kernel` |
| `/ideo-scrum:designer` | `ideo-kernel` → `scrum-kernel` → `design-kernel` |
| `/ideo-scrum:stakeholder` | `ideo-kernel` → `scrum-kernel` |

| 测试口径 | Developer 建议（未运行） |
| --- | --- |
| 证据 | 从宿主确认角色入口生效后，把每次 `Skill` 调用与成功结果按 ID 配对；前一个成功后才调下一个，全部成功后才开始角色工作。纯文本、`Read`、工具请求未成功、合批并行或先做其他事都不算。冷启动不多调其他内核。同会话只可略过已实际成功加载的内核。 |
| 样本与线 | 每角色三对，候选须各 3/3 通过。Master 固定用 PBI-80 的 G1 三对，只判还没收到题面的角色入口回合，不重开会话；G2、D1、R1 的入口不替换 G1。其余三角色各用同一 G1 夹具开新会话，首条只发上表原生命令。两臂 Stakeholder 第 1 个试次入口成功后，在原进程发 `/ideo-scrum:developer`，应只新调 `sprint-kernel`；基线若首轮失败则注明无复用前提，不另选试次。候选复用例也须通过，不替代冷启动。 |
| 失败与停止 | 缺调、错序、失败后继续、用读文件顶替均不补跑。宿主未原生解释角色命令、模型或工具隔离有漂移、取不到成功结果时先停；技术补测用跨 PBI 总表的共同额度，不另开预算。 |
| DSH 边界 | [现有适配器](../../dsh/index.js)在原生角色正文中直接放入 `ideo-kernel`、`scrum-kernel`，再按任务调其他内核；这不算 Claude 的实际工具调用证据。建议本期按 Claude 核验上表，DSH 保留独立原生行为与既有回归；若 PO 也要求 DSH 逐次实调同一套顺序，需单独谈兼容性、范围和真实入口验收，不默改适配器。 |

**Developer 初估 S（1–2 个会话）**，按上述 Claude 入口范围；跨宿主改行为则重估。

**PBI-82（Developer 草案；经 Master 复审）**：以上表用户故事为 POV。我们怎样让 Planning 一调入 `sprint-kernel` 就能看到需要的原文，而不把其他阶段的材料一股脑带进来？F15 已定前一项；F14 把其他预载范围留给实测，不把全量常驻、拷贝或索引定为做法。

| 证据 | 样本与建议通过线（未运行） |
| --- | --- |
| 加载即包含 | 三对新会话，复用 PBI-80 的隔离环境与两份快照，固定输入「请用 Skill 加载 `ideo-scrum:sprint-kernel`，先到这里。」只看首次成功加载时实际给同一会话的正文，不看后来读到的资料或模型背诵。候选 3/3 都须包含[现行产物原文](../../plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-sprint-backlog.md)从 `## Sprint Backlog` 到文末的完整段落（含 `Commitment: Sprint Goal`），对应溯源和授权可核对。除换行格式外逐字校对；摘要、链接、残页、随后才读到均不通过。在正文有变化的同一提交里，重新对照该原文防止漂移。 |
| 与 PBI-80 分开 | 本条只证明来源内容在加载时已经可用；不替代起草前指定材料读全、草稿使用正确的双证据。原文保留、导航和署名按产品 DoD 核对；DSH 既有回归另验，若触及分发另验真实安装和入口。 |
| 可选预载取舍 | 先以只满足必带原文的候选作对照。只有 PBI-80 在特定场景还漏了资料，且现有证据指向入口内容不足，才提一个可选材料集，让 Master 确定后同题做三对冷会话对照。建议至少多一个先读与用对双通过的样本、两栏均不倒退，且首次携带可选材料的模型请求，相比对照臂同一位置的请求，新增总输入不超过 1,000 tokens（计入缓存读写，候选线，未定）；无改善、证据不足或超线都不增加预载。不得给试题加阅读提示，也不强求预载来弥补草稿判定不合。 |
| 试次与停止 | 必带原文的三对单独冷启动，不借角色入场的加载结果；可选对照另列在本节末的跨 PBI 总表。实际载入正文取不到时停报证据不足；读到了错误或不完整的正文是行为失败，不补跑。 |

**Developer 初估 S（1–2 个会话）**，限已确定的必带原文与判据；可选预载另看证据和预算，不先承诺扩大。

**PBI-83（Developer 草案；经 Master 复审）**：以上表用户故事为 POV。我们怎样让常态发消息少等，同时保证该提示时仍得到承诺原文？已确定的是语义不变。F04 的 2.1–2.4 秒是旧测，不代替 `00c224b` 同条件实测；300 ms 是旧建议，不是 PO 门槛。

| 语义证据（未运行） | 两份快照的预期结果及证据范围 |
| --- | --- |
| 脚本层 · 会话起点 | 合成 `SessionStart` 的 `startup`、`resume`、`clear`、`compact`、`fork`，脚本每次须输出当前承诺原文。`clear`、`compact`、`fork` 本轮只到脚本层，不验证宿主是否触发或交付上下文。 |
| 脚本层 · 常态及内容变化 | 使用 G2 的合成产品日志和含 R1 目标的单冲刺日志。启动后，连续两条普通消息、只改备注，脚本均无输出；将「续借」改成同字节长的「展期」（另复测相同修改时间），下一条须输出更新后的全文，再下一条静默。不同会话不共用上次状态；无历史状态时仍须输出当前承诺。 |
| 脚本层 · 日志与开关边界 | 用中英承诺表各跑；单一 Sprint／设计时输出正确目标和名称，多个同类时仅报数量；模板占位不输出；缺产品日志或无有效产品承诺时静默；不可读的次级日志不抹掉 Product 和 Product Goal。`IDEO_SCRUM_COMMITMENTS=off` 时两类事件均静默、正常退出；恢复开启后按原行为输出。 |
| 脚本层 · 判定 | 按[现行承诺约定](../../plugins/ideo-scrum/skills/scrum-kernel/overview.md)与 [hook 注册](../../plugins/ideo-scrum/hooks/hooks.json)重放合成事件。以夹具日志预先确定的原文判输出、静默、退出结果和更新次序；全部样本须正确。只能证明脚本行为，不证明宿主已注入。 |
| 真实宿主层 · 判定 | 总表六次启动只覆盖新会话启动、恢复、承诺未变、承诺变更及关闭开关；逐项核对原生 hook 事件及 debug 日志中的上下文交付记录，不用脚本 stdout 或模型复述代替。并列报告脚本证据与实际取得的宿主证据；宿主证据缺失不写通过。DSH 另跑既有回归，不套用 Claude hook 的计时。 |

| 耗时口径 | Developer 建议（未运行，与语义证据分开） |
| --- | --- |
| 环境、基线、样本 | 同一台 Windows、同一 Claude/Git Bash 版本及同类磁盘，`00c224b` 对候选。固定两种日志夹具：G2 产品日志加一份已填 Sprint Goal；第二种在同一夹具产品日志末尾添加 200 行固定无关备注。每臂用独立临时目录与会话状态，先做 `SessionStart`、再暖身三条；每夹具采 30 对普通不变提示，交替臂顺序。用单调钟量事件触发时承诺处理的等待，含命令启动，不算模型生成、网络或交互时间。主要在本机重放，宿主 `hook_started`／`hook_response` ID 配对只作边界核对；不能用不同计时范围或不同缓存状态相减。另报告 startup 和内容变化耗时，不混进常态样本。 |
| 性能通过线（Master 按 PO 委托定案，未运行） | 同日同环境与 `00c224b` 比较，两种夹具的常态未变提示各自 P50 至少下降 50%，P95 不高于基线且 ≤1 秒。两层各自覆盖的承诺原文、注入时机、开关行为须全部通过，不拿少注入换速度。旧测 2.1–2.4 秒仅作参考，300 ms 不是门槛。若同日基线不复现旧慢，带证据停报 Master，不临时改线。 |
| 失败与停止 | 维持现有 10 秒超时判定；超时不当作短耗时，也不剔掉归因于插件的失败。事件无法配对、时钟或环境不可比、样本不足或语义失败即停，不给出优化通过。宿主和本机额度分列在下方总表；本机重放不发模型请求。 |

**Developer 初估 M（3–5 个会话）**，含当前瓶颈复测与不改变承诺行为的验证。

**跨 PBI 试次分配与预算（必需项的规划上限；未授权实测或支出）**：一对为基线与候选各一试次。启动数按进程计，恢复同一会话也计一次；同进程续轮不新增启动，但其时间与费用计入总额。共享样本按预定编号复用原始记录，各 PBI 独立判定，不挑试次或重复计费。

| 必需证据 | 试次分配与共享 | 计入本轮的新增宿主启动 |
| --- | --- | ---: |
| 共用冒烟 | 各臂一次；检查实际模型与隔离、原生角色入口和取证能力，不计入通过样本。 | 2 |
| PBI-80 · 首稿与纠偏 | G1、G2、D1、R1 各三对；每个试次先发 Master 角色命令，再发固定题面。G1 的六次纠偏在原进程续轮。 | 24 |
| PBI-81 · 四角色入口 | Master 的三对固定共享 PBI-80 的 G1 首回合；Developer、Designer、Stakeholder 各新增三对。Stakeholder 的两条同会话复用检查不另启动。 | 18 |
| PBI-82 · 必带原文 | 三对直接调用 `sprint-kernel`，验证加载即有全文；不拿 PBI-81 的角色入口折抵。 | 6 |
| PBI-83 · 真实宿主核验 | 每臂 3 次：开关开启的新会话（启动、未变、变更、再次未变），恢复该会话，开关关闭的新会话。只核验宿主注入，不用这三次替代本机耗时样本。 | 6 |
| 共用技术补测 | PBI-80–82 合用至多两对；每对至多补一次，仅限有记录的非插件技术失败。宿主核验缺证据先停，不自动增跑。 | 最多 4 |

| 预算分组 | 启动／调用上限 | 墙钟上限 | 建议费用上限 |
| --- | --- | ---: | ---: |
| 必需 · 宿主／无头 | 56 次计划启动，含共用冒烟；加技术补测共最多 60 次。 | 180 分钟 | US$5 |
| 必需 · PBI-83 本机重放 | 双夹具各 30 对，共 120 次常态计时；16 次启动准备及暖身、最多 64 次语义／其他状态调用、最多 4 次有记录的技术补测，合计最多 204 次本机调用。无模型请求，不计为宿主启动。 | 20 分钟 | US$0 |
| **本轮规划合计** | **最多 60 次宿主启动，另有最多 204 次本机调用。** | **200 分钟** | **US$5** |
| 可选 · PBI-82 其他材料预载 | 未获放行，不计入本轮；历史候选口径保留供以后另议。 | — | — |

**规划上限与费用口径**：仅按必需项规划：最多 60 次宿主启动、另有本机重放最多 204 次，合计最多 200 分钟、US$5。上限不是报价、支出或跑测授权；可选预载及其试次不纳入 How。冒烟、基线、性能、真实宿主及付费回归均未运行，须另获放行。届时按网关可核对的实际计费口径（含续轮、恢复、重试和单次费用上界）记账，不拿 CLI 估算当账单；无法核实费用、下一试次可能超限、证据不足或已不可能过线，就停并报实况。

**PO 决定（2026-11-20，UTC+8，Master 转达）**：「嗯。嗯，可以放行，我觉得。至于是多少秒不好说啊，主要是我没什么参考，你知道吗，我只知道现在比较慢，我希望你来定一个好不好。」PBI-80–83 的 What 收口，只进入 How 规划；PO 委托 Master 定 PBI-83 性能通过线，定案见上表，不授权施工或实测。决策时的 Sprint Goal 原文：「先读原文再动笔：叫出角色就能调齐该用的内核；定目标、写设计问题或精化条目前，AI 先读并用上对应的原文、约定和模板注释，不用 PO 反复提醒；承诺照常提示，发消息时不再为检查未变的承诺等上几秒。」

## 3. How

<!-- The Developer writes this chapter as a plan for making the selected items, short and not in detail (sprint-log.md, convention 7): the work items in order, each with its output and how to tell it is done; the key choices and why; the risks and open points. The last line is the go-ahead (sprint-log.md, convention 8). -->

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| H1 | 准备共用验证材料 | 合成夹具、固定题面、证据索引和判卷表 | ✓ 2026-11-20 对应 §2.2 的样本、冻结快照和上限；G1 首回合固定共享，四个 PBI 独立判定；不需真实项目资料。 |
| H2 | 对齐四角色入口（PBI-81） | 四个 Claude 角色入口及一致的加载说明 | ✓ 2026-11-20 开场顺序分别为 4／3／3／2；只跳过已成功加载项，不静默跳过失败；DSH 的原生入口与预载行为保持。 |
| H3 | 让 `sprint-kernel` 加载即带原文（PBI-82） | 带出处的 Sprint Backlog／Sprint Goal 原文与一致性检查 | ✓ 2026-11-20 加载正文涵盖 §2.2 指定篇幅，文字、署名和授权可逐字核对；原参考可达，不加可选预载。 |
| H4 | 把必读要求放到 Scrum 的起草入口（PBI-80） | Product Goal、Sprint Goal、精化各自的按需读用指引 | ✓ 2026-11-20 起草前能找到完整原文、相关约定和模板注释；被纠正先回查，指引不把进入下一阶段当作已获批准。 |
| H5 | 把必读要求放到设计起草入口（PBI-80） | 设计挑战／目标／问题的按需读用指引 | ✓ 2026-11-20 入口明确指向该阶段原文、IDEO 模式、约定和模板注释；不把可选访谈或设计推进写成必做。 |
| H6 | 复核承诺 hook 基线（PBI-83，须先获本机实测放行） | 同条件基线记录与瓶颈证据 | ✓ 2026-11-20 分清命令启动与其余开销；若 `00c224b` 不复现旧慢，停在这里报 Master，不改 hook、不改线。 |
| H7 | 降低不变提示的 hook 开销（PBI-83，H6 支持且获准后） | 保持现有注册与语义的优化候选 | 只消除证据指出的重复工作；承诺选择、原文、触发时机、开关和异常退出行为不变，候选留待双层验证。 |
| H8 | 验证首稿与纠偏（PBI-80，实测放行后） | 四类场景与纠偏回合的双证据报告，并留存 G1 首回合的角色调用证据 | 各场景按 §2.2 分判读全和用对，首稿不被续轮覆盖；入口调用证据不替代任何一栏。 |
| H9 | 验证角色入口与载入原文（PBI-81／82，实测放行后） | 四角色顺序和首次加载正文的分项报告 | Master 固定复用 H8 的 G1 首回合；冷启动、复用和必带原文各按 §2.2 判。链接或读文件不冒充加载结果。 |
| H10 | 验证承诺行为与耗时（PBI-83，实测放行后） | 两个夹具的 P50／P95 与脚本层、宿主层分列报告 | 两夹具各自达 §2.2 性能线；两层各自覆盖的承诺语义全过；`clear`、`compact`、`fork` 不报宿主通过。 |
| H11 | 核对完整 DoD 并交审（实测放行后） | 质量证据与 Master 审阅所需差异 | 原文、署名、描述长度、两跳和死链逐条核对，Claude 严格校验与 DSH 既有回归通过；如改 `hooks/`，严格校验后按仓库规矩交 validator。无证据的项不记通过。 |

**Key choices**

- 让角色入口负责实际调用，让阶段入口负责先读再写。优先把指引放在已有入口和导航，不用写入 hook 阻断，也不把全部阶段材料变成常驻上下文。
- 只把 §2.2 要求的 SGEP 原文逐字带入 `sprint-kernel` 的加载正文，以现有 reference 为校对源。显式标出处及授权并检查漂移；不用运行时 shell 拼正文，避免 Claude 与 DSH 看到不同正文。
- PBI-83 先用证据定优化点；不以文件大小或修改时间相同判定承诺未变，不新增用户必装的运行时。保持以当前检出的活动日志路径选取承诺：Sprint 23 设计结束待归档时仍保留该路径，不读 `Now` 过滤。提示只是目标提醒，不证明阶段开放或 PO 放行。

**Risks and open points**

- PBI-80／81 若因为入口或取证能力不一致而无法比较，停报 Master；不加暗示题面、补跑行为失败或动通过线。有关 Sprint 22 角色入口、Sprint 23 日志与模板、Sprint 25 DSH 的重叠接口，留待整合后按影响复核；不依赖 Sprint 26 Memory。
- 计费或宿主事件不可核实就不启动付费运行，不能以本机结果代替宿主。H6 的基线复测也需单独放行；若安排在测试阶段，回施工仍须获准。只列必需测试的规划上限，可选预载不实施、不测。分发方式不变时不新增实机重装专项。

Go-ahead: 2026-11-20（UTC+8），PO SeaPawn（由 Master 转达）： 「你觉得没什么问题了对吧？你觉得没什么问题就放行吧，24。」Master 已审 `9deb68d` §3，无必改项；仅放行 H1–H5 施工与本期分支内的交审检查点。H6 基线实测、H7 hook 优化、H8–H11 正式 Test、冒烟、可选预载、支出、合并、推送、打 tag 和发布均不在此次放行内。放行时 Sprint Goal 原文：「先读原文再动笔：叫出角色就能调齐该用的内核；定目标、写设计问题或精化条目前，AI 先读并用上对应的原文、约定和模板注释，不用 PO 反复提醒；承诺照常提示，发消息时不再为检查未变的承诺等上几秒。」

## 4. Increment notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (sprint-log.md, conventions 9 and 20). A session that picks up the Sprint reads these first. The chapter ends with the Product Owner's decision that the Increment can go into testing (sprint-log.md, convention 24). -->

**书面委托（2026-11-20，UTC+8；PO SeaPawn，由 Master 转达）**：「现在他们全部都开跑了，这样子我跟你讲。嗯，每一个对话，我现在给你权限，每一个对话，等到他们 review 之前向我报告就可以了。不意是每一个对话哦。因为他们现在都已经开始跑了。」Master 代 PO 处理 Sprint 21–25 各自在 Review 前的阶段门与常规事项，决定逐项记入各期日志，责任仍归 PO。本期的 Product Goal、取消 Sprint、推翻 PO 既定决定、PO 点名的品味、正式 Review／Retro／收官、推送发布以及 `CLAUDE.md` 的直接授权仍归 PO。此委托不改变 [§1.1 的 Sprint Goal](#11-sprint-goal)，不等于放行下一个工作项：继续已放行的 H1–H5；H6 的本机基线口径、H7 启动条件及正式 Test 的快照、判据、隔离与费用上界须另交 Master 核准，在此之前不实测、不冒烟、不支出；不做可选预载。

**H1–H5 施工与交审检查点（2026-11-20，UTC+8；分支 `claude/sprint-24-loading-reliability-012ded`，工作树 `sprint-24-loading-reliability-012ded`）**

- **核对与改动边界**：开工前已按 [§1.1 承诺表](#11-sprint-goal) 原文核对目标并在 §3 Go-ahead 补录放行人、原话与仅限 H1–H5 的边界；全部改动都在本期工作树内，主检出 `S:\IDEO-Scrum` 与 `plugins/ideo-scrum/hooks/*`、`dsh/*`、`package.json` 均未改动。
- **H1（共用验证材料）**：新增 [试次索引](validation/trial-index.md)、[独立判卷表](validation/scorecard.md) 与 `validation/fixtures/{g1,g2,r1}/` 四份夹具。夹具从 `00c224b` 的产品与冲刺模板仅填 §2.2 指定字段；题面、试次对号、B/C 交替顺序、G1 `/entry` 固定共享与上限（计划 56 次、最多 60 次宿主启动；最多 204 次本机调用；200 分钟；US$5）与 §2.2 一致，均标明未运行。
- **H2（四角色入口，PBI-81）**：修改 `plugins/ideo-scrum/commands/{scrum-master,developer,designer,stakeholder}.md` 开场指令，仅限 Claude Code 入口逐个调用 `4 / 3 / 3 / 2` 个内核（前一个成功后再调下一个、仅跳过本会话已成功的 Skill 调用、缺调或失败即停并报告，不以读文件或看到描述代替），保留 frontmatter `description`、`# Identity`、`# Code of Conduct` 与 SGEP 正文不变，并显式指向 DSH 适配器自身的预载与路由。同步更新 `plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 8 条、`docs/glossary.md`、`docs/quick-start.md`、`docs/quick-start.zh-CN.md`、`README.md` 与 `README.zh-CN.md`。
- **H3（`sprint-kernel` 加载带入原文，PBI-82）**：在 `plugins/ideo-scrum/skills/sprint-kernel/SKILL.md` 末尾逐字嵌入 [scrum-artifact-sprint-backlog.md](../../plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-sprint-backlog.md) 的 `## Sprint Backlog` 至文末（含 `### Commitment: Sprint Goal`），附 `> Source:`、`> License:` 与本地参考链接；不额外预载其他阶段文件（F14）。同步更新 `ATTRIBUTION.md` 第 2 节并在 `scripts/check_dsh.mjs` 增加正文一致性、局部出处／参考链接及 `ATTRIBUTION.md` 登记检查。
- **H4–H5（起草前必读与运用指引，PBI-80）**：补齐 `plugins/ideo-scrum/skills/scrum-kernel/SKILL.md`（Product Goal）、`plugins/ideo-scrum/skills/sprint-kernel/SKILL.md`（Sprint Goal 与条目精化）与 `plugins/ideo-scrum/skills/design-kernel/SKILL.md`（Empathize 的挑战／设计目标／设计问题）按需必读清单、方法运用要求及在对话中给首稿的约束；明确未读全先停、PO 指出偏差先回查原文再重拟、起草不等于批准目标或进入下一阶段；保持 *Ask the Experts* 访谈／研究按需执行（约定 7）。
- **静态核对与对抗审阅结果（均在最后一次改动后复核；未跑任何宿主或性能实测）**：
  - `claude plugin validate --strict plugins/ideo-scrum`、`node --test scripts/check_dsh.mjs`、`python -X utf8 -I scripts/check_docs.py` 及 `--selftest`、`npm pack --dry-run --json --ignore-scripts` 均于提交前复跑通过（具体结果见本节后文或提交说明前核对；不替代运行时证据）。
  - 四个技能与四个命令 `description` 字符数均 ≤ 1024（`ideo-kernel` 1023、`design-kernel` 1007、`scrum-kernel` 968、`sprint-kernel` 943）；plugin、Sprint 24 与 `ATTRIBUTION.md` 内链全部可达；各 `SKILL.md` 到参考材料均 ≤ 2 跳（`design-kernel/steps/2-3-pick-a-target.md` 经 `conventions/design-log.md` 两跳可达）。
  - 内部 Haiku Workflow 五维审阅 + 对抗复核后已修正：`commands/*.md` 去掉无所指的 `above`、`scrum-kernel/SKILL.md` 补齐「起草不等于定目标或推进」、去掉会命中 H1 的 `#sprint-backlog` 锚点、`check_dsh.mjs` 补齐链接位置与 `ATTRIBUTION.md` 断言、`README*` 补充 Claude Code 顺序说明与 DSH 界定。`sprint-kernel`/`design-kernel` 的 `description` 保留 `00c224b` 原文，待 H9 冷启动实测若出现犹豫再另议，不在无触发实测下改动。
- **当前状态与后续待审条件（均未运行、未支出、未请求 PO 测试放行）**：
  - 当前增量尚未完整（H6–H11 全部未标记完成，§5 无测试记录），仅提交本地检查点供 Master 对照 `00c224b` 审阅 H1–H5。
  - **H6（PBI-83 本机基线）待审前提**：须 Master 先核准 `L1`/`L2` 夹具生成、同机同隔离环境与 `00c224b` 的单调钟重放计时口径（`SessionStart` + 3 次暖身 + 30 对常态样本，另报启动与变更耗时）；若 `00c224b` 不复现旧慢，立即停报 Master。
  - **H7（hook 优化）待审前提**：仅在 H6 实测确认存在且可归因的重复开销后才申请施工；保持现有 `hooks.json` 注册、承诺选择、原文、触发时机、开关与异常退出行为不变。
  - **H8–H11（正式 Test）待审前提**：须 Master 另行核准两臂冻结快照、按 [headless-testing.md](../documents/headless-testing.md) 的隔离配置、实际模型与路由核对、网关可核对计费口径、仓外日志位置，以及共用冒烟（2 次）+ 计划 56 次（上限 60 次）宿主启动／204 次本机调用／200 分钟／US$5 上限；`clear`/`compact`/`fork` 仅记脚本层，不报宿主通过；不实施不测可选预载；不改分发方式时不另开实机重装专项。
  - **并行接口提示**：`commands/*.md`（Sprint 22）、日志与模板边界（Sprint 23）、`README*.md` 与 `docs/quick-start*.md`（Sprint 25）留待整合时按影响复核；本期不依赖 Sprint 26 Memory。

**Master 审阅裁定与 H6 放行（2026-11-20 22:28，UTC+8；依 2026-11-20 PO 书面委托）**：
- **H1–H5 审阅通过（无必改项）**：复核 `c5c6577`（基线 `00c224b`）22 个文件与干净工作树、4 份夹具、`claude plugin validate --strict`、`check_dsh.mjs`（7/7）、`check_docs.py`（107 链 0 错 / `--selftest` 17/17）、`npm pack --dry-run`、29/29 内链、84/84 ≤2 跳、`description` ≤1024 及 `hooks/*`／`dsh/*`／`package.json` 零改动通过；`sprint-kernel`/`design-kernel` 的 `description` 暂留 `00c224b` 原状待 H9 观察。
- **仅放行 H6（PBI-83 本机基线复核，US$0、零模型请求、零宿主启动）**：仓外独立临时目录构造 `L1`（G2+R1）与 `L2`（`L1` 产品日志末加 200 行固定无关备注）并记 SHA-256；以 `hooks.json` 同等方式在当前 Windows Git Bash 单调钟重放 `00c224b` 的 `commitments.sh`（独立状态与会话 ID；每夹具 `SessionStart` + 3 暖身 + 30 常态未变 `UserPromptSubmit`，另单列 `startup` 与承诺变更耗时）；在仓外副本定量拆解命令启动开销与脚本内部开销（不改动工作树且不混入基线样本）。若不复现旧慢停报 Master；若复现且可归因，同样停在 H6 交审并附 H7 拟议方案。
- **仍未放行**：H7（未获 Master 核准前不动 `plugins/ideo-scrum/hooks/*`）、H8–H11（不跑 `claude-magpie`、冒烟、无头测试、真实宿主或付费调用）、可选预载、改通过线、合并、打 tag、推送、正式 Review 与越级向 PO 请示。

**H6 本机基线复核与瓶颈拆解（2026-11-20，UTC+8；US$0、零模型请求、零宿主启动）**

- **仓外证据位置（不改仓库内夹具及 `hooks/*`／`dsh/*`／`package.json`）**：`S:\IDEO-Scrum-Archives\sprint-24-loading-reliability\h6-baseline\`（报告 `h6-summary.md`、原始计时 `raw/h6_baseline_and_profile.json`、生成与重放脚本 `scripts/generate_fixtures.py` 与 `scripts/run_h6.py`）。
- **冻结基线与 L1／L2 SHA-256（供 H10 复用）**：
  - `00c224b` `commitments.sh`（6965 B，184 行 LF）：`7ce9cff1a67c7e33370f8090564b605fe2aac5cfddf84edc5f5c75aed6776b57`；`hooks.json`：`33e60cb5c8ea1944e2edeb3f0c68c90784b5d0f0072c8e8800c16731852c171b`。
  - `L1`（G2+R1）：`ProductBacklog.md`（1934 B，63 行）`a48caf49562d2d0878c4d64c426a81a6b649fb7a6e9e2d5a858a4e2f066d5aaa`；`SprintBacklog.md`（3375 B，55 行）`966c423c9bc1e8551cf60420faff1c5cf37e17cce5ebed0226ed669d7ab6f9d6`。
  - `L2`（`L1` 产品日志末尾追加 200 行固定 `- Appendix note 001..200: unrelated static log padding line for PBI-83 L2 baseline replay.`）：`ProductBacklog.md`（19134 B，263 行）`f3202f678fe52c0e14fa68f34f2822c91a47990127b53ced0921ea5f06de529d`；`SprintBacklog.md` 同 `L1`。
- **环境元信息（已脱敏，未打印环境变量值）**：Windows 10 Pro（10.0.19045，64-bit）；Git `2.56.0.windows.4`；`E:\GIT\Git\usr\bin\sh.exe`（GNU bash `5.3.15(2)-release`, `x86_64-pc-cygwin`）；`GNU Awk 5.4.1`、`GNU sed 4.9`、`coreutils 8.32`（`tr`/`cksum`/`cat`）；Python `3.13.15`（`perf_counter_ns`）。隔离沙箱与 `CLAUDE_PLUGIN_DATA` 位于 `C:`（NTFS NVMe SSD），仓外归档与夹具源位于 `S:`（NTFS USB SSD），Git 二进制位于 `E:`（SATA HDD）。
- **基线重放结果（`sh -c 'sh "${CLAUDE_PLUGIN_ROOT}/hooks/commitments.sh"; exit 0'`；`C:` 沙箱，每组独立目录与会话）**：
  - **`L1`**：`startup = 4653.57 ms`；3 暖身 `[3327.05, 3532.44, 5646.49] ms`；30 次常态未变 `UserPromptSubmit` **`P50 = 2874.29 ms`、`P95 = 9682.46 ms`**（min `2516.23`、max `10997.68`、mean `3408.16`）；`change`（`续借`→`展期`）`2732.82 ms`、变更后静默 `3017.72 ms`。
  - **`L2`**：`startup = 2884.80 ms`；3 暖身 `[2750.84, 3313.37, 2923.44] ms`；30 次常态未变 `UserPromptSubmit` **`P50 = 3241.42 ms`、`P95 = 8531.39 ms`**（min `2461.08`、max `9159.85`、mean `3718.07`）；`change` `2835.35 ms`、变更后静默 `3051.61 ms`。
  - 全部试次 `exit 0`、输出与预期完全一致；**明确复现旧慢**，常态 P50 约 2.87–3.24 s，且出现 8.5–11.0 s 尾延迟逼近或超过 10 s 超时线。
- **定量瓶颈拆解（仓外 `$EPOCHREALTIME` 零 fork 插桩，12 样本，未混入上表）**：
  - **外部壳启动**：与 `hooks.json` 相同的双层壳空脚本 `sh -c 'sh empty.sh; exit 0'` 仅 **`P50 = 169.79 ms`（`P95 = 345.31 ms`）**，占 `L1_root` 总耗时（`2606.91 ms`）约 **6.4%**（`167.71 ms`）。
  - **脚本内部开销占 `93.6%`（`L1_root` `2439.20 ms`；`L2_root` `2725.69 ms`；嵌套 3 层 `L1_depth3` `3033.09 ms`）**：根因是每次常态 `UserPromptSubmit` 在 Cygwin/Git Bash 下顺序 fork+exec **20 个（depth3 为 23 个）外部短进程**，单次 fork 约 70–120 ms，高频 fork 还放大数秒级长尾：
    - `cat | tr`（`165.68 ms`）+ `3× sed`（`442.78 ms`）= **5 次 fork / `608.46 ms`（23.3%）**
    - `find_root`（`tr` + 逐级 `dirname`）：depth 0 为 `196.45 ms`（1 fork）；depth 3 为 **`481.19 ms`（4 forks）**
    - `ProductBacklog` 解析（`tr` + `awk` + `3× field awk`）：**5 forks / `716.26 ms`（27.5%）**
    - `SprintBacklog` 解析（`tr` + `awk` + `field awk` + `dirname` + `basename`）：**5 forks / `531.52 ms`（20.4%）**；而纯 shell `for` 扫目录仅 **`1.40 ms`（0.1%）**
    - 状态处理（`mkdir` `69.54 ms` + `cksum | awk` `184.93 ms` + `cat $state` `121.93 ms`）：**4 forks / `376.40 ms`（14.4%）**
  - 辅助对照：`S:` USB SSD（`n=10`）P50 `3118.98 ms`，与 `C:` 同量级；`startup` 遇 >200 `.fp` 修剪额外 `+695 ms`（`3084 -> 3779 ms`）。
- **H7 拟议优化方案（停在 H6 待 Master 核准；未改任何 `hooks/*`）**：
  - 保持 `hooks.json` 注册、承诺选择、中英文原文、触发时机、`IDEO_SCRUM_COMMITMENTS=off` 与静默 `exit 0` 不变；不引入新必需运行时；**不以文件大小或 `mtime` 判未变**，每轮仍实读日志正文并逐字比对最新承诺输出。
  - **主选方案 A（把脚本内部 20–28 次外部 fork 减至 1 次，预计常态降至 P50 ~260 ms / P95 ~450–550 ms）**：① 用 POSIX `sh` 内建 `while IFS= read -r` 与参数展开取代 `cat`/`tr`/`3× sed`；② 用纯 `sh` 参数展开取代 `find_root` 与 `dirname`/`basename`；③ 将产品／冲刺／设计日志的 `\r` 剥离、表格提取、占位过滤与文本拼装合并为**单次**标准 POSIX `awk`（`FNR == 1` 分文件，兼容 `gawk`/`mawk`/`dash`，保留全部正则与 `\|`、`{{...}}` 语义）；④ `[ -d "$state_dir" ] || mkdir -p` 跳过已存在目录，用纯 `sh` 内建读写 `$state` 并直接逐字比对 `$out`（去掉 `cksum`/`awk`/`cat`）。**备选 B**：若后续同日实测单次 `awk` 仍近 1 s，则改用纯 `sh` 读行解析做到脚本内部 0 fork。**停点重申**：仅留下本记录检查点，不改 `hooks/*`、不写 §5 正式测试、不进 H7–H11。

## 5. Test

<!-- Record here the Developer's tests, the reviewer's check (by default the Scrum Master), the Product Owner's end-to-end test, and the result of each Definition of Done item and acceptance criterion. Fix a problem on the spot and test again (sprint-log.md, convention 16). The chapter ends with the Product Owner's decision: close, or go back (sprint-log.md, convention 24). -->
