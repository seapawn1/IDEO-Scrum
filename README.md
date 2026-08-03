# IDEO-Scrum

为 Claude Code 提供 Design Thinking 与 Scrum Sprint 方法论的插件。v1.0.2。

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
/output-style designer         # 设计结对：IDEO 五模式，先发散后收敛
/output-style developer        # Developer：Sprint Backlog、DoD、Review、Retro
```

**插件提供什么**

| 组件 | 内容 |
|---|---|
| `design-kernel` skill | IDEO / d.school 五模式（Empathize → Test）、~40 个设计方法、Design Sprint 五天流程 |
| `scrum-kernel` skill | Scrum Guide 2020 全文、Artifact 与 Event 的分项引用、6 个 Scrum 角色 agent |
| 3 个 output-style | Scrum Master / Designer / Developer 三种工作视角 |

## 这里是什么

本插件将 Design Thinking（设计思维）和 Scrum Sprint（敏捷冲刺）两套方法论集成到 Claude Code 中，通过技能（skills）、角色代理（agents）和输出样式（output-styles）提供结构化的协作流程。不做项目管理工具本身，不做 JIRA/Linear 集成，也不做团队协作平台——只提供方法论引导和流程框架。

## 文件地图

### 根目录

| 文件/目录 | 内容 |
|---|---|
| `LICENSE` | MIT — 覆盖本仓库原创部分 |
| `ATTRIBUTION.md` | 四个第三方来源的完整署名与授权条款 |
| `.claude-plugin/marketplace.json` | marketplace 清单，供 `/plugin marketplace add` 使用 |

### 插件

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/.claude-plugin/plugin.json` | 插件清单 v1.0.2 |
| `plugins/ideo-scrum/output-styles/designer.md` | Output-style — agent 设计结对（IDEO 五模式，先发散后收敛） |
| `plugins/ideo-scrum/output-styles/developer.md` | Output-style — Developer 角色（Sprint Backlog / DoD / Sprint Review / Retro） |
| `plugins/ideo-scrum/output-styles/scrum-master.md` | Output-style — Scrum Master 角色（三大支柱 / 五项价值观 / 仪式优先） |

### design-kernel skill

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/skills/design-kernel/SKILL.md` | Design Kernel 入口（IDEO 五模式表 + Design Sprint 单行引用 + Method Catalog + Use Protocol） |
| `plugins/ideo-scrum/skills/design-kernel/IDEO-modes/` | IDEO Design Thinking 五模式 reference（Empathize / Define / Ideate / Prototype / Test，各含 WHAT/WHY/HOW + Transition） |
| `plugins/ideo-scrum/skills/design-kernel/methods/` | Design Thinking 方法库（~40 个方法，含 Use Before / Use Notes / Do Not Use When） |
| `plugins/ideo-scrum/skills/design-kernel/DesignSprint/design-sprint.md` | Design Sprint 五天入口（Monday checklist 完整，引用 `references/`；Tuesday-Friday 待 PBI-6 重构） |
| `plugins/ideo-scrum/skills/design-kernel/DesignSprint/references/` | Monday 6 个引用文件：define-the-challenge / start-at-the-end / make-a-map / ask-the-experts / how-might-we / pick-a-target |

### scrum-kernel skill

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/skills/scrum-kernel/SKILL.md` | Scrum Sprint 技能内核（Scrum Guide 概述 + Artifact/Event 目录表 + Role Agent 列表） |
| `plugins/ideo-scrum/skills/scrum-kernel/scrum-guide-2020.md` | Scrum Guide 2020 官方全文 |
| `plugins/ideo-scrum/skills/scrum-kernel/agents/` | 6 个 Scrum 角色 agent（PO / SM / PD / Stakeholder / Supporter / AI，SGEP 原文摘抄） |
| `plugins/ideo-scrum/skills/scrum-kernel/assets/scrum-guide-expansion-pack-2026.1.md` | SGEP 完整源文档（Theory / Values-OODA / Roles / 引用列表） |
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

原始源材料（书籍原件、扫描配图等）**不入库**，仅保留在作者本地。插件内的所有摘录均带章节级署名，来源与授权条款见 [ATTRIBUTION.md](ATTRIBUTION.md)。

## 来源与授权

本仓库的**原创部分**（插件结构、skill 组织、Scrum 工作记录）以 [MIT](LICENSE) 发布。

插件内的方法论摘录来自四个外部来源，各自的许可条款不同：

| 来源 | 许可 |
|---|---|
| The Scrum Guide 2020 | CC BY-SA 4.0 |
| Scrum Guide Expansion Pack 2026.1 | CC BY-SA 4.0 |
| Stanford d.school Design Thinking Bootleg | CC BY-**NC**-SA 4.0 |
| *Sprint* (Knapp et al., 2016) | 全版权，仅记录方法流程 |

> ⚠️ 第三项含**非商业限制**，因此本仓库整体**不构成 OSI 定义下的开源软件**。商业场景使用前请阅读 [ATTRIBUTION.md](ATTRIBUTION.md)。

本仓库不包含任何书籍全文或原始出版物。若这些方法论对你有价值，请通过官方渠道支持原作者。

## 当前状态

2026-08-03：v1.0.2。5 个 Sprint 完成——插件具备完整的两套方法论体系（IDEO Design Thinking + Scrum Sprint），含 skills、agents、output-styles、method catalog。Design Sprint 五天流程中 Monday 已结构化完成，Tuesday-Friday 待 PBI-6（solo+AI 方法论设计）。

v1.0.0 之后的增量：删除设计冲刺知识代理文档（v1.0.1）；output-style `agent-designer` 更名 `designer`，Monday 流程中 Map 提前至 Ask the Experts 之前、`POV and HMW` 收敛为 `HMW`（v1.0.2）。

### Product Backlog 概览

| # | 标题 | Size | 状态 |
|---|---|---|---|
| PBI-1 | 细化 design-kernel SKILL.md — 融合 Stanford Design Guides | L | ✅ Sprint 01 |
| PBI-2 | 插件新增 output-styles | M | ✅ Sprint 05 |
| PBI-3 | scrum-kernel agents 重构——SGEP 原文摘抄 | L | ✅ Sprint 02 |
| PBI-4 | 细化插件所有 description 字段 | S | ✅ Sprint 04 |
| PBI-5 | 重组 Design Sprint 内容结构 | — | ◐ Sprint 03 |
| PBI-6 | Design Sprint Tuesday-Friday 细化——solo+AI 方法论设计 | L | ⏳ |
