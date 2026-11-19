# Sprint Backlog — Sprint 22 (project-agents)

> Started: 2026-11-19 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `claude/sprint-22-project-agents-b09bf1` | Product Owner: SeaPawn | Scrum Master: 项目 Scrum Master | Developer: Sprint 22 Developer
> Now: What；PO 已放行本期 What，并定案参谋「默认 Fable，可另选」；两项首轮验收草案已记，待 Master 与 PO 逐项收口。
> Waiting for PO: 1. PBI-75 验收是否必须为普通子代理和 Workflow 两个入口分别举证？
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

沿用 §2.1 的用户故事，先精化 PBI-73，再精化 PBI-75，两项分别验收。以下是 Master 在 2026-11-19 提出的首轮验收草案及 Developer 的复述和暂估。除注明的 PO 定案外，判据仍待收口，未做实测。

**PBI-73：参谋**

来源：[产品日志 §3.1](../ProductBacklog.md#31-当前的-pbi) 中 PBI-73 所列个人原型 `advisor-synthesis.md`（§1、§8–9）和 Master 首轮提议。原型的脚本、双模型投票、费用线、固定回话模板和当时「不做插件」的限制不自动沿用；原型不等于插件已有能力。

复述：在拍板、选方案或评审设计时，给参谋一个待决定的问题、约束及点名材料的原文。参谋独立回答「怎么看，为什么」，理由能对照原件；只读，不改产物，不替 PO 决定。

| 验收场景（草案） | 过线行为 |
| --- | --- |
| 材料足以纠正一个前提 | 指出哪个前提需改、哪处原文支持纠正，以及为何影响判断。 |
| 原方案有充分依据 | 可以赞同，独立说明理由，不为展示差异强造反对意见。 |
| 缺少关键材料 | 指出缺什么、为何会改变判断；可以请求补充，不编造依据或强下结论。 |

三个场景分别核对独立判断、原件依据、只读与决策边界。不以意见是否不同于主会话作为过线依据。

**模型选择，PO 定案（2026-11-19，Master 转达）：**「默认 Fable，可另选」。

| 情形 | 要核验的行为 |
| --- | --- |
| 未指定其他模型 | 默认选 Fable。 |
| 项目明确另选可用模型 | 遵从该选择。 |
| 所选模型不可用 | 如实提示，可另选或取消，不静默换模型。 |

这个决定只约束参谋，不约束普通 Stakeholder、Developer 或现有会话。配置入口与模型名解析留给 How；不把固定版本 ID 或个人网关映射当成通用规则。

**Developer 暂估：S～M，偏 M。** 除三个意见场景，还有三种模型选择行为；若调研证明既有做法可同时满足只读、独立与模型选择，才向 S 调整。保留 PO 要求的调研：实际设计前用适用的 IDEO 方法了解已有做法，结论交三方，再定 How。

**PBI-75：项目 Stakeholder**

来源：[产品日志 §2.1](../ProductBacklog.md#21-stakeholders) 的角色卡、§3.1 的 PBI-75、[现行 Stakeholder 命令](../../plugins/ideo-scrum/commands/stakeholder.md#code-of-conduct) 和 Master 首轮提议。

复述：用一张已确认的角色卡（例如「陌生人」）核对。项目 Stakeholder 按卡片立场给外部反馈，每个项目只登记自己的角色。可复用的是角色定义，不是旧评议；即使共用技术手段，也不把 Stakeholder 反馈当成参谋的第二判断。

Master 转达 PO 原话：「开子代理的时候，开工作流的时候就可以直接复用」。两种入口复用同一份已注册的项目角色，不做两套注册，也不要求每个项目启用 Workflow。

| 验收场景（草案） | 过线行为 |
| --- | --- |
| 接受配置 | 角色卡确认后展示可选配置，接受才只在本项目登记，并让该项目产品日志 §2.1 指到对应角色。Master 建议在支持 Workflow 的 Claude Code 环境，分别从普通子代理和 Workflow 按名调用同一份角色定义；各用独立的新上下文，不带旧评议，不强求意见不同。 |
| 拒绝配置 | 不写文件、不造引用；仍能临时按角色卡请全新子代理给外部反馈。 |
| 角色卡变更或已有同名配置 | 先显示差异；未批准则原文件和引用保持不变，批准才更新，不静默覆盖。 |
| 角色职责与召唤权 | 常驻 PO 助手不冒称独立审阅者，不串用职责；在 Sprint Review，外部视角仍由 PO 或 Scrum Master 召唤，建造者不召唤。 |

**Developer 暂估：M（3–5 个会话）。** 四种情形需分别取得证据。只核验一个入口不能证明另一个；验收是否必须为两处分别举证，由 Master 向 PO 确认。Claude Code 中项目角色在两类入口的可发现范围待查；不能用全局配置兜底。

现只核对 Claude Code 已明的项目作用域；不做通用 Claude Code Setup、MCP 或全局配置。DSH 的项目 Agent 等价能力待查，不在本期承诺内。

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |

**Key choices**

**Risks and open points**

## 4. Increment notes

## 5. Test
