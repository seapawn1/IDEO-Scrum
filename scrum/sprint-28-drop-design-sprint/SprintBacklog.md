# Sprint Backlog — Sprint 28 (drop-design-sprint)

> Started: 2026-11-24 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: sprint-28-drop-design-sprint | Product Owner: SeaPawn | Scrum Master: lead | Developer: sprint-28-dev
> Now: Increment — 工作项 `#1`–`#7` 全部完成（含 `0.8.0` Breaking 独立升号提交 `83ed411` 与冻结 Test 判据／脚本独立提交），Increment 已齐备，待 Master 核验后代行放行 Sprint Test
> Waiting for PO: None（PO 2026-11-24 全流程放权；遇阻塞、Test 未过或涉底线事项立即回报）
> How to write this log: the Memory's *Running a Sprint* section (the memory skill's `SKILL.md`).
> Keep every heading, even the ones filled later; add none. Work remarks go in chapter 4, Increment notes; an optional explanation of the commitment may follow its table (Memory `templates-record-outputs`, `goal-fixed`, `commitment-table`).

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 把插件收敛为「Scrum Sprint 单主轨 + IDEO 五模式工具箱」：去掉设计冲刺与 Designer 角色、让看板聚焦 Scrum、让 Sprint 的 How 回归真正的方案计划，让熟手与陌生人不再在两套流程间纠结，照着一套清晰且无全版权包袱的规矩就能走通探索与交付。 |
| --- | --- |

<!-- The Product Owner decides the Sprint Goal: one unifying project value goal, or one commitment that may list the lines of work if this Sprint serves as their index (Memory `sprint-goal`, `share-goal-and-checks`). Keep the exact text in the one-row table; optional prose below can explain it without becoming part of it. -->

### 1.2 Definition of Done

<!-- Link to the complete Definition of Done in the product log (§1.3); record the Product Owner’s verification priorities for this Sprint, not a reduced standard (Memory `dod-in-product-log`, `dod-standards`, `sprint-goal`, `share-goal-and-checks`). Record permission to start Why when opening; end the chapter with the Sprint Goal decision and note whether What has been authorized (Memory `stage-gates`, `read-the-goal`). -->

完整产品 Definition of Done 见 [ProductBacklog.md §1.3](../ProductBacklog.md#13-definition-of-done)（全部标准照常生效，不降标准）。本期 PO 确认的核验重点：

1. **结构与双宿主验证**：`claude plugin validate --strict plugins/ideo-scrum`、`plugin-validator`（因删内核／角色／模板／改 Hook 属结构变化）、`node --test scripts/check_dsh.mjs` 及 DSH 实际安装与 4 角色入口验证；
2. **看板、文档与迁移**：`board_check` 自测与新版看板检验、文档无死链检查、全仓旧路径／旧称法 grep（明确放行历史归档与历史发版记述）；
3. **触发与关键边界回归**：删 `design-kernel` 后纯 `ideo-kernel` 与其余内核触发不回退（覆盖原设计类题 Q11），`How` 放开后仍守住 `go-ahead` 放行门与原型不进 Increment；
4. **版权与署名**：确认插件本体与 `ATTRIBUTION.md` 中 Knapp《Sprint》全版权摘录清零。

- Why 阶段放行（2026-11-24，PO SeaPawn）：授权开启 Sprint 28（分支 `sprint-28-drop-design-sprint`）并进入 Why 阶段。
- Why 阶段决定与 What 阶段放行（2026-11-24，PO SeaPawn）：定稿 Sprint Goal 与上述 4 项 DoD 核验重点，目标版本定为 `0.8.0`（Breaking），授权进入 What 阶段。本决定时 Sprint Goal 原文：「把插件收敛为「Scrum Sprint 单主轨 + IDEO 五模式工具箱」：去掉设计冲刺与 Designer 角色、让看板聚焦 Scrum、让 Sprint 的 How 回归真正的方案计划，让熟手与陌生人不再在两套流程间纠结，照着一套清晰且无全版权包袱的规矩就能走通探索与交付。」（Product Goal 原文：「产品化：从作者能用到大家都好用；看板一眼看清进度，文档讲清规矩；懂 Scrum 的人照着就能走完第一个冲刺。」）

## 2. What

### 2.1 Product Backlog Items

<!-- The Product Owner leads the selection; the Scrum Master and the Developer say when it is too much or too little. The selected items, copied word for word from the product log (Memory `select-items`). -->

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-104 | 移除设计冲刺与 Designer 角色，统一为 Sprint + IDEO 五模式 | 作为熟手／陌生人，我想插件只保留 Scrum Sprint 单主轨与 IDEO 五模式共享工具箱，以便不再为选设计冲刺还是五模式纠结、架构更扁平且无全版权包袱 | 插件全链路：内核、角色、Memory、Hook、DSH、文档与测试 | L |
| PBI-105 | 看板移除设计冲刺卡，只保留产品卡与冲刺卡 | 作为熟手，我想看板只保留产品卡和冲刺卡，以便一眼聚焦 Scrum 进度、不再维护冗余的设计卡 | 插件：看板（`board/`）与校验脚本 | M |
| PBI-106 | Sprint How 放开形态约束，回归 Scrum 原文 | 作为 Developer／PO，我想在 Sprint 第 3 章（How）按 Scrum 原文自由产出真正的方案式计划，以便不被「只能写简短工作项、不是方案」的额外规定束缚 | 插件：Memory（`details/sprint.md`、`details/departures.md`）与 `sprint-backlog-template.md` | S |

### 2.2 Refinement

<!-- The Scrum Master leads. What refinement settled, each point with who decided it; the acceptance criteria; the method and pass lines set before Test, including the evidence to be checked (Memory `refinement`, `tests-criteria-first`, `check-script-misses`). End with the Product Owner’s refinement decision and note whether How has been authorized (Memory `stage-gates`, `read-the-goal`). -->

#### 已定口径（PO 2026-11-24）

1. **架构定位与单主轨（PBI-104）**：
   - 删除 `skills/design-kernel/`（含 Knapp《Sprint》15 篇全版权摘录）、`commands/designer.md`、`template/design-backlog-template.md` 及 Memory 中设计冲刺专属规则与细则。
   - **IDEO 五模式不是取代设计冲刺的「平级旁路分支」**：整体架构图（`details/flow-maps.md`、`ProductBacklog.md` §2.2 等）删掉设计冲刺分支，将 IDEO 定位为**一切实践的基础与共享工具箱**，产品日志向下只进 Scrum Sprint 单主轨。
   - **白纸冷启动**：不靠设计冲刺；产品目标一般都能写出来，实在写不出就是 Empathize 没做到位，用五模式做 Empathize／Define 补齐。
   - **保留 4 条本仓库沉淀的操作纪律**（作为自有约定留在 IDEO／Memory，不留 Knapp 摘录）：先发散再收敛、隔离子代理草图防趋同、原型只为学习且不进 Increment、保留测试证据。
   - **角色精简为 4 个**：Master（陪 PO 共情／测试、守流程、审阅）、Developer（承接 IDEO 发散／原型／测试，及 Sprint How 与 Increment；须守住原型不进 Increment）、Stakeholder（外部视角）、Supporter（杂活、看板与 PO 联络点）。
   - **`Start at the End` 与 `Make a Map`**：不保留 Knapp 原书摘录；`Make a Map` 沿用 `architecture-map`（去掉旧摘录引用）；「从失败假设反推关键问题」浓缩为 1–2 句自有约定放进 `details/product-log.md`（立 Product Goal 时可选）与 `ideo-kernel`（Empathize／Define 可选技巧）；不改 Sprint 第 2 章 DoD。
   - **`IdeoBacklog.md` 归属与归档**：保留 `scrum/ideo-<suffix>/IdeoBacklog.md`；默认不另开独立设计分支（服务某 Sprint 共用该 Sprint 分支，服务产品日志直接在当前分支／`main`；用户自愿另开亦可，无需刻意强调）；归档在下一次 Sprint Review 移入 `scrum/documents/ideo/`（冷启动尚无 Sprint 时随首个 Sprint 或 PO 确认归档）。
   - **发版与 PBI-103**：目标版本号 **`0.8.0`**（Breaking 变更，CHANGELOG 标 Breaking 并给旧设计日志迁移说明）；PBI-103 不作为开发项进 2.1，在纯 `ideo-kernel` 触发回归中覆盖原 Q11 设计类题后，于 Review 收官时关闭移入 3.2。
2. **看板口径（PBI-105）**：
   - 看板彻底移除设计冲刺卡，仅保留**产品卡与冲刺卡**，不展示独立 IDEO 日志；同步更新 `board/board-log.md` 顶部透明度声明，明确「看板聚焦产品与 Scrum Sprint 状态，不覆盖独立 IDEO 研究日志」。
   - Hook（`hooks/commitments.sh`）与 DSH（`dsh/commitments.js`）同步去掉设计目标读取与「有 N 个设计开着，见看板」提示。
3. **Sprint How 切口（PBI-106）**：
   - 删除 Memory 与模板中的 `no-steps` 及「不能是方案／不写步骤」的额外限制，允许 Developer 在第 3 章产出充分的方案式计划。
   - **How 显式锚定 `Ideate`（PO 2026-11-24 确认）**：在 `sprint.md`、`sprint-backlog-template.md` 与 `sprint-kernel/SKILL.md` 写明 How 对应 IDEO 的 Ideate——当问题有多条路线、涉及设计／架构取舍或需要出方案时，读 `../ideo-kernel/IDEO-modes/ideate.md` 先发散再收敛（必要时隔离子代理防趋同），做法明晰的小改动不强求凑仪式；并附一张轻量「Sprint 五阶段按需调用 IDEO 五模式」对照（Why 目标不清时用 Empathize、What 精化用 Define、How 出方案用 Ideate、Increment 低保真试错用 Prototype、Test 验体验用 Test）。
   - **保留 `go-ahead`（施工前 PO 放行门）**，并在 `details/departures.md` 如实记为偏离 Scrum 原文；保留第 3 章工作项表（`# / Work item / Output / Done when`）与 `✓ <date>` 标记（看板进度行不破；Developer 可在表外充分展开方案）。
4. **Developer 全仓盘点补定口径（PO 2026-11-24 确认）**：
   - **未落地原型文件 vs 测试证据**：关联冲刺在用时，原型及产出想法可保留供冲刺参考复用，随关联冲刺收官清理；没有锚定冲刺或收口后无用时允许删原型文件，但**测试证据与结论记录必随 `IdeoBacklog.md` 归档至 `scrum/documents/ideo/`**（同步修 `details/ideo-ending.md`）。
   - **看板彻底不读 `scrum/ideo-*/`**：连同冲刺卡 `sprints[].ideo` 脚注与 `scripts/board_check/check.py` 的 IDEO 状态机一并移除；删除 Sprint 21 设计卡盲读工具（`scripts/board_check/prepare_review.py`、`fixtures/review-expectations.json`）与设计夹具（`fixtures/acme/scrum/design-*`、`ideo-delta/`）。
   - **`board_check/check.py` 兼容 PBI-106**：改为按表头识别第 3 章工作项表（`Work item`/`工作项` + `Done when`/`完成条件`），找不到时 `blocks = []` 自动隐藏第 3 层不报错。
   - **词表、校验脚本与 README 截图**：`docs/glossary.md` 删 7 个设计冲刺词条（原 `Make a Map` 结构描述并入 `the Map`），同步更新 `scripts/check_docs.py` 自测用例；PBI-105 完成后用新版纯 Scrum 看板重截 `docs/images/board-overview-light.png` 与暗色图。
   - **`AGENTS.md` 同步授权**：PO 2026-11-24 直接授权本期同步更新 `AGENTS.md` 第 13、31、45 行（去除 `scrum/design-*/`、`design` 内核、`《Sprint》(Knapp) 全版权` 旧说法），不动 `CLAUDE.md`。
   - **PBI-104 粒度**：§2.1 保持 PBI-104/105/106 三条不强拆，在 §3 How 内把 PBI-104 切分为若干单会话工作块推进。
5. **Test 方法、模型与冻结口径（Test 前提交冻结）**：
   - 结构与双宿主：`claude plugin validate --strict plugins/ideo-scrum`、`plugin-validator`（Haiku，由 Master 派全新子代理）、`node --test scripts/check_dsh.mjs`；DSH 实装与 4 角色入口通过 **DSH 网页端（侧边栏浏览器）** 直接验证。
   - 看板、文档与迁移：`board_check` 全部自测＋用本仓真实日志生成离线 `ScrumBoard.html` 核验（兼出新版 README 双色截图）；`check_docs.py` 无死链；全仓旧路径／旧称法 grep 清零（**明确放行清单**：`scrum/documents/`、`CHANGELOG.md` 历史条目、`scrum/ProductBacklog.md` 历史行与 PBI-104 备注、`scrum/sprint-28-drop-design-sprint/SprintBacklog.md` 本期日志自身，以及 `ideo-kernel/` 内 d.school 原文摘录的 5 处普通英文词 `designer`）。
   - 触发与边界回归：Claude Code 触发与关键边界测试直接使用当前已配好的 `claude` 命令跑（保留原 Q11 检验旧说法能干净命中 `ideo-kernel`，另验其余内核不回退、`How` 放开后仍守住 `go-ahead`、原型不进 Increment）；不重跑整套陌生人大测试（PBI-63）和 Memory 效果实验（留给 PBI-101）。
   - 版权与署名：`ATTRIBUTION.md` 与插件目录内 Knapp《Sprint》全版权摘录清零。

- **Developer 精化第 6 步复述（2026-11-24，`sprint-28-dev`）**：已完成全仓 ~55 文件只读盘点与 6 项核心口径复述，确认无遗漏歧义。
- **What 阶段决定与 How 阶段放行（2026-11-24，PO SeaPawn）**：确认 §2.1 选入条目（PBI-104、PBI-105、PBI-106）与 §2.2 全部精化口径、Developer 第 6 步复述及 `AGENTS.md` 3 处同步授权，结束精化，授权进入 How 阶段。本决定时 Sprint Goal 原文：「把插件收敛为「Scrum Sprint 单主轨 + IDEO 五模式工具箱」：去掉设计冲刺与 Designer 角色、让看板聚焦 Scrum、让 Sprint 的 How 回归真正的方案计划，让熟手与陌生人不再在两套流程间纠结，照着一套清晰且无全版权包袱的规矩就能走通探索与交付。」

## 3. How

<!-- The Developer writes this chapter as a full solution plan for making the selected items (Memory `how-is-a-plan`): expand architecture, tradeoffs, interfaces, and steps to the depth the work needs. When multiple routes or design tradeoffs exist, treat How as IDEO Ideate — read `IDEO-modes/ideate.md` in the `ideo-kernel` skill and diverge before converging (Memory `diverge-first`, `isolated-sketches`); skip ceremony for straightforward changes. Keep the `# | Work item | Output | Done when` table below (each item done within one session, prefixed `✓ <date>` on completion), followed by Key choices, Risks and open points, and the go-ahead line at the end (Memory `go-ahead`, `review-handover`, `mark-done`). -->

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | 104-a 删除设计冲刺资产并重构 3 内核、4 角色、2 Claude 入口与 2 模板 | 删除 `skills/design-kernel/`（16 文件）、`commands/designer.md`、`template/design-backlog-template.md`；更新 `ideo/scrum/sprint-kernel` `SKILL.md`、4 角色命令、`agents/advisor.md`、`claude-skills/project-stakeholder/SKILL.md`、`product/ideo-backlog-template.md` | ✓ 2026-11-24 删除清单全部移除；3 内核与 4 角色无 `design-kernel`/`Designer`/`DesignBacklog` 残留；所有 `description` ≤ 1024 字符；`sprint-kernel` 内联 SGEP 摘录与参考文件逐字一致 |
| 2 | 104-b + 106-a 重构 Memory（`SKILL.md` 与留存 13 份 `details/`）及 `sprint-backlog-template.md` | 删除 `details/design.md`、`details/design-ending.md`；更新 `memory/SKILL.md` 与留存 13 份细则（4 纪律落位、单主轨 `flow-maps.md`、`IdeoBacklog` 归档与原型／证据口径、白纸与失败假设反推、删 `no-steps` 留 `go-ahead` 的 `sprint.md` 与 `departures.md`）及 `sprint-backlog-template.md` | ✓ 2026-11-24 Memory 清单与 13 份细则相对路径全解析、无死句柄；`departures.md` 收敛为 6 条；`no-steps` 与设计冲刺专属句柄清零 |
| 3 | 104-c 更新 Hook、DSH 适配与 `check_dsh.mjs` | 更新 `hooks/commitments.sh`、`hooks/hooks.json`、`dsh/index.js`、`dsh/commitments.js`、`dsh/locale/{en,zh}.json`、`scripts/check_dsh.mjs` | ✓ 2026-11-24 `node --test scripts/check_dsh.mjs` 全过（含忽略残余 `design-*/` 负例）；`commitments.sh` 实测单/多冲刺与忽略旧设计日志均退出 0；`claude plugin validate --strict plugins/ideo-scrum` 通过 |
| 4 | 105-a 重构看板规范、HTML 模板与 `board_check` 校验套件 | 更新 `board/board-log.md`、`board/scrum-board-template.html`、`scripts/board_check/check.py`（表头匹配第 3 章工作项表兼容 PBI-106）与 `fixtures/acme/`；删除 `prepare_review.py`、`fixtures/review-expectations.json`、`design-*` 与 `ideo-delta/` 夹具 | ✓ 2026-11-24 `python -X utf8 -I scripts/board_check/check.py selftest` 全过（含表前方案表、无工作项表、忽略旧 `design-*/` 与 `ideo-*/` 新用例）；用本仓日志生成 `ScrumBoard.html` 通过 `check --render` |
| 5 | 104-d + 105-b + 106-b 版权清零、中英文档、校验脚本、新版看板截图与 `AGENTS.md` 同步 | 更新 `ATTRIBUTION.md`、`README*.md`、`docs/{quick-start,maintaining,project-agents}*.md`、`docs/glossary.md`、`scripts/check_docs.py`、`AGENTS.md`（仅第 13/31/45 行，不动 `CLAUDE.md`）；用新版纯 Scrum 看板重截替换 `docs/images/board-overview{-light,}.png` | ✓ 2026-11-24 `python -X utf8 -I scripts/check_docs.py` 与 `--selftest` 0 错；全仓旧路径／旧称法／Knapp 版权 grep 除 §2.2 放行清单外命中 0；双色截图不含设计卡且正常显示 |
| 6 | 104-e 大改约定审阅门禁（Master 审阅 + 全新 Codex 对抗审查）与修订提交 | 完成全部内容改动的 Master 审阅与全新 Codex 对抗审查，逐条闭环修订；提交内容改动（不含改号） | ✓ 2026-11-24 Master 独立复核 `97bbc54` 通过：8 组 Codex 采纳项与 PO 清理 `scrum/sprint-26-plugin-memory/` 全部闭环、静态校验全绿 |
| 7 | 104-f 升号 `0.8.0`（Breaking）独立提交与冻结 Test 脚本／判据 | 独立提交更新 `plugin.json`、`package.json`、中英 `README` 首行版本与 `CHANGELOG.md`（`## [0.8.0]` 标 Breaking 并附旧 `scrum/design-*/` 迁移说明）；提交冻结触发与边界回归脚本及通过线 | ✓ 2026-11-24 Commit A（`83ed411`）纯 `0.8.0` 升号与 CHANGELOG 全套静态校验全绿；Commit B 冻结 `test-criteria.md` 与 `run_s28_tests.py`（`selftest` 34/34 通过，未提前跑正式测试） |

**方案设计**

- **A. Memory 删改句柄清单与 4 条纪律落位（PBI-104 / PBI-106）**
  - **删除文件（2 份）**：`details/design.md`、`details/design-ending.md`。
  - **删除句柄（22 条）**：整节 `Running a design sprint` 删 18 条（`question-needs-design`、`open-a-design`、`hard-point-only`、`design-roles`、`one-session-both-roles`、`design-branch`、`design-folder`、`design-stages`、`talk-with-po`、`choose-with-po`、`combine-or-rumble`、`storyboard`、`criteria-before-test`、`design-ends`、`design-conclusions`、`ideo-in-every-stage`、`ideate-arrangement`、`small-design`），另删 `sprint-or-modes`、`research-as-empathize`、`designs-beside-sprints`、`no-steps`。
  - **4 条自有操作纪律落位**（写入 `memory/SKILL.md` 的 *The five modes and the IDEO log*、`details/ideo-ending.md` 及 `ideo-kernel/SKILL.md`，不留 Knapp 摘录）：
    1. `diverge-first`（自原设计节迁入重写）：构思先发散再收敛——至少用两种方法且含至少一种 `ideo-kernel` Ideate 方法，先追求数量、暂缓评判，再收敛方案；
    2. `isolated-sketches`（新增短句柄）：需要多条思路不同的方案时，派多个互不可见的全新子代理各自发散起草，不共享同一份示例摘要，防趋同；
    3. `prototype-not-increment`（新增短句柄）：原型只为学习，低保真快做，绝不进入 Increment；关联冲刺在用时可留在冲刺里参考复用并随收官清理，无锚定或收口后无用时允许删原型文件；
    4. `keep-test-evidence`（新增短句柄）：无论结论是否落地，测试证据（谁测了、观察到什么、回答了什么问题）与结论记录均写入 `IdeoBacklog.md` 第 5 章或所服务日志，随日志归档至 `scrum/documents/ideo/`。
  - **核心细则改写点**：
    - `details/product-log.md`：`blank-page` 改为写不出产品或 Product Goal 时补做 Empathize／Define 五模式（不再指向设计冲刺）；在产品目标／问题梳理处浓缩 1–2 句「从失败假设反推关键问题」可选技巧（同步放 `ideo-kernel/SKILL.md`）；`item-columns` 的 `Status` 去 `in a design`；`architecture-map` 去 Knapp 摘录引用、保留自足画图规则。
    - `details/ideo-ending.md`：去 `Outside a design` / `Inside a design` / `DesignBacklog.md`；写明默认不另开独立分支（服务 Sprint 跟该 Sprint 共用分支，服务产品日志在当前分支／`main`），归档在下一次 Sprint Review 移入 `scrum/documents/ideo/`（冷启动尚无 Sprint 时随首个 Sprint 或 PO 确认归档），并落地上述 4 条纪律及原型文件 vs 测试证据区分口径。
    - `details/flow-maps.md`：删 `## A design` 整图；重写全流程图与各日志图——**IDEO 五模式画为共享工具箱底座，不画成产品日志旁的平级分叉分支，产品日志向下只有 Scrum Sprint 单主轨**。
    - `details/roles.md`、`gates.md`、`goal-fixed.md`、`refinement.md`、`closing.md`、`folders.md`、`handoff.md`、`names.md`：同步清零设计冲刺与 Designer 残句，`three-layers` 与 `scrum-folders` 仅保留产品日志／冲刺日志／Increment 及 `scrum/ideo-<suffix>/`、`scrum/documents/ideo/`。
- **B. 4 角色职责边界与内核／入口契约（PBI-104）**
  - 删除 `skills/design-kernel/`（16 文件）、`commands/designer.md`、`template/design-backlog-template.md`。
  - 4 角色加载序与分工（Claude Code 顺序加载；DSH 预载 `ideo-kernel → scrum-kernel → memory`，按需加载 `sprint-kernel`）：
    - `scrum-master`（`ideo → scrum → sprint → memory`）：守流程、审阅、引导 Planning/Refinement/Review/Retro，并**陪 PO 做 Empathize／Test**；遇白纸或精化难题直接引入 IDEO 五模式（1–2 方法就地记，多轮开 `IdeoBacklog.md`）。
    - `developer`（`ideo → scrum → sprint → memory`）：负责 Sprint How 与 Increment，并**承接 IDEO 发散／原型／测试**，显式守住先发散再收敛、隔离子代理防趋同、低保真原型不进 Increment、保留测试证据。
    - `stakeholder`（`ideo → scrum → memory`）：独立外部视角（删 `Designer` 称法，留 `Increment or prototype`）。
    - `supporter`（`ideo → scrum → memory`）：杂活、看板与 PO 联络点（删 `design` 日志与 `Designer` 称法）。
  - Claude 专属入口：`agents/advisor.md`（删 `design-kernel` 与 `design sprint`，核第 9 行角色数措辞）、`claude-skills/project-stakeholder/SKILL.md`（删 `design-kernel`）。
  - 描述长度红线：修改 `ideo-kernel`、`scrum-kernel`、`sprint-kernel`、`scrum-master`、`developer` 等 `description` 后全部实测字符数 ≤ 1024；`ideo-kernel` 的 `IDEO-modes/` 与 `methods/` 原文摘录逐字不动。
- **C. Hook 与 DSH 适配层契约（PBI-104）**
  - `hooks/commitments.sh` & `hooks/hooks.json`：仅读 `scrum/ProductBacklog.md` 与 `scrum/sprint-*/SprintBacklog.md`，删 `DesignBacklog.md`、`designGoal`、`many_designs_*`；残余 `scrum/design-*/` 静默忽略，异常退出码恒为 0。
  - `dsh/index.js`：`kernels = ['ideo-kernel', 'scrum-kernel', 'sprint-kernel', 'memory']`、`roles = ['scrum-master', 'developer', 'stakeholder', 'supporter']`；删第 47–48 行 `design-kernel` 特判；`roleRouting` 仅按需加载 `sprint-kernel`。
  - `dsh/commitments.js` 与 `dsh/locale/{en,zh}.json`：移除 `designGoal`、`DesignBacklog.md` 分支与 `/designer`；`scripts/check_dsh.mjs` 同步断言并新增「残余 `design-*/` 不入承诺上下文」负例。
- **D. 看板纯 Scrum 契约与 `board_check` 表头匹配规则（PBI-105）**
  - `board/board-log.md`：顶部加透明度声明「看板聚焦产品与 Scrum Sprint 状态，不覆盖独立 IDEO 研究日志」；数据 schema 仅含 `lang`、`generated`、`product`、`items`（`group ∈ {"sprint", "next", "later"}`）、`sprints`（移除 `designs` 与 `sprints[].ideo`）。
  - `board/scrum-board-template.html`：删除 `--design` 样式、`designCard`、设计节点／连线、`ideoLines`、`design` 分组与对应双语文案；保留 `s.blocks` 有表即画、空表自动隐藏第 3 层。
  - `scripts/board_check/check.py`：`LOG_FILES = {"sprint": "SprintBacklog.md"}`，`GROUPS = ("sprint", "next", "later")`，移除设计卡与 IDEO 状态机；**第 3 章工作项表匹配规则**：提取 `## 3.` 至下一 `##` 标题之间的全部 Markdown 表格，仅选中表头同时包含 `Work item`（或 `工作项`，忽略大小写）且包含 `Done when`（或 `完成条件`）的 4 列表解析 `(r[0], r[1], r[3].startswith("✓"))`；章内存在其他方案对比表时跳过，无匹配工作项表时返回 `blocks = []` 不报错；对历史回验页面里可能残留的多余顶层键不硬报错。
  - 夹具与工具清理：删 `scripts/board_check/prepare_review.py`、`fixtures/review-expectations.json`、`fixtures/acme/scrum/design-*`、`ideo-delta/`；更新 `acme/scrum/ProductBacklog.md`、`selftest()`，并用本仓新版看板重截浅色／深色两图替换 `docs/images/board-overview{-light,}.png`。
- **E. Sprint How 新措辞切口、`How ↔ Ideate` 锚定与 `departures.md` 同步（PBI-106）**
  - 删 `no-steps`；改写 `how-is-a-plan`、`details/sprint.md`、`template/sprint-backlog-template.md`、`commands/developer.md`、`details/flow-maps.md`、`docs/quick-start*.md` 与 `skills/sprint-kernel/SKILL.md`：明确第 3 章是 Developer 的方案式计划，可自由展开技术方案、权衡、接口与步骤；**显式锚定 `How ↔ Ideate`**（多路线／设计／架构取舍时先读 `../ideo-kernel/IDEO-modes/ideate.md` 按 Ideate 先发散再收敛、必要时隔离子代理防趋同；做法明晰的小改动不凑仪式），并在 `sprint-kernel/SKILL.md` 与 `details/sprint.md` 附一张轻量「Sprint 五阶段按需调用 IDEO 五模式」对照；保留 `# | Work item | Output | Done when` 工作项追踪表（每项 ≤1 会话、`✓ <date>` 标记）与末行 `Go-ahead:` 放行门。
  - `details/departures.md`：删 `Designs sit beside Sprints` 行，将 How 行改写为 `Building waits for the go-ahead`（偏离 Scrum Guide `"at the sole discretion of the Developers"`：SM/PO 审方案且施工等 PO 放行，因 AI 仍可能跑偏；总计 6 处偏离）；中英 `README` 的 `How it differs` 表与 `departures.md` 逐字一致，受 `check_docs.py` 强制校验。
- **F. Test 冻结脚本与通过线草案（工作项 7 单独提交冻结，开跑前不改线）**
  - **静态与双宿主**：`claude plugin validate --strict plugins/ideo-scrum` 0 错；Master 派全新 `plugin-validator`（Haiku）0 阻塞；`node --test scripts/check_dsh.mjs` 全过；`npm pack --dry-run --json --ignore-scripts` 确认无旧文件；DSH 网页端（侧边栏浏览器）实装验证 4 角色入口、3 内核 + Memory 预载与承诺注入。
  - **看板、文档与迁移**：`check.py selftest` 全过 + 本仓 `ScrumBoard.html` 通过 `check --render`；`check_docs.py` 与 `--selftest` 0 错；全仓旧路径／旧称法／Knapp 版权 grep 除 §2.2 放行清单外命中 0；全组件 `description` ≤ 1024 字符。
  - **LLM 触发与关键边界回归**（使用已配好的 `claude` 命令、隔离临时目录运行）：① 触发组：原 Q11 直接路径 3/3 命中 `ideo-kernel`（覆盖关闭 PBI-103）；Q9、Q10 直接路径各 ≥2/3 命中 `ideo-kernel`；Q2、Q3（白纸）经 `/ideo-scrum:scrum-master` 各 3/3 正确加载且不提设计冲刺；通用 Scrum 泛问（2 题 × 2 次）0/4 误触发 `scrum-kernel`/`sprint-kernel`。② 边界组：How 放开场景（2 次）产出方案 + 工作项表且 0/2 越过 `go-ahead` 动手改源码；原型边界场景（2 次）保持低保真且 0/2 将原型写入正式 Increment。

**Key choices**

- **保留 `details/ideo-ending.md` 原文件名承载 4 纪律与 IDEO 生命周期**：避免无谓改名引入旧路径迁移噪音，同时直接对齐 §2.2 既有引用；仅删 `design.md` 与 `design-ending.md`。
- **第 3 章工作项表按表头识别而非按「第一张表」盲抓**：彻底解除 PBI-106 放开 How 形态后与 `board_check` 的结构性冲突，既允许在方案区写对比表，也不破坏看板进度条。
- **内容改动与 `0.8.0` 升号严格分提交，并在升号前完成 Master + Codex 双重审阅**：严格遵守仓库规矩（「内容改动与改号分开提交」「大改约定走 Master 审 → 全新对抗审查」），避免版本提交与规范修订混杂。
- **保留 `ideo-kernel/` 内 d.school 原文摘录逐字不动**：正文中的 5 处普通英文词 `designer` 属第三方原文（CC BY-NC-SA），按「原文优先」规矩列进 grep 放行清单而不篡改原文。

**Risks and open points**

- **`check_docs.py` 中英对等强校验风险**：`README`、`quick-start`、`maintaining`、`project-agents` 任何增删行、列表项、表格行、链接或 `departures.md` 措辞偏差都会触发报错；每个文档改动后须立即跑 `check_docs.py` 与 `--selftest` 双验。
- **`ideo-kernel` 触发波动风险**：删掉 `design-kernel` 后 `ideo-kernel` 描述变短且职责更清晰，但原 Q11 题面含「设计目标和地图」旧词，需确保新 `description` 保留「design / 设计 / 目标与流程梳理 / 用户研究」相关自然触发信号，同时不过度触发无关代码设计请求。
- **DSH 网页端实装与浏览器截图环境**：重截 `docs/images/board-overview{-light,}.png` 与 DSH 网页端验证需确保本地无头浏览器／DSH 网页服务可用；若遇环境阻塞立即上报 Master。
- **`scrum/ProductBacklog.md` 更新时机**：产品日志的 §1.3 DoD（删 `/ Sprint`）、§2.2 架构图（去 Designer 与设计冲刺分支）与 PBI-103/104/105/106 状态刷新留到 Review 收官统一做，施工阶段不提前改 `ProductBacklog.md`。

Go-ahead: 2026-11-24，PO SeaPawn 正式批准第 3 章 How 方案（含 `How ↔ Ideate` 锚定）并给出施工放行与全流程授权——Developer（`sprint-28-dev`）可在 `sprint-28-drop-design-sprint` 冲刺分支上施工并提交（内容改动与 `0.8.0` 升号分提交）；Master（`lead`）获授权全权代行后续审阅、Test 放行、Review/Retro 收官、合入 `main`、打 `sprint-28-drop-design-sprint` 与 `v0.8.0` tag、推送 `origin` 及更新本机插件（逐字原话与仍回 PO 边界记于第 4 章）。本决定时 Sprint Goal 原文：「把插件收敛为「Scrum Sprint 单主轨 + IDEO 五模式工具箱」：去掉设计冲刺与 Designer 角色、让看板聚焦 Scrum、让 Sprint 的 How 回归真正的方案计划，让熟手与陌生人不再在两套流程间纠结，照着一套清晰且无全版权包袱的规矩就能走通探索与交付。」

## 4. Increment notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (Memory `increment-notes`, `mark-done`, `goal-fixed`). A session that picks up the Sprint reads these first. Record the Product Owner’s decision on the Increment and whether the Sprint Test has been authorized. Developer checks inside building are not this Test (Memory `stage-gates`, `read-the-goal`). -->

### PO 2026-11-24 全流程放权记录（按 `AGENTS.md` 逐字记录）

- **PO 原话（逐字，2026-11-24 02:53，主会话）**：「呃，不必了，后面我直接把权利授据权给你好吧，就是后面你就是啊。已经有所有权利了，除非说有问题的话再向我报告，没有问题就不需要向我报告。然后，呃，然后对，然后就是说就差不多，我就不用管了，就你们自己就是说把这个流程全部走完，然后定好版本，然后升，然后推送更新就可以了。嗯，授权 developer 开始个施工，就是我放进之后，他就啊可以施工了。最后合并，然后 tag 和 pass 的时候，你来做就行，我就授权给你了。」
- **授权范围**：施工放行（`go-ahead`）；PO 免中途全文强审（改为 Master 审阅 + 全新 Codex 对抗审查闭环）；Master 代行后续阶段决定（Test 放行、Review 与 Retro 收官）；合入 `main`、打 `sprint-28-drop-design-sprint` 与 `v0.8.0` tag、推送 `origin`、更新本机插件并清理分支与工作树。
- **仍回 PO 的事项（红线不代行）**：修改 Product Goal、取消冲刺、推翻 PO 已说过的话、PO 点名要看的品味、GitHub Release 等超出 `git push` 的公开发布、改动 `CLAUDE.md` 或超出本次已授权 3 处（第 13/31/45 行）之外的 `AGENTS.md`、以及施工／审查／Test 中遇到阻塞或未过线问题（立即停下回报 PO）。

### 2026-11-24 施工记录（工作项 `#1`～`#5`，`sprint-28-dev`）

- **`#1`（`104-a`）**：删除 `plugins/ideo-scrum/skills/design-kernel/`（16 文件，含 Knapp《Sprint》15 篇全版权摘录）、`plugins/ideo-scrum/commands/designer.md`、`plugins/ideo-scrum/template/design-backlog-template.md`。重构 `ideo-kernel`、`scrum-kernel`、`sprint-kernel`（新增 `How ↔ Ideate` 锚定与「Sprint 五阶段按需调用 IDEO 五模式」对照表，保持 SGEP 内联摘录逐字未损），精简 4 角色命令（Master 陪 PO 共情／测试、Developer 承接 Ideate/Prototype/Test 与原型不进 Increment 边界）、更新 `agents/advisor.md`（删 `fifth Scrum role` 与 `design-kernel`）、`claude-skills/project-stakeholder/SKILL.md`、`template/{product,ideo}-backlog-template.md`。全组件 `description` 复量均 ≤ 1024 字符（最长 `supporter.md` 977、`scrum-kernel` 943、`sprint-kernel` 940、`ideo-kernel` 894）。
- **`#2`（`104-b + 106-a`）**：删除 `memory/details/design.md`、`details/design-ending.md`；重构 `memory/SKILL.md`（103 → 84 条句柄：删 22 条、新增 `isolated-sketches` / `prototype-not-increment` / `keep-test-evidence` 并重写 `diverge-first` 落位于 *The five modes and the IDEO log*）与留存 13 份 `details/`（含 `sprint.md` 放开 How 并附 `How ↔ Ideate` 及五阶段对照、`departures.md` 收敛为 6 条偏离、`ideo-ending.md` 写明 4 纪律＋默认不另开分支＋关联冲刺原型复用清理＋测试证据归档至 `scrum/documents/ideo/`、`product-log.md` 白纸走 Empathize/Define＋失败假设反推、`flow-maps.md` 改为 IDEO 底座共享工具箱＋Sprint 单主轨）及 `template/sprint-backlog-template.md`。
- **`#3`（`104-c`）**：更新 `hooks/commitments.sh`（纯 LF 验证通过，未用 `find`）、`hooks/hooks.json`、`dsh/index.js`（删 `design-kernel` 特判与 `designer`）、`dsh/commitments.js`、`dsh/locale/{en,zh}.json`、`scripts/check_dsh.mjs`（补残余 `design-*/` 忽略负例）。实测：`node --test scripts/check_dsh.mjs` 9/9 通过；POSIX `sh`（`E:\GIT\Git\bin\sh.exe`）实测单冲刺、多冲刺与忽略残余 `design-old/DesignBacklog.md` 均退出 0；`claude plugin validate --strict plugins/ideo-scrum` 0 错通过。
- **`#4`（`105-a`）**：更新 `board/board-log.md`（顶部补纯 Scrum 透明度声明）、`board/scrum-board-template.html`（彻底移除 `--design`、`designCard`、`ideoLines`）、`scripts/board_check/check.py`（移除设计卡与 IDEO 状态机；`work_item_table()` 改为按表头识别第 3 章含 `Work item`/`工作项` 与 `Done when`/`完成条件` 的 4 列表，跳过方案对比表、无表返回 `[]`）与 `fixtures/acme/scrum/ProductBacklog.md`；删除 `prepare_review.py`、`fixtures/review-expectations.json`、`fixtures/acme/scrum/{design-*,ideo-delta}/`。实测：`board_check/check.py selftest` 39/39 通过；用本仓真实日志生成 `scrum/ScrumBoard.html`（已 `.gitignore` 不入库）通过 `check --render`（`pbi: 10, nodes: 1, cards: 2, fail: false`）。
- **`#5`（`104-d + 105-b + 106-b`）**：更新 `ATTRIBUTION.md`（清零 Knapp 第 4 节与 `Simon & Schuster`）、中英 `README`（与 `departures.md` 6 条逐字对齐，版本号仍守 `0.7.0`）、`docs/{quick-start,maintaining,project-agents}*.md`、`docs/glossary.md`（删 7 设计冲刺词条）、`scripts/check_docs.py`、`AGENTS.md`（仅改 PO 授权的第 13/31/45 行，未动 `CLAUDE.md`）；用 Edge 无头模式按本仓新版纯 Scrum 看板重截 `docs/images/board-overview-light.png` 与 `docs/images/board-overview.png` 并肉眼复核无设计卡。实测：`check_docs.py` 9 篇 188 链接 0 错，`check_docs.py --selftest` 17/17 通过，`npm pack --dry-run --json --ignore-scripts` 91 文件且 0 旧设计资产，全仓 grep 除 §2.2 放行清单及测试负例与 SGEP 原文文献 `[20]` 外命中 **0**。
- **红线守卫**：未改版本号（仍 `0.7.0`）、未改 `CHANGELOG.md`、未改 `CLAUDE.md`、未改 `scrum/ProductBacklog.md`、未 merge/tag/push。下一步交 Master 进入 `#6` 审阅与全新 Codex 对抗审查。

### 2026-11-24 `#6` 审阅修订与遗留清理记录（`sprint-28-dev`）

- **PO 清理遗留目录指示（Memory `po-word-relayed`）**：
  - `PO (via Supporter, 2026-11-24 03:47, S:\SeaPawn Supporter 会话 session-bc74018b): 「那肯定是删掉啊，直接很奇怪啊，为什么不删呢？」` —— Master 决定在 Sprint 28 `#6` 顺手删除 `scrum/sprint-26-plugin-memory/` 并同步取消放行清单豁免。
  - 已彻底删除整个 `scrum/sprint-26-plugin-memory/`（110 个文件，含 `memory-draft/`、`review/`、`scripts/`；Sprint 26 已归档在 `scrum/documents/sprint/sprint-26-plugin-memory*.md`），并同步从本日志 §2.2 第 5 点全仓 grep 放行清单中移除 `scrum/sprint-26-plugin-memory/`。
- **Codex 对抗审查（`codex-s28-review`）采纳项逐条处置**：
  1. **`[高-1 + 中-1 + 低-3]` `plugins/ideo-scrum/hooks/commitments.sh`**：`find_root_set` 逐级拒绝 `$d/scrum` 与 `$d/scrum/ProductBacklog.md` 为 symlink，未命中且 `[ -e "$d/.git" ] || [ -L "$d/.git" ]` 时立即 `return 1` 止步不越界；开放冲刺循环逐级拒绝冲刺目录与 `SprintBacklog.md` 为 symlink；`read` 去掉 `rest` 以保留承诺正文中的真实 tab；保持纯 LF、POSIX `sh`、不用 `find`。经 `E:\GIT\Git\bin\sh.exe` 全用例实测通过（单冲刺、多冲刺、忽略 `design-*/`、嵌套 `.git` 目录与 `.git` 文件均止步、含 tab 承诺原文保真、Windows 原生 symlink 四类拦截全过）。
  2. **`[高-2]` `scrum/sprint-28-drop-design-sprint/SprintBacklog.md:84`**：已将 §3 残留 `short and not in detail` / `no-steps` 的旧模板 HTML 注释替换为 `plugins/ideo-scrum/template/sprint-backlog-template.md:37` 现行注释。
  3. **`[中-2/3/4]` `scripts/board_check/check.py`**：新增 `split_table_row()` 供 `parse_table_rows()` 与 `table_after()` 共用，按未转义管道符拆列并还原 `\|` 为 `|`；`work_item_table()` 第 3 章起点收紧为 `^##\s*3\.`，并按表头动态定位 `#` 列索引 `id_idx`；在 `selftest()` 补齐转义 `\|`、非默认列序、`### 3.` 子标题干扰回归用例（自测 39 → 43 全过）。
  4. **`[中-5]` `plugins/ideo-scrum/skills/memory/details/flow-maps.md:31-34`**：全流程图改为从 `IDEO` 分别虚线连向 `A` 与 Sprint 五阶段 `S1`–`S5`，与同文件 Sprint 图及五阶段对照表一致。
  5. **`[中-6]` `plugins/ideo-scrum/commands/developer.md:34`**：将 `IdeoBacklog.md or the Sprint log` 改为 `IdeoBacklog.md or the log served (the Sprint or product log)`。
  6. **`[低-2]` `scripts/check_docs.py:207-212`**：Departures 表校验收紧为同时检测未知行、重复行、行数差及顺序错位（保证 `got != departures` 必报错），并在 `--selftest` 补齐换序与重复行用例（自测 17 → 19 全过）。
  7. **`[低-4]` `plugins/ideo-scrum/skills/ideo-kernel/SKILL.md:25-29`**：将 4 条独立纪律列表项与 4 个句柄（`diverge-first`、`isolated-sketches`、`prototype-not-increment`、`keep-test-evidence`）拆清一一对应，`Optional Empathize/Define prompt` 移出列表作为下方独立一句。
  8. **`[低-5]` `ATTRIBUTION.md:6-8`**：澄清第 8 行为不含任何**未授权商业书籍**全文或原始出版物，第三方内容均为遵循对应公开许可（CC BY-SA / CC BY-NC-SA）的署名全文或方法摘录（同步将第 6 行小标由「第三方摘录」改作「第三方内容」保持前后一致）。
- **Master 明确不采纳的 3 条 Codex 意见（未改对应文件）**：
  1. `docs/maintaining*.md:37`「五个角色」：系 2026-11-23 对 `0.7.0` 的历史实测记录（`0.7.0` 确为 5 角色），不可改写历史证据；现行架构第 15 行已是 4 角色。
  2. `plugins/ideo-scrum/template/sprint-backlog-template.md:37`（`IDEO-modes/ideate.md`）：按 Sprint 17 规矩，模板复制到项目 `scrum/sprint-NN-*/` 后无法解析插件内相对 `../` 路径，故保持技能名＋包内相对路径写法。
  3. `README*.md:116`：陈述 Claude Code 宽泛提示下的已知宿主实测限制（`a known limitation`），与触发契约不冲突，保留。
- **状态说明**：本修订提交仍守版本号 `0.7.0`、未碰 `CHANGELOG.md` / `CLAUDE.md` / `scrum/ProductBacklog.md`、`AGENTS.md` 仍仅改 PO 授权第 13/31/45 行；工作项 `#6` 暂不打 `✓`，交 Master 复核确认。

### 2026-11-24 `#7` 升号 `0.8.0`（Commit A）与冻结 Test 判据／脚本（Commit B）（`sprint-28-dev`）

- **`#6` Master 独立复核通过**：Master 已完成对 `97bbc54` 的逐文件独立复核，8 组 Codex 采纳项与 PO 指示清理 `scrum/sprint-26-plugin-memory/` 全部通过，授权为 `#6` 打 `✓ 2026-11-24`。
- **Commit A（`83ed411`，纯 `0.8.0` Breaking 版本升级，不夹带脚本与日志）**：
  - 改动 7 个文件：`plugins/ideo-scrum/.claude-plugin/plugin.json`、`package.json`、`README.md`（第 5/69 行）、`README.zh-CN.md`（第 5/69 行）、`docs/maintaining.md`（第 45 行）、`docs/maintaining.zh-CN.md`（第 45 行）、`CHANGELOG.md`（新增 `## [0.8.0] — 2026-11-24` Breaking 条目与旧 `scrum/design-*/` 迁移说明）；保留既有 `0.6.3 → 0.7.0` 历史升级记述与 `0.7.0` 历史实测表未动。
  - 静态验证全绿：`claude plugin validate --strict plugins/ideo-scrum`（exit 0，0 错）、`node --test scripts/check_dsh.mjs`（9/9）、`npm pack --dry-run --json --ignore-scripts`（`@seapawn/ideo-scrum@0.8.0`，91 文件）、`python -X utf8 -I scripts/check_docs.py`（9 篇 188 链接 0 错）与 `--selftest`（19/19）、`python -X utf8 -I scripts/board_check/check.py selftest`（43/43）。
- **Commit B（冻结 Sprint 28 Test 判据与回归脚本）**：
  - 新增 [test-criteria.md](test-criteria.md)（对齐 §1.2、§2.2、§3 F 与 `scrum/documents/headless-testing.md`，冻结静态／双宿主、看板／文档／版权、Claude Code 无头 T1/T2/T3 通过线及旧术语肯定／否定子句判定与人工复核规则）；
  - 新增 [run_s28_tests.py](run_s28_tests.py)（复用 `scripts/stranger_test/driver.py` 白名单隔离、`neutral_parent`、`/context all`、`magpie claude run` 与 `taskkill /T /F` 进程树清理；从 Commit A `83ed411` 经 `git archive` 导出 `0.8.0` 插件核实 `Base directory`；T3 使用 `acceptEdits` 并在 `smoke` 实测可写以避免权限假阳性；支持 `selftest` / `smoke` / `run` / `report`）；
  - 冻结前仅运行 `python -X utf8 -I scrum/sprint-28-drop-design-sprint/run_s28_tests.py selftest`：**34/34 PASS**（未提前运行正式测试）；
  - 为 §3 `#6` 与 `#7` 勾选 `✓ 2026-11-24`，确认 `CLAUDE.md` 与 `scrum/ProductBacklog.md` 仍未改动。
- **阶段状态**：**Increment 已齐备（`#1`–`#7` 全部完成），待 Master 核验后代行放行 Sprint Test。**

## 5. Test

<!-- Record the Developer’s tests, the independent review and any required Product Owner acceptance. Trace each Output Done standard and item criterion to new evidence, still-valid earlier evidence and why it holds, or a stated condition that did not arise and why. Keep missing evidence visible; record outcome signals separately and judge the Test against the pass lines set beforehand (Memory `record-the-tests`). End with the Product Owner’s close or return decision (Memory `stage-gates`, `read-the-goal`). -->
