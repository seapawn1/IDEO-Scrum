# Product Backlog

> 按 Scrum Guide Expanded v2026.1 的 Product Backlog artifact 框架定义。
> Product Owner: SeaPawn

---

## Product Goal

**ideo-kernel 达到与 scrum-kernel 同等细致的结构化水平。**

---

## Product Backlog Items

| # | 标题 | 用户故事 | Outcome Criteria | Acceptance Criteria | Size | 当前状态 | 备注 |
|---|---|---|---|---|---|---|---|
| PBI-1 | 细化 ideo-kernel SKILL.md — 融合 Stanford Design Guides | 作为 ideo-kernel 用户，我希望 SKILL.md 中的五模式引导有 WHAT / WHY / HOW 三层结构，而不是当前的单层概述，这样一次对话就能获得完整方法论引导，不需要额外查阅 Stanford 原文 | ideo-kernel SKILL.md 的每个 mode 达到 Stanford Design Guides 的细致程度，用户在 Empathize / Define / Ideate / Prototype / Test 任一 mode 都能获得"是什么—为什么—怎么做"的完整引导 | 5 个 mode 各自包含 WHAT / WHY / HOW 三个子节；内容忠于 `references/IDEO-StanfordDesignGuides.md` 原文；标注 Source: IDEO / Stanford d.school Design Guides；保留当前 verbatim 段中 Stanford 未覆盖的补充内容；mode 间 transition 指引保留（如 Empathize >> Define 的 Unpack） | L | 进行中 | 源材料：`references/IDEO-StanfordDesignGuides.md`（214 行）；当前 SKILL.md verbatim 段约 100 行，需扩展为 5 个 mode × 3 层结构 |
| PBI-2 | 插件新增 output-styles — Design Thinking 与 Scrum 对话风格 | 作为 IDEO-Scrum 用户，我希望在 Design Thinking 或 Scrum Sprint 场景下能切换 Claude 的输出风格，让对话氛围与当前方法论模式匹配——比如 Empathize 时偏探索式提问，Sprint Planning 时偏结构化引导——而不需要每次在 prompt 里手动设定角色 | 用户在 Design Thinking 模式和 Scrum Sprint 模式下各有可直接使用的 output-style 文件；切换后 Claude 的行为调性与方法论要求一致，用户不需要额外解释"你现在应该用什么语气" | ① 新增 output-style `.md` 文件，放在插件目录下；② 每个 style 文件符合 Claude Code output-style 规范（YAML frontmatter `name` + `description` + markdown body）；③ Design Thinking style 覆盖五模式下的提问/引导风格（探索式、不急于收敛）；④ Scrum style 覆盖 Sprint 事件中的角色语气（聚焦目标、时间盒意识、检视与适应）；⑤ 与现有 scrum-kernel role agents 互补——agent 做深度方法论引导，output-style 做对话层调性 | M | 待开始 | — |
