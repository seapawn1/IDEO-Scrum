# Sprint Backlog — Sprint 27 (wrap-up)

> Started: 2026-11-22 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `worktree-sprint-27-wrap-up` | Product Owner: SeaPawn | Scrum Master: IDEO # [master]-[main]-[manage sprint] | Developer: Sprint 27 Developer
> Now: 已收官 · 2026-11-23，PO 放行收官（经 Supporter）；该期版本不动（仍是 0.6.3 的未发布候选）、未推送、未发布。
> Waiting for PO: None
> 归档：在办日志全文见 `3793f84` 树中的 `scrum/sprint-27-wrap-up/SprintBacklog.md`，含 2.2 冻结的通过线与放行表、第 4 章全部决定记录、第 5 章逐条证据，以及同一文件夹 `validation/` 里的触发题面和各证据脚本。仓外原始记录在 `S:/IDEO-Scrum-Archives/sprint-27-wrap-up/`（`trigger/` 触发测试、`load/` 无头加载、`dsh/` DSH 会话记录、`codex/` Codex 审阅原文）。

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 秘书管杂活：看板、传话这类杂活交给秘书，PO 不用操心，各角色的叫法不再混；模板、看板各归其位，留下的小毛病补齐，熟手照着就能用。 |
| --- | --- |

依据：PO「27的话应该是建立秘书角色。对，我觉得可以稍微改一改。」英文名定为 `supporter`，中文叫「秘书」。

### 1.2 Definition of Done

[完整产品 DoD](../../ProductBacklog.md#13-definition-of-done) 全部生效。本期重点核验：署名（84：摘录正文逐字不动，diff 只动 Source／License 行、`ATTRIBUTION.md` 与两份 README 授权表里 d.school 的一行）；可导航、无死链（85 迁路径后全仓 grep 旧路径到零；90 的新 docs 进导航）；插件校验与描述长度（`claude plugin validate --strict` 通过，改过与新增的描述 ≤1024，重跑触发测试不比改前差）；DSH 分发（`check_dsh` 通过，另验实装与角色入口）；自检（`check_docs.py`、`board_check selftest`）。

## 2. What

### 2.1 Product Backlog Items

- **PBI-86**：全辅助的秘书角色 Supporter，各角色入口里旧的助手称法统一。
- **PBI-85**：四份日志模板与看板文件按用途收拢。
- **PBI-89**：看板认得收尾待归档的写法，说明与模板占位前后一致。
- **PBI-90**：Sprint 22 Review 的九条意见，项目 Agent 与参谋入口的说明补齐。
- **PBI-84**：IDEO 五模式摘录补齐 2010 与 2018 双源署名。

### 2.2 Refinement

- **Supporter 的定位与边界（PO 2026-11-22 定）**：名字 `supporter`，入口 `/ideo-scrum:supporter`。SGEP 写 Supporter 是 Stakeholder 的一种（"a specific Stakeholder type"，"doing what is requested"，"participate when and where needed or as requested"），本插件只取「照请求做事」这一面，作者的取舍在入口里用斜体标明；加载 ideo → scrum，不在入口钉 `model`。边界沿用：不排序、不决定、不审阅、不改插件文件，只传 PO 或 Master 已定的事。PO 随后追加三条：Supporter 是 PO 的联络点（收齐各日志头部 `> Waiting for PO:` 与各会话报来的待决问题，带上下文一次问 PO，再把答复原话带回）；Supporter 转达的 PO 意见视同 PO 的（依据 Scrum Guide 2020「The Product Owner may do the above work or may delegate the responsibility to others. Regardless, the Product Owner remains accountable.」；条件是标明、附原话与日期；工具权限与设置、`CLAUDE.md`／`AGENTS.md`、推送与发布不在此列）；三级分流（自己能定的自己定，归流程或书面授权内的问 Master，只有 PO 能定的交 Supporter 汇总），规则只写在 `overview.md` 约定 14，别处只引用。`scrum-master` 入口去掉旧的助手味，写成有权的 Master：守流程、审、在书面授权内代 PO 定。
- **85 的位置（Master 2026-11-22 按授权定）**：四份模板进插件根 `template/`，看板的 `board-log.md` 与 `scrum-board-template.html` 进 `board/`。依据：PO「模板专门拉一起放在 template 里面」；DSH 对照测在默认受限预设下，`skills/` 之外的包内路径也读得到。技能引用写 `../../template/<文件>`、`../../board/<文件>`，`package.json` 的 `files` 加这两个目录。
- **89**：三条建议都做（`check.py` 认无「已」的 `收官 · …`、阶段前缀后的宿主结束、`solution: null` 时亦省略 `story`；`ideo-backlog-template.md` 的 `For` 占位补提 `DesignBacklog.md`），脚本只放宽不收紧，每处配正负例。后来补一处：`check.py` 的 `product.source` 放宽到约定允许的 `branch <名> @ <提交>` 写法。
- **90**：九条里做 ①②④⑤⑦⑧⑨，⑥ 在快速上手补一行，③ 不做（改召唤示例要 Review 批准加实机验证，现有示例准确）；不动任何 `description`。
- **84**：2010 *Design Process Mini-Guide*（`CC BY-NC-SA 3.0 Unported`）为底本，2018 *Design Thinking Bootleg*（`CC BY-NC-SA 4.0`）补料 38 处；五个文件头与 `ATTRIBUTION.md` 第 3 节、两份 README 授权表三处一致，正文不动。
- **测试方法与通过线**（冻结于 `d72b0a6`，全文见在办日志 2.2）：静态检查四项加 `npm pack`；两条 grep（旧路径、旧称法）命中必须正好等于逐处列出的放行表（旧路径 2 处、旧称法 14 处）；完整 DoD 逐条；触发测试 A（杂活）、B（外部视角）、C（Master 事务）三组各 3 题，每题每臂 3 次，A 组改后臂 ≥6／9，B、C 不低于改前，两条混用线 ≤1／9；`/ideo-scrum:supporter` 无头加载 3／3；DSH 实装验收；独立审阅与角色边界对抗核对；Outcome 本期不设必须的信号。

## 3. How

| 工作项 | Done when |
| --- | --- |
| H1：85 迁路径 | ✓ 2026-11-22；四份模板进 `template/`、两份看板文件进 `board/`，引用同提交改全，`check_dsh.mjs` 新增模板与看板引用检查，旧路径全仓 grep 只剩两处归档里的历史记述。 |
| H2：86 supporter 入口与改称 | ✓ 2026-11-22；新 `commands/supporter.md`，`stakeholder`、`scrum-master` 两入口改称，约定 8、10、12、14、glossary、README 中英同步。 |
| H3：86 的 DSH 部分 | ✓ 2026-11-22；DSH 角色表与 locale 加 supporter，`check_dsh` 覆盖五个角色。 |
| H4：84 署名 | ✓ 2026-11-22；五个文件头、`ATTRIBUTION.md` 3.1／3.2、两份 README 授权表，正文对基线逐字相同。 |
| H5：89 看板收尾态 | ✓ 2026-11-22；`check.py` 三处修复，自测 79 → 99 例，`board-log.md` 与 `ideo-backlog-template.md` 同步。 |
| H6：90 九条 | ✓ 2026-11-22；做八条，③ 不做并说明理由。 |
| H7：收口 | ✓ 2026-11-22；`CHANGELOG.md` 未发布条目，`plugin-validator` 无阻塞问题，通过线冻结。 |

关键选择：模板与看板放插件根而不是各内核里，才拉得到一起；Supporter 只取 SGEP 里「照请求做事」一面；中文叫「秘书」；脚本只放宽不收紧；提交按工作项分开；版本号不动，要给新角色升号另议。

## 4. Increment notes

- **PO 书面授权（2026-11-22）**：「B 线的话，我基本上就交给 AI 自己做了就是交给 Developer 自己做了，我就不参与 Developer 的团队了。」「B 线的话就是 developer 自己做，然后你来审审核他，你们两个一块做就行」。本期各阶段决定——定 Sprint Goal、结束精化、施工放行、Sprint Test 放行、收官与本地合入 main——由 Master 代 PO 做并记日志；仍回 PO 的是改 Product Goal、推送与发布、取消冲刺、推翻 PO 说过的话、PO 点名要看的品味。
- **施工**：Master 放行 How，条件是 B、C 组触发线改成「不低于改前」、H1 的位置等 DSH 探测结果。先做不依赖位置的 H4、H6，再做 H2、H3、H5，H1 最后。
- **触发测试第 1 轮**（改前 `1145382`，改后 `52b42fa`，每臂 27 次有效，技术失败 0）：A 组 0／9 → 9／9，混用 `stakeholder` 0／9；B 组 3／9 → 4／9，混用 `supporter` 0／9；C 组 9／9 → 9／9。B 组两臂都偏低是 `stakeholder` 描述原有的缺口，不是本期引入的退步，没改线、没补跑。第一次起跑的一轮因 PO 追加联络点职责、描述要变而杀掉，没读过结果，封存，题面重冻结。
- **89 追加**：另一期的核验员发现 `board-log.md` 第 11 条允许 `branch <名> @ <提交>`，`check.py` 却恒要 `working copy`；放宽并补 6 例自测（99 → 105），`board-log.md` 第 4 条补一句指向。
- **Master 审过 Increment、放行 Sprint Test（2026-11-22）**，条件是补上述那一句并单独提交，Codex 按这个提交（`a2a9578`）审。
- **Codex 审阅与三处修复（`c0746c8`、`d428188`、`778b767`）**：收尾态判断把任何提到归档的句子当待归档，改成只认明确的等待说法；转达的 PO 意见只是可追溯、不等于验证了身份，正文与约定 14 各补一句；分流措辞写清「等 PO 决定的问题归 Supporter，PO 已给的答复归 Master 记」，`description` 不改（改了要重跑整轮触发测试）。Master 审过 diff，不再请 Codex。
- **PO 全面放权（2026-11-23）**：「这样子把，我不审了，后面自动过吧，你作为master监督审阅他们，然后最后进入review时候，我再来看各自的结果，中间我就不进来了。」「26 27的review这些交给你和codex就可以，我只负责放行什么的」。Review 之前的决定与审阅、Review 本身由 Master 代做；收官等 PO 放行；推送、发布、改 Product Goal、取消冲刺、推翻 PO 说过的话、改 `CLAUDE.md`／`AGENTS.md` 仍回 PO。
- **Review 与退回（2026-11-23）**：Master 派全新的「熟手」视角看本期入口和说明，基本满意，有两处说法打架。Master 按放权定退回 Increment、范围只五处：转达的 PO 意见里范围、条目、go-ahead 这几类的接收方是 Master（`589b3c3`）；转达写明 PO 在哪里说的（会话名、时间）（`c62a93d`）；约定 12 的 permission 写成 stage permission 并说明不是工具权限（`d2d615d`）；约定 14 分流第二级补「没有 Scrum Master 会话时直接问 PO」（`96b7e12`）；快速上手「要看板」补「交给 supporter」（`bcd6d48`）；另有 `CHANGELOG.md` 一句（已装的旧版 0.6.3 在更新前还指旧位置，`a4e32e8`）。不改的四点：约定 14 与 `sprint-log.md` 约定 14 同号（引用都带文件名）、地图里没有 Supporter 节点（交给 26 的长文件）、Supporter 能登记条目（本来就照 PO 或 Master 的话）、缓存里的旧版 0.6.3。`description` 一律没动，Master 审过五处 diff，项 ②③ 不重测。
- **已记的风险**：转达的 PO 意见没有身份验证，靠标明、原话、日期、在哪里说的与三类例外，这是 PO 的决定，只记风险；DSH 的 `engines.dsh` 是 `>=0.2.2-rc.5 <0.3.0`，DSH 0.2.3-alpha.2 自己检查时带 `includePrerelease`，所以接受它，`<0.3.0` 也会放进 0.3.0 的预发布版，不登记新问题。
- **PO 放行收官（2026-11-23）**：PO（经 Supporter 转）：「放行」，2026-11-23，在 Supporter 会话 `IDEO # [supporter]-[main]-[support PO]` 里用选择按钮作答。范围：本地合入 main、打 tag `sprint-27-wrap-up`、关工作树、删分支；不推送。

## 5. Test

- **项 ① 静态检查与两条 grep**：`validate --strict` 通过；`check_dsh` 8／8；`check_docs.py` 195 条链接 0 错、自测 17 例；`board_check selftest` 147 例；`npm pack` 101 个文件；两条 grep 正好等于放行表（旧路径 2 处、旧称法 14 处），基线上同一脚本是 27 处与 23 处；12 个 `description` 与触发测试用的 `52b42fa` 逐字相同。Codex 审后与 Review 退回后各重跑一遍，都过。
- **项 ② 无头加载**：`/ideo-scrum:supporter` 三个会话 3／3，经 Skill 加载的内核依次是 `ideo-kernel`、`scrum-kernel`，没有 `sprint-kernel`、`design-kernel`，技术失败 0；只证明加载顺序，不证明会话里读得到插件目录里的文件（测试自己的限制拒了那几次读取）。
- **项 ③ DSH 实装验收**：IDEO 秘书会话在 `a2a9578` 上做，DSH 0.2.3-alpha.2，三条全过——`/supporter` 被认出并展开、按 ideo → scrum 预载、读得到新位置的模板；原生事件逐项核过。工作区之外的读取靠早先探测覆盖（DSH 0.2.2-rc.5，版本不同、未重测）。
- **项 ④ Codex 独立审阅**（审 `a2a9578`）：验收逐条基本都过，角色边界没找到越界的句子；四条意见——DSH 实装证据审阅时未齐、之后已补；其余三条已修（见第 4 章）。
- **Output Done 七条全过**：内容忠实、署名、可导航、无死链、插件校验、描述长度、DSH 分发。**Outcome**：本期不设必须的信号，两条产品信号（一次会话走通方法论环节；陌生人走完第一个冲刺）记为尚未观察到，不据此声称完整 DoD 已过。

Test 判定（2026-11-23，Master 按 PO 全面放权）：通过。四项都有结果：① 静态检查与 grep 全过；② 无头加载 3/3；③ DSH 实装三条全过；④ Codex 审阅，三处修复由 Master 审过 diff。Output Done 七条全过；Outcome 本期不设必须的信号，记为尚未观察到。当时的目标原文：『秘书管杂活：看板、传话这类杂活交给秘书，PO 不用操心，各角色的叫法不再混；模板、看板各归其位，留下的小毛病补齐，熟手照着就能用。』进 Review；收官等 PO 放行。
