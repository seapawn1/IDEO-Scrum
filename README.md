# IDEO-Scrum

为 Claude Code 提供 Design Thinking 与 Scrum Sprint 方法论的插件。

## 这里是什么

本插件将 Design Thinking（设计思维）和 Scrum Sprint（敏捷冲刺）两套方法论集成到 Claude Code 中，通过技能（skills）和输出样式（output-styles）提供结构化的协作流程。不做项目管理工具本身，不做 JIRA/Linear 集成，也不做团队协作平台——只提供方法论引导和流程框架。

## 文件地图

| 文件/目录 | 内容 |
|---|---|
| `.gitignore` | Git 忽略规则 |
| `.env` | 本地私人环境 |
| `seapawn.md` | 本地私人笔记 |
| `resources/ideo-kernel/SKILL.md` | IDEO Design Thinking 技能内核 |
| `resources/ideo-kernel/methods/` | Design Thinking 方法库（~40 个方法） |
| `resources/scrum-kernel/SKILL.md` | Scrum Sprint 技能内核 |

## 当前状态

2026-07-22：方法论内核已引入——Design Thinking（IDEO 五模式 + 方法库）与 Scrum Sprint（Scrum Guide 原文），配置 ai-partner 输出样式。待开发面向用户的 skill 入口。
