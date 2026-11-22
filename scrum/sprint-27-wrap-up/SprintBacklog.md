# Sprint Backlog — Sprint 27 (wrap-up)

> Started: 2026-11-22 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `worktree-sprint-27-wrap-up` | Product Owner: SeaPawn | Scrum Master: IDEO # [master]-[main]-[manage sprint] | Developer: Sprint 27 Developer
> Now: Increment · 2026-11-22：H1–H7 施工与自查都做完（第 3 章各行已标 ✓，H7 一行等 Master 审），等 Master 审 Increment、放行 Sprint Test；2.2 的测试方法与通过线冻结于 `d72b0a6`；DSH 实装验收待 IDEO 秘书会话。PO 最近一次决定：Supporter 加「联络点」、转达的 PO 意见视同 PO 的、三级分流。
> Waiting for PO: None
> How to write this log: `sprint-log.md` in the sprint-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled later; add none. Work remarks go in chapter 4, Increment notes; an optional explanation of the commitment may follow its table (`overview.md` in the scrum-kernel skill folder, conventions 16 and 17).

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 秘书管杂活：看板、传话这类杂活交给秘书，PO 不用操心，各角色的叫法不再混；模板、看板各归其位，留下的小毛病补齐，熟手照着就能用。 |
| --- | --- |

依据：PO「27的话应该是建立秘书角色。对，我觉得可以稍微改一改。」秘书这一角色的英文名定为 `supporter`（见 2.2 Q1）。

### 1.2 Definition of Done

[完整产品 DoD](../ProductBacklog.md#13-definition-of-done) 全部生效。本期重点核验（Master 选，吸收 Developer 2026-11-22 的补充，待 PO 审）：

- **署名**：84 补齐双源 Source／License；摘录正文逐字不动，diff 只动 Source／License 行、`ATTRIBUTION.md` 与 README 中英授权表里 d.school 的一行（三处要彼此一致，Codex 详审 2026-11-22 指出原写法太窄）。
- **可导航、无死链**：85 迁路径后全仓 grep 旧路径到零；90 的 ⑥ 新 docs 进导航。
- **插件校验、描述长度**：`claude plugin validate --strict` 通过；86 新入口与改动的描述（`scrum-master`、`stakeholder`）≤1024，重跑触发测试，不比改前差。
- **DSH 分发**：`node --test scripts/check_dsh.mjs` 通过；85 改 DSH 加包范围，86 新角色进 DSH 的角色表；另验实际安装与角色入口。
- **自检**：`scripts/check_docs.py`、`board_check selftest`（85、89）。

**开张与 Why 放行**：PO 本人 2026-11-22（Master 会话，经 Master 转述）：「我觉得可以先不着急，我们可以先把每个的目标定出来」。范围：定 Sprint Goal 与本期 DoD 重点。

**Sprint Goal 决定**：Master 按书面授权定稿，2026-11-22。PO 审过草案：「剩下的我觉得问题不大了」「差不多了就可以进入，让27就是同步给冲刺27的 developer，然后进入 How 阶段」。当时的目标原文：「秘书管杂活：看板、传话这类杂活交给秘书，PO 不用操心，各角色的叫法不再混；模板、看板各归其位，留下的小毛病补齐，熟手照着就能用。」

**What**：PO 2026-11-22：「你把 S7也先写出来吧。然后这两个我一起审掉。」范围：Master 起草第 1、2 章，与 Sprint 26 一起由 PO 审。目标未定就写精化，跟约定 24 的先后不同，是 PO 要两期同审；审时 PO 先定目标，再看精化。How 未放行。

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-84 | 署名：补齐 IDEO 五模式双源署名 | 作为熟手，我想要 IDEO 五模式摘录的来源与许可标注同时对上 2010 *Design Process Mini-Guide* 与 2018 *Bootleg*，以便插件的第三方署名与 `ATTRIBUTION.md` 逐项一致 | 插件：`ideo-kernel`（`IDEO-modes/`）与 `ATTRIBUTION.md` | S |
| PBI-85 | 结构：模板与看板按用途收拢 | 作为熟手，我想在插件里按用途一眼找到模板和看板，以便引用和维护都井然有序 | 插件：目录结构 | M |
| PBI-86 | 角色：PO 秘书与「秘书」说辞统一 | 作为 PO，我想有一个全辅助的秘书角色（更新看板、讲解机制等），并把 SM 与 Stakeholder 入口里「秘书」的说法换成统一的新称法，以便角色边界与称呼不混淆 | Map ②、③；插件：commands／agents／docs | S～M |
| PBI-89 | 看板：收尾态识别与三条说明 | 作为熟手，我想让看板认得收尾待归档的写法，说明与模板占位前后一致，以便收尾中的设计和 IDEO 日志挂在对的地方 | 插件：`board/board-log.md`、`template/ideo-backlog-template.md`；`scripts/board_check/` | 待估 |
| PBI-90 | 入口：Sprint 22 Review 的九条意见 | 作为熟手，我想让项目 Agent 与参谋入口的说明补齐写法、提示和后续路径，措辞前后一致，以便照着说明就能用 | 插件：`claude-skills/project-stakeholder`、`claude-skills/second-opinion`、`agents/advisor.md`；docs | 待估 |

对照目标：86 →「杂活交给秘书」「叫法不再混」；85 →「各归其位」；89、90、84 →「小毛病补齐」。五条都服务目标，没有缺的。87、91 PO 定本轮不收。规模「待估」的由 Developer 在 How 前估。

### 2.2 Refinement

> 草案 · Master 2026-11-22 起草，待 PO 审；Developer 复述（第 6 步）在 PO 审后。授权内的点由 Master 定，PO 保留的点标「PO（保留）」。

**PBI-86 · 秘书角色**

- 视角（照抄）：作为 PO，我想有一个全辅助的秘书角色（更新看板、讲解机制等），并把 SM 与 Stakeholder 入口里「秘书」的说法换成统一的新称法，以便角色边界与称呼不混淆
- HMW：我们怎样让杂活有人接，PO 一句话就交得出去？我们怎样让每个角色的叫法一听就分得清？

| # | 要点 | 谁定 |
| --- | --- | --- |
| Q1 | 秘书叫什么，入口（命令名）叫什么 | PO（保留）✓ |
| Q2 | 定位与边界：做什么（PO 原话：更新看板、传达事情、讲解机制，「各种杂活都归他」）；不做什么——现「PO assistant」的边界是不排序、不决定、不审阅、不改插件文件，Master 建议沿用 | PO（保留）✓ |
| Q3 | 删掉 Stakeholder 的「PO assistant」身份后，`scrum-master` 描述等处原来的说法换成什么 | PO（保留）✓ |
| Q4 | 便宜模型：PO「它一般用非常便宜的模型」；入口里怎么落（写死还是建议） | Developer 提，Master 定 |
| Q5 | 加载哪些内核（参照 Stakeholder 的 ideo → scrum；看板约定在 scrum-kernel） | Developer 提，Master 定 |
| Q6 | DSH：`dsh/index.js` 的角色表与 locale 加入新角色 | Developer |
| Q7 | 本项目产品日志 §2.1 的「PO 助手（常驻会话）」卡与地图说法 | Master，收官时改 |

**定案（2026-11-22）**

- Q1：`supporter`，全小写，入口 `/ideo-scrum:supporter`。PO 先定 `assistant`（「Assistant 的也可以……我觉得这个名字好。呃，看你同不同意吧」），随后改为：「非常同意，要不然，我们改为supporter把？你觉得呢？似乎sgep就提到过这五种呢？PO master developer stakeholder supporter？ designer是另外理论」。Master 同意：SGEP 写 Supporter「is a specific Stakeholder type」，「doing what is requested」「should participate when and where needed or as requested」，正对这个角色。SGEP 的 Supporter 还是 change agent、guiding coalition，本插件只取「照请求做事」这一面，按作者约定标明。中文叫法由 Developer 提（PO 口头叫「秘书」）。
- Q2：沿用现边界——不排序、不决定、不审阅、不改插件文件，只传 PO 或 Master 已定的事。PO：「不做什么，我觉得你我觉得可以沿用，你看看有没有什么要修改的，然后也可以修改一下」。Master：沿用，不改。定位按 SGEP 的 Supporter（a Stakeholder type）立，见 Q1；PO：「它其实本质上也是也算是 stakeholder 的一种」。（PO 2026-11-22 追加）加一项职责——PO 的联络点：从各会话和各日志头部的 `> Waiting for PO:` 收齐等 PO 定的问题，带上下文一次交给 PO，再把 PO 的回答原话转回去，由各日志记录；不替 PO 回答、不决定、不删减问题，涉及范围与放行的回答经 Master 记录。PO：「就是你其实可以加一个 support 的职责。Supporter 的职责可以是一个和 PO 直接沟通。就是收集问题，然后呃 PO 沟通嘛，这这本来也是秘书的职责嘛，对不对？其实我觉得可以这样子稍微地倾斜一下」。（PO 2026-11-22 再追加）Supporter 转达的 PO 意见算正式的 PO 意见，其他角色以它为准，不必 PO 再亲口说；依据：Scrum Guide 2020「The Product Owner may do the above work or may delegate the responsibility to others. Regardless, the Product Owner remains accountable.」。Master 定的条件：转达时标明是 PO 的意见，附 PO 原话与日期，自己的解释不算；接收方记成「PO（经 Supporter 转）：原话」。不在此列的：工具权限与设置、`CLAUDE.md`／`AGENTS.md` 的改动（宿主规则与项目规矩都要 PO 直接点头），以及推送、发布这类对外动作，仍要 PO 亲口确认。PO：「他可以代表我的意志，因为我们的 scrum 其实本质上也说过嘛，就是说 po 可以把他的权利委托给秘书，但是最终的责任是在 po 上面。所以说秘书也就是 supporter 他所表达的内容，其实是可以作为啊正式的 po 意见的，然后所有的呃这个这个就是说其他的角色都可以以这个意见为准，就是不需要 po 再亲自去告诉他了，这样子。我觉得这个权限要给他。」（PO 2026-11-22 三追加）分流：各角色遇到要 PO 的事，交给 Supporter 汇总后提示 PO，不再经 Master 转；自己能定的自己定，归 Master 的问 Master。Master 定的写法：照 `overview.md` 约定 10「unless the Product Owner has sent that kind of question elsewhere」，写明 PO 把只有 PO 能定、能做的事（含工具权限、设置、`CLAUDE.md`／`AGENTS.md`、推送发布）交给 Supporter 汇总；Supporter 把不归 PO 的问题退回并说明归谁；没有 Supporter 会话时照旧直接问 PO。PO：「我必须要靠一个 supporter 也就是秘书的角色来给我汇总」「他在遇到问题的时候。他应该去同步给秘书，让秘书向我提示」「以前的时候其实是通过你了……但是我觉得其实 supporter 这个角色会更好一点」「我又害怕这样做了之后就是角色重复了……很多事情他可以自己决定，然后或者说让你决定」「我不知道还要不要专门的去嗯声明这个事情」。（PO 2026-11-22 认可 Master 复述的 Supporter 与 Master 分界）「你定的这个 support 和这个Master 的职责非常好，职责分界非常好，可以说是非常 good。……我们现在就可以以这个标准来尝试。」
- Q3：PO：「我觉得应该叫就是 master 吧，就是说有权力的 master，我觉得你想想呢」。Master 的读法：`scrum-master` 入口去掉「秘书」味，看板、汇总、传话这类杂活交给 supporter；SM 写成有权的 Master：守流程、审、在书面授权内代 PO 定。Scrum Guide 原文不动；排序、目标等产品决定仍归 PO。
- Q4：便宜模型写不写进入口由 Developer 定；PO 要整个角色「比较漂亮一点，比较优雅一点」，「不写也行」。
- Q5：跟 Stakeholder 一样，ideo → scrum（PO：「就跟 stakeholder 一样就行」）。
- Q6：DSH 实装与角色入口的测试可交现有的 IDEO 秘书会话（`IDEO # [secretary]-[main]-[support PO]`）（PO：「DSA 是可以让他去测试」，DSA 即 DSH），由 Master 转交。

- 已知改动处：`commands/stakeholder.md`（description、第 15 与 34 行）、`commands/scrum-master.md` 的 description、`overview.md` 约定 8 的表与约定 14、`docs/glossary.md`、`claude-skills/project-stakeholder/SKILL.md`、`scripts/check_docs.py` 的术语表；其余由 Developer 全仓再查。
- 验收：新入口能叫出、按定的顺序加载内核，Claude Code 与 DSH 各验一次；旧的「PO assistant／PO 助手」按下面「通过线」的 grep 范围与例外为零，新称法前后一致；Review 召唤权与建造者边界不变；改过的描述 ≤1024，触发测试不比改前差。

**PBI-85 · 模板与看板**

- 视角（照抄）：作为熟手，我想在插件里按用途一眼找到模板和看板，以便引用和维护都井然有序
- HMW：我们怎样让找模板、找看板的人第一眼就落对地方？
- 要点：模板放每个内核各自的 `template/`，还是插件一处共用——Developer 提，Master 定，须顾到技能间按名字调用、SKILL.md 的相对引用和 `package.json` 的加包范围；看板相关（`board-log.md`、`scrum-board-template.html`）进 `board/`，其中的规矩由 26 期再转进 Memory；同一提交内全仓 grep 旧路径到零（项目规矩）；本条排第一项，先合 main（总表「续」）。
- **定案（Master 2026-11-22，按授权）**：四份日志模板放插件根的 `template/`，看板相关（`board-log.md`、`scrum-board-template.html`）放插件根的 `board/`。依据：PO 原话「模板专门拉一起放在 template 里面」；DSH 对照测——默认受限预设（workspace-write，approval ask）下，`skills/` 里的 `overview.md` 与 `skills/` 外的 `commands/developer.md` 都读到、`isError:false`、没触发审批（秘书会话两份 DSH 会话记录，`session-0fa490f5…`、`session-a3e7f38f…`）。三点：技能引用写 `../../template/<文件>`、`../../board/<文件>`；`package.json` 的 `files` 加这两个目录；DSH 读得到。
- 验收：模板都在定好的位置，看板相关都在 `board/`；旧路径按下面「通过线」的 grep 范围与例外为零；`validate --strict`、`check_dsh`、`check_docs.py`、`board_check selftest` 通过；DSH 实装后角色入口读得到模板。

**PBI-89 · 看板收尾态**

- 视角（照抄）：作为熟手，我想让看板认得收尾待归档的写法，说明与模板占位前后一致，以便收尾中的设计和 IDEO 日志挂在对的地方
- HMW：我们怎样让收尾中的日志在看板上挂在它该在的地方？
- 要点：先修 `Test: Concluded — awaiting archive` 识别不了的缺口；三条建议（`check.py` 兼容无「已」的 `收官 · …`、`host_concluded` 剥离阶段前缀、阶段前缀不跳过无主语规则；`board-log.md` 第 12 条补明 `solution: null` 时亦省略 `story`；`ideo-backlog-template.md` 的 `For` 占位补提 `DesignBacklog.md`）逐条做，或写明不做的理由——Developer 提，Master 定；检查脚本不比约定严。
- 验收：每处修改各有正例与负例夹具，`board_check selftest` 全过；Sprint 23 的三态合成日志（开放、`Concluded — awaiting archive`、迁出活动路径）重跑通过；改了条文的，条文与脚本一致。

**PBI-90 · 九条意见**

- 视角（照抄）：作为熟手，我想让项目 Agent 与参谋入口的说明补齐写法、提示和后续路径，措辞前后一致，以便照着说明就能用
- HMW：我们怎样让第一次登记 Agent、请参谋的人照着说明就做成？
- 要点：九条逐条定做或不做，写理由——Developer 提，Master 定；③ 改召唤示例须按 Review 流程批准并验证（来源条件）；⑥ README 已链到 `docs/project-agents.md`，先查快速上手是否还缺。
- 分量：PO「我很担心你这个89和90很重啊，尤其这个90」。90 是九条小意见，不是九十条；不值得做的写理由不做，89 和 90 都别做重，规模由 Developer 估。
- 验收：九条每条有结论与理由；做了的各有证据；改过的描述 ≤1024，触发测试不比改前差。

**PBI-84 · 署名**

- 视角（照抄）：作为熟手，我想要 IDEO 五模式摘录的来源与许可标注同时对上 2010 *Design Process Mini-Guide* 与 2018 *Bootleg*，以便插件的第三方署名与 `ATTRIBUTION.md` 逐项一致
- HMW：我们怎样让每段摘录都对得上它真正的版本和许可？
- 要点：两源已定（PO 2026-11-21 Review 拍板 ①）——2010 *Design Process Mini-Guide* 为主体（`CC BY-NC-SA 3.0 Unported`），2018 *Bootleg* 补料 38 处（`CC BY-NC-SA 4.0`）；五个 `IDEO-modes/*.md` 文件头与 `ATTRIBUTION.md` 第 3 节怎么写——Developer 提，Master 定；摘录正文不动。
- 验收：五个文件头与 `ATTRIBUTION.md` 第 3 节逐项对上两源；diff 只动 Source／License 行、`ATTRIBUTION.md` 与 README 中英授权表里 d.school 的一行（Codex 详审 2026-11-22：原写法「只动 Source／License 与 ATTRIBUTION」太窄，README 的授权表本来也要与 ATTRIBUTION 一致）；中英两张表与 `ATTRIBUTION.md` 逐项核对一致；许可有可达链接或存档出处（仓外取证路径见 PBI-84 备注）。

**测试**（第 13 条；How 定稿前补齐通过线，Test 前提交，提交后不改）

- 要新证据：`validate --strict`、`check_dsh`（含新角色）、`check_docs.py`、`board_check selftest`、旧路径与旧称法 grep、摘录 diff、描述长度、触发测试（与改前同日对照）、新角色入口加载（Claude Code、DSH）。
- 沿用旧证据：无，本期动到的检查都重跑。
- Outcome：不设本期必须的信号；Review 时 Master 召「熟手」看入口与说明，意见记为信号。产品日志 §1.3 的两条 Outcome Done 信号（一次会话走通方法论环节；懂 Scrum 的陌生人走完第一个冲刺）在第 5 章各记一句：观察到、没观察到，或不适用及原因；没有证据的记「尚未观察到」，有相反证据的记「未达到」并写影响；不据此声称完整 DoD 已过（约定 16）。

**通过线**（Developer 拟，2026-11-22，Master 审；Test 前提交，提交后不改。正式跑之前先冒烟一次，冒烟不计数）：

- **静态**：`claude plugin validate --strict plugins/ideo-scrum`、`node --test scripts/check_dsh.mjs`（覆盖五个角色，含 H1 新增的模板与看板引用检查）、`python -X utf8 -I scripts/check_docs.py`（含 `--selftest`）、`python -X utf8 -I scripts/board_check/check.py selftest` 全过；`npm pack --dry-run --json --ignore-scripts` 的清单含新的 `template/`、`board/`（若 Master 定退回各内核自己的 `template/`，则含各内核的 `template/`）与 `commands/supporter.md`；新命令与改过 frontmatter 的入口派 `plugin-dev:plugin-validator`（Haiku）无阻塞问题。
- **grep 为零**（Codex 详审 2026-11-22 后改：不再把整个 `scrum/` 排除在外；项目规矩是迁移类改动同一提交内全仓 grep 旧值到零）：
  - **查什么**：① 旧路径——模板与看板的旧位置（各内核 `conventions/` 目录下的四份 `*-backlog-template.md`、`scrum-board-template.html`、`board-log.md`，按「`conventions/` 加文件名」和「`skills/scrum-kernel/conventions/` 加文件名」两种写法搜）；② 旧称法——`PO assistant`、`PO 助手`、`standing assistant`、`standing helper`、`standing Stakeholder`、「常驻的助手」「助手会话」。
  - **在哪查**：整个仓库的跟踪文件（`git grep`）：`plugins/`、`dsh/`、`docs/`、`README*`、`scripts/`、`package.json`、`.gitignore`、根目录的规则与说明文件、`scrum/` 里的产品日志、总表与本日志，以及 `scrum/documents/` 里的全部文件；只有下面逐处列出的命中放行。产品日志里的旧路径（PBI-89 的 Place 一栏）、总表里的看板约定链接、本日志里的旧路径，以及归档 Sprint 21 日志里两条指向已搬走文件的链接，都在 H1 的同一提交内改到新位置（归档那处只动了两个链接地址，行里的文字没动：改前全仓没有一条死链，不改就会多出两条）。
  - **搜索命令**（Test 里原样再跑）：
    - 旧路径：`git grep -n -E "conventions/(board-log|scrum-board-template|(product|sprint|design|ideo)-backlog-template)"`
    - 旧称法：`git grep -n -i -E "PO assistant|PO 助手|standing assistant|standing helper|\bstanding Stakeholder|常驻的助手|助手会话"`（`\bstanding Stakeholder` 带词界，免得把 SGEP 原文「understanding Stakeholders」算成命中）
  - **放行的命中，逐处列出**（冻结时的文件与行号；Test 里再跑上面两条命令，命中必须正好是这些：多一处或少一处都不过。CHANGELOG 与 `scrum/documents/design/` 里两条命令都没有命中，所以不设例外）：
    - 旧路径，共 2 处，都是归档里对当时路径的历史记述：`scrum/documents/sprint/sprint-09-design-template.md:60`（代码样式写的当时设计日志模板的路径）；`scrum/documents/conventions-review-log.md:24`（Sprint 11 审阅记录表里当时被审文件的路径，其中别的文件路径早已因 Sprint 12 变过，从未回改）。
    - 旧称法，共 14 处：
      - `scrum/documents/sprint/sprint-18-rules-first.md:35`、`scrum/documents/sprint/sprint-22-project-agents.md:81`：已归档冲刺日志里对当时做法的记述，归档不回改；
      - `scrum/ProductBacklog.md:57`（§2.1 角色卡表头）与 `:77`（§2.2 地图节点）：Q7，Master 收官时改；
      - `scrum/ProductBacklog.md:117`：PBI-86 条目，PO 定的条目原文，要删的正是这个旧说法，收官时整条移进 3.2；
      - `scrum/ProductBacklog.md:145`：3.2 完成表里 Sprint 18 一行，历史；
      - `scrum/documents/sprint-roadmap.md:66`：总表「续」一节在 Sprint 27 开张前写的范围说明，那个说法正是 86 要改的东西；
      - `CHANGELOG.md:11`：未发布条目里写「它原来兼作……」的改名说明，发布说明要让从旧版升上来的人认得出改的是哪个旧叫法，必须点出旧名；
      - `scrum/sprint-27-wrap-up/SprintBacklog.md` 的 6 处（行 60、61、65、77、119、123）：Q2、Q3、Q7 三行是 Master 写的问题原文，86 验收一条是本期的验收标准本身，「查什么」与「搜索命令」两行是词表本身——都是在点名那个旧说法，不是在用它。
    - 本日志第 3、4、5 章与别处的叙述我已改写成不含这些词的写法；Test 里若有别的命中就是新增，要么改写，要么回来在这里登记并说明理由。
- **完整 DoD 逐条**（约定 4、16：本期重点之外的标准照样生效，逐条给证据；不声称完整 DoD 已过）：
  - **内容忠实**：H2——`supporter.md` 引的三处 SGEP 短语与 `overview.md` 约定 14 引的 Scrum Guide 2020 原句，各对 `assets/` 里的原文逐字核（脚本）；`assets/`、`references/`、`events/` 里的 Scrum Guide 与 SGEP 摘录对基线 `git diff` 为空；作者的取舍在 `supporter.md` 里用斜体标明。H3——只动注册、locale 与维护文档，没有方法论正文的改动（`git diff` 核）。H5——看板与 IDEO 约定的改动是作者约定，条文与 `check.py` 一致（自测）。H6——docs 与入口说明，没有原书摘录的改动。
  - **署名**：H4 五个文件头与 `ATTRIBUTION.md` 第 3 节、README 中英授权表三处一致；`supporter.md` 引 SGEP 在 `ATTRIBUTION.md` 第 2 节已登记。
  - **可导航**：`scripts/check_dsh.mjs` 的新检查——六个文件各被某个内核的 `SKILL.md` 用 `../../template/…`、`../../board/…` 写到（1 跳）；写到的路径都存在、都在打包清单里；技能与约定文件里不再有旧位置的写法（另做过一次反向对照：故意写回一处旧写法，这条检查果然失败，再还原）。
  - **无死链**：`check_docs.py`（README 与 docs）；`validation/h1/dead_links.py` 对全部跟踪的 markdown 解析相对链接（`--base 1145382` 查「基线能通、现在不通」的），基线为 0 处死链，改后仍须为 0（H1 原本会让归档 Sprint 21 日志里两条看板文件链接失效，已改到新位置）；`validation/h1/resolve_refs.py` 按各文件声明的基准目录解析六个搬走的文件里写的相对路径，预期的 2 处「未解析」都不是缺陷（一处是示例路径，一处是模板正文里写明「在 scrum-kernel 技能文件夹」的 `overview.md`）。结果列进第 5 章。
  - **插件校验、描述长度、DSH 分发**：见上面各条。
  - **Outcome Done**：见上面「Outcome」一条。
- **84**：对基线提交 `1145382` 逐文件比，五个 `IDEO-modes/*.md` 去掉头部引注行后的正文逐字相同（脚本比）；头、`ATTRIBUTION.md` 第 3 节与 `README.md`／`README.zh-CN.md` 授权表里 d.school 的一行，三处逐项一致、都对上两源，许可有可达链接或存档出处；这次提交里除这三类文件外不应有改动。
- **描述长度**：改过与新增的 `description` 逐条用脚本量，全部 ≤1024，并在第 5 章写出数值。
- **触发**（同日、同环境、同一脚本）：
  - **冻结的文件**：题面 `scrum/sprint-27-wrap-up/validation/trigger/prompts.json`，判定与运行脚本 `scrum/sprint-27-wrap-up/validation/trigger/run_trigger.py`（v1 为 `91aac4e`，A2 换题后的 v2 随下一个冻结提交；v1 未读结果即作废，见第 4 章）。改前臂取基线提交 `1145382` 的 `git archive`，改后臂取冲刺分支上冻结提交之后的提交；题不带引导词；原始输出放 `S:/IDEO-Scrum-Archives/sprint-27-wrap-up/trigger/`，仓库里只留判定汇总。
  - **组与分母**：A 杂活（更新看板、收齐等 PO 拍板的事、讲解机制）、B 外部视角（以新店员或外部利益相关者身份评原型与增量）、C Master 事务（开冲刺并主持 Planning、过检查点、走 Review 与 Retro）各 3 题；每题每臂 3 次，**每组每臂分母 9**（有效试次）；每臂共 27。
  - **行为栏**（唯一判定的一栏）：一个试次里，Skill 工具被调用过 `ideo-scrum:<角色>`（任何时候，调用几次都只算一次）。**分子**：A 组数 `supporter` 被加载的试次，B 组数 `stakeholder`，C 组数 `scrum-master`；某试次加载了两个角色，两个角色各计一次（命中与混用分别计）。
  - **内容栏**：不设。本测试问的是「用户说一句平常话，插件的哪个入口被叫来」，答案内容与此无关；试次限 4 轮、只给读文件的工具，也无从判答案；两臂同一口径。
  - **过线**：A 组改后臂分子 ≥6（分母 9）；B、C 组改后臂分子各 ≥ 同组改前臂分子（不留余量，Master 2026-11-22 定，依据 AGENTS.md「改了描述就重跑触发测试，结果不能比改前差」；不降线）。**两条混用线**只计改后臂：B 组中 `supporter` 被加载的试次数 ≤1（分母 9）；A 组中 `stakeholder` 被加载的试次数 ≤1（分母 9）。
  - **补跑**：某组只差一次未过（A 组分子 5；B、C 组改后臂分子比改前臂少 1），该组两臂同补一轮（每题再 3 次，分母 18），按合并计数重判一次——A 组线 ≥12/18，混用线 ≤2/18，B、C 组仍是不低于改前臂；只补这一轮，不挑样本。
  - **技术失败**（无 init、无 result、超过 240 秒、执行错误；`error_max_turns` 算有效）：每个槽位最多补跑 2 次，按第一次有效的算。
- **加载**：Claude Code 无头，`/ideo-scrum:supporter` 的 Skill 调用顺序为 ideo-kernel → scrum-kernel，3/3，且不加载 sprint-kernel、design-kernel。DSH：交 IDEO 秘书会话（Master 转），在 Standard 会话看到 `/supporter`、按 ideo → scrum 预载、读得到新位置的模板；证据取原生事件，不取模型复述（手册第 28 条）。
- **89**：`selftest` 新增正例（`Test: Concluded — awaiting archive`；带阶段前缀、无「已」的 `收官 · …`）与负例（进行中写法里出现 closed、待收官）各至少 1 个，原有场景不变，全过；三态合成日志（开放、`Concluded — awaiting archive`、迁出活动路径）重跑通过。
- **90**：九条各有结论与理由；做了的各有 diff；中英对照页 `check_docs.py` 通过。
- **角色边界**（Master 2026-11-22 加）：Test 里派一个全新子代理（Master 派，显式写 `model`），对 `supporter` 入口、`overview.md` 约定 8、10、12、14、`stakeholder` 入口、`scrum-master`／`developer`／`designer` 入口里「问 PO」与「Report to the Scrum Master」那几条的边界文字做一次对抗核对，查：① 有没有与「不排序、不决定、不审阅、不改插件文件」或 Review 召唤权相冲的句子；② 有没有让 Supporter 自己做决定、变成审批人（批准、拒绝、代答）的句子；③ 有没有越过三类例外（工具权限与设置、`CLAUDE.md`／`AGENTS.md`、推送发布，这些要 PO 本人确认）的句子；④ 有没有让各角色把自己能定的事也推给 PO 的句子；⑤ 约定 14 一处写、其余引用，有没有哪处自己又写了一遍规则或与约定 14 说法不一；问题逐条写处置。

**精化决定**（2026-11-22）：PO 定了 Q1–Q3，认可其余：「剩下的我觉得问题不大了」。Developer 同步（第 6 步：提出疑问、逐点复述；PO：「其实不叫审核，应该叫同步」）无疑问即结束精化、进 How，Master 按书面授权确认；PO：「差不多了就可以进入，让27就是同步给冲刺27的 developer，然后进入 How 阶段。」施工放行由 Master 审过 How 后按授权给。提交由 Developer 自行做，不推送（PO：「提交的话就 developer 那边做就行了，你就不用管了」）。

## 3. How

<!-- The Developer writes this chapter as a plan for making the selected items, short and not in detail (sprint-log.md, convention 7): the work items in order, each with its output and how to tell it is done; the key choices and why; the risks and open points. The last line is the go-ahead (sprint-log.md, convention 8). -->

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| H1 | 85 迁路径（第一项，M） | 四份日志模板集中到插件根的 `template/`，`board-log.md` 与看板模板进 `board/`（`git mv`，文件名不变）；`SKILL.md`、各 `conventions/`、`overview.md`、`check.py`／`prepare_review.py`／`stranger_test/driver.py` 里的路径常量、docs、README 中英、`.gitignore` 注释、`package.json` 的 `files` 同一提交改全；产品日志里的旧路径（PBI-89 的 Place 一栏）、`scrum/documents/sprint-roadmap.md` 的看板约定链接、本日志的旧路径同一提交一并改 | ✓ 2026-11-22 旧路径按 2.2「通过线」的范围与放行清单全仓 grep 为零；`validate --strict`、`check_dsh`、`check_docs.py`、`board_check selftest` 通过；`npm pack --dry-run` 含新目录 |
| H2 | 86 supporter 入口与改称（M） | 新 `commands/supporter.md`；`stakeholder`、`scrum-master` 两入口改称；`overview.md` 约定 8、14，glossary（中英一对）、README 中英、`check_docs.py` 术语表、`project-stakeholder` 里的旧说法同步；SGEP 引文在 `ATTRIBUTION.md` 登记；PO 2026-11-22 追加的三条（联络点、转达的 PO 意见视同 PO 的、三级分流）规则只写在 `overview.md` 约定 14，约定 10、12 与各角色入口的「问 PO」只引用 | ✓ 2026-11-22 插件、docs、README、脚本里旧称法 grep 为零；改过与新增的描述 ≤1024（脚本量）；Review 召唤权与建造者边界的句子都还在 |
| H3 | 86 的 DSH 部分（S） | `dsh/index.js` 角色表、`dsh/locale/en.json`、`zh.json`、`check_dsh.mjs`、`docs/maintaining*.md` 加 supporter；2.2 的 DSH 验收条目交 Master 转 IDEO 秘书会话 | ✓ 2026-11-22 `check_dsh` 通过且覆盖五个角色；`npm pack --dry-run` 含 `commands/supporter.md`；验收条目已交 Master |
| H4 | 84 署名（S） | 五个 `IDEO-modes/*.md` 的头与 `ATTRIBUTION.md` 第 3 节补成两源，正文不动 | ✓ 2026-11-22 对基线逐文件比，正文逐字相同；头与第 3 节逐项对上；许可有链接或存档出处 |
| H5 | 89 看板收尾态（S） | `check.py` 修三处并加正负例；`board/board-log.md` 第 12 条补一句；`template/ideo-backlog-template.md` 的 `For` 占位补提 `DesignBacklog.md`；`ideo-log.md` 约定 4 的 For 说明同步（与模板 `For` 占位、看板宿主判定对齐） | ✓ 2026-11-22 `board_check selftest` 全过且含新增正负例；三态合成日志重跑通过；条文与脚本一致 |
| H6 | 90 九条（S） | 做 ①②④⑤⑦⑧⑨，⑥ 在快速上手补一行，③ 不做；只动 `second-opinion`、`project-stakeholder`、`advisor.md` 的正文与 `docs/project-agents*.md`、`quick-start*.md`，不动任何 description | ✓ 2026-11-22 九条各有结论与理由；做了的有 diff；`check_docs.py` 通过 |
| H7 | 收口 | `CHANGELOG.md` 的 Unreleased 补记；全仓 grep 复核；`validate --strict` 后派 `plugin-dev:plugin-validator`（Haiku，新命令与 frontmatter 改动属结构变化）；2.2 通过线提交冻结；报 Master 请放行 Test | 上述检查通过；通过线已提交；Master 审过 Increment |

**Key choices**

- **模板与看板放插件根的 `template/`、`board/`（Master 2026-11-22 按授权定，DSH 对照测通过，见 2.2 PBI-85 的定案）**：用户故事是「按用途一眼找到」，PO 原话是「模板专门拉一起放在 template 里面」，一处共用才拉得到一起；26 的记忆与约定包也会在同级。当时提的三点（探测前的写法，现已全部走通）：
  - ① **相对路径怎么写**：照现在的做法，按「引用它的技能文件夹」写，统一为 `../../template/<文件>`、`../../board/<文件>`——不裸写文件名，也不因引用者在 `SKILL.md` 还是 `conventions/` 而变（约定文件已声明 `../` 相对技能文件夹）。与 AGENTS.md「引用别的技能的文件写 `../<kernel>/file.md`」同一个精神，只是多上一级。
  - ② **`package.json` 的 `files` 要加**：加 `plugins/ideo-scrum/template/`、`plugins/ideo-scrum/board/`。现有清单只含 `commands/`、`skills/`、`icon.png`，不加则 DSH 包里没有模板。Claude Code 是整个插件文件夹进缓存，不用另加。
  - ③ **DSH 读得到吗**：设计上可以——`roleRouting` 让模型按「点名该资源的内核」的绝对路径读，`../../template/…` 拼出来就是包内绝对路径；`check_dsh.mjs` 可静态核每条 `../../template`、`../../board` 引用都落在打包清单里。但 DSH 的 `read` 工具读不读得了 `skills/` 之外的包内路径，本会话验证不了（现有证据只到跨内核，即 `skills/` 之内）。建议放行前让 IDEO 秘书会话探一次：在 DSH Standard 会话里读 `<内核目录>/../../commands/developer.md`（包内、`skills/` 之外）；读不到就退回。
  - 两个方案改的地方一样，只差路径前缀。
- **86 的定位：Supporter 是 SGEP 里的一种 Stakeholder，只取「照请求做事」这一面**，不取 change agent、guiding coalition（按作者约定标明）。入口与 `stakeholder` 分开：`stakeholder` 给外部视角（拿角色卡的新子代理），`supporter` 做常驻杂活；两条描述各写明「不管什么」，防模型混用，触发测试专门盯这条。`overview.md` 约定 8 的表加 Supporter 一行（标「a Stakeholder type」），约定 14 把「Stakeholder 会话带工作身份」改成 supporter。SGEP 引文照抄，署名在 `ATTRIBUTION.md` 登记，命令文件不加头两行。PO 随后追加三条职责或权限（联络点、转达的 PO 意见视同 PO 的、三级分流）：只写在约定 14 一处（重排成一小段加四条：做什么、问题往哪去、回答怎么回、PO 的话怎么转），约定 10 与 12 只指向它，各角色入口的「问 PO」各一句引用，不各写一遍；supporter 的描述不再加（977 字符），新内容进正文。
- **中文叫法「秘书」（Master 2026-11-22 定，不转 PO）**：这是 PO 的口头用词，也是 Sprint Goal 用的词；英文入口 `supporter`；glossary 写「Supporter ｜ 秘书」，释义里注一句只取 SGEP Supporter「照请求做事」这一面。备选「支持者」是直译，读着像拉拉队，不像干杂活的。
- **Q4：不在入口钉 `model`，也不写建议**：杂活多用便宜模型，但 PO 也会让它讲机制，钉死会误伤；看板约定本来就写了「便宜的模型就能写」。
- **`scrum-master` 只改描述与 Identity 一段**：杂活去向改成 supporter；明写有权——守流程、审、在书面授权内代 PO 定；Scrum Guide 摘录不动。
- **89 三条建议都做，脚本只放宽不收紧**：每处配正例与负例；收官态写法以约定为准，约定没说的不判错。
- **90：做 ①②④⑤⑦⑧⑨，⑥ 补一行，③ 不做**：七条各是一两句正文或一个 frontmatter 提示，且不碰 description，不引发触发测试。⑥ 查得 README 已链（中英 README 末尾文档链接列表里的「Project agents and second opinions」一条），快速上手没链，在其「When you are lost」一节末补一条（用标题引用，不写行号，行号随改动会变）。③ 不做：改召唤示例要 Review 批准加实机验证，现有示例准确，等 PO 体验后再定。
- **提交分开**：H1 一个提交（grep 到零）；H2、H3、H4、H5、H6、H7 各自提交；改号不在本期。

**Risks and open points**

- 触发测试有随机性：便宜模型、每臂 27 次；B、C 组的线是「≥ 改前臂」，不留余量（Master 定），只差一次的组两臂同补一轮，已在 2.2 写定；两臂同日同环境跑，技术失败补足不挑样本。
- 与 26 的接口：26 稍后会改所有角色入口（含 supporter）的加载方式；`supporter.md` 与其余入口保持同一版式，让 26 的改动可以机械地做。27 合入 main 后，Master 把改动文件与规矩列给 26。
- 约定改在冲刺内（项目规矩是约定攒着集中改）：`overview.md` 约定 8、10、12、14，`board-log.md` 第 12、16 条，`ideo-backlog-template.md` 的 `For` 占位，`ideo-log.md` 约定 4，都是 PO 交给本期的条目所需。起初只是一行表项、一句替换和一句补明，Master 判不算大改约定；后来 PO 追加的三条（联络点、转达的 PO 意见视同 PO 的、三级分流）改变了「谁能代 PO 发话、问题往哪去」，比这个量大，但都是 PO 本人的决定（2.2 Q2 原话）、规则只写一处、不改 Scrum Guide 原文。审法不变：Master 审，Test 里全新子代理对角色边界文字做对抗核对（范围见 2.2「角色边界」）；是否另走 PO 强审由 Master 定。合入时 Master 把这些改动列给 26。
- 转达的 PO 意见没有身份验证：接收方只凭「标明、原话、日期」判断，冒称 Supporter 的会话能发出「PO 的意见」。三类例外（工具权限与设置、`CLAUDE.md`／`AGENTS.md`、推送发布）与「只传 PO 对它说过的话」堵住最大的口子，但普通决定与阶段放行走这条路时，靠 Supporter 的诚实和 PO 事后在日志里看到 `PO (via Supporter)` 记号。这是 PO 的决定，只记风险，不改。
- 没有 Supporter 会话时，各角色照旧直接问 PO（约定 14 已写）；Supporter 会话一旦存在，它就成了所有「只有 PO 能定」的事的必经之路，会话断了、没人起它时消息会堆在那儿——这靠各日志头部的 `Waiting for PO` 兜底（它收的就是这些行）。
- 版本号不动（仍是未发布的 0.6.3 候选），`CHANGELOG.md` 的 Unreleased 补记；要给新角色升号，另议，单独提交。
- DSH 实装验收靠 IDEO 秘书会话，由 Master 转交；转不动时只有 `check_dsh` 与打包核对这些静态证据，Test 里如实记「实装未验」。
- 90 的「不做 ③」要 Master 认可：PBI-90 的验收是「九条每条有结论与理由」，不做也算结论。
- 产品日志 §2.1 里旧的助手角色卡与 §2.2 地图里的对应节点（Q7）归 Master 收官时改；它们是 2.2「通过线」里列明放行的几处之一。

Go-ahead: 2026-11-22，Master 按 PO 的书面授权（见第 4 章）放行 H1–H7。范围：在本分支提交，按 Key choices 分开提交；不推送、不改版本号、不发版；合入 main 在收官时另定；Sprint Test 另等 Master 放行。条件：① 触发测试 B、C 组的通过线改成「≥ 改前」（AGENTS.md：结果不能比改前差），Risks 里「留 −1 余量」同改，改完再冻结；② H1 的模板与看板位置等 DSH 探测结果定：读得到包内 `skills/` 之外的路径，就用插件根的 `template/`、`board/`；读不到，就退回各内核自己的 `template/`，看板放 `skills/scrum-kernel/board/`。结果回来前可以先做不依赖位置的 H4、H6。90 不做 ③，Master 认可。当时的目标原文：「秘书管杂活：看板、传话这类杂活交给秘书，PO 不用操心，各角色的叫法不再混；模板、看板各归其位，留下的小毛病补齐，熟手照着就能用。」

## 4. Increment notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (sprint-log.md, conventions 9 and 20). A session that picks up the Sprint reads these first. Record the Product Owner’s decision on the Increment and whether the Sprint Test has been authorized. Developer checks inside building are not this Test (sprint-log.md, convention 24). -->

- **开张（2026-11-22）**：Developer 会话建日志；基线 `1145382`（等于 main），分支 `worktree-sprint-27-wrap-up`（原生 worktree 前缀；收官打 tag `sprint-27-wrap-up`，并删此分支）。已读：三内核、产品日志、[六期总表](../documents/sprint-roadmap.md)与其「续」一节。Why 尚未放行：不起草目标、不选条目、不写 How（`overview.md` 约定 12）。
- **PO 书面授权（2026-11-22，原话逐字，抄自[六期总表](../documents/sprint-roadmap.md)「续」一节；「B 线」指本期）**：
  - 「B 线的话，我基本上就交给 AI 自己做了就是交给 Developer 自己做了，我就不参与 Developer 的团队了。」
  - 「我建议是能给 B 线的就给 B 线，这样我就不用操心了，让 B 线自己去重组。」
  - 「B 线的话就是 developer 自己做，然后你来审审核他，你们两个一块做就行」
  - 89、90 交 27：「交给他，交给他呗，可以啊，你觉得可以就行。」
  - 范围由 Master 提议，PO 认可：「OK，你定的这些就是这样子。」
- **授权范围**：本期各阶段决定——定 Sprint Goal、结束精化、施工放行、Sprint Test 放行、收官与本地合入 main——由 Master 代 PO 做，记进本日志（每条写谁定、何时、依据）。**仍回 PO**：改 Product Goal；推送与发布；取消冲刺；推翻 PO 说过的话；PBI-86 的新称法与秘书定位（PO：「后面修改的话再说具体的那个修改内容」）；PO 点名要看的品味。
- **并行约束（总表「续」）**：27 先合 main，26 再动插件文件；85 的迁路径排第一项；27 碰的范围——模板与看板（85、89）、角色入口与旧的助手称法（86）、`IDEO-modes/` 与 `ATTRIBUTION.md`（84）、`project-stakeholder` 与参谋入口（90）——26 暂不动。
- **同步与 How（2026-11-22）**：Master 通知第 1、2 章已定，86 改名 `supporter`（Q1、Q2、Q6 已改）。Developer 重读磁盘日志，无疑问，逐点复述五条发 Master；写第 3 章 How（H1–H7），并按 2.2 的要求补了通过线（Developer 拟，Master 审）。提交由 Developer 在本分支自行做，不推送（PO：「提交的话就 developer 那边做就行了」，经 Master 转述）。
- **触点盘点（写 How 时查得；施工时再全仓 grep 复核）**：
  - 85：四个 `SKILL.md`；`sprint-log.md`、`design-log.md`、`product-log.md`、`board-log.md`、`overview.md`；`scripts/board_check/check.py`（`TEMPLATE`）、`prepare_review.py`、`scripts/stranger_test/driver.py`；`docs/glossary.md`、`docs/maintaining*.md`、`README*.md`；`.gitignore` 的注释；`package.json` 的 `files`。`CHANGELOG.md` 里的旧路径是历史条目，不改。
  - 86：`commands/stakeholder.md` 与 `scrum-master.md` 的 description（旧的助手称法写在各自第 2 行，当时约 860、730 字符）；`overview.md` 约定 8、14；`docs/glossary.md`；`check_docs.py` 的 `GLOSSARY_TERMS`；`claude-skills/project-stakeholder/SKILL.md` 第 67、81 行；`README*.md` 第 93、151 行；`dsh/index.js` 与 `scripts/check_dsh.mjs` 的 `roles`；`dsh/locale/*.json`；`docs/maintaining*.md`。`package.json` 的 `files` 含 `commands/`、`skills/`，不含 `claude-skills/`、`agents/`（这两处只给 Claude Code）。
- **Master 对三问的答复（2026-11-22，Master 按授权）**：① 模板放置倾向插件根一处共用 `template/`（合 PO 原话），How 须写清相对路径、`files`、DSH 读取三点，一点走不通就退回各内核自己的 `template/`；② 中文叫法用「秘书」（PO 自己的叫法，不转 PO），glossary 写 Supporter｜秘书，再注一句只取 SGEP Supporter「照请求做事」这一面；③ `overview.md` 约定 8、14 与 `board-log.md` 第 12 条的改动是新角色带来的称法与分工更新，不算大改约定：Master 审，Test 里再加一个全新子代理对角色边界文字做对抗核对，不用 PO 强审。90 不做 ③、Q4 入口不钉 `model`，Master 都同意。
- **接手点**：施工已放行（第 3 章末行：H1–H7，本分支提交，不推送、不改版本号、不发版；Test 另等放行）。H4、H6 不依赖位置，先做；H1，以及依赖它的 H5、H2 里引用看板约定的一处，等 Master 转来的 DSH 探测结果——读得到 `skills/` 之外的包内路径就用插件根的 `template/`、`board/`，读不到就退回各内核自己的 `template/`、看板放 `skills/scrum-kernel/board/`。做完一项，在第 3 章该行 Done when 前加 `✓ <日期>`，并在这里记改了什么、为什么。
- **Master 放行 How（2026-11-22）**：条件 ① B、C 组触发通过线改成「≥ 改前臂」，依据 AGENTS.md「改了描述就重跑触发测试，结果不能比改前差」，担心噪声就加次数、不降线——已改 2.2 与 Risks，只差一次的组两臂同补一轮的规则现在写定；条件 ② H1 位置等探测。A 组 ≥6/9 与两条混用线照旧。
- **顺序调整（2026-11-22，Developer 在 How 授权的范围内调，Master 知悉）**：How 表里 H1 排第一，实际先做 H4、H6，再做 H2、H3、H5，H1 放到最后。原因：H1 的位置（插件根的 `template/`、`board/`，还是各内核自己的）要等 DSH 探测结果，而 H4、H6、H2、H3、H5 都不依赖位置。H2、H3、H5 在原位置改内容，H1 再 `git mv`，文字跟着走；这些新写的文字里不写会变的路径。H1 收尾的全仓 grep 要把 H2、H3、H5 新写的文字也算进去（Master 要求）。第 3 章的行序不改，保留原计划，调整记在这里。
- **H4 · 84 署名（2026-11-22）**：五个 `IDEO-modes/*.md` 的头三行统一改成两源——2010 *Design Process Mini-Guide* 为底本（CC BY-NC-SA 3.0 Unported），2018 *Design Thinking Bootleg* 为补料（CC BY-NC-SA 4.0）；各带可达链接（两份 CC 许可全文、2010 PDF 的 Wayback 存档、Stanford 页）。正文没动：对基线 `git diff --numstat` 每个文件 3 增 3 删，hunk 只在 `@@ -3,3 +3,3 @@`。`ATTRIBUTION.md` 第 3 节拆成 3.1（2010 底本：许可依据是 d.school「Design Resources」维基首页的声明，写明声明在首页、原站已下线、未另取书面确认，附两条存档链接）和 3.2（2018 补料与方法库，加五模式补料对应表：8／6／9／7／8 块，共 38，对应 2018 PDF 第 3–12 页）；NonCommercial 提示改成「两份许可都含」。Test 的头与另四个相同（PBI 要求五个都补双源），2018 补料没有保留独有表述写在 3.2 的表里。另改 `README.md`、`README.zh-CN.md` 授权表的 d.school 一行，免得与 `ATTRIBUTION.md` 不一致（PBI 原文没列，按「改一条规矩先找它的其他说法」顺手做）。证据：Wayback 首页与 PDF、Stanford 页、CC 3.0 许可全文四个链接实测均 200（2026-11-22）；仓外取证在 `S:/IDEO-Scrum-Archives/sprint-21-design-board/h6-9558a0a/checks/attribution-audit/`；`check_docs.py` 无错误。
- **H2 · 86 supporter 入口与改称（2026-11-22）**：
  - **新入口** `commands/supporter.md`：版式与 `stakeholder.md` 相同（加载 ideo → scrum，DSH 一句，子代理一句，约定一句）；Identity 引 SGEP 原文短语「a specific Stakeholder type」「doing what is requested」「participate when and where needed or as requested」，并用斜体注明作者取舍——只取「照请求做事」一面，不取 change agent、guiding coalition；「做什么」五条（看板、整理日志与汇总、传已定的事、讲解机制、其他杂活）；Code of Conduct 九条，沿用旧边界（不排序、不决定、不审阅、不改插件文件，范围、条目与放行走 Master），另写明「不是外部视角」（外部视角由新子代理拿角色卡给，Review 只由 PO 或 Master 召唤）、「源码归 Developer」。不钉 `model`（Q4）。文件头无两行署名，署名在 `ATTRIBUTION.md` 第 2 节加了一行本仓库位置，并把修改说明里的角色命令清单加上 supporter。
  - **`stakeholder.md`**：description 删去旧助手身份的全部说法（860 → 599 字符），保留判别词「outside view」「fresh subagent given a role card」「Any role may summon…never the builder」「rather than claiming fresh eyes」「Feedback goes to the PO」，末句指向 `supporter`；Identity 改成只给外部视角；删原来那条「助手而非第二个 Scrum Master」的行为准则与另三处牵连的半句；Review 召唤权与建造者边界的句子都在。
  - **`scrum-master.md`**：description 杂活去向改为 Supporter（729 → 718）；Identity 后加一段「你是 Master，不是秘书」：守流程、审、在书面授权内代 PO 定，优先级、目标等价值决定仍归 PO，没有决定的杂活交 Supporter；第 57 条里把看板与汇总交给常驻 Stakeholder 会话的那句改指 Supporter。Scrum Guide 摘录未动。
  - **`overview.md`**：约定 8 的角色表 Stakeholder 一行只剩外部视角，新增 Supporter 一行（注明 SGEP 里是 Stakeholder 的一种，加载 ideo → scrum）；约定 14 改为「交给常驻的 Supporter」，边界一句不变、外部视角指 `stakeholder`。约定 15 里的「the author's assistant」指作者的 AI 助手，不是这个角色，不改。
  - **其余同步**：`board-log.md` 第 3 条里写看板的常驻会话那一处改指 Supporter；`project-stakeholder/SKILL.md` 两处；`docs/glossary.md`（Stakeholder 一行去掉杂务，旧的助手词条换成「Supporter｜秘书」，释义里注明只取 SGEP「照请求做事」这一面，Master 定）；`scripts/check_docs.py` 的术语表；README 中英（角色清单、斜杠命令块与 DSH 块各加一行、看板一段、文件表「五个角色」）。
  - **没动、留给后面**：DSH 角色表、locale 与 `check_dsh.mjs`、`docs/maintaining*.md`、`docs/project-agents*.md` 的「四个角色命令」（H3）；产品日志 §2.1 旧的助手角色卡与 §2.2 的图（Q7，Master 收官时改）；`CHANGELOG.md`（H7）。`maintaining*.md` 第 29 行是 2026-11-20／21 对旧 0.6.3 候选的迁移实测（「四个角色」），属历史证据，H3 时加限定说明、不改写，并报 Master。
  - **检查**：旧称法 grep（词表见 2.2「通过线」）当时查了 `plugins/`、`dsh/`、`docs/`、`README*`、`scripts/`、`package.json`、`ATTRIBUTION.md`，无命中（Codex 详审指出：这个范围与 2.2 不一致、没含 `.gitignore` 与根目录规则文件；范围已在 2.2「通过线」统一为整个仓库加五类明列的例外，全范围的最终 grep 在 Test 里跑）；描述长度 718／599／681，皆 ≤1024；`check_docs.py`（195 条链接）与 `--selftest`（17 例）通过；`claude plugin validate --strict` 通过，已列出 `ideo-scrum:supporter`。触发测试要等描述定稿后与改前同日对照，放在 H7。
- **H3 · 86 的 DSH 部分（2026-11-22）**：`dsh/index.js` 与 `scripts/check_dsh.mjs` 的角色表各加 `supporter`（排在 `stakeholder` 之后，`check_dsh` 比对注册顺序）；`dsh/locale/en.json`、`zh.json` 的描述加 `/supporter`（`check_dsh` 要求描述含每个角色的斜杠名）；`docs/maintaining*.md` 第 15 行改为「四个内核与五个用户可调用角色」并列出 `/supporter`；`docs/project-agents*.md` 的「四个角色命令」改为五个。`maintaining*.md` 第 29 行是 2026-11-20 对旧 0.6.3 候选的迁移实测，只在「四个角色」前加「当时的」（英文 `of that date`），不改写证据；这一条按 Developer 的判断做，请 Master 审时留意。检查：`node --test scripts/check_dsh.mjs` 7／7 通过（含注册顺序与五个角色预载）；`check_docs.py` 无错误；`npm pack --dry-run --json --ignore-scripts` 共 101 个文件，含 `commands/supporter.md`。
  - **DSH 验收条目（交 Master 转 IDEO 秘书会话；隔离环境，不碰日常实例；证据取原生事件，不取模型复述，手册第 28 条；链接本分支的 `plugins/ideo-scrum`，记下提交号）**：① 开 Standard 会话，技能建议里有 `/supporter`，其余四个角色仍在；② 输入 `/supporter` 加一句杂活（例如汇总冲刺走到哪），会话日志里 `user/message` 的 `skill-invocation` 来源是 supporter，原生角色内容里按 IDEO → Scrum 预载，没有 sprint-kernel、design-kernel 的预载；③ 同会话从某个内核目录读 `../../commands/developer.md`（包内、`skills/` 之外的路径），回报读得到还是读不到——这是 H1 的位置探测；④ 记 DSH 版本、链接路径、会话日志位置，原始记录放仓外。
- **H7 准备 · 触发测试题面与脚本冻结（2026-11-22）**：Master 同意「先提交冻结再跑」，通过线不改（A ≥6/9，B、C 不低于改前，两条混用线照旧）。
  - **重冻结（Master 要求记清三件事）**：① `91aac4e` 冻结过 v1；② 第一轮在旧的 supporter 描述上起跑，PO 的联络点职责随后经 Master 转来，描述要变，我立刻杀了这一轮，**没读过任何一条结果**，部分输出封存为 `…-round1-ABORTED-superseded-unread`，不计入；③ 为什么重冻结：冻结的目的是防「看了结果再改标准」，这里结果没看、描述又确实要变，所以重冻结不违背它；同时 A2（汇总进度）换成「把现在各条线上等我拍板的事都收齐，一次问我」——汇总进度与 Master 的「跟进度」重叠最多、看板题已覆盖「各条线走到哪」，联络点是新职责，需要自己的一题（Master 认可）。v2 随下一个冻结提交，题面文件里的 `_note` 记了这件事。
  - **v2 又补了定义**：Codex 详审（2026-11-22）要求 2.2 引用冻结文件路径、写明每组分子分母、行为栏与内容栏怎么判、混用线怎么计——已写进 2.2「触发」一条，在冻结之前。
  - **触发测试第 1 轮结果（Developer 在施工内按冻结线跑的，2026-11-22 21:27；正式 Test 放行后引用为新证据，Master 若要 Test 里重跑，说一声）**：改前臂 `1145382`、改后臂 `52b42fa`（描述都已定稿），v2 题面不动；两臂各 27 次有效、技术失败 0、没有补跑；原始输出在 `S:/IDEO-Scrum-Archives/sprint-27-wrap-up/trigger/20261122-212701-round1/`（`raw/` 108 份流与错误日志、`results.jsonl`、`meta.jsonl`），仓库只留这份汇总。模型是 magpie 的便宜模型，非 Haiku（`--model haiku` 被包装器映射）。
    | 组（题数×3 次，分母 9） | 改前臂 命中 | 改后臂 命中 | 混用（改后臂） | 过线 |
    | --- | --- | --- | --- | --- |
    | A 杂活：加载 `supporter` | 0／9（`supporter` 不存在；2 次加载 `stakeholder`，7 次什么角色都没加载） | 9／9（A1、A2、A3 各 3／3） | `stakeholder` 0／9（线 ≤1） | ✓ ≥6／9 |
    | B 外部视角：加载 `stakeholder` | 3／9（B1 0、B2 0、B3 3） | 4／9（B1 1、B2 0、B3 3） | `supporter` 0／9（线 ≤1） | ✓ 4 ≥ 3 |
    | C Master 事务：加载 `scrum-master` | 9／9 | 9／9 | — | ✓ 9 ≥ 9 |
    - **行为栏**按冻结定义只看 Skill 调用；**内容栏不设**（见 2.2）。试次都在限制下跑：54 次 init 的工具集都是 `Glob Grep Read Skill`、`permissionMode` 都是 `dontAsk`，出现过 21 次权限拒绝（限制在起作用）；51 次因 4 轮上限以 `error_max_turns` 结束（按冻结规则算有效，加载入口与内核就要占几轮），3 次 `success`；单次最长 72.9 秒。
    - **我读出来的两点，供审时参考（不改线、不补跑）**：① A 组的 9／9 对 0／9 主要是因为改前根本没有这个入口——改前臂有 2 次把杂活叫进了 `stakeholder`（旧的助手身份），7 次什么角色都没叫，说明杂活原来没有明确的家；② B 组两臂都偏低（改前 3／9、改后 4／9）：B2「草图想听店员怎么看」两臂都是 0／3，B1「假设你是新店员」只有改后臂 1／3，B3「从外部利益相关者的角度」两臂 3／3；就是说 `stakeholder` 的描述对不带「利益相关者」字样的外部视角请求本来就不灵——这是原有的缺口，不是本期引入的退步（Sprint 18 的自然触发专项已被 PO 取消，不在本期范围）。
    - **H1 之后是否重跑**：H1 只迁模板与看板的位置、改正文里的引用，不碰任何 `description`；H1 提交后我用 `git diff 52b42fa` 核五个入口与四个内核 `SKILL.md` 的 `description` 行逐字未变，则本结果继续有效，不重跑；若有变，重跑。
  - **做法**：`validation/trigger/run_trigger.py` 每个试次起一个 magpie 无头会话（`--model haiku` 被包装器映射到 magpie 的便宜模型，非 Haiku），工具只留 `Read,Grep,Glob,Skill`，`--permission-mode dontAsk`、`--setting-sources project,local`、`--strict-mcp-config`；环境白名单、全新家目录、运行目录放 `C:\Users\Public\s27-trigger\`（上级没有指令文件）；项目用 `scripts/board_check/fixtures/acme` 的副本；两臂的插件用 `git archive` 取提交，不用工作区；判定只读流里的 Skill 调用（`ideo-scrum:<角色>`），某个角色在试次里任何时候被加载即算「加载」。三组各 3 题（`prompts.json`，题不带插件名、角色名或引导词），每题每臂 3 次，每臂 27 次；两臂交错跑，3 个并发；技术失败（无 init、无 result、超时、执行错误）补跑最多 2 次，不挑样本；`error_max_turns`（限 4 轮）算有效。「只差一次」的组两臂同补一轮、合并计数重判一次，规则在 2.2 与脚本里都已写定。
  - **自测与冒烟**：判定脚本自测 15 项通过（含：只含角色名的技能不算角色、没前缀的名字算、技术失败与重试只算一次、不完整的格不当通过）；隔离探针 `/context all` 无指令文件泄入；冒烟每臂一次有效，init 里工具只有 Glob/Grep/Read/Skill、`permissionMode` 为 `dontAsk`；另用一条不在题面里的试探句看到真实流里的写法是 `Skill {"skill": "ideo-scrum:scrum-master"}`，之后接 ideo → scrum → sprint 三个内核，与判定脚本读的字段一致。试探与冒烟不计入。
- **H5 · 89 看板收尾态（2026-11-22）**：
  - **复现**：改前拿探针跑 `host_concluded`，`Test: Concluded — awaiting archive`（设计、冲刺宿主都是）、`测试：已结束，待归档`、`收官 · 2026-11-14，…`（Sprint 18、19、20 的归档日志真有这种写法）都判成「未结束」，IDEO 日志于是还挂在已结束的宿主卡下；`已收官 · …` 与带主语的写法本来就认。
  - **`check.py`**（只放宽、不收紧）：① 冲刺宿主认「收官」，有无「已」都算；② 去掉「有阶段前缀就跳过无主语规则」：阶段前缀剥掉后，无主语的 `Concluded`／`已结束` 也算宿主结束，但**同句要写明待归档**（`archiv`／`归档`）——设计日志约定 19 要求设计结束时在 Now 里写「已结束、待归档」，所以 `Test: Concluded — awaiting archive` 在内；`Prototype: Concluded; Test next` 这类只是一个阶段完了，仍不算。这是我的取舍：不加这个条件，阶段结束会被误读成宿主结束，IDEO 条目悄悄从卡上消失；加了之后最坏是个别没写「待归档」的结束行不被认出，IDEO 条目多挂一会儿，看得见。「阶段前缀剥离」本来就有（做主语规则时），所以第三条建议的实质是上面的②。
  - **自测**（79 → 99 例）：宿主 Now 的写法扩成列表——冲刺 5 种宿主结束（含 `收官 · …`、`已收官 · …`、`Closed · …`、`Test: Concluded — awaiting archive`）加 3 种阶段结束，设计 3 种宿主结束（含 `Test: Concluded — awaiting archive`、`测试：已结束，待归档`）加 3 种阶段结束，每种都核 IDEO 挂不挂；新增「宿主日志已归档在 `scrum/documents/`」的 IDEO 归属、一份归档设计日志不被发现为活动卡（第三态）；新增负例：`solution: null` 却带 `story` 要报错。把改后的自测里新增的场景放到旧逻辑上跑，宿主结束的四种新写法全部失败（探针副本，用后即删），说明这些例子真能抓出缺口。三态合成日志（开放、`Concluded — awaiting archive`、迁出活动路径）即上述宿主三态，重跑通过。
  - **条文**：`board-log.md` 第 12 条补「`solution` 为 `null` 时也省略 `story`」（脚本本来就报错，条文补齐）；第 16 条给「宿主结束」写了几种写法的例子，并说明带阶段名时要同句写明待归档，以便手写看板的便宜模型和脚本判断一致；`ideo-backlog-template.md` 的 `For` 占位说明改成「产品日志、Sprint 的 `SprintBacklog.md`、设计的 `DesignBacklog.md`」。
  - **顺手改的一处（请 Master 留意）**：`ideo-log.md` 约定 4 里「For 指向 product log or sprint log」「结论流回 product log or sprint log」，与模板、看板（`ideo_host` 认设计日志做宿主）不一致，与模板 `For` 占位、看板宿主判定（`ideo_host` 认设计日志做宿主）对齐，同改为含设计日志。约定 2 说「设计冲刺不开 IDEO 日志」，那是设计自己不另开一份，与「别的 IDEO 运行可以服务一个设计」不冲突；若 Master 认为超出本条范围，可退回这两处，不影响脚本与模板。
  - **检查**：`board_check selftest` 99 例通过；`check_docs.py`（195 条链接）通过；`claude plugin validate --strict` 通过。
- **H2 追加 · supporter 加「PO 的联络点」职责（2026-11-22，PO 经 Master 转来，原话在 2.2 Q2）**：
  - **改了什么**：`supporter.md` 的 description（681 → 943 字符，≤1024）与正文——「做什么」加一条联络点（收齐各日志头部 `> Waiting for PO:` 与各会话报来的待决问题，每个问题带上回答所需的上下文，一次交给 PO；再把 PO 的回答原话转回给拥有那份日志的会话，由它记录；范围与放行的回答经 Master 记录），「行为准则」两条补「不替 PO 回答、不删减或改写问题、PO 关于范围与放行的回答也经 Master」；`overview.md` 约定 8 的角色表、约定 14 补反方向；`docs/glossary.md` 中英释义；README 中英的命令注释。
  - **日志边界（Master 2026-11-22 点明，四处同一说法）**：Supporter 照 PO 或 Master 的话整理**产品日志**（登记 PBI、改状态与备注）、维护看板；冲刺日志、设计日志、IDEO 日志由各自的会话写。因此 `scrum-master.md` 描述与 Identity 里的「organizing logs」、overview 约定 8 的表与 glossary 里的「organizing logs／整理日志」都改成「organizing the product log／整理产品日志」，与 `supporter.md` 正文、约定 14 对上。
  - **再追加 · Supporter 转达的 PO 意见视同 PO 的（PO 经 Master 转来，原话与条件在 2.2 Q2，Developer 改进 86 的同一提交、赶在触发题面重新冻结之前）**：
    - **只写一处来源**：`overview.md` 约定 14——转达须标明是 PO 的意见、附 PO 原话与日期，接收方记成 `PO (via Supporter): <原话>`；Supporter 自己的解释、建议不算；引 Scrum Guide 2020 原文「The Product Owner may do the above work or may delegate the responsibility to others. Regardless, the Product Owner remains accountable.」（与 `assets/scrum-guide-2020.md` 第 113 行逐字核过）；不在此列：工具权限与设置、`CLAUDE.md`／`AGENTS.md` 的改动、推送与发布等对外动作，仍要 PO 直接确认。
    - **别处只引用**：约定 12 加一句指向约定 14；`supporter.md` 写 Supporter 这边怎么标明（「做什么」一条、「行为准则」一条「不替 PO 编话」，指向约定 14）；`scrum-master.md`、`developer.md`、`designer.md` 的「问 PO」一条各加一句「Supporter 标明转达的 PO 意见视同 PO 的」，指向约定 14（Master 那句另写了记成 `PO (via Supporter)`）；`stakeholder.md` 不接收 PO 决定，没加；overview 约定 8 的角色表与 glossary 中英各补半句。
    - **描述**：`supporter` 加一句，并删去末句「Board conventions are in scrum-kernel」、把「scope or item changes, go-aheads and the Product Owner's answers about them」缩成「scope or item changes and go-aheads」让位（PO 答案经 Master 记录一事留在正文与约定 14），977 字符，≤1024。
    - **我留意到的风险（请 Test 里的对抗核对一并看）**：转达没有身份验证——接收方只能凭「标明、原话、日期」判断，一个会话冒称 Supporter 就能发出「PO 的意见」；上面三类例外与「Supporter 只传 PO 对它说过的话」把最大的口子堵住了，但普通决定与阶段放行（约定 12）走这条路径时，靠的是 Supporter 的诚实与 PO 事后能在日志里看到 `PO (via Supporter)` 的记号。这是 PO 的决定，我只记风险，不改。
  - **三追加 · 三级分流（PO 经 Master 转来，原话在 2.2 Q2；赶在触发题面重新冻结之前）**：
    - **规则**：各角色遇到要 PO 的事，交给 Supporter 汇总后一次提示 PO，不再经 Master 转。三级：① 自己能定的自己定（Developer 的做法、Designer 的方案细节）；② 归流程的、或在书面授权内的，问 Master；③ 只有 PO 能定、能做的交 Supporter 汇总——Product Goal、条目与优先、没有授权的阶段放行、PO 保留的品味，以及要 PO 本人在场的工具权限与设置、`CLAUDE.md`／`AGENTS.md`、推送发布。Supporter 把不归 PO 的问题退回并说明归谁（本人或 Master），只分流、不替谁做决定；没有 Supporter 会话时照旧直接问 PO。
    - **只写一处**：`overview.md` 约定 14，与「转达的 PO 意见视同 PO 的」放在一起；因为约定 14 已是一大段，重排成一小段加四条（做什么、问题往哪去、回答怎么回、PO 的话怎么转），内容照旧、没有删规则。约定 10 只加一句「约定 14 说各类问题往哪去」（`sprint-log.md` 约定 25、`design-log.md` 约定 21 本来就指向约定 10，不用改）。
    - **别处只引用**：`scrum-master.md`、`developer.md`、`designer.md` 的「问 PO」一条改成一句引用（各类问题往哪去、转达的意见怎么算，见约定 14；Master 那条另写「记成 `PO (via Supporter)`」）；`supporter.md` 正文加「分流，不替谁决定」一条（把不归 PO 的退回并说明归谁；不批准、不拒绝、不代答，也不扣下或改写只有 PO 能定的问题），原「问 PO」一条改成「拿不准就问交给你杂活的人」；supporter 描述按 Master 的话不再加，仍 977 字符。overview 约定 8 的表与 glossary 中英各补半句。
    - **顺手发现并改的一处冲突**：`developer.md`「Report to the Scrum Master」里原写「ask for any new stage permission through it」（阶段放行经 Master 问），与「不再经 Master 转」相左；改为：书面授权覆盖的向 Master 要，没有授权覆盖的只有 PO 能给、按约定 14 走。其余角色入口里没有类似的「经 Master 转 PO」的说法（已 grep）。
  - **检查**：三条描述 977／729／599（developer 476、designer 557），皆 ≤1024；`check_docs.py` 195 条链接无错；`check_dsh` 7/7；`validate --strict` 通过。
- **H6 · 90 九条（2026-11-22）**：逐条结论，涉及 `second-opinion`、`project-stakeholder` 两份 `SKILL.md`、`advisor.md`、`docs/project-agents*.md`、`docs/quick-start*.md`，没碰任何 description。
  - ① 做：参数写法定为 `model: <name>`——`second-opinion` 的 `argument-hint` 加 `| model: <optional>`，§1 加第四项，§3 写明作为 `Agent` 调用的 `model` 参数（例 `model: "opus"`）；docs 写「在请求后面加 `| model: opus`」。
  - ② 做：`project-stakeholder` §1 指向 §3；§3 加「没有何时召唤栏」的路径——只展示定义文件、不加引用，用户选「不带引用写文件」或「停下等 PO 加栏」，不自己改表。
  - ③ **不做**：召唤示例（docs 里的 `Agent, subagent_type: ...`）改成 @-mention 或自然语言，按 Sprint 22 的来源条件要走 Review 批准并实机验证；现有示例准确、能用，成本高于收益，等 PO 体验后再定（Master 已认可）。
  - ④ 做：`project-stakeholder` 加 `argument-hint`（角色卡名）。
  - ⑤ 做：`project-stakeholder` §4 加「宿主自己的提示」一段（`.claude/` 写入另有权限确认，不替代用户对预览的 yes）；docs 第 2 步加一句，中英同改。
  - ⑥ 做一行：README 已挂（中英 README 末尾文档链接列表里「Project agents and second opinions」那一条），快速上手没挂——在其「When you are lost」（中文「迷路了怎么办」）一节末补一条，中英同改。（Codex 详审指出此处原写的行号已过时：README 现在在第 169 行、`docs/quick-start.md` 补的那条在第 89 行；改为标题引用，行号随改动会变。）
  - ⑦ 做：我的读法——「两入口／三条列项」指 docs「按名召唤」的三条：开头写「同一份文件供两个入口使用」，第三条（临时看一眼）却不用文件。改成「供前两种用法使用，第三种不需要文件」，中英同改。归档里只有一句话、没有明细，这是我的读法；Master 若另有所指，请说，我再改。
  - ⑧ 做：`second-opinion` §2 标题改「Keep the brief clean」，docs 的「The context is clean」改「The brief is clean」（中文「交给参谋的说明是干净的」），`advisor.md` 的「a context that carries none of the earlier discussion」改「a fresh context that was given only the brief」。
  - ⑨ 做：`second-opinion` §3 与 docs 写明 `fable` 要账号有权限，用不了时说明并问换哪个模型，不自己选。
  - 检查：`check_docs.py` 无错误（195 条链接）；`claude plugin validate --strict` 通过；description 没动，所以不触发触发测试；frontmatter 有两处加了 `argument-hint`，H7 的 `plugin-validator` 一并看。

- **Master 写第 1、2 章（2026-11-22）**：PO：「你把 S7也先写出来吧。然后这两个我一起审掉。」Developer 原计划的头部与 1.2 改动由 Master 代写；提交等 PO 审后再定。

- **H1 · 85 迁路径（2026-11-22）**：
  - **位置（Master 2026-11-22 按授权定）**：四份日志模板进 `plugins/ideo-scrum/template/`，`board-log.md` 与 `scrum-board-template.html` 进 `plugins/ideo-scrum/board/`，用 `git mv`（提交里是重命名，内容只动引用）。依据是 DSH 对照测，Master 转告：默认受限预设（workspace-write、approval ask）下，DSH 0.2.2-rc.5 加包 0.6.3，`skills/` 里的 `overview.md` 与 `skills/` 之外的 `commands/developer.md` 都读到，`isError:false`、没触发审批、有原生 tool/call 与 tool/result 记录；证据在 IDEO 秘书会话的两份 DSH 会话记录（`session-0fa490f5…`、`session-a3e7f38f…`）——这两份记录我没有自己读过，这里只记 Master 的转告。
  - **引用怎么写**：技能入口、约定与 `overview.md` 里按各自声明的基准（技能文件夹）写 `../../template/<文件>`、`../../board/<文件>`；`board-log.md` 搬出了技能文件夹，开头改成写明「本文件里的路径相对 scrum-kernel 技能文件夹，不是 `board/`」；设计日志模板里一处 `../sprint-kernel/…` 的路径改成「`sprint-log.md`，在 sprint-kernel 技能的 `conventions/` 文件夹」的写法（与其余模板一致，不依赖自己放在哪）。`package.json` 的 `files` 加 `plugins/ideo-scrum/template/`、`plugins/ideo-scrum/board/`。
  - **脚本**：`scripts/board_check/check.py` 的模板常量改到新位置；`prepare_review.py` 与 `scripts/stranger_test/driver.py` 要从**别的提交**读当时的模板（`--baseline`、被测提交），这是我多想的一处：原来写死旧路径，搬了之后读旧提交会失败（`prepare_review`），或者悄悄回退成读现在的模板（`driver` 的 `template_at` 返回空，检查改用当前模板——手册明说这样是错的）。改成按文件名在那个提交的插件目录里找，所以搬之前的提交也读得到它当时的模板。验证：`driver.py selftest` 新增一条对 `v6.0.3`（搬之前）的检查，连同原有的对 `HEAD` 的检查都过；`prepare_review.py --baseline v6.0.3` 生成了材料。
  - **`check_dsh.mjs` 新检查**（回归防线）：六个文件都在新位置、都在打包清单里；技能与约定文件里每条 `../../template/…`、`../../board/…` 都解析得到、都被打包；六个文件各被某个 `SKILL.md` 写到（1 跳）；技能与约定文件里不能再出现旧位置的写法。反向对照：把 scrum-kernel 的 `SKILL.md` 里一条新写法换回旧写法，检查失败，再逐字节还原，检查通过。
  - **文档与记录**：`docs/maintaining*.md`（表行、白名单、链接）、README 中英（看板链接、文件表加两个文件夹）、`docs/glossary.md` 的看板链接、`.gitignore` 的注释、产品日志 PBI-89 的 Place 一栏、总表的看板约定链接、本日志 2.1 的同一格（要与产品日志一致）。归档 Sprint 21 日志第 63 行有两条指向已搬走文件的链接，我只改了这两个链接地址（行里文字没动）——这是我的判断：改前全仓没有一条死链，不改就会多出两条，而项目规矩只禁回改归档的内容；Master 若认为归档一字不动，说一声我还原，并把这两条登记进 2.2 的放行清单。
  - **grep 到零**：旧路径命令（2.2 里原样）在整个仓库只剩 2 处放行（`sprint-09-design-template.md:60`、`conventions-review-log.md:24`），其余 0；旧称法命令只剩 2.2 清单里的 13 处。第一次我只排除了几类目录，Master 要求逐处列出后，把叙述改成不含旧词，清单里列的是所有命中（文件与行号）。
  - **检查结果（H1 提交前，工作区；提交后我在提交上再核一遍并记在这里）**：`claude plugin validate --strict` 通过；`check_dsh` 8/8；`check_docs.py` 195 条链接无错、`--selftest` 17 例；`board_check selftest` 99 例；`npm pack --dry-run` 101 个文件，含 `template/` 四份、`board/` 两份与 `commands/supporter.md`，旧位置的文件 0 个；12 个入口与内核 `description` 与触发测试的候选 `52b42fa` 逐字相同（所以触发结果继续有效）；`validation/h1/dead_links.py`：扫了 153 个跟踪的 markdown、245 条相对链接，死链 0，「基线能通、现在不通」0；`validation/h1/resolve_refs.py`：预期的 2 处未解析（示例路径、模板里写明在 scrum-kernel 技能文件夹的 `overview.md`），其余都解析。
  - **两处自我纠正，如实记下**：① 第一次写 `dead_links.py` 时数错了仓库根的层级，只扫到了 `scrum/` 下的文件，报出的「0」是假的；发现后改对，并让脚本打印扫了多少文件与链接，再跑才得到上面的 0。② 暂存 H1 时我用了目录范围的 `git add -A -- plugins scripts docs …`，违反项目规矩「`git add` 逐个写文件」；当时工作区里只有我自己的改动，对暂存清单逐行核过没有夹带，之后都改回逐个文件。
- **H7 · 收口（2026-11-22）**：
  - **`CHANGELOG.md` 的 [Unreleased]** 补了七条：Supporter、问题往哪去、stakeholder 与 scrum-master 入口的变化、模板与看板的新位置（写明旧位置要改的人怎么办）、看板识别收尾待归档、署名两源、项目 Agent 与参谋入口的小改。版本号不动（仍是 0.6.3 的未发布候选）。其中第 11 行写了旧叫法（改名说明要让升级的人认得出改的是哪个旧名），已在 2.2 的放行清单登记。
  - **`plugin-dev:plugin-validator`（我派的，`model: haiku` 显式写）**：无阻塞问题。12 个入口与内核的 `description` 都是单行、≤1024（supporter 977、ideo-kernel 1023）；`hooks.json` 与 `commitments.sh` 正常；19 处 `../../template/…`、`../../board/…` 引用（`template/` 16 处、`board/` 3 处，涉及四个 `SKILL.md`、四份约定与 `overview.md`）全部解析；旧位置在插件里 0 处，只在 `scrum/` 里剩 2 处归档里的历史记述（已在放行清单）。它的四条非阻塞意见的处置：① `../../` 只在从技能文件夹解析时成立——这是各文件声明的基准，与插件里 `../<内核>/…` 的写法一致，不改；② `advisor.md` 的 `model: fable`——是 PO 在 Sprint 22 定的（「默认 Fable，可另选」），不在本期，不改；③ 行尾混用——仓库里的 blob 全是 LF（对 `supporter.md`、`developer.md`、一份模板核过，CR 数都是 0），不同只在 Windows 工作区（autocrlf），不用处理；④ `icon` 字段——原有，`--strict` 通过，没动。
  - **还差的一项证据**：H3 写的 DSH 实装验收条目（`/supporter` 出现、按 ideo → scrum 预载、读得到新位置的模板）要在最终提交上由 IDEO 秘书会话做，我这边没有 DSH 环境；Test 时有 Master 转来的原生事件证据就引用，没有就如实记「实装未验」，不拿静态检查顶替。
  - **通过线冻结**：2.2 的测试方法与通过线（含触发题面 v2、脚本和 grep 放行清单）以最后一个改动 2.2 的提交为准，提交哈希记在下面一条；此后到 Test 跑完之前，2.2 不再改，要改须经 Master。
- **通过线冻结于 `d72b0a6`（2026-11-22）**：这是最后一个改动 2.2 的提交，此后 2.2 不再改（要改须经 Master）。冻结内容：触发题面 v2 与判定脚本（`validation/trigger/`）、grep 的两条搜索命令与放行清单（旧路径 2 处、旧称法 14 处，逐处列出）、描述长度、DoD 逐条证据的做法、角色边界的对抗核对范围。冻结时已有的新证据（H1 提交后的各项自检、触发测试第 1 轮）已记在上面各条；第 5 章引用它们，Test 时对最终提交再跑一遍静态检查与两条 grep。

## 5. Test

<!-- Record the Developer’s tests, the independent review and any required Product Owner acceptance. Trace each Output Done standard and item criterion to new evidence, still-valid earlier evidence and why it holds, or a stated condition that did not arise and why. Keep missing evidence visible; record outcome signals separately and judge the Test against the pass lines set beforehand (sprint-log.md, convention 16). End with the Product Owner’s close or return decision (convention 24). -->
