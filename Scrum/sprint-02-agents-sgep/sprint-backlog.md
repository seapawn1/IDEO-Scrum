# Sprint Backlog — Sprint 02

> 按 Scrum Guide Expanded v2026.1 的 Sprint Backlog artifact 框架定义。
> Product Owner: SeaPawn

---

## Sprint Goal

将 6 个 scrum role agent 的方法论内容替换为 SGEP v2026.1 原文直接摘抄。 ✅ 达成

> 相干 Product Goal：design-kernel 达到与 scrum-kernel 同等细致的结构化水平。

---

## What — 选中的 PBI

| # | 标题 | 用户故事 | Outcome Criteria | Size | 当前状态 | 备注 |
|---|---|---|---|---|---|---|
| PBI-3 | scrum-kernel agents 重构——移至插件 agents/ 目录 + 内容改回 SGEP 原文摘抄 | 作为 IDEO-Scrum 用户，我希望 scrum-kernel 的 6 个角色能够以真正的 subagent 形式被召唤（如 `/ideo-scrum:scrum-scrum-master`），并且每个 agent 的方法论内容直接摘抄 SGEP 原文而非经过改写，这样我能信任 agent 输出的是方法论原文、而非 agent 编写者的个人解读 | scrum-kernel 的 6 个角色从"skill 附属参考文档"升级为"可独立 spawn 的 Claude Code subagent"；用户召唤任一 role agent 后，其回答内容忠于 SGEP 原文、标注章节出处，不发生自创或释义性偏离 | L | 已完成 | Sprint 02 交付：6 个 agent 全部重写为 SGEP 原文摘抄（266 行总计），SGEP Roles 拆分至 references/scrum-roles.md |
