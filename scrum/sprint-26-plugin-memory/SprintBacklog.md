# Sprint Backlog — Sprint 26 (plugin-memory)

> Started: 2026-11-22 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `worktree-sprint-26-plugin-memory` | Product Owner: SeaPawn（兼 Developer，共作） | Scrum Master: IDEO # [master]-[main]-[manage sprint] | Developer: Sprint 26 Developer
> Now: Increment · 2026-11-23：PO 2026-11-23 全面放权（原话见第 4 章「PO 全面放权」）：本期 PO 不审，Review 之前由 Master 监督审阅，PO 在 Review 时看结果；How 已照此改（行 5、9、10、12、Key choices、Risks、Go-ahead 范围）；行 1 台账完成（111 条）；行 2 标注与核验完成（26 个核验文件到齐，补跑后共改 21 条标注，另有 5 条我覆盖了核验结论）；行 3 判据已提交；行 4 装置搭好，冒烟在跑（并发 2，开跑与跑完报 Master），两档替身（约 10k／约 20k 字符）的参数改动冒烟后单独提交发 Master 审；行 6–8 的起草完成：111 条各有新行或去向、29 个非编号块各有去向（`check_drafts.py check` 0 问题），装配出 102 行、14.1k 字符的清单（每行 ≤ 150），长文件 15 个有初稿，`roles-and-routing` 与标「待 27」的三行等 27 并入后同步；提交由 Developer 在本分支做；推送、发版仍要 PO 亲口说。
> Waiting for PO: None
> How to write this log: `sprint-log.md` in the sprint-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled later; add none. Work remarks go in chapter 4, Increment notes; an optional explanation of the commitment may follow its table (`overview.md` in the scrum-kernel skill folder, conventions 16 and 17).

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 约定变成 Memory：插件的约定逐条审过去留，收成一份短清单，长的另成文件、清单里留索引；叫出角色就带上同一套规矩，不用每次手动说明，照着就能守。 |
| --- | --- |

「叫出角色就带上」是 PO 要的结果（「只要敲了这个角色进来，那么这个 memory 就自动会被加载进来」）；写进角色入口还是用 hook，留给 How，目标里不定。

### 1.2 Definition of Done

[完整产品 DoD](../ProductBacklog.md#13-definition-of-done) 全部生效。本期重点核验（Master 选，PO 2026-11-22 审过）：

- **内容忠实**：原书摘录与 PO 原话逐字保留；作者约定标出依据。
- **署名**：带摘录的 Memory 文件有 Source／License 两行，与 `ATTRIBUTION.md` 一致。
- **可导航、无死链**：从 SKILL.md 入口 ≤2 跳到 Memory 的每条与每个长文件；全仓旧路径与旧约定引用迁到零。
- **插件校验、描述长度**：`claude plugin validate --strict` 通过；新增或改动的描述 ≤1024，并重跑触发测试，不比改前差。
- **DSH 分发**：`node --test scripts/check_dsh.mjs` 通过；DSH 的角色入口也带上 Memory。
- **Outcome**：本期要拿出「不用每次手动说明」的证据，判据在 2.2 定。

**开张与 Why 放行**：PO 2026-11-22（Master 会话）：「我觉得可以先不着急，我们可以先把每个的目标定出来」。范围：定 Sprint Goal 与本期 DoD 重点。

**Sprint Goal 决定**：PO 2026-11-22：「目标承诺约定变成 Memory 插件的约定，逐条审过去留。嗯。没毛病没毛病。」当时的目标原文：「约定变成 Memory：插件的约定逐条审过去留，收成一份短清单，长的另成文件、清单里留索引；叫出角色就带上同一套规矩，不用每次手动说明，照着就能守。」

**What 放行**：PO 2026-11-22：「然后你看一下。DOD，然后给选上，然后 PPI 条目给选上。然后你再来主导把 refinement 的。写进去，然后我再审一审」。范围：选 DoD 重点与条目，Master 主导写精化，PO 审；How 未放行。

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-51 | 通读：全插件约定逐条审去留 | 作为熟手，我想让插件的每条约定都有审过的去留和依据，以便转进 Memory 的都是该留的规矩 | 插件：四内核与角色 | M |
| PBI-92 | Memory：形状、载体与带上方式 | 作为熟手，我想让 Memory 放在一处、照定好的样子写、叫出角色就带上，以便规矩只有一份又随叫随到 | 插件：四内核与角色 | M |
| PBI-93 | Memory 草稿：sprint-log 与 ideo-log | 作为熟手，我想让 sprint-log 与 ideo-log 的规矩各转成一行或一个长文件，以便照着就能守 | 插件：sprint-kernel、ideo-kernel 的约定 | S |
| PBI-94 | Memory 草稿：design-log 与 product-log | 作为熟手，我想让 design-log 与 product-log 的规矩各转成一行或一个长文件，以便照着就能守 | 插件：design-kernel、scrum-kernel 的约定 | M |
| PBI-95 | Memory 草稿：board-log 与 overview | 作为熟手，我想让 board-log、overview 和角色命令里重复的规矩各转成一行或一个长文件，以便照着就能守 | 插件：scrum-kernel 的约定与角色命令 | M |
| PBI-96 | Memory 草稿：汇总与对抗审查 | 作为熟手，我想让整份 Memory 草稿先过 Master 审和独立的对抗审查，以便落盘前就把错漏改掉 | 插件：四内核与角色 | S |
| PBI-97 | Memory：落盘与引用迁移 | 作为熟手，我想让 Memory 落进插件、旧约定删掉、各处引用都指到新位置，以便只有一份规矩、链接都通 | 插件：四内核、角色入口、docs 与检查脚本 | M |
| PBI-98 | Memory：角色带上与验证 | 作为熟手，我想叫出任一角色就带上同一套规矩，以便不用每次手动说明 | 插件：角色入口与 DSH | M |

对照目标：51 已含 85 并入的「记忆与约定另立包」（产品日志 PBI-51 备注），目标的每一分句都落在 51 里，不缺条目。51 原为 L 级，2.2 精化时切成上面八条，2026-11-22 登记进产品日志。

### 2.2 Refinement

> Master 2026-11-22 起草，PO 当日审过；Developer 当日同步（第 6 步），提的 8 点已并入（标「同步补」）。

**视角**（照抄 PBI-51 用户故事）：作为熟手，我想让审订过的插件约定有一处可按需调用的 Memory，以便既能遵守同一套规矩，又不用每次手动说明。

**HMW**

1. 我们怎样让每条规矩一行就读懂，长的又不丢细节？
2. 我们怎样让 PO 逐条定去留，又不用逐行打勾？
3. 我们怎样让叫出角色就带上规矩，不叫的时候不打扰？
4. 我们怎样让规矩只有一份，不在新旧两处各存一份？
5. 我们怎样让原书摘录和 PO 原话原样留下，作者写的又能大改？
6. 我们怎样让 Claude Code 和 DSH 带上的是同一份？

**要点与归属**

| # | 要点 | 谁定 | 状态 |
| --- | --- | --- | --- |
| P1 | 形状：以短清单为主，一行一条；长的单开文件，清单里留一行索引（「说白了就是 Claude.md 和 memory 这两个混合」） | PO | ✓ 2026-11-22 已定 |
| P2 | 转哪些：六份约定文件（`overview.md`、`product-log.md`、`board-log.md`、`sprint-log.md`、`design-log.md`、`ideo-log.md`）的编号条目全转；SKILL.md、角色命令和模板注释里的规矩在通读时一并审，与约定重复的改为指向 Memory；原书摘录（`events/`、`references/`、`steps/`、`methods/`、`IDEO-modes/`、`assets/`）只读不转。同步补：条目之外的图、`overview.md` 的 Departures 表（README「How it differs」与它逐字对表，并链到它的锚点）随对应条目或长文件走，Source／License 行随含摘录的文件走（Master 定） | PO | ✓ 2026-11-22：「然后你说 PR 呃，我觉得没问题」（Master 读作 P2） |
| P3 | 旧约定文件：转完删掉，Memory 是唯一一份（「把以前的约定全部转换成 memory」） | PO | ✓ 2026-11-22：「P3转完就删也没问题啊」。**例外（Master 2026-11-23）：`board-log.md` 不并进 Memory 的长文件，也不删**，留在 `plugins/ideo-scrum/board/board-log.md`（27 搬过去的），当写看板的那份长文件用，清单里写看板的 4 行直接指向 `../../board/board-log.md`。原因：PO 的 PBI-85 定了「看板专门放到 board 里面去」（Master 转述），看板模板与 `scripts/board_check/check.py` 也指着它；「转完即删」对它不适用。其余五份（overview、product-log、sprint-log、design-log、ideo-log）照删 |
| P4 | 怎么审：Developer 先给每条标出处（原文／PO 原话／作者／补充）和建议（留／改／并／删），三批起草汇成一份完整草稿；PO 在整份草稿做完后一次性逐条过目——一条一条读、一条一条聊留什么不留什么、逐条微调，Developer 逐条记进过目账；没过目的行不进最终 Memory；过目后的改动随 Review 报给 PO | PO 定审法，Developer 出标注 | ✓ 2026-11-22。先定按文件成批、整份读：「批次我觉得怎么审？嗯，你这样说也行吧，我也能接受吧」「P4这样也可以」。同日 PO 对 Developer 改为逐条过目：「我一定要把每一处都给审核掉」「每一条我都要过目一遍」「我去一条一条读，然后我们一条一条的微调……因为它是记忆嘛记忆其实很重要」。再改为整份草稿一次过目：「你把他们所有的东西都做成了 memory 的草稿，然后直接推给我就行了，我一起审」「一共我只需有两点」「别的我都不需要在场」（均见第 4 章）。PO 2026-11-23 改为本期免审，由 Master 审定（见第 4 章「PO 全面放权」） |
| P5 | 载体与位置：PO 11-17 设想的独立技能「名字就叫 memory」，或放进现有内核。同步补：做独立技能的话，角色加载数由 4/3/3/2 变 5/4/4/3，DSH 的 `rolePrelude` 与 `check_dsh` 断言随改，How 里写给 PO 看 | Developer 提、Master 审定（PO 2026-11-23 本期免审，Review 时看结果） | ✓ PO 2026-11-23 定 A1：「26那就选择A1把，然后dsh要支持要记得」；位置与名字（`skills/memory/` 加 `long/`）、加载数 4/3/3/2→5/4/4/3：Master 审定 2026-11-23（`review/memory-outline.md` 第 1、2 节） |
| P6 | 怎么带上：写进角色入口（像现在按序调内核）、hook，或入口为主、hook 可选且默认关。PO：「每一个角色里面都会让他们先加载 memory」，hook「我们后面再讨论吧」；产品日志原定「不配置则不自动加载，开启才自动，始终可手动调用」。子代理是否也带上，一并提 | Developer 提、Master 审定（PO 2026-11-23 本期免审，Review 时看结果） | ✓ PO 2026-11-23 定 A1：「26那就选择A1把，然后dsh要支持要记得」；Memory 排角色入口最后调用（对 PO「先加载」读作「在做任何角色工作之前加载」）、子代理那句加上 memory：Master 审定 2026-11-23（`review/memory-outline.md` 第 2 节） |
| P7 | 同一份还是分角色：共用的规矩一份；角色专属的（Developer 的 DoD 核对、Master 的阶段门）怎样挂 | Developer 提、Master 审定（PO 2026-11-23 本期免审，Review 时看结果） | ✓ Master 审定 2026-11-23：一份共用清单，行上带角色标签（`dev` `sm` `des` `stk` `po`，无标签的行约束每个角色）；一行 ≤150 字符、软线 130；长文件判据、图与 Departures 表的去处、尺寸上限 16,000 字符、档位 20,000（A1 过 ② 的最大一档与约 16,000 字符中小的，结果表 `review/carrier-results.md`，Master 审定 2026-11-23）（`review/memory-outline.md` 第 3–7 节）；PO 2026-11-22 对 Developer：「先按你们的理解先给一份，最后我再来审核」 |
| P8 | 原书摘录与 PO 原话逐字保留，AI 写的约定可以大改 | PO | ✓ 已定（PO 2026-11-12） |
| P9 | 与 Sprint 27 的先后：先通读、逐条审，不动插件文件；27 合入 main 后再动文件，27 不碰的部分可先改（[总表「续」](../documents/sprint-roadmap.md)）。同步补：27 不碰的部分很少，所以合入前不落盘；转换草稿放本冲刺文件夹，不算动插件文件（Master 定） | Master（PO 交定） | ✓ 2026-11-22 已定 |
| P10 | 引用迁移：插件、docs、README、glossary、检查脚本里的旧路径与「convention N」引用一并迁，全仓 grep 旧值到零（已归档的历史日志不改） | — | ✓ 项目规矩（`AGENTS.md`） |
| P11 | 走大改约定的流程：Developer 起草 → Master 审 → 对抗审查（全新子代理）→ PO 强审 → 最后一轮流程测试 → 收官。本期的「PO 强审」由 Master 审定加全新对抗审查替代（PO 2026-11-23 全面放权，见第 4 章），PO 在 Review 时看结果 | — | ✓ 项目规矩（`AGENTS.md`） |
| P12 | PO 共作线：精力足时做；PO 定方向、逐条审，重复与技术活可交 AI | PO | ✓ 已定（F16） |

没有要研究的点：P5–P7 是做法选择，Developer 用实测说话，不需要设计冲刺或五模式。

**切分**（第 5 步；同步时 Developer 把转换拆成草稿与落盘两条，规模由 Developer 估；How 审过、批次切定后一并登记进产品日志，51 改为第一条）

| 条目 | 做成什么 | 验收 |
| --- | --- | --- |
| 51 · 通读与逐条审 | 全插件约定逐条有去留决定 | 六份约定文件每条一行审读记录：出处、建议、PO 的决定与日期；SKILL.md、角色命令、模板注释里与约定重复的已标出；记录放本冲刺文件夹；Master 审定，每条有决定与依据（PO 2026-11-23 本期免审，Review 时看结果） |
| 新 · Memory 的形状、载体与带上方式 | P5–P7 有定案 | 先交大纲（`sprint-log.md` 约定 11）：放哪、叫什么、短清单样子（拿 3–5 条真条目示范）、长文件怎样索引、角色和 DSH 怎样带上；带上方式附实测（叫角色、压缩后、子代理三种情况）；PO 定稿后才进转换 |
| 新 · 转换草稿 | 按审读结果写出 Memory 草稿，放本冲刺文件夹，不依赖 27 | 留下的每条规矩在草稿里恰好一处、一行读懂，长的有索引行；摘录与 PO 原话 diff 逐字不变；Master 审定、对抗审查过（PO 2026-11-23 本期免审，Review 时看结果）。规模 L，按 P4 的文件批次再切 |
| 新 · 落盘与引用迁移 | 27 合入 main 后，草稿落进插件，旧约定按 P3 删 | 全仓 grep 旧引用为零；`validate --strict`、`check_dsh`、`check_docs.py`、`board_check` 自测通过；Sprint 24「首稿前读全」的判定按新位置改过并重跑 |
| 新 · 角色带上与验证 | 叫出角色就带上同一套规矩 | 四个角色入口（27 合入后加秘书）在 Claude Code 与 DSH 各验一次；改过的描述 ≤1024，触发测试不比改前差；Outcome「不用每次手动说明」按下面「测试」定的判据与样本量过线 |

**测试**（第 13 条；How 定稿前补齐通过线，Test 前提交，提交后不改）

- 要新证据：`validate --strict`、`check_dsh`、`check_docs.py`、全仓旧引用 grep、摘录逐字 diff、描述长度、触发测试（与改前同日对照）、角色入口加载（Claude Code、DSH）、无头流程测试（做法见 `scrum/documents/headless-testing.md`）。
- 沿用旧证据：无。`check.py` 与看板模板都写着由 `board-log.md` 列出字段，迁 board-log 要两处同改，所以 `board_check` 自测重跑（同步补）。
- 回归：Sprint 24「首稿前读全」的判定按新位置重跑；角色加载数与 DSH 断言随 P5、P6 的定案改（同步补）。
- Outcome 信号「不用每次手动说明」：写进了目标，没证明就不过 Test。判据与样本量由 Developer 在 How 里提（同步时提的是约 8 条探针、每臂 3 次，对照臂先探路再冻结），Master 审，Test 前定。

**PO 审精化草案**（2026-11-22）：定 P2–P4（见上表），其余认可：「我觉得你这个26问题不大」。

**精化结束与 How 放行**（PO 2026-11-22，有条件）：「你可以让 PO 去出那个 HOW，然后他出不是先让他审吧，先让他也审一下，让他同步一下，他觉得有什么问题你再修改，没什么问题的就进入 HOW，然后让他去写这个 HWHOW 的时候呢，要考虑我的角色，然后让他去出一个 HOW 好吧。」Master 的读法：「他」指本期 Developer。PO 随后更正：「其实应该是让他提出疑问，他觉得有没有什么疑问，然后进行那个同步嘛，其实其实不叫审核，应该叫同步」。所以 Developer 同步第 1、2 章：提出疑问、逐点复述（第 6 步）；有疑问由 Master 改，改完或没有疑问即精化结束、进 How。How 要写明 PO 兼 Developer 的分工（`overview.md` 约定 11）。施工另等 PO 放行。切分的新条目在 How 审过、批次切定后一并登记进产品日志，同时把 PBI-51 备注里「不配置则不自动加载，开启才自动」改成与目标一致的读法：角色入口无条件带上，hook 才是「开启才自动」、可选且默认关（同步补，Master 定）。

**精化结束**（2026-11-22）：Developer 同步无阻塞疑问，8 点已并入；按 PO 的有条件放行，精化结束，进 How。

**提交**：PO 2026-11-22：「提交的话就 developer 那边做就行了，你就不用管了」。Developer 在本分支自行提交，不推送。

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | **[AI 自做]**〔通读〕台账：通读六份约定文件，抽出每条编号规矩，另列非编号块（图、Departures 表、署名行）和逐字块；写两个小脚本（抽条目、逐字比对） | `review/ledger.md` 与脚本，放本冲刺文件夹 | ✓ 2026-11-22 条目数与 grep 一致（`*-log` 五份 94＋`overview.md` 17＝111）；每份抽 3 条与原文逐字相同；脚本先拿已知样例自测 |
| 2 | **[AI 自做]**〔通读〕标出处与建议（P4）：六份文件每条标出处、依据、建议；SKILL.md ×4、角色命令 ×4、模板注释里与约定重复的规矩另表标出 | `review/<文件>.md` 六份＋散落规矩表；无据条目单列 | ✓ 2026-11-22 每条有出处、可指的依据（提交或日志行）、建议和理由（留的理由、删了会丢什么）；每份抽检 ≥10% 并改正；与行 3–5 互不依赖，可并行 |
| 3 | **[AI 自做]**〔形状〕判据与大纲（P5–P7）：先把判据①–⑧写定并单独提交，再提大纲，三案（A 入口调 Skill、B hook、C 合用）并列；大纲先交 Master（约定 11）；示范与原型放在插件副本（系统临时目录），不碰插件文件 | 判据（见 Key choices）；大纲：位置与名字、一行的句型、句柄、角色标签、索引写法、长文件判据、字符预算、图与 Departures 表去处；3–5 条真条目示范；三案×判据的后果并列表 | ✓ 2026-11-23（Master 审定大纲；PO 选 A1 后判据收窄，末节单独提交在正式测开跑前）判据在行 4 开跑前提交，之后不改；Master 审过；示范逐字取自台账；三案的后果按判据并列写全（含 A1 的加载数 4/3/3/2→5/4/4/3、DSH `rolePrelude` 与 `check_dsh`、新描述与触发测试、结构校验） |
| 4 | **[AI 自做]**〔形状〕（2026-11-23 起照第 4 章「载体实测收窄」读：PO 定 A1，只测 A1 与对照 N，B、C、A2 取消）三案平等实测（P6）：在副本上做出 A（含并入 `scrum-kernel` 的变体）、B、C，按判据①–⑧测：叫角色、`/compact` 后、子代理、普通会话、每条消息耗时，Claude Code 与 DSH 各一轮；另测角色由模型用 Skill 工具调（不是用户打 `/`）时 B 还触不触发，不触发再试 `PreToolUse`（matcher `Skill`）；压缩一格再测调用顺序（Memory 排最后与排最前，四个内核都调用、总额吃紧时哪个保得住） | 三案×判据结果表，加调用顺序的对照；原始证据放仓外，日志只留汇总 | ✓ 2026-11-23（A1 与 N，照第 4 章的收窄读；③ 只跑 1/6、另测 0/3，挪到行 14 补测（PO 问，Master 定），见第 4 章）每格有事件流或会话日志证据（不靠模型复述）；三案同题、同日、同环境；冒烟先过；技术失败补满有效试次；token 与耗时成对比；做不完当场拆开，第 4 章记一笔 |
| 5 | **[AI＋Master]**〔形状〕定方案（P5–P7）：我照三案×判据结果表提方案——带上方式（含子代理）、位置与名字、共用／分角色、一行写法与字符预算——并写一行的句型（3–5 条真条目示范）；Master 审定（PO 2026-11-23 全面放权：方案由 Master 审定）；理由、结果表和被否的方案放进审阅文件，Review 时随结果给 PO 看；示范与结果表另发 supporter，PO 想看就看，不等回复 | P5–P7 的方案与句型，带理由和被否的方案；Master 的审定 | ✓ 2026-11-23（Master 审定大纲；大纲与 5 条示范已发 supporter，载体结果表待正式测跑完，出来后另发）Master 审定；P5–P7 各有方案、理由与被否的方案；句型有 3–5 条示范；已发 supporter |
| 6 | **[AI 自做]**〔草稿 A〕`sprint-log.md`（26）＋`ideo-log.md`（4）：给每条保留的规矩写「转后的一行」，长的写长文件草稿；逐字块用脚本搬 | 逐条表（旧条逐字｜出处与依据｜建议与理由｜转后的一行／去向），加旧→新、新→旧两张覆盖表；`memory-draft/` 下草稿 | ✓ 2026-11-22（预算：整份清单 14,156 字符，在 16,000 的上限内；按批的份额没有另定，见第 4 章）每条旧规矩有去向、每个新行对得上旧规矩（脚本查两个方向）；每条保留的规矩恰好一行或一个长文件入口；逐字比对 0 差异；不超本批的预算份额；跨文件重复标出 |
| 7 | **[AI 自做]**〔草稿 B〕`design-log.md`（27）＋`product-log.md`（18）：做法同行 6，照行 5 选定的句型 | 同行 6 | ✓ 2026-11-22（预算同行 6）同行 6 |
| 8 | **[AI 自做]**〔草稿 C〕`board-log.md`（19）＋`overview.md`（17）＋角色命令里的重复规矩：做法同行 6；这两份是 27 要改的，放最后，若 27 已合入就按合入后的文件起草 | 同行 6 | ✓ 2026-11-22（预算同行 6；`ask-the-po`、`who-gets-which-work`、`board-writer` 三行与 `roles-and-routing` 标「待 27」，27 合入后改）同行 6 |
| 9 | **[AI 自做]**〔草稿〕三批汇成一份完整草稿，做成审阅文件（开头是方案与结果表，之后每条：旧规矩原文｜出处与依据｜我的建议｜新行），跑检查 | 完整草稿与审阅文件、旧→新与新→旧两张覆盖表 | ✓ 2026-11-23（清单 105 行、14,741 字符，在 16,000 的上限内；`check_drafts` 0 个问题，两个方向的覆盖与句柄唯一都过；装配无未解占位符，细则文件都被指到、指向 board-log 的路径真有这个文件；引文逐字 18 处里 17 处，另一处是 ideo-log#2 里用户的叫法，见第 4 章）预算、逐字、句柄唯一、索引无死链、两个方向的覆盖检查通过 |
| 10 | **[AI＋Master]**〔审定〕整份草稿由 Master 审定：方案（含结果表与被否的方案）、111 条旧规矩的新行、29 个非编号块的去向，逐条；再由 Master 发起一个全新审阅（Codex 或子代理）做对抗审查；我按意见逐条改，不同意的写明理由（PO 2026-11-23 全面放权：本期 PO 免审，Review 时看结果；原定 PO 整份过目取消；同日稍后改为「PO 中途看一遍」，意见记在 `review/po-opinions.md`，见第 4 章） | 审定账：P5–P7 的最终决定（带日期与依据）、每条的定稿文字与日期（Master 审定）、对抗审查报告与处理；新旧两张覆盖表照留 | P5–P7 各有 Master 的审定；每条旧规矩有去向、每个新行有 Master 审定的文字与日期；对抗审查意见逐条有处理（改了，或写明不改的理由）；Master 说「行」 |
| 11 | **[AI 自做]**〔落盘〕等 27 合入 main：把 main 同步进本分支，对 Master 给的「27 改了哪些文件与规矩」逐项对草稿 | 27 增量表 | ✓ 2026-11-23（`review/s27-increment.md`：第一节含义变了的单列交 Master 审，最后一节记同步后做了什么）27 碰过的条、路径、术语在草稿里逐项处理；改了含义的规矩单列、交 Master 审，列入改动清单 |
| 12 | **[AI 自做]**〔落盘〕Memory 入插件，旧约定文件按 P3 删；SKILL.md、角色入口（含 27 的秘书；A1 案按行 5 审定的调用顺序，排最后压缩后最保）、DSH 适配按行 5 审定的方案改 | 插件树里的 Memory；旧约定文件已删；改动清单（落盘后与审定账不同的行） | 逐字比对 0 差异；落盘后每一行与审定账比对，不同的列入改动清单，随 Review 报给 PO（含义变化的由 Master 审），不停下等；带摘录的文件有 Source／License 两行且与 `ATTRIBUTION.md` 一致；描述 ≤1024；`validate --strict` 通过；结构有变就派 `plugin-dev:plugin-validator`（Haiku） |
| 13 | **[AI 自做]**〔迁移〕迁引用：docs、README 中英、glossary、`check_docs.py`（含 Departures 对表来源与锚点）、`board_check` 与看板模板的占位句、`check_dsh` 等 | 旧句柄→新位置的替换表；改好的文件 | 旧路径与旧「convention N」引用 grep 为零（`scrum/documents/` 归档与 `references/` 除外）；`check_docs.py`（含 `--selftest`）、`check_dsh`、`board_check` 自测通过 |
| 14 | **[AI 自做]**〔验证〕带上验证与回归（Developer 自测，不是 Sprint Test）：四个角色入口在两宿主各一轮（27 之后五个，含 Supporter）；触发测试；Sprint 24「首稿前读全」按新位置改判定重跑；补载体测试挪过来的两项（PO 问、Master 2026-11-23 定）：③ 子代理带不带 memory（3 个会话）与另测模型自己调角色时入口的加载序列含 memory 跑不跑（3 个会话），都只报、一次跑一个，③ 若 0/3 就改那句提示的写法再测一轮；DSH 压缩后没人问起清单时模型会不会自己重载 | 验证表，证据放仓外，汇总记入第 4 章 | 各项不比改前差；角色入口加载有事件流或会话日志证据；缺口如实写 |
| 15 | **[AI＋Master]**〔测试〕冻结测试方案：探针清单、样本量、通过线、判定脚本自测；对照臂探路；Master 审 | 测试方案文本（Master 放进 2.2「测试」）；单独一个提交 | 提交后不改；判定脚本拿已知结果自测过 |

**Key choices**

- **草稿放冲刺文件夹，落盘等 27**（P9）：27 的 85、86、89 几乎盖住六份约定（五份提到模板，`overview.md` 有「PO assistant」，`board-log.md` 在 89 里），所以按「合入前不落盘」排。`review/` 与 `memory-draft/` 在本冲刺文件夹里，不算动插件文件；27 迟迟不合也不挡行 1–10。
- **整份草稿由 Master 审定，再对抗审查（PO 2026-11-23 免审，同日稍后改为「PO 中途看一遍」，见第 4 章）**（PO 原话见第 4 章「PO 全面放权」；此前 PO 2026-11-22 的几次改法——逐条过目、整份一次过目、先出草稿最后再审——也留在第 4 章）：审阅文件比 P4 多一列「转后的一行／去向」，Master 一条一条审，不先审标注、再审成品两遍；再由 Master 发起一个全新审阅（Codex 或子代理）做对抗审查，我按意见逐条改，不同意的写明理由；PO 在 Review 时看结果（审阅文件、审定账、覆盖表、对抗审查报告）。代价是被删的条目白写一行，AI 成本可忽略；所以方案与句型先由我提、Master 审定（行 5），照着往下做。
- **没经 Master 审定的行不进最终 Memory**：审阅文件里每行带「Master 审定的文字＋日期」（审定账）；融合产生的新句子也在审阅文件里，同样逐条给 Master 看。另出旧→新、新→旧两个方向的覆盖表，旧规矩不会悄悄消失，新行不会没人看过。审定之后的改动（27 增量、审查意见、句柄改号、迁引用）不再停下等：落盘后用脚本与审定账比对，不同的行列成改动清单，随 Review 报给 PO，含义变化的由 Master 审。
- **按文件批次起草，只是 AI 的顺序**：A（`sprint-log`、`ideo-log`，30 条）→ B（`design-log`、`product-log`，45 条）→ C（`board-log`、`overview`，36 条）。27 要改的放最后，期间它可能已合入，少起草一遍旧文。三批做完才汇成一份交 Master 审定，Master 不按批各审一次；句型的口味靠行 5 的 3–5 条真条目示范先定（Master 审定，也发 supporter），起草都照它写，免得整份返工。
- **载体与带上方式：三案平等，判据先冻结再测，我提、Master 审定，PO 在 Review 时看结果**（2026-11-23 PO 定 A1，实测收窄，见第 4 章；下面三案并列与后果表留作被否方案的记录。P5、P6；PO 指出 hook 与 Skill 还没正经比过，Master 转述；PO 2026-11-22：「先按你们的理解先给一份，最后我再来审核」，2026-11-23 改为全面放权由 Master 审定）：
  - **A 入口调 Skill**：A1 独立 `memory` 技能（PO 11-17 的设想），清单内联在 SKILL.md，每个角色入口在调用序列里多调一次；A2 并入 `scrum-kernel`，不新增技能。
  - **B hook**：叫出角色命令时由 `UserPromptExpansion`（matcher 按命令名，如 `ideo-scrum:developer`）注入 `additionalContext`（≤10,000 字符）；压缩后由 `SessionStart`（matcher `compact`）补注；另留一个手动入口技能，始终可手动调用。
  - **C 合用**：入口调 Skill，hook 只在压缩后补注。
  - **判据**（行 3 写定，行 4 开跑前单独提交，之后不改）：① 叫出角色必带上，两宿主都测；② 压缩后还在；③ 子代理；④ 不做 Scrum 的会话不打扰；⑤ 每条消息的开销（Sprint 24 的教训：hook 不能拖慢发消息）；⑥ DSH 能否等价；⑦ 能否按角色挂不同的部分；⑧ 维护量与是否优雅。另测：角色由模型用 Skill 工具调（不是用户打 `/`）时，B 还触不触发。
  - **后果并列**（预期；「文档」「仓库」是已核的事实，「待测」由行 4 定）：

    | 判据 | A1 独立技能 | A2 并入 `scrum-kernel` | B hook | C 合用 |
    | --- | --- | --- | --- | --- |
    | ① 叫出角色必带上 | 入口指令调 Skill，靠模型照做；Sprint 24 测过四角色按序加载 4/3/3/2（产品日志），多加一次调用后再测 | 同 A1，不多一次调用 | hook 注入，不靠模型自觉；只 Claude Code；matcher 命中 `ideo-scrum:<角色>` 待测 | 同 A1 |
    | ② 压缩后还在 | 技能重新附上，从最近调用的开始填，单个 ≤5,000 token、合计 25,000（文档）；Memory 排最后最保，吃紧情形待测 | 与 `scrum-kernel` 正文共用 5,000 token，超出的尾部被截（文档：保留开头），Memory 接在正文后面可能被截；`scrum-kernel` 排第二个调用，较早，吃紧时易被挤 | `SessionStart`（matcher `compact`）补注，不占技能额度（文档） | 同 B 的补注 |
    | ③ 子代理 | 临时派的子代理预载不了技能，委托时放相关几行；自定义 agent 的 `skills:` 可预载（文档） | 同 A1 | `SubagentStart` 可注入（文档），要会话标记免得打扰无关会话；待测 | 同 A1，或加 B 的路线 |
    | ④ 普通会话不打扰 | 不调用就零成本；但新描述常驻技能清单，要写成「召唤才来」并测不误触发 | 只在加载 `scrum-kernel` 时带上（它本来就召唤才加载），但 Stakeholder 也会带上 | matcher 只命中角色命令；补注、子代理注入要先判断会话叫过角色 | 补注同样要判断 |
    | ⑤ 每条消息的开销 | 无额外耗时；加载后内容常驻上下文 | 同 A1 | `UserPromptExpansion` 只在命令展开时跑，不挂每条消息；耗时待量 | 只在压缩后跑一次 |
    | ⑥ DSH 等价 | `rolePrelude` 预载是现成路径；`rolePrelude` 与 `check_dsh` 断言要改（仓库） | 近乎不改：DSH 本来逐字预载 `scrum-kernel`（仓库） | DSH 适配器现在只用 `skills.register` 与 `systemPrompt.context`（仓库），未见命令展开 hook；等价办法是适配器按角色把 Memory 拼进角色内容，或走 `systemPrompt.context`；待测 | 同 A1；压缩由 DSH 的命名上下文回放处理，待查 |
    | ⑦ 按角色挂不同部分 | 正文整份加载；分角色要拆多份、入口指定读哪份，多一跳 | 同 A1，且 Stakeholder 也带上 | 脚本按 `command_name` 选段，直接（文档） | 同 A1 |
    | ⑧ 维护量与优雅 | 新增 1 技能；改各角色入口、DSH 适配与断言；最简 | 不新增文件，但 `scrum-kernel` 变长、混进作者约定，PO「名字就叫 memory」落空 | 新增 hook 脚本（sh）＋DSH 的 JS 等价＋手动入口技能，两处同步；Windows 上靠 `sh`（承诺 hook 已有先例） | A1 加一个很小的补注 hook |
    | 另测：模型自己用 Skill 工具调角色 | 入口指令随角色正文走，照常 | 同 A1 | `UserPromptExpansion` 多半只管用户打 `/` 的展开，要试 `PreToolUse`（matcher `Skill`）补；待测 | 同 A1 |
    | 其他后果 | 加载数 4/3/3/2→5/4/4/3（F07 口径要改）；新描述 ≤1024 且测触发；结构有变要 `--strict` 加 validator | 加载数、描述都不变 | 手动入口技能同样要新描述；改 `hooks.json` 属结构变化；取证用 `--include-hook-events` | A1 的后果，加一个补注 hook |

  - **我的倾向**：A1 先；② 压缩后保不住再加 C 的补注；B 只在 ① 或 ⑥ 的实测明显更好、DSH 又做得出等价时才取。理由：最简优先，A1 沿用已验证的「入口按序调 Skill」和 DSH 现成的预载路径，不新增 hook 脚本；B 的好处是不靠模型自觉、按角色选段、压缩后可靠，代价是两宿主各写一份，所以让实测说话。PO 说的是「先加载」，与 A1「排最后压缩后最保」有出入，顺序由行 4 的实测定，行 10 由 PO 最后审。
- **开关与子代理**（P6 余下的）：叫出角色就带上是无条件的（目标原话）；hook 若取（B 或 C），关法沿用承诺 hook 的环境变量（`IDEO_SCRUM_MEMORY=off`，与 `IDEO_SCRUM_COMMITMENTS` 同一路），要不要开关在行 5 提、行 10 由 PO 最后审；两宿主都有先例（Claude Code `hooks/commitments.sh`、DSH `systemPrompt.context`）。子代理默认不带全文，委托时只放相关几行；行 4 实测「带」与「不带」的差别后在行 5 提，行 10 由 PO 最后审。
- **清单预算 ≤8,000 字符**（提议，行 5 提、Master 审定；2026-11-23 真清单约 14k 字符，按两档替身（约 10k／约 20k）测，最终尺寸按结果定，见第 4 章）：hooks 的 `additionalContext` 超 10,000 字符会被转存成文件，只给 2,000 字预览（[hooks](https://code.claude.com/docs/en/hooks#add-context-for-claude)）；自动压缩后，技能只重新附上最近一次调用，每个取前 5,000 token、合计 25,000，从最近调用的技能开始填，老的可能整个丢掉（[技能生命周期](https://code.claude.com/docs/en/skills#skill-content-lifecycle)、[压缩后留下什么](https://code.claude.com/docs/en/context-window#what-survives-compaction)）。所以 A1 案里 Memory 排角色入口最后调用，压缩后最先保住（PO 说的是「先加载」，两者有出入，顺序由行 4 的实测定，行 10 由 PO 最后审）。超了往长文件挪，仍装不下就回 PO 定再删，不加预算。预算按字符、技能上限按 token：英文约 4 字符一个 token（估），8,000 字符约 2,000 token，留有余量；清单若写中文要重算。按每行约 100–130 字符估，清单约放 60–80 行；111 条旧规矩融成多少行，要行 1 的台账与行 2 的标注出来才报数，条数由 PO 逐条定。
- **一行带稳定句柄**（如 `sprint-24`＝旧文件简称＋旧编号）：旧「convention N」引用在插件内约 150 行／18 个文件，仓库层对 `conventions/`、`overview.md` 的引用约 65 行／14 个文件，可按替换表机械迁移；并掉的留别名，删掉的在表里标「已删」并改引用处。句柄样式在行 5 提。
- **做法**：逐字块（原书摘录、PO 原话、署名行）用脚本搬再比对，不手抄，便宜的模型抄长文会丢字，AI 写的约定才由模型改写（P8）。标注与起草每份文件一个子代理，显式 `model: Haiku`，我抽检，出错或判断不够再升档并写理由；对抗审查用全新子代理，Haiku 起步，按结果升档。
- **PO 的分工（PO 兼 Developer，约定 11；2026-11-23 全面放权）**：本期 PO 不进场：Review 之前的各阶段决定与审阅（方案、整份草稿、Increment 认可、放行 Sprint Test、Test 判定）都由 Master 代 PO 做，PO 在 Review 时看各期结果。台账、标注、定方案（我提、Master 审定）、起草、汇总、Master 审与对抗审查、落盘、迁引用、跑测试都由 AI 做；途中真有要 PO 审、加入或回答的，通知 supporter（`IDEO # [supporter]-[main]-[support PO]`），由它提醒 PO，不阻塞的先往下做（PO 2026-11-22：「有什么需要我来审核，或者说我加入的，你有什么问题想问我的，你就可以去通知那个 supporter，然后 supporter 他会提醒我的」）。仍回 PO 的：改 Product Goal、推送与发布、取消冲刺、推翻 PO 说过的话、`CLAUDE.md`／`AGENTS.md` 的改动（第 44、56 行迁移已获直接点头）。PO 不写命令、不盯守，也不要求打勾，决定由我逐条记（F16、P12）；Master 审三处：形状大纲、整份草稿、冻结方案，并发起对抗审查。
- **测试通过线**（提议；Master 审后放进 2.2，Test 前冻结提交）：`validate --strict`、`check_dsh`、`check_docs.py`（含 `--selftest`）、`board_check` 自测全过；旧引用 grep 0 处；摘录逐字 diff 0 处；每个 description ≤1024 字符。触发测试沿用现有题组与次数，改前同日同环境重测，每条路径改后 ≥ 改前（AGENTS.md：改了描述就重跑触发测试，结果不能比改前差）；担心噪声就加次数，不降线，次数冻结时写死。角色入口加载：每入口每宿主 3 次新会话，3/3 次在做其他事前带上 Memory（事件流或会话日志证据）。Sprint 24「首稿前读全」：题组与次数照旧，改后不比改前差（≥ 改前）；担心噪声同样加次数，不降线。
- **Outcome 判据与样本量**（提议）：「不用每次手动说明」＝叫出角色后给一个不提规矩的自然任务，AI 自己照 Memory 的规矩做。
  - 探针 8 条，六份约定文件各至少 1 条（`sprint-log`、`design-log` 可各 2）；每条是不带引导词的短任务加一个「不守规矩就会错」的坑，由脚本读会话日志或落盘文件判定；清单在冻结时定，这里只给选法。
  - 两臂：对照臂＝27 合入后的 main（无 Memory），Memory 臂＝本分支；同一天、同环境、同一便宜模型（magpie）。
  - 样本：每探针每臂 3 次（Sprint 20「一组 3 次」先例），共 48 次；另加压缩后 1 条、子代理 1 条（若 P6 带子代理）各 3 次 ×2 臂；技术失败补满有效试次，不挑样本。
  - 入选：先用对照臂探路（每条 3 次），对照臂守规矩 ≤1/3 才入选，免得改前已满分（Sprint 14 教训）；探路结果不进 Test，Test 重跑新试次。
  - 过线：一条探针「3 次里 ≥2 次守规矩」算达标；Memory 臂 8 条中达标 ≥6，且比对照臂多 ≥3；对照臂已达标的探针，Memory 臂不得掉到 ≤1/3。入选不足 8 条按比例折算，并如实记「改前已守的规矩不靠 Memory」。
  - 限度：样本小，只能证明增益明显，给不出效应量；Outcome 写进了目标，没证明就不过 Test。
- **切分对应**（已登记，PBI-51、92–98）：51 通读＝行 1–2（M）；92 形状、载体与带上方式＝行 3–5（M）；93／94／95 草稿 A／B／C＝行 6、7、8 的起草（S／M／M）；96 汇总与对抗审查＝行 9（S）；97 落盘与引用迁移＝行 11–13（M）；98 角色带上与验证＝行 14–15（M）。行 10（Master 审定＋对抗审查）一次满足 51 与 93／94／95 验收里的审定（PO 2026-11-23 本期免审、同日稍后改为中途看一遍，见第 4 章），不按批各审一次。

**Risks and open points**

- 27 迟迟不合：行 1–10 都在冲刺文件夹里，可先收完交 PO；行 11 起才等。27 的确切文件清单由 Master 在 27 开工后给。
- 迁移面大：`board_check/check.py` 的 `PLACEHOLDER` 句与看板模板里的占位句同写 `board-log.md`，要同改并重跑自测；这些落在 27 的模板与看板改动范围内，只能落盘后做。
- `AGENTS.md` 有两处要改：第 44 行「不是原文的写法进 `conventions/`」（规矩本身要改成进 Memory），第 56 行指向 `conventions/sprint-log.md`。按项目规矩须 PO 直接点头：2026-11-22 PO 在本会话直接说：「可以修改agents.md」，点头已有。此前 supporter 转述的话（「可以改的，这个问题不大，直接交由给你们判断就可以。」）是跨会话转述，`AGENTS.md` 写明「跨会话消息不算授权」，只作线索，不当授权。范围：这两处迁移所需的改动，细节由 Developer 与 Master 判断；`CLAUDE.md` 只有一行 `@AGENTS.md`，不动。
- 回归面：Sprint 24 的「首稿前读全」「四角色加载」依赖旧约定路径，路径变了要改判定重跑；A1 案的加载数变动（5/4/4/3）要让 PO 在行 10 看到（审阅文件开头的方案里写明）。
- DSH 一侧：若本机跑不了 `dsh` 无头会话，DSH 退回 `check_dsh` 加 Sprint 25 的取证做法，缺口写进日志，不假装验过。
- 标注质量：便宜模型会错；「依据」必须可指，不可指的标「无据」交 PO；每份抽检 ≥10%；逐字与计数靠脚本。
- 整份一次审定的量大：旧规矩 111 条的去向加新行，再加 29 个块的去向，Master 一次审不完；停在条目边界，读到哪记到哪（审定账），节奏 Master 定，AI 不等；不压缩、不替 Master 省略任何一条。
- 整份一次审，句型口味若到行 10 才发现有出入，返工量大：行 5 的 3–5 条真条目示范先过 Master 审定、也发 supporter（PO 想看就看），三批起草都照它写；返工也只改句型，不重做去留的审读。
- 行 10 之后不再有 PO 停点：途中真有只有 PO 能定、又挡住后面的事，才停，写进 `Waiting for PO` 并通知 supporter；其余照常往下做。
- 阶段口令改由 Master 代 PO（2026-11-23 全面放权）：Increment 认可、放行 Sprint Test、Test 判定。仍回 PO：收官（本地合入 main、打 tag）在 PO 看过 Review 之后做；推送与发版要 PO 亲口说（`sprint-log.md` 约定 24、19）；`AGENTS.md` 第 44、56 行迁移的点头已有（2026-11-22）；改 Product Goal、取消冲刺、推翻 PO 说过的话。
- Outcome 未证则 Test 不过：对照臂若本来就守规矩，如实记「Memory 对这条无增益」，不挑样本凑数。
- 审读记录归档：PO 逐条的决定是本期成果，收官时随日志归档到 `scrum/documents/`，不当可清理的工作文件（Review 时由 Master 与 PO 定）。
- 版本号与发版：本期不预设，收官时 PO 定；推送与发布另授权。

Go-ahead: 2026-11-22，PO（SeaPawn）直接对 Developer 说：「OK，现在我觉得差不多了，然后 Master 同意之后，你就可以直接开工了。」Master 同日同意（「How 这一轮我又审了一遍，没问题」），条件已满足。PO 随后又说：「你可以你们先出一份比较好的草稿，你知道吧，最后再给我来审核」「你可以直接去修改掉你的这个 How」，How 已照此改。范围：第 3 章行 1–15；在本分支提交（含行 15 的冻结提交；提交由 Developer 做，PO 已定，见 2.2 末）；27 合入 main 后把 main 同步进本分支；27 合入前不动插件文件；不推送、不发版（仍要 PO 亲口说）；合入 main 和打 tag 在 PO 看过 Review 之后做；`AGENTS.md` 第 44、56 行迁移的点头已有；放行 Sprint Test 由 Master 代 PO（2026-11-23 PO 全面放权，见第 4 章；Master 2026-11-23 通知 Developer 照此改 How，范围按他记在第 4 章的为准）。当时的 Sprint Goal：「约定变成 Memory：插件的约定逐条审过去留，收成一份短清单，长的另成文件、清单里留索引；叫出角色就带上同一套规矩，不用每次手动说明，照着就能守。」2026-11-22 PO 又在本会话直接说：「可以修改agents.md」——`AGENTS.md` 第 44、56 行迁移的点头已有，范围见 Risks。

## 4. Increment notes

- **开张（2026-11-22）**：PO 定由 Master 先写第 1、2 章，PO 审后交 Developer 复述精化、写 How，再由 Master 审（PO：「我们现在直接把他的前两部分写好，然后让他们审过，然后再让他们写 how 你再审过就可以了」）。基线 `1145382`（等于 main）；本文件由 Master 建，Developer 在本分支提交（git 历史可查）。
- **How 草案（2026-11-22，Developer）**：第 3 章已写，依据 PO 的有条件放行，基于 Master 同步补后的第 1、2 章。清单预算 8,000 字符、探针 8 条×每臂 3 次、各条通过线都是提议，Master 审后放进 2.2「测试」，Test 前冻结提交。等 Master 审，再交 PO；施工未放行。
- **Master 审 How，改三处（2026-11-22，Developer 改）**：① 触发测试与「首稿前读全」的通过线改为 ≥ 改前（AGENTS.md 要求不能比改前差），担心噪声就加次数、不降线；② 清单预算的限制数字附官方文档链接，并补一条：独立技能案里 Memory 排角色入口调用顺序的最后，压缩后最先保住，行 4 的实测也测这一点；③ AGENTS.md 要改的两处（第 44、56 行）写进 Risks，PO 直接点头前行 15 不碰它。另：2.1 由 Master 换成登记后的八条（51、92–98），「切分对应」改为已登记。行 2、15、16 一次做不完就当场拆开，在此记一笔，不回头改 How。
- **PO 对 How 的意见（2026-11-22，PO 直接对 Developer 说）**：「我一定要把每一处都给审核掉」「每一条我都要过目一遍」「我去一条一条读，然后我们一条一条的微调……因为它是记忆嘛记忆其实很重要」；先读后读都行，其他的在场不在场问题不大。据此改 How：PO 的审改成逐条读、逐条聊、逐条微调（P4 原写「整份读，不逐行打勾」，Master 已在 2.2 改）；新增「没过目的行不进最终 Memory」与两个方向的覆盖表；相关工作项、Key choices、Go-ahead 随改。
- **PO 把在场的点减到两处（2026-11-22，PO 直接对 Developer 说）**：「你把他们所有的东西都做成了 memory 的草稿，然后直接推给我就行了，我一起审」「一共我只需有两点」…「别的我都不需要在场」；两点是定方案（hook、入口调 Skill 或合用）和整份草稿的一次审，终稿不用再读（「最后什么样那就不需要管了」）。据此改 How：在场点由五个减为两个（行 5 定方案、行 10 整份草稿一次过目），三批草稿只是 AI 的起草顺序，不再各坐一次；终稿那次整份重读去掉，改为落盘后用脚本与过目账比对，不同的行列成改动清单随 Review 报给 PO；阶段口令（Increment 认可、放行 Sprint Test、收官）与 `AGENTS.md` 点头不算在场，见 Risks。行号对照（旧→新）：1–6 不变；7、9、11 并入新行 10；8→7；10→8；12→9；13→11；14→12；15→13；16→14；17 去掉；18→15；前面几条备注里的行号按旧号读。
- **PO 放行施工，并改为先出整份草稿、最后再审（2026-11-22，PO 直接对 Developer 说）**：「OK，现在我觉得差不多了，然后 Master 同意之后，你就可以直接开工了」；Master 随后同意。又说：「你可以你们先出一份比较好的草稿，你知道吧，最后再给我来审核」「就是先按你们的理解先给一份，最后我再来审核」「你可以直接去修改掉你的这个 How」，中途有事「你就可以去通知那个 supporter，然后 supporter 他会提醒我的」。据此改 How：行 5 由「PO 在场」改为「AI＋Master」定方案，方案与结果表并进审阅文件，随整份草稿在行 10 给 PO 最后审（PO 可推翻）；PO 的在场点只剩行 10（上一条备注写的「两处」作废）；中途要 PO 的事通知 supporter（`IDEO # [supporter]-[main]-[support PO]`）。行号不变。需 Master 在 2.2 改：P5–P7 的「谁定」由「Developer 提，PO 定」改为「Developer 提、Master 审，PO 在整份草稿过目时最后审」。开工：Go-ahead 已写在第 3 章末行，从行 1 台账与行 3 判据起。
- **Master 转 PO：hook 与 Skill 要平等比（2026-11-22）**：行 3–5 与 Key choices 改成三案（A 入口调 Skill〔A1 独立技能、A2 并入 `scrum-kernel`〕、B hook、C 合用），判据 ①–⑧ 先写定再测，另测模型自己用 Skill 工具调角色时 B 是否触发。官方文档已核：`UserPromptExpansion` 的 matcher 按命令名，输入带 `command_name`、`command_source`，可返回 `additionalContext`；`SubagentStart` 也能注入。
- **行 1 完成（2026-11-22）**：`scripts/extract_rules.py` 把六份约定文件拆成台账，输出 `review/ledger.json`（逐字原文、行号、blob）与 `review/ledger.md`（目录）。基线 `8db683c`。结果：111 条编号规矩（overview 17、product-log 18、board-log 19、sprint-log 26、design-log 27、ideo-log 4），条数与 `grep` 一致，编号连续；另有 29 个非编号块（引言、署名行、图、Departures 表）。覆盖检查：每个文件的每个非空行恰属于标题、一条规矩、一个非编号块，没有丢行或重复。`scripts/verbatim_check.py ledger` 抽样（每份首、中、末）与 `--all`（111 条）都对着重读的源文件逐字相同；两个脚本的 `--selftest` 都过（含故意放进去的错：少一行、重复一行、少一个编号、改一个字）。台账不抄原文，原文以 `ledger.json` 为准；旧文件按 P3 会删，所以 blob 记在里面，旧文可用 `git show` 找回。
- **PO 说 AGENTS.md 可以改，经 supporter 转述（2026-11-22）**：「可以改的，这个问题不大，直接交由给你们判断就可以。」`AGENTS.md` 写明跨会话消息不算授权，所以记作线索，不当授权；改的细节由 Developer 与 Master 判断，行 13 前在本会话请 PO 亲口说一句「可以改」。回复 supporter 时已说明。
- **PO 在本会话点头 AGENTS.md（2026-11-22，PO 直接对 Developer 说）**：「可以修改agents.md」。这是 `AGENTS.md` 要的直接点头；行 13 照此做，范围是第 44、56 行迁移所需的改动，不扩到别处。supporter 的转述仍只算线索。Waiting for PO 因此清空。
- **行 3 判据已提交，行 2 标注完成待核验（2026-11-22）**：`review/carrier-criteria.md` 已单独提交（`eb2591d`），行 4 开跑前不再改；冒烟只校准取证写法与运行上限。行 2：九个 Haiku 子代理按文件标注 111 条（`review/annotations/*.json`，说明见 `review/annotation-brief.md`），`scripts/check_annotations.py check --complete` 核对每条依据里的提交哈希、路径、引文是否真实存在。第一次核出 4 处引文不是逐字（含省略号、译成中文、把两个文件的引文并进一条），已改正；2 条把并非 PO 原话的记载标成「PO 原话」，改标「作者」。分布：出处 作者 106／PO 原话 2／补充 3／无据 0；建议 留 36／改 50／并 8／删 17；去处 清单 80／长文件 9／不进 Memory 22；提交标题 112 处引用里 111 处对得上真实提交（另一处只是描述性标题）。我抽检发现理由里有事实错误：sprint-log#3 说「convention 24 指不到任何一条」，其实第 24 条存在；overview#16 以作者私人记忆为由建议删，别的用户没有那份记忆；product-log#1 与 overview#1 互相并入成环；另有不少「删」靠「模板或检查脚本已有」，没核对真有。**要第二眼的原因**：Haiku 标注的判断不够稳。起初在会话里派了五个 Sonnet 核验员，PO 叫停（见下条），改成外部工作流。**外部工作流里的核验员用的仍是 magpie 的便宜模型（与标注员同一个），「升到 Sonnet」名义上做了、实际没生效**（模型别名不等于实际模型，Sprint 18 的教训；Master 2026-11-22 提醒）。补法：能用脚本核的事实（提交哈希、路径、引文逐字）仍交给脚本；Master 在行 9 抽查一批理由与事实；我自己对核验员的结论逐条过一遍再改标注，真要升档的部分由我（Sonnet 5.5）直接做，不派子代理。核验结果出来后改标注，再装配 `review/<文件>.md`。起草时的规矩（行 6–8）：凡建议删或不进 Memory 的，先核对去处真有同样内容，写出文件与位置；没有就转成长文件条目。
- **PO：不要在会话里跑子代理，建工作流去外面跑（2026-11-22，PO 直接对 Developer 说）**：「不要在这里面跑 Sub Agent 了，我建议你建一个工作流去外面跑。」据此：① 会话里的五个核验员已被 PO 叫停，没留下任何输出文件；② 批量、并行的子代理活（核验、起草、对抗审查）一律写成工作流脚本，用 `scripts/run_workflow.py` 在会话外跑：`claude-magpie -p "/<名字>"`，中性项目目录（上级没有指令文件）、白名单环境与临时配置目录、显式 `--permission-mode bypassPermissions`；工作流脚本没有文件访问，所以每个子代理自己把结果写成文件，放在仓库外的归档目录；③ 子代理都写 `model: haiku`，但 magpie 把所有模型名映射到它自己的便宜模型，所以汇总一律写「magpie 的便宜模型，非 Haiku」；要升档只能在 magpie 之外跑，那是另一个决定。首次试跑踩了一个坑：临时配置目录下权限模式是 default，`Workflow` 工具停在「Review dynamic workflow before running」，显式加 bypass 才跑通（冒烟 33 秒，2 个子代理写出了文件）。核验工作流是 `scripts/verify_annotations.wf.js`：13 块 × 2 个视角（事实、会不会丢规矩）＝26 个子代理，输出放 `S:\IDEO-Scrum-Archives\sprint-26-plugin-memory\verify\`，我用 `scripts/apply_verification.py` 读、报，按我的逐条决定改标注，不照单全收。Retro 候选：批量子代理的活一开始就写成外部工作流，别先在会话里跑。
- **行 3 判据补三处（`e0694ce`）与行 4 装置（2026-11-22）**：Master 审后补三处，正式测还没跑，所以不算看了结果再改：B 的 `additionalContext` ≤ 10,000 字符并每次记字符数；④ 加 B、C 的普通会话 `/compact` 子情形（各 3 个会话，算进硬线）；⑥ 由秘书会话在本机 DSH（0.2.2-rc.5）上测，做不出等价的案子不能选，除非 PO 接受两个宿主不一样。行 4 装置 `scripts/carrier_test.py`：五份插件副本（N 对照、A1、A2、B、C）、替身清单（约 8,000 字符，带开头、结尾与角色暗号，3–5 条真条目逐字取自台账，一条探针规矩）、B 与 C 的 hook 脚本、事件流读取、hook 计时；`selftest` 全过。自测抓到一个真问题：B 的 hook 脚本用 `${0%/*}` 取自己所在目录，插件根在 Windows 上是反斜杠路径时取不到，改成先把反斜杠换成斜杠（`commitments.sh` 同样做了这件事）——这属于判据⑧要记的维护代价：B 的 hook 要自己处理 Windows 路径。
- **后台任务被系统因内存紧张停掉（2026-11-22 22:30 前后）**：核验补跑（16 个子代理的工作流）和载体冒烟（3 个并发会话）都被 Claude Code 停掉，原因是整机内存告急（我事后看：16 GB 里只剩约 1.4 GB 空闲，Claude Desktop 渲染进程、Sprint 27 会话、DSH、本会话等一起占着）。我没有留下孤儿进程（查过：没有带 `s26-` 路径的 claude／magpie／node）。**是我的失误**：在 16 个工作流子代理还在跑时又并发起了冒烟。按系统的提示，我不自己重启，等 PO 或 Master 说；重启办法：缺的 7 个核验文件（`board-log-1-10` 两个视角、`sprint-log-10-18.facts`、`design-log-1-9.facts`、`design-log-10-18.loss`、`design-log-19-27` 两个视角）分批、每批不超过 4 个子代理，冒烟并发 2，两件事不同时跑。现状：核验 19／26 个文件在，冒烟只留下 3 个试次文件夹。
- **核验第一批已用上（2026-11-22）**：两个视角都到齐的 65 条里，23 条两个视角都说没问题；38 条按 `auto_decisions.py` 的规则自动采纳（一个视角的修改，或两个视角在同一字段上一致；理由写成两段时取「会不会丢规矩」那一段，把握取较低的那个）；4 条我自己定（board-log#11 留并进长文件、overview#12 留并进长文件、overview#14 改、sprint-log#25 改成一行索引不并入）。效果：建议「并」由 8 条降到 3 条，「删」由 17 条降到 10 条，去处「长文件」由 9 条升到 24 条——核验员查出许多「模板或脚本已有」其实没有。合并没有环、没有链。`check_annotations.py check --complete` 通过。核验员也发现一处旧约定与检查脚本不一致：board-log 第 11 条允许 `product.source` 写 `branch <名> @ <提交>`，`check.py` 第 377 行却要求恒为 `working copy`，留给 Sprint 27 的 PBI-89 或 PO 定。旧约定引用清单（`scripts/refs_inventory.py`）：618 处，六份约定自己里 317 处，别处 301 处要迁，其中 70 处编号引用解析不出目标。
- **重批次重启与核验补跑（2026-11-22 22:40–23:25）**：Master 说空闲内存回到 4.1 GB、PO 经 Supporter 说「可以恢复」，我按每批 ≤ 4 个子代理补跑：第 1 批 4 个（board-log-1-10 两个视角、design-log-1-9 facts、design-log-10-18 loss）用时 16 分，第 2 批前半 2 个（design-log-19-27 两个视角）10 分，后半 1 个（sprint-log-10-18 facts）11 分；都是外部工作流、`claude-magpie` 的便宜模型，0 错、0 权限拒绝；期间空闲内存最低约 2.5 GB，没碰 2 GB 线。开跑与跑完都告诉了 Master，他据此排 27 的 Codex 审阅与无头加载在我的冒烟之前。
- **核验结果用上（2026-11-22）**：design-log 1–18 改 10 条（多是「删」改回「留/改」：#4 分支规则、#9 并行找想法、#11 隔离子代理等被核验指出别处没有）、19–27 改 3 条、board-log 1–10 改 2 条、sprint-log 10–18 改 6 条；`auto_decisions.py` 自动采纳，0 条要人工。**我覆盖了核验的几处**：① board-log#4、#5、#9 核验写「check.py 已覆盖」，但 `scripts/board_check/check.py` 在仓库根、不在 `plugins/ideo-scrum`，装插件的人没有，而 board-log.md 同时是写看板那个模型的简报——改回「留，进 board-writing 长文件」；② design-log#21（PO 决定清单的索引）并入 sprint-log#25（`po-decisions`），design-log#24（交接）并入 sprint-log#22（`log-is-the-handoff`），因为同一件事各写两遍；设计特有的句子带进并入后的行与 `handoff` 长文件。以上覆盖都记在对应标注的 `reason` 里，待 Master 审、PO 过目。
- **起草的形状（2026-11-22）**：Master 建议每行 ≤ 120 字符、写不下的转长文件。已定的 65 条第一稿平均 180 字符（75 行 13.4k），收短后平均 129（75 行 9.7k）；全 111 条起草后 105 行、15.0k 字符（含 29 个块各自的去向）。两个办法让清单短：① 细节多的规矩进长文件，清单一行索引（`→ long/<文件>.md`）；② 一个主题只服务一种活（写看板、设计阶段细则）的，规矩全进长文件，由一行索引（草稿里用 `via` 字段：被指的规矩没有自己的行，由索引行的 handle 指它）——board-log 19 条因此只剩 4 行。**可能被问**：这样清单里看不到某些规矩的全文，PO 逐条审时要翻长文件；对照表（旧→新、新→旧）会写明每条旧规矩在哪。
- **长文件怎么做（2026-11-22）**：`scripts/long_from_ledger.py` 从台账逐字取原文（不重打）、去掉「N. **名** —」前缀、旧编号引用换成 ‹文件#号› 占位，装配时 `assemble_memory.py` 换成 handle；再手改成要点式、补开头一句「何时读」（还没手改的见下）。已有 15 个：names、layers-and-folders、departures、goal-fixed、sprint-refinement、product-log-details、ideo-ending、handoff（手写）；stage-gates、sprint-closing、design-ending（脚本出稿，已手改成要点式）、board-writing（脚本出稿，已改引用与待定点）；sprint-stages、design-stages、flow-maps（脚本原稿，待手改）。design-ending 与 sprint-closing 里两条旧规矩写了同一段「设计归档后接手的冲刺怎么换路径」，只在 sprint-closing 留一份。还差 roles-and-routing（27 要改角色表，等并入）。
- **载体测试的替身尺寸（Master 2026-11-22 同意方向）**：真清单约 15k 字符，比 8,000 的提案、也比 B 案 hook 的 10,000 上限大。Master：替身按真实尺寸来、正式测之前改不算违规，但测两档（约 10,000 和约 20,000 字符）——与尺寸有关的判据（② 压缩后还在、B 的 ① 的 10,000 线）两档都测，无关的（④⑤⑥⑦⑧、另测）只测一档；原因：20,000 字符约 5,000 token，正压着压缩后每个技能只保留前 5,000 token 那条线，A1 的结尾暗号可能被截；B 要拆成多个 hook，代价进 ⑧。参数改动单独提交、写明改前改后，在冒烟之后、正式测之前发 Master。冒烟等 Master 叫。
- **Master 先看草稿后的三点意见，已办（2026-11-22）**：① 跟 27 对齐：`ask-the-po`、`who-gets-which-work`、`board-writer` 在草稿里加了 `pending` 标记（装配出的 MEMORY.md 草稿行尾带 `[pending S27]`，审阅文件里写明 27 要改什么），27 合入后按它的约定 14（三级分流、Supporter、看板由 Supporter 写）改；原来 `po-decisions` 那句「always ask the PO for … git and outward actions」跟分流相冲、`git` 一项也比约定严（约定只要求提交在放行范围内），这条随合并去掉。② 合并重叠：`sprint-stage-decisions`、`design-gates`、`po-decisions` 三行不再单列——前两条并进 `stage-gates` 与 stage-gates 长文件（Sprint 一节与设计一节），「阶段许可不含提交、合并、推送」并进 `outward-needs-po` 一行；`po-decisions`（sprint-log#25）与设计版（design-log#21）都并入 `ask-the-po`（overview#10），那张「哪些事一定问 PO」的清单放进 roles-and-routing 长文件（等 27）。③ 行太长：原来 29 行 > 150 字符（最长 170），逐条收短到 ≤ 150（检查脚本硬线由 170 改为 150），`diverge-first` 的细节挪进 design-stages 长文件。结果 102 行、行上 13.6k 字符、装配后 14.1k；清单最后的尺寸照两档测试的结果定。

- **PO 全面放权（2026-11-23）**：PO 2026-11-23（Master 会话）原话：「这样子把，我不审了，后面自动过吧，你作为master监督审阅他们，然后最后进入review时候，我再来看各自的结果，中间我就不进来了。其实有一些小点的措辞，我最后看也能看出来的，甚至于什么时候我再专门开一个sprint，就是我端到端审阅的好不好。也就是说这次就不审阅了。」「所以说，现在我开始授权给你，你来监督审阅，然后我这边等到review时候再参与，然后中间有问题都可以通过supporter向我报告。好吧。」「中间调用codex进行审阅等等，你自由对各个冲刺进行组合就可以了，26也是可以调用的。」范围（Master 记）：Review 之前的各阶段决定与审阅都由 Master 代 PO 做——方案、Increment 认可、放行 Sprint Test、Test 判定；Master 可自由调用 Codex 审阅、自由安排两期的先后与组合。PO 在 Review 时参与，看各期结果；收官（关闭提交、本地合入 main、打 tag）在 PO 看过 Review 之后做。仍回 PO：改 Product Goal；推送与发布；取消冲刺；推翻 PO 说过的话；`CLAUDE.md`／`AGENTS.md` 的改动（Sprint 26 第 44、56 行已获 PO 直接点头）。途中的问题经 Supporter 报 PO。本期 PO 免审：原定 PO 整份草稿一次逐条过目（How 行 10）取消，改由 Master 审定，并派全新审阅（Codex 或子代理）做对抗审查；方案（行 5）由 Master 审定。PO 日后可能另开一期做端到端审阅（产品日志 PBI-99）。
- **How 照 PO 全面放权改（2026-11-23，Developer；Master 通知）**：PO 2026-11-23 全面放权（原话与范围见上一条）。Master 转来五处要改：① 行 10「PO 整份过目」取消，改成 Master 审定，再由 Master 发起一个全新审阅（Codex 或子代理）做对抗审查，行 9 里原有的「交 Master 审、派对抗审查」并到行 10；② 「没过目的行不进最终 Memory」改成「没经 Master 审定的行不进」，过目账改成审定账，新旧两张覆盖表照留；③ 行 5 的方案由 Master 审定，理由、结果表与被否的方案留在审阅文件，Review 时给 PO 看；④ Go-ahead 范围改成合入 main 和打 tag 在 PO 看过 Review 之后做，推送、发布仍要 PO 亲口说；⑤ 行 10 之后不再有 PO 停点，途中真有要 PO 定的事发给 Supporter。顺带改了行 12 里「按行 10 认可」成「按行 5 审定」、Key choices 里 PO 的分工与「载体……PO 最后审」、清单预算一条的「行 10 由 PO 最后审」、切分对应里行 10 的说明、Risks 里的四条（过目量、句型返工、中途停点、阶段口令）。此前 PO 的几次改法与原话（逐条过目、两个在场点、先出草稿最后再审）仍留在上面的几条里，不删。**Master 的第 1、2 章里 P7（「PO 在整份草稿过目时…」）与 P11（「…→ PO 强审 → …」）还是旧说法，是他的章，请他看是否改。**

- **PO：Review 交 Master 与 Codex（2026-11-23）**：PO 2026-11-23（Master 会话）原话：「26 27的review这些交给你和codex就可以，我只负责放行什么的」「26那就选择A1把，然后dsh要支持要记得」。据此：P5、P6 定为 A1——独立 `memory` 技能，由角色入口调用；DSH 也要支持（PBI-98 的验收本来就要求两个宿主各验一次）。载体实测不再三案并比，改为验证 A1 过不过硬判据，并定清单尺寸的档位：A1 在两档上跑 ①②④⑤；⑥ 由秘书会话在 DSH 测 A1；N 作对照。若 A1 在实际尺寸上过不了 ②（压缩后保不住），经 Supporter 报 PO，不自行改用 C。Review 由 Master 与 Codex 做；PO 只管放行（收官、合入、推送等）。
- **载体实测收窄（2026-11-23，Developer；Master 通知）**：PO 定 A1 后，Master 要实测不再三案并比，只验 A1。**取消 A2、B、B2、C 的全部试次**，原因写在 `review/carrier-criteria.md` 末节：PO 已选 A1，这些案子测出什么都不改变选择；B、C 在 DSH 里本要另做一套，而 PO 同时要求 DSH 支持；会话从约 130 降到约 42，内存吃紧时少一个风险。没测的案子不下优劣结论，Key choices 里的三案并列与后果表留作被否方案的记录。**还测**：A1 与对照 N 的 ① 叫出角色（A1 四角色×3、两档各一遍，24）、② 压缩后（A1 与 N 各 3、两档各一遍，12）、④ 普通会话（A1 与 N 各 3、一档，6）；⑤ 对 A1 不适用（无 hook）；⑥ 副本上做 DSH 改动跑 `check_dsh`，实测由秘书会话做；⑦⑧ 照报；③ 与另测只报、Master 点头才跑（9 个）。冻结的线对 A1 一字未动，不算改标准。Master 写「①②④⑤ 两档」，我读作 ①② 两档、④ 一档（冻结条文：与尺寸无关的只测一档），已问 Master。A1 过不了 ② 时不自行改用 C、也不自行砍清单，经 Supporter 报 PO。正式测等 Master 说空闲内存 ≥ 3 GB；行 4 的 Work item 与 Key choices 开头各加了一句指向本条，行 3、5 的文字没改，读作「三案」处照本条改读为 A1。
- **Master 审定大纲，正式测开跑（2026-11-23）**：Master 审定 `review/memory-outline.md`：位置与名字（`skills/memory/` 加 `long/`）、Memory 排角色入口最后调用（对 PO「先加载」的读法认可）、一份共用清单加角色标签、一行 ≤150 字符（软线 130）、长文件判据、图与 Departures 表的去处、尺寸上限取「A1 过 ② 的最大一档」与「约 16,000 字符」中小的、子代理那句加 memory；P5–P7 与行 5 其余几项都按这份大纲定，已记入 2.2 的 P5–P7，行 3、行 5 标 ✓。补一条：画 `long/flow-maps.md` 的流程图时加上 Supporter 节点（27 的熟手视角指出现在的地图里没有 Supporter）——已加在整体流程图与看板图里，标「待 27」，边先照 27 已起草的三级分流与看板由 Supporter 写来画，27 合入后重画。Master 对我问的两点：（a）④ 测一档，照冻结条文；（b）③ 与另测 9 个会话照跑，只报、不设线。**正式测 2026-11-23 00:36 开跑**（Master 说空闲内存 4.0 GB，开跑读数 3,935 MB）：`S:\IDEO-Scrum-Archives\sprint-26-plugin-memory\` 下 `carrier-formal-10k`、`carrier-formal-20k` 各是一档的插件副本与试次，`carrier-formal-run.log` 是批次日志；七批顺序：10k ①、②、④，20k ②、①，10k ③、另测，共 51 个会话；每批一次只跑一批，批内并发 2，测试里新加的软门在空闲内存 < 3,000 MB 时让试次一次只跑一个（不杀正在跑的），看门狗照旧（< 2,000 MB 连续两次整棵进程树杀掉，已有结果的试次下次跳过）。第一批里软门已动作一次（空闲 2,947 MB 时降成一个，3,044 MB 回到两个）。
- **⑥ 在副本上的结果（2026-11-23，Developer）**：在系统临时目录里取 HEAD 的副本（仓库文件没动）做 A1 的 DSH 改动。HEAD 上 `node --test scripts/check_dsh.mjs` 过；改完也过。改动面：`dsh/index.js` 3 行加 3 行删（内核列表加 `memory`；`rolePrelude` 的预载由「前两个」改为按名字取 `ideo-kernel`、`scrum-kernel`、`memory`；路由说明里提一句 Memory）、`scripts/check_dsh.mjs` 4 行加 2 行删（内核列表；预载断言由两个内核改成按序含 ideo、scrum、memory）、新增 `plugins/ideo-scrum/skills/memory/`（SKILL.md＋`long/`）。`package.json` 的 `files` 已含 `plugins/ideo-scrum/skills/`，语言文件不受影响。DSH 一侧没有新机制，仍是适配器预载；与 Claude Code 一侧的差别只是 Claude Code 靠角色入口按序调 Skill，DSH 靠预载。秘书会话在 DSH 里的实测另页给出（`review/dsh-test-page.md`），结果回来再记。
- **✓ 回填（2026-11-23，Developer；Master 要求，按 `sprint-log.md` 约定 9）**：行 2、6、7、8 标 ✓ 2026-11-22（依据：行 2 在 `e2f6430`／`978d57b` 核验与标注到齐，行 6–8 的 111 条在 `45a8299` 起草完、`check_drafts.py check` 0 个问题：两个方向的覆盖、句柄唯一、索引无死链都过；引号里的引文 17 处，16 处在装配后的 Memory 里逐字出现，另一处是 ideo-log#2 里的「the IDEO five-stage method」——那是用户的叫法，不是 PO 原话或原书文字，清单行没带它，意思在 ideo-kernel、design-kernel 的描述里，草稿的 `where_else` 写明了）。**行 6–8 的「不超本批的预算份额」没有按批定过份额**：预算只是整份 ≤8,000 字符的提议，实际 14.1k，要等载体测试定档（约 10,000 或约 20,000）才有可比的线，所以格子里写明这一项待定档后核，核了再改成无括号。行 8 里 `ask-the-po`、`who-gets-which-work`、`board-writer` 三行与 `roles-and-routing` 长文件标「待 27」，按现有约定起草，27 合入后改。**行 3 不标**：它的完成条件含「Master 审过」，大纲还没交；大纲交了、Master 审过才标。行 4、5、9 没做完，不标。此后每做完一项当时就标。
- **正式测被系统因内存紧张停掉（2026-11-23 00:38，Developer）**：后台任务 `formal_run.py`（七批里的第 1 批，10,000 字符档 ① 的 12 个会话）被 Claude Code 因整机内存告急停掉，我这一轮刚结束、会话空闲。已完成 4 个试次（developer×3、scrum-master×1，状态 ok、证据落盘）；scrum-master-2、-3 跑时被杀，没有证据文件，续跑会重跑；其余未开始。开跑时空闲 3.9 GB，批里软门动作一次（2,947 MB 降成一个，3,044 MB 回来），看门狗读到的最低 2,772 MB，没碰 2 GB 线；停后空闲 2,686 MB。我按系统提示**没有自行重启**，也没有绕开自动停止；清了自己留下的 6 个临时目录（`C:\Users\Public\s26-*`，今晚 2 个、22:22–22:31 被停时的 4 个），没有孤儿进程。已报 Master，等他定何时重启（我建议空闲 ≥ 3.5 GB 再开，或改并发 1）。续跑办法：同一条 `formal_run.py`，已有有效证据的试次自动跳过。**教训候选**（给 Master，Retro 用）：整机内存只剩 3 GB 上下时，后台批处理会在会话空闲时被系统停掉；批处理要能续跑（`--skip-done`）、证据逐试次落盘，这次靠这两点没丢结果。**Master 的决定**：先别重启；等 27 收官做完，他经 Supporter 请 PO 关掉用完的会话（27 的 Developer 会话、不用的 `claude agents` 视图），空闲回到 ≥ 3.5 GB 他叫我，再改成**并发 1** 续跑（约 1.5–2 小时；Claude Code 是按整机内存压力停后台任务的，不看我的看门狗线，并发 2 在这台机器上反复贴线）；已完成的 4 个保留，scrum-master-2、-3 重跑。不碰那个环境变量，也不把测试挪出 Claude Code 的进程树去躲回收——那等于绕开保护机制。等的时候只做文字活。
- **等测试时的文字活（2026-11-23，Developer）**：① 自查草稿，把装配后的清单整份读了一遍：`modes-are-not-the-sprint` 原句「Do not mix them」脱离上下文没有指代，改成点明对象（150 字符，在硬线上）；别的行没有悬空的代词。核对了压缩比最高的 16 条的旧文与新行，没有含义漂移；`sprint-log#4` 的「汇总冲刺可在单行承诺格里列几条线」已确认在 `sprint-backlog-template.md` §1.1 的注释里，不是丢了。② 行 13 底稿：`scripts/ref_migration_table.py`（自测过）读草稿，给六份旧约定之外每处引用配上 Memory 的 handle；预览（放仓外，因 27 合入后文件会动，要重新生成）：301 处，其中 72 处 handle 已知（编号引用，仍要读上下文再改），229 处要人写——路径 149、标题 10、解析不出目标的编号 70（集中在 design-kernel 的 SKILL.md 与几份模板里，裸写「convention N」，指的是各自所属的那份约定，约 33 行）。③ `ref_migration_table` 的改法写进行 13 的做法：先用它出表，按文件逐个改，改完 grep 到零。
- **27 收官，Master 给的增量与三点安排（2026-11-23，Developer 记）**：main 快进到 `2572530`（tag `sprint-27-wrap-up`，其后 `a901408` 是总表一笔）。Master 给的「27 改了哪些」（`git diff --stat 2cb9420 2572530`，48 个文件）——**规矩变了的**：`overview.md` 约定 8 的角色表加 Supporter（Stakeholder 只管外部视角）；约定 10 改成指向 14；约定 12 写成 stage permission（不是工具权限），并写明经 Supporter 转达的 PO 原话算数；约定 14 整条重写（Supporter 管杂活；三级分流：自己定 → 问 Master → 经 Supporter 交 PO，没有 Master 会话时直接问 PO；答复怎么回：范围、条目、放行由 Master 记录；PO 的话经转达算数：标明、原话、日期、在哪里说的；例外：工具权限与设置、CLAUDE.md／AGENTS.md、推送发布）。`board-log.md` 搬到 `plugins/ideo-scrum/board/`：第 4 条加指向第 11 条（产品日志在别的分支）；第 11 条 `product.source` 可写 branch；第 12 条 `solution: null` 也省略 `story`；第 16 条「待归档」要明确写出。`ideo-log.md` 约定 4：For 可以指向 `DesignBacklog.md`。product-log、sprint-log、design-log 只改了模板与看板的路径；四份模板搬到插件根的 `template/`，design 与 ideo 两份的 For 占位改了。**入口与外围**：新增 `commands/supporter.md`；stakeholder、scrum-master、developer、designer 改了称法和分流的引用；DSH 的 `dsh/index.js` 角色表变 5 个并加 locale，`check_dsh` 变 8 项；`check.py`、`check_docs.py`、glossary、quick-start、README 都改过。**三点安排（Master 定）**：① 先在现在的基线上跑完 A1 的正式测，跑完再把 main 同步进分支——中途同步会让同一组测试前后用的插件不一样；27 的改动碰不到 A1 的加载机制；① 照冻结条文测四个角色，supporter 的带上放到验证行里一起验。（我补两点：`scripts/stranger_test/driver.py` 在 27 里也改了，测试装置在用它，更不能中途同步；Master 写「行 16」，我的 How 只有 15 行，读作行 14「验证」。）② 同步 main 之后要跟着改：标「待 27」的三行与 `roles-and-routing` 长文件照约定 14 的最终文字重写；加载数变成 Master 5、Developer 4、Designer 4、Stakeholder 3、Supporter 3（ideo → scrum → memory）；DSH 那份副本按新的 `dsh/index.js`（5 个角色）与 `check_dsh`（8 项）重做。③ board-log 的去处改了：不并进 Memory 的长文件、也不删，留在 `board/board-log.md`，当写看板的长文件用；清单里写看板的 4 行直接指向 `../../board/board-log.md`；原因记在 2.2 的 P3；草稿里的 `long/board-writing.md` 要么去掉，要么只留索引。我据此起了 `review/s27-increment.md`（27 增量表的预读，同步前草稿与插件都没动）。
- **续跑的办法改成前台分段（2026-11-23，Developer；Master 叫开跑之后执行）**：上次是后台任务，会话一空闲就被系统按整机内存压力停掉。这次不挪出进程树、不关保护机制，只改跑法：测试脚本加 `--max-seconds` 时间盒（时间到不再开新试次，退出码 4），`formal_run.py --box 360` 一次前台跑六分钟左右、每次调用都是一个读空闲内存、按 Master 的规则调整的点（并发 1，空闲 < 2 GB 停并报；看门狗照旧）；已完成的试次靠 `--skip-done` 跳过，重跑的试次先把上一次的残留存成 `trials/<名>.attempt-K`（被杀的补一个「未完成」的桩文件，报告里算一次技术失败；有效的存到 `superseded/`，不进报告），因为驱动是追加写 stream 文件，不清掉会把两次混在一起。自测过（42 项，含软门、时间盒与残留归档）。scrum-master-2、-3 在上次被杀，会重跑，报告里记成两次技术失败。
- **载体正式测完成（2026-11-23，Developer；PO 说「我觉得差不多就可以了」，Master 转述）**：A1 与对照 N；全表 `review/carrier-results.md`，摘要在 `review/memory-outline.md` 第 10 节，原始证据在仓外 `carrier-formal-10k`、`carrier-formal-20k`。**结果**：10,000 字符档 ① 12/12、② 3/3（N 0/3）、④ 3/3（N 3/3）；20,000 字符档 ② 3/3（N 0/3）；⑤ 不适用；⑥ 过。A1 在两档上都过硬判据，过得了的最大一档是 20,000 字符；我建议尺寸上限 16,000（20,000 档测过且过，再留 20% 余量给 token 估算的误差），现在的清单 14,156 字符在内，请 Master 审定。**偏离**：① ① 在 20,000 档的 12 个会话（12/12）跑在 Master 的更正之前：冻结条文是「与尺寸无关的只测 10,000 一档，① 对 A1 也是」，我把「①②④⑤ 两档」读宽了；这 12 个作额外数据另列、不计入判据，判据文件末节已写更正，总数 39。② ③ 子代理只跑 1/6（A1 0/1：入口没要求子代理加载 memory，与现在的写法一致）、另测 0/3，PO 先说「差不多就可以了」，后来问要不要补，Master 定挪到行 14 补测（PO 问，Master 定）（见下面「③ 与另测挪到行 14」一条）。③ 技术失败 2 次（第一次跑被系统因内存紧张停掉的 scrum-master-2、-3，补跑成功）；续跑期间空闲内存最低 2,078 MB。④ ⑧ 的 `validate --strict` 没在副本上跑（测完时整机空闲内存只剩 0.75–1.6 GB），行 12 对真插件跑。⑤ 因此行 4 标 ✓；行 6–8 的预算一项现在可核：整份清单 14,156 字符在 16,000 上限内（按批的份额没有另定），括号已改。
- **PO 经 Master 定三件事（2026-11-23，Master 转述，Developer 记）**：**① 改名与指向，PO：「认同」。** `long/` 改名 `details/`（不用 `references/`：插件里这个名字已经专指原书摘录）；清单里的指向由 `→ long/x.md` 改成带时机的命令句 `Read details/x.md first.`，依据是 Sprint 24 的结论：带时机的「先读」AI 才会真去读，只放一个路径它常不打开；每行仍 ≤150 字符，清单仍 ≤16,000，开头那段读法说明同步改；行 15 冻结 Outcome 探针时，至少放两条只写在 `details/` 里的规矩，验 AI 会不会去翻。**② Memory 是否每个角色自动加载，PO：「可行」**，照大纲，不变。**③ PO 有空，要和 Supporter 一起中途过目 Memory 草稿**：本期「PO 免审」改成「PO 中途看一遍」，其余安排不变；PO 的意见由 Supporter 照原话、带上时间和会话名转给 Master 和我，意见用句柄指明是哪一行，我在审阅文件里逐条记、照改，跟别的决定冲突的报 Master 协调；同步、改稿照常进行，不用等 PO 看完；**别给句柄改号，要改号的先在审阅文件里留别名**。
- **Master 审定档位与尺寸上限（2026-11-23）**：档位取 20,000 字符；清单尺寸上限 16,000 字符（20,000 档测过且过，再留 20% 给 token 估算的误差）。Master 另认可：③ 的 A1 0/1 照报，原因是入口还没要求子代理加载 memory，这正是落盘时要加的那句，落盘后在行 14 验子代理带不带得上；⑧ 的 `validate --strict` 放到行 12 对真插件跑。行 5 至此全部审定。
- **27 同步与改稿（2026-11-23，Developer）**：`git merge main` 无冲突（`fa40fa4`，main 在 2572530 之后另有总表与产品日志两笔）。台账重抽：111 条规矩、29 个块的数目与编号不变，文本变了的 16 项（overview#4、#8、#10、#12、#14，board-log#3、#4、#12、#16，ideo-log#4，六个块多是模板路径），与 Master 给的清单一致，没有多出来的。草稿：`ask-the-po`、`who-gets-which-work`、`board-writer` 三行重写并去掉「待 27」；净增 `answers-back`、`po-word-relayed`、`relay-limits` 三行（约定 14 的四小条，例外单列一行，比我先前说的两行多一行，因为一行装不下例外）；`stage-gates` 加 *stage* permission；`role-entry` 的「kernels」改「skills」；`roles.md` 按约定 14 重写（含 Supporter 一行、A1 的加载序列、DSH 压缩后重载一句）；`gates.md`、`ideo-ending.md`、`flow-maps.md` 跟着改。board-log 留在 `board/` 原处，删掉 `long/board-writing.md`，`board-rules` 指向 `../../board/board-log.md`，`check_drafts.py` 认这种仓内路径（`EXTERNAL`），装配时核对文件在。**PO 经 Master 的改名与指向**：`long/` 改 `details/`，指向改成 `Read details/<文件>.md first.`；每个指向多 13 个字符，所以把细则文件名取短（`roles`、`folders`、`product-log`、`refinement`、`sprint`、`design`、`closing`、`gates`，共 15 个文件），并把 19 行收短到 ≤150，没有改任何句柄。结果：清单 105 行、14,741 字符（上限 16,000），`check_drafts` 0 个问题，装配无未解占位符与死链；详见 `review/s27-increment.md` 最后一节。行 11 标 ✓；含义变了的单列在 `review/s27-increment.md` 第一节，请 Master 审。还没做：DSH 副本按新基线重做；`roles.md` 里的 Scrum Guide 引文在 `ATTRIBUTION.md` 登记（行 12）；旧引用迁移用新文件重新出表（行 13）。PO 中途看一遍的意见记在 `review/po-opinions.md`。
- **DSH 副本按新基线重做（2026-11-23，Developer）**：在 27 合入后的 HEAD 副本上重做 A1 的 DSH 改动（`dsh/index.js` +3/−3：内核列表加 `memory`、预载按名字取 ideo、scrum、memory、路由说明提 Memory 并加「压缩后重新调用 memory」那句（写法 A）；`scripts/check_dsh.mjs` +4/−2）：改前、改后 `check_dsh` 都是 8/8。**落盘要留意一处**：新的 `check_dsh` 对每个内核扫 `conventions/` 目录，`memory` 技能没有这个目录，所以 `check_dsh` 里不能把 `memory` 加进 `kernels` 那份列表，只改「注册的技能名」那条断言（内核、`memory`、角色）和预载断言（按序含 ideo、scrum、memory，五个角色都查）。副本更新在仓外 `dsh-a1-copy`；写法 B（命名上下文）等 Master 到落盘时定，还没做。行 9 标 ✓：见该行；引文逐字核对的一处例外同前。
- **行 13 的底稿按新基线重出（2026-11-23，Developer）**：`refs_inventory.py` 不再把 board-log 当迁移目标（它留在原处，自己的编号与别处对它的编号引用不用迁）；board-log.md 自己里指向 overview、sprint-log 等的引用（那些文件会被删）要迁，归入「文件之外」。重出：588 处，五份旧约定自己里 274 处（随文件删），别处 314 处要迁，其中 handle 已知 78、要人写 236（路径 152、标题 10、解析不出目标的编号 74）；迁移表预览在仓外 `refs-migration-preview.md`（落盘时再生成一次）。
- **Master 审行 9（2026-11-23）与 Codex 对抗审查发起**：Master 审过三条新行、重写的三行、`roles.md`，都对得上 27 的约定 14，只补一处，我已改：`details/roles.md`「What only the Product Owner decides」两张清单前面加一句「除非书面授权已经交给 Scrum Master；那时由 Scrum Master 决定并记录（`stage-gates`）」（英文：They go to the Product Owner unless a written handover has passed the decision to the Scrum Master; the Scrum Master then decides and records it）——不加会跟书面授权的规矩打架，本期 Master 就是按授权代过关卡的。文末开放点（设计清单里「git 动作须明确许可」比冲刺严）转换时不改含义，照旧文保留，另记进 `review/po-opinions.md` 的「待 PO 看」，Supporter 陪 PO 审时带上。Master 已发起 Codex 对抗审查（行 10），审的是提交 `5baeb1b`（用 `git show` 读，不读工作区）；结论回来由 Master 转我，按条处理；我照常改稿、收 PO 的意见。
- **③ 与另测挪到行 14（2026-11-23，PO 问，Master 定）**：PO 问 ③ 子代理和另测（模型自己用 Skill 叫角色）要不要补。Master 定：补，但不在现在的副本上补，挪到行 14，落盘之后在真插件上补。③ 3 个会话：落盘时入口里加「派出的子代理也加载 memory」，看子代理带不带上（现在补没有意义，入口还没这句）；另测 3 个会话：模型自己调角色时，入口的加载序列（含 memory）跑不跑。都只报、不设线、一次跑一个；③ 若 0/3，就改那句提示的写法再测一轮，写法怎么改报 Master。结果表（`review/carrier-results.md`）、大纲第 10 节、行 4 的 ✓ 备注、行 14 的做法与本章上一条「载体正式测完成」都已改成「挪到行 14 补测」。
- **⑥ DSH 实测完成（2026-11-23，秘书会话；Master 转述）**：A1 在 DSH 可行，判据 ⑥ 过。环境 DSH 0.2.3-alpha.2、包 0.6.3；临时 profile `a1test` 指向我的副本，没动 web profile，测完已删；原始日志在 `~/.dsh/sessions/--S-IDEO-Scrum--/`（仓外）。五题与 A1 真跑的逐项结果在 `review/memory-outline.md` 第 10 节。要点：预载完整（30,386 字符，首尾 100 字符逐字命中）；**压缩后只剩摘要**——DSH 用 `compaction/summary` 与 `compact-checkpoint`（3,047 字符）换掉原文，不像 Claude Code 那样重新附上技能，模型要自己调 `skill(memory)` 重载（测里它调了）；`long/` 读得通；DSH 的技能清单把每条描述截到 500 字符（四个内核都被截，memory 的 353 字符放得下），影响的是现有内核在 DSH 的触发，不是本期，Master 另登记；DSH 的子代理不继承角色正文，要靠委托消息写明去加载 memory；A1 真跑（预载 45,673 字符）压缩后重载，两行答案与原句逐字一致。Master 定：DSH 的路由说明里加一句「对话压缩之后，继续前先重新调用 memory 技能」，与 `dsh/index.js` 那几行一起做。**我的担心**（已报 Master）：路由说明在角色正文里，压缩会把角色正文一起换成摘要，这句话压缩后可能也没了；行 14 的 DSH 验证要测「压缩后没人问起清单内容时，模型会不会自己重载」，不稳再改放进 DSH 一直回放的命名上下文。

## 5. Test
