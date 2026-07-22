# Sprint Backlog — Sprint 04

> 按 Scrum Guide Expanded v2026.1 的 Sprint Backlog artifact 框架定义。
> Product Owner: SeaPawn

---

## Sprint Goal

**插件所有 description 字段经过审计和优化后，自动触发精确度和召回率达到可用水平——核心场景不漏触发，非相关场景不误触。**

> 相干 Product Goal：design-kernel 达到与 scrum-kernel 同等细致的结构化水平。

---

## What — 选中的 PBI

| # | 标题 | 用户故事 | Outcome Criteria | Acceptance Criteria | Size | 当前状态 | 备注 |
|---|---|---|---|---|---|---|---|
| PBI-4 | 细化插件所有 description 字段——提升自动触发准确率 | 作为 IDEO-Scrum 用户，我希望插件的 skills、agents、output-styles 能在正确的场景下被自动触发或召唤——该出现时出现，不该出现时不打扰——而不是我每次都要手动 `/` 调用 | 插件的所有 `description` 字段经过审计和优化后，自动触发的精确度和召回率达到可用水平——核心场景不漏触发，非相关场景不误触 | — | S | 已完成 | description 是 Claude Code 自动发现机制的核心匹配依据——模糊的 description 导致 skill/agent 不被触发，过于宽泛的 description 导致错误触发、浪费上下文窗口 |

---

## How — 工作计划

| # | 步骤 | 输入 | 输出 | 状态 |
|---|---|---|---|---|
| 1 | 审计所有 description 字段 | plugin.json + 2 SKILL.md + 10 agents | 13 个 description 的问题清单：① "discussing" 过于狭窄（漏掉 "acting as" 和 "perspective needed" 场景）；② SKILL.md design-kernel 使用 "covering" 而非 "Use when" 触发模式；③ SKILL.md scrum-kernel 第二句指向 skill 自身而非触发场景；④ plugin.json 仅中文且缺乏场景关键词；⑤ 同 kernel agent 间描述模板趋同，区分度不足 | 完成 |
| 2 | 优化 2 个 SKILL.md description | design-kernel + scrum-kernel SKILL.md frontmatter | design-kernel：改为 "Use when applying Design Thinking or Design Sprint —" + 具体方法名关键词；scrum-kernel：扩展为包括 Sprint 事件名和角色名，移除自身描述句 | 完成 |
| 3 | 优化 10 个 agent description | scrum-kernel 6 + design-kernel 4 agents frontmatter | "discussing" → "role is needed" / "perspective is needed"；每个 agent 增加角色专属场景词（如 PO→backlog prioritization, SM→impediment removal）；design-sprint 4 个 agent 增加五天流程的特定活动名 | 完成 |
| 4 | 优化 plugin.json description | plugin.json | 双语场景关键词：Design Thinking + Scrum Sprint + methodology + human-centered design + agile | 完成 |
| 5 | 更新 Product Backlog | product-backlog.md | PBI-4 标记已完成 | 完成 |
| 6 | Sprint Review | Sprint 完成 | SprintReview.md | 完成 |
