# IDEO-Scrum

为 Claude Code 与 Codex 提供 Design Thinking 与 Scrum Sprint 方法论的插件。v5.1.2。

## 快速开始

### Claude Code

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

也可以显式进入某个角色工作（角色注入当前对话，不影响其他对话）：

```
/ideo-scrum:scrum-master     # Scrum Master：三大支柱、五项价值观、仪式优先
/ideo-scrum:designer         # Designer：设计结对——IDEO 五模式 + 设计冲刺，原型快速验证
/ideo-scrum:developer        # Developer：Sprint Backlog、DoD、Review、Retro
/ideo-scrum:stakeholder      # Stakeholder：一个命令多种身份——外部视角，或常驻做非源码杂务；源码归 Developer
```

### Codex

在终端中安装：

```
codex plugin marketplace add seapawn1/IDEO-Scrum
codex plugin add ideo-scrum@ideo-scrum
```

如果以前通过 `--ref codex` 从旧 `codex` 分支安装过 3.2.0，先移除旧插件和 marketplace 注册，再按默认分支重新注册并安装：

```
codex plugin remove ideo-scrum@ideo-scrum
codex plugin marketplace remove ideo-scrum
codex plugin marketplace add seapawn1/IDEO-Scrum
codex plugin add ideo-scrum@ideo-scrum
```

随后在新会话输入 `$`，从技能菜单选中相应角色；角色简称如下：

```
$scrum-master   # Scrum Master
$designer       # Designer
$developer      # Developer
$stakeholder    # Stakeholder
```

三个内核的设置允许 Codex 自动调用；四个角色的设置要求显式选择。它们和 Claude Code 版使用同一份源内容。需要区分同名技能时，可用插件命名空间，例如 `$ideo-scrum:developer`。

**插件提供什么**

| 组件 | 内容 |
|---|---|
| `ideo-kernel` skill | IDEO / d.school 五模式（Empathize → Test）、~40 个设计方法——整个插件共用的工具箱，也是设计各阶段的基础 |
| `design-kernel` skill | 设计冲刺：按 IDEO 五阶段（共情、定义、构思、原型、测试）组织的《Sprint》原文摘录，加设计日志约定与模板；设计与冲刺平级，结论回流产品日志 |
| `scrum-kernel` skill | Scrum Guide 2020 全文、SGEP 扩展包全文（含角色章）、Artifact / Event 分项引用 |
| 4 个角色 | Scrum Master / Designer / Developer / Stakeholder。Claude Code 用四个 command（如 `/ideo-scrum:scrum-master`）；Codex 用四个角色 skill，从 `$` 菜单显式选择。角色入口要求先加载对应内核（都先加载 ideo-kernel） |

## 这里是什么

本插件将 Design Thinking（设计思维）和 Scrum Sprint（敏捷冲刺）两套方法论提供给 Claude Code 与 Codex：Claude Code 使用技能（skills）和斜杠命令（commands），Codex 中全部是技能（skills），共同提供结构化的协作流程。不做项目管理工具本身，不做 JIRA/Linear 集成，也不做团队协作平台——只提供方法论引导和流程框架。

## 文件地图

### 根目录

| 文件/目录 | 内容 |
|---|---|
| `LICENSE` | MIT — 覆盖本仓库原创部分 |
| `ATTRIBUTION.md` | 四个第三方来源的完整署名与授权条款 |
| `.claude-plugin/marketplace.json` | marketplace 清单，供 `/plugin marketplace add` 使用 |
| `.agents/plugins/marketplace.json` | Codex marketplace 清单，指向同一分支里的 Codex 分发包 |
| `scripts/sync_codex.py` | 从 Claude Code 源文件生成 Codex 包：`python scripts/sync_codex.py` |
| `scripts/check_codex.py` | 核对 Codex 内容一致性、内部链接、导航与重复生成；需要 PyYAML |
| `.claude/` | 项目配置——`settings.json`、`seapawn.md`（作者待办与私人笔记，不入库）；项目指令 `CLAUDE.md` 在仓库根目录，记忆在仓库外 `S:\SeaPawn-Memory\memory\IDEO-Scrum\` |

### Claude Code 插件

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/.claude-plugin/plugin.json` | 插件清单 v5.1.2 |
| `plugins/ideo-scrum/commands/designer.md` | Command `/ideo-scrum:designer` — 设计阶段结对（IDEO 五模式 + 设计冲刺，原型快速验证、拍板前不落地；进入时加载 ideo-kernel 与 design-kernel） |
| `plugins/ideo-scrum/commands/developer.md` | Command `/ideo-scrum:developer` — Developer 角色（Scrum Guide 2020 原文抄录＋2026 精炼补充；进入时加载 ideo-kernel 与 scrum-kernel） |
| `plugins/ideo-scrum/commands/scrum-master.md` | Command `/ideo-scrum:scrum-master` — Scrum Master 角色（Scrum Guide 2020 原文抄录＋2026 精炼补充；替 PO 派活、派子代理审阅；进入时加载三个内核） |
| `plugins/ideo-scrum/commands/stakeholder.md` | Command `/ideo-scrum:stakeholder` — Stakeholder（SGEP 角色章为底；一个命令多种身份：外部视角——按项目写定的身份看产品和增量，说出期望与现状的差距，反馈交 PO，独立评价由全新子代理给；也可作常驻会话做非源码杂务，如维护看板；源码归 Developer；进入时加载 ideo-kernel） |

### Codex 分发包

`codex/plugins/ideo-scrum/` 由 `python scripts/sync_codex.py` 生成，版本取 Claude Code 插件清单。修改三个内核或角色时，先改 `plugins/ideo-scrum/`，再运行同步命令；生成包中的工具用语适配由脚本统一处理。

| 文件/目录 | 内容 |
|---|---|
| `codex/plugins/ideo-scrum/.codex-plugin/plugin.json` | Codex 插件清单 |
| `codex/plugins/ideo-scrum/skills/ideo-kernel/`、`design-kernel/`、`scrum-kernel/` | 三个内核的全部文件，含约定、模板和源材料 |
| `codex/plugins/ideo-scrum/skills/scrum-master/`、`designer/`、`developer/`、`stakeholder/` | 四个原生角色 skill；各有 SKILL.md 和 agents/openai.yaml |
| `codex/plugins/ideo-scrum/README.md`、`LICENSE`、`ATTRIBUTION.md` | 包内说明及来源授权 |
| `scripts/codex_interface.json`、`scripts/codex_readme.md` | Codex 展示文字与包内 README 的生成源 |

### design-kernel skill

> `design-kernel` 是 v3 用过的名字（当时指设计冲刺与 IDEO 合在一起的内核，v4 改名 ideo-kernel）；v5 起重新启用，意思变了：专讲设计冲刺，IDEO 五模式与方法库留在 ideo-kernel。

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/skills/design-kernel/SKILL.md` | Design Kernel 入口（设计冲刺按 IDEO 五阶段组织：每个阶段对应的 IDEO 模式、原书摘录、Use Protocol） |
| `plugins/ideo-scrum/skills/design-kernel/` 下 `empathize/`、`define/`、`ideate/`、`prototype/`、`test/` | 设计冲刺原书摘录（Knapp，原文只删不改，例图改画成 Mermaid 或文字）：共情 define-the-challenge / start-at-the-end / ask-the-experts；定义 make-a-map / how-might-we / pick-a-target；构思 remix-and-improve / sketch / decide / rumble / storyboard；原型 fake-it / prototype；测试 small-data / interview / learn |
| `plugins/ideo-scrum/skills/design-kernel/conventions/` | 设计日志约定 v1（design-log：设计放哪、谁定、各阶段怎么用子代理与角色卡、收官）与设计日志模板（design-backlog-template，五章） |

### ideo-kernel skill

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/skills/ideo-kernel/SKILL.md` | IDEO Kernel 入口（整个插件共用的工具箱：IDEO 五模式表 + Method Catalog：按模式索引与合表 + Use Protocol） |
| `plugins/ideo-scrum/skills/ideo-kernel/IDEO-modes/` | IDEO Design Thinking 五模式 reference（Empathize / Define / Ideate / Prototype / Test，各含 WHAT/WHY/HOW + Transition） |
| `plugins/ideo-scrum/skills/ideo-kernel/methods/` | Design Thinking 方法库（~40 个方法，含 Use Before / Use Notes / Do Not Use When） |

### scrum-kernel skill

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/skills/scrum-kernel/SKILL.md` | Scrum Sprint 技能内核（Scrum Guide 概述 + Artifact / Event / Reference 目录表） |
| `plugins/ideo-scrum/skills/scrum-kernel/scrum-guide-2020.md` | Scrum Guide 2020 官方全文 |
| `plugins/ideo-scrum/skills/scrum-kernel/assets/scrum-guide-expansion-pack-2026.1.md` | SGEP 完整源文档（Theory / Values-OODA / Roles / 引用列表） |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-*.md` | 4 个 Artifact reference：Product / Increment / Product Backlog / Sprint Backlog |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-event-*.md` | 5 个 Event reference：Sprint / Sprint Planning / Daily Scrum / Sprint Review / Sprint Retrospective |
| `plugins/ideo-scrum/skills/scrum-kernel/overview.md` | 约定总览 v1（与 SKILL.md 并列）：三层、文件与文档文件夹、角色、会话分工、目标不变其余可调、与官方故意不同之处 |
| `plugins/ideo-scrum/skills/scrum-kernel/conventions/` | 约定 v1：product-log 与 product-backlog-template（产品日志）；sprint-log 与 sprint-backlog-template（冲刺日志） |

### 工作记录（scrum/）

| 文件/目录 | 内容 |
|---|---|
| `scrum/ProductBacklog.md` | 产品日志——一 Product / Product Goal / DoD；二 利益相关者表与 Map（流程见插件 scrum-kernel 的 conventions/）；三 PBI（3.1 当前、3.2 已完成附出处） |
| `scrum/documents/ExpertNotes.md` | 客户之声——作者使用流程已口述落盘（项目骨架→IDEO→design 文件→背景研究→target 四阶段，含与 SprintBacklog 同源表、分工原则、未决清单）；将作为方法论分享的素材 |
| `scrum/documents/PBI-27-bot-research.md` | Bot 工作方式研究（PBI-27）：Grok Bot、DeepSeekBot（pstack）、DS-Bot 等的可借鉴机制，带出处 |
| `scrum/documents/five-stage-mapping.svg` | Scrum 三阶段与 IDEO 五模式的对应图（2026-11-06，ExpertNotes 附录用） |
| `scrum/documents/sprint-08-design-kernel.md` | Sprint 08 冲刺日志归档（设计内核独立，v5.0.0）：关键决定、触发回归、审查与 Review |
| `scrum/documents/sprint-09-design-template.md` | Sprint 09 冲刺日志归档（设计日志模板改正，小冲刺，v5.0.1） |
| `scrum/documents/sprint-10-conventions.md` | Sprint 10 冲刺日志归档（流程全部进插件，v5.1.0）：关键决定、三轮测试、审查与 Review |
| `scrum/documents/conventions-review-log.md` | PO 逐段审阅约定 v1 的记录（2026-11-09，19 处，每条带状态）；当时对照的四份中文译文已删，见 `git show 6a2fd5e` |
| `scrum/documents/sprint-11-conventions-review.md` | Sprint 11 冲刺日志归档（约定照 PO 审阅改定，小冲刺，v5.1.1）：19 处的结论、审阅、design-log 读着别扭的地方 |
| `scrum/documents/sprint-12-overview-to-root.md` | Sprint 12 冲刺日志归档（总览挪到 scrum-kernel 根目录，小冲刺，v5.1.2） |
| **冲刺蒸馏 / 归档** | 1.x 五期与 Sprint 06、07 已蒸馏至 `S:\SeaPawn-Memory\memory\IDEO-Scrum\`（MEMORY.md 索引 + 各期教训档案，含出处指向 git）；Sprint 08 起，冲刺日志压缩后归档进 `scrum/documents/` |

### 源参考

原始源材料（书籍原件、扫描配图等）**不入库**，仅保留在作者本地。插件内的所有摘录均带章节级署名，来源与授权条款见 [ATTRIBUTION.md](ATTRIBUTION.md)。

## 来源与授权

本仓库的**原创部分**（插件结构、skill 组织、工作记录 `scrum/`）以 [MIT](LICENSE) 发布。

插件内的方法论摘录来自四个外部来源，各自的许可条款不同：

| 来源 | 许可 |
|---|---|
| The Scrum Guide 2020 | CC BY-SA 4.0 |
| Scrum Guide Expansion Pack 2026.1 | CC BY-SA 4.0 |
| Stanford d.school Design Thinking Bootleg | CC BY-**NC**-SA 4.0 |
| *Sprint* (Knapp et al., 2016) | 全版权，仅记录方法流程 |

> ⚠️ 第三项含**非商业限制**，因此本仓库整体**不构成 OSI 定义下的开源软件**。商业场景使用前请阅读 [ATTRIBUTION.md](ATTRIBUTION.md)。

本仓库不包含任何书籍全文或原始出版物。若这些方法论对你有价值，请通过官方渠道支持原作者。
