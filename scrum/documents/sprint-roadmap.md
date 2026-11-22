# Sprint 21–26：使用反馈收齐

2026-11-19，PO：SeaPawn。方向：把前期使用积累的反馈和待做的插件条目落实到产品里，做成一版经过实际使用打磨的插件。现有 Product Goal 不变；这里确定六期的分工，不代替每期自己的 Sprint Goal、How 或施工放行。PBI 的故事、状态与规模只在[产品日志](../ProductBacklog.md)维护。

## 六期分工

**六个 Sprint，各一名 Developer。** 按共同交付结果分，不按“凡有品味要求就交给 PO 施工”分。先建 21 的 Developer（PO 指定 Sonnet、与 Master 相同的思考强度、Ultracode），其他 Developer 逐个接入，已接入的各期并行准备 Planning，不必等上一期定完。PO、Master 与各期 Developer 分别确认本期目标、范围和 How；六期先把 Planning 备齐，再由 PO 一期一期放行施工。已分别放行的工作可在独立工作树并行，互不等待 Memory。

| Sprint · 文件夹／分支短名 | PBI | 做成什么；哪些不在范围内 | 三方要谈清、验清的事 |
| --- | --- | --- | --- |
| **21 · `sprint-21-design-board`** | 74、71 | 只重做设计冲刺卡。第一块只放设计目标；第二块取设计日志的地图主线，借用产品卡的简略路线表达；第三块独立展示选定方案，是本期重点。产品卡与普通 Sprint 卡不改版。 | AI Developer 提方案，Master 跟进。核对设计日志 1.2（目标）、2.1（地图）、3.1（方案）与可选的 3.2（故事板）。没选方案或没画故事板时仍有独立区域，不编造内容。PBI-71 另验服务产品日志／已收尾 IDEO 日志的归属，不混同于设计卡。 |
| **22 · `sprint-22-project-agents`** | 73、75 | 参谋给独立第二意见；插件让**各个使用它的项目**按自己的 Stakeholder 角色卡复用 Agent。不是给所有项目装同一批角色，也不是通用 Claude Code Setup。 | Developer 用合适的 IDEO 方法调研已有做法，再提设计。角色卡定后展示配置；接受才写该项目的 Agent 并在产品日志 2.1 引用，拒绝不写且流程照走。更新先展示差异、确认，不覆盖用户文件。独立反馈用新上下文。Master 关注注册、引用与权限，不替 Developer 定 How；DSH 等价能力待查。 |
| **23 · `sprint-23-log-rules`** | 76、77、78、79、69 | 把决定、承诺、验收与收尾说清。DoD 全部生效，选本轮核验重点不是豁免。进入或返回阶段前等 PO；Ideate 发散前 PO 先组织。承诺原文只存一份，可另写解释；区分汇总级和项目级 Goal。保留设计中间材料，项目 Retro 的重要教训分条入记忆。 | 分别验证 How 到施工、选方案到原型等阶段门；不把认可上一阶段当下一阶段放行。解释不是承诺，已有等价规则不重写。保留速写、演示、评审、合成稿及被否方案，不把原型算 Increment。PBI-69 管项目教训，不与 PBI-51 合并。 |
| **24 · `sprint-24-loading-reliability`** | 80、81、82、83 | 定 Product Goal、Sprint Goal，写设计挑战／目标／问题与精化产出前，确实读了指定原文、约定和模板注释。角色入口实际调用 4/3/3/2 个内核。sprint-kernel 加载时即包含 Sprint Backlog／Sprint Goal 方法论原文，单有链接不算。解决承诺 hook 在每条消息上的开销。 | 分别验证“调用 Skill”和“读原文并使用”；其他阶段材料是否预载靠实测，不一次全塞。保留来源署名与原文。Master 与 Developer 调研 hook 瓶颈，必要时用五模式或提设计研究；旧测 2.1–2.4 秒，300ms 是候选值，先定环境、样本、通过线和预算，再跑测试；注入频率、原文和开关不变。 |
| **25 · `sprint-25-dsh-docs`** | 72 | 验收已有的 DSH 分发、收齐 README、快速上手及维护说明。Claude 与 DSH **两版都改为 0.6.3**，不是其中一版降号。建立跨宿主的 `AGENTS.md`；`CLAUDE.md` 单向导入 `@AGENTS.md`，不循环互引。 | DSH 实现 `b2679aa` 已在 main；原 DSH 工作树同点，无待合入内容。先查 SeaPawn `advisor-workspace` 的既有验收，再补缺口，不重复造包。打包／自动检查与实际安装、角色入口、承诺上下文分开验；验证版本回退的升级行为；DSH 是否读取共用文件及能否注册项目 Agent 由 Developer 实查。改号归本期，发布另授权。 |
| **26 · `sprint-26-plugin-memory`** | 51 | PO 与 Developer **通读整个插件**，不只 conventions；审作者约定的依据与去留，把插件自己的约定做成 Memory。不是项目知识库或 Retro 档案。 | PO 主要定方向、品味和内容，也可以交 AI 自动化处理大量工作；不要求 PO 自己写命令、逐段施工或全程盯守。未配置时不自动加载，开启才自动加载，两种情况下都可手动调用。Skill／命令只是候选，载体未定；若选 Skill，用 skill-creator 等相应工具。保留原书摘录、PO 原话和已批准文本。 |

## 谁问、谁决定、何时合

- **每期都可以、也必须把关键问题交回 PO**，包括 PO 不亲自跟进或审稿的期：目标和范围不清、价值／品味取舍、验收含义或证据不足、与已有决定冲突、是否进入下一阶段。已定的实现细节由 Developer 自主处理；不让 PO 决定每个技术步骤。Master 及时报阻碍、跟进依据与审阅，不替 PO 拍板，不代写 Developer 的 How。
- PO、Master、该期 Developer 一起定本期 Why、What 和精化；Developer 提 How 并在本期工作树建 `SprintBacklog.md`。认可计划不自动授权施工。Master 只维护跨期材料，不提前建六份日志，不批量启动团队。
- Developer 自测，Master 对照任务、DoD、验收条件审阅；合入前把完整增量和未决取舍交给 PO。PO 可选择哪些内容要亲自看、哪些让 AI 做；提交、合并、推送、发布各按明确授权。
- 工作树隔离施工目录，不消除同段或语义冲突。尤其留意 21/23 的设计日志字段、22/24 的角色入口、23/24 的模板、24/25 的承诺行为，以及 26 的全插件整理。交接所用基线和受影响的规则，合入时列清差异，按 PO 决定整合并重验。

## 反馈对账

下面的短名对应反馈索引 `memory/FeedBack/MEMORY.md` 所指 IDEO-Scrum 文件；F 只用于核对来源，不是新的 PBI 或优先级。进入规划不等于反馈已解决。

| 来源 | PBI／Sprint | 原问题与去向 |
| --- | --- | --- |
| F01 · conventions-as-index | 51／26 | 约定怎样组织为可复用 Memory；索引是候选，不锁定实现。 |
| F02 · retro-lessons-as-separate-memories | 69／23 | Retro 只存重要教训，一条一条，不写汇总。 |
| F03 · product-goal-source-not-read | 80／24 | 定 Product Goal 前读对应产物原文；PO 指出偏差先回查依据。 |
| F04 · commitment-hook-cost | 83／24 | 保留承诺注入，定位每条消息的耗时，用同条件复测。 |
| F05 · author-conventions-need-review | 51／26 | 作者规矩逐条审去留，不把助手附加的建议当成规范。 |
| F06 · stage-read-before-draft | 80／24 | 设计、Planning、精化的漏读场景分别验证，不能只验证技能被调用。 |
| F07 · role-command-loads-kernels | 81／24 | Master／Developer／Designer／Stakeholder：4／3／3／2。 |
| F08 · drop-codex-for-dsh | 72／25 | 换宿主已有实现，收齐验收与用户、维护文档。 |
| F09 · ideate-entry-needs-po-approval | 77／23 | PO 先组织本次如何发散；助手写的“至少两种方法”不是 PO 规定。 |
| F10 · commitment-table-with-notes | 78／23 | 表下可解释为什么定这个目标；解释不计入承诺原文。 |
| F11 · keep-design-working-material | 79／23 | 收尾保留决策依据，包括没选的方案。 |
| F12 · dsh-build-version-0-6-3 | 72／25 | PO 最新决定：两版均为 0.6.3，不再单独追问 CC 是否改号。 |
| F13 · sprint-goal-style | 78／23 | 汇总级可按条目列；项目 Sprint 保留统一的价值目标。 |
| F14 · force-load-stage-text | 82／24 | 不全量预载所有方法和阶段文件；其余边界按测试证据定。 |
| F15 · sprint-backlog-artifact-location | 82／24 | sprint-kernel 的加载内容包含 Sprint Backlog 原文；实现要避免原文漂移。 |
| F16 · plugin-update-needs-full-energy | 51／26 | 是 PO 共作线的精力约束，不是其他五期的开工前置，更不是产品功能。 |
| F17 · commitment-hook-sprint-anchor | 91／未排 | 承诺钩子只认产品日志，只有冲刺日志的小项目会注进上层项目的承诺；PO 2026-11-22 定先登记、本轮不收，体验后再定。 |

**范围之外**：PBI-12 公开方法论分享留待以后；PBI-67 的自然触发专项按 PO 决定取消，从当前项撤下，不算已修好，不改写 Sprint 18 历史。

**交接依据**：[产品日志及 DoD](../ProductBacklog.md)、[无头验证约定](headless-testing.md)、[看板约定](../../plugins/ideo-scrum/board/board-log.md)。看板使用模板和 `scripts/board_check/check.py`，源文档与用户说明使用 `scripts/check_docs.py`；插件／分发按现行 DoD 验证。各期先定自己的判据再测，不把某期专项测试当六期统一门槛。

## 续：Sprint 26、27 两线并行（2026-11-22）

2026-11-22，PO：SeaPawn。Sprint 21–25 已收官。26 照上表做插件 Memory；另开 27，把反馈和零碎项收尾。两期并行，各一名 Developer，会话由 PO 开。PO 说今天精力够（F16：「我精力精力今天可以的，所以说我要开 A 线」）。

| Sprint · 文件夹／分支短名 | PBI | 谁做 | 关卡 |
| --- | --- | --- | --- |
| **26 · `sprint-26-plugin-memory`** | 51（含 85 的「记忆与约定另立包」） | PO 以 Developer 身份与 Developer 共作 | 照常由 PO 过；大改约定按 Developer 起草 → Master 审 → 对抗审查 → PO 强审 → 流程测试 |
| **27 · `sprint-27-wrap-up`** | 84、85（模板与看板）、86、89、90 | Developer 自做，Master 审 | Master 按下面的书面授权代 PO 过 |

**同一批文件不同时改**（并行的做法由 Master 定，PO：「你来想一种两全其美的办法吧」）：

- 26 先通读插件，逐条定每条约定的最终样子，记进 26 的日志；这一段不动插件文件。
- 27 照常施工，85 的迁路径排第一项。27 合入 main 后，Master 把改动的文件与规矩列给 26；26 合入 main，再动插件文件。
- 27 没合完，26 先改 27 不碰的部分。27 碰的是：模板与看板（85、89）、角色入口与「PO assistant」的说法（86）、`IDEO-modes/` 与 `ATTRIBUTION.md`（84）、`project-stakeholder` 与参谋入口（90）。
- 新的秘书角色照现有角色入口的加载方式写；26 定下 Memory 的加载方式后，所有角色入口（含秘书）在 26 里一起改。

**Sprint 27 的书面授权**（PO 2026-11-22 原话，逐字；27 开张时抄进其日志第 4 章）：

- 「B 线的话，我基本上就交给 AI 自己做了就是交给 Developer 自己做了，我就不参与 Developer 的团队了。」
- 「我建议是能给 B 线的就给 B 线，这样我就不用操心了，让 B 线自己去重组。」
- 「B 线的话就是 developer 自己做，然后你来审审核他，你们两个一块做就行」
- 89、90 交 27：「交给他，交给他呗，可以啊，你觉得可以就行。」

范围按 Master 提议、PO 认可（「OK，你定的这些就是这样子。」）：27 的各阶段决定——定 Sprint Goal、结束精化、施工放行、Sprint Test 放行、收官与本地合入 main——由 Master 代 PO 做，记进 27 的日志。仍回 PO：改 Product Goal；推送与发布；取消冲刺；推翻 PO 说过的话；86 的新称法与秘书定位（PO：「后面修改的话再说具体的那个修改内容」）。

**不做与不收**：PBI-88（pi 版插件）PO 2026-11-22 定不做，已从产品日志删去，仓库保留 DSH 与 Claude Code 两套分发；87、91 等 PO 体验后再定；12 以后。

**进展（2026-11-23，Master 记）**：

- **27 已收官**：tag `sprint-27-wrap-up`，main 快进到 `2572530`，未推送；归档在 [sprint-27-wrap-up.md](sprint/sprint-27-wrap-up.md)。上面「同一批文件不同时改」的前提已满足：26 把 main 同步进自己的分支后，即可动插件文件。
- **PO 全面放权**：「我不审了，后面自动过吧，你作为master监督审阅他们……」「26 27的review这些交给你和codex就可以，我只负责放行什么的」。所以 26 改为 PO 免审：Master 审定，派 Codex 或全新子代理做对抗审查，PO 只管放行。上表 26 一行里的「照常由 PO 过」「PO 强审」，由此替代；原话与范围见两期日志第 4 章。
- **26 的载体**：PO 定 A1——独立 `memory` 技能，由角色入口调用；「dsh要支持要记得」。
- **问题分流**：PO 定三级分流（自己定 → 问 Master → 经 Supporter 交 PO），Supporter 转达的 PO 意见算 PO 的（有例外），已随 27 写进约定 14。
- **PO 中途审了 Memory 草稿**：PO 在 Supporter 会话里逐条审（2026-11-23 02:55–03:4x），口径是「只要与 Memory 其它条目、各技能的说法不矛盾，就算过、就保留」。
  - 意见：要改 7 处，要补 2 处，其中一处是新规矩——Review／Retro 时由 Master 列出异议点和待研点，PO 挑哪些落 `documents/`、哪些落记忆。
  - 处置：Master 全部转给 26 Developer。PO 交 Master 判的几点：ideate-arrangement 只强调放行这一关；sprint-or-modes 照 PO 的话重写；modes-are-not-the-sprint 整条删。
  - relay-limits：Master 原判不放宽（Supporter 把它误记成「交 Master 判断」），PO 已推翻。经 PO 授权的 Supporter 转达，在权限、设置、CLAUDE.md／AGENTS.md、推送发布上也算 PO 的话；PO 在 Master 会话亲口说：「我授权之后，然后我让 supporter 去发，那实际上也认为是我的意见」。宿主只认动手会话里确认的，照宿主来，写进细则。
  - 改完 PO 不看第二遍，Master 复核后落盘。原话与处置记在 26 的 `review/po-review-2026-11-23.md` 和日志第 4 章。
- **Codex 对抗审查的修改**：26 Developer 在 `6a0bee9` 改完 15 条，并对 111 条规矩做了分句覆盖核查；Master 审过。附带一个条件：落盘后拿插件里的文件重跑覆盖核查。
- **删两条 PBI**：PBI-91 是 PO 定不做；PBI-99 的原话是「我记得99这个肯定是要删的，因为我已经审略完了」（经 Supporter，2026-11-23 03:5x）。Supporter 在 `d143bbd` 删掉了这两条。照 answers-back，条目的增删本该交 Master 记，这次内容无误，不回改。
- **26 收官的书面授权**（PO 在 Master 会话里亲口说，2026-11-23 约 04:2x，原话逐字）：「然后前面那几个点，我现在就开始授权，好吧。啊，一个是让 DSA 是临时读什么工作数啊。你直接让那个 supporter 帮你做就行。然后那个推送收关放行，我现在都都那个同意了。然后的话，嗯，最后 review review 和 retro 的内容我也同意了。反正到最后你你直接我给你授权到什么地步呢，就是说全部都 merge 完。后推送到远端，然后跟心我们这个本地的插件，一个是 DSH，还有一个是那个claude code。这两个都要更新。」
  - 授权范围：DSH 临时读 26 工作树（交 Supporter 做）；收官放行与推送已同意；Review、Retro 的内容由 Master 定、事后报；一直做到全部合入 main、推送远端、更新本机 DSH 与 Claude Code 上的插件（收官照常升版本号）。
  - 仍回 PO：改 Product Goal、取消冲刺、推翻 PO 说过的话、PO 点名要看的品味；GitHub Release 这类超出推送的公开发布；CLAUDE.md／AGENTS.md 除 44、56 行以外的改动；宿主要 PO 在场确认的权限提示。
  - 核对点照旧留成动作：推送前扫提交，推送后 `ls-remote`，装完核版本，审阅派 Codex。
