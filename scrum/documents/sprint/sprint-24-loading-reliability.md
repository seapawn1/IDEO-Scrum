# Sprint Backlog — Sprint 24 (loading-reliability)

> Started: 2026-11-19 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `claude/sprint-24-loading-reliability-012ded` | Product Owner: SeaPawn | Scrum Master: IDEO-Scrum Master | Developer: Sprint 24 Developer
> Now: 已收官 · 2026-11-21，PO 确认 Review 通过；该期未改版号、未推送、未发布。
> Waiting for PO: None
> 归档：在办日志全文见 `b00367d` 树中的 `SprintBacklog.md`，含冻结判据、原始账目与独立复核。仓外原始记录在 `S:/IDEO-Scrum-Archives/sprint-24-loading-reliability/`。

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 先读原文再动笔：叫出角色就能调齐该用的内核；定目标、写设计问题或精化条目前，AI 先读并用上对应的原文、约定和模板注释，不用 PO 反复提醒；承诺照常提示，发消息时不再为检查未变的承诺等上几秒。 |
| --- | --- |

### 1.2 Definition of Done

[完整产品 DoD](../../ProductBacklog.md#13-definition-of-done) 继续生效。本期重点核验原文与署名、导航、内部链接、严格校验和 DSH 既有回归，四项功能的行为和性能单独判定。

## 2. What

### 2.1 Product Backlog Items

- **PBI-80**：起草产物前真正读到阶段原文。
- **PBI-81**：角色入口按顺序调齐内核。
- **PBI-82**：内核加载时带入需要的方法原文。
- **PBI-83**：承诺 hook 的响应时间。

### 2.2 Refinement

四类稿件分开判「首稿前读全」和「用对」，纠偏稿不替换首稿。角色入口核对实际成功的 `Skill` 调用顺序；加载证据核正文逐字一致。本机重放的两个夹具各自 P50 至少降 50%，P95 不高于基线且不超过 1 秒。宿主另以原生 hook 事件与 debug 交付记录判语义。完整冻结标准与题面见历史 §2.2；[试次索引](sprint-24-loading-reliability-validation/trial-index.md)、[判卷表](sprint-24-loading-reliability-validation/scorecard.md)和夹具一同保留。

## 3. How

| 工作项 | Done when |
| --- | --- |
| H1–H6：夹具、四角色入口、必带原文、起草入口与本机基线 | ✓ 2026-11-20（六项）；原完成条件见历史 §3。 |
| H7：承诺 hook 优化 | ✓ 2026-11-21；`a482a52` 的脚本内部常态开销降为单次 `awk`，保持现有语义。 |
| H8：四题首稿与 G1 纠偏 | ✓ 2026-11-21；各 3 对，分判读全和用对，纠偏先回查原文。 |
| H9：实际角色入口与首次原文加载 | ✓ 2026-11-21；四角色各 3/3，LOAD 逐字 3/3。 |
| H10：承诺语义与耗时 | ✓ 2026-11-21；L1／L2 本机性能与 HOST-01–03 宿主证据分列。 |
| H11：逐项对账与交审 | ✓ 2026-11-21；静态校验通过，validator 无必改；H1–H11 完成 11/11。 |

关键选择：用入口指导先读再写，不全量预载；只内联必要的 Sprint Backlog 原文。hook 仍读日志正文，不以大小或 `mtime` 判未变，保持注册、原文、触发时机、开关与静默退出。

## 4. Increment notes

- `c5c6577`：四角色入口按序实调；三个阶段起草入口明示必读材料；`sprint-kernel` 载入 SGEP 原文并检查逐字一致。
- `ca64cd4` → `a482a52`：复现旧慢并定位到重复的外部短进程；通过边界审阅后以单次 POSIX `awk` 合并解析。`hooks.json` 的触发配置与超时没改。
- `b3a7af5`、`b00367d`：记入 Master Test 终审及宿主 debug 证据；H7–H11 完成标记落在 `Done when`。
- **PO 收官授权（2026-11-21，本会话直接原话）**：「可以，后面你自主决定，收口所有分支，我都review认为通过」。委托本批 Review／Retro、归档、产品日志、本地 tag、合入及清理。改 Product Goal／Sprint Goal、取消 Sprint、推翻 PO 定案、PO 点名品味、修改 `CLAUDE.md` 及对外推送发布仍归 PO。

## 5. Test

- **PBI-80**：候选四题首稿前读全各 3/3（总 12/12，对照基线 0/12），草稿用对；G1 纠偏先回查原文。
- **PBI-81／82**：候选四角色按 4／3／3／2 调用，各 3/3；复用只新增 `sprint-kernel`。首次直接加载含所需原文 3/3（2,499 字符去尾换行，逐字一致），基线 0/3。
- **PBI-83**：本机 L1／L2 P50 为 215.56／206.00 ms，降 90.7%／91.1%；P95 为 239.17／242.59 ms。脚本语义 50/50（WSL 两实现各 48/48，265 步等价）；宿主的启动、未变静默、同字节长同 `mtime` 变更、恢复与关闭通过。`clear`／`compact`／`fork` 只记脚本证据。
- **Output DoD 对账**：严格校验、DSH 7/7、文档 107 链零错与 selftest 17/17；四内核描述合格、≤2 跳，新增 SGEP 原文及许可有据。五模式底本既有署名缺口仍见产品日志，不因本期检查改判。全流程 Outcome Done 本期未重测。
- **宿主账目**：60 次启动，含冒烟与 4 次批准的定向补测；CLI 累计估算 $19.630688 / US$30 上限，不是网关账单。US$15 旧停点曾因漏扣冒烟跨线后停报；4 次超时原流和 3 次沙箱外路径拒绝留档。宿主 `--debug` 原始证据保留到仓外 `h8-h11/raw/`。

**PO 决定收官（2026-11-21）**：已核对 Master Test 终审与本期增量，PO 认定 Review 通过。承诺原文：「先读原文再动笔：叫出角色就能调齐该用的内核；定目标、写设计问题或精化条目前，AI 先读并用上对应的原文、约定和模板注释，不用 PO 反复提醒；承诺照常提示，发消息时不再为检查未变的承诺等上几秒。」
