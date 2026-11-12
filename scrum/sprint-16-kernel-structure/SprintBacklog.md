# Sprint Backlog — Sprint 16 (kernel-structure)

> Started: 2026-11-12 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `sprint-16-kernel-structure`（Developer 的原生 worktree） | Product Owner: SeaPawn | Scrum Master: IDEO # [master]-[main]-[start sprint] | Developer: IDEO # [developer]-[sprint-16]-[执行冲刺]
> How to write this log: `sprint-log.md` in the scrum-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled later; add none — remarks go in chapter 4, Increment notes (`overview.md`, convention 16).

**委托**（sprint-log 第 8 条）：PO 2026-11-12 把 Sprint 16、17 全权交给 Master：审 How、审新结构、审全文，以及各阶段结束时的决定，都由 Master 做；只在三处停下等 PO——① 两个冲刺的 How 都审过后，PO 一起放行（放行范围可以到推送和更新本机插件，PO 已同意）；② PO 整份读 Sprint 17 的约定审阅稿，排在最后一轮流程测试之前；③ 最后 PO 亲手试一次，之后 Master 发版 v6.0.0、推送、更新本机插件。改 Sprint Goal 或 Product Goal、取消冲刺，仍由 PO 定。平时只在卡住时报告 PO。

**两个冲刺并行**：本冲刺改结构和加载，Sprint 17（`sprint-17-conventions-rewrite`）改约定内容，各有一个 Developer 会话。本冲刺先合入 main；Sprint 17 先在自己的文件夹里写全文审阅稿、不碰插件，等本冲刺合入后从新的 main 搬进插件。两个冲刺各自收官、打 tag；版本号本冲刺不动（仍 5.2.0），v6.0.0 等两个冲刺都做完一起发。Master 与 Developer 用跨会话消息联系，长的审阅写在 plan 文件里、消息里只给路径；派子代理一律显式写 `model: haiku`。

## 1. Why

### 1.1 Sprint Goal

**结构统一、按需加载**：四个内核各是一个技能，下面带几个文件夹；IDEO 和 Scrum 每个角色都加载，设计和冲刺用到才加载；打开技能就知道该读哪份。

（Master 照 PO 的写法代拟；PO 2026-11-12 看过拆分表里的这句草稿，说没问题。开冲刺前核对了 Product Goal「优化现有插件」：在目标之内——sprint-kernel 是从 scrum-kernel 拆出来的，不是新功能。）

### 1.2 Definition of Done

- 内容忠实：原文摘录（Scrum Guide、SGEP、《Sprint》、d.school）逐字不变，只挪不改；约定的条文只改路径和加载说法；署名照 ATTRIBUTION.md。
- 可导航：从每个技能的 SKILL.md 入口 ≤2 跳到达它的任意文件。
- 无死链：插件和 Codex 包里所有内部链接和路径都解析得到。

Master 2026-11-12（PO 委托）：Sprint Goal 定。

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-44 | 内核结构统一——四个技能形状一致 | 作为熟手，我想要四个内核形状一致、打开就知道里面有什么、什么时候读哪一份，以便不用自己理清结构 | 插件：四个技能 | L |
| PBI-57 | 加载分层——角色全加载 IDEO 和 Scrum，按需加载设计冲刺与 Sprint | 作为熟手，我想要每个角色都完整加载 IDEO 和 Scrum，设计和冲刺用到才加载，以便上下文只装当前要用的东西 | 插件：四个命令、overview 第 8 条 | S |
| PBI-52 | 白纸入口——新想法、还没有产品日志时带到设计 | 作为陌生人，我想要说出「我有个想法、还没有产品日志」时，插件就把我带到先开设计、由设计结论去填产品日志这条路上，以便不会一上来就硬写产品日志或直接出方案 | Map ①（装插件，开会话） | S～M |
| PBI-25 | 插件小修集合 | 作为陌生人，我想要单独装上的插件里链接、署名、触发句和标题层级都对，以便不被死链和过时的说法误导 | 插件文件 | S |
| PBI-46 | Codex 版后续小修 | 作为熟手，我想要 Codex 包的同步和说明再顺一点，以便以后每次发版重跑同步都不用多想，陌生人在 Codex 里也能起步 | Map ①（装插件，开会话） | S |

### 2.2 Refinement

**选入**（照抄产品日志 3.1，对照 Sprint Goal 查过够不够——PO 2026-11-12，PBI-54 ④）：44、57 是目标本身；52 让白纸的话也读到该读的那份；25 带 ①②⑥⑦⑧——要挪的文件反正要碰；46 带 ①④——同步脚本要跟着四个内核改，④ 是命令描述，和本冲刺的触发测试一起跑。25 ③、46 ②⑤⑥ 不在这两个冲刺里，留在产品日志；46 ③ 在 Sprint 17（PO 同意的拆分）。

**定案**

- 布局（PBI-44，PO 2026-11-12）：
  - scrum-kernel：`SKILL.md`、`overview.md` 留在根目录；`assets/` 放 `scrum-guide-2020.md` 和 SGEP；`conventions/` 放产品日志的约定和模板；`references/` 放四个工件。
  - sprint-kernel（新）：`conventions/` 放冲刺日志的约定和模板；`events/` 放从 `references/` 挪来的五个事件。
  - design-kernel：五个阶段文件夹合成 `steps/`，16 份文件名带「阶段-步骤」序号，如 `1-1-define-the-challenge.md`。
  - ideo-kernel 的 `conventions/` 连同内容由 Sprint 17 建（PBI-56），本冲刺不建。
- 引用写法（`convention N`、`../` 路径）不改，只把路径改对（PO 2026-11-12）。
- 加载（PBI-57，PO 2026-11-12）：每个角色——包括 Stakeholder——和派出去的子代理都加载 ideo-kernel 和 scrum-kernel；design-kernel 只在开设计冲刺时加载，sprint-kernel 只在开冲刺时加载；写进四个命令的加载说明和 overview 第 8 条（Roles）。什么时候该开设计冲刺，由 Sprint 17 的 PBI-56 写，本冲刺不写。
- 约定的内容不改：条文、条号和模板的结构都留给 Sprint 17；本冲刺只改路径、加载说法、技能和命令的描述，以及上面选入的小修（Master 定：两个冲刺不改同一处）。
- 新布局的文件清单（每个文件挪到哪、叫什么）先定下来，写进 How：Sprint 17 照它写审阅稿（Master 定）。
- 旧路径：现行的说法全仓 grep 到零——插件、Codex 包、README、CLAUDE.md、产品日志 3.1、两个冲刺的日志；历史记录不改——`scrum/documents/` 里的归档、产品日志 3.2（Master 定，照 CLAUDE.md「已完成 sprint 的内容不回改」）。
- 版本号不动（仍 5.2.0）；v6.0.0 在两个冲刺做完后一起发（PO 同意）。

**验收**

1. 布局：四个技能的文件夹和文件照上面的布局；design-kernel 的 `steps/` 下 16 份，名字照 PBI-44 的规则；挪动的文件 `git diff -M` 认得出是改名。
2. 内容：原文摘录逐字不变；约定的条文只有路径和加载说法变了（diff 逐处看过）。
3. 加载：四个命令和 overview 第 8 条照 PBI-57 写。
4. 路径：插件里所有相对路径和链接都指得到文件，「convention N」都指得到条（脚本核对，0 缺）；改过路径的引用逐处读所指的地方，确认真有那句话；全仓 grep 旧路径，现行的说法 0 处。
5. 校验：`claude plugin validate --strict plugins/ideo-scrum` 通过；对 `.claude-plugin/marketplace.json` 加 `--strict` 也通过（25 ⑧）；结构改了，再派 `plugin-dev:plugin-validator`（`model: haiku`），没有必改项。
6. Codex：`python scripts/sync_codex.py` 后 `python scripts/check_codex.py` 通过，紧接着再同步一次没有差异；脚本适配四个内核；只差换行不算差异（46 ①）。
7. README 的文件地图和说明同步；CLAUDE.md 里指向插件文件的说法改对。
8. 触发测试过线（见下）。
9. 审阅：Master 审；全新子代理（Haiku）对抗审查，必改项清零。

**测试**（跑之前写定，跑后不改；Master 定，PO 委托）

- 判定标准和题目先写、Master 审过、单独提交，再跑；跑后不改标准、不改判；脚本判错的逐条人工看，改判写明理由。
- 测法：无头 `reclaude -p --plugin-dir <插件的 Windows 路径>`（reclaude 不可用时用 `claude -p`，参数相同），Haiku；只开 Read、Grep、Glob、Skill，连 PowerShell 一起禁；工作目录是系统临时目录里新建的空项目，每次一个全新会话；正式跑之前先冒烟。
- 同日同环境：先跑 5.2.0（main 的 `9769bd6`）作基线，改完再跑新版。
- 题目：沿用 Sprint 14 流程测试的题 1–5（题目与判定见 `git show a87bd1c:scrum/sprint-14-conventions-tuning/SprintBacklog.md` 的 2.2；题 3 是白纸）；另加两题覆盖新的拆分——说产品日志的事（该加载 scrum-kernel、读 product-log），说冲刺的事（新版该加载 sprint-kernel、读 sprint-log）。用自然的说法，不带引导词；「读到约定」按各版自己的路径判。
- 两条路径：直接说；从角色命令进入（每题配一个合适的角色）。每题每条路径 3 次。一次回答算过：读到该读的约定、必答项全中、没有「不能」项（Sprint 14 的判定）。
- 汇总分两栏：行为（加载了哪些技能、读没读该读的约定）、内容（必答项中没中）。
- 过线：① 每条路径的行为栏合计，新版不少于基线减 1（留 1 次余量，防基线接近满分，见 CLAUDE.md 回归测试）；② 没有一题从过线（3 次里至少 2 次过）跌到不过线；③ 白纸题（PBI-52）新版两条路径各至少 2/3 过；④ 加载冒烟（新版）：四个命令各 2 次，都加载了 ideo-kernel 和 scrum-kernel，不开设计、不开冲刺时不加载 design-kernel、sprint-kernel。
- 原始输出放 `S:\IDEO-Scrum-Archives\sprint-16-kernel-structure\`，仓库里只留汇总；提交前按提供方地址、凭据值、令牌形态扫一遍。

Master 2026-11-12（PO 委托）：精化到此（Developer 复述，没有疑问）。

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | 测试题与判定写定，送 Master 审 | `scrum/sprint-16-kernel-structure/test-questions.md`：题 1–5 照 `git show a87bd1c:scrum/sprint-14-conventions-tuning/SprintBacklog.md` 的 2.2 取回（必答、不能项照抄；「读到约定」按两版各自的路径写），另写两题（产品日志、冲刺），每题写两条路径的进入说法与判定 | Master 说行；标准单独一个提交，跑后不改；题面不带引导词 |
| 2 | 冒烟：测试工具先跑通 | 冒烟记录（第 4 章）：无头调用成功，模型、空目录、读文件权限都对；四个角色命令各进 1 次 | 冒烟通过；角色命令进不去，就在跑任何正式测试之前把测法定下来并写进第 4 章（这时改不算违规）；`reclaude` 不可用就用 `claude -p` |
| 3 | 拆出 sprint-kernel，两个 SKILL.md 写定 | 新技能 `skills/sprint-kernel/`：`SKILL.md`、`conventions/`（sprint-log、sprint-backlog-template）、`events/`（五个事件）；scrum-kernel 的 `SKILL.md` 去掉冲刺日志两行与事件章、留下一句指向 sprint-kernel；`scrum-guide-2020.md` 挪进 `assets/` | `git diff -M` 把挪动的文件认作改名；scrum-kernel 里没有指向已移文件的路径；sprint-kernel 的描述照组件描述规约写；每个技能从 SKILL.md 入口 ≤2 跳到达自己的全部文件 |
| 4 | design-kernel 合成 `steps/`，全插件路径改对 | 16 份按 `阶段-步骤-原名.md` 改名；design-kernel 的 `SKILL.md`、`design-log.md`、`design-backlog-template.md` 里的摘录路径；`product-log.md` 两处 design 路径；`ideo-kernel/SKILL.md` 的 `prototype/fake-it.md`；跨技能的 sprint-log 路径 | `git diff -M` 全认作改名；插件里旧路径 0 处；`convention N` 全部指得到条（脚本核） |
| 5 | 加载分层：四个命令 + overview 第 8 条 | 四个命令同一段加载说明：ideo、scrum 全加载；design 只在开设计冲刺时、sprint 只在开冲刺时；派子代理也加载 ideo 和 scrum。overview 第 8 条 Roles 表同改；sprint-kernel 的 SKILL.md 写「开冲刺前 scrum-kernel 未加载就先读它」一句 | 四个命令说法一致；overview 与命令一致；加载说法不再散在别处 |
| 6 | 描述与 PBI-25、46 ④ 的小修 | 各技能描述：新写 sprint-kernel 的，scrum-kernel 让出冲刺用词，PBI-52 的白纸说法进 scrum-kernel 与 design-kernel（按场景写，不用题 3 的例子）；25 ① 16 份摘录的许可行改成自足；25 ② **三个** SKILL.md（ideo、scrum、sprint）加 Source/License 头；25 ⑥ 两章与 9 份 reference 先对 `references/scrum-guide-expanded-2025.6.md` 逐句核，再改标；25 ⑧ marketplace 顶层说明；46 ④ scrum-master 简介 | 25 与 46 ④ 逐条落；25 ⑥ 的核对结果写进第 4 章；`claude plugin validate --strict plugins/ideo-scrum` 与 marketplace 的 `--strict` 都通过 |
| 7 | Codex 脚本与包适配 | `scripts/sync_codex.py`、`scripts/check_codex.py`：四个内核、新的加载句子、只差换行不算差异（46 ①）、idempotency 不再写死 `sprint-13-codex` 分支；`codex_interface.json` 的「Three kernels」与 `codex_readme.md` 的文件表；重生成 Codex 包 | `python scripts/sync_codex.py` 后 `check_codex.py` 通过；紧接着再同步 0 变化；只差换行不再算差异 |
| 8 | 文档同步与全仓 grep | README 的文件地图与版本说法；CLAUDE.md 里指向插件的路径；ATTRIBUTION 的位置表（含新 sprint-kernel、`assets/`、`steps/`），并登记 2025.6（原文不收进插件） | 全仓 grep 旧路径，现行的说法 0 处（插件、Codex 包、README、CLAUDE.md、产品日志 3.1；历史归档与 3.2 不动；Sprint 17 的日志由它自己改） |
| 9 | 自检与校验 | 路径与 `convention N` 的核对脚本及结果；插件内部链接核对；两处 `plugin validate --strict`；`plugin-dev:plugin-validator`（`model: haiku`）；`sync_codex.py`／`check_codex.py` | 脚本 0 缺；validator 没有必改项；结果抄进第 5 章 |
| 10 | 审阅 | 交 Master 审；Master 另派全新 Haiku 子代理做对抗审查（验收 9）；必改项清单 | 必改项清零、我的修改已提交；验收 9 写进第 5 章 |
| 11 | 基线：5.2.0 冒烟并跑测 | 冒烟；题 1–7 各走直接说、角色命令两条路径，每条 3 次，共 42 次；原始输出进 `S:\IDEO-Scrum-Archives\sprint-16-kernel-structure\baseline\`；`baseline-summary.md` 两栏汇总 | 冒烟确认模型、空目录、读权限正常；42 次都有原始输出；扫描无提供方地址、凭据、令牌；与第 12 项同一天连着跑（日期用 PowerShell `Get-Date` 看台北时间） |
| 12 | 新版冒烟并跑测、汇总与过线判定 | 新版同样 42 次；四个命令的加载冒烟各 2 次；`new-summary.md`；对照基线的过线 ①–④ 判定 | 过线四条全过，或缺口逐条写明；原始输出进归档、仓库只留汇总；扫描干净；与第 11 项同一天 |
| 13 | 收官准备：Review 与 Retro | 一个提交：日志压缩改名 `sprint-16-kernel-structure.md` 移进 `scrum/documents/`、删中间文件；产品日志保鲜（做完的 44、57、52 移进 3.2，25、46 没做的几项留在 3.1）；Retro 教训写进记忆或 CLAUDE.md | 一个提交；之后由 Master 打 tag、合入 main、关 worktree、删分支；PO 亲手试在停点 ③、两个冲刺一起试，本冲刺不等它 |

**Key choices**

**新布局的文件清单**（Sprint 17 照它写审阅稿）

scrum-kernel（根 `plugins/ideo-scrum/skills/scrum-kernel/`）

| 现在 | 之后 |
| --- | --- |
| `SKILL.md` | 原位，改：去掉冲刺日志两行与事件章、事件表；`scrum-guide-2020.md` 改 `assets/scrum-guide-2020.md`；约定段指向 sprint-kernel |
| `overview.md` | 原位，改：`conventions/sprint-log.md` 等改指 `../sprint-kernel/conventions/`；第 8 条 Roles 表按 PBI-57 |
| `scrum-guide-2020.md` | → `assets/scrum-guide-2020.md` |
| `assets/scrum-guide-expansion-pack-2026.1.md` | 原位 |
| `conventions/product-log.md` | 原位，改：`sprint-log.md` 三处、`../design-kernel/define/*` 两处 |
| `conventions/product-backlog-template.md` | 原位（查有无路径要改） |
| `conventions/sprint-log.md` | → `sprint-kernel/conventions/sprint-log.md`，开头「相对 scrum-kernel」改 sprint-kernel |
| `conventions/sprint-backlog-template.md` | → `sprint-kernel/conventions/sprint-backlog-template.md`，第 4 行指回 sprint-kernel |
| `references/scrum-artifact-{product,increment,product-backlog,sprint-backlog}.md` | 原位（25 ⑥ 若定改出处，只改文件头） |
| `references/scrum-event-*.md`（5 份） | → `sprint-kernel/events/`，文件名不变 |

sprint-kernel（新，`plugins/ideo-scrum/skills/sprint-kernel/`）

| 文件 | 内容 |
| --- | --- |
| `SKILL.md` | 新写：描述、开头一段、约定表两行（从 scrum-kernel 逐字挪）、事件章与事件表（逐字挪，路径改 `events/`）、一句指向 scrum-kernel |
| `conventions/sprint-log.md` | 从 scrum-kernel 移入 |
| `conventions/sprint-backlog-template.md` | 从 scrum-kernel 移入 |
| `events/scrum-event-sprint.md`、`-sprint-planning.md`、`-daily-scrum.md`、`-sprint-review.md`、`-sprint-retrospective.md` | 从 scrum-kernel/references/ 移入 |

ideo-kernel：原地不动，`conventions/` 由 Sprint 17 建；只改 `SKILL.md` 里 `prototype/fake-it.md` 一处路径。

design-kernel：`steps/` 按 SKILL.md 五阶段表的摘录顺序编号；`pick-a-target` 不在表里（白纸收官用），排 Define 末。

| 现在 | 之后 |
| --- | --- |
| `empathize/define-the-challenge.md` | `steps/1-1-define-the-challenge.md` |
| `empathize/start-at-the-end.md` | `steps/1-2-start-at-the-end.md` |
| `empathize/ask-the-experts.md` | `steps/1-3-ask-the-experts.md` |
| `define/make-a-map.md` | `steps/2-1-make-a-map.md` |
| `define/how-might-we.md` | `steps/2-2-how-might-we.md` |
| `define/pick-a-target.md` | `steps/2-3-pick-a-target.md` |
| `ideate/remix-and-improve.md` | `steps/3-1-remix-and-improve.md` |
| `ideate/sketch.md` | `steps/3-2-sketch.md` |
| `ideate/decide.md` | `steps/3-3-decide.md` |
| `ideate/rumble.md` | `steps/3-4-rumble.md` |
| `ideate/storyboard.md` | `steps/3-5-storyboard.md` |
| `prototype/fake-it.md` | `steps/4-1-fake-it.md` |
| `prototype/prototype.md` | `steps/4-2-prototype.md` |
| `test/small-data.md` | `steps/5-1-small-data.md` |
| `test/interview.md` | `steps/5-2-interview.md` |
| `test/learn.md` | `steps/5-3-learn.md` |

`SKILL.md`、`conventions/design-log.md`、`conventions/design-backlog-template.md` 原地改路径。

仓库其他：`commands/` 四个；`README.md`、`ATTRIBUTION.md`、`CLAUDE.md`；`scripts/` 的四个文件；`codex/plugins/ideo-scrum/` 由脚本重生成；`.claude-plugin/marketplace.json`。

**sprint-kernel 的内容只挪不改**：约定两行、事件章与事件表的文字从 scrum-kernel 逐字搬，SGEP 原文不动；新写的只有描述、开头一段、指向 scrum-kernel 的一句。

**描述怎么分**：scrum-kernel 让出「冲刺怎么跑」的用词（事件名、冲刺日志），留住产品日志、角色、Scrum 框架、DoD；sprint-kernel 拿事件名与冲刺日志的词。裁决线：产品日志题触发 scrum-kernel，冲刺题触发 sprint-kernel，旧题行为不塌（过线 ①②）。

**PBI-52 的改法**：白纸说法进 scrum-kernel 与 design-kernel 的描述，按场景写（没有产品日志，产品和 Product Goal 都还写不出来），不用题 3 的具体例子（社区图书馆、帮读者找书）——例子不要用正在测的那个点（Sprint 15 的教训）；design-kernel 的 SKILL.md 写明白纸先读 product-log 第 2 条。

**写 SKILL.md 与描述之前**（Master 建议）：先用 plugin-dev 的 skill-development（或 skill-creator）查格式与描述写法；sprint-kernel 写完可派 `plugin-dev:skill-reviewer`（`model: haiku`）看一遍，它提的必改项先对一遍 PO 的定案，有冲突报 Master。

**25 ② 的头**：三个 SKILL.md（ideo、scrum、sprint）都加 Source/License 头，先判定各份里哪些段落属摘录。

**25 ⑥ 的出处**：查过 `assets/` 的 v2026.1，只有理论、价值观、角色三块，没有 Artifacts、Events 两章（特征句 0 处）。2025.6 原文在本地 `references/scrum-guide-expanded-2025.6.md`（worktree 里也有，`.worktreeinclude` 带过来的）；两章与 9 份 reference 先逐句对它核，核过再改标「Scrum Guide Expanded（2025.6）」；ATTRIBUTION 登记 2025.6，原文不收进插件。

**25 ⑦ 的图标**（Master 2026-11-12 定）：这次不加图标；查 schema 只回答「支不支持」；第 4 章记一笔，PBI 留在产品日志。

**测试口径**：题 1–5 与判定照 `a87bd1c` 取回；「读到约定的路径」按两版各自判；新两题的判定照必答/不能的格式自写，先给 Master 看。基线和新版放最后、同一天连着跑，日期用 PowerShell `Get-Date` 看台北时间。

**Risks and open points**

- **描述挪动是最大风险**：冲刺用词从 scrum-kernel 挪走后，题 1、2、5 的触发可能变差；过线 ① 只留 1 次余量、② 不许跌，若不过不动标准，把行为栏摆给 Master。
- **白纸题（过线 ③）**：四轮 0/3 的历史说明光改描述未必够；两条路径各 2/3 是硬线，缺口记进第 5 章。
- **无头下的角色命令入口**：冒烟提到第 2 项；进不去就在跑任何正式测试之前把测法定下来写进第 4 章（Master 说这时改不算违规）。
- **25 ⑥ 的核对**：两章与 9 份 reference 要逐句对 2025.6；若有句子对不上 2025.6，改标前先报 Master。
- **check_codex 的 idempotency 写死了 `sprint-13-codex` 分支**：只改分支判断，内容核对不变。
- **耗时**：基线与新版放最后、同一天连着跑；跨会话时按第 4 章笔记接上。
- **合入 main 的时机**：验收与审阅过后本冲刺先合，Sprint 17 才搬稿；tag、合入、关 worktree、删分支由 Master 做；版本号不动。

Go-ahead: 2026-11-12，PO（停点 ①，两个冲刺一起放行，原话「全部放行」）；范围：在冲刺分支上提交；验收和审阅过后由 Master 收官——打 tag、合入 main、关 worktree、删分支；版本号不动；推送在停点 ③ 之后，随 v6.0.0 一起由 Master 做。

## 4. Increment notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (sprint-log.md, conventions 9 and 20). A session that picks up the Sprint reads these first. The chapter ends with the Product Owner's decision that the Increment can go into testing (sprint-log.md, convention 24). -->

- **工作区**（2026-11-12）：Developer 的原生 worktree `S:\IDEO-Scrum\.claude\worktrees\wizardly-almeida-5485e1`，分支 `sprint-16-kernel-structure`；原自动分支 `claude/wizardly-almeida-5485e1` 已删。所有命令都在这个 worktree 里跑，不 `cd` 到主检出。
- **Master 2026-11-12 审 How（`d9a1123`）**：方案与文件清单可用，补了几处；处理如下，全部写进第 3 章。
  1. 加两个工作项——审阅（Master 审＋全新 Haiku 子代理对抗审查，必改项我改完）与收官准备（Review＋Retro 一个提交；之后 Master 打 tag、合入 main、关 worktree、删分支；PO 亲手试在停点 ③、两个冲刺一起，本冲刺不等）。→ 第 10、13 项。
  2. 25 ②：sprint-kernel 的 SKILL.md 也带 SGEP 事件章，头要加三个 SKILL.md（ideo、scrum、sprint）。→ 第 6 项与 Key choices。
  3. 25 ⑥：2025.6 原文在本地，先拿两章与 9 份 reference 逐句核，再改标；ATTRIBUTION 登记 2025.6，原文不收进插件。→ 已确认 worktree 的 `references/scrum-guide-expanded-2025.6.md`（`.worktreeinclude` 带过来）；第 6、8 项与 Key choices。
  4. 冒烟提前到第 1 项之后，先确认测试工具，尤其无头下从角色命令进入；进不去就在跑任何正式测试之前定测法（那时改不算违规）。→ 第 2 项。
  5. 25 ⑦ 的图标：这次不加（Master 定）；查 schema 只回答「支不支持」，记一笔，PBI 留在产品日志 3.1。→ Key choices。
  6. 写新 SKILL.md 与改描述之前先用 plugin-dev 的 skill-development 查格式与描述写法；sprint-kernel 写完可派 `plugin-dev:skill-reviewer`（`model: haiku`），必改项先对 PO 的定案，冲突报 Master。→ Key choices。
  7. PBI-52 按场景写（没有产品日志、产品和 Product Goal 都写不出来），不用题 3 的具体例子；例子不要用正在测的那个点（Sprint 15 的教训）。→ Key choices。
  8. 时间：2026-11-12 18:30（PowerShell `Get-Date`，台北时间）。
- **Master 2026-11-12 审测试题（`a504b96`）**：两处必改——题 3 的角色命令改 `/ideo-scrum:scrum-master`（陌生人带着想法来，默认从 scrum-master 进；从 designer 进等于已经知道要先做设计）；基线固定在 `9769bd6`，用 `git archive` 解到仓库外跑，不指向主检出（main 在合入前可能被别的提交动到）。一处建议——题 6、7 的必答按要点判，不比约定原文更严。都改了。
- **25 ⑥ 核对（2026-11-12）**：先对本地 2025.6 核，8 份 reference 有段落对不上（含 2025.6 没有的说法：determinate consistent length、Outcomes confirm user changes、As a subset, outcome criteria、data-informed ideas、timeboxed to four hours）；报 Master 后查明：`git show e8056d0:plugins/ideo-scrum/skills/scrum-kernel/assets/scrum-guide-expanded-2026.1.md`（2026-07-22 首次入库，821 行）是 v2026.1 全文、带 Artifacts 与 Events 两章，29f0e65 把这两章 251 行抽进 references/ 与 SKILL.md，assets 只剩其余部分。拿这份全文核：9 份 reference 与两章逐段一致（规范引号、去引用号后 0 段低于 0.97）。**结论：标签 v2026.1 正确，PBI-25 ⑥ 的前提（2025.6）错了**；Master 定：标签不动、2025.6 不登记、改掉「assets 是全文」的说法、CLAUDE.md 那句错的改过来。
- **25 ⑥ 改的地方**：scrum-kernel SKILL.md 的 Reference Catalog 与 ATTRIBUTION 写明 assets 是 v2026.1 除两章以外的部分、两章在 references/ 与 sprint-kernel/events/；ATTRIBUTION 的路径按新布局改（guide 进 assets/、design 摘录进 steps/）；CLAUDE.md「原文优先」那句写明误判与核对（不出现在插件文字里）。
- **第 3–8 项完成**（每项一个提交）：`4a58693` 拆 sprint-kernel（events 五份、sprint-log 与模板移入，scrum-kernel 的 SKILL.md 让出事件章与两行约定表，guide 进 assets/）；`7d5a769` design-kernel 16 份进 `steps/`（顺序照 SKILL.md 五阶段表，pick-a-target 排 2-3，全插件路径与技能名说法改对）；`31b23ef` 四命令同一段加载说明 + overview 第 8 条；`9a42b61` 描述与小修（25 ①②⑥⑦⑧、46 ④ 待 Master 批展示文案）；`08fbc86` Codex 四内核适配与重生成（sync 再跑 0 变化，check 0 错，idempotency 两轮 clean）；`4e1acf3` README 与 CLAUDE.md 同步。
- **第 9 项自检**：`scrum/sprint-16-kernel-structure/check_paths.py` 先自测（好样本 0 错、坏条号与坏路径各能检出）再跑：195 条路径、2 条链接、140 处 `convention N` 引用，0 缺。`claude plugin validate --strict` 插件目录与 marketplace 都通过（25 ⑧ 验过）。`claude plugin validate` 前先 `sync_codex.py`、`check_codex.py`，0 错。`plugin-dev:plugin-validator`（Haiku）后台跑，结果补在下面。
- **plugin-validator（Haiku）结果与处理（2026-11-12）**：结构无阻塞。必改 2——① ATTRIBUTION 第 1 节把 SGEP 的 Artifact / Event 摘录记在 2020 版名下（同一批文件第 2 节也登记了），已改：第 1 节只留 2020 全文与角色命令，修改说明改写；② ideo-kernel SKILL.md 的 `steps/4-1-fake-it.md` 跨 skill 解析不到，改成 `../design-kernel/steps/4-1-fake-it.md`。建议已采纳：三处引用偏松（冲刺模板 convention 20 改成「4 and 20」；模板里 `overview.md` 补 scrum-kernel 位置；设计模板裸 convention 21 写成 `convention 21 in design-log.md`）；四命令的 Conventions 行统一成 developer 的写法，stakeholder 的 product-log 引用改成具名路径；两个 description 超 1024（1253、1084），压到 975、985；`check_paths.py` 收紧——去掉跨 skill 全目录兜底，跨 skill 必须写 `../`（重跑 196 条路径、140 处引用，0 缺）。观察（事件引言与事件原文两份拷贝）接受，不改。
- **测试通道（2026-11-12 定）**：`claude -p` + 去掉 `CLAUDE_CODE_HOST_AUTH_ENV_VAR`、`CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`、`ANTHROPIC_BASE_URL`；模型 claude-haiku-5-5；只开 Read、Grep、Glob、Skill；基线插件用 `git archive 9769bd6` 解到 `S:\IDEO-Scrum-Archives\sprint-16-kernel-structureaseline-plugin`；每次调用给一个新的空 TEMP/TMP 与工作目录（冒烟时模型会翻到同级的旧测试目录）。基线 42 次在后台跑，原始输出进 `...aseline\`。
- **25 ⑦**：product-log 与 sprint-log 开头「路径（括号）, convention 15」改成「convention 15 of `overview.md`，…」；overview 里裸写的 `product-log.md` 改成 `conventions/product-log.md`；「三处引用与条名贴合得宽松」原文没登记是哪三处，留到第 9 项 plugin-validator 报出来再改；图标这次不加（Master 定），留在产品日志。
- **冒烟（2026-11-12 18:5x）**：`reclaude` 两次回「账号暂不可用」（`status --check` 显示线路与登录可连接，但调用被拒），`claude -p` 回「Not logged in」。测试通道暂缺；先做第 3–9 项，跑测前再试，不通就报 Master。

## 5. Test

<!-- Record here the Developer's tests, the reviewer's check (by default the Scrum Master), the Product Owner's end-to-end test, and the result of each Definition of Done item and acceptance criterion. Fix a problem on the spot and test again (sprint-log.md, convention 16). The chapter ends with the Product Owner's decision: close, or go back (sprint-log.md, convention 24). -->
