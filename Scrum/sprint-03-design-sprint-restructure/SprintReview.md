# Sprint Review — Sprint 03

> 按 Scrum Guide Expanded v2026.1 的 Sprint Review event 框架。
> Date: 2026-07-23

---

## Increment Delivered

| Output | Path | Status |
|---|---|---|
| Monday 引用文件 (6) | `DesignSprint/references/` | 交付——忠实摘录原书，统一 Source 标注，叙事精简 |
| design-sprint.md Monday 部分 | `DesignSprint/design-sprint.md` | 交付——8 项 checklist 全部引用 references/ |
| SKILL.md 重构 | `SKILL.md` | 交付——单行 Reference 表 + 简化五天总览 + Use Protocol 合并 |
| 源材料清洗 | `references/DesignSprint-HowtoSolveBigProblemsandTestJakeKnapp.md` | 交付——OCR 修复、章节标题补齐、分隔线清理 (~17处) |
| Tuesday 引用文件 (已回滚) | — | 未交付——发现方法论分化后回滚 |
| Thursday 引用文件 (已回滚) | — | 未交付——同上 |

---

## Sprint Goal Assessment

> **Sprint Goal:** Design Sprint 全书内容（3750 行）从单一 checklist 文件拆分为结构化的多文件体系，与 IDEO-modes/ 和 SGEP references/ 的结构质量一致。

**部分达成。** Monday 达到目标质量，全书结构化因发现方法论分化而调整范围。

- [x] Monday 引用文件：6 个文件，结构质量与 IDEO-modes/ 一致
- [x] Source 标注：每个文件含 Author/Year/Book/Chapter
- [x] SKILL.md 入口：单行 Reference 表 + 简化五天总览
- [ ] Tuesday-Friday 引用文件：未完成（回滚），见关键发现

---

## Definition of Done Check

### Output Done

| 维度 | 状态 | 备注 |
|---|---|---|
| 内容忠实 | ✅ | 对照原书逐段摘录，Source 行标注章节 |
| 结构一致 | ✅ | 每个 reference file 含 H1 + Source + 正文 |
| 无冗余叙事 | ✅ | Graco/Bentz/Byard 故事均压缩，移除冗余案例 |
| 可导航 | ✅ | 从 SKILL.md Reference 表 → design-sprint.md → references/ 三层可达 |
| 路径正确 | ✅ | `monday/` → `references/` 重命名，全局引用更新 |

### Outcome Done

| 类别 | 度量 | 状态 |
|---|---|---|
| User outcomes | Monday 方法论可独立查阅 | ✅ references/ 下每文件可独立阅读 |
| User outcomes | 从 SKILL.md 到具体方法的路径 ≤ 2 步 | ✅ SKILL.md → design-sprint.md → references/ |
| Product Stakeholder outcomes | 原书 Monday 内容无遗漏 | ✅ 对照 Challenge → Target 六个章节 |
| Business impact | Sprint 产出可发布的 Increment | ✅ 6 个 reference files + SKILL.md 重构 |

---

## Key Finding

**Monday 和 Tuesday-Friday 是两种不同的内容类型。**

Monday 的每个节是独立的认知单元（隐喻 + 原理 + 方法），天然适合独立引用文件。Tuesday-Friday 是 workshop 操作系统（纸笔、折纸、圆点贴纸、匿名评审）的流程步骤，核心概念一句话能讲完，剩余的都是 7 人 × 5 天 × 物理空间的实现细节。

这意味着不能对 Design Sprint 全书统一套用同一种文件化模式。Monday 的结构化已到位；Tuesday-Friday 需要为 solo + AI 场景重新设计方法论，而非忠实摘录原书。

---

## Lessons Learned

1. **先拆一个样本，再决定拆全部。** Monday 做完后模式清晰，但周二一做就暴露了结构差异。每个 day 应该用更小的样本验证再铺开。
2. **引用文件 ≠ 翻译 checkboxes。** "Fold a sheet of paper into eight panels" 变成引用文件仍然是操作指令，不会变成方法论。引用文件适合概念密度高的内容。
3. **Design Sprint 全书有一个隐含的 UI 假设：7 人在一个房间里。** 拆文件的过程本质上是在做解耦——把方法论核心从这个特定 UI 中分离出来。
4. **文件命名应该等待结构稳定后再定。** `monday/` → `references/` 的重命名在确认 Tuesday 文件也需要存在后立刻发生。下次先确认整体文件树再命名。
5. **流程步骤型内容（Tuesday-Friday）和认知单元型内容（Monday）的边界是方法论文件化工作的核心判断维度。** 后续任何方法论的结构化工作都应该先用这个维度做分类。

---

## Product Backlog Adaptations

- PBI-5 标记为部分完成
- 新建 PBI：为 solo + AI 场景设计 Design Sprint Tuesday-Friday 方法论（非摘录，是新设计）
- Product Goal 不变：design-kernel 达到与 scrum-kernel 同等细致的结构化水平
- 建议：下个 Sprint 之前，确认周二到周五的方向——是继续 Design Sprint 还是先处理 PBI-2/PBI-4（小 S 级 PBI）
