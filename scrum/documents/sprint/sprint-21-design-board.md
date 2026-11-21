# Sprint Backlog — Sprint 21 (design-board)

> Started: 2026-11-19 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `claude/sprint-21-design-board-2a4e5b`（原生 worktree `sprint-21-design-board-2a4e5b`）| Product Owner: SeaPawn | Scrum Master: IDEO # [master]-[main]-[manage sprint] | Developer: Sprint 21 Developer
> Now: 已收官 · 2026-11-21，Sprint Goal 达成，Master 依 PO 授权收官归档（版本维持 6.0.3，未推送、未发布）
> Waiting for PO: None
> 归档：2026-11-19 开工，2026-11-21 收官；版本号维持 `6.0.3`（不推送、不发布）。日志已压缩成关键决定，完整逐条原文见 `git show fe200ee:scrum/sprint-21-design-board/SprintBacklog.md`；H6 原始运行、首轮误判、复测截图、B 卡独立盲读原答与五模式署名官方维基取证见仓外归档 `S:/IDEO-Scrum-Archives/sprint-21-design-board/h6-9558a0a/`。

**CLAUDE.md 未改**：本期未改动 `CLAUDE.md`。Retro 教训按约定 18 与 PBI-69 一条一文件写入 `S:\SeaPawn-Memory\memory\IDEO-Scrum\` 并登记至 `MEMORY.md`，不写每期汇总。

**PO 决定与书面委托（原话）**：
- **Review 前委托（2026-11-20／21）**：「嗯，这样子对于21来说，呃，其他所有的都由你来决定。嗯，关键是到了最后 review 之前，让我来通知我就可以了，其他的在此之前的所有事情你来决定就可以，对于21来讲。」（随后统一扩展至已开跑的 Sprint 21–25，均到各自正式 Review 前向 PO 报告。）
- **Review 验收与署名拍板（2026-11-21）**：「review-21，非常棒得增量和品位。很不错得设计 然后书名也能看到，我认为也不错其实」「①接受，可以开始review了」——接受 2010 *Design Process Mini-Guide* 官方维基空间级 `CC BY-NC-SA 3.0 Unported` 存档证据，另立 **PBI-84** 补齐 `IDEO-modes/` 双源署名。
- **Stakeholder 与合流时机（2026-11-21）**：「21 1.召唤也可以，看你吧 2.我觉得可以现在就合并，你觉得呢？还是打算等？」
- **收官确认（2026-11-21）**：「确认retro，按照你的决定即可」——确认按 Master 呈报方案执行 H6 补勾、Retro 落盘、产品日志刷新与 PBI-84 登记、归档、唯一收官提交、打本地 tag `sprint-21-design-board`、合入本地 `main` 及清理 Sprint 21 工作树与分支。仍归 PO 专属的边界不变：改 Product Goal、推送发布、取消冲刺、推翻 PO 既定决定、PO 点名品味与 `CLAUDE.md` 直接授权。

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 设计方案看得懂：打开设计冲刺卡，一眼看清这次设计的目标、路线和选定的方案；即使没画故事板，也能知道选了什么、方案怎么用。 |
| --- | --- |

**依据：** 承接 [Product Goal](../../ProductBacklog.md#12-product-goal) 的「看板一眼看清进度」。按[六期总表](../sprint-roadmap.md)，PBI-74 只改设计冲刺卡，产品卡和普通 Sprint 卡不改版；PBI-71 独立核验 IDEO 日志归属，让看板约定与检查脚本对同一件事给出同一答案。

### 1.2 Definition of Done

[产品日志 §1.3 的完整 DoD](../../ProductBacklog.md#13-definition-of-done) 全程生效，本期重点核验三组：内容忠实（区分选定方案与可选故事板、未选定不编造）、可导航与无死链（≤2 跳、受影响文档与看板链接可解析）、插件与分发校验（`claude plugin validate --strict` 与 `node --test scripts/check_dsh.mjs`，未改分发方式不加重装专项）。署名、技能描述长度等未列为重点的标准不豁免。

## 2. What

### 2.1 Product Backlog Items

- **PBI-74**：看板：重做设计冲刺卡（作为熟手，我想一眼看见设计目标、地图主线和选定方案，以便不用翻完整日志就能理解这次设计）。
- **PBI-71**：看板：服务产品日志的 IDEO 日志怎么处理（作为用插件做设计的人，我想要看板约定写清「服务产品日志、或已经收尾的 IDEO 日志页面怎么处理」，以便模型和检查脚本对同一件事有同一个答案）。

### 2.2 Refinement

- **PBI-74（设计卡三块，产品卡与普通 Sprint 卡不变）**：
  - 第一块只放本设计 §1.2 目标原文；第二块沿用产品卡简略路线展示 §2.1 地图主线（不改顺序、不发明节点）；第三块独立展示 §3.1 选定方案与用法（`solution` 为 `{title, text}` 对象或 `null`），§3.2 故事板可选折叠附在下方、不以 `story` 推断定案。
  - 三场景隔离验证：A（已选定、有故事板）、B（已选定、无单独故事板，取材归档[反馈闭环设计 §3.1](../design/design-feedback-loop.md#31-方案)并由独立 Sonnet 评阅者只看卡盲读）、C（尚未选定，保留方案区且不将候选写成已选）；另验 R（6 组离线环境 1440/900/375 × 浅/深、产品卡与普通 Sprint 卡零回归）。
- **PBI-71（独立 IDEO 日志归属）**：
  - 按 `For` 实际宿主与 `Now` 收尾态判定：仅指向实际开放宿主的在办 IDEO 日志上板并挂正确宿主卡；仅服务产品日志、明确已收尾（中英文）、无开放宿主或宿主已结束待归档的不上板；待收尾及 `Question` 中提及 `For:` 不误判；不新增日志必填字段。
  - 5 类负例（错挂、漏挂、改写 `Now`、正确宿主先／后出现的跨卡重复挂载）须退出 1 且命中对应错误。
- **冻结测法与通过线**：先于 `9558a0a` 独立提交冻结，再执行验证，过程中未改通过线；Output Done 与 Outcome Done 两条信号分列对账。

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| H1 | PBI-74 · 对齐设计卡的取材约定 | 看板约定中的设计卡数据约定，以及直接受影响的中英文说明 | ✓ 2026-11-20 §1.2 的目标、§2.1 的地图主线、§3.1 的选定方案与可选 §3.2 各有清楚的来源和缺项规则。README 中英不再把设计卡写成展示已完成工作块。 |
| H2 | PBI-74 · 做成三块设计卡 | 更新后的看板模板 | ✓ 2026-11-20 设计卡只在第一块放设计目标，第二块用本设计的简略路线，第三块独立展示方案或明确的未选定状态。产品卡、普通 Sprint 卡及既有导航不改版。 |
| H3 | PBI-74 · 备齐独立样本和判据 | A、B、C 的隔离样本、与约定一致的参考生成和自动检查、读卡对照材料 | ✓ 2026-11-20 A、B 的源日志均明示定案，B 只借用归档 §3.1 的内容，C 明确尚未选定。能用同一数据核其他卡及离线、宽中窄、深浅色表现，读卡任务不透露答案。 |
| H4 | PBI-71 · 对齐 IDEO 日志归属 | 同一归属规则下的看板约定、参考生成与检查判定 | ✓ 2026-11-20 只显示指向实际开放宿主的在办日志；无开放宿主不另建卡，也不判漏挂。仅服务产品日志或已明确收尾的不上板。用既有 `For` 和 `Now`，不增加日志必填字段，不改变合法归属。 |
| H5 | PBI-71 · 拆开归属核验样本 | 三类独立样本及误挂、错挂、漏挂、跨卡重复挂载和改写 `Now` 的检查对照 | ✓ 2026-11-20 每条规则都有独立证据，收尾有中英文代表；不靠一个同时满足两条排除条件的样本。应显示的 IDEO 日志只挂正确宿主才通过；同一条日志同时挂在正确和错误宿主下，无论遍历顺序都必须判错。约定、页面和检查能按 §2.2 逐项对账。 |
| H6 | 本期验收与 DoD 核对 | 两条 PBI 分列的测试证据、DoD 对账和 Master 审阅材料 | ✓ 2026-11-21 两条 PBI（74-A/B/C/R、71-1/2/3/N、79 项自测）与本期 Output Done 全过；基线遗留 `IDEO-modes/` 五模式署名缺口按 PO 2026-11-21 Review 拍板 ① 处置（接受 2010 *Design Process Mini-Guide* 维基存档证据，另立 PBI-84 补齐双源署名），原 Test 实录与仓外证据完整保留。 |

**关键选择**：保留「固定页面 + 一份日志数据」；`solution` 与 `story` 脱钩，不以旧 `story` 反推是否已选；沿用产品卡 `.metro` 路线样式但只改设计卡；`check.py` 与参考生成共用归属规则，记录全部挂载且不让后出现的正确宿主掩盖错挂。

**Go-ahead**：2026-11-19，PO 放行 H1–H5 施工；2026-11-20，Master 依 PO 书面委托放行 Increment → Test（H6）。

## 4. Increment notes

- **初交审（`7453a50`）**：更新[看板约定](../../../plugins/ideo-scrum/skills/scrum-kernel/conventions/board-log.md)、[看板模板](../../../plugins/ideo-scrum/skills/scrum-kernel/conventions/scrum-board-template.html)、中英文 README、[检查脚本](../../../scripts/board_check/check.py)、[对照准备脚本](../../../scripts/board_check/prepare_review.py)及 `scripts/board_check/fixtures/` 隔离夹具与 `review-expectations.json`。
- **Master 静态复审修订（`f030513`）**：PBI-74 无静态阻塞；PBI-71 修正三处——明确收尾的完整开头语义判定、宿主已结束但未归档时不挂在办 IDEO、`Question` 内含 `For:` 不抢实际头部字段（按引用头竖线分隔匹配）。复审通过后进 Test。

## 5. Test

- **PBI-74（`7ae87ff`，旧模板基线 `00c224b`）**：
  - **74-A / 74-B / 74-C / 74-R 全过**：6 组离线环境（1440/900/375 × 浅/深）共 42 卡次通过，产品卡与普通 Sprint 卡 12 组对照零回归，控制台错误与外部 HTTP 请求均 0。
  - **首轮驱动判错与复测**：首轮未核实 `navigator.onLine`、未阻断 HTTP(S)，且误用隐藏段落空 `innerText` 判折叠；保留原始首轮记录，仅修仓外驱动（导航前禁 HTTP(S)、断言离线、核 `open` 与展开前后可见文本）并按原口径全量复测通过。
  - **B 卡独立盲读（Sonnet 子代理）**：只看无故事板 B 卡渲染截图与三问，准确答出选定方案（「记一下就够」，全局说明指路、按产品进全局记忆）、使用方式（发现问题说一句「记一下」、不报位置）与后续动作（会话里立即生效、更新时取回由 PO 决定），与冻结语义逐项对齐。
- **PBI-71（`7ae87ff`）**：13 份独立夹具离线实开全过（6 例排除场景省略且误挂各被拒、待收尾与 `Question` 含 `For:` 正确挂载）；5 类负例全退出 1 且命中对应错误；`check.py --selftest` 79 项全过。
- **DoD 对账**：
  - **本期 Output Done 全过**：内容忠实、可导航（≤2 跳）、无死链、`claude plugin validate --strict plugins/ideo-scrum` 通过、技能 `description` ≤1024 且未改、`node --test scripts/check_dsh.mjs` 6/6 通过。另记基线既有 3 处跨内核裸文件名（非断链，本期未顺手改）。
  - **Outcome Done 分列**：两条产品级信号（一次会话走通、陌生人 PBI-63，参考 [Sprint 20 §5](sprint-20-presentable.md#5-test)）本期未重跑全流程，诚实记未重测，不拿 B 卡局部盲读代替。
  - **基线遗留五模式署名取证（`ec37180` → `050b1cd` → `fe200ee`）**：核实 `IDEO-modes/*.md` 含两路底本——`89eb3dd` 主体逐词对应 Stanford d.school 2010 *Design Process Mini-Guide*（6 页 `ModeGuideBOOTCAMP2010L.pdf`，与 ALNAP 副本逐字节一致，归属官方 `designresources` 维基页 `wiki/36873`，同维基首页 2011–2023 存档明载空间级 `CC BY-NC-SA 3.0 Unported`），`0d2629f` 的 38 处补料对应 2018 *Design Thinking Bootleg*（`CC BY-NC-SA 4.0`）。因本期未改动 `ATTRIBUTION.md` 或 `IDEO-modes/*.md`，Test 停点维持「本期增量全过、基线署名缺口未闭环、H6 暂不勾」，交 PO 在 Review 拍板。
- **§5 补记（2026-11-21 · PO Review 拍板 ① 后 H6 补勾）**：保留上述原 Test 实录与仓外证据不覆写。PO 在 Review 明确拍板 ①（接受 2010 *Design Process Mini-Guide* 官方维基空间级存档证据，另立 **PBI-84** 补齐双源署名），H6 其余完成条件均已证实满足；据此在本轮收官提交中为 H6 补打 `✓ 2026-11-21`，口径与 ① 处置及 PBI-84 登记一致。

---

### Review 与收官记录（2026-11-21）

- **目标核对快照（§1.1 原文）**：「设计方案看得懂：打开设计冲刺卡，一眼看清这次设计的目标、路线和选定的方案；即使没画故事板，也能知道选了什么、方案怎么用。」
- **PO 验收**：认可增量与品味，拍板 ① 处置基线五模式署名缺口（另立 PBI-84），批准收官并即刻合入本地 `main`（不推送、不发布、版本维持 `6.0.3`）。
- **「熟手」Stakeholder Review（独立 Sonnet 子代理）**：无阻塞满意度落差；3 条非阻塞建议并入[产品日志](../../ProductBacklog.md) PBI-79「21+23 合流回验」备注（① `check.py` 结束态兼容无「已」的 `收官 · …` 写法、`host_concluded` 剥离阶段前缀及避免阶段前缀跳过无主语规则；② `board-log.md` 第 12 条补明 `solution: null` 时亦省略 `story`；③ `ideo-backlog-template.md` 的 `For` 占位说明补提 `DesignBacklog.md`；连同 Sprint 23 结束待归档态的宿主发现与 IDEO 归属一并回验）。
- **产品日志与 `scrum/` 保鲜**：PBI-74、PBI-71 移入 §3.2；新增 **PBI-84**（待选，S）；复查 `scrum/` 与 `scrum/documents/` 无过时文件需删；`scripts/board_check/fixtures/review-expectations.json` 旧日志路径同步更新至本归档路径。
- **Retro（无独立章，依约定 18 & PBI-69）**：写入两条可复用教训至 `S:\SeaPawn-Memory\memory\IDEO-Scrum\` 并登记于 `MEMORY.md`——`third-party-license-by-exact-edition.md` 与 `html-board-verify-offline-and-details.md`；`CLAUDE.md` 未改动。等待点补充记录：前期放权前逐阶段门等 PO 点头（放权至 Review 前后已消除），以及 21 Developer 会话中途关闭离线一次。
