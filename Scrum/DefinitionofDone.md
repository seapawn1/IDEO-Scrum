# Definition of Done

> 按 Scrum Guide Expanded v2026.1 的 Product 与 Increment artifact 框架定义。
> Product Owner: SeaPawn

---

## Definition of Outcome Done

> Product 的承诺。定义价值是否被实现的**可观测证据**（定量或定性）。在价值实现前定义度量，以避免偏见和错误解读。优先使用直接证据而非间接证据。

| 类别 | 度量 | 目标信号 |
|---|---|---|
| **User outcomes** | 一次对话中完成完整 Scrum Event 引导 | 事件引导覆盖 Why / What / How 三个层面 |
| | 一次对话中完成完整 Design Thinking mode 引导 | mode 引导覆盖该 mode 的核心动作（如 Empathize 的 Observe/Engage/Immerse） |
| | 查阅 reference 后能独立执行，不反复追问 | ≤ 2 轮对话进入执行 |
| | 角色 agent 回答被采纳或认可 | 用户不再追问同一问题 |
| **Product Stakeholder outcomes** | scrum-kernel 引用完整性 | SGEP 关键章节无遗漏 |
| | ideo-kernel 引用完整性 | IDEO/Stanford Design Guides 五个 mode 原文无遗漏 |
| | 文档溯源标注合规 | 所有 reference + method 文件标注来源和 license（SGEP CC BY-SA 4.0 / IDEO Stanford Design Guides / Design Sprint by Jake Knapp） |
| | 新用户从 SKILL.md 找到目标 reference 的跳数 | ≤ 2 跳（两个 kernel 均满足） |
| **Business impact** | 第三方用户成功安装并使用 | `claude plugins install` 可用 |
| | 版本迭代节奏 | 每个 Sprint 产出可发布的 Increment |

---

## Definition of Output Done

> Increment 的承诺。定义 Increment 达到可交付 Stakeholders 的**质量标准**。是整体 Increment 的合格线，而非逐项 Acceptance Criteria。不可在 Sprint 中弱化。

| 维度 | 标准 |
|---|---|
| **内容忠实** | 所有 reference 文档内容忠于源材料（SGEP / IDEO Stanford Design Guides / Design Sprint），不增不减不曲解 |
| **溯源合规** | 每个拆分自 SGEP 的文件标注 `Source: Scrum Guide Expanded v2026.1` + `License: CC BY-SA 4.0` + 作者署名 |
| **结构一致** | 文件路径与 README 文件地图一致；SKILL.md 的 Reference Catalog 和目录表指向的文件全部存在 |
| **无死链** | 所有 markdown 内部链接（`[text](path.md)`）可解析，无 404 |
| **可导航** | 用户从 SKILL.md 入口出发，≤ 2 次点击到达任意 reference 文档或 role agent |
| **语言分明** | 项目文档（README、CLAUDE.md、Scrum/ 下文件）用中文；引用源材料的内容保留原文语言（英文） |
