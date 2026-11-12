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

## 3. How

<!-- The Developer writes this chapter as a plan for making the selected items, short and not in detail (sprint-log.md, convention 7): the work items in order, each with its output and how to tell it is done; the key choices and why; the risks and open points. The last line is the go-ahead (sprint-log.md, convention 8). -->

| # | Work item | Output | Done when |
| --- | --- | --- | --- |

**Key choices**

**Risks and open points**

Go-ahead: （待 PO：停点 ①，两个冲刺的 How 都审过后一起放行）

## 4. Increment notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (sprint-log.md, conventions 9 and 20). A session that picks up the Sprint reads these first. The chapter ends with the Product Owner's decision that the Increment can go into testing (sprint-log.md, convention 24). -->

## 5. Test

<!-- Record here the Developer's tests, the reviewer's check (by default the Scrum Master), the Product Owner's end-to-end test, and the result of each Definition of Done item and acceptance criterion. Fix a problem on the spot and test again (sprint-log.md, convention 16). The chapter ends with the Product Owner's decision: close, or go back (sprint-log.md, convention 24). -->
