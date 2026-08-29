---
name: sprint-04-pbi4-descriptions
description: Sprint 04 蒸馏——description=trigger condition、区分度>全面性（已提升为 CLAUDE.md 规约）
metadata: 
  node_type: memory
  type: project
  originSessionId: 6b3a6baf-f74a-4d46-8db8-825e4b9b70fb
  modified: 2026-08-29T21:08:43.357Z
---

# Sprint 04（pbi4-descriptions）蒸馏

> 源：全文 `Scrum/sprint-04-pbi4-descriptions/SprintBacklog.md`（git 历史 `v1` tag 起可查）。

**增量**：13 个 description 字段（plugin.json + 2 SKILL + 10 agents）从"自我介绍"改为 "Use when" 触发模式。

**核心发现（约束后所有组件编写）**：description 的功能是 **trigger condition**（embedding 锚点），不是自我介绍——"Use when X role is needed" 优于 "when discussing X"（后者只在元层对话触发）。同类组件**区分度优先于全面性**（模板趋同 = embedding 中互相叠影，系统无法选择）。plugin.json 的 description 是元数据，非触发主战场。

**教训**：S 级 PBI 单人一次成型约 30 分钟，不拆分。

> 此发现已提升为 CLAUDE.md 规约。
