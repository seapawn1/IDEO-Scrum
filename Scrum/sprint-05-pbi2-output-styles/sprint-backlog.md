# Sprint Backlog — Sprint 05

> 按 Scrum Guide Expanded v2026.1 的 Sprint Backlog artifact 框架定义。
> Product Owner: SeaPawn

---

## Sprint Goal

**插件新增 output-styles——seapawn 提供的 3 个角色型输出风格（agent-designer / developer / scrum-master）放入插件 `output-styles/` 目录，可通过 `/config` 切换。**

> 相干 Product Goal：design-kernel 达到与 scrum-kernel 同等细致的结构化水平。

---

## What — 选中的 PBI

| # | 标题 | 用户故事 | Outcome Criteria | Acceptance Criteria | Size | 当前状态 | 备注 |
|---|---|---|---|---|---|---|---|
| PBI-2 | 插件新增 output-styles — Design Thinking 与 Scrum 对话风格 | 作为 IDEO-Scrum 用户，我希望在 Design Thinking 或 Scrum Sprint 场景下能切换 Claude 的输出风格，让对话氛围与当前方法论模式匹配——比如 Empathize 时偏探索式提问，Sprint Planning 时偏结构化引导——而不需要每次在 prompt 里手动设定角色 | 用户在 Design Thinking 模式和 Scrum Sprint 模式下各有可直接使用的 output-style 文件；切换后 Claude 的行为调性与方法论要求一致，用户不需要额外解释"你现在应该用什么语气" | — | M | 部分完成 | seapawn 提供 3 个角色型文件：agent-designer / developer / scrum-master。Design Thinking 模式型和 Scrum 事件型 output-style 留待后续。 |

---

## How — 工作计划

| # | 步骤 | 输入 | 输出 | 状态 |
|---|---|---|---|---|
| 1 | 接收 seapawn 提供的 3 个 output-style 文件 | agent-designer.md / developer.md / scrum-master.md | 文件审阅——格式正确（frontmatter + body），keep-coding-instructions: true，内容完整 | 完成 |
| 2 | 放入插件 output-styles/ 目录 | 3 个文件 | 复制到 `plugins/ideo-scrum/output-styles/`，修正项目名引用（"ClaudeDream" → "当前项目"） | 完成 |
| 3 | 更新 Product Backlog | product-backlog.md | PBI-2 标记部分完成，注记剩余范围 | 完成 |
| 4 | Sprint Review | Sprint 完成 | SprintReview.md | 完成 |
