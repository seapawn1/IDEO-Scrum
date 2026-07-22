# Sprint Backlog — Sprint 01

> 按 Scrum Guide Expanded v2026.1 的 Sprint Backlog artifact 框架定义。
> Product Owner: SeaPawn

---

## Sprint Goal

**ideo-kernel SKILL.md 融合 Stanford Design Guides，五模式达到 WHAT / WHY / HOW 三层结构。**

> 相干 Product Goal：ideo-kernel 达到与 scrum-kernel 同等细致的结构化水平。

---

## What — 选中的 PBI

| # | 标题 | 用户故事 | Outcome Criteria | Acceptance Criteria | Size | 当前状态 | 备注 |
|---|---|---|---|---|---|---|---|
| PBI-1 | 细化 ideo-kernel SKILL.md — 融合 Stanford Design Guides | 作为 ideo-kernel 用户，我希望 SKILL.md 中的五模式引导有 WHAT / WHY / HOW 三层结构，而不是当前的单层概述，这样一次对话就能获得完整方法论引导，不需要额外查阅 Stanford 原文 | ideo-kernel SKILL.md 的每个 mode 达到 Stanford Design Guides 的细致程度，用户在 Empathize / Define / Ideate / Prototype / Test 任一 mode 都能获得"是什么—为什么—怎么做"的完整引导 | 5 个 mode 各自包含 WHAT / WHY / HOW 三个子节；内容忠于 `references/IDEO-StanfordDesignGuides.md` 原文；标注 Source: IDEO / Stanford d.school Design Guides；保留当前 verbatim 段中 Stanford 未覆盖的补充内容；mode 间 transition 指引保留（如 Empathize >> Define 的 Unpack） | L | 进行中 | 源材料：`references/IDEO-StanfordDesignGuides.md`（214 行）；当前 SKILL.md verbatim 段约 100 行，需扩展为 5 个 mode × 3 层结构 |

---

## How — 工作计划

| # | 步骤 | 输入 | 输出 | 状态 |
|---|---|---|---|---|
| H-1 | 拆分 Stanford Design Guides 为 5 个 mode 文件 | `references/IDEO-StanfordDesignGuides.md` | `stanford-modes/stanford-empatize.md` ~ `stanford-test.md`，各含 WHAT/WHY/HOW + Transition + Source/License | ✅ 完成 |
| H-2 | 摘抄当前 ideo-kernel SKILL.md 五模式内容 | `plugins/ideo-scrum/skills/ideo-kernel/SKILL.md` verbatim 段 | `ideo-modes/ideo-empatize.md` ~ `ideo-test.md`，各含当前 mode 原文 + Source 标注 | ✅ 完成 |
| H-3 | 融合 Stanford + IDEO → 最终版五模式 | `stanford-modes/`（底本）+ `ideo-modes/`（补充） | `final-modes/empathize.md` ~ `test.md`，Stanford WHAT/WHY/HOW 骨架 + ideo 独特内容（Immerse / POV checklist / focus-flare / 四目的） | ✅ 完成 |
| | | | | |
