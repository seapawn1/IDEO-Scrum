---
name: sprint-01-skill-stanford
description: Sprint 01 日志全文——PBI-1：design-kernel SKILL.md 融合 Stanford Design Guides，五模式 WHAT/WHY/HOW 三层；命名反复三换
metadata:
  type: project
---

# 冲刺日志 — Sprint 01（skill-stanford）

> 按 Scrum Guide Expanded v2026.1 的 Sprint Backlog / Sprint Review artifact 框架定义。
> Product Owner: SeaPawn · Sprint 01 · 2026-07-22

## Goal-why

### Sprint Goal

**design-kernel SKILL.md 融合 Stanford Design Guides，五模式达到 WHAT / WHY / HOW 三层结构。** ✅ 达成

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

| # | 标题 | 用户故事 | Outcome Criteria | Acceptance Criteria | Size | 当前状态 | 备注 |
|---|---|---|---|---|---|---|---|
| PBI-1 | 细化 ideo-kernel SKILL.md — 融合 Stanford Design Guides | 作为 ideo-kernel 用户，我希望 SKILL.md 中的五模式引导有 WHAT / WHY / HOW 三层结构，而不是当前的单层概述，这样一次对话就能获得完整方法论引导，不需要额外查阅 Stanford 原文 | ideo-kernel SKILL.md 的每个 mode 达到 Stanford Design Guides 的细致程度，用户在 Empathize / Define / Ideate / Prototype / Test 任一 mode 都能获得"是什么—为什么—怎么做"的完整引导 | 5 个 mode 各自包含 WHAT / WHY / HOW 三个子节；内容忠于`references/IDEO-StanfordDesignGuides.md` 原文；标注 Source: IDEO / Stanford d.school Design Guides；保留当前 verbatim 段中 Stanford 未覆盖的补充内容；mode 间 transition 指引保留（如 Empathize >> Define 的 Unpack） | L | 已完成 | Sprint 01 交付：`design-kernel/SKILL.md` 重构 + `IDEO-modes/` 5 文件（WHAT/WHY/HOW + Transition + Source/License） |

### 细化

| # | 步骤 | 输入 | 输出 | 状态 |
|---|---|---|---|---|
| H-1 | 拆分 Stanford Design Guides 为 5 个 mode 文件 | `references/IDEO-StanfordDesignGuides.md` | `stanford-modes/stanford-empatize.md` ~ `stanford-test.md`，各含 WHAT/WHY/HOW + Transition + Source/License | ✅ 完成 |
| H-2 | 摘抄当前 ideo-kernel SKILL.md 五模式内容 | `plugins/ideo-scrum/skills/ideo-kernel/SKILL.md` verbatim 段 | `ideo-modes/ideo-empatize.md` ~ `ideo-test.md`，各含当前 mode 原文 + Source 标注 | ✅ 完成 |
| H-3 | 融合 Stanford + IDEO → 最终版五模式 | `stanford-modes/`（底本）+ `ideo-modes/`（补充） | `final-modes/empathize.md` ~ `test.md`，Stanford WHAT/WHY/HOW 骨架 + ideo 独特内容 | ✅ 完成 |
| H-4 | 重构 SKILL.md：Overview + Method Catalog 两层架构 | `IDEO-modes/` + 旧 SKILL.md verbatim 段 + Method Catalog | 新 SKILL.md：① Overview（IDEO + Design Sprint 两节，含合并 5 列 table）② Use Protocol ③ Method Catalog ④ Runtime Rule；旧 verbatim 段 + Mode Reference 节已移除 | ✅ 完成 |

（注：H-3 声明的 `final-modes/` 最终未单独成产——产物即 `IDEO-modes/`，与命名反复一并见 Review。）

## Developer-how

### 执行总结

计划以"拆分 → 摘抄 → 融合 → 重构"四步线性推进（H-1→H-4）：

1. **H-1**：将 Stanford Design Guides 拆成 5 个 mode 文件，每文件含 WHAT/WHY/HOW + Transition + Source/License——底本。
2. **H-2**：摘抄当前 SKILL.md verbatim 段，沉淀 5 个 ideo-modes 文件——对照源。
3. **H-3**：Stanford 骨架 + ideo 独有内容（Immerse 技法、POV checklist 扩展、focus-flare、Prototype 四目的）融合为正式五模式——设计决策：以 Stanford 为骨架、ideo 作补充层，避免两套并行。
4. **H-4**：SKILL.md 重构为 Overview（IDEO + Design Sprint 两节）+ Use Protocol + Method Catalog + Runtime Rule 两层架构；旧 verbatim 段与 Mode Reference 节删除。

**执行中反复（命名）**：ideo-kernel → design-thinking → design-kernel（三换）；IDEO-modes → modes → IDEO-modes（三换）。最终定名与 scrum-kernel 对称。**结果落点**：`plugins/ideo-scrum/skills/design-kernel/SKILL.md` + `IDEO-modes/`（5 文件）——见 Review。

## Review

### Increment Delivered

| Output | Path | Status |
|---|---|---|
| 重构后的 SKILL.md | `plugins/ideo-scrum/skills/design-kernel/SKILL.md` | 交付——Overview 两节（IDEO + Design Sprint）含合并 table、Use Protocol、Method Catalog、Runtime Rule |
| IDEO 五模式 reference | `plugins/ideo-scrum/skills/design-kernel/IDEO-modes/` (5 files) | 交付——每个 mode 含 WHAT/WHY/HOW + Transition + Source/License |
| Skill 更名 | `ideo-kernel` → `design-kernel` | 交付——与 `scrum-kernel` 对称 |
| 全英文 | SKILL.md 全文 | 交付——除 method 文件名外全部英文化 |

### Sprint Goal Assessment

> **Sprint Goal:** ideo-kernel SKILL.md 融合 Stanford Design Guides，五模式达到 WHAT / WHY / HOW 三层结构。

**达成。** 五项 Acceptance Criteria 全部满足：

- [x] 5 个 mode 各自包含 WHAT / WHY / HOW 三个子节
- [x] 内容忠于 `references/IDEO-StanfordDesignGuides.md` 原文
- [x] 标注 Source: IDEO / Stanford d.school Design Guides
- [x] 保留 verbatim 段中 Stanford 未覆盖的补充内容（Immerse 技法、POV checklist 扩展、focus-flare、Prototype 四目的）
- [x] mode 间 transition 指引保留（Empathize >> Define 的 Unpack 等）

额外交付（超出 Acceptance Criteria 的增值）：

- Skill 从 `ideo-kernel` 更名为 `design-kernel`
- 新增完整的 Design Thinking Overview（IDEO + Design Sprint 两节，含 Wikipedia 摘抄）
- 合并 Mode Reference 表到 Overview，消除冗余章节
- Design Sprint overview 补充了 Monday-Friday 完整流程

### Definition of Done Check

**Output Done：**

| 维度 | 状态 | 备注 |
|---|---|---|
| 内容忠实 | ✅ | 对照 Stanford Design Guides 原文，逐句忠实 |
| 溯源合规 | ✅ | 每个 IDEO-modes 文件标注 Source + License |
| 结构一致 | ⚠️ | README 尚未更新——文件地图未覆盖 `IDEO-modes/` 和 `design-kernel/` 更名 |
| 无死链 | ✅ | SKILL.md 内链接全部可解析 |
| 可导航 | ✅ | 从 SKILL.md Overview table 直达任意 mode reference |
| 语言分明 | ✅ | SKILL.md 全文英文 |

**Outcome Done：**

| 类别 | 度量 | 状态 |
|---|---|---|
| User outcomes | DT mode 引导覆盖核心动作 | ✅ 每个 mode 的 WHAT/WHY/HOW 覆盖完整 |
| User outcomes | ≤ 2 轮对话进入执行 | 未验证——需要后续端到端测试 |
| Product Stakeholder outcomes | IDEO/Stanford 五个 mode 原文无遗漏 | ✅ 已逐段对照 |
| Product Stakeholder outcomes | 文档溯源标注合规 | ✅ |
| Business impact | 每个 Sprint 产出可发布的 Increment | ✅ PBI-1 完成 |

### Lessons Learned

1. **H-1 → H-4 的线性拆分工作有效。** 拆分源材料 → 摘抄现状 → 融合 → 重构的步骤清晰、可回溯。
2. **单个 L-size PBI 占满整个 Sprint。** 风险高——如果中途发现方向错误，已投入大量时间。Sprint 02 应尝试 2-3 个小 PBI。
3. **SKILL.md 的重构过程出现了命名反复。** （ideo-kernel → design-thinking → design-kernel，IDEO-modes → modes → IDEO-modes）。下次先定命名再做内容。
4. **Sprint Planning、Daily Scrum、Sprint Review 全部缺失。** 流程被跳过，Scrum 只保留了 Backlog 和 Increment 两端，中间的事件脚手架完全没用到。

### Product Backlog Adaptations

- PBI-1 标记完成
- Product Goal 更新为 `design-kernel`（与更名同步）
- PBI-2（output-styles）和 PBI-3（scrum-kernel agents 重构）排队中
- 建议：Sprint 02 之前更新 README（Output Done 的结构一致项未达标）
