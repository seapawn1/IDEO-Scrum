# IDEO-Scrum

为 Claude Code 提供 Design Thinking 与 Scrum Sprint 方法论的插件。

## 这个仓库是什么

两层结构，改动前先分清在哪一层：

| 层 | 位置 | 性质 |
|---|---|---|
| **插件本体** | `plugins/ideo-scrum/` | 交付物。别人安装的就是这里 |
| **工作记录** | `scrum/` + `docs/` | 用本插件的方法论开发本插件的过程记录 |

`scrum/` 是**当前状态工作区**（产品日志）；`docs/` 放工作记录文档（如 ExpertNotes 客户之声）。1.x 的 sprint 日志是**历史记录**，教训已蒸馏入 `.claude/memory/`（原文 git 历史可追溯），不回改。除非发现事实错误，否则不要回头修改已完成 sprint 的内容。

## 当前状态（蒸馏锚点，随 Sprint 更新）

- **2026-08-31 · Sprint 06 收官（v2.0.0 已发布）**：本冲刺完成 PBI-16（双内核描述互链）、14-1/14-2/14-4 + 14-A（designer 重造回归）、15-B/15-C（DesignSprint 手术：五天法废弃、五阶段进 skill、decider→Product Owner、L18a 关闭）；**留待后续冲刺：15-D（scrum-kernel 重构）、14-B（developer/scrum-master 重构）、17（关键文档预先规格）、18（双内核执行模板）**；15-4 两机制点经 PO 定案不落文（定案存产品日志）；PBI-12（笔记）下一冲刺。分支 `sprint-06-dual-kernel-refactor` 已合入 main、tag v2.0.0、推送远端。详见 [../scrum/ProductBacklog.md](../scrum/ProductBacklog.md) 与 [../scrum/SprintBacklog.md](../scrum/SprintBacklog.md)。插件本体 v2.0.0。
- **1.x 已收官蒸馏**：旧目标（两内核结构对等）判定方向性错误，勿延续；教训见 `.claude/memory/`（MEMORY.md 索引 + 五期档案）。

## 维护规约

**README 是文件索引与当前状态，Git 历史负责追溯过去。**

- README 面向外部读者：只陈述这里是什么、文件地图、来源授权；作者侧的当前状态不入 README——由本文件「当前状态」锚点与 `scrum/ProductBacklog.md`（产品日志）承担
- 提交前确认 README 是否需要同步更新——尤其是新增/删除/重命名文件、改动插件版本号时
- 若发现 README 已过期、可能误导新会话的 LLM，必须显式提醒用户更新，不要默默放过
- 追溯旧决策、文件演变、阶段状态时，放手查阅 Git 历史

**版本号与 tag**

- 主干分支是 `main`，永远指向最新状态
- 版本号用 tag 标记，不写进分支名
- 插件版本号在 `plugins/ideo-scrum/.claude-plugin/plugin.json`，改动时 README 的两处版本号需同步

**组件描述（attribute description）规约**

写插件组件（skill / agent / output-style）的 `description` 时：它是**触发条件**，不是自我介绍——用 "Use when..." + 具体场景词；同类组件描述必须有区分度（模板趋同 = embedding 空间互相叠影，系统无法选择）。plugin.json 的 description 是元数据（展示用），非触发主战场。（来源：Sprint 04。）

**冲刺蒸馏闭环**

每期 Sprint 结束的 Review 阶段，本着"SprintBacklog 归西"的目的：AI 狠读冲刺日志 + 产品日志 → 写入四段式日志（Review 段写厚）→ 将教训/关键发现/变更**蒸馏**为一份记忆档案（30-50 行，带出处指向 git）存入 `.claude/memory/` → 删除 SprintBacklog 及中间产物。脚手架已拆、教训常在、原文 git 兜底。

> 三分工：**memory 管教训**（常驻、蒸馏过，见 `.claude/memory/MEMORY.md`），**git 管原文**（可查、完整），**`scrum/` 管现状**（产品日志、工作记录）。

**插件验证**

本仓库无 build/test。改动插件后，用 Agent 类型 `plugin-dev:plugin-validator` 校验插件结构/plugin.json；涉及 skill 质量时用 `plugin-dev:skill-reviewer`（两者经 Agent 工具调用，非 slash command）。marketplace 清单在 `.claude-plugin/marketplace.json`。

## 源材料与授权

插件内所有第三方摘录必须带署名。新增摘录时：

1. 文件顶部标注 `> Source:` 与 `> License:` 两行，License 须与 [../ATTRIBUTION.md](../ATTRIBUTION.md) 中记录的条款一致
2. 若引入新来源，先在 ATTRIBUTION.md 中登记，再写摘录

**已知的授权约束：**

- Scrum Guide 2020 / SGEP —— CC BY-SA 4.0，可摘录、可商用
- Stanford d.school Bootleg —— CC BY-**NC**-SA 4.0，含非商业限制
- 《Sprint》(Knapp) —— 全版权。**仅记录方法流程，不逐字摘录大段原文，不含书内插图**

`references/` 是源材料原件，**不入库**（`.gitignore` 已拦截），仅存于作者本地。

## 插件内容的自足性

插件会运行在别人的 Claude Code 里，那里没有本仓库的上下文，也没有作者的全局配置。

**写插件内容时，不要依赖任何未在插件内言明的约定。** 例如「用 mermaid 画图」必须同时说明方向（`flowchart TD`），否则在他人环境中行为不一致。
