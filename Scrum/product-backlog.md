# Product Backlog

> 按 Scrum Guide Expanded v2026.1 的 Product Backlog artifact 框架定义。
> Product Owner: SeaPawn

---

## Product Goal

**design-kernel 达到与 scrum-kernel 同等细致的结构化水平。**

---

## Product Backlog Items

| # | 标题 | 用户故事 | Outcome Criteria | Acceptance Criteria | Size | 当前状态 | 备注 |
|---|---|---|---|---|---|---|---|
| PBI-1 | 细化 ideo-kernel SKILL.md — 融合 Stanford Design Guides | 作为 ideo-kernel 用户，我希望 SKILL.md 中的五模式引导有 WHAT / WHY / HOW 三层结构，而不是当前的单层概述，这样一次对话就能获得完整方法论引导，不需要额外查阅 Stanford 原文 | ideo-kernel SKILL.md 的每个 mode 达到 Stanford Design Guides 的细致程度，用户在 Empathize / Define / Ideate / Prototype / Test 任一 mode 都能获得"是什么—为什么—怎么做"的完整引导 | 5 个 mode 各自包含 WHAT / WHY / HOW 三个子节；内容忠于 `references/IDEO-StanfordDesignGuides.md` 原文；标注 Source: IDEO / Stanford d.school Design Guides；保留当前 verbatim 段中 Stanford 未覆盖的补充内容；mode 间 transition 指引保留（如 Empathize >> Define 的 Unpack） | L | 已完成 | Sprint 01 交付：`design-kernel/SKILL.md` 重构 + `IDEO-modes/` 5 文件（WHAT/WHY/HOW + Transition + Source/License） |
| PBI-2 | 插件新增 output-styles — Design Thinking 与 Scrum 对话风格 | 作为 IDEO-Scrum 用户，我希望在 Design Thinking 或 Scrum Sprint 场景下能切换 Claude 的输出风格，让对话氛围与当前方法论模式匹配——比如 Empathize 时偏探索式提问，Sprint Planning 时偏结构化引导——而不需要每次在 prompt 里手动设定角色 | 用户在 Design Thinking 模式和 Scrum Sprint 模式下各有可直接使用的 output-style 文件；切换后 Claude 的行为调性与方法论要求一致，用户不需要额外解释"你现在应该用什么语气" | ① 新增 output-style `.md` 文件，放在插件目录下；② 每个 style 文件符合 Claude Code output-style 规范（YAML frontmatter `name` + `description` + markdown body）；③ Design Thinking style 覆盖五模式下的提问/引导风格（探索式、不急于收敛）；④ Scrum style 覆盖 Sprint 事件中的角色语气（聚焦目标、时间盒意识、检视与适应）；⑤ 与现有 scrum-kernel role agents 互补——agent 做深度方法论引导，output-style 做对话层调性 | M | 待开始 | — |
| PBI-3 | scrum-kernel agents 重构——移至插件 agents/ 目录 + 内容改回 SGEP 原文摘抄 | 作为 IDEO-Scrum 用户，我希望 scrum-kernel 的 6 个角色能够以真正的 subagent 形式被召唤（如 `/ideo-scrum:scrum-scrum-master`），并且每个 agent 的方法论内容直接摘抄 SGEP 原文而非经过改写，这样我能信任 agent 输出的是方法论原文、而非 agent 编写者的个人解读 | scrum-kernel 的 6 个角色从"skill 附属参考文档"升级为"可独立 spawn 的 Claude Code subagent"；用户召唤任一 role agent 后，其回答内容忠于 SGEP 原文、标注章节出处，不发生自创或释义性偏离 | ① 6 个 agent 文件从 `skills/scrum-kernel/agents/` 移至 `plugins/ideo-scrum/agents/`，符合 Claude Code agent 自动发现路径；② 每个 agent body 的方法论内容改为直接摘抄 SGEP `assets/scrum-guide-expanded-2026.1.md` 对应的原文段落，保留原文引用标注（如 `[12-17]`）；③ 保留 agent frontmatter 中的 `name`、`description`、`model`、`color`、`tools` 字段；④ 保留并优化 `When to invoke`、`Guiding Principles`、`Output Format` 等行为层指令（这些是 agent 独有、SGEP 中没有的）；⑤ SKILL.md 的 Reference Catalog 中 role agents 表更新为 scoped name（如 `ideo-scrum:scrum-scrum-master`）并标注为可 spawn agent 而非 reference 文档；⑥ 现有 PBI-1 / PBI-2 中依赖 agent 的工作不因此 PBI 而被阻塞——agent 重构可与 ideo-kernel 工作并行 | L | 待开始 | 当前 agent 文件位于 skill 目录下，未被 Claude Code 自动发现（已验证：`subagent_type` 传入当前路径和文件名均返回 not found）；SGEP Scrum Master 原文在 `scrum-guide-expanded-2026.1.md` L421-488，PO 在 L385-419，Product Developer 在 L361-383 |
| PBI-4 | 细化插件所有 description 字段——提升自动触发准确率 | 作为 IDEO-Scrum 用户，我希望插件的 skills、agents、output-styles 能在正确的场景下被自动触发或召唤——该出现时出现，不该出现时不打扰——而不是我每次都要手动 `/` 调用 | 插件的所有 `description` 字段（plugin.json、2 个 SKILL.md、6 个 agents、output-styles）经过审计和优化后，自动触发的精确度和召回率达到可用水平——核心场景不漏触发，非相关场景不误触 | ① 审计当前所有 `description` 字段（`plugin.json`、`design-kernel/SKILL.md`、`scrum-kernel/SKILL.md`、6 个 agent frontmatter、若干 method 文档的 trigger 字段），记录现状；② 提炼 description 编写规范——遵循 "Use when…" 模式，覆盖触发场景关键词但避免过度宽泛；③ 逐个优化 description：明确 WHAT（组件做什么）、WHEN（什么场景触发）、不 WHAT（排除什么场景）；④ 验证：通过 Claude Code 实际对话测试每种场景的触发行为，记录误触发和漏触发；⑤ description 审计报告纳入 `Scrum/` 目录作为质量文档 | S | 待开始 | description 是 Claude Code 自动发现机制的核心匹配依据——模糊的 description 导致 skill/agent 不被触发，过于宽泛的 description 导致错误触发、浪费上下文窗口 |
| PBI-5 | 重组 Design Sprint 内容结构 | 作为 IDEO-Scrum 用户，我希望 Design Sprint 方法论的内容像 Stanford Design Guides 和 SGEP 一样有清晰的文件结构，而不是堆在一个大 markdown 文件里，这样在 Sprint Week 的每个阶段都能快速找到对应的方法论引导 | — | — | — | 待开始 | 源材料：`references/DesignSprint-HowtoSolveBigProblemsandTestJakeKnapp.md`（全书，含 111 张图片引用）；当前只有一个 `methods/design-sprint.md` 作为入口；目标是将全书内容拆分为结构化的多文件体系 |
| PBI-6 | 删除所有 SGEP 相关内容 | — | — | — | — | 待开始 | — |
