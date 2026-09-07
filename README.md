# IDEO-Scrum

为 Claude Code 提供 Design Thinking 与 Scrum Sprint 方法论的插件。v2.0.1。

## 快速开始

在 Claude Code 会话中安装：

```
/plugin marketplace add seapawn1/IDEO-Scrum
/plugin install ideo-scrum@ideo-scrum
/reload-plugins
```

装好后不需要记任何命令——描述你在做的事，相关方法论会自动介入：

```
帮我规划下个 Sprint，我们有 5 个待办项要排优先级
```
```
这个功能要不要做我拿不准，先做一轮用户访谈的设计
```

也可以显式切换到某个角色视角工作：

```
/output-style scrum-master     # Scrum Master：三大支柱、五项价值观、仪式优先
/output-style designer         # Designer：设计结对——IDEO 五模式 + 设计冲刺，原型快速验证
/output-style developer        # Developer：Sprint Backlog、DoD、Review、Retro
```

**插件提供什么**

| 组件 | 内容 |
|---|---|
| `design-kernel` skill | IDEO / d.school 五模式（Empathize → Test）、~40 个设计方法、设计冲刺五阶段（快速锁定目标，为 Scrum 铺垫） |
| `scrum-kernel` skill | Scrum Guide 2020 全文、SGEP 扩展包全文、Artifact / Event / Roles 分项引用 |
| 3 个 output-style | Scrum Master / Designer / Developer 三种工作视角 |

## 这里是什么

本插件将 Design Thinking（设计思维）和 Scrum Sprint（敏捷冲刺）两套方法论集成到 Claude Code 中，通过技能（skills）和输出样式（output-styles）提供结构化的协作流程。不做项目管理工具本身，不做 JIRA/Linear 集成，也不做团队协作平台——只提供方法论引导和流程框架。

## 文件地图

### 根目录

| 文件/目录 | 内容 |
|---|---|
| `LICENSE` | MIT — 覆盖本仓库原创部分 |
| `ATTRIBUTION.md` | 四个第三方来源的完整署名与授权条款 |
| `.claude-plugin/marketplace.json` | marketplace 清单，供 `/plugin marketplace add` 使用 |
| `.claude/` | 项目配置——`CLAUDE.md`（项目指令，随会话加载）、`memory/`（蒸馏档案 + MEMORY.md 索引）、`settings.json` |

### 插件

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/.claude-plugin/plugin.json` | 插件清单 v2.0.1 |
| `plugins/ideo-scrum/output-styles/designer.md` | Output-style — 设计阶段结对（IDEO 五模式 + 设计冲刺，原型快速验证、拍板前不落地） |
| `plugins/ideo-scrum/output-styles/developer.md` | Output-style — Developer 角色（Sprint Backlog / DoD / Sprint Review / Retro） |
| `plugins/ideo-scrum/output-styles/scrum-master.md` | Output-style — Scrum Master 角色（三大支柱 / 五项价值观 / 仪式优先） |

### design-kernel skill

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/skills/design-kernel/SKILL.md` | Design Kernel 入口（IDEO 五模式表 + 设计冲刺：定位/文件表/五阶段表 + Method Catalog + Use Protocol） |
| `plugins/ideo-scrum/skills/design-kernel/IDEO-modes/` | IDEO Design Thinking 五模式 reference（Empathize / Define / Ideate / Prototype / Test，各含 WHAT/WHY/HOW + Transition）；另含设计冲刺 5 阶段参考（Knapp 摘录：define-the-challenge / start-at-the-end / ask-the-experts / make-a-map / pick-a-target） |
| `plugins/ideo-scrum/skills/design-kernel/methods/` | Design Thinking 方法库（~40 个方法，含 Use Before / Use Notes / Do Not Use When） |

### scrum-kernel skill

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/skills/scrum-kernel/SKILL.md` | Scrum Sprint 技能内核（Scrum Guide 概述 + Artifact / Event / Reference 目录表） |
| `plugins/ideo-scrum/skills/scrum-kernel/scrum-guide-2020.md` | Scrum Guide 2020 官方全文 |
| `plugins/ideo-scrum/skills/scrum-kernel/assets/scrum-guide-expansion-pack-2026.1.md` | SGEP 完整源文档（Theory / Values-OODA / Roles / 引用列表） |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-*.md` | 4 个 Artifact reference：Product / Increment / Product Backlog / Sprint Backlog |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-event-*.md` | 5 个 Event reference：Sprint / Sprint Planning / Daily Scrum / Sprint Review / Sprint Retrospective |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-roles.md` | Scrum Roles 规范（SGEP 角色节摘录） |

### 工作记录（scrum/ + docs/）

| 文件/目录 | 内容 |
|---|---|
| `scrum/ProductBacklog.md` | 产品日志——Product 定义 / Vision / DoD / v2.0.0 PBI 序列（PBI-12~18）/ Architecture（草案大节，据验证轮客户之声抽象） |
| `scrum/SprintBacklog.md` | Sprint 06 冲刺日志（Sprint Goal + DoD / PBI+验收标准 / How 区）——Review 后按蒸馏闭环删除 |
| `docs/ExpertNotes.md` | 客户之声——作者使用流程已口述落盘（项目骨架→IDEO→design 文件→背景研究→target 四阶段，含与 SprintBacklog 同源表、分工原则、未决清单）；感悟待写 |
| **五期冲刺蒸馏** | 已蒸馏至 `.claude/memory/`（MEMORY.md 索引 + 五期教训档案，含出处指向 git）；原文 git 历史可追溯 |

### 源参考

原始源材料（书籍原件、扫描配图等）**不入库**，仅保留在作者本地。插件内的所有摘录均带章节级署名，来源与授权条款见 [ATTRIBUTION.md](ATTRIBUTION.md)。

## 来源与授权

本仓库的**原创部分**（插件结构、skill 组织、工作记录 `scrum/` + `docs/`）以 [MIT](LICENSE) 发布。

插件内的方法论摘录来自四个外部来源，各自的许可条款不同：

| 来源 | 许可 |
|---|---|
| The Scrum Guide 2020 | CC BY-SA 4.0 |
| Scrum Guide Expansion Pack 2026.1 | CC BY-SA 4.0 |
| Stanford d.school Design Thinking Bootleg | CC BY-**NC**-SA 4.0 |
| *Sprint* (Knapp et al., 2016) | 全版权，仅记录方法流程 |

> ⚠️ 第三项含**非商业限制**，因此本仓库整体**不构成 OSI 定义下的开源软件**。商业场景使用前请阅读 [ATTRIBUTION.md](ATTRIBUTION.md)。

本仓库不包含任何书籍全文或原始出版物。若这些方法论对你有价值，请通过官方渠道支持原作者。
