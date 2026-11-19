# Sprint Backlog — Sprint 22 (project-agents)

> Started: 2026-11-19 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `claude/sprint-22-project-agents-b09bf1` | Product Owner: SeaPawn | Scrum Master: 项目 Scrum Master | Developer: Sprint 22 Developer
> Now: What；PO 已委托 Master 决定 PBI-75 双入口验收门槛，Master 已定。PBI-73、75 的验收判据已通过 Master 审阅，精化未结束。
> Waiting for PO: 1. 是否结束 Sprint 22 的 What 精化？
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

沿用 §2.1 的用户故事，先精化 PBI-73，再精化 PBI-75，两项分别验收。以下是 Master 在 2026-11-19 提出的验收场景及 Developer 的复述和暂估；判据已通过 Master 审阅，待 PO 决定是否结束 What，未做实测。

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

**Developer 核对（2026-11-19）：** 两项分别落实 §1.1 的独立判断和项目角色复用；PBI-73 的设计前 IDEO 调研仍待完成。

**Master 审阅（2026-11-19，基于 `a5a7595`）：** PBI-73、75 的验收场景和取证口径均无必改项，可交 PO 决定是否结束 What。判据审阅通过不是功能验收通过；未放行 How、施工或实测。

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |

**Key choices**

**Risks and open points**

## 4. Increment notes

## 5. Test
