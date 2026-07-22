# IDEO-Scrum

为 Claude Code 提供 Design Thinking 与 Scrum Sprint 方法论的插件。

## 这里是什么

本插件将 Design Thinking（设计思维）和 Scrum Sprint（敏捷冲刺）两套方法论集成到 Claude Code 中，通过技能（skills）和输出样式（output-styles）提供结构化的协作流程。不做项目管理工具本身，不做 JIRA/Linear 集成，也不做团队协作平台——只提供方法论引导和流程框架。

## 文件地图

### 项目

| 文件/目录 | 内容 |
|---|---|
| `.gitignore` | Git 忽略规则 |
| `.env` | 本地私人环境 |
| `seapawn.md` | 本地私人笔记 |
| `CLAUDE.md` | 项目定位 |
| `.claude-plugin/marketplace.json` | Marketplace 清单 |

### design-kernel skill

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/.claude-plugin/plugin.json` | 插件清单 |
| `plugins/ideo-scrum/skills/design-kernel/SKILL.md` | Design Kernel 入口（Overview + Use Protocol + Method Catalog + Runtime Rule） |
| `plugins/ideo-scrum/skills/design-kernel/IDEO-modes/` | IDEO Design Thinking 五模式 reference（Empathize / Define / Ideate / Prototype / Test，各含 WHAT/WHY/HOW + Transition） |
| `plugins/ideo-scrum/skills/design-kernel/methods/` | Design Thinking 方法库（~40 个方法） |

### scrum-kernel skill

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/skills/scrum-kernel/SKILL.md` | Scrum Sprint 技能内核（Elements of Scrum + Reference Catalog + Artifact/Event 目录表） |
| `plugins/ideo-scrum/skills/scrum-kernel/scrum-guide-2020.md` | Scrum Guide 2020 官方全文（foundation） |
| `plugins/ideo-scrum/skills/scrum-kernel/agents/` | 6 个 Scrum 角色 agent（PO / SM / PD / Stakeholder / Supporter / AI） |
| `plugins/ideo-scrum/skills/scrum-kernel/assets/scrum-guide-expanded-2026.1.md` | SGEP 完整源文档（Theory / Values-OODA / Roles / End Note / 引用列表） |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-product.md` | Artifact — Product + Definition of Outcome Done |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-increment.md` | Artifact — Increment + Definition of Output Done |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-product-backlog.md` | Artifact — Product Backlog + PBI + Acceptance Criteria + Refinement + Product Goal |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-sprint-backlog.md` | Artifact — Sprint Backlog + Sprint Goal |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-event-sprint.md` | Event — The Sprint（容器事件） |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-event-sprint-planning.md` | Event — Sprint Planning（Why / What / How） |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-event-daily-scrum.md` | Event — Daily Scrum |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-event-sprint-review.md` | Event — Sprint Review |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-event-sprint-retrospective.md` | Event — Sprint Retrospective |

### Scrum 工作目录

| 文件/目录 | 内容 |
|---|---|
| `Scrum/product.md` | Product artifact — Product 定义 + Vision |
| `Scrum/DefinitionofDone.md` | Definition of Outcome Done + Definition of Output Done |
| `Scrum/product-backlog.md` | Product Backlog — Product Goal + PBI 列表 |
| `Scrum/sprint-01-skill-stanford/` | Sprint 01：sprint-backlog + SprintReview + 工作材料（stanford-modes / ideo-modes） |
| `Scrum/sprint-02-agents-sgep/` | Sprint 02 ✅：PBI-3 — 6 个 agent 全部替换为 SGEP 原文摘抄 + SprintReview |
| `Scrum/sprint-03-design-sprint-restructure/` | Sprint 03：PBI-5 — Design Sprint 全书拆分为多文件体系 |

### 源参考

| 文件/目录 | 内容 |
|---|---|
| `references/scrum-guide-expanded-2025.6.md` | Scrum Guide Expanded 历史版本 (Jun 2025) |
| `references/scrum-on-one-page.md` | Scrum on One Page 概要 |
| `references/DesignSprint-HowtoSolveBigProblemsandTestJakeKnapp.docx` | *Design Sprint* 原始 Word 文档 |
| `references/DesignSprint-HowtoSolveBigProblemsandTestJakeKnapp.md` | *Design Sprint* — Jake Knapp 全书（含 111 张图片引用） |
| `references/IDEO-StanfordDesignGuides.docx` | IDEO / Stanford 原始 Word 文档 |
| `references/IDEO-StanfordDesignGuides.md` | IDEO / Stanford d.school 设计思维五模式指南（含 7 张图片引用） |
| `references/images/design-sprint/` | Design Sprint 配图（115 张，12 MB） |
| `references/images/ideo-design-guides/` | IDEO Design Guides 配图（9 张，8.8 MB） |

## 当前状态

2026-07-22：Sprint 01 完成——design-kernel（原 ideo-kernel）完成结构化改造：SKILL.md 重构为 Overview（IDEO + Design Sprint）+ Method Catalog 两层架构，五模式拆分为独立 IDEO-modes/ reference（WHAT/WHY/HOW + Transition），skill 更名为 design-kernel 与 scrum-kernel 对称。Sprint 02（PBI-3：agents SGEP 原文摘抄）已完成。Sprint 03（PBI-5：Design Sprint 内容重组）即将开始。PBI-2（output-styles）、PBI-4（description 审计）、PBI-6（删除 SGEP 内容）排队中。
