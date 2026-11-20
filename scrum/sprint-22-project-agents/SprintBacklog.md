# Sprint Backlog — Sprint 22 (project-agents)

> Started: 2026-11-19 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `claude/sprint-22-project-agents-b09bf1` | Product Owner: SeaPawn | Scrum Master: 项目 Scrum Master | Developer: Sprint 22 Developer
> Now: Increment；H3–H6 已施工并按 Master 审阅意见修订（`b88a79b`），H7 修订版方案在 §4 待冻结；未获放行前不跑 H7、不进 Review／合并／推送。
> Waiting for PO: None
> How to write this log: [Sprint log conventions](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md).

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 独立的第二视角：拍板前能请参谋复核方案，也能按本项目的角色卡听取 Stakeholder 的反馈；身份不用每次重讲，意见每次独立，决定仍由 PO 来做。 |
| --- | --- |

这一步服务于[产品化](../ProductBacklog.md#12-product-goal)：让用户不用借作者的项目配置，也能在自己的项目里拿到独立反馈、继续走流程。

### 1.2 Definition of Done

完整产品 DoD 继续生效，重点核验角色职责与方法依据是否写准、用户能否从产品日志找到对应的角色定义，以及 Claude 插件校验和 DSH 现有回归是否通过。DSH 回归通过，不等于已经支持项目 Agent；这项能力仍待实查。

完整标准与校验命令见[产品日志 §1.3](../ProductBacklog.md#13-definition-of-done)。以上是核验标准，不是测试结果。

**PO 决定（2026-11-19，Master 转达）：**「按这版定」确认本期 DoD 核验重点和 Sprint Goal「独立的第二视角：拍板前能请参谋复核方案，也能按本项目的角色卡听取 Stakeholder 的反馈；身份不用每次重讲，意见每次独立，决定仍由 PO 来做。」；另以「两期同时放行」明确放行 Sprint 22 进入 What，不含 How、施工或测试，不以 Sprint 21 的进度为前提。

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-73 | 参谋：独立提供第二意见的 Agent | 作为用插件干活的 solo 开发者，我想要在拍板、选方案、评审设计时叫一个只读的子代理独立看一眼，以便拿到第二判断，而不是自己再想一遍 | Map ②、设计冲刺收敛 | S～M |
| PBI-75 | 各项目按角色卡注册 Stakeholder Agent | 作为项目 PO，我想把常用 Stakeholder 角色配置成本项目可复用的 Agent，以便子代理或 Workflow 按名召唤独立反馈 | Map ③、设计测试、⑧ | 待估 |

### 2.2 Refinement

沿用 §2.1 的用户故事，先精化 PBI-73，再精化 PBI-75，两项分别验收。以下是 Master 在 2026-11-19 提出的验收场景及 Developer 的复述和暂估；两项精化已定案，未做实测。

**PBI-73：参谋**

来源：[产品日志 §3.1](../ProductBacklog.md#31-当前的-pbi) 中 PBI-73 所列个人原型 `advisor-synthesis.md`（§1、§8–9）和 Master 首轮提议。原型的脚本、双模型投票、费用线、固定回话模板和当时「不做插件」的限制不自动沿用；原型不等于插件已有能力。

复述：在拍板、选方案或评审设计时，给参谋一个待决定的问题、约束及点名材料的原文。参谋独立回答「怎么看，为什么」，理由能对照原件；只读，不改产物，不替 PO 决定。

| 验收场景 | 过线行为 |
| --- | --- |
| 材料足以纠正一个前提 | 指出哪个前提需改、哪处原文支持纠正，以及为何影响判断。 |
| 原方案有充分依据 | 可以赞同，独立说明理由，不为展示差异强造反对意见。 |
| 缺少关键材料 | 指出缺什么、为何会改变判断；可以请求补充，不编造依据或强下结论。 |

**取证口径：** 分别从不带旧评议的新上下文考察三个场景，核对交给参谋的材料、理由与原件、调用记录及被评议产物前后状态。不以意见是否不同于主会话作为过线依据。

**模型选择，PO 定案（2026-11-19，Master 转达）：**「默认 Fable，可另选」。

| 情形 | 要核验的行为 |
| --- | --- |
| 未指定其他模型 | 默认选 Fable。 |
| 项目明确另选可用模型 | 遵从该选择。 |
| 所选模型不可用 | 如实提示，可另选或取消，不静默换模型。 |

这个决定只约束参谋，不约束普通 Stakeholder、Developer 或现有会话。配置入口与模型名解析留给 How；不把固定版本 ID 或个人网关映射当成通用规则。[Claude Code 文档](https://code.claude.com/docs/en/sub-agents#choose-a-model) 说明宿主限制可能替换请求的模型。

**模型取证口径：** 用可归属到该次调用的可信宿主或提供方执行记录核对实际模型，不能仅凭请求的别名或模型自报。网关映射无法核实，记「实际模型未验证」；确认被替换，则不能把该回答计为指定模型的成功。不得为取证更改用户模型、网关或权限，不限定某个专有日志字段。

**Developer 暂估：S～M，偏 M。** 除三个意见场景，还有三种模型选择行为；若调研证明既有做法可同时满足只读、独立与模型选择，才向 S 调整。保留 PO 要求的调研：实际设计前用适用的 IDEO 方法考察已有做法，结论交三方，再定具体 How。这次文档审阅和后续功能测试都不能代替该调研。

**PBI-75：项目 Stakeholder**

来源：[产品日志 §2.1](../ProductBacklog.md#21-stakeholders) 的角色卡、§3.1 的 PBI-75、[现行 Stakeholder 命令](../../plugins/ideo-scrum/commands/stakeholder.md#code-of-conduct) 和 Master 首轮提议。

复述：用一张已确认的角色卡（例如「陌生人」）核对。项目 Stakeholder 按卡片立场给外部反馈，每个项目只登记自己的角色。可复用的是角色定义，不是旧评议；即使共用技术手段，也不把 Stakeholder 反馈当成参谋的第二判断。

Master 转达 PO 原话：「开子代理的时候，开工作流的时候就可以直接复用」。

**双入口验收门槛，PO 委托，Master 决定（2026-11-19）：** PO 原话「你来决定吧，我不太清楚呢」，只委托本条门槛。在支持 Workflow 的 Claude Code 环境里，普通子代理和 Workflow 两个入口必须各自按名调用同一份仅在本项目注册的 Stakeholder 角色成功，并分别留证：实际使用了该项目角色定义，评议从新上下文开始、不带旧评议。不以意见不同为通过条件，也不能从一个入口成功推断另一个成功。只注册一份；未启用 Workflow 的项目仍可独立使用普通子代理。环境无 Workflow 时，该入口记为「未验证」，不记「已通过」。不扩到 DSH。

| 验收场景 | 过线行为 |
| --- | --- |
| 接受配置 | 角色卡确认后展示可选配置；接受后，核对仅在本项目登记一份，且该项目产品日志 §2.1 指到对应角色；双入口各按上述门槛举证。 |
| 拒绝配置 | 对照项目文件及引用，核对不写文件、不造引用；仍能临时按角色卡请全新子代理给外部反馈。 |
| 角色卡变更或已有同名配置 | 留存展示的差异；核对未批准时原文件和引用不变，批准才更新，不静默覆盖。 |
| 角色职责与召唤权 | 核对不同身份仍按各自角色卡发言；常驻 PO 助手不冒称独立审阅者。Sprint Review 的外部视角仍由 PO 或 Scrum Master 召唤，建造者不召唤。 |

**双入口取证口径：** 可用来源、作用域记录或独立对照，分别证明两个入口命中同一份本项目角色定义且使用新评议上下文；只有同名调用或相似输出不够，不强求某个宿主专有字段。任一入口缺证据就标「未验证」，双入口项不能算通过。

**Developer 暂估：M（3–5 个会话）。** [Claude Code 文档](https://code.claude.com/docs/en/sub-agents#choose-the-subagent-scope) 支持项目作用域说明，也说明同名角色存在优先级。按名调用是否成功仍须分别实测，不能用全局配置兜底。

只核对 Claude Code 的项目作用域；不做通用 Claude Code Setup、MCP 或全局配置。DSH 的项目 Agent 等价能力待查，不在本期承诺内。

**Developer 核对（2026-11-19）：** 两项精化均已核对：PBI-73 的只读第二意见与 PBI-75 的项目角色复用分别服务 §1.1，验收场景和取证口径齐备。PBI-75 两个入口均未实测，记「未验证」。PBI-73 的 IDEO 调研是方案设计的前置工作：先用适用方法调研已有做法，把结论交 PO、Master 与 Developer，再确定具体 How。

**Master 审阅（2026-11-19，基于 `a5a7595`）：** PBI-73、75 的验收场景和取证口径均无必改项。判据审阅通过不是功能验收通过。

**PO 决定（2026-11-19，Master 转达）：**「定案并放行 What」。对照 §1.1 的 Sprint Goal「独立的第二视角：拍板前能请参谋复核方案，也能按本项目的角色卡听取 Stakeholder 的反馈；身份不用每次重讲，意见每次独立，决定仍由 PO 来做。」Master 据此记录 PBI-73、75 的 What 精化结束，转入 How 规划；How 方案尚未获批，施工及实测未放行。

## 3. How

**Developer 提案（2026-11-20，按 Master 初审意见修订，已复审）。** 依据 §4 的设计前调研和 §2.2 的已定判据。以下均为放行后的工作，不代表已经施工或通过测试；每块控制在一个会话内。

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| H1 | 对齐新增组件、项目登记与取证接口 | 新增 agent、登记说明及用户说明的大纲；§2.2 各场景的验证计划 | ✓ 2026-11-20 Master 看过大纲、涉及文件及与 Sprint 23／24／25 的交接面；判据、环境、费用和样本预算在实测前冻结，获准后另作提交。 |
| H2 | 尽早核验宿主能否提供关键证据（须另获实测授权） | 隔离项目的模型执行记录、最小角色定义的生效条件、Agent 与 Workflow 各自的证据 | 按下方两处停点分别判断相关实现能否继续。任一项未达到判据，带证据停在该线并报 Master，不改用户设置、不自行降标。 |
| H3 | 交付 PBI-73 专用只读参谋 | 插件 agent、手动调用入口、模型选择与不可用时的反馈 | 新组件全文经审阅后落插件；明确请求才召唤，默认 Fable、明确另选、不可用三种路径符合 §2.2；只读与新上下文有工具及调用证据。 |
| H4 | 交付 PBI-75 首次登记与拒绝路径 | Claude Code 侧可选登记入口、项目角色文件和产品日志引用 | 以用户项目已确认的角色卡为准，完整预览后接受才成对写入项目定义及 §2.1 引用；拒绝不写，临时召唤照常。只在隔离项目验证，不拿作者家目录当用户项目。 |
| H5 | 补齐角色更新、冲突和双入口复用 | 差异确认、同名检查及按名召唤说明 | 未批准时原文件与引用不变；批准才更新；同名遮蔽不被当成项目定义命中。一份定义供两个入口使用，保留角色职责和 Review 召唤权，建造者不因注册而取得召唤权。 |
| H6 | 对齐用户可用的入口与文档 | Claude Code 侧的调用、登记说明和文档导航 | 新行为有来源或标为作者设计；不改共用约定、已批准 Identity 和原文。用户从产品日志能找到对应角色；无 Workflow 仍可普通召唤，DSH 不被写成已支持项目 Agent。 |
| H7 | 正式 Test 放行后核验功能与完整 DoD，交 Master 审阅 | 逐项证据表、未验证项与完整增量 | §2.2 的参谋正反例、模型选择及项目登记四组场景分别有结果；Claude 严格校验、文档链接、description 长度及 DSH 既有回归合格。结构变化按仓库规则另派 Haiku validator；缺证据不判通过。 |

**Key choices**

- **参谋用插件专用 agent，由手动入口调用。** 新增只在用户明确请求第二意见时使用的 [Claude Code 手动入口](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill)；它准备问题、约束与点名原件，调非 fork、非续接的新实例，不传旧评议或主会话倾向。用宿主的工具限制保证只读，不靠角色提示自律，不启用评议记忆；保留既有内核加载边界，不增加写入或再委派能力。无需新服务或全局配置。
- **默认值与实际执行分开。** 插件定义请求 Fable；PO 明确另选时，优先用本次调用的模型参数，不自动保存设置。[宿主可覆盖模型](https://code.claude.com/docs/en/sub-agents#choose-a-model)，因此按 H2 的模型停点处理，既不承诺能锁住宿主回退，也不把请求值当执行证据。
- **Stakeholder 的一份定义只属于用户项目。** Claude Code 侧的可选登记动作衔接现有 Stakeholder 与产品日志；角色卡定后，展示[项目作用域](https://code.claude.com/docs/en/sub-agents#choose-the-subagent-scope)的角色文件与 §2.1 相对引用。不改 DSH 共用的 Stakeholder 命令正文。角色定义保存已确认的卡片内容和角色边界，承接现行守则、内核入口和 Review 召唤权；不依赖卡片固定列数，不固化留白、不带旧评议，也不把常驻 PO 助手转成独立审阅者。
- **登记和引用作为一项变更确认。** 展示两处目标和完整差异；宿主写权限不代替用户确认。写前核对项目边界、同名来源和当前内容是否仍是预览版本；遇同名遮蔽不静默覆盖。若半途失败，报告未完成、恢复一致性，不覆盖并行出现的用户改动；不修改其他作用域来消除重名。
- **先查关键可行性，再补全内容。** H2 只做最小能力核验，须另获 PO 明确实测授权；即使施工获准也不自动包含 H2。H7 的正式验收须等 PO 放行 Test。既有 `claude-magpie` 隔离回归可验行为，固定模型映射不能证明默认 Fable。取证不改用户模型、网关、权限或遥测；不改分发则只跑既有 DSH 回归、不重复验安装。

**Risks and open points**

| H2 停点与其他风险 | 处理方式 |
| --- | --- |
| PBI-73：指定模型不可用、被替换或无法证实 | 区分三态：①有可归属到本次调用的可信记录证实指定模型，才把意见作为该模型的结果交付；②确知不可用或被替换，明确告知，由用户另选或取消，不交替代意见；③证据不足，记「实际模型未验证」，不把意见当成指定模型结果。若宿主不能识别替换或证实实际模型，留存已有证据与缺口，停在 PBI-73 线，报 Master／PO；不进入 H3，不计通过，不自行降标。 |
| PBI-75：项目定义不生效，或有入口无法举证 | 在隔离项目用同一份最小项目角色定义，记录宿主何时、怎样使新登记定义生效，再分别取普通 Agent 和 Workflow 按名命中该定义、从新上下文开始评议的证据。可用来源／作用域记录或独立对照；仅同名或相似输出不够。任一入口缺证据，含宿主无 Workflow，记「未验证」，带证据停在 PBI-75 线并报 Master／PO；不进入 H4／H5，不用复制提示词或全局配置代替。 |
| 严格只读与内核加载的工具需求冲突 | H1 明确工具和加载边界；H2 验实际工具面，尤其写入、Shell、再委派和评议记忆。若需要扩大权限，先报 Master，不以提示词声称受限。 |
| 项目卡片、文件和引用漂移，或不同作用域存在同名定义 | 角色卡为身份依据；展示差异和实际命中来源。用户文件冲突不自动覆盖、不扫改全局；拒绝仍保留临时召唤。 |
| 23／24 改共用约定和角色入口，25 改文档与版本 | Master 对齐接口后再改重叠段；本期只追加项目角色能力，不承担内核加载修正、两版改号或发布。 |

**Master 复审（2026-11-20，基于 `8de87d1`）：** 两处 H2 停点及分线边界已补齐，How 计划通过复审。此为 Master 对计划的结论，不是 PO 放行或实测通过；由 Master 按并行安排报 PO。

**施工 Go-ahead（2026-11-20，Master 转达 PO 原话）：**「放行22吧。他的 how 我大概看了一眼。反正你觉得可以就可以的，放行吧。」对照放行时 §1.1 的 Sprint Goal「独立的第二视角：拍板前能请参谋复核方案，也能按本项目的角色卡听取 Stakeholder 的反馈；身份不用每次重讲，意见每次独立，决定仍由 PO 来做。」PO 放行 How → Increment，以 Master 对 How 的复审为依据；这不是全权授予。按计划先做 H1、在本分支作本地检查点；H2 最小宿主实测与 H7 正式 Test 仍须 PO 分别明确放行，H3–H6 不跳过相关 H2 停点。不含更改验收线、合并、tag、推送或发布。

## 4. Increment notes

**2026-11-20（UTC+8）· PBI-73 设计前调研。** 仍在 How 规划。用 [Assume a beginner's mindset](../../plugins/ideo-scrum/skills/ideo-kernel/methods/assume-beginners-mindset.md) 和 [What? How? Why?](../../plugins/ideo-scrum/skills/ideo-kernel/methods/what-how-why.md)，把个人原型的实际决定、宿主文档和推论分开。调研工作笔记为 `sprint-22-advisor-research.md`（PBI-73）；复核要点及来源列在下方。私有原件保留原处，不复制入库。

| 发现 | 对 How 的影响 |
| --- | --- |
| 个人原型最后选的是手动召唤的只读 Explore 子代理；因未满足真实决策试用条件，收口但未验收。`86c7f6b` 只登记了 PBI。 | 保留手动召唤、点名原件和只给意见的体验，不把旧脚本、双模型或本机网关选择当作产品规格。 |
| [原生 advisor](https://code.claude.com/docs/en/advisor) 由 Claude 决定何时咨询，读取整段对话；[内置 Explore](https://code.claude.com/docs/en/sub-agents#built-in-subagents) 的默认模型受主会话和宿主影响。 | 建议优先考虑专用只读子代理：每次新上下文、只带点名原件，实际模型须有对应调用的可信记录。普通上下文隔离不等于完全没有项目规则，也不靠模型不同来证明独立。 |
| [宿主可能替换子代理模型](https://code.claude.com/docs/en/sub-agents#when-an-allowlist-blocks-a-subagent-model)，网关映射也可能不可核实。 | 「默认 Fable，可另选」不变；需区分请求、宿主替换和实际执行，证据不足记「实际模型未验证」，不以改模型、权限或网关取证。 |

**复核出处：** 个人原型的最后决定和未验收原因见《Sprint Backlog — advisor-workspace》§2.2 的 PBI-058「advisor（已收口，未验收）」；早期候选与模型归属缺口见《advisor（参谋）构思综合》（`advisor-synthesis.md`）§1–2、§5、§8–9。宿主证据的含义见 [Agent 执行结果](https://code.claude.com/docs/en/agent-sdk/python#agent)及[子代理完成事件](https://code.claude.com/docs/en/monitoring-usage#subagent-completed-event)，仅供理解起始模型与最终执行模型的区别，并不指定取证字段或要求开启遥测。

调研时的检查点：结论交三方，之后由 Developer 提具体 How 给 Master／PO 审阅。调研未定封装、未写 Agent、未跑功能测试；PBI-75 的普通子代理与 Workflow 入口仍「未验证」。

**2026-11-20 · How 提案交审。** Master 转达 PO 已明确同意 What 进入 How Planning，研究可先做；常规实现路径由 Developer 提，不另设「起草 How」批准门。本次把 §4 研究结论落实为 §3 的提案，待 Master 审阅；不代表方案已批准。仅改本期日志，未实现 Agent、未生成用户项目配置、未做功能实测，亦不提交、合并、推送或发布。

**2026-11-20 · H1 接口、大纲与取证方案（交 Master 审阅）。** 依据 §2.2、§3 及[六期分工](../documents/sprint-roadmap.md)；下列文件名和接口是实现提案，不是已安装能力。H1 只交大纲及取证计划，不写组件全文、不生成项目配置。

| 工作项 | 拟动文件／接口 | 输入、输出与边界 |
| --- | --- | --- |
| H3 · 参谋 | `plugins/ideo-scrum/agents/advisor.md`；`plugins/ideo-scrum/claude-skills/second-opinion/SKILL.md` | `/ideo-scrum:second-opinion` 由用户手动发起，入口只把待决定的问题、约束和点名原件交给新的 `ideo-scrum:advisor` 普通子代理，不转发主对话或旧答案。Agent 默认请求 `fable`；另选只用宿主本次调用支持的别名，不改主会话或持久设置。入口核对同次实际调用，按 §3 三态交付或停住。 |
| H3／H5 · 角色与工具 | 子代理启动次序、参谋的只读白名单 | 按[现行 Stakeholder 入口](../../plugins/ideo-scrum/commands/stakeholder.md)和[角色约定](../../plugins/ideo-scrum/skills/scrum-kernel/overview.md#who-does-what)实际调用 IDEO → Scrum，Sprint／Design 内核按任务所涉加载；预载或读文件不算调用。两种评议均不带持久评议记忆。参谋不是第五个 Scrum 角色，拟只留 `Read` 与必要的 `Skill`，不授予写入、Shell、MCP、转派或会话通信；H2 核对加载内核前后工具没扩大。项目登记不额外授予权限，不改外部反馈职责。参谋入口禁止模型自动调用，Agent 描述也只允许显式请求；不能用描述或入口设置代替触发验证。 |
| H4–H5 · 项目 Stakeholder | `plugins/ideo-scrum/claude-skills/project-stakeholder/SKILL.md`；用户项目的 `.claude/agents/<角色名>.md` 与产品日志 §2.1 | 从实际产品日志取得 PO 已确认的角色卡（不依赖固定列／行方向），只保存卡上身份及现行外部反馈边界，保留其留白。先展示定义和相对引用的完整差异；核对同一项目根、路径实际归属、名称来源及预览版本，明确同意后才成对写入。拒绝不写；变更或重名不静默覆盖，无法安全恢复部分写入时报告具体不一致。Agent 和 Workflow 各按宿主专有入口按名取同一份定义，不注入替代提示或旧评议。Review 的召唤权和常驻 PO 助手的边界照旧。 |
| H6 · Claude Code 独有装载 | `plugins/ideo-scrum/.claude-plugin/plugin.json` 的 `skills` 路径项 | [清单文档](https://code.claude.com/docs/en/plugins/manifest-reference#how-each-key-combines-with-its-default-location)说明该项是追加，不替代现有 `skills/`。两项入口放在 DSH bundle 的既有文件范围之外；不改共用命令、内核、DSH 适配器或打包清单，不新增钩子、后台服务或权限配置。 |

| 待写全文 | 拟定章节（各只放一种信息） |
| --- | --- |
| 参谋 Agent | **何时介入**：明确的第二意见请求；**输入与判断**：原件、约束和缺料时怎么回；**交付边界**：依据、不代决定、不写回。 |
| 手动参谋入口 | **请求与材料**：组织题面，不改写原件；**召唤与模型**：新实例、默认、另选；**返回**：仅可信的同次执行证据足够才按指定模型交付。 |
| 项目登记入口 | **选卡与同名核对**：本项目卡片和作用域；**预览与确认**：两处变更一起批准，支持拒绝；**更新与恢复**：并发改动、失败报告；**复用**：双入口共用定义、不同上下文。 |
| `docs/project-agents.md` 与 `docs/project-agents.zh-CN.md`（提案） | **选参谋还是 Stakeholder**：两种用途，PO 拍板；**请参谋**：题面、模型选择、模型未验证的处理；**登记和维护角色**：接受／拒绝／更新及从产品日志定位；**按名复用**：Agent、Workflow 与临时召唤，附实际验证的生效条件；**宿主边界**：无 Workflow 的项目仍可普通召唤，DSH 不作支持声明。中英快速上手各加一条导航，由 Sprint 25 先交共用段落，Master 对齐后再接。 |

**并行交接。** Sprint 23 提供产品／冲刺日志的共用规则，本期只消费已确认角色卡与产品日志 §2.1，不改模板、阶段门、收尾；Sprint 24 先交角色入口实际加载顺序，本期按审过的接口承接，不改四角色的 Identity、内核或承诺 hook；Sprint 25 先交分发／文档与版本接口，本期只交 Claude Code 专用清单路径项和用法导航，不改版本或 DSH 能力口径。三条交接都由 Master 核对实际基线再动重叠处。

**H2 最小宿主取证提案（两线分别判；先审阅、冻结并提交，后由 PO 另行放行）。** 以 Windows 上同一 Claude Code 版本为基线，PBI-73 用能观察同次模型执行的获准通道，PBI-75 用启用 Workflow 的隔离交互会话，不以无 Workflow 的无头环境替代。按[无头回归手册](../documents/headless-testing.md)的隔离与超时原则：在仓外空目录建测试家目录与合成 Git 项目，仅夹具内写最小定义，会话从环境白名单启动。只用合成数据，不读取作者家目录、配置或真实材料，不改用户模型、网关、权限或遥测。开跑前记录宿主版本、运行方式、Workflow 可用性与证据通道；原始记录留仓外，只回填可分享的结果、范围和缺口。`claude-magpie` 固定映射只供行为复验，不证明实际 Fable；前置不具备就停在相应线。

| 待核 | 最小样本与要留的证据 | 停点 |
| --- | --- | --- |
| PBI-73 · 指定模型可否核实、替换可否识别且参谋仍只读 | 同一最小插件定义、同一合成题面，最多三格各一次：无覆盖默认、显式另选、已获准通道中原本就不可用／会替换的对照。不改策略造负例。用同一调用的发起、可归属的实际执行与完成记录核对请求及实际模型（有切换要看完整记录），确认返回入口能据此不交替代意见；同时核对调用确为新实例，读取／内核加载前后实际工具面无写入及再委派，并对照夹具文件前后。 | 已证实才交指定模型结果；已知不可用／替换则告知另选或取消；缺模型或替换证据、缺对照环境、实际工具不受限均记缺口，停在 H2，不进 H3。不以起始别名、模型自报或没出现告警作证。 |
| PBI-75 · 一份项目角色何时生效，两个入口能否各自证明 | 一个隔离项目、一份唯一的合成角色。先核登记前、登记后原会话和新会话的宿主加载状态，记录实际生效条件；生效后用同一角色定义，普通具名 Agent、Workflow 各一次新评议。优先留各入口命中来源、作用域或加载内容与该文件的一致性，并核独立启动及实际上下文不含预置旧评议；来源不透明时可各补一次唯一定义在／不在的独立对照，角色识别信息不进题面。 | 入口缺证（含宿主无 Workflow）记「未验证」；若任一入口没证实按名命中这份定义及新上下文，停在 H2，不进 H4／H5。不从另一入口外推，不复制角色提示或改全局兜底。 |

**拟冻结预算。** PBI-73 至多 3 个宿主调用样本、US$1.50；PBI-75 至多 4 个（两入口各一正例、必要时各一对照）、US$0.50。总计最多 7 个样本、US$2.00、一次会话内最多 20 分钟；每样本最多 180 秒，加载状态预查优先用不请求模型的宿主记录。成本含父／子请求、缓存、思考及重试；开跑前按通道现行费率、上下文和请求上限核算并确认可守住两线及总额；无法限制自动重试或预估费用时不启动，不超额补跑。超时按手册终止整棵测试进程树，保留技术失败和已发生费用，不替换为成功样本。任一线证据缺口独立报 Master，不降低 §2.2 通过线。

**H7 正式 Test 对照。** 另获 Test 放行后，按 §2.2 的三个参谋意见场景逐个比对输入、原件、理由与文件状态，并分别核验默认／另选／不可用及非显式请求没有误召唤；项目线逐项比对接受、拒绝、更新／同名冲突与角色职责，实际跑双入口并记录各自归属和新上下文。先冻结正式样本、预算与通过线再跑；完整 DoD 及仓库校验另列证据，不用 H2 的最小夹具代替。此处只做 H1 交审，H2–H7 未启动，§5 不填测试结果。

**2026-11-20 · Master 审阅 H1（基于 `8b5dc33`）。** 接口、全文大纲及最小取证方案通过审阅；已核对 Claude Code 清单的追加 `skills` 行为和本仓库 DSH 文件白名单。沿提案新增 Claude 专用入口，不动共用内核、DSH 打包或版本。此为 H1 方案审阅结论，不是 H2 实测授权或功能通过。

**H2 取证补充要求（Master 审阅意见）。** PBI-73 必须分开留证：一是事后能复核同次调用的实际执行模型；二是返回入口在交付意见前确实取得同次可信证据，能识别替换／证据不足并按 §3 三态处理。第一项不能代替第二项，事后补查不能算入口已阻止替代意见交付。沿同次调用核对证据与交付先后，不为此改用户配置或开启遥测。隔离 Workflow、实际模型证据、只读工具验真或费用上界任一前置不具备，停对应线并报 Master。

Master 将请 PO 单独放行隔离 H2：合计最多 7 个样本、20 分钟、US$2.00；PBI-73 的 3 样本／US$1.50 与 PBI-75 的 4 样本／US$0.50 分线限额不变。须同时具备 PO 明确放行与测法／通过线的独立本地提交才开始，当前两项均未具备；不跑冒烟、宿主或付费实测，不跳到 H3–H7。H2 不替代 H7 正式验收。

**2026-11-20 · PO 授权 Sprint 22 施工中间决定（Master 转达）。**「呃，我告诉你这种。之间的就不需要我来放行了，这种之间的就你来决定就可以了。然后等他到 test 之前。向我报告就行。」仅限本期已获准施工内的 H2 最小取证、按线判断推进 H3–H6、分支本地检查点，由 Master 决定并记账。到正式 H7 Test 前停下，由 Master 报 PO，Test 仍由 PO 明确放行；不改变 Sprint Goal、PO 已定决定或验收线，不合并、tag、推送、发布或改用户配置。

**2026-11-20 · Master 放行 H2，测法与通过线冻结。** 在上述授权内，只准按下表做隔离最小宿主取证；本段先独立本地提交，才复核开跑条件及执行。H2 结果回 Master 按线决定能否推进；本次不进 H3–H7。原 §2.2 不改，§5 仍留空。

**开跑条件。** 使用同一 Windows Claude Code 构建，PBI-73 须有获准且可核实际执行的通道，PBI-75 须有可隔离的 Workflow 交互入口。只用仓外测试家目录、合成项目／定义和环境白名单；执行范围须可验证地限制在合成夹具内，不继承作者文件、会话、凭据映射、通信或额外工具。先核对宿主版本、入口、隔离和可信记录可见性，以及可执行的费用、请求上界；不读或改用户模型、网关、权限、遥测来凑条件。事后才拿得到实际模型不算参谋入口可用。条件缺一，不发起对应样本，记「未验证」并留可分享的依据；不把本机通用入口或固定模型映射当隔离能力证据。

| 线／样本 | 测法与留证 | 通过线／停点 |
| --- | --- | --- |
| PBI-73 · 73-A 默认、73-B 显式另选、73-C 不可用或替换对照，各至多一次 | 在同一最小插件定义与合成题面上，用手动入口起新、普通、非续接的参谋。73-A 不设调用覆盖；73-B 用通道上可核的明确另选别名；73-C 只用获准环境中原有的不可用或替换行为，不改策略构造。按同次调用串起请求、实际执行及入口接收到的记录、入口交付先后；另记实际子代理工具范围和内核加载前后、夹具文件前后、不含旧评议的派单。区分可供事后审查的记录与入口当次能用的证据。 | 73-A 可信记录证实实际 Fable，73-B 证实另选，73-C 能识别不可用／替换，明确告知、不交替代意见；无可信执行证据时明确「实际模型未验证」且不交指定模型意见。入口须能在交付前据同次记录作出上述判断，且实际只读、无再委派、起新上下文。若对照环境或任一证据缺失，停在 H2；不进 H3，不以事后日志、起始别名或自报替代。 |
| PBI-75 · 75-A Agent、75-W Workflow，各一次；来源不透明时各一次独立对照 | 在同一个隔离项目只登记一份唯一合成角色定义，比较写前、写后原会话及新会话加载状态，记录生效条件。生效后从普通具名 Agent 和 Workflow 分别按名启动新评议；用宿主来源／作用域或定义内容核对同一份文件，核对新启动及实收上下文无预置旧评议。需要独立对照时只改变该定义是否存在，角色区分信息不进入两入口的题面。 | 普通 Agent 与 Workflow 须分别证实按名命中这份定义且新上下文，两入口都举证才过；相同名称、相似回答或一条仅有角色标记都不能替代。任一入口无证（含无隔离 Workflow）记「未验证」，不进 H4／H5，不复制角色提示或用全局配置兜底。 |

**预算及停止。** PBI-73 至多 3 样本／US$1.50，PBI-75 至多 4 样本／US$0.50，总计 7 样本／20 分钟／US$2.00；单样本最长 180 秒，以先到的上限为准。冒烟与补跑占样本，父／子所有请求、缓存、自动重试及超时已发请求计入费用；启动前必须核算可执行的上界，超时终止整棵测试进程树，不能用超时或客户端估算上限当账单上界。保留实际次数、费用、逐线证据与缺口，只在仓内记可分享的汇总。不加跑、不挪用另一线预算，不用无损失假设放行；H2 不替代正式 Test。

**2026-11-20 · H2 开跑核对（冻结基准 `5ef57d9`）。** 只核对本机入口是否安装、仓内回归脚本和公开宿主文档，未启动测试宿主或读取个人配置。原生 CLI 与现有回归入口都存在，但安装不等于隔离、取证和预算条件成立。

| 线 | 实际样本／费用 | 核对结果与停点 |
| --- | --- | --- |
| PBI-73 | 0／US$0.00 | [回归手册](../documents/headless-testing.md)的固定便宜映射不能证实实际 Fable。[Agent 完成结果](https://code.claude.com/docs/en/agent-sdk/python#agent)文档可说明起始模型与中途切换记录的含义，却不能证明本期允许的运行路径下，手动入口在交付前能读到同次实际执行证据。没有核实到同时满足上述取证、只读工具范围、不可用／替换对照和费用上界的获准隔离通道。73-A／B／C 均未启动，实际模型、交付前识别和只读能力未验证；不进 H3。 |
| PBI-75 | 0／US$0.00 | 现有[陌生人回归驱动](../../scripts/stranger_test/driver.py)第 101–129 行仅隔离部分目录，提供方配置仍指向作者环境；[守卫](../../scripts/stranger_test/guard.py)第 53–59 行读取配置／输入失败时放行，不能作为本次隔离保证。[CLI 费用参数](https://code.claude.com/docs/en/cli-reference#cli-flags)仅适用 print 模式且可超出估算上限；[Workflow 会自动重试](https://code.claude.com/docs/en/workflows#when-an-agent-stalls-and-restarts)。没有核实到同一隔离项目内启用 Workflow、可核全部请求 US$0.50 上界的获准交互会话；既不在当前会话借跑，也不先跑普通入口作替代。两入口及生效条件均未验证；不进 H4／H5。 |

合计 **0 个样本、0 次模型调用、US$0.00**（H2 单列，含冒烟、父／子、重试，均为零）。这是前置条件未满足，不是实测失败，也不说明所有宿主都不支持。未生成测试夹具或更改用户配置；测法和判据不变。请 Master 复核：如后续有获准且可验证隔离与费用上界的通道，再依原门槛核对；不据此推进 H3–H6，不进 H7。

**2026-11-20（UTC+8）· PO 授权各期正式 Sprint Review 前的阶段决定（Master 转达）。**「现在他们全部都开跑了，这样子我跟你讲。嗯，每一个对话，我现在给你权限，每一个对话，等到他们 review 之前向我报告就可以了。不意是每一个对话哦。因为他们现在都已经开始跑了。」本期由 Master 决定并记录正式 Review 前的阶段放行，含今后 H7 Test 门；替代本章先前「Test 仍由 PO 明确放行」的安排，不是现在放行 Test。Developer 只向 Master 交审和报阻碍，由 Master 在正式 Review 前向 PO 报告。

**保留事项。** 更改 Product Goal 或 Sprint Goal、取消 Sprint、推翻 PO 已定决定、PO 点名要看的品味事项、正式 Sprint Review／Retro／收官及对外发布，均不在此次授权内。不因此获得合并、tag、推送、发布或改用户配置的授权；修改 `CLAUDE.md` 仍须 PO 直接授权修改它的会话。

**H2 只读补查复核（2026-11-20，Master）。** 维持 `e3e5459` 的未启动／未验证停点：PBI-73 仍缺入口交付前可用的同次可信实际模型证据和可验只读的隔离通道；`PostToolUse` 的宿主解析／换模记录不能替不透明网关证明实际执行，不临时新增 hook。PBI-75 仍缺同一隔离项目内的普通 Agent／Workflow 双入口取证条件，以及覆盖交互 Workflow 含重试费用的可核分线上界。默认 Fable、双入口判据及 `5ef57d9` 的安全、取证与预算门槛不变；两条窄版建议暂不实施。有经核符合原门槛的通道才报 Master，不试跑未知环境。仅记授权和补查边界，未新增测试、组件或支出，不进 H3–H7。

**2026-11-20（UTC+8）· PO 更新 PBI-73 模型决定及适用范围（Master 转达）。** 对照 §1.1 的 Sprint Goal「独立的第二视角：拍板前能请参谋复核方案，也能按本项目的角色卡听取 Stakeholder 的反馈；身份不用每次重讲，意见每次独立，决定仍由 PO 来做。」，PO 新决定原话为：「我说实话，22那个随便一个模型就可以。到时候再详细配置，用户回详细配置就行了，他测试的时候随便找个模型测就行，他可以用 Opus 去测也行啊。」

- **覆盖与保留范围：** 本条依据[日志约定第 20 条](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md)调整 Sprint 22 本轮 H2 的开跑与过线门槛：在获准隔离通道上用可用模型先验证参谋核心功能，不把 2026-11-19 的「默认 Fable，可另选」（§2.2）或指定 Opus、入口交付前同次真实型号核验、以及换模／不可用专门对照作为本轮开跑门或功能过线门（同步调整上段复核对 PBI-73 模型的停点要求）。原 §2.2 的「默认 Fable，可另选」及三态表、§4 `5ef57d9` 原冻结段及 `e3e5459` 零样本记录（含「合计 0 个样本、0 次模型调用、US$0.00」与「这是前置条件未满足，不是实测失败」）全部保留不改写；详细模型配置与指定模型／换模取证另留后续，本轮不声称某精确型号已测试、不伪装用户所选、不静默改变配置。不为用 Opus 多花费、不改作者设置、不加型号验证 hook。§3 H3／H7 中「默认 Fable、明确另选、不可用」措辞是随本轮单列收敛对齐，还是留作后续详细配置项，待 Master 核准下述草案时一并裁示。
- **PBI-75 线不动：** §2.2 PBI-75 四个验收场景、双入口门槛、取证口径、M 暂估及 `5ef57d9` 的普通 Agent／Workflow 同一项目定义与 4 样本／US$0.50 预算不变；两线不互等。

**2026-11-20（UTC+8）· PBI-73 H2 修订草案（待 Master 核准，尚未冻结／未开跑）。** 沿 `5ef57d9` 在第 4 章追加 H2 预检口径（不改 §2.2，不填 §5，不替代 H7 正式 Test；未获 Master 核准并独立作本地检查点提交前，不发起任何样本）。

| 样本（共 <= 3 个） | 测法、触发与旧意见隔离设计（零隐藏探针） | 通过线与实际工具面核验 |
| --- | --- | --- |
| 73-A（纠正前提）· 73-B（独立赞同）· 73-C（缺少材料） | 在仓外最小测试插件定义（仅含临时 `advisor` 与手动 `second-opinion`，不动 `plugins/ideo-scrum/`）及隔离合成 Git 夹具上，每样本起一个独立隔离会话（`--input-format stream-json`）：**第 1 轮**只作普通决策讨论并由父会话提出带标记的偏颇旧意见（`OLD-OPINION-...`），不请求第二意见、不点名入口；**第 2 轮**显式调用 `/ideo-scrum:second-opinion`，只传待决问题、约束与点名合成材料路径，不转第 1 轮旧意见，召唤新、非 fork、非续接的 `advisor` 实例。3 个样本分别对应 §2.2 三种意见场景；每样本的父会话双轮、子代理调用、缓存及重试全部计入本线预算，不再另跑第 4 次「非自动触发探针」。 | ① 明确手动召唤与非自动触发：3 个样本第 1 轮调用／事件追踪均无 `second-opinion` 或 `advisor` 自动召唤（不单独拿静态 `disable-model-invocation` 代替运行时触发验证），第 2 轮均显式命中；② 全新上下文与无旧意见泄漏：子代理为新普通实例（非 fork／续接），实收派单与上下文不含第 1 轮 `OLD-OPINION-...`；③ 实际只读且不转派：照 §3 H1 与[回归手册](../documents/headless-testing.md)，子代理加载内核（`ideo-kernel` → `scrum-kernel`，按需 `sprint-kernel`／`design-kernel`）前后工具面均含 `Read` 与 `Skill`，且**不含** `Write`、`Edit`、`NotebookEdit`、`Bash`、`PowerShell`、`Agent`、`Workflow`、`SendMessage`、`WebFetch`、`WebSearch` 及 `mcp__*`（不强制限定全集仅 `{Read, Skill}`），运行时零写入／Shell／再委派／通信调用，且夹具文件前后 SHA-256 与 mtime 一致；④ 三个场景均按 §2.2 给出可对照原件的独立意见，不代决定、不写回、不编造缺料依据。 |

- **隔离基线与待 Master 核准的通道／上界选项：** 按[无头回归手册](../documents/headless-testing.md)第 10、34 条：同一 Windows Claude Code 构建；仓外全新 `USERPROFILE`／`HOME`／`APPDATA`／`LOCALAPPDATA`／`TEMP`／`TMP`／`CLAUDE_CONFIG_DIR`；项目置于无任何上级 `CLAUDE.md`／`AGENTS.md`／`.claude/rules` 的位置（如 `C:\Users\Public\...`）并 `git init`；开跑前每个会话用 `/context all` 确认指令文件为 0；白名单环境变量、`--setting-sources project,local`、`--strict-mcp-config`、`--tools`／`--disallowedTools`；180 秒超时终止整棵进程树；保留 3 样本／US$1.50／单样本 180 秒／总量 20 分钟边界不扩。现有两条可行路径供 Master 选定其一并核准其上界条件（不把 `PostToolUse` 新增 hook 列为候选）：
  1. **通道 1（非作者隔离 API 凭据 + Console 工作区限额 + `-p` / `stream-json`）：** 完整凭据隔离且响应含真实 `model`／`usage`；但 CLI `--max-budget-usd` 仅适用 print 模式且按客户端估算可超出（`e3e5459` 已记），不能单独算可执行账单上界，须由 Master／PO 提供非作者专用 `ANTHROPIC_API_KEY` 并在对应 Console 工作区确认可设 `<= US$1.50` 限额（目前未具备）。
  2. **通道 2（本机 `claude-magpie` 硬化隔离行为通道）：** 按手册第 6、10 条即时可用且为便宜模型（汇总记「magpie 的便宜模型，非 Haiku」），在新 PO 决定下不再因「固定映射不能证 Fable」而被否；**必须由 Master 明确核准的两项边界：**（a）`claude-magpie` 经由作者本机 `magpie` 网关／凭据路由（不共用作者设置／会话／项目文件，并可另加故障即拒的本地路径守卫而不沿用遇错放行的 `scripts/stranger_test/guard.py`），属于**网关配置归作者环境、执行范围隔离**，非非作者独立 API 账号；（b）网关不透明，无服务端硬性 US$1.50 计费上界，只能以客户端 `--max-budget-usd`（估算）配合单样本 180 秒树杀与只读工具白名单兜底。
  未获 Master 明确选定上述通道与预算接受口径、并作独立检查点固定前，PBI-73 H2 仍维持 **0 样本／US$0.00**，不启动、不进 H3–H7。

**2026-11-20（UTC+8）· Master 核准 PBI-73 H2 修订、通道 2 口径与实施细化冻结（仅启动 PBI-73 H2）。** 对照 §1.1 的 Sprint Goal「独立的第二视角：拍板前能请参谋复核方案，也能按本项目的角色卡听取 Stakeholder 的反馈；身份不用每次重讲，意见每次独立，决定仍由 PO 来做。」依据[日志约定第 20 条](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md)，Master 复核 PBI-75 仓外夹具与计费核对通过并维持停点（0 样本／US$0.00），同时核准仅启动 PBI-73 H2 并冻结以下条款（先只暂存并独立提交本文件作冻结检查点，再进行零调用预检与样本执行）：

1. **选定通道 2（本机 `claude-magpie` 硬化隔离行为通道）及接受边界（仅用于 PBI-73 H2）：**
   - 网关／凭据经本机 `magpie`（[无头回归手册](../documents/headless-testing.md)第 6 条既定便宜模型测试入口），属执行范围严格硬化隔离：仓外全新 `USERPROFILE`／`HOME`／`APPDATA`／`LOCALAPPDATA`／`TEMP`／`TMP`／`CLAUDE_CONFIG_DIR`，零写入作者 `~/.claude`，上级无指令文件目录（`C:\Users\Public\...`）并 `git init`，每会话开跑前以 `/context all` 确认指令文件为 0，白名单环境变量、`--setting-sources project,local`、`--strict-mcp-config`、故障即拒本地路径守卫，绝不访问作者配置、记忆或仓库；
   - 不声称服务端硬账单上限，不声称验证了 Fable／Opus 等具体型号（汇总统一标「magpie 的便宜模型，非 Haiku」，不写模型名、网关地址或提供方）；以客户端 `--max-budget-usd`（总计 `<= US$1.50`）＋单样本 180 秒 `taskkill /T /F` 整棵进程树终止＋总计 `<= 20` 分钟＋严格最多 3 样本兜底。
2. **开跑前补齐并冻结的三项实施细化：**
   - **父会话 vs 子代理工具面分开：** 父会话保留 `Read,Grep,Glob,Skill,Agent`（同时禁 `Write,Edit,NotebookEdit,Bash,PowerShell,Workflow,SendMessage,WebFetch,WebSearch` 与 MCP）以在第 2 轮召唤 `advisor`；`advisor` 子代理本身由仓外临时代理定义强制只读与不转派（加载内核前后均含 `Read` 与 `Skill`，不含 `Write`/`Edit`/`NotebookEdit`/`Bash`/`PowerShell`/`Agent`/`Workflow`/`SendMessage`/`WebFetch`/`WebSearch`/`mcp__*`），不以父会话限制代替子代理工具面证据。
   - **故障即拒守卫放入隔离项目 `.claude/settings.local.json`：** 按[无头回归手册](../documents/headless-testing.md)第 36 条，绝不经 CLI `--settings` 传守卫；因启用 `--setting-sources project,local`（屏蔽用户 settings），守卫钩子置于隔离项目的 `.claude/settings.local.json`（不计入合成材料哈希、命令本身不提测试或作者路径），并在零成本预检阶段确认守卫确实被加载且不影响 `/context all` 指令文件为 0。
   - **零额外模型冒烟＋首样本熔断：** `/context all`、守卫脚本本地单测与夹具哈希均为零模型调用预检；真实模型调用严格控制在 `73-A`／`73-B`／`73-C` 至多 3 样本内，不另跑第 4 次模型探针。若 `73-A` 出现隔离串入、守卫失效、工具面越权或无法召唤，立即停机回报 Master，不继续跑 `73-B`／`73-C`。
3. **本轮 H3／H7 单列覆盖口径（保留 §2.2 与 §3 原文不回改）：**
   - 本轮 H3／H7 对 PBI-73 按 PO 2026-11-20 决定执行模型无关的功能交付与验收（手动召唤、非自动触发、全新无旧意见上下文、实际只读不转派、§2.2 三场景独立意见、插件校验与 DSH 回归）；代理定义保留可配置模型接口但不锁死个人网关或固定版本 ID，不加模型验证 hook。
   - 原 §2.2 与 §3 的「默认 Fable、明确另选、不可用」三态实测及用户侧详细模型配置明确留作后续配置项，不在本轮标为已测，也不静默删除，待 Review 时一并向 PO 列明。
4. **阶段边界：** 不动 `plugins/ideo-scrum/`，原始流放仓外，入仓只留脱敏汇总；PBI-75 不动；PBI-73 H2 结果未交 Master 审阅前不进 H3–H7，不改 `CLAUDE.md`，不进 Review／合并／打 tag／推送／发布。

**2026-11-20～21（UTC+8）· PBI-73 H2 样本结果（3/3 跑完，交 Master 审阅）。** 冻结基准 `4709f8f`。零调用预检先行：`/context all` 指令文件 0、`claude doctor` 无无效设置、守卫 15 项本地单测全过（含配置缺失／输入非 JSON／非字典输入的故障即拒）、守卫在隔离项目 `.claude/settings.local.json` 中被实际加载并向每次工具调用执行、预检阶段无任何推理请求。随后按 73-A → 73-B → 73-C 顺序各跑一次，**无补跑、无第 4 个探针**。

| 项 | 实测 |
| --- | --- |
| 宿主 | Claude Code 2.1.329（Windows），仓外临时插件 `6.0.3` 加两个新增组件，`claude plugin validate --strict` 通过 |
| 通道 | 通道 2（本机 `claude-magpie` 硬化隔离行为通道）；模型为 **magpie 的便宜模型，非 Haiku**，本轮不声称任何具体型号 |
| 隔离 | 每样本独立测试家目录与 `CLAUDE_CONFIG_DIR`、白名单环境变量、`--setting-sources project,local`、`--strict-mcp-config`、故障即拒守卫；项目位于无上级指令文件的目录并 `git init` |
| 工具面 | 父会话 `Read,Grep,Glob,Skill,Agent`（`init` 中报作 `Task`），显式禁 `Write,Edit,NotebookEdit,Bash,PowerShell,Workflow,SendMessage,WebFetch,WebSearch` 与 MCP；`advisor` 由定义强制 `Read,Skill` 只读不转派 |
| 样本 | 3／3 完成；单样本最长 141.4 秒；累计实测 415.0 秒；费用（客户端估算）合计 **US$0.9527**，未超 3 样本／US$1.50／180 秒／20 分钟上限 |

| 样本 | 第 1 轮（普通讨论，带偏颇旧意见） | 第 2 轮（显式第二意见） | 首轮熔断项 | 判定 |
| --- | --- | --- | --- | --- |
| 73-A 纠正前提 | 父会话记下「演练与回退都稳妥、周一直接全量切换无风险」 | 派单 `ideo-scrum:advisor` 一次，仅含问题、约束、点名材料；子代理调 `Skill(ideo-kernel)`→`Skill(scrum-kernel)`→`Read`，据原文指出固件断网缺陷与回退路径缺失两个独立阻塞，结论「不能」，并列出须先满足的前提与缺失信息 | 无自动召唤、无续接、无旧意见泄漏、无越权调用、夹具不变 | 符合 §2.2「纠正前提」 |
| 73-B 独立赞同 | 父会话记下「半夜校验多半撞后台同步，至少要改到工作日中午」 | 同上一次派单与同一工具序列；子代理据原文判定方向有支持但「不足以构成充分依据」，逐条列出材料自述、未覆盖项与前提，既不附和旧意见也不无条件赞同 | 同上 | 符合 §2.2「独立赞同／独立判断」 |
| 73-C 缺少材料 | 父会话记下「A 便宜 600 元，直接选 A 最划算」 | 同上一次派单与同一工具序列；子代理判定「不能确定」，指出预算上限与可接受停机天数两项关键输入缺失、A/B 字段不对应，并分层列出还需补齐的馆方与供应商材料 | 同上；另有守卫拒绝 1 次（见下） | 符合 §2.2「缺少材料」 |

**通过线逐条对照：** ① **明确手动召唤、非自动触发**——三样本第 1 轮对 `second-opinion`／`advisor` 的自动调用均为 0，第 2 轮各 1 次显式命中；② **全新上下文、无旧意见**——三次均为新普通实例（非续接／非 fork），派单文本、子代理实收消息、子代理流与落盘子代理记录中旧意见标记均为 0；③ **实际只读且不转派**——子代理实际调用仅 `Skill`、`Skill`、`Read`，禁用集与 `mcp__*` 调用为 0，夹具三文件 SHA-256 与 mtime 前后一致、`git status` 干净；④ **三场景独立意见**——均给出可对照原件的判断、不代决定、不写回、不编造缺料依据。

**如实说明的边界与缺口：**
- **费用**：只有客户端估算，网关不透明、无服务端硬账单上限；本轮以 `--max-budget-usd`、单样本 180 秒整棵进程树终止和总量上限兜底，不能把估算当账单。
- **模型归属**：本轮按 PO 2026-11-20 决定做模型无关的功能验证，未验证任何具体型号，也未验证入口在交付前识别换模／不可用的能力；该项仍属后续详细配置项，不在本轮通过线内。
- **守卫的一次拒绝**：73-C 中父会话有一次 `Glob` 指向自身沙箱配置目录的 `memory/`，被守卫以「工作区外路径」拒绝（退出码 2），模型改用工作区内方式完成任务，结论不受影响。这属守卫按设计拦下工作区外路径，**不是隔离串入**，也不是守卫失效；作者路径、记忆库、本仓库与测试归档目录全程 0 命中。
- **时间口径**：20 分钟按三样本实测运行时间累计（415.0 秒）计，不含两次样本之间开发者侧的间隔；每样本 180 秒与总费用上限未受影响。
- **原始材料**：宿主原始流、调试记录与脚本全部留在仓外的 `S:\IDEO-Scrum-Archives\sprint-22-project-agents\pbi-73-h2\`，本段只记可分享的汇总；`plugins/ideo-scrum/` 未改动，§2.2 与 §5 未改。

**结论（交 Master 按线决定）：** PBI-73 H2 的三项开跑前细化均已落实并有实测证据，四类通过线在 3 个样本内均成立；未发现隔离串入、守卫失效、工具面越权或无法召唤。**据此仅报 Master 审阅；未获审阅结论前不进 H3–H7，PBI-75 维持停点。**

**2026-11-21（UTC+8）· PO 委托（Master 转达，逐字）。**「可以，先审 22、23、25 吧  后面这些，嗯，对话。他们到 review 之前再向我报告。就是后面的事情你都可以决定了，review 之前再向我报告。」对照 §1.1 的 Sprint Goal「独立的第二视角：拍板前能请参谋复核方案，也能按本项目的角色卡听取 Stakeholder 的反馈；身份不用每次重讲，意见每次独立，决定仍由 PO 来做。」本期由 Master 在正式 Review 前决定阶段放行与记账，Developer 只向 Master 交审和报阻碍。**仍回 PO 的事项：** 改 Product Goal／Sprint Goal 承诺、取消 Sprint、推翻 PO 定案、PO 点名品味、改本仓库 `CLAUDE.md`、正式 Review／Retro／收官、合并、tag、推送、发布。本委托不降验收线，不授权越界。

**2026-11-21 · Master 审阅结论：PBI-73 H2 通过。** 已复核 `4709f8f`／`79078de` 及仓外 `S:\IDEO-Scrum-Archives\sprint-22-project-agents\pbi-73-h2\` 的原始流、报告与调试日志：零调用预检清白（指令文件 0、`claude doctor` 正常、守卫在隔离项目 `.claude/settings.local.json` 实际生效）；三样本均符合四类通过线，第 1 轮自动召唤 0、第 2 轮各 1 次显式命中；均为新实例非 fork／非续接，`OLD-OPINION` 零泄漏；子代理实际调用严格为 `Skill(ideo-kernel)`→`Skill(scrum-kernel)`→`Read`，禁集与 MCP 为 0，夹具哈希与 mtime 未变；三场景可对照原件且不代决定；73-C 单次 `Glob` 被守卫拦截属预期拦截、零作者串入；代价 415.0 秒／估算 US$0.9527 在上界内。**顺记一处事实观察（非 PBI-73 阻塞）：** 预检 73-A 有 `commitments.sh` 冷启动 10 秒超时（73-B／73-C 及正式会话正常），留供交接参考。

**2026-11-21 · PBI-75 H2 双入口取证（Master 移交，停点解开）。** 按 PO 2026-11-21 指示，Master 已在其交互会话（Claude Code `2.1.329`，显式 `model: "haiku"`）完成 PBI-75 双入口最小验证；原始证据与汇总归档于仓外 `S:\IDEO-Scrum-Archives\sprint-22-project-agents\pbi-75-h2\`（`summary.json`、`fixture-catalog-reader.md`、`receipt-note.md`、`75-A` 与 `75-W` 原始记录）。

| 核验项 | 实测结果 |
| --- | --- |
| `definition_absent` | `75-A-absent` 与 `75-W-absent` 均报错 `agent type 'fixture-catalog-reader' not found`，零模型调用，未回退通用代理 |
| `definition_present` 的生效条件 | 落盘**同轮内**仍报 `not found`；**同会话下一轮用户消息边界**自动注册生效，无需重启会话 |
| `75-A`（普通具名 Agent） | `Agent(subagent_type="fixture-catalog-reader", model="haiku")`：API `system` 块含定义正文，`tools` 为 `["Read"]`，无 `OLD-REVIEW-N8V2`，拒认采购单 24 册并输出 `CATALOG-ROLE-Q7M4` |
| `75-W`（Workflow） | `Workflow` `wf_6c05a7c3-e7e`，`agentType: 'fixture-catalog-reader'`，脚本未内联角色正文与标记；API `system` 块含定义正文，`tools` 为 `["Read"]`，同样无旧评议、输出角色标记 |
| 夹具完整性 | SHA-256 与 mtime 前后一致 |

- **须写进 H4–H6 文档的两条宿主实测事实：** ① 新建 `.claude/agents/<name>.md` 不在同轮热刷新，而在**同会话下一轮用户消息边界**生效（不必重启会话）；② Workflow 子代理不继承先前对话历史，但宿主会把**触发该 Workflow 的当轮用户原话**作为 `[Workflow harness — user request]` 透传给子代理，因此触发独立评议的当轮提示也不应夹带倾向。
- **须如实保留的边界：** 该次实测在 Master 交互会话中以 `haiku` 路由完成，附带常规会话 `instructions`，非零指令文件的 `CLAUDE_CONFIG_DIR` 沙箱；不宣称特定后端型号或服务端账单硬顶。
- **Sprint 25 H1 交接结论：** `dsh-v0.2.2-rc.5`（`9c2670d`）的 `agent-preset`／`tool-subagent` 不证明按项目自动发现 Agent 文件，DSH 文档边界如实标为未证实、不作项目级 Agent 支持声明。

**2026-11-21 · 放行 H3–H6 施工（不含 H7 正式 Test）。** 依上述 PO 委托，在分支 `claude/sprint-22-project-agents-b09bf1` 上完成 H3 → H4 → H5 → H6 施工及逐文件本地检查点提交：H3 按 `4709f8f` 第 3 条口径写 `agents/advisor.md` 与 `claude-skills/second-opinion/SKILL.md`；H4–H5 写 `claude-skills/project-stakeholder/SKILL.md` 并写入上述两条宿主实测事实；H6 在 `plugin.json` 追加 `skills` 路径，写齐两份 `docs/project-agents*.md`，暂不改 `docs/quick-start*.md`（拟加的 1 行双语导航草案记入下方交接）。**H6 完成后自检并停点交审；未获 Master 审阅 H3–H6 并冻结放行 H7 前，不运行 H7 正式 Test，不进 Review、合并、tag、推送或发布。**

**2026-11-21 · H3–H6 施工结果（交 Master 审阅）。** 四个本地检查点，逐文件提交，未合并、未推送、未打 tag。

| 提交 | 内容 | 要点 |
| --- | --- | --- |
| `a9c3eaa` H3 | `plugins/ideo-scrum/agents/advisor.md`；`plugins/ideo-scrum/claude-skills/second-opinion/SKILL.md` | 参谋 `tools: Read, Skill`、`disallowedTools` 覆盖写入／Shell／再委派／通信／网络／MCP，`model: fable`；入口 `disable-model-invocation: true`，只传问题、约束与点名路径，新普通实例非 fork／续接；三态模型实测如实标为后续配置项，入口不声称已验证具体型号 |
| `dcf2fd2` H4–H5 | `plugins/ideo-scrum/claude-skills/project-stakeholder/SKILL.md` | 从产品日志 §2.1 取卡；先展示两处变更再写入；拒绝不写、同名只报不覆盖、半途失败逐项报告；写入两条宿主实测事实（下一轮用户消息边界生效、Workflow 透传触发当轮原话）；保留 Review 召唤权与常驻 PO 助手边界 |
| `c4f578e` H6 | `plugin.json` 追加 `"skills": ["./claude-skills/"]`；`docs/project-agents.md` 与 `.zh-CN.md`；`scripts/check_docs.py` 的 `PAIRS` | 默认 `skills/` 保留不变（清单该项为追加）；两份文档结构对等并加入配对检查；未改版本号、`dsh/`、`package.json`、`CLAUDE.md`、共用命令／内核／约定 |

**H6 自检（全过）：** `claude plugin validate --strict plugins/ideo-scrum` 通过（识别新增 `ideo-scrum:advisor` 与两个新技能，共 6 个 skills）；`node --test scripts/check_dsh.mjs` 6 项全过（DSH 侧只注册四内核四角色，未受影响）；`python -X utf8 -I scripts/check_docs.py` 无错误（链接 103 条），`--selftest` 17 例全过；新增 description 长度 640／420／580 字符，均 ≤ 1024。

**quick-start 导航草案（交接，本期不改 `docs/quick-start*.md`）。** 英文：`- For a second opinion, or a stakeholder your project keeps: [project agents](project-agents.md).`；中文：`- 需要第二意见，或想留住本项目的 Stakeholder：[项目 Agent](project-agents.zh-CN.md)。` 由 Sprint 25 先交共用段落，Master 对齐后再接。

**2026-11-21 · H4–H6 按 Master 审阅意见修订（`b88a79b`）。** 三处必改均已落实：

| 必改项 | 修订 |
| --- | --- |
| §2.1 不依赖固定列／行方向 | 入口改为按语义定位角色卡：支持角色排在行上或排在列上（本仓库自己的产品日志即转置表：`是谁`／`要什么`／`怎么算满意`／`看得到什么`／`何时召唤`／`负责`／`不负责`）、任意语言与任意字段集；只取卡上实有的事实，不编造缺失项，不把措辞改写掉；相对路径写进该卡对应的「何时召唤」格 |
| 生成定义的最低有效结构与并发／更新核验 | 写明必须合法 YAML frontmatter（`name` 与文件名同为 kebab-case、单行双引号 `description` ≤ 1024 且说明何时召唤）、不给源码写入权限（保留 `commands/stakeholder.md` 的外部反馈与不改源码边界，`Bash` 仅在用户明说时按角色需求授予）、正文按序 `Skill` 加载 ideo → scrum（按需 sprint／design）并写入角色卡原文身份；更新时展示与现有文件及日志引用的 diff，落盘前重读两处确认未被并发修改，变了就停下来展示新差异而不是覆盖 |
| 双语文档 | 修正中文错别字「直到新的一定被接受」→「直到新的定义被接受」；中英均把「那一行／that row」改为「角色卡／role card」，并补上入口命令 `/ideo-scrum:project-stakeholder` 的代码块 |

**H4–H6 修订后自检（全过）：** `claude plugin validate --strict` 通过；`node --test scripts/check_dsh.mjs` 6/6；`python -X utf8 -I scripts/check_docs.py` 无错误（103 链），`--selftest` 17/17；三个新增 description 640／420／**692** 字符，均 ≤ 1024。

**H7 正式 Test 方案（修订版提案，未冻结；须先独立提交并由 Master 放行 Increment → Test 后才执行）。**

| 项 | 提案 |
| --- | --- |
| 顺序与前置 | ① 本方案先独立提交冻结，Master 放行 **Increment → Test** 后才执行；② 结构变更先派 `plugin-dev:plugin-validator`，显式 `model: "haiku"`，审 `agents/advisor.md`、两个新技能、清单 `skills` 追加与两份文档；③ 再做无头场景；④ 生成的 Agent 定义交 Master 在交互会话补跑 Workflow 闭环 |
| 环境 | 仓外空测试家目录与 `CLAUDE_CONFIG_DIR`、合成 Git 项目、白名单环境变量、`--setting-sources project,local`、`--strict-mcp-config`、故障即拒守卫；每次开跑前 `/context all` 确认指令文件为 0；只用合成数据，不改用户模型／网关／权限／遥测 |
| **工具面（按场景分，不混用）** | **PBI-73 参谋线**：父会话 `Read,Grep,Glob,Skill,Agent`，禁 `Write,Edit,NotebookEdit,Bash,PowerShell,Workflow,SendMessage,WebFetch,WebSearch` 与 `mcp__*`；子代理由定义强制只读。**PBI-75 登记线**：父会话 `Read,Grep,Glob,Write,Edit,Skill,Agent`（不加 Shell、网络与 MCP），并由故障即拒守卫把 `Write`／`Edit` 硬限在该样本的合成项目目录内，严禁写项目外、真实 `~/.claude/agents/` 或本仓库 |
| Developer 侧（隔离无头，`-p`） | **参谋线**：纠正前提、独立赞同、缺少材料各一次；另核非显式请求 0 自动召唤、实际只读不转派、夹具前后一致。**角色线四场景**：① 接受登记——至少一例**中文转置或非固定形态** §2.1 夹具，验「预览 → 明确同意 → 成对写入 → 同会话下一轮普通 `Agent` 按名召唤且无旧评议」；② 拒绝——两处未改，临时 `stakeholder` 召唤仍可用；③ 更新与重名冲突——含隔离 `HOME/.claude/agents/` 的同名作用域冲突，只报不覆盖、未批不变、批准才更新且不改他域；④ 角色职责与 Review 召唤权边界 |
| Master 侧（交互 Workflow 闭环） | 场景 ① 中由 `project-stakeholder` 真实生成的 `.claude/agents/<name>.md` 与合成夹具归档到 `S:\IDEO-Scrum-Archives\sprint-22-project-agents\h7\generated-agent\`；由 Master 在交互 Claude Code `2.1.329`（显式 `model: "haiku"`）对**该真实生成文件**补跑 `Workflow`（`75-W`）与普通 `Agent` 双入口验收，不在无头 `-p` 里空写跑 Workflow |
| 模型字段口径 | `advisor.md` 定义请求 `fable`；`claude-magpie` 不认该别名时，按 PO 2026-11-20 授权在该样本的调用参数里指定通道可用的模型（不改用户设置），开跑前先预检通道路由，避免因模型字段白耗预算；无论哪种，`second-opinion` 都不得把未验证的型号写成已验证，H7 只核这一条行为，不把具体型号列为通过线 |
| DoD 对账（§1.3，H7 填 §5 时逐项列证据） | 完整产品 DoD：`claude plugin validate --strict plugins/ideo-scrum`、`node --test scripts/check_dsh.mjs`、`python -X utf8 -I scripts/check_docs.py` 与 `--selftest`；**全部**技能与代理 `description` ≤ 1024；内容忠实（本次未改第三方原文；基线五模式署名缺口另见 Sprint 21）；署名（新文件为作者自写，无第三方摘录，不入 ATTRIBUTION）；可导航与无死链（`check_docs` 覆盖）；Outcome Done 诚实标注「未重测全流程」，不以本期局部验证代替 |
| 预算（提案） | 参谋 3 样本、角色 4 样本，合计 7 样本；单样本 ≤ 240 秒、总量 ≤ 30 分钟、客户端估算 ≤ US$3.00；登记与拒绝类动作中不调用模型的部分零成本；超时终止整棵进程树；不补跑、不挪预算 |
| 停点 | 任一场景缺证据记「未验证」并停在该场景，不改验收线；H7 结果交 Master；正式 Review／合并／tag／推送／发布仍由 PO 决定 |

**2026-11-21 · Master 冻结并放行 Increment → Test（H7）。** 复核 `b88a79b`、`6e4f45c`，并在 `6e4f45c` 上独立复跑 `claude plugin validate --strict`（通过）、`node --test scripts/check_dsh.mjs`（6/6）、`python -X utf8 -I scripts/check_docs.py`（7 文档、103 链、0 错）与 `--selftest`（17/17），确认三处组件／文档修订及四处 H7 方案修订全部落实。依 PO 2026-11-20 Review 前全权委托，冻结 `6e4f45c` 并放行按该方案执行 H7。

核对放行时 §1.1 的 Sprint Goal 原文快照：「独立的第二视角：拍板前能请参谋复核方案，也能按本项目的角色卡听取 Stakeholder 的反馈；身份不用每次重讲，意见每次独立，决定仍由 PO 来做。」

执行约束：先派结构审阅（`plugin-dev:plugin-validator`，显式 `model: "haiku"`；后台会话不提供该类型时报 Master 代跑，不换模型、不跳过）；再按冻结方案跑 7 个隔离无头场景，分场景工具面、故障即拒守卫、`/context all` 指令文件为 0、先预检通道路由；原始证据存仓外 `S:\IDEO-Scrum-Archives\sprint-22-project-agents\h7\`，场景 ① 真实生成的定义与夹具归档到其 `generated-agent\` 供 Master 补跑 `Workflow` 与 `Agent` 双入口；执行期间不改通过线与产品源码，实测暴露组件缺陷就停下报 Master 裁定；完成后结果与 §1.3 完整产品 DoD 对账写入 §5 并单文件提交，停在 Master 补跑与 Review 前复核。

## 5. Test
