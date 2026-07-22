# Sprint Review — Sprint 01

> 按 Scrum Guide Expanded v2026.1 的 Sprint Review event 框架。
> Date: 2026-07-22

---

## Increment Delivered

| Output | Path | Status |
|---|---|---|
| 重构后的 SKILL.md | `plugins/ideo-scrum/skills/design-kernel/SKILL.md` | 交付——Overview 两节（IDEO + Design Sprint）含合并 table、Use Protocol、Method Catalog、Runtime Rule |
| IDEO 五模式 reference | `plugins/ideo-scrum/skills/design-kernel/IDEO-modes/` (5 files) | 交付——每个 mode 含 WHAT/WHY/HOW + Transition + Source/License |
| Skill 更名 | `ideo-kernel` → `design-kernel` | 交付——与 `scrum-kernel` 对称 |
| 全英文 | SKILL.md 全文 | 交付——除 method 文件名外全部英文化 |

---

## Sprint Goal Assessment

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

---

## Definition of Done Check

### Output Done

| 维度 | 状态 | 备注 |
|---|---|---|
| 内容忠实 | ✅ | 对照 Stanford Design Guides 原文，逐句忠实 |
| 溯源合规 | ✅ | 每个 IDEO-modes 文件标注 Source + License |
| 结构一致 | ⚠️ | README 尚未更新——文件地图未覆盖 `IDEO-modes/` 和 `design-kernel/` 更名 |
| 无死链 | ✅ | SKILL.md 内链接全部可解析 |
| 可导航 | ✅ | 从 SKILL.md Overview table 直达任意 mode reference |
| 语言分明 | ✅ | SKILL.md 全文英文 |

### Outcome Done

| 类别 | 度量 | 状态 |
|---|---|---|
| User outcomes | DT mode 引导覆盖核心动作 | ✅ 每个 mode 的 WHAT/WHY/HOW 覆盖完整 |
| User outcomes | ≤ 2 轮对话进入执行 | 未验证——需要后续端到端测试 |
| Product Stakeholder outcomes | IDEO/Stanford 五个 mode 原文无遗漏 | ✅ 已逐段对照 |
| Product Stakeholder outcomes | 文档溯源标注合规 | ✅ |
| Business impact | 每个 Sprint 产出可发布的 Increment | ✅ PBI-1 完成 |

---

## Lessons Learned

1. **H-1 → H-4 的线性拆分工作有效。** 拆分源材料 → 摘抄现状 → 融合 → 重构的步骤清晰、可回溯。
2. **单个 L-size PBI 占满整个 Sprint。** 风险高——如果中途发现方向错误，已投入大量时间。Sprint 02 应尝试 2-3 个小 PBI。
3. **SKILL.md 的重构过程出现了命名反复。** （ideo-kernel → design-thinking → design-kernel，IDEO-modes → modes → IDEO-modes）。下次先定命名再做内容。
4. **Sprint Planning、Daily Scrum、Sprint Review 全部缺失。** 流程被跳过，Scrum 只保留了 Backlog 和 Increment 两端，中间的事件脚手架完全没用到。

---

## Product Backlog Adaptations

- PBI-1 标记完成
- Product Goal 更新为 `design-kernel`（与更名同步）
- PBI-2（output-styles）和 PBI-3（scrum-kernel agents 重构）排队中
- 建议：Sprint 02 之前更新 README（Output Done 的结构一致项未达标）
