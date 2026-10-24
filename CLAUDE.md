# IDEO-Scrum

为 Claude Code 提供 Design Thinking 与 Scrum Sprint 方法论的插件。

## 这个仓库是什么

两层结构，改动前先分清在哪一层：

| 层 | 位置 | 性质 |
|---|---|---|
| **插件本体** | `plugins/ideo-scrum/` | 交付物。别人安装的就是这里 |
| **工作记录** | `scrum/` + `docs/` | 用本插件的方法论开发本插件的过程记录 |

`scrum/` 是**当前状态工作区**（产品日志）；`docs/` 放工作记录文档（如 ExpertNotes 客户之声）。1.x 的 sprint 日志是**历史记录**，教训已蒸馏入 `S:\SeaPawn-Memory\memory\IDEO-Scrum\`（原文 git 历史可追溯），不回改。除非发现事实错误，否则不要回头修改已完成 sprint 的内容。

## 当前状态（蒸馏锚点，随 Sprint 更新）

- **2026-10-25 · Sprint 07 收官，发版 v4.0.0**：Sprint Goal 达成（一天）。PBI-21：design-kernel 改名 ideo-kernel（调用名变，故升大版本），「Two Schemes」分清 IDEO 五模式与设计冲刺五阶段（设计冲刺之后接构思、原型、测试，HMW 不单列），五阶段参考迁 `design-sprint/`，Method Catalog 去重并加按模式索引；PBI-20：只有 PO 必须是人（作者设计，注明与 SGEP 不同），stakeholder 一个命令多种身份、可常驻做非源码杂务，SM 派活跟进度、派子代理审阅，Developer 交证据；PBI-22：developer / designer / scrum-master 进入即加载对应内核，ideo-kernel 描述加强（「用 IDEO 五模式」触发 0/5 → 5/5）；PBI-24：插件与 marketplace.json 零中文。蒸馏为记忆档 `sprint-07-roles-kernels`，SprintBacklog 删除（原文 `git show 8f3fb44:scrum/SprintBacklog.md`）。Retro 改进项写入下方「组件描述规约」与「插件验证」。codex 分支未同步，停在 3.2.0，这次没做到双版本同号。新登记 PBI-25、PBI-26，排序由 PO 在 Sprint 08 Planning 定。插件本体 v4.0.0（tag `v4.0.0`、`sprint-07-done`）。
- **2026-10-24 · #28 讨论定案，准备 Sprint 07**：Product Goal 由 PO 重定为「IDEO-Scrum 4.0：让插件带着流程走——角色、内核、流程参考与模板成体系，新项目照着就能跑通」；新增 PBI-20（角色重定义：只有 PO 必须是人；Stakeholder 一个命令多种身份、可常驻；Master 派活跟进度，审阅派全新子代理）、PBI-21（design-kernel 改名 ideo-kernel，分清 IDEO 五模式与设计冲刺五阶段）、PBI-22（角色命令自动加载内核）、PBI-23（流程化参考与文件模板）；PBI-12 改写为方法论分享；PBI-15 关闭，17、18 并入 23，19 并入 20。拆分：Sprint 07＝PBI-21、20、22，Sprint 08＝PBI-23，之后 PBI-12。「Sprint 节律」第一条由「发版即收官」改为「按时间盒收官」；Sprint 06 收官 tag 改名 `sprint-06-done`。插件本体 v3.2.0 未动。详见 [scrum/ProductBacklog.md](scrum/ProductBacklog.md)。
- **2026-10-24 · Sprint 06 正式收官（Review + Retro，单提交）**：Sprint 06 自 08-30 起一份日志跨 55 天、含五次发版（v2.0.0 / v2.0.1 / v3.0.0 / v3.1.0 / v3.2.0），超出 4 周时间盒；下方 08-31 条的「收官」只是 v2.0.0 发版时的范围定案，Review 与 Retro 当时未做，本日由 Developer 收口。本次：四段式日志经 PO 批准后蒸馏为记忆档 `sprint-06-dual-kernel-refactor`（`S:\SeaPawn-Memory\memory\IDEO-Scrum\`），`scrum/SprintBacklog.md` 删除（原文：`git show 3f81260:scrum/SprintBacklog.md`）；记忆路径、Product 节（output-styles→commands）、PBI-15 / PBI-19 状态、README 文件地图已对齐；**总目标（v2.0.0）所指版本早已发布，产品日志原处标「待 PO 重定」，文字未改**；未完成项（15-D、17、18、19 的核验去向、12）回产品日志。Retro 改进项：发版即收官、时间盒写日志头、计划外工作先登记、PBI 状态只写产品日志、迁移类改动全仓 grep，已写入下方「维护规约」的「Sprint 节律」；蒸馏闭环补「日志不单独入库」一句。插件本体 v3.2.0 未动。
- **2026-10-13 · v3.2.0 角色说明更新（SeaPawn 日 Sprint #14）**：stakeholder 由监理位改为**外部视角**——按项目写定的身份看产品与增量，谁都可召唤（新起子代理，或 PO 开临时独立会话），Sprint Review 时由 PO / SM 召唤，不施工，反馈交 PO（依据：PO 10-10 在 D:\MidTerm 定的五条规则；10-13 定保留命令形式、可开独立会话）；正文按逐字保留规约改，【原文】块与 v3.1.0 逐字一致；scrum-master / developer / designer 三个 description 原句不动、末尾追加边界与相互关系句（组件描述规约同步补一句）；PBI-19 监理位撤回、独立核验去向待定；codex 分支同步（四份角色 skill 重生成，`.agents/AGENTS.md` 删除）。插件本体 v3.2.0（main 与 codex 双版本同号）。
- **2026-10-04 · v3.1.0 发版（大整合批）**：roles 参考层撤销（PO 定「指导性内容不进参考层」——SGEP 角色章还回 asset、删 scrum-roles.md 与 SKILL.md Roles 条目）；**14-B 完成**（scrum-master / developer 以 SG2020 原文重建：三节式＝Identity 原稿逐字／原文抄录／CoC 原条目＋2026 精炼）；第四 command **stakeholder**（监理位——PBI-19 升级位；designer 与 stakeholder 随后三节定稿）；**codex 分支同步**（角色载体由 AGENTS.md 模板改为原生 skill：`$scrum-master / $designer / $developer / $stakeholder` 显式调用，templates/ 废弃）；命令不设 Source/License 文件头（署名归 ATTRIBUTION，规约已加例外）；双复检（validator / skill-reviewer）通过；v3.0.0（09-23，output-style→command）经补录。**留待后续：15-D、17、18**（14-B 已闭）。插件本体 v3.1.0（main 与 codex 双版本同号）。详见 [scrum/ProductBacklog.md](scrum/ProductBacklog.md)。
- **2026-09-08 · Sprint 06 延续：v2.0.1 小发版**：执行 seapawn.md L44——scrum-master output-style 去 coding 功能（frontmatter 移除 `keep-coding-instructions`，docs 语义：角色不做软件工程即不放；developer/designer 保留）；sm/developer/designer 三 output-style 全量英文化（description 随落英文 Use when 触发式，译文经 PO 过目放行）；版本号 2.0.0→2.0.1（plugin.json + README 两处）；分支 `sprint-06-dual-kernel-refactor` 合入 main、tag v2.0.1、推送远端。留待后续冲刺不变：15-D、14-B（抄书合规路径）、17、18。详见 [scrum/ProductBacklog.md](scrum/ProductBacklog.md)。插件本体 v2.0.1。
- **2026-08-31 · Sprint 06 收官（v2.0.0 已发布）**：本冲刺完成 PBI-16（双内核描述互链）、14-1/14-2/14-4 + 14-A（designer 重造回归）、15-B/15-C（DesignSprint 手术：五天法废弃、五阶段进 skill、decider→Product Owner、L18a 关闭）；**留待后续冲刺：15-D（scrum-kernel 重构）、14-B（developer/scrum-master 重构）、17（关键文档预先规格）、18（双内核执行模板）**；15-4 两机制点经 PO 定案不落文（定案存产品日志）；PBI-12（笔记）下一冲刺。分支 `sprint-06-dual-kernel-refactor` 已合入 main、tag v2.0.0、推送远端。详见 [scrum/ProductBacklog.md](scrum/ProductBacklog.md)。插件本体 v2.0.0。
- **1.x 已收官蒸馏**：旧目标（两内核结构对等）判定方向性错误，勿延续；教训见 `S:\SeaPawn-Memory\memory\IDEO-Scrum\`（MEMORY.md 索引 + 五期档案）。

## 维护规约

**README 是文件索引与当前状态，Git 历史负责追溯过去。**

- README 面向外部读者：只陈述这里是什么、文件地图、来源授权；作者侧的当前状态不入 README——由本文件「当前状态」锚点与 `scrum/ProductBacklog.md`（产品日志）承担
- 提交前确认 README 是否需要同步更新——尤其是新增/删除/重命名文件、改动插件版本号时
- 若发现 README 已过期、可能误导新会话的 LLM，必须显式提醒用户更新，不要默默放过
- 追溯旧决策、文件演变、阶段状态时，放手查阅 Git 历史

**版本号与 tag**

- 主干分支是 `main`，永远指向最新状态
- 版本号用 tag 标记，不写进分支名
- 插件版本号在 `plugins/ideo-scrum/.claude-plugin/plugin.json`，改动时 README 的两处版本号需同步

**组件描述（attribute description）规约**

写插件组件（skill / command）的 `description` 时：它是**触发条件**，不是自我介绍——用 "Use when..." + 具体场景词；同类组件描述必须有区分度（模板趋同 = embedding 空间互相叠影，系统无法选择）。plugin.json 的 description 是元数据（展示用），非触发主战场。（来源：Sprint 04。）角色命令可以在触发句之后追加一两句边界和相互关系（替谁做事、不做什么、谁召唤谁），让各角色在技能清单里互相知道；触发句保持在最前（2026-10-13，#14）。触发不足时，写明「什么情况下先加载」，不要只堆关键词（2026-10-25，PBI-22：ideo-kernel 的触发由 1/10 升到 5/5）。

**冲刺蒸馏闭环**

每期 Sprint 结束的 Review 阶段，本着"SprintBacklog 归西"的目的：AI 狠读冲刺日志 + 产品日志 → 写入四段式日志（Review 段写厚）→ 将教训/关键发现/变更**蒸馏**为一份记忆档案（30-50 行，带出处指向 git）存入 `S:\SeaPawn-Memory\memory\IDEO-Scrum\`（路径以 `.claude/settings.json` 的 `autoMemoryDirectory` 为准）→ 删除 SprintBacklog 及中间产物。脚手架已拆、教训常在、原文 git 兜底。日志经 PO 批准后即蒸馏，日志本身不单独入库。

> 三分工：**memory 管教训**（常驻、蒸馏过，见 `S:\SeaPawn-Memory\memory\IDEO-Scrum\MEMORY.md`），**git 管原文**（可查、完整），**`scrum/` 管现状**（产品日志、工作记录）。

**Sprint 节律**（2026-10-24，Sprint 06 Retro）

- **按时间盒收官**：Sprint 到 SprintBacklog 头部写的截止日（≤4 周）收官，当天做 Review + Retro（单提交）；期间发版照常，记进当期日志，不结束 Sprint；之后的新工作开新 Sprint、新日志；日志当日记，不事后补录。（10-24 由「发版即收官」改：SGEP 的 Sprint 长度固定，一个 Sprint 内可多次发版。）
- **时间盒写在日志头**：SprintBacklog 头部写截止日（≤4 周）；到期未完成的 PBI 回产品日志，不顺延。
- **计划外工作先登记**：作者待办或对话中定下的新工作，先在产品日志登记 PBI，再由 PO 定是否进当前 Sprint（范围可重谈，Sprint Goal 不变）；不进则等下个 Sprint。
- **PBI 状态只写产品日志**：SprintBacklog 引用 PBI 编号，不复写状态；进展写在 How 区。
- **迁移类改动全仓 grep**：路径、位置、名称迁移时，同一提交内全仓 grep 旧值至零残留（README、CLAUDE.md、日志都算）。

**插件验证**

本仓库无 build/test。改动插件后，用 Agent 类型 `plugin-dev:plugin-validator` 校验插件结构/plugin.json；涉及 skill 质量时用 `plugin-dev:skill-reviewer`（两者经 Agent 工具调用，非 slash command）。marketplace 清单在 `.claude-plugin/marketplace.json`。

**回归测试**（2026-10-25，Sprint 07 Retro）

- 判定标准先写、单独提交，再跑；出结果后不改标准。
- 触发测两条路径：从角色命令进入，和直接说。
- 比较描述效果，同日同环境对照，带改前基线。
- 无头测法：`reclaude -p --plugin-dir <插件 Windows 路径>`（顶替已装同名插件）；Git Bash 下 `/` 开头的提示加 `MSYS_NO_PATHCONV=1`，路径用 `cygpath -w`。
- 工具审查员（skill-reviewer 等）的必改项，落盘前先对一遍 PO 的定案；冲突就报 Master，不照改。

## 源材料与授权

插件内所有第三方摘录必须带署名。新增摘录时：

1. 文件顶部标注 `> Source:` 与 `> License:` 两行，License 须与 [ATTRIBUTION.md](ATTRIBUTION.md) 中记录的条款一致
2. 若引入新来源，先在 ATTRIBUTION.md 中登记，再写摘录

> 例外：命令类组件（`commands/*.md`）的抄录主体不设文件头两行；其署名义务由 ATTRIBUTION.md 的登记承担。

**已知的授权约束：**

- Scrum Guide 2020 / SGEP —— CC BY-SA 4.0，可摘录、可商用
- Stanford d.school Bootleg —— CC BY-**NC**-SA 4.0，含非商业限制
- 《Sprint》(Knapp) —— 全版权。**仅记录方法流程，不逐字摘录大段原文，不含书内插图**

`references/` 是源材料原件，**不入库**（`.gitignore` 已拦截），仅存于作者本地。

## 插件内容的自足性

插件会运行在别人的 Claude Code 里，那里没有本仓库的上下文，也没有作者的全局配置。

**写插件内容时，不要依赖任何未在插件内言明的约定。** 例如「用 mermaid 画图」必须同时说明方向（`flowchart TD`），否则在他人环境中行为不一致。
