# Sprint Backlog — Sprint 27 (wrap-up)

> Started: 2026-11-22 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `worktree-sprint-27-wrap-up` | Product Owner: SeaPawn | Scrum Master: IDEO # [master]-[main]-[manage sprint] | Developer: Sprint 27 Developer
> Now: Increment · 2026-11-22：Master 按授权放行 H1–H7（带两个条件，见第 3 章末行）；先做不依赖位置的 H4、H6，H1 的模板与看板位置等 DSH 探测。PO 最近一次决定：新角色定名 `supporter`，86 的 Q1–Q3 已定。
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

- **署名**：84 补齐双源 Source／License；摘录正文逐字不动，diff 只动 Source／License 行与 `ATTRIBUTION.md`。
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
| PBI-89 | 看板：收尾态识别与三条说明 | 作为熟手，我想让看板认得收尾待归档的写法，说明与模板占位前后一致，以便收尾中的设计和 IDEO 日志挂在对的地方 | 插件：scrum-kernel `conventions/board-log.md`、ideo-kernel `conventions/ideo-backlog-template.md`；`scripts/board_check/` | 待估 |
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
- Q2：沿用现边界——不排序、不决定、不审阅、不改插件文件，只传 PO 或 Master 已定的事。PO：「不做什么，我觉得你我觉得可以沿用，你看看有没有什么要修改的，然后也可以修改一下」。Master：沿用，不改。定位按 SGEP 的 Supporter（a Stakeholder type）立，见 Q1；PO：「它其实本质上也是也算是 stakeholder 的一种」。
- Q3：PO：「我觉得应该叫就是 master 吧，就是说有权力的 master，我觉得你想想呢」。Master 的读法：`scrum-master` 入口去掉「秘书」味，看板、汇总、传话这类杂活交给 supporter；SM 写成有权的 Master：守流程、审、在书面授权内代 PO 定。Scrum Guide 原文不动；排序、目标等产品决定仍归 PO。
- Q4：便宜模型写不写进入口由 Developer 定；PO 要整个角色「比较漂亮一点，比较优雅一点」，「不写也行」。
- Q5：跟 Stakeholder 一样，ideo → scrum（PO：「就跟 stakeholder 一样就行」）。
- Q6：DSH 实装与角色入口的测试可交现有的 IDEO 秘书会话（`IDEO # [secretary]-[main]-[support PO]`）（PO：「DSA 是可以让他去测试」，DSA 即 DSH），由 Master 转交。

- 已知改动处：`commands/stakeholder.md`（description、第 15 与 34 行）、`commands/scrum-master.md` 的 description、`overview.md` 约定 8 的表与约定 14、`docs/glossary.md`、`claude-skills/project-stakeholder/SKILL.md`、`scripts/check_docs.py` 的术语表；其余由 Developer 全仓再查。
- 验收：新入口能叫出、按定的顺序加载内核，Claude Code 与 DSH 各验一次；插件与 docs 里旧的「PO assistant／PO 助手」grep 为零（归档的历史日志除外），新称法前后一致；Review 召唤权与建造者边界不变；改过的描述 ≤1024，触发测试不比改前差。

**PBI-85 · 模板与看板**

- 视角（照抄）：作为熟手，我想在插件里按用途一眼找到模板和看板，以便引用和维护都井然有序
- HMW：我们怎样让找模板、找看板的人第一眼就落对地方？
- 要点：模板放每个内核各自的 `template/`，还是插件一处共用——Developer 提，Master 定，须顾到技能间按名字调用、SKILL.md 的相对引用和 `package.json` 的加包范围；看板相关（`board-log.md`、`scrum-board-template.html`）进 `board/`，其中的规矩由 26 期再转进 Memory；同一提交内全仓 grep 旧路径到零（项目规矩）；本条排第一项，先合 main（总表「续」）。
- 验收：模板都在定好的位置，看板相关都在 `board/`；旧路径全仓 grep 为零（归档的历史日志除外）；`validate --strict`、`check_dsh`、`check_docs.py`、`board_check selftest` 通过；DSH 实装后角色入口读得到模板。

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
- 验收：五个文件头与 `ATTRIBUTION.md` 第 3 节逐项对上两源；diff 只动 Source／License 行与 `ATTRIBUTION.md`；许可有可达链接或存档出处（仓外取证路径见 PBI-84 备注）。

**测试**（第 13 条；How 定稿前补齐通过线，Test 前提交，提交后不改）

- 要新证据：`validate --strict`、`check_dsh`（含新角色）、`check_docs.py`、`board_check selftest`、旧路径与旧称法 grep、摘录 diff、描述长度、触发测试（与改前同日对照）、新角色入口加载（Claude Code、DSH）。
- 沿用旧证据：无，本期动到的检查都重跑。
- Outcome：不设本期必须的信号；Review 时 Master 召「熟手」看入口与说明，意见记为信号。

**通过线**（Developer 拟，2026-11-22，Master 审；Test 前提交，提交后不改。正式跑之前先冒烟一次，冒烟不计数）：

- **静态**：`claude plugin validate --strict plugins/ideo-scrum`、`node --test scripts/check_dsh.mjs`（覆盖五个角色）、`python -X utf8 -I scripts/check_docs.py`（含 `--selftest`）、`python -X utf8 -I scripts/board_check/check.py selftest` 全过；`npm pack --dry-run --json --ignore-scripts` 的清单含新的 `template/`、`board/`（若 Master 定退回各内核自己的 `template/`，则含各内核的 `template/`）与 `commands/supporter.md`；新命令与改过 frontmatter 的入口派 `plugin-dev:plugin-validator`（Haiku）无阻塞问题。
- **grep 为零**：旧模板与看板路径（`conventions/` 下的 `*-backlog-template.md`、`scrum-board-template.html`、`board-log.md`）、旧称法（`PO assistant`、`PO 助手`、「常驻的助手」「standing assistant」）在 `plugins/`、`dsh/`、`docs/`、`README*`、`scripts/`、`package.json`、`.gitignore` 内为零；`scrum/` 下的归档与在办日志、产品日志（Q7 由 Master 收官时改）和 `CHANGELOG.md` 的历史条目不在范围内。
- **84**：对基线提交 `1145382` 逐文件比，五个 `IDEO-modes/*.md` 去掉头部引注行后的正文逐字相同（脚本比）；头与 `ATTRIBUTION.md` 第 3 节逐项对上两源，许可有可达链接或存档出处。
- **描述长度**：改过与新增的 `description` 逐条用脚本量，全部 ≤1024，并在第 5 章写出数值。
- **触发**（同日、同环境、同一脚本；改前臂取自基线提交的 `git archive`，改后臂取冲刺分支；题不带引导词）：三组各 3 题、每题 3 次，每臂 27 次——A 杂活（更新看板、汇总进度、讲解机制）、B 外部视角（以用户或利益相关者身份看原型）、C Master 事务（开 Sprint 计划、查阻碍）。行为栏与内容栏分列。过线：A 组改后臂加载 `supporter` ≥6/9；B、C 两组改后臂命中数各 ≥ 改前臂（Master 2026-11-22 改，依据 AGENTS.md「改了描述就重跑触发测试，结果不能比改前差」；不降线）；某组只差一次未过的，该组两臂同补一轮（每题再 3 次），按合并计数重判一次，补跑规则现在写定，不算挑样本；混用——B 组中 `supporter` 被加载 ≤1 次，A 组中 `stakeholder` 被加载 ≤1 次。技术失败按手册补足有效试次，不挑样本。
- **加载**：Claude Code 无头，`/ideo-scrum:supporter` 的 Skill 调用顺序为 ideo-kernel → scrum-kernel，3/3，且不加载 sprint-kernel、design-kernel。DSH：交 IDEO 秘书会话（Master 转），在 Standard 会话看到 `/supporter`、按 ideo → scrum 预载、读得到新位置的模板；证据取原生事件，不取模型复述（手册第 28 条）。
- **89**：`selftest` 新增正例（`Test: Concluded — awaiting archive`；带阶段前缀、无「已」的 `收官 · …`）与负例（进行中写法里出现 closed、待收官）各至少 1 个，原有场景不变，全过；三态合成日志（开放、`Concluded — awaiting archive`、迁出活动路径）重跑通过。
- **90**：九条各有结论与理由；做了的各有 diff；中英对照页 `check_docs.py` 通过。
- **角色边界**（Master 2026-11-22 加）：Test 里派一个全新子代理（Master 派，显式写 `model`），对 `supporter` 入口、`overview.md` 约定 8、14 与 `stakeholder` 入口的边界文字做一次对抗核对：无与「不排序、不决定、不审阅、不改插件文件」或 Review 召唤权相冲的句子；问题逐条写处置。

**精化决定**（2026-11-22）：PO 定了 Q1–Q3，认可其余：「剩下的我觉得问题不大了」。Developer 同步（第 6 步：提出疑问、逐点复述；PO：「其实不叫审核，应该叫同步」）无疑问即结束精化、进 How，Master 按书面授权确认；PO：「差不多了就可以进入，让27就是同步给冲刺27的 developer，然后进入 How 阶段。」施工放行由 Master 审过 How 后按授权给。提交由 Developer 自行做，不推送（PO：「提交的话就 developer 那边做就行了，你就不用管了」）。

## 3. How

<!-- The Developer writes this chapter as a plan for making the selected items, short and not in detail (sprint-log.md, convention 7): the work items in order, each with its output and how to tell it is done; the key choices and why; the risks and open points. The last line is the go-ahead (sprint-log.md, convention 8). -->

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| H1 | 85 迁路径（第一项，M） | 四份日志模板集中到插件根的 `template/`，`board-log.md` 与看板模板进 `board/`（`git mv`，文件名不变）；`SKILL.md`、各 `conventions/`、`overview.md`、`check.py`／`prepare_review.py`／`stranger_test/driver.py` 里的路径常量、docs、README 中英、`.gitignore` 注释、`package.json` 的 `files` 同一提交改全 | 旧路径全仓 grep 为零；`validate --strict`、`check_dsh`、`check_docs.py`、`board_check selftest` 通过；`npm pack --dry-run` 含新目录 |
| H2 | 86 supporter 入口与改称（M） | 新 `commands/supporter.md`；`stakeholder`、`scrum-master` 两入口改称；`overview.md` 约定 8、14，glossary（中英一对）、README 中英、`check_docs.py` 术语表、`project-stakeholder` 里的旧说法同步；SGEP 引文在 `ATTRIBUTION.md` 登记 | ✓ 2026-11-22 插件、docs、README、脚本里旧称法 grep 为零；改过与新增的描述 ≤1024（脚本量）；Review 召唤权与建造者边界的句子都还在 |
| H3 | 86 的 DSH 部分（S） | `dsh/index.js` 角色表、`dsh/locale/en.json`、`zh.json`、`check_dsh.mjs`、`docs/maintaining*.md` 加 supporter；2.2 的 DSH 验收条目交 Master 转 IDEO 秘书会话 | ✓ 2026-11-22 `check_dsh` 通过且覆盖五个角色；`npm pack --dry-run` 含 `commands/supporter.md`；验收条目已交 Master |
| H4 | 84 署名（S） | 五个 `IDEO-modes/*.md` 的头与 `ATTRIBUTION.md` 第 3 节补成两源，正文不动 | ✓ 2026-11-22 对基线逐文件比，正文逐字相同；头与第 3 节逐项对上；许可有链接或存档出处 |
| H5 | 89 看板收尾态（S） | `check.py` 修三处并加正负例；`board/board-log.md` 第 12 条补一句；`template/ideo-backlog-template.md` 的 `For` 占位补提 `DesignBacklog.md` | `board_check selftest` 全过且含新增正负例；三态合成日志重跑通过；条文与脚本一致 |
| H6 | 90 九条（S） | 做 ①②④⑤⑦⑧⑨，⑥ 在快速上手补一行，③ 不做；只动 `second-opinion`、`project-stakeholder`、`advisor.md` 的正文与 `docs/project-agents*.md`、`quick-start*.md`，不动任何 description | ✓ 2026-11-22 九条各有结论与理由；做了的有 diff；`check_docs.py` 通过 |
| H7 | 收口 | `CHANGELOG.md` 的 Unreleased 补记；全仓 grep 复核；`validate --strict` 后派 `plugin-dev:plugin-validator`（Haiku，新命令与 frontmatter 改动属结构变化）；2.2 通过线提交冻结；报 Master 请放行 Test | 上述检查通过；通过线已提交；Master 审过 Increment |

**Key choices**

- **模板与看板放插件根的 `template/`、`board/`（Master 倾向此案，审 How 时定；下面三点有一点走不通，就退回各内核自己的 `skills/<内核>/template/`，看板放 `skills/scrum-kernel/board/`）**：用户故事是「按用途一眼找到」，PO 原话是「模板专门拉一起放在 template 里面」，一处共用才拉得到一起；26 的记忆与约定包也会在同级。三点：
  - ① **相对路径怎么写**：照现在的做法，按「引用它的技能文件夹」写，统一为 `../../template/<文件>`、`../../board/<文件>`——不裸写文件名，也不因引用者在 `SKILL.md` 还是 `conventions/` 而变（约定文件已声明 `../` 相对技能文件夹）。与 AGENTS.md「引用别的技能的文件写 `../<kernel>/file.md`」同一个精神，只是多上一级。
  - ② **`package.json` 的 `files` 要加**：加 `plugins/ideo-scrum/template/`、`plugins/ideo-scrum/board/`。现有清单只含 `commands/`、`skills/`、`icon.png`，不加则 DSH 包里没有模板。Claude Code 是整个插件文件夹进缓存，不用另加。
  - ③ **DSH 读得到吗**：设计上可以——`roleRouting` 让模型按「点名该资源的内核」的绝对路径读，`../../template/…` 拼出来就是包内绝对路径；`check_dsh.mjs` 可静态核每条 `../../template`、`../../board` 引用都落在打包清单里。但 DSH 的 `read` 工具读不读得了 `skills/` 之外的包内路径，本会话验证不了（现有证据只到跨内核，即 `skills/` 之内）。建议放行前让 IDEO 秘书会话探一次：在 DSH Standard 会话里读 `<内核目录>/../../commands/developer.md`（包内、`skills/` 之外）；读不到就退回。
  - 两个方案改的地方一样，只差路径前缀。
- **86 的定位：Supporter 是 SGEP 里的一种 Stakeholder，只取「照请求做事」这一面**，不取 change agent、guiding coalition（按作者约定标明）。入口与 `stakeholder` 分开：`stakeholder` 给外部视角（拿角色卡的新子代理），`supporter` 做常驻杂活；两条描述各写明「不管什么」，防模型混用，触发测试专门盯这条。`overview.md` 约定 8 的表加 Supporter 一行（标「a Stakeholder type」），约定 14 把「Stakeholder 会话带工作身份」改成 supporter；规则本身不改。SGEP 引文照抄，署名在 `ATTRIBUTION.md` 登记，命令文件不加头两行。
- **中文叫法「秘书」（Master 2026-11-22 定，不转 PO）**：这是 PO 的口头用词，也是 Sprint Goal 用的词；英文入口 `supporter`；glossary 写「Supporter ｜ 秘书」，释义里注一句只取 SGEP Supporter「照请求做事」这一面。备选「支持者」是直译，读着像拉拉队，不像干杂活的。
- **Q4：不在入口钉 `model`，也不写建议**：杂活多用便宜模型，但 PO 也会让它讲机制，钉死会误伤；看板约定本来就写了「便宜的模型就能写」。
- **`scrum-master` 只改描述与 Identity 一段**：杂活去向改成 supporter；明写有权——守流程、审、在书面授权内代 PO 定；Scrum Guide 摘录不动。
- **89 三条建议都做，脚本只放宽不收紧**：每处配正例与负例；收官态写法以约定为准，约定没说的不判错。
- **90：做 ①②④⑤⑦⑧⑨，⑥ 补一行，③ 不做**：七条各是一两句正文或一个 frontmatter 提示，且不碰 description，不引发触发测试。⑥ 查得 README 已链（`README.md:167`、`README.zh-CN.md:167`），快速上手没链，补一行。③ 不做：改召唤示例要 Review 批准加实机验证，现有示例准确，等 PO 体验后再定。
- **提交分开**：H1 一个提交（grep 到零）；H2、H3、H4、H5、H6、H7 各自提交；改号不在本期。

**Risks and open points**

- 触发测试有随机性：便宜模型、每臂 27 次；B、C 组的线是「≥ 改前臂」，不留余量（Master 定），只差一次的组两臂同补一轮，已在 2.2 写定；两臂同日同环境跑，技术失败补足不挑样本。
- 与 26 的接口：26 稍后会改所有角色入口（含 supporter）的加载方式；`supporter.md` 与其余入口保持同一版式，让 26 的改动可以机械地做。27 合入 main 后，Master 把改动文件与规矩列给 26。
- 约定改在冲刺内（项目规矩是约定攒着集中改）：`overview.md` 约定 8、14，`board-log.md` 第 12 条，`ideo-backlog-template.md` 的 `For` 占位，都是 PO 交给本期的条目所需；改动限于一行表项、一句替换和一句补明，不改规则本身。Master 已判不算大改约定：Master 审，Test 里加全新子代理对角色边界文字做对抗核对，不走 PO 强审。
- 版本号不动（仍是未发布的 0.6.3 候选），`CHANGELOG.md` 的 Unreleased 补记；要给新角色升号，另议，单独提交。
- DSH 实装验收靠 IDEO 秘书会话，由 Master 转交；转不动时只有 `check_dsh` 与打包核对这些静态证据，Test 里如实记「实装未验」。
- 90 的「不做 ③」要 Master 认可：PBI-90 的验收是「九条每条有结论与理由」，不做也算结论。
- 产品日志里的「PO 助手」卡与图（Q7）归 Master 收官时改，不在本期 grep 范围内。

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
- **并行约束（总表「续」）**：27 先合 main，26 再动插件文件；85 的迁路径排第一项；27 碰的范围——模板与看板（85、89）、角色入口与「PO assistant」说法（86）、`IDEO-modes/` 与 `ATTRIBUTION.md`（84）、`project-stakeholder` 与参谋入口（90）——26 暂不动。
- **同步与 How（2026-11-22）**：Master 通知第 1、2 章已定，86 改名 `supporter`（Q1、Q2、Q6 已改）。Developer 重读磁盘日志，无疑问，逐点复述五条发 Master；写第 3 章 How（H1–H7），并按 2.2 的要求补了通过线（Developer 拟，Master 审）。提交由 Developer 在本分支自行做，不推送（PO：「提交的话就 developer 那边做就行了」，经 Master 转述）。
- **触点盘点（写 How 时查得；施工时再全仓 grep 复核）**：
  - 85：四个 `SKILL.md`；`sprint-log.md`、`design-log.md`、`product-log.md`、`board-log.md`、`overview.md`；`scripts/board_check/check.py`（`TEMPLATE`）、`prepare_review.py`、`scripts/stranger_test/driver.py`；`docs/glossary.md`、`docs/maintaining*.md`、`README*.md`；`.gitignore` 的注释；`package.json` 的 `files`。`CHANGELOG.md` 里的旧路径是历史条目，不改。
  - 86：`commands/stakeholder.md` 与 `scrum-master.md` 的 description（「PO assistant」写在第 2 行，现约 860、730 字符）；`overview.md` 约定 8、14；`docs/glossary.md`；`check_docs.py` 的 `GLOSSARY_TERMS`；`claude-skills/project-stakeholder/SKILL.md` 第 67、81 行；`README*.md` 第 93、151 行；`dsh/index.js` 与 `scripts/check_dsh.mjs` 的 `roles`；`dsh/locale/*.json`；`docs/maintaining*.md`。`package.json` 的 `files` 含 `commands/`、`skills/`，不含 `claude-skills/`、`agents/`（这两处只给 Claude Code）。
- **Master 对三问的答复（2026-11-22，Master 按授权）**：① 模板放置倾向插件根一处共用 `template/`（合 PO 原话），How 须写清相对路径、`files`、DSH 读取三点，一点走不通就退回各内核自己的 `template/`；② 中文叫法用「秘书」（PO 自己的叫法，不转 PO），glossary 写 Supporter｜秘书，再注一句只取 SGEP Supporter「照请求做事」这一面；③ `overview.md` 约定 8、14 与 `board-log.md` 第 12 条的改动是新角色带来的称法与分工更新，不算大改约定：Master 审，Test 里再加一个全新子代理对角色边界文字做对抗核对，不用 PO 强审。90 不做 ③、Q4 入口不钉 `model`，Master 都同意。
- **接手点**：施工已放行（第 3 章末行：H1–H7，本分支提交，不推送、不改版本号、不发版；Test 另等放行）。H4、H6 不依赖位置，先做；H1，以及依赖它的 H5、H2 里引用看板约定的一处，等 Master 转来的 DSH 探测结果——读得到 `skills/` 之外的包内路径就用插件根的 `template/`、`board/`，读不到就退回各内核自己的 `template/`、看板放 `skills/scrum-kernel/board/`。做完一项，在第 3 章该行 Done when 前加 `✓ <日期>`，并在这里记改了什么、为什么。
- **Master 放行 How（2026-11-22）**：条件 ① B、C 组触发通过线改成「≥ 改前臂」，依据 AGENTS.md「改了描述就重跑触发测试，结果不能比改前差」，担心噪声就加次数、不降线——已改 2.2 与 Risks，只差一次的组两臂同补一轮的规则现在写定；条件 ② H1 位置等探测。A 组 ≥6/9 与两条混用线照旧。
- **顺序调整（2026-11-22，Developer 在 How 授权的范围内调，Master 知悉）**：How 表里 H1 排第一，实际先做 H4、H6，再做 H2、H3、H5，H1 放到最后。原因：H1 的位置（插件根的 `template/`、`board/`，还是各内核自己的）要等 DSH 探测结果，而 H4、H6、H2、H3、H5 都不依赖位置。H2、H3、H5 在原位置改内容，H1 再 `git mv`，文字跟着走；这些新写的文字里不写会变的路径。H1 收尾的全仓 grep 要把 H2、H3、H5 新写的文字也算进去（Master 要求）。第 3 章的行序不改，保留原计划，调整记在这里。
- **H4 · 84 署名（2026-11-22）**：五个 `IDEO-modes/*.md` 的头三行统一改成两源——2010 *Design Process Mini-Guide* 为底本（CC BY-NC-SA 3.0 Unported），2018 *Design Thinking Bootleg* 为补料（CC BY-NC-SA 4.0）；各带可达链接（两份 CC 许可全文、2010 PDF 的 Wayback 存档、Stanford 页）。正文没动：对基线 `git diff --numstat` 每个文件 3 增 3 删，hunk 只在 `@@ -3,3 +3,3 @@`。`ATTRIBUTION.md` 第 3 节拆成 3.1（2010 底本：许可依据是 d.school「Design Resources」维基首页的声明，写明声明在首页、原站已下线、未另取书面确认，附两条存档链接）和 3.2（2018 补料与方法库，加五模式补料对应表：8／6／9／7／8 块，共 38，对应 2018 PDF 第 3–12 页）；NonCommercial 提示改成「两份许可都含」。Test 的头与另四个相同（PBI 要求五个都补双源），2018 补料没有保留独有表述写在 3.2 的表里。另改 `README.md`、`README.zh-CN.md` 授权表的 d.school 一行，免得与 `ATTRIBUTION.md` 不一致（PBI 原文没列，按「改一条规矩先找它的其他说法」顺手做）。证据：Wayback 首页与 PDF、Stanford 页、CC 3.0 许可全文四个链接实测均 200（2026-11-22）；仓外取证在 `S:/IDEO-Scrum-Archives/sprint-21-design-board/h6-9558a0a/checks/attribution-audit/`；`check_docs.py` 无错误。
- **H2 · 86 supporter 入口与改称（2026-11-22）**：
  - **新入口** `commands/supporter.md`：版式与 `stakeholder.md` 相同（加载 ideo → scrum，DSH 一句，子代理一句，约定一句）；Identity 引 SGEP 原文短语「a specific Stakeholder type」「doing what is requested」「participate when and where needed or as requested」，并用斜体注明作者取舍——只取「照请求做事」一面，不取 change agent、guiding coalition；「做什么」五条（看板、整理日志与汇总、传已定的事、讲解机制、其他杂活）；Code of Conduct 九条，沿用旧边界（不排序、不决定、不审阅、不改插件文件，范围、条目与放行走 Master），另写明「不是外部视角」（外部视角由新子代理拿角色卡给，Review 只由 PO 或 Master 召唤）、「源码归 Developer」。不钉 `model`（Q4）。文件头无两行署名，署名在 `ATTRIBUTION.md` 第 2 节加了一行本仓库位置，并把修改说明里的角色命令清单加上 supporter。
  - **`stakeholder.md`**：description 删去 PO assistant 的全部说法（860 → 599 字符），保留判别词「outside view」「fresh subagent given a role card」「Any role may summon…never the builder」「rather than claiming fresh eyes」「Feedback goes to the PO」，末句指向 `supporter`；Identity 改成只给外部视角；删「PO assistant, not a second Scrum Master」一条与另三处牵连的半句；Review 召唤权与建造者边界的句子都在。
  - **`scrum-master.md`**：description 杂活去向改为 Supporter（729 → 718）；Identity 后加一段「你是 Master，不是秘书」：守流程、审、在书面授权内代 PO 定，优先级、目标等价值决定仍归 PO，没有决定的杂活交 Supporter；第 57 条的「standing Stakeholder session」改指 Supporter。Scrum Guide 摘录未动。
  - **`overview.md`**：约定 8 的角色表 Stakeholder 一行只剩外部视角，新增 Supporter 一行（注明 SGEP 里是 Stakeholder 的一种，加载 ideo → scrum）；约定 14 改为「交给常驻的 Supporter」，边界一句不变、外部视角指 `stakeholder`。约定 15 里的「the author's assistant」指作者的 AI 助手，不是这个角色，不改。
  - **其余同步**：`board-log.md` 第 3 条「standing helper session」→ Supporter；`project-stakeholder/SKILL.md` 两处；`docs/glossary.md`（Stakeholder 一行去掉杂务，「PO assistant｜PO 助手」换成「Supporter｜秘书」，释义里注明只取 SGEP「照请求做事」这一面，Master 定）；`scripts/check_docs.py` 的术语表；README 中英（角色清单、斜杠命令块与 DSH 块各加一行、看板一段、文件表「五个角色」）。
  - **没动、留给后面**：DSH 角色表、locale 与 `check_dsh.mjs`、`docs/maintaining*.md`、`docs/project-agents*.md` 的「四个角色命令」（H3）；产品日志 §2.1 的「PO 助手」卡与图（Q7，Master 收官时改）；`CHANGELOG.md`（H7）。`maintaining*.md` 第 29 行是 2026-11-20／21 对旧 0.6.3 候选的迁移实测（「四个角色」），属历史证据，H3 时加限定说明、不改写，并报 Master。
  - **检查**：全仓旧称法 grep（`PO assistant`、`PO 助手`、`standing assistant`、`standing helper`、`standing Stakeholder`、「常驻的助手」「助手会话」）在 `plugins/`、`dsh/`、`docs/`、`README*`、`scripts/`、`package.json`、`ATTRIBUTION.md` 内无命中；描述长度 718／599／681，皆 ≤1024；`check_docs.py`（195 条链接）与 `--selftest`（17 例）通过；`claude plugin validate --strict` 通过，已列出 `ideo-scrum:supporter`。触发测试要等描述定稿后与改前同日对照，放在 H7。
- **H3 · 86 的 DSH 部分（2026-11-22）**：`dsh/index.js` 与 `scripts/check_dsh.mjs` 的角色表各加 `supporter`（排在 `stakeholder` 之后，`check_dsh` 比对注册顺序）；`dsh/locale/en.json`、`zh.json` 的描述加 `/supporter`（`check_dsh` 要求描述含每个角色的斜杠名）；`docs/maintaining*.md` 第 15 行改为「四个内核与五个用户可调用角色」并列出 `/supporter`；`docs/project-agents*.md` 的「四个角色命令」改为五个。`maintaining*.md` 第 29 行是 2026-11-20 对旧 0.6.3 候选的迁移实测，只在「四个角色」前加「当时的」（英文 `of that date`），不改写证据；这一条按 Developer 的判断做，请 Master 审时留意。检查：`node --test scripts/check_dsh.mjs` 7／7 通过（含注册顺序与五个角色预载）；`check_docs.py` 无错误；`npm pack --dry-run --json --ignore-scripts` 共 101 个文件，含 `commands/supporter.md`。
  - **DSH 验收条目（交 Master 转 IDEO 秘书会话；隔离环境，不碰日常实例；证据取原生事件，不取模型复述，手册第 28 条；链接本分支的 `plugins/ideo-scrum`，记下提交号）**：① 开 Standard 会话，技能建议里有 `/supporter`，其余四个角色仍在；② 输入 `/supporter` 加一句杂活（例如汇总冲刺走到哪），会话日志里 `user/message` 的 `skill-invocation` 来源是 supporter，原生角色内容里按 IDEO → Scrum 预载，没有 sprint-kernel、design-kernel 的预载；③ 同会话从某个内核目录读 `../../commands/developer.md`（包内、`skills/` 之外的路径），回报读得到还是读不到——这是 H1 的位置探测；④ 记 DSH 版本、链接路径、会话日志位置，原始记录放仓外。
- **H6 · 90 九条（2026-11-22）**：逐条结论，涉及 `second-opinion`、`project-stakeholder` 两份 `SKILL.md`、`advisor.md`、`docs/project-agents*.md`、`docs/quick-start*.md`，没碰任何 description。
  - ① 做：参数写法定为 `model: <name>`——`second-opinion` 的 `argument-hint` 加 `| model: <optional>`，§1 加第四项，§3 写明作为 `Agent` 调用的 `model` 参数（例 `model: "opus"`）；docs 写「在请求后面加 `| model: opus`」。
  - ② 做：`project-stakeholder` §1 指向 §3；§3 加「没有何时召唤栏」的路径——只展示定义文件、不加引用，用户选「不带引用写文件」或「停下等 PO 加栏」，不自己改表。
  - ③ **不做**：召唤示例（docs 里的 `Agent, subagent_type: ...`）改成 @-mention 或自然语言，按 Sprint 22 的来源条件要走 Review 批准并实机验证；现有示例准确、能用，成本高于收益，等 PO 体验后再定（Master 已认可）。
  - ④ 做：`project-stakeholder` 加 `argument-hint`（角色卡名）。
  - ⑤ 做：`project-stakeholder` §4 加「宿主自己的提示」一段（`.claude/` 写入另有权限确认，不替代用户对预览的 yes）；docs 第 2 步加一句，中英同改。
  - ⑥ 做一行：README 已挂（`README.md:167`、`README.zh-CN.md:167`），快速上手没挂——在「迷路了怎么办」补一条，中英同改。
  - ⑦ 做：我的读法——「两入口／三条列项」指 docs「按名召唤」的三条：开头写「同一份文件供两个入口使用」，第三条（临时看一眼）却不用文件。改成「供前两种用法使用，第三种不需要文件」，中英同改。归档里只有一句话、没有明细，这是我的读法；Master 若另有所指，请说，我再改。
  - ⑧ 做：`second-opinion` §2 标题改「Keep the brief clean」，docs 的「The context is clean」改「The brief is clean」（中文「交给参谋的说明是干净的」），`advisor.md` 的「a context that carries none of the earlier discussion」改「a fresh context that was given only the brief」。
  - ⑨ 做：`second-opinion` §3 与 docs 写明 `fable` 要账号有权限，用不了时说明并问换哪个模型，不自己选。
  - 检查：`check_docs.py` 无错误（195 条链接）；`claude plugin validate --strict` 通过；description 没动，所以不触发触发测试；frontmatter 有两处加了 `argument-hint`，H7 的 `plugin-validator` 一并看。

- **Master 写第 1、2 章（2026-11-22）**：PO：「你把 S7也先写出来吧。然后这两个我一起审掉。」Developer 原计划的头部与 1.2 改动由 Master 代写；提交等 PO 审后再定。

## 5. Test

<!-- Record the Developer’s tests, the independent review and any required Product Owner acceptance. Trace each Output Done standard and item criterion to new evidence, still-valid earlier evidence and why it holds, or a stated condition that did not arise and why. Keep missing evidence visible; record outcome signals separately and judge the Test against the pass lines set beforehand (sprint-log.md, convention 16). End with the Product Owner’s close or return decision (convention 24). -->
