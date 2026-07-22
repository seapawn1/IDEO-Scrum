# IDEO-Scrum

为 Claude Code 提供 Design Thinking 与 Scrum Sprint 方法论的插件。v1.0.0。

## 这里是什么

本插件将 Design Thinking（设计思维）和 Scrum Sprint（敏捷冲刺）两套方法论集成到 Claude Code 中，通过技能（skills）、角色代理（agents）和输出样式（output-styles）提供结构化的协作流程。不做项目管理工具本身，不做 JIRA/Linear 集成，也不做团队协作平台——只提供方法论引导和流程框架。

## 文件地图

### 插件

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/.claude-plugin/plugin.json` | 插件清单 v1.0.0 |
| `plugins/ideo-scrum/output-styles/agent-designer.md` | Output-style — agent 设计结对（IDEO 五模式，先发散后收敛） |
| `plugins/ideo-scrum/output-styles/developer.md` | Output-style — Developer 角色（Sprint Backlog / DoD / Sprint Review / Retro） |
| `plugins/ideo-scrum/output-styles/scrum-master.md` | Output-style — Scrum Master 角色（三大支柱 / 五项价值观 / 仪式优先） |

### design-kernel skill

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/skills/design-kernel/SKILL.md` | Design Kernel 入口（IDEO 五模式表 + Design Sprint 单行引用 + Method Catalog + Use Protocol） |
| `plugins/ideo-scrum/skills/design-kernel/IDEO-modes/` | IDEO Design Thinking 五模式 reference（Empathize / Define / Ideate / Prototype / Test，各含 WHAT/WHY/HOW + Transition） |
| `plugins/ideo-scrum/skills/design-kernel/methods/` | Design Thinking 方法库（~40 个方法，含 Use Before / Use Notes / Do Not Use When） |
| `plugins/ideo-scrum/skills/design-kernel/DesignSprint/design-sprint.md` | Design Sprint 五天入口（Monday checklist 完整，引用 `references/`；Tuesday-Friday 待 PBI-6 重构） |
| `plugins/ideo-scrum/skills/design-kernel/DesignSprint/references/` | Monday 6 个引用文件：define-the-challenge / start-at-the-end / make-a-map / ask-the-experts / how-might-we / pick-a-target（忠实摘录 Knapp 原书） |
| `plugins/ideo-scrum/skills/design-kernel/DesignSprint/agents/` | Design Sprint 4 个角色 agent（Decider / Facilitator / Sprint Team / Experts） |

### scrum-kernel skill

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/skills/scrum-kernel/SKILL.md` | Scrum Sprint 技能内核（Scrum Guide 概述 + Artifact/Event 目录表 + Role Agent 列表） |
| `plugins/ideo-scrum/skills/scrum-kernel/scrum-guide-2020.md` | Scrum Guide 2020 官方全文 |
| `plugins/ideo-scrum/skills/scrum-kernel/agents/` | 6 个 Scrum 角色 agent（PO / SM / PD / Stakeholder / Supporter / AI，SGEP 原文摘抄） |
| `plugins/ideo-scrum/skills/scrum-kernel/assets/scrum-guide-expanded-2026.1.md` | SGEP 完整源文档（Theory / Values-OODA / Roles / 引用列表） |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-*.md` | 4 个 Artifact reference：Product / Increment / Product Backlog / Sprint Backlog |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-event-*.md` | 5 个 Event reference：Sprint / Sprint Planning / Daily Scrum / Sprint Review / Sprint Retrospective |

### Scrum 工作目录

| 文件/目录 | 内容 |
|---|---|
| `Scrum/product.md` | Product artifact — Product 定义 + Vision |
| `Scrum/DefinitionofDone.md` | Definition of Outcome Done + Definition of Output Done |
| `Scrum/product-backlog.md` | Product Backlog — Product Goal + PBI 列表（PBI-1~4 已完成，PBI-5 部分完成，PBI-6 待开始） |
| `Scrum/sprint-01-skill-stanford/` | Sprint 01 ✅：PBI-1 — design-kernel SKILL.md 重构 + IDEO-modes/ 五模式 WHAT/WHY/HOW |
| `Scrum/sprint-02-agents-sgep/` | Sprint 02 ✅：PBI-3 — 6 个 scrum-kernel agent 全部替换为 SGEP 原文摘抄 |
| `Scrum/sprint-03-design-sprint-restructure/` | Sprint 03 ◐：PBI-5 — Monday references/ 6 文件 + SKILL.md 重构完成；Tuesday-Friday 发现方法论分化，转 PBI-6 |
| `Scrum/sprint-04-pbi4-descriptions/` | Sprint 04 ✅：PBI-4 — 13 个 description 字段全部优化（"discussing" → "role is needed"） |
| `Scrum/sprint-05-pbi2-output-styles/` | Sprint 05 ✅：PBI-2 — 3 个角色型 output-style 放入插件（agent-designer / developer / scrum-master） |

### 源参考

| 文件/目录 | 内容 |
|---|---|
| `references/scrum-guide-expanded-2025.6.md` | Scrum Guide Expanded 历史版本 (Jun 2025) |
| `references/scrum-on-one-page.md` | Scrum on One Page 概要 |
| `references/DesignSprint-HowtoSolveBigProblemsandTestJakeKnapp.docx` | *Design Sprint* 原始 Word 文档 |
| `references/DesignSprint-HowtoSolveBigProblemsandTestJakeKnapp.md` | *Design Sprint* — Jake Knapp 全书（已清洗 OCR、章节标题、分隔线） |
| `references/IDEO-StanfordDesignGuides.docx` | IDEO / Stanford 原始 Word 文档 |
| `references/IDEO-StanfordDesignGuides.md` | IDEO / Stanford d.school 设计思维五模式指南 |
| `references/images/design-sprint/` | Design Sprint 配图（115 张，12 MB） |
| `references/images/ideo-design-guides/` | IDEO Design Guides 配图（9 张，8.8 MB） |

## 当前状态

2026-07-23：v1.0.0。5 个 Sprint 完成——插件具备完整的两套方法论体系（IDEO Design Thinking + Scrum Sprint），含 skills、agents、output-styles、method catalog。Design Sprint 五天流程中 Monday 已结构化完成，Tuesday-Friday 待 PBI-6（solo+AI 方法论设计）。

### Product Backlog 概览

| # | 标题 | Size | 状态 |
|---|---|---|---|
| PBI-1 | 细化 design-kernel SKILL.md — 融合 Stanford Design Guides | L | ✅ Sprint 01 |
| PBI-2 | 插件新增 output-styles | M | ✅ Sprint 05 |
| PBI-3 | scrum-kernel agents 重构——SGEP 原文摘抄 | L | ✅ Sprint 02 |
| PBI-4 | 细化插件所有 description 字段 | S | ✅ Sprint 04 |
| PBI-5 | 重组 Design Sprint 内容结构 | — | ◐ Sprint 03 |
| PBI-6 | Design Sprint Tuesday-Friday 细化——solo+AI 方法论设计 | L | ⏳ |
