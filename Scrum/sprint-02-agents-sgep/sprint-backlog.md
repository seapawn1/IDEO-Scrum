# Sprint Backlog — Sprint 02

> 按 Scrum Guide Expanded v2026.1 的 Sprint Backlog artifact 框架定义。
> Product Owner: SeaPawn

---

## Sprint Goal

**scrum-kernel 的 6 个 role agent 从"skill 附属文档"升级为可独立发现的 Claude Code subagent，内容改回 SGEP 原文摘抄。**

> 相干 Product Goal：design-kernel 达到与 scrum-kernel 同等细致的结构化水平。

---

## What — 选中的 PBI

| # | 标题 | 用户故事 | Outcome Criteria | Acceptance Criteria | Size | 当前状态 | 备注 |
|---|---|---|---|---|---|---|---|
| PBI-3 | scrum-kernel agents 重构——移至插件 agents/ 目录 + 内容改回 SGEP 原文摘抄 | 作为 IDEO-Scrum 用户，我希望 scrum-kernel 的 6 个角色能够以真正的 subagent 形式被召唤（如 `/ideo-scrum:scrum-scrum-master`），并且每个 agent 的方法论内容直接摘抄 SGEP 原文而非经过改写，这样我能信任 agent 输出的是方法论原文、而非 agent 编写者的个人解读 | scrum-kernel 的 6 个角色从"skill 附属参考文档"升级为"可独立 spawn 的 Claude Code subagent"；用户召唤任一 role agent 后，其回答内容忠于 SGEP 原文、标注章节出处，不发生自创或释义性偏离 | ① `plugins/ideo-scrum/agents/` 目录创建，6 个 agent 从 `skills/scrum-kernel/agents/` 迁移至此；② 每个 agent body 的 Core Knowledge（方法论内容）替换为 SGEP `assets/scrum-guide-expanded-2026.1.md` 对应原文段落，保留引用标注（如 `[12-17]`）；③ 保留 agent frontmatter 中的 `name`、`description`、`model`、`color`、`tools` 字段；④ 保留并优化 `When to invoke`、`Guiding Principles`、`Output Format` 等行为层指令（这些是 agent 独有、SGEP 中没有的）；⑤ SKILL.md Reference Catalog 中 role agents 表更新为 scoped name（如 `ideo-scrum:scrum-scrum-master`）并标注为可 spawn agent 而非 reference 文档；⑥ 现有 PBI 不因此 PBI 而被阻塞 | L | 进行中 | SGEP 原文映射：Stakeholder L301-323，Supporter L325-329，AI L331-359，Product Developer L361-383，Product Owner L385-419，Scrum Master L421-488 |

---

## How — 工作计划

| # | 步骤 | 输入 | 输出 | 状态 |
|---|---|---|---|---|
| H-1 | 创建 `plugins/ideo-scrum/agents/` 目录，确认 Claude Code agent 自动发现路径 | 无 | `agents/` 目录就绪 | ⏳ 待开始 |
| H-2 | 重构 6 个 agent body — Core Knowledge 替换为 SGEP 原文摘抄，保留并优化行为层指令 | `skills/scrum-kernel/agents/*.md` + SGEP `assets/` 原文段 | 6 个新 agent（位于 `agents/`），body 分为：① SGEP 原文摘抄（标注行号引用）② When to invoke ③ Guiding Principles ④ Output Format | ⏳ 待开始 |
| H-3 | 更新 `scrum-kernel/SKILL.md` Reference Catalog — role agents 表改为 scoped name，标注为可 spawn agent | 当前 SKILL.md L35-53（Reference Catalog role agents 表） | 更新后的 SKILL.md，role agent 列改为 `agents/scrum-*.md → ideo-scrum:scrum-*` | ⏳ 待开始 |
| H-4 | 验证 — 确认 agent 可被 Claude Code 自动发现，scoped name 可被召唤 | `plugins/ideo-scrum/agents/` | 验证结果记录 | ⏳ 待开始 |
| | | | | |
