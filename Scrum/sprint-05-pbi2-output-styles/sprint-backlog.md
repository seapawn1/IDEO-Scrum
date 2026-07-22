# Sprint Backlog — Sprint 05

> 按 Scrum Guide Expanded v2026.1 的 Sprint Backlog artifact 框架定义。
> Product Owner: SeaPawn

---

## Sprint Goal

**插件新增 output-styles——Design Thinking 与 Scrum Sprint 场景下各有可直接切换的输出风格，Claude 的行为调性与方法论模式匹配，无需每次手动设定角色。**

> 相干 Product Goal：design-kernel 达到与 scrum-kernel 同等细致的结构化水平。

---

## What — 选中的 PBI

| # | 标题 | 用户故事 | Outcome Criteria | Acceptance Criteria | Size | 当前状态 | 备注 |
|---|---|---|---|---|---|---|---|
| PBI-2 | 插件新增 output-styles — Design Thinking 与 Scrum 对话风格 | 作为 IDEO-Scrum 用户，我希望在 Design Thinking 或 Scrum Sprint 场景下能切换 Claude 的输出风格，让对话氛围与当前方法论模式匹配——比如 Empathize 时偏探索式提问，Sprint Planning 时偏结构化引导——而不需要每次在 prompt 里手动设定角色 | 用户在 Design Thinking 模式和 Scrum Sprint 模式下各有可直接使用的 output-style 文件；切换后 Claude 的行为调性与方法论要求一致，用户不需要额外解释"你现在应该用什么语气" | — | M | 进行中 | output-styles 目录位于插件根目录。格式：frontmatter (name, description, keep-coding-instructions) + markdown body。 |

---

## How — 工作计划

| # | 步骤 | 输入 | 输出 | 状态 |
|---|---|---|---|---|
| 1 | 确定粒度与数量 | IDEO 五模式行为调性 + Scrum 四事件行为调性 | Design Thinking 5 个（Empathize / Define / Ideate / Prototype / Test）+ Scrum 4 个（Sprint Planning / Daily Scrum / Sprint Review / Sprint Retrospective）= 9 个 output-style 文件 | 待开始 |
| 2 | 编写 Design Thinking 5 个 output-style 文件 | IDEO-modes/ 各 mode 的 WHAT/WHY/HOW | `output-styles/design-thinking-empahtize.md` 等 5 个文件 | 待开始 |
| 3 | 编写 Scrum 4 个 output-style 文件 | scrum-kernel/references/ 各 event 文件 | `output-styles/scrum-sprint-planning.md` 等 4 个文件 | 待开始 |
| 4 | 更新 Product Backlog | product-backlog.md | PBI-2 标记已完成 | 待开始 |
| 5 | Sprint Review | Sprint 完成 | SprintReview.md | 待开始 |
