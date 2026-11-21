> 按 Scrum Guide Expanded v2026.1 的 Product / Increment / Product Backlog artifact 框架定义。
> Product Owner: SeaPawn

# 一、Product

## 1.1 Product

| 承诺 | IDEO-Scrum：把 Design Thinking 与 Scrum Sprint 装进 Claude Code。 |
| --- | --- |

**IDEO-Scrum** 是 Claude Code marketplace 插件，也是可从仓库根目录安装的 DeepSeek Harness（DSH）bundle。两者直接共用同一套 Design Thinking 与 Scrum Sprint 方法论正文，通过角色入口和技能提供结构化的引导与流程框架。

**边界**：不做项目管理工具本身，不做 JIRA/Linear 集成，也不做团队协作平台——只提供方法论引导和流程框架。看板只读日志、不另存状态，由便宜的模型生成，不是项目管理工具。

## 1.2 Product Goal

| 承诺 | 产品化：从作者能用到大家都好用；看板一眼看清进度，文档讲清规矩；懂 Scrum 的人照着就能走完第一个冲刺。 |
| --- | --- |

**常态**：优化插件——用的时候攒下的反馈，随时开小冲刺改进插件；熟手照着就能走。它不是目标，是一直在做的事，由副线承担（PO 2026-11-13）。

**远景**：让 Claude Code 成为一个随身的设计思维与敏捷教练——有方法论需求的人打开 Claude Code 调用 IDEO-Scrum，就能获得结构化、忠于原文、可操作的方法论引导。

**换目标**（2026-11-13）：「优化现有插件」（2026-11-12 定）换成产品化——PO 定产品化更要紧，优化转为常态。更早的目标见 git 历史。

**本轮与之后**：插件的记忆机制（PBI-51）排入本轮；公开方法论分享（PBI-12）留待以后。六期的分工、范围与反馈去向见[六期总表](documents/sprint-roadmap.md)。

## 1.3 Definition of Done

### Definition of Outcome Done

| 度量 | 目标信号 |
| --- | --- |
| 一次会话走通方法论环节：完整引导（结构化、忠于原文） | 用户不反复追问 |
| 懂 Scrum 的陌生人走完第一个冲刺 | 体验测试（PBI-63）里不问作者、没有卡死的点 |

### Definition of Output Done

| 维度 | 标准 |
| --- | --- |
| 内容忠实 | 忠于源材料（SGEP / d.school / Sprint）；方法论设计部分（融合、solo+AI）标注来源与依据 |
| 署名 | 第三方摘录带 Source / License 两行，与 ATTRIBUTION.md 一致 |
| 可导航 | 从 SKILL.md 入口 ≤2 跳到达任意 reference |
| 无死链 | 所有 markdown 内部链接可解析，无 404 |
| 插件校验 | `claude plugin validate --strict plugins/ideo-scrum` 通过 |
| 描述长度 | 每个技能的 description 不超过 1024 字符 |
| DSH 分发 | `node --test scripts/check_dsh.mjs` 通过，共用的正文无需同步；分发改动另验实际安装与角色入口 |

# 二、架构

> 2.1 是谁，2.2 一张 Map。流程怎么走，见插件 scrum-kernel 的 `overview.md` 与各内核的 `conventions/`。

## 2.1 Stakeholders

> 召唤 Stakeholder 时报卡名，它按卡上的身份看、只看卡上写的东西；常驻会话另加「负责 / 不负责」两栏。派子代理做审阅、外部视角、测试、方案评议时，能用卡就用（PO 2026-11-08）。

| | 熟手 | 陌生人 | 读者 | PO 助手（常驻会话） |
| --- | --- | --- | --- | --- |
| 是谁 | 像作者这样的 solo 开发者：用 Claude Code 和本插件做自己的项目，熟悉这套流程 | 懂 Scrum、第一次装本插件的 solo 开发者：会用 Claude Code，没见过本仓库，也没有作者的记忆和配置 | 不装插件、只看公开分享（文章、网页、视频）的人：想学 solo + AI 怎么用 Scrum 与设计思维 | 常驻的 Claude Code 会话，替 PO 整理产品日志 |
| 要什么 | 流程跟着插件走，不用每次口述规矩；会话断了、压缩了能接上 | 装上就知道第一句说什么；插件自己的词有解释；很快进入干活 | 一套讲得清、能照着做的方法 | PO 或 Master 交代的改动说得清、有出处 |
| 怎么算满意 | 不用反复提醒 AI 规矩；冲刺照约定开、记、收 | 不问作者也能走完第一个冲刺 | 读完能在自己的项目里用起来 | 产品日志与实际一致；PO 不用自己动手整理 |
| 看得到什么 | 全部：插件、产品日志、冲刺日志 | 插件、README，和 README 链到的文档（体验测试只给这些；Sprint 20 Master 定，快速上手和词汇表放在 `docs/`） | 只有公开发布的内容 | 全部：插件、产品日志、冲刺日志 |
| 何时召唤 | Review 看增量；改约定前看顺不顺手 | 体验测试（PBI-63）；Review 涉及入口、说明、术语时 | 分享内容的草稿（PBI-12） | PO 或 Master 要登记 PBI、改状态与备注、要一份进度汇总时 |
| 负责 | — | — | — | 照 PO 或 Master 的话改产品日志；汇总进度给 PO |
| 不负责 | — | — | — | 排序、定目标、替 PO 拍板；改插件文件；审阅；没问过不删条目 |

## 2.2 架构

> 照 Make a Map 画：上面是人，下面是结局，中间是步骤；括号里是挂在这一步上的 PBI。

```mermaid
flowchart TD
    U["用户：懂 Scrum 的 solo 开发者（也是 PO）"]
    M["Master"]
    D["Developer"]
    G["Designer"]
    S["Stakeholder（含 PO 助手）"]
    U --> A["① 装插件，读 README 与快速上手（PBI-62、64）"]
    A --> A2["② 召唤角色进门（PBI-73、81）"]
    A2 --> B["③ 写产品日志：Product · 架构 · PBI（product-log）"]
    M --> B
    B --> C["④ Planning：Why → What（精化）→ How（计划，不是步骤）（sprint-log）"]
    B -- "某条 PBI 要设计" --> X0{"设计冲刺还是五模式？（ideo-log）"}
    X0 -- "设计冲刺" --> X["设计冲刺：五个阶段，各站在一个 IDEO 模式上（design-log）"]
    X0 -- "五模式" --> I["五模式：一两个方法就地用，或开 IDEO 日志（ideo-log）"]
    B -- "白纸：产品和 Product Goal 写不出来" --> X
    C -- "精化碰到难点" --> X0
    G --> X
    S --> X
    X -- "结论回流" --> B
    I -- "结论回流" --> B
    C --> P["⑤ PO 放行"]
    P --> W["⑥ 施工（sprint-log）"]
    D --> W
    W --> R["⑦ Test：测试 · 审阅 · PO 决定收官或回去"]
    R --> V["⑧ Review：冲刺日志、已结束的设计日志与 IDEO 日志归档 · 产品日志保鲜"]
    S --> V
    V --> T["⑨ Retro（PBI-69）"]
    T --> E["结局：Sprint Goal 达成，增量交付，Product Goal 向前一步（体验测试 PBI-63 从 ① 走到这里）"]
    C -. "日志头部" .-> K["看进度：看板卡片 · 目标常驻 hook（PBI-68）"]
    K -.-> U
```

# 三、Product Backlog Items

> 编号只是枚举序，不是优先级。行按三组排：主线（新功能）、副线（插件的规矩与讲规矩的文档）、以后；不加节（PO 2026-11-12、11-13）。备注只写决定和开放点，做法到做的时候写进冲刺日志（PO 2026-11-13）。七列写法见插件 scrum-kernel 的 `conventions/product-log.md` 第 10 条。

## 3.1 当前的 PBI

> 「规划：Sprint NN」表示已分配到该期，不表示已开工或已通过验收。新增项的规模由对应 Developer 在三方 Planning 时估量；F 编号对应[总表中的反馈对账](documents/sprint-roadmap.md#反馈对账)。

| 编号 | 标题 | 用户故事 | 架构定位 | 当前状态 | 规模 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| PBI-51 | 全插件审读与插件约定 Memory | 作为熟手，我想让审订过的插件约定有一处可按需调用的 Memory，以便既能遵守同一套规矩，又不用每次手动说明 | 插件：四内核与角色 | 规划：Sprint 26 | L | 做插件约定，不做全局知识库，不收项目 Retro。PO 与 Developer 通读整个插件，逐条审约定；PO 定方向，可交 AI 自动化实施。不配置则不自动加载，开启才自动，始终可手动调用；是否用 Skill／命令留给共作。来源 F01、F05、F16、Sprint 14 Stakeholder。 |
| PBI-84 | 署名：补齐 IDEO 五模式双源署名 | 作为熟手，我想要 IDEO 五模式摘录的来源与许可标注同时对上 2010 *Design Process Mini-Guide* 与 2018 *Bootleg*，以便插件的第三方署名与 `ATTRIBUTION.md` 逐项一致 | 插件：`ideo-kernel`（`IDEO-modes/`）与 `ATTRIBUTION.md` | 待选 | S | 来源：Sprint 21 Test 署名核查与 PO 2026-11-21 Review 拍板 ①。核实 `IDEO-modes/*.md` 含两路底本：`89eb3dd` 主体出自 Stanford d.school 2010 *Design Process Mini-Guide*（`ModeGuideBOOTCAMP2010L.pdf`，官方维基首页存档标 `CC BY-NC-SA 3.0 Unported`），`0d2629f` 的 38 处补料出自 2018 *Design Thinking Bootleg*（`CC BY-NC-SA 4.0`）；仓外取证归档见 `S:/IDEO-Scrum-Archives/sprint-21-design-board/h6-9558a0a/checks/attribution-audit/publisher-wiki/`。须将 `ATTRIBUTION.md` 第 3 节与 `IDEO-modes/*.md` 补齐双源 Source / License 标注，不改原书摘录正文。 |
| PBI-85 | 结构：模板、看板与记忆约定按用途收拢 | 作为熟手，我想在插件里按用途一眼找到模板、看板和记忆约定，以便引用和维护都井然有序 | 插件：目录结构 | 待选 | M | 来源：PO 2026-11-21 Sprint 22 Review 讨论。原话：「模板专门拉一起放在template里面去，hh，然后看板专门放到board里面去，然后井然有条之。」「我应该添加一个memory包呢，专门放记忆和约定呢。」范围：模板集中到 `template/`、看板相关集中到 `board/`、记忆与约定另立包（名称待定）。迁移类改动同一提交内全仓 grep 旧路径到零；技能之间按名字调用不受影响，但 SKILL.md 的相对引用、`board_check` 脚本与 fixtures、`package.json` 的 DSH 加包范围、`check_docs.py`／`check_dsh.mjs`、README 与 docs 链接须同步。迁完跑 `claude plugin validate --strict`、`check_dsh.mjs`、`check_docs.py`、`board_check selftest`。 |
| PBI-86 | 角色：PO 秘书与「秘书」说辞统一 | 作为 PO，我想有一个全辅助的秘书角色（更新看板、讲解机制等），并把 SM 与 Stakeholder 入口里「秘书」的说法换成统一的新称法，以便角色边界与称呼不混淆 | Map ②、③；插件：commands／agents／docs | 待选 | S～M | 来源：PO 2026-11-21 原话：「PO 加上秘书角色，全辅助角色--更新看板，介绍机制等等，并且更换sm得秘书说辞，变成其他说法，注意stakeholder也要变换说辞。这里还有一个点，也要计入PBI里面去，下午我们来做掉。」范围：新增 PO 秘书角色（全辅助，做更新看板、介绍机制等事务；非独立审阅者，不代 PO 决定）；统一 SM 命令／agent 与 stakeholder 命令／agent 中的「秘书」措辞，另起说法；保留 Review 召唤权与建造者边界。**删掉 `commands/stakeholder.md` 里原有的常驻「PO assistant」身份**（description、正文「PO assistant, not a second Scrum Master」段及 `skills/scrum-kernel/overview.md`、`docs/glossary.md` 等处相关说法一并清理或改写），由新的 PO 秘书承接。具体名称与落点待精化。 |
| PBI-87 | 调研：Stakeholder 角色是否可选自动登记为 Agent | 作为 PO，我想评估让 Stakeholder 角色按需或自动登记为项目 Agent 的可能，以便少手工操作又能守住边界 | 插件：`project-stakeholder`／产品日志 §2.1 | 待选 | S | 来源：PO 2026-11-21 原话：「你记得stakeholder角色是否自动登记agent，计入一个反馈PBI里面吧？还是一个PBI？我觉得可以一类可能反馈，因为我可能要测试一下，未来有可能放开去自动创建agent去，这个你要记得最好。」内容：先测手动登记的实际使用体验；若合适，再研究可选的批量／自动登记（默认关闭，逐张预览或规则化确认），不改变「PO 定角色、登记不改共享命令、Review 召唤权不变」的边界。按想法／反馈类登记，暂不排期。**未来需测试**：召唤 subagent 与 Workflow 时，是否会局限在已给的 agent 角色列表和产品日志 Stakeholder 表格之内；能否跳出这个约定，新建角色来做 subagent／Workflow。 |
| PBI-12 | 方法论分享——公开系列 | 作为读者，我想要一套公开的方法论分享（系列文章、网页或视频），讲清 solo + AI 怎么用 Scrum 和设计思维，以便不装插件也能学会、用到自己的项目里 | 产品之外：分享线（1.2「之后」） | 以后 | L | 决定：下一步做（PO 2026-11-13）；公开发布前过一遍授权（d.school 非商业）、经 PO 确认。素材：[ExpertNotes.md](documents/ExpertNotes.md)、`git show 3f43476:scrum/documents/five-stage-mapping.svg`（图里冲刺还是旧的三段，用前改成五个阶段；2026-11-14 PO 整理 documents 时从仓库删去）。来源：2026-10-24 PO 改为方法论分享 |

## 3.2 已完成 / 已关闭的 PBI

> 每个冲刺一行，列出条目编号，细节见出处与 git 历史（PO 2026-11-13：条目多了按条列读不完，偏离 product-log 第 17 条的每条一行）。Sprint 08 起，出处是 `scrum/documents/` 里归档的冲刺日志。

| 冲刺 | 条目 | 结果 | 出处 |
| --- | --- | --- | --- |
| 1.x（至 2026-08-30） | PBI-1～11 | 1.x 以 v1.0.2 收官；PBI-7～11 于 08-30 废弃 | git 历史；记忆档 sprint-01～05 |
| Sprint 06（2026-08-31～10-24，v2.0.0→v3.2.0） | PBI-13 角色体系（撤销）、14 设计阶段快原则、15 ideo 与设计冲刺融合（关闭）、16 双内核联动；17、18 并入 23，19 并入 20 | 双内核成形 | tag `v2.0.0`、`v3.1.0`；记忆档 sprint-06-dual-kernel-refactor |
| Sprint 07（2026-10-25，v4.0.0） | PBI-20 角色重定义、21 ideo-kernel 改名、22 角色命令自动加载内核、24 全文英文化 | 角色与内核成体系 | tag `sprint-07-done`；记忆档 sprint-07-roles-kernels |
| 精化（2026-11-07） | PBI-26 并入 30（11-08 删去判据）、27 Bot 工作方式研究 | 研究结论用于架构 v1 | [documents/PBI-27-bot-research.md](documents/PBI-27-bot-research.md) |
| Sprint 08（2026-11-08，v5.0.0） | PBI-28 设计日志约定、29 ideo-kernel 收窄、34 新建 design-kernel、36 角色命令先加载 ideo-kernel | 设计冲刺进插件 | [documents/sprint/sprint-08-design-kernel.md](documents/sprint/sprint-08-design-kernel.md) |
| Sprint 09（2026-11-08，v5.0.1） | PBI-38 设计日志模板只记产出 | — | [documents/sprint/sprint-09-design-template.md](documents/sprint/sprint-09-design-template.md) |
| Sprint 10（2026-11-08，v5.1.0） | PBI-23 冲刺日志约定、31 产品日志约定、32 角色命令接上约定、37 开设计与接手、39 总览约定 | 流程全部进插件 | [documents/sprint/sprint-10-conventions.md](documents/sprint/sprint-10-conventions.md) |
| Sprint 11（2026-11-09，v5.1.1） | PBI-41 约定按 PO 审阅修订 | — | [documents/sprint/sprint-11-conventions-review.md](documents/sprint/sprint-11-conventions-review.md) |
| Sprint 12（2026-11-09，v5.1.2） | PBI-42 总览挪到 scrum-kernel 根目录 | — | [documents/sprint/sprint-12-overview-to-root.md](documents/sprint/sprint-12-overview-to-root.md) |
| Sprint 13（2026-11-10，版本不动） | PBI-43 Codex 版 | Codex 包由脚本生成，并入 main | [documents/sprint/sprint-13-codex.md](documents/sprint/sprint-13-codex.md) |
| Sprint 14（2026-11-10，v5.2.0） | PBI-40 约定第一次集中修订、47 构思先发散后收敛、48 设计阶段对上五模式、49 约定精调、50 什么时候必须开设计 | 约定精调；白纸题没过线，登记 PBI-52 | [documents/sprint/sprint-14-conventions-tuning.md](documents/sprint/sprint-14-conventions-tuning.md) |
| Sprint 15（2026-11-12，版本不动） | PBI-55 自我反馈 | 反馈进全局记忆 | [documents/design/design-feedback-loop.md](documents/design/design-feedback-loop.md)、[documents/sprint/sprint-15-feedback-loop.md](documents/sprint/sprint-15-feedback-loop.md) |
| Sprint 16（2026-11-12，版本不动） | PBI-44 内核结构统一、57 加载分层 | 四个内核、按需加载 | [documents/sprint/sprint-16-kernel-structure.md](documents/sprint/sprint-16-kernel-structure.md) |
| Sprint 17（2026-11-13，v6.0.0） | PBI-54 产品日志与冲刺约定修订、58 设计约定修订、56 设计冲刺与五阶段法分清、53 Developer 在别的工具里、52 白纸入口 | 约定改顺、IDEO 日志；题 9、10 的缺口登记 PBI-59 | [documents/sprint/sprint-17-conventions-rewrite.md](documents/sprint/sprint-17-conventions-rewrite.md) |
| 产品日志整理（2026-11-13） | PBI-30 产品化、25 插件小修、46 Codex 小修、59 分界题的直接路径、45 流程命令、33 方法库改写 | 30 拆成 62 教学、63 体验测试、64 发布包装（看板、hook 另有 35、61）；61 拆出 66；25 关闭（③ 删，图标转 64）；46 关闭（Codex 不是核心）；59 删（普通时候不触发是好事，测试结果转为 65 的来源）；45 删（角色命令加约定已够，陌生人真在哪一步迷路再带证据登记）；33 删（与原文优先相反） | git 历史 |
| Sprint 18（2026-11-13，随 Sprint 19 发 v6.0.2） | PBI-66 日志头部、65 加载边界、60 角色说明 | 日志头部统一（承诺小表、Now、Waiting for PO、✓ 完成标记、决定前引用目标）；scrum、sprint、design 召唤才来；Master 在书面授权内代行、PO 助手身份写清。C 组 ideo 自然触发 3/9 没过，转 PBI-67（PO 定）；白纸项目的直接路径不再自动进设计冲刺——65 有意的结果，PBI-52 的直接路径行为就此改变，从角色命令进来照旧 | [documents/sprint/sprint-18-rules-first.md](documents/sprint/sprint-18-rules-first.md) |
| Sprint 19（2026-11-14，发 v6.0.2，连同 Sprint 18） | PBI-35 看板、61 目标常驻 hook | 看板第 1 版：scrum-kernel 的 `conventions/board.md` 与 `board-template.html`，单文件网页，产品卡、冲刺卡、设计卡，只读日志、不存状态，便宜的模型照约定生成；hook：开会话、恢复、压缩后各注一次承诺原文，承诺变了再注，可关，Codex 一并同步。频率测试：不装 hook 也过线，约定是主力、hook 补位。PO 看过真实看板，第 1 版认可，要强审重做，登记 PBI-68 | [documents/sprint/sprint-19-board-hook.md](documents/sprint/sprint-19-board-hook.md) |
| Sprint 20（2026-11-14，v6.0.3） | PBI-68 看板改版、64 发布包装、62 教学、63 体验测试、70 约定小修（七处） | 看板照设计的第 3 版重做成「固定页面 + 一块数据」，三档屏、离线、跟着系统的深浅色，检查脚本 `scripts/board_check/check.py`，便宜的模型能写，PO 看过说「非常好」；README、快速上手、词汇表、CHANGELOG、图标、升级与反馈；七处约定小修；体验测试照 63-a 跑：一组 3 次里两次走完，没有文档的卡点，陌生人一路装插件、开冲刺、收官、看看板 | [documents/sprint/sprint-20-presentable.md](documents/sprint/sprint-20-presentable.md)、[documents/design/design-board.md](documents/design/design-board.md) |
| Sprint 21（2026-11-21，版本不动，仍 v6.0.3） | PBI-74 看板重做设计冲刺卡、PBI-71 服务产品日志／已收尾的 IDEO 日志处理 | 设计卡重做为「目标原文／地图主线／独立方案区（故事板可选折叠、未选定不编造）」，产品卡与普通 Sprint 卡不变；独立 Sonnet 盲读 B 卡过线，6 组离线环境 42 卡次通过；IDEO 归属按 `For` 实际开放宿主与 `Now` 收尾态对齐 `board-log.md` 第 11、16 条与 `check.py`（13 份独立夹具＋5 负例＋79 项自测）。PO 接受增量与品味并拍板 ①（接受 2010 *Design Process Mini-Guide* 维基存档证据、另立 PBI-84 补双源署名）；「熟手」Review 无阻塞落差，3 条非阻塞建议并入 PBI-79「21+23 合流回验」备注 | [documents/sprint/sprint-21-design-board.md](documents/sprint/sprint-21-design-board.md) |
| Sprint 22（2026-11-21） | PBI-73 独立参谋、PBI-75 项目 Stakeholder 登记 | 参谋只读、手动发起，不传旧评议、不代 PO 决定；登记先预览同意，普通 Agent 与 Workflow 交互双入口各自按名命中。两处入口仅 Claude Code；实际模型三态仍待验证，登记写入职责的口径并入 PO 秘书议题，文档导航留 25 合流。 | [documents/sprint/sprint-22-project-agents.md](documents/sprint/sprint-22-project-agents.md) |
| Sprint 23（2026-11-21） | PBI-76 DoD、PBI-77 阶段放行、PBI-78 承诺、PBI-79 设计归档、PBI-69 Retro | DoD、阶段授权、承诺按原文、设计工作材料保全、Retro 分条记忆；按冻结口径 10/10，s10 定向复测 3/3。跨期核对及 Sprint 21 熟手提出的非阻塞留项见归档。 | [documents/sprint/sprint-23-log-rules.md](documents/sprint/sprint-23-log-rules.md) |
| Sprint 24（2026-11-21） | PBI-80 起草前读原文、PBI-81 顺序加载、PBI-82 内联原文、PBI-83 承诺 hook | 候选四题首稿前读全 12/12 对基线 0/12；四角色 4／3／3／2；Sprint Backlog 原文加载 3/3。两夹具 hook 常态 P50 降约 91%，已测承诺语义不变；未重测全流程 Outcome。 | [documents/sprint/sprint-24-loading-reliability.md](documents/sprint/sprint-24-loading-reliability.md) |
| Sprint 25（2026-11-21） | PBI-72 DSH 分发：验收与跨宿主维护说明 | 两个宿主的 0.6.3 新装、6.0.3 迁移与共用规则读取均在隔离环境取证；保留各自迁移步骤及实调角色边界。Claude 与 DSH 本地候选同为 0.6.3，尚未发布。 | [documents/sprint/sprint-25-dsh-docs.md](documents/sprint/sprint-25-dsh-docs.md) |
