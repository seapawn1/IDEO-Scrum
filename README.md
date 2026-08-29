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

### 工作记录层（docs/）

| 文件/目录 | 内容 |
|---|---|
| `docs/README.md` | 本目录的文件索引与当前状态（一层索引） |
| `docs/ProductBacklog.md` | 产品日志——Product 定义 / Vision / Architecture（待补）/ DoD（草案）/ v2.0.0 PBI 序列 / Review 1.x 收官 |
| `docs/Design.md` | v2.0.0 验证轮设计地图——Challenge / Goal / Q1-Q3；Map 待专家会议后绘制 |
| `docs/ExpertNotes.md` | 客户之声——作者作为插件真实用户的使用流程与感悟（骨架，待口述填充） |
| `Scrum/sprint-01-skill-stanford/` ~ `sprint-05-pbi2-output-styles/` | Sprint 01-05 日志（PBI-1~5）——已迁出至 `.claude/memory/`（MEMORY.md 详细索引 + 五期全文档）；git 历史可追溯原文 |

> 五期冲刺日志全文（`SprintBacklog.md`，四段式：Goal-why / PBI-what / Developer-how / Review）已迁入 `.claude/memory/`。

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

2026-08-30：**v2.0.0 新轨**。1.x 的 Product Goal（结构对等）判定为方向性错误（详见 [docs/ProductBacklog.md](docs/ProductBacklog.md) 修订记录）。插件仍为 v1.0.2；v2.0.0 PBI 序列（PBI-7~11）已立项为草案，PBI-7（ideo 与 Design Sprint 融合重构）前置 Design Sprint 验证轮。工作层已重整：产品三件套合并为 `ProductBacklog.md`，五期冲刺日志归一为四段式 `SprintBacklog.md`（已迁入 `.claude/memory/`）。

v1.0.2（2026-08-03）：5 个 Sprint 完成——插件具备完整的两套方法论体系（IDEO Design Thinking + Scrum Sprint），含 skills、agents、output-styles、method catalog。Design Sprint 五天流程中 Monday 已结构化完成，周二至五发现方法论分化。

v1.0.0 之后的增量：删除设计冲刺知识代理文档（v1.0.1）；output-style `agent-designer` 更名 `designer`，Monday 流程中 Map 提前至 Ask the Experts 之前、`POV and HMW` 收敛为 `HMW`（v1.0.2）。

### Product Backlog 概览

| # | 标题 | 状态 |
|---|---|---|
| PBI-1 | 细化 design-kernel SKILL.md — 融合 Stanford Design Guides | ✅ Sprint 01 |
| PBI-2 | 插件新增 output-styles | ✅ Sprint 05 |
| PBI-3 | scrum-kernel agents 重构——SGEP 原文摘抄 | ✅ Sprint 02 |
| PBI-4 | 细化插件所有 description 字段 | ✅ Sprint 04 |
| PBI-5 | 重组 Design Sprint 内容结构 | ✅ Sprint 03（剩余范围并入 PBI-7） |
| PBI-6 | Design Sprint Tuesday-Friday 细化——solo+AI 方法论设计 | 已并入 PBI-7（五天法废弃） |
| PBI-7 | ideo 与 Design Sprint 融合重构 | ⏳ 待开始（前置 Design Sprint 验证轮） |
| PBI-8 | 角色体系重构 | ⏳ 待开始 |
| PBI-9 | 双内核联动 | ⏳ 待开始 |
| PBI-10 | designer output-style 重写 | ⏳ 待开始 |
| PBI-11 | 方法论感悟背景文档 | ⏳ 待开始 |

> 详细定义见 [docs/ProductBacklog.md](docs/ProductBacklog.md)。
