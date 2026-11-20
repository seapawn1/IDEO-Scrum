# Sprint Backlog · Sprint 24（加载可靠性）

> Started: 2026-11-19 | 达成 Sprint Goal 或 PO 停止时收官 | Branch: `claude/sprint-24-loading-reliability-012ded` | Product Owner: SeaPawn | Scrum Master: IDEO-Scrum Master | Developer: Sprint 24 Developer
> Now: What，PBI-80–83 的精化草案待 Master 逐项复审。PO 已确认 Sprint Goal 与本期 DoD 核验重点，并放行 What。
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

**PBI-80（Master 提议的验收口径；下列样本与门槛由 Developer 草拟，待 Master 复审）**：以上表用户故事为 POV。我们怎样让 AI 在交首稿前读全当前阶段指定的原文、约定和模板注释，并在草稿里用对，不等 PO 追问？PO 指出不合方法时，先回查对应依据再重拟。

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

**Developer 初估仍为 M（3–5 个会话）**：包括四类样本、纠偏与可审证据；扩大宿主或场景覆盖再估。§2.1 的原文不变。未选实现、未启动测试，What 未结束。

**PBI-81（Developer 草案，待 Master 复审）**：以上表用户故事为 POV。我们怎样让四种角色一进门就调齐对应内核，不等 PO 补一句？按 F07，Claude Code 角色入口的承诺是**实际调用**，不是把正文放进上下文就算调用。下表省略 `ideo-scrum:` 前缀。

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

**PBI-82（Developer 草案，待 Master 复审）**：以上表用户故事为 POV。我们怎样让 Planning 一调入 `sprint-kernel` 就能看到需要的原文，而不把其他阶段的材料一股脑带进来？F15 已定前一项；F14 把其他预载范围留给实测，不把全量常驻、拷贝或索引定为做法。

| 证据 | 样本与建议通过线（未运行） |
| --- | --- |
| 加载即包含 | 三对新会话，复用 PBI-80 的隔离环境与两份快照，固定输入「请用 Skill 加载 `ideo-scrum:sprint-kernel`，先到这里。」只看首次成功加载时实际给同一会话的正文，不看后来读到的资料或模型背诵。候选 3/3 都须包含[现行产物原文](../../plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-sprint-backlog.md)从 `## Sprint Backlog` 到文末的完整段落（含 `Commitment: Sprint Goal`），对应溯源和授权可核对。除换行格式外逐字校对；摘要、链接、残页、随后才读到均不通过。在正文有变化的同一提交里，重新对照该原文防止漂移。 |
| 与 PBI-80 分开 | 本条只证明来源内容在加载时已经可用；不替代起草前指定材料读全、草稿使用正确的双证据。原文保留、导航和署名按产品 DoD 核对；DSH 既有回归另验，若触及分发另验真实安装和入口。 |
| 可选预载取舍 | 先以只满足必带原文的候选作对照。只有 PBI-80 在特定场景还漏了资料，且现有证据指向入口内容不足，才提一个可选材料集，让 Master 确定后同题做三对冷会话对照。建议至少多一个先读与用对双通过的样本、两栏均不倒退，且首次携带可选材料的模型请求，相比对照臂同一位置的请求，新增总输入不超过 1,000 tokens（计入缓存读写，候选线，未定）；无改善、证据不足或超线都不增加预载。不得给试题加阅读提示，也不强求预载来弥补草稿判定不合。 |
| 试次与停止 | 必带原文的三对单独冷启动，不借角色入场的加载结果；可选对照另列在本节末的跨 PBI 总表。实际载入正文取不到时停报证据不足；读到了错误或不完整的正文是行为失败，不补跑。 |

**Developer 初估 S（1–2 个会话）**，限已确定的必带原文与判据；可选预载另看证据和预算，不先承诺扩大。

**PBI-83（Developer 草案，待 Master 复审）**：以上表用户故事为 POV。我们怎样让常态发消息少等，同时保证该提示时仍得到承诺原文？已确定的是语义不变。F04 的 2.1–2.4 秒是旧测，不代替 `00c224b` 同条件实测；300 ms 是旧建议，不是 PO 门槛。

| 语义样本 | 两份快照须分别得到的结果 |
| --- | --- |
| 会话起点 | `SessionStart` 的 startup、resume、clear、compact 各带入一次当前承诺原文；固定宿主若支持 fork，则同样核对。用角色日志中的精确文本预先立期望，不用模型复述或单看退出码。 |
| 常态及内容变化 | 使用 G2 的合成产品日志和含 R1 目标的单冲刺日志。新会话启动后，连续两条普通消息均不重复注入；只改备注也不注入；把「续借」改成同字节长的「展期」后（另覆测相同修改时间），会话下一条消息注入更新后的全文，再下一条无新注入。不同会话不共用上次状态；无历史状态时仍可取得当前承诺。 |
| 日志与开关边界 | 用中英承诺表各跑；单一 Sprint／设计时带正确目标和名称；多个同类时仅报数量，不误挑一个目标；模板占位不入上下文；缺产品日志或无有效产品承诺时静默；不可读的次级日志不抹掉已确认的 Product 和 Product Goal。`IDEO_SCRUM_COMMITMENTS=off` 时两类事件都不注入、不阻断消息；恢复正常配置的新次序恢复原行为。 |
| 证据与通过线 | 按[现行承诺约定](../../plugins/ideo-scrum/skills/scrum-kernel/overview.md)与 [hook 注册](../../plugins/ideo-scrum/hooks/hooks.json)重放合成事件，逐条核对输出原文、静默、退出结果和更新次序。全部样本须正确；宿主另验启动、未变、变更、恢复与关闭，使用原生 hook 事件和 debug 日志中的上下文交付记录，不用脚本 stdout 或模型复述代替。DSH 的承诺由宿主运行时段另行回归，不套用 Claude hook 的计时。 |

| 耗时口径 | Developer 建议（未运行，与语义证据分开） |
| --- | --- |
| 环境、基线、样本 | 同一台 Windows、同一 Claude/Git Bash 版本及同类磁盘，`00c224b` 对候选。固定两种日志夹具：G2 产品日志加一份已填 Sprint Goal；第二种在同一夹具产品日志末尾添加 200 行固定无关备注。每臂用独立临时目录与会话状态，先做 `SessionStart`、再暖身三条；每夹具采 30 对普通不变提示，交替臂顺序。用单调钟量事件触发时承诺处理的等待，含命令启动，不算模型生成、网络或交互时间。主要在本机重放，宿主 `hook_started`／`hook_response` ID 配对只作边界核对；不能用不同计时范围或不同缓存状态相减。另报告 startup 和内容变化耗时，不混进常态样本。 |
| 性能通过线（待 PO 定） | 各夹具分别报 P50、P95 和有效样本数。**Developer 新建议，尚非 PO 定案**：常态候选 P50 比同日基线至少低 50%，P95 不高于同日基线且不超过 1 秒；两种夹具各自过线，承诺语义全过。掉提示或吞错误不算变快。F04 的 300 ms 是旧建议，不列入本候选线；若同日基线不复现旧问题，先报告差异，由 Master 交 PO 判断是否仍值得改，不临时改线凑过。 |
| 失败与停止 | 维持现有 10 秒超时判定；超时不当作短耗时，也不剔掉归因于插件的失败。事件无法配对、时钟或环境不可比、样本不足或语义失败即停，不给出优化通过。宿主和本机额度分列在下方总表；本机重放不发模型请求。 |

**Developer 初估 M（3–5 个会话）**，含当前瓶颈复测与不改变承诺行为的验证。

**跨 PBI 试次分配与总预算（Developer 建议，待复审及 PO 授权；未运行）**：一对为基线与候选各一试次。启动数按进程计，恢复同一会话也计一次；同进程续轮不新增启动，但其时间与费用计入总额。共享样本按预定编号复用原始记录，各 PBI 独立判定，不挑试次或重复计费。

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
| **必需合计** | **最多 60 次宿主启动，另有上行 204 次本机调用。** | **200 分钟** | **US$5** |
| 可选 · PBI-82 可选预载 | 仅在必需证据确实指向特定缺口时，另审一个材料集：三对新的冷会话，最多再补一对技术失败；不复用版本或条件不同的试次。 | 30 分钟 | US$1 |
| **含可选的总上限** | **最多 68 次宿主启动；本机额度不增加。** | **230 分钟** | **US$6** |

**放行与费用口径**：以上金额只是建议上限，不是报价或已批预算。Master 复审后，须由 PO 明确拍板 PBI-83 性能门槛、正式预算和网关实际费用口径（含续轮、恢复、重试及可核对的单次费用上界），并明确放行测试阶段、宿主核验和付费运行；冒烟也算在内。CLI 估算不当账单；没有可核对的费用上界、下一试次可能超限、证据不足或已不可能过线，就停并报实况。可选项另等 PO 放行，不因必需项有余额就开跑。未选实现、未运行测试，What 未收口，How 未放行。

## 3. How

<!-- The Developer writes this chapter as a plan for making the selected items, short and not in detail (sprint-log.md, convention 7): the work items in order, each with its output and how to tell it is done; the key choices and why; the risks and open points. The last line is the go-ahead (sprint-log.md, convention 8). -->

| # | Work item | Output | Done when |
| --- | --- | --- | --- |

**Key choices**

**Risks and open points**

Go-ahead: <date, who gave it, and how far it reaches — for example: commit on the Sprint branch; merge, tag, and release decided at Review; no push>

## 4. Increment notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (sprint-log.md, conventions 9 and 20). A session that picks up the Sprint reads these first. The chapter ends with the Product Owner's decision that the Increment can go into testing (sprint-log.md, convention 24). -->

## 5. Test

<!-- Record here the Developer's tests, the reviewer's check (by default the Scrum Master), the Product Owner's end-to-end test, and the result of each Definition of Done item and acceptance criterion. Fix a problem on the spot and test again (sprint-log.md, convention 16). The chapter ends with the Product Owner's decision: close, or go back (sprint-log.md, convention 24). -->
