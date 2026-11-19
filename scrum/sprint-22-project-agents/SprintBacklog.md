# Sprint Backlog — Sprint 22 (project-agents)

> Started: 2026-11-19 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `claude/sprint-22-project-agents-b09bf1` | Product Owner: SeaPawn | Scrum Master: 项目 Scrum Master | Developer: Sprint 22 Developer
> Now: What；PO 已确认 Why 并明确放行本期 What；PBI-73、PBI-75 已列入，待 Master 给出首轮精化判据。
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

先精化 PBI-73，再精化 PBI-75，两项分别验收。以下为 Developer 的边界复述与暂估，验收判据和通过线待 Master 主导精化，尚未定案。

| 条目 | 边界复述 | 规模与可行性（暂估） |
| --- | --- | --- |
| PBI-73 | 拍板、选方案或评审设计时，参谋只读地提供独立第二意见，不改被评议产物，不替 PO 拍板。按 PO 要求，实际设计前先用适用的 IDEO 方法调研已有做法。 | 沿用 S～M。若既有做法能复用且满足只读与独立性，偏 S；若需重新验证角色或宿主约束，偏 M。早期原型是调研输入，不能当作插件已有能力。 |
| PBI-75 | 每个项目只注册自己的 Stakeholder 角色，角色卡是外部反馈的立场，不是参谋的第二判断。角色卡定后展示可选配置，接受才写入该项目并在该项目产品日志 §2.1 引用；拒绝不写，仍可临时召唤。更新先展示差异，得到同意后才写，不静默覆盖。只复用角色定义，每次用新上下文听取反馈，不沿用旧评议。 | 暂估 M（3–5 个会话）。注册、拒绝、更新与后续按名召唤都需要证据。待实查项目角色在 Claude Code 子代理或 Workflow 中的可发现范围；这会影响验收，不能用全局配置兜底。 |

Claude Code 是已知宿主；不含通用 Claude Code Setup、MCP 或全局配置。DSH 的项目 Agent 等价能力待查，不在本期承诺内。

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |

**Key choices**

**Risks and open points**

## 4. Increment notes

## 5. Test
