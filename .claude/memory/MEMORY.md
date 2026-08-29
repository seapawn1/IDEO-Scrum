# MEMORY.md —— 索引

> 1.x 五期冲刺日志全文（v2.0.0 新轨后从 Scrum/ 迁入，git 历史 `99a28ba` 及更早存档）。每期一条，键对象 = 文件。细则查对应文件；忘记在哪查时先看本索引。

## 1.x 冲刺日志（5 期）

- [Sprint 01 — skill-stanford](sprint-01-skill-stanford.md) — PBI-1：design-kernel SKILL.md 融合 Stanford Design Guides，五模式 WHAT/WHY/HOW 三层。**教训：** ① 命名反复三换（ideo-kernel→design-thinking→design-kernel；IDEO-modes 三换）——先定命名再做内容；② 单个 L 级 PBI 占满 Sprint 风险高，下期应试 2-3 个小 PBI；③ Sprint Planning / Daily Scrum / Sprint Review 全部缺席——流程只留了 Backlog 和 Increment 两端；④ H-1→H-4 线性拆分（拆源→摘抄→融合→重构）有效、可回溯。**残留工作：** README 更新滞后（结构一致项未达标）。
- [Sprint 02 — agents-sgep](sprint-02-agents-sgep.md) — PBI-3：6 个 scrum role agent 替换为 SGEP v2026.1 原文摘抄（266 行总计），SGEP Roles 拆分至 references/scrum-roles.md。**教训：** ① agent 留在 skill 目录内聚性最好，勿移插件层；② "做 A 顺便做 B"（拆分 SGEP Roles）是单人团队有效模式；③ worktree 写入坑——文件位置混乱，后续 Sprint 直接主分支。
- [Sprint 03 — design-sprint-restructure](sprint-03-design-sprint-restructure.md) — PBI-5：Design Sprint 全书（3750 行）从单 checklist 拆为结构化多文件；Monday references/ 6 文件 + SKILL.md 重构完成；Tuesday 回滚。**核心发现（v2.0.0 种子）：** Monday 是**认知单元**（隐喻+原理+方法，适合独立引用文件），Tuesday-Friday 是 **workshop 操作系统**（纸笔/折纸/圆点贴纸/匿名评审——7 人×5 天×物理空间实现细节，核心一句话讲完）——不能统一套用文件化模式，需为 solo+AI 场景重新做方法论设计（PBI-6 → 并入 PBI-7）。**教训：** ① 先拆一个样本再决定拆全部；② 引用文件 ≠ 翻译 checkboxes；③ 原书含隐含 UI 假设"7 人在一个房间"——拆文件本质是解耦；④ 流程步骤型 vs 认知单元型的分层是方法论文件化工作的核心判断维度；⑤ 文件名等结构稳定后再定（monday/→references/ 重命名）。
- [Sprint 04 — pbi4-descriptions](sprint-04-pbi4-descriptions.md) — PBI-4：13 个 description 字段（plugin.json + 2 SKILL + 10 agents）全部优化，"discussing"→"role/perspective is needed"。**核心发现：** description 的功能是 **trigger condition**（embedding-space anchor placement）——"Use when..." 优于 "This is..."；区分度 > 全面性（模板趋同=embedding 里互相叠影）；plugin.json description 是人类元数据，非触发主战场。**教训：** S 级 PBI 单人一次成型 ~30 分钟，不需拆分。
- [Sprint 05 — pbi2-output-styles](sprint-05-pbi2-output-styles.md) — PBI-2：3 个角色型 output-style 入插件（agent-designer / developer / scrum-master，`keep-coding-instructions: true`）。**核心发现：** output-style 有两种形态——**模式型**（改变探索/综合/发散行为倾向）与**角色型**（定义身份/职责/节律/边界，更高承诺、一整套行为契约）；本次交付为角色型。**教训：** 插件文件项目名引用须通用化（"ClaudeDream"→"当前项目"）。

## 其他

- [v2.0.0 验证轮设计地图](Scrum/.IDEO/DesignMapping.md) — v2.0.0 验证轮；挑战 = 插件重塑为 agent 插件（solo 用户 vs 团队方法论场景错配），Goal = 产品愿景，Q1-Q3（速度/收敛张力/信度）。说明：此条指向仓库文件，随仓库入库。
