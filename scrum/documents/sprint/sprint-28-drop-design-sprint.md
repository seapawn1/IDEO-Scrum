# Sprint Backlog — Sprint 28 (drop-design-sprint)

> Started: 2026-11-24 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `sprint-28-drop-design-sprint` | Product Owner: SeaPawn | Scrum Master: `lead` | Developer: `sprint-28-dev`
> Now: 已收官 · 2026-11-24，Master 按 PO 2026-11-24 全流程放权代行收官；发布 `v0.8.0`（Breaking），合入 `main`、打 `sprint-28-drop-design-sprint` 与 `v0.8.0` tag 并推送 `origin`。
> Waiting for PO: None
> 归档：在办日志全文、冻结 Test 判据与无头回归脚本见 `6839235` 树中的 `scrum/sprint-28-drop-design-sprint/`（`SprintBacklog.md`、`test-criteria.md`、`run_s28_tests.py`）。仓外原始证据归档于 `S:/IDEO-Scrum-Archives/sprint-28-drop-design-sprint/`（`plugin-0.8.0/`、`trials/`、`dsh-s6-web/`、`report.md`）。

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 把插件收敛为「Scrum Sprint 单主轨 + IDEO 五模式工具箱」：去掉设计冲刺与 Designer 角色、让看板聚焦 Scrum、让 Sprint 的 How 回归真正的方案计划，让熟手与陌生人不再在两套流程间纠结，照着一套清晰且无全版权包袱的规矩就能走通探索与交付。 |
| --- | --- |

### 1.2 Definition of Done

[完整产品 DoD](../../ProductBacklog.md#13-definition-of-done) 全部生效。本期重点核验：① 结构与双宿主验证（`claude plugin validate --strict`、独立 `plugin-validator`、`check_dsh.mjs`、DSH 网页端 4 角色实装）；② 看板、文档与迁移（`board_check` 自测与纯 Scrum 看板渲染、`check_docs.py` 无死链、全仓旧路径／旧称法 grep）；③ 触发与关键边界回归（纯 `ideo-kernel` 覆盖原设计类题 Q11、其余内核不回退、`How` 放开后守住 `go-ahead` 与原型不进 Increment）；④ 版权与署名（Knapp《Sprint》全版权摘录与 `Simon & Schuster` 清零）。目标版本 `0.8.0`（Breaking）。

## 2. What

### 2.1 Product Backlog Items

- **PBI-104**：移除设计冲刺与 Designer 角色，统一为 Sprint + IDEO 五模式。
- **PBI-105**：看板移除设计冲刺卡，只保留产品卡与冲刺卡。
- **PBI-106**：Sprint How 放开形态约束，回归 Scrum 原文。
- **PBI-103**（不作为开发项进 2.1，在纯 `ideo-kernel` 触发回归覆盖原 Q11 后随 Review 关闭）。

### 2.2 Refinement 关键决定（PO 2026-11-24 定）

- **单主轨与工具箱（PBI-104）**：删除 `skills/design-kernel/`（16 文件，含 Knapp《Sprint》15 篇全版权摘录）、`commands/designer.md`、`template/design-backlog-template.md` 及 Memory 中设计冲刺细则（`details/design.md`、`design-ending.md`）。IDEO 五模式定位为所有实践的共享工具箱而非平级旁路；白纸冷启动写不出产品目标时走 Empathize／Define 补齐；保留 4 条本仓操作纪律（`diverge-first`、`isolated-sketches`、`prototype-not-increment`、`keep-test-evidence`）；角色精简为 4 个（Master 陪 PO 共情／测试、Developer 承接发散／原型／测试并守原型边界、Stakeholder、Supporter）；「失败假设反推」浓缩为 1–2 句自有约定放进 `product-log.md` 与 `ideo-kernel`（不留 Knapp 摘录）；保留 `scrum/ideo-<suffix>/IdeoBacklog.md`，默认不另开分支，下一次 Review 归档至 `scrum/documents/ideo/`。
- **纯 Scrum 看板（PBI-105）**：移除设计卡与独立 IDEO 展示，仅留产品卡与冲刺卡；`board-log.md` 顶部加透明度声明；Hook（`commitments.sh`）与 DSH（`dsh/commitments.js`）去掉设计目标扫描并静默忽略历史 `scrum/design-*/`。
- **Sprint How 回归方案计划（PBI-106）**：删 `no-steps`；第 3 章放开为充分方案式计划并显式锚定 `How ↔ Ideate`；保留 `go-ahead` 放行门与工作项表；`departures.md` 收敛为 6 条偏离；`board_check` 改为按表头匹配工作项表以兼容方案对比表。
- **文档与红线**：PO 专项授权同步 `AGENTS.md` 第 13、31、45 行（不动 `CLAUDE.md`）；内容改动与 `0.8.0` 升号分提交；保持 SGEP 与 d.school 原文摘录逐字不动；不重跑 PBI-63 陌生人大测试与 PBI-101 Memory 效果实验。

## 3. How

| # | 工作项 | 结果 |
| --- | --- | --- |
| 1 | `104-a` 删设计冲刺资产并重构 3 内核、4 角色、2 Claude 入口与 2 模板 | ✓ 2026-11-24（`b5a027d`） |
| 2 | `104-b + 106-a` 重构 Memory（103 → 84 句柄，留存 13 细则）与 `sprint-backlog-template.md` | ✓ 2026-11-24（`b5a027d`） |
| 3 | `104-c` 更新 Hook、DSH 适配与 `check_dsh.mjs` | ✓ 2026-11-24（`b5a027d`） |
| 4 | `105-a` 重构看板规范、HTML 模板、`board_check`（表头匹配）与夹具 | ✓ 2026-11-24（`b5a027d`） |
| 5 | `104-d + 105-b + 106-b` 更新 `ATTRIBUTION.md`、中英 README／docs、`check_docs.py`、`AGENTS.md` 3 行与双色看板截图 | ✓ 2026-11-24（`b5a027d`） |
| 6 | Master 独立审阅 + 全新 Codex 对抗审查闭环与清理遗留 `scrum/sprint-26-plugin-memory/` | ✓ 2026-11-24（`97bbc54`） |
| 7 | `0.8.0` Breaking 独立升号与 `CHANGELOG.md`（`83ed411`）+ 冻结 Test 判据与回归脚本（`7c2f1fd`） | ✓ 2026-11-24 |

## 4. Increment notes（关键决定与审查摘要）

- **PO 2026-11-24 全流程放权（原话）**：「呃，不必了，后面我直接把权利授据权给你好吧，就是后面你就是啊。已经有所有权利了，除非说有问题的话再向我报告，没有问题就不需要向我报告。然后，呃，然后对，然后就是说就差不多，我就不用管了，就你们自己就是说把这个流程全部走完，然后定好版本，然后升，然后推送更新就可以了。嗯，授权 developer 开始个施工，就是我放进之后，他就啊可以施工了。最后合并，然后 tag 和 pass 的时候，你来做就行，我就授权给你了。」仍回 PO 红线：改 Product Goal、取消冲刺、推翻 PO 原话、超出 `git push` 的公开发布、改 `CLAUDE.md` 或超出授权 3 行的 `AGENTS.md`、阻塞或 Test 未过线立即停报。
- **清理遗留目录（PO 经 Supporter，2026-11-24 03:47，`session-bc74018b`）**：PO 原话「那肯定是删掉啊，直接很奇怪啊，为什么不删呢？」——在 `97bbc54` 彻底删除 `scrum/sprint-26-plugin-memory/`（110 文件）并撤销 grep 豁免。
- **独立 Codex 对抗审查（`codex-s28-adv-review` 审 `b5a027d`）**：提出 4 Must-Fix + 5 Should-Fix；采纳 8 组修订落盘于 `97bbc54`（`commitments.sh` symlink 拦截／`.git` 止步／tab 保真、日志 §3 旧模板注释、`board_check` 转义 `\|` 与表头列定位、`flow-maps.md` 五阶段虚线、`developer.md` 补产品日志、`check_docs.py` Departures 顺序与去重、`ideo-kernel` 4 纪律拆清、`ATTRIBUTION.md` 澄清不含未授权商业书籍）；3 条不采纳（`maintaining*.md` 的 `0.7.0` 历史实测不改写、模板不写插件内 `../` 路径、`README*.md` 宿主限制说明保留）。
- **PO 2026-11-24 Test 阶段原话指示与裁定**：
  - 测试模型：「测试的话，其实你可以找一个比较轻量的对吧？不过你好像是做端到端测试。那也没关系了，那外部里面你就可以选那个 OpenCode 的 DeepSeek 去测试，然后 Claude Code 的话也是选 DeepSeek 的 OpCode 去测试.」
  - 首轮 `B1`（0/2，题面含 PO 直接说「并把代码也顺手改完」，依 `stage-gate-negative-prompts` 判为非有效负例）与 `Q3-1`（两次 300s 便宜模型过度读文件超时）立即停报 PO；PO 裁定：「`B1  选A  Q3选A吧`」——保留旧原始证据不删，不动 `83ed411` 插件本体，增干净负例 `B1b` × 2 与放宽至 420s 补跑 `Q3-1b` × 1（在 `test-criteria.md` 末尾追加第四节），全量证据提交于 `6839235`。
- **外部 Stakeholder Review（2026-11-24，全新独立子代理，非构建者）**：
  - **熟手（`review-veteran`）**：**0 阻塞**，总体**满意**（单主轨开、记、收与断线续接顺手利落）。非阻塞建议：① `scrum-master.md`/`developer.md`/`roles.md` 提及冲刺子代理时可补明按需载 `sprint-kernel`、`project-stakeholder` 补 `memory`；② `sprint-backlog-template.md` 头部 `add none` 可明示「允许章内分块」以减少与 How 完整方案的张力；③ 收官刷新 `ProductBacklog.md` §1.3 与 §2.2（本次 Review 已落实）。
  - **陌生人（`review-stranger`）**：**0 阻塞**，总体**满意**（装上即知第一句，专有词清晰，不问作者可走完第一个冲刺）。非阻塞建议：① `README`/`quick-start`/`glossary`/`roles.md` 写 SM／Developer 的五模式分工时补列「定义（Define）」；② 快速上手集中补两行「直接开 Sprint vs 1–2 方法 vs 开 `IdeoBacklog.md`」判断标准；③ 统一中文字眼「工作项」与「工作块」；④ 快速上手点明新手首冲刺可留在单会话由 SM 带跑。

## 5. Test

> 被测插件候选提交：`83ed411`（`0.8.0` 纯升号）；完整逐条证据见 `6839235` 树中 `SprintBacklog.md` §5 及仓外归档 `S:/IDEO-Scrum-Archives/sprint-28-drop-design-sprint/`。

- **静态、打包与双宿主（S1–S6 全过）**：`claude plugin validate --strict` 退出 0（0 errors，6 skills / 4 commands / 1 agent / 2 hooks）；独立 `plugin-validator`（`s28-plugin-val-080`）10 步全审 **PASS**（0 阻塞，3 条非阻塞提示）；`node --test scripts/check_dsh.mjs` **9/9 PASS**；`npm pack --dry-run` `@seapawn/ideo-scrum@0.8.0` 91 文件（0 已删设计资产）；`hooks/commitments.sh` 纯 LF（0 CR）且 POSIX `sh` 全用例通过；DSH 网页端（临时 profile `v28-s6`，Standard 模式，轻量测试模型）菜单实证 4 角色与 3 内核 + Memory（0 `/designer`、0 `design-kernel`），`/scrum-master` 会话原生 `session.v4.jsonl.zstd`（24 事件）验证 `ideo-kernel → scrum-kernel → memory` 严格按序预载与承诺注入。
- **看板、文档、版权与迁移（D1–D6 全过）**：`board_check selftest` **43/43 PASS**；本仓纯 Scrum 看板渲染校验 `ok: true, cards: 2, fail: false`（双色截图已更新复核）；`check_docs.py` 9 篇 188 链接 **0 errors**，`--selftest` **19/19 PASS**；全仓区分／不区分大小写 grep 除冻结放行清单外 **0 意外命中**；11 个组件 `description` 全部 ≤ 1024 字符（最长 977）；Knapp《Sprint》摘录与 `Simon & Schuster` 署名清零。
- **Claude Code 无头触发与边界回归（T1/T2/T3，从 `83ed411` 导出 `0.8.0` 副本，模型口径：magpie 的便宜模型，非 Haiku；冒烟 3/3 PASS，`/context all` 为 `[]`）**：
  - 全部 11 项有效试次达标：`Q11`（覆盖关闭 PBI-103）**3/3**、`Q9` **3/3**、`Q10` **3/3**、`Q2` **3/3**、`Q3`（`Q3-2` + `Q3-3` + PO 裁定补跑 `Q3-1b` 60.5s）**3/3**、`G1/G2` **0/4** 误触发、`R_STK` **1/1**、`R_SUP` **1/1**、PO 裁定干净负例 `B1b`（替换保留作废的 `B1`）**2/2**（`src/app.py` SHA256 不变、§3 落盘 Ideate 方案与工作项表、显式等 `go-ahead`）、`B2`（原型不进 Increment）**2/2**；全部有效试次 **0** 旧设计冲刺术语命中。
- **Output Done 与 Outcome Done**：Output Done **7/7 全过**（内容忠实、署名、可导航、无死链、插件校验、描述长度、DSH 分发）；Outcome Done 两条产品信号（PBI-63 陌生人大测试与 PBI-101 Memory 效果实验）按 §2.2 口径本期未新测，如实留白。

Test 判定（2026-11-24，Scrum Master `lead` 按 PO 全流程放权代行）：**通过，放行进入 Review 与收官**。当时的目标原文：「把插件收敛为「Scrum Sprint 单主轨 + IDEO 五模式工具箱」：去掉设计冲刺与 Designer 角色、让看板聚焦 Scrum、让 Sprint 的 How 回归真正的方案计划，让熟手与陌生人不再在两套流程间纠结，照着一套清晰且无全版权包袱的规矩就能走通探索与交付。」
