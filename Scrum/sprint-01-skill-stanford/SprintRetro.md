# Sprint Retrospective — Sprint 01

> 按 Scrum Guide Expanded v2026.1 的 Sprint Retrospective event 框架。
> Date: 2026-07-22

---

## What Went Well

1. **Increment 质量达标。** 五个 IDEO-modes 文件 + 重构后的 SKILL.md 内容忠于原文、引用清晰、结构可用。Output Done 六条标准中五条满足。
2. **H-1 → H-4 分步提交纪律好。** 每一步原子化、可回溯，符合 Definition of Output Done 对"无死链"和"结构一致"的要求。
3. **SM agent review 有价值。** 虽然 SM agent 未成功 spawn（用 general-purpose 替代），但 review 揭示了我们跳过了 Review / Retro / Daily Scrum / README 更新等关键事件。没有这个外部视角，这些漏洞会被忽略。
4. **Scrum artifact 体系运作良好。** Product → DoD → Product Backlog → Sprint Backlog 的链条清晰，SGEP 框架在单人团队中仍然提供了结构化的检视点。

---

## What Didn't Go Well

1. **Scrum 事件全部缺失。** Sprint Planning 是隐式的（我们直接跳进 H-1），没有 Daily Scrum，没有正式的 Sprint Review 和 Retro（这次补写了 Review，但 Retro 是 Sprint 关闭后才写的——失去了"在 Sprint 内检视与适应"的意义）。**这本质不是在跑 Scrum，而是在跑一个带 Backlog 的 checklist。**

2. **Sprint 过长，没有时间盒。** 从开始到结束跨越了一整天（但包含了大量反复改名和结构调整），没有为 Sprint 设定明确的时间约束。没有时间盒意味着没有 Focus 的压力——可以无限打磨。

3. **PBI-1 过大，不可检视。** 单个 L-size 项占满整个 Sprint，H-1 到 H-4 是顺序依赖的瀑布步骤而非独立可交付的增量。如果在 H-3 融合时发现方向问题，H-1 和 H-2 的工作无法独立交付价值。

4. **命名反复。** `ideo-kernel → design-thinking → design-kernel`，`IDEO-modes → modes → IDEO-modes`。根源是边做边想而非先达成共识。这在实际编码中浪费了多次 commit 和心智切换。

5. **README 延迟更新。** CLAUDE.md 要求 README 是"项目地图"和"当前状态"，但它在整个 Sprint 期间都处于过期状态。这是 SM review 才发现的——自我检视机制缺失。

---

## Improvement Actions for Sprint 02

| # | Action | Severity |
|---|---|---|
| 1 | **设定 Sprint 时间盒。** Sprint 02 在开始时明确结束时间（建议：一个工作会话或一天）。过期即停止，而非无限打磨。 | 高 |
| 2 | **Sprint Planning 必须结构化。** 在开始 Sprint 02 之前，明确 Sprint Goal（Why）、选中的 PBI（What）、和工作计划（How），并写入 sprint-backlog。不做隐式 Planning。 | 高 |
| 3 | **至少做一次 Daily Scrum 检查点。** 即使单人团队，中途暂停一次问三个问题：昨天做了什么、今天要做什么、有什么阻碍。这创造了一个"检视与适应"的时刻，而非事后回顾。 | 中 |
| 4 | **拆分 PBI。** 不选单个 L-size PBI。Sprint 02 至少选 2 个小 PBI，每个可独立交付价值。split 的标准：每个 PBI 应该在 Sprint 50% 时间内可完成。 | 中 |
| 5 | **命名在 Planning 时确定。** 在开始写代码之前定好新的文件/目录名，不边做边改。 | 低 |
| 6 | **README 随 Increment 同步更新。** 将 README 更新纳入 Definition of Output Done 的隐性要求——任何改变文件结构的 Increment 必须附带 README 更新。 | 中 |
