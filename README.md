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
| `.claude-plugin/marketplace.json` | Marketplace 清单 |
| `plugins/ideo-scrum/.claude-plugin/plugin.json` | 插件清单 |
| `plugins/ideo-scrum/skills/ideo-kernel/SKILL.md` | IDEO Design Thinking 技能内核 |
| `plugins/ideo-scrum/skills/ideo-kernel/methods/` | Design Thinking 方法库（~40 个方法） |
| `plugins/ideo-scrum/skills/scrum-kernel/SKILL.md` | Scrum Sprint 技能内核 |
| `Scrum/ProductBacklog.md` | 项目 Product Backlog |

## 当前状态

2026-07-22：方法论内核已包装为 marketplace 插件 `ideo-scrum@ideo-scrum`，包含 ideo-kernel 与 scrum-kernel 两个 skill。安装方式：`/plugin marketplace add <路径> --scope user` → `/plugin install ideo-scrum@ideo-scrum --scope user` → 开启 auto-update。
