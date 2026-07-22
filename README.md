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

### ideo-kernel skill

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/.claude-plugin/plugin.json` | 插件清单 |
| `plugins/ideo-scrum/skills/ideo-kernel/SKILL.md` | IDEO Design Thinking 技能内核（5 mode + Use Protocol + Method Catalog） |
| `plugins/ideo-scrum/skills/ideo-kernel/methods/` | Design Thinking 方法库（~40 个方法） |

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

2026-07-22：scrum-kernel 完成结构化改造——Scrum Guide Expanded 的 Artifacts 和 Events 章节已拆分为 9 个独立 reference 文档，6 个角色拆分为 agent，SKILL.md 作为入口通过 Reference Catalog 和目录表索引所有文件。ideo-kernel 保持原有结构。
