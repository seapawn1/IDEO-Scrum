---
name: sprint-02-agents-sgep
description: Sprint 02 日志全文——PBI-3：6 个 scrum role agent 替换为 SGEP 原文摘抄；worktree 写入坑；做 A 顺便做 B 模式
metadata:
  type: project
---

# 冲刺日志 — Sprint 02（agents-sgep）

> 按 Scrum Guide Expanded v2026.1 的 Sprint Backlog / Sprint Review artifact 框架定义。
> Product Owner: SeaPawn · Sprint 02 · 2026-07-22

## Goal-why

### Sprint Goal

将 6 个 scrum role agent 的方法论内容替换为 SGEP v2026.1 原文直接摘抄。 ✅ 达成

> 相干 Product Goal：design-kernel 达到与 scrum-kernel 同等细致的结构化水平。

### Definition of Output Done

> 照抄产品级增量 DoD（Increment 的承诺；**Outcome Done 不抄**——产品级价值证据归产品日志）。

| 维度 | 标准 |
|---|---|
| 内容忠实 | 忠于源材料（SGEP / d.school / Sprint）；方法论设计部分（融合、solo+AI）标注来源与依据 |
| 可导航 | 从 SKILL.md 入口 ≤2 跳到达任意 reference / 角色 agent |
| 无死链 | 所有 markdown 内部链接可解析，无 404 |

## PBI-what

### 选中的 PBI

| # | 标题 | 用户故事 | Outcome Criteria | Size | 当前状态 | 备注 |
|---|---|---|---|---|---|---|
| PBI-3 | scrum-kernel agents 重构——移至插件 agents/ 目录 + 内容改回 SGEP 原文摘抄 | 作为 IDEO-Scrum 用户，我希望 scrum-kernel 的 6 个角色能够以真正的 subagent 形式被召唤（如 `/ideo-scrum:scrum-scrum-master`），并且每个 agent 的方法论内容直接摘抄 SGEP 原文而非经过改写，这样我能信任 agent 输出的是方法论原文、而非 agent 编写者的个人解读 | scrum-kernel 的 6 个角色从"skill 附属参考文档"升级为"可独立 spawn 的 Claude Code subagent"；用户召唤任一 role agent 后，其回答内容忠于 SGEP 原文、标注章节出处，不发生自创或释义性偏离 | L | 已完成 | Sprint 02 交付：6 个 agent 全部重写为 SGEP 原文摘抄（266 行总计），SGEP Roles 拆分至 references/scrum-roles.md |

### 细化

原 Sprint 未制定 How 计划；实际执行分解（自 Review 反推）：

| # | 步骤 | 输出 | 状态 |
|---|---|---|---|
| 1 | 6 个 agent body 逐个体替换为 SGEP 原文摘抄（统一三段结构：frontmatter / behavioral summary / `## SGEP v2026.1 — Role`） | `agents/*.md`（266 行总计） | ✅ |
| 2 | SGEP Roles 章节拆分（涌现需求） | `references/scrum-roles.md` | ✅ |
| 3 | SKILL.md Reference Catalog 校正与索引更新 | `SKILL.md` | ✅ |

## Developer-how

### 执行总结

原计划为"移入插件 `agents/` 目录 + 内容改回 SGEP 摘抄"，执行中有三项关键修正：

1. **位置决策反转**：agent 从"移动到 `plugins/ideo-scrum/agents/`"改为"留在 `skills/scrum-kernel/agents/`"——移到插件层会脱离 SKILL.md 的索引上下文，破坏内聚性。
2. **顺势拆分**：SGEP Roles 章节拆到 `references/scrum-roles.md` 是执行中涌现的需求（做 A 时顺便做 B，单人团队有效模式）。
3. **Worktree 踩坑**：Sprint 02 在 worktree 中工作导致文件写入位置混乱，后续 Sprint 直接在主分支更可靠。

结果落点：6 个 agent（统一三段结构 + `[12-17]` 内联引用保留）+ `references/scrum-roles.md` + SKILL.md 索引更新——见 Review。

## Review

### Increment Delivered

| Output | Path | Status |
|---|---|---|
| 6 个 agent SGEP 原文摘抄 | `plugins/ideo-scrum/skills/scrum-kernel/agents/*.md` | 交付——每个 agent body 替换为 `## SGEP v2026.1 — Role (L范围)` 段，原文直接摘抄，内联引用保留 |
| scrum-roles 参考文档 | `references/scrum-roles.md` | 额外交付——SGEP Roles 章节拆分为独立 reference |
| SKILL.md Reference Catalog 更新 | `SKILL.md` | SGEP Source 行校正、scrum-roles 索引、Source Document 节合并 |

### Sprint Goal Assessment

> **Sprint Goal:** 将 6 个 scrum role agent 的方法论内容替换为 SGEP v2026.1 原文直接摘抄。

**达成。** 6/6 agent 完成，每个统一结构：

- Frontmatter → 保留
- 一句话 behavioral summary（agent 特有，非 SGEP）
- `## SGEP v2026.1 — Role (行号范围)` → 全文摘抄，`[12-17]` 等引用标记保留

### Definition of Done Check

#### Output Done

| 维度 | 状态 | 备注 |
|---|---|---|
| 内容忠实 | ✅ | 每个 agent body 与 SGEP 原文逐段一致 |
| 溯源合规 | ✅ | SGEP 行号标注 + 内联引用保留 |
| 结构一致 | ✅ | 6 个 agent 统一结构 |
| 无死链 | ✅ | |
| 可导航 | ✅ | SKILL.md Reference Catalog 角色表路径正确 |
| 语言分明 | ✅ | SGEP 原文英文，项目文档中文 |

### Lessons Learned

1. **Agent 留在 skill 目录是对的。** 最初计划移到 `plugins/ideo-scrum/agents/`，但这样 agent 脱离了 SKILL.md 的上下文。留在 `skills/scrum-kernel/agents/` 保持了内聚性。
2. **SGEP 拆分顺势做了。** SGEP Roles 章节拆到 `references/scrum-roles.md` 是过程中涌现的需求，不是原计划的一部分。这种"做 A 时顺便做 B"的模式在单人团队中有效。
3. **Worktree 踩坑。** Sprint 02 的 worktree 导致文件写入位置混乱。后续 Sprint 直接在主分支工作更可靠。

### Product Backlog Adaptations

- PBI-3 标记完成，备注更新为实际交付内容
- PBI-5（Sprint 03）排队中
