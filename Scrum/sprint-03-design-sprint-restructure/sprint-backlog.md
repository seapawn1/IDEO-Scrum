# Sprint Backlog — Sprint 03

> 按 Scrum Guide Expanded v2026.1 的 Sprint Backlog artifact 框架定义。
> Product Owner: SeaPawn

---

## Sprint Goal

**Design Sprint 全书内容（3750 行）从单一 checklist 文件拆分为结构化的多文件体系，与 IDEO-modes/ 和 SGEP references/ 的结构质量一致。**

> 相干 Product Goal：design-kernel 达到与 scrum-kernel 同等细致的结构化水平。

---

## What — 选中的 PBI

| # | 标题 | 用户故事 | Outcome Criteria | Acceptance Criteria | Size | 当前状态 | 备注 |
|---|---|---|---|---|---|---|---|
| PBI-5 | 重组 Design Sprint 内容结构 | 作为 IDEO-Scrum 用户，我希望 Design Sprint 方法论的内容像 Stanford Design Guides 和 SGEP 一样有清晰的文件结构，而不是堆在一个大 markdown 文件里，这样在 Sprint Week 的每个阶段都能快速找到对应的方法论引导 | — | — | L | 部分完成 | 源材料：`references/DesignSprint-HowtoSolveBigProblemsandTestJakeKnapp.md`（3750 行）；入口：`DesignSprint/design-sprint.md`；Monday 6 个引用文件完成（`references/`），SKILL.md 重构完成；**周二到周五发现方法论分化——内容本质是 workshop 流程，不能套 Monday 的引用文件模式，后续 Sprint 需重新设计** |

---

## How — 工作计划

| # | 步骤 | 输入 | 输出 | 状态 |
|---|---|---|---|---|
| 1 | 源材料清洗 | `references/DesignSprint-HowtoSolveBigProblemsandTestJakeKnapp.md` (3750行) | OCR 修复、章节标题、分隔线清理（~17 处）、图片引用重排 | 完成 |
| 2 | Monday 引用文件提取 | 源材料 L680-1190（Challenge → Target） | `references/` 下 6 个文件：define-the-challenge / start-at-the-end / make-a-map / ask-the-experts / how-might-we / pick-a-target | 完成 |
| 3 | Monday 引用文件精简 | 6 个引用文件 | 合并 start-at-the-end（2→1）、压缩 Graco 故事、统一结构与数据源标注 | 完成 |
| 4 | `monday/` → `references/` 重命名 | design-sprint.md 内部引用路径 | 全局路径更新 | 完成 |
| 5 | SKILL.md Design Sprint 部分重构 | 旧版段落 + 5 行冗余表 | 单行 Reference 表 + 简化五天总览（3列） | 完成 |
| 6 | SKILL.md Use Protocol 整理 | Runtime Rule + Use Protocol 分离 | 合并为单节，移至文件末尾 | 完成 |
| 7 | Tuesday 引用文件（已回滚） | 源材料 L1190-1430（Remix and Improve + Sketch） | `tuesday/lightning-demos.md` + `tuesday/four-step-sketch.md` | 已回滚 |
| 8 | Tuesday-Friday 方法论评估 | Tuesday 引用文件 + 源材料 L1430-2200 | 发现：周二到周五是 workshop 流程步骤，Monday 是认知单元；不能套同一套引用文件模式 | 完成 |

---

详见 `SprintReview.md`
