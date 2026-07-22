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
| PBI-5 | 重组 Design Sprint 内容结构 | 作为 IDEO-Scrum 用户，我希望 Design Sprint 方法论的内容像 Stanford Design Guides 和 SGEP 一样有清晰的文件结构，而不是堆在一个大 markdown 文件里，这样在 Sprint Week 的每个阶段都能快速找到对应的方法论引导 | Design Sprint 内容从"全量引用源书 + 单一 checklist"升级为"结构化多文件参考体系"；用户在 Monday-Friday 任一天都能快速定位对应的方法论原文，不必翻阅 3750 行源书 | ① 源书 `references/DesignSprint-HowtoSolveBigProblemsandTestJakeKnapp.md`（3750 行）按 Set the Stage + Monday-Friday 拆分为 6 个 day 文件，放在 `design-kernel/design-sprint/` 下；② 每个 day 文件包含 WHAT（当日目标）/ WHY（为什么是这天）/ HOW（具体方法与技巧），内容摘抄自源书原文；③ 每个文件标注 Source: Jake Knapp et al., *Sprint* (2016)，保留章节引用；④ 现有 `methods/design-sprint.md` checklist 内容拆分或整合到新结构中，旧文件移除或改为入口索引；⑤ SKILL.md Design Sprint 节表格的 Reference 列更新为新文件路径；⑥ 不丢失源书内容——所有方法论核心段落均有对应新文件归属 | L | 待开始 | 源材料：`references/DesignSprint-HowtoSolveBigProblemsandTestJakeKnapp.md`（3750 行，含 111 张图片引用）；当前入口：`methods/design-sprint.md`（245 行 checklist）；目标目录：`design-kernel/design-sprint/`（新建） |

---

## How — 工作计划

| # | 步骤 | 输入 | 输出 | 状态 |
|---|---|---|---|---|
| H-1 | 确定 Design Sprint 文件拆分方案——对标 IDEO-modes/ 的 WHAT/WHY/HOW 模式 + 章节映射 | 源书目录结构（L164-2922） | 拆分方案：文件清单 + 每文件对应的源书行号范围 | ⏳ 待开始 |
| H-2 | 创建 `design-kernel/design-sprint/` 目录，拆分源书为 6 个 day 文件（Set the Stage + Mon-Fri），提取 WHAT/WHY/HOW，保留源书原文 | `references/DesignSprint-HowtoSolveBigProblemsandTestJakeKnapp.md` | 6 个 day 文件 + 可选 checklist 文件 | ⏳ 待开始 |
| H-3 | 整合/移除旧 `methods/design-sprint.md`——checklist 内容合并到对应 day 文件或独立保留 | `methods/design-sprint.md` | 旧文件处理完毕 | ⏳ 待开始 |
| H-4 | 更新 SKILL.md Design Sprint 节——表格 Reference 列指向新文件路径 | SKILL.md L24-38（Design Sprint 表格） | 更新后的 SKILL.md | ⏳ 待开始 |
| H-5 | 验证——所有新文件无死链，源书方法论核心内容均有归属 | `design-kernel/design-sprint/` | 验证结果 | ⏳ 待开始 |
| | | | | |
