# Sprint Backlog — Sprint 20 (presentable)

> Started: 2026-11-14 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: worktree-sprint-20-presentable | Product Owner: SeaPawn | Scrum Master: 会话 IDEO # [master]-[main]-[management sprint] | Developer: Claude Code（会话 IDEO # [developer]-[sprint-20]-[do presentable]，原生 worktree sprint-20-presentable）
> Now: What：精化 68，第 1～5 步 PO 已在 Master 会话里过了，等 PO 定两点；第 6 步等 Developer 复述 · 最近一次 PO 决定：2026-11-14 定 Sprint Goal
> Waiting for PO: 68-① 原型从第 1 版骨架起步，还是放开重排；68-② 照抄和概括的分界；frontend-design 用不用 seapawn:frontend-design
> How to write this log: `sprint-log.md` in the sprint-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled later; add none — remarks go in chapter 4, Increment notes (`overview.md` in the scrum-kernel skill folder, convention 16).

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 拿得出手：看板改版，好看、好读；README、快速上手、词汇表讲清规矩，发布包装补齐；懂 Scrum 的人照着就能装上、走完第一个冲刺，不问作者。 |
| --- | --- |

### 1.2 Definition of Done

**Outcome Done**

| 度量 | 目标信号 |
| --- | --- |
| 懂 Scrum 的陌生人走完第一个冲刺 | 体验测试（PBI-63）里不问作者、没有卡死的点 |

**Output Done**

| 维度 | 标准 |
| --- | --- |
| 内容忠实 | 忠于源材料（SGEP / d.school / Sprint）；方法论设计部分（融合、solo+AI）标注来源与依据 |
| 署名 | 第三方摘录带 Source / License 两行，与 ATTRIBUTION.md 一致 |
| 无死链 | 所有 markdown 内部链接可解析，无 404 |
| 插件校验 | `claude plugin validate --strict plugins/ideo-scrum` 通过 |
| Codex 包 | 改了插件就跑 `scripts/sync_codex.py`，`scripts/check_codex.py` 通过 |

PO 2026-11-14 定 Sprint Goal（「可以，我觉得目标可以的」）；DoD 交 Master 挑（「DOD 你来挑吧」），Master 挑定 1.2 现列各项；冲刺名 presentable PO 认可。

## 2. What

### 2.1 Product Backlog Items

| 编号 | 标题 | 用户故事 | 架构定位 | 规模 |
| --- | --- | --- | --- | --- |
| PBI-68 | 看板改版——更好看、更好读 | 作为熟手（也是 PO），我想要看板好看、好读，电脑全屏和手机上都能看，并且亲自参与原型，以便打开就一眼看清进度、拿它拍板 | Map「看进度」 | M～L |
| PBI-64 | 发布包装 | 作为懂 Scrum 的陌生人，我想要插件有版本记录、发布渠道、授权说明、反馈渠道和图标，以便放心装、知道怎么升级和反馈 | Map ① | S～M |
| PBI-62 | 教学——README、快速上手、词汇表、示例项目 | 作为懂 Scrum 的陌生人，我想要一份讲清本插件规矩的 README、一页快速上手、一张词汇表和一个真实的示例，以便不读作者的仓库也能走完第一个冲刺 | Map ① | M |
| PBI-63 | 体验测试——陌生人从装插件走到看板 | 作为懂 Scrum 的陌生人，我想要每版都有人替我从头走一遍，以便我装上就能用、不被卡住 | Map ①～⑨ 全程 | M |

### 2.2 Refinement

> 精化由 Master 主持。PBI-68 的第 1～5 步是 Master 领着 PO 在它的会话里过的，2026-11-14 转来，下面原样写进；第 6 步等 PO 答完 68-①②，Developer 再复述；第 7 步由 PO 说精化结束。64、62、63 按这个顺序，精化到哪条再拿出来跟 PO 定。

**PBI-68 看板改版**

**①② 立足点**（照抄用户故事）：「作为熟手（也是 PO），我想要看板好看、好读，电脑全屏和手机上都能看，并且亲自参与原型，以便打开就一眼看清进度、拿它拍板」

**③④ 要回答的问题和不清楚的点，各归谁**

| # | 要回答的问题 | 归谁 |
| --- | --- | --- |
| a | HMW 让 PO 第一眼看到最要紧的事（等他拍板的、正在做的）？看板放什么、不放什么，第 1 版的骨架留不留？ | PO 在原型轮里定（即 68-①） |
| b | HMW 把架构图变成一眼看懂的概括，而不是照抄 Mermaid？用什么画？ | Developer 在原型里出方案 |
| c | 哪些照抄、哪些由 LLM 重新组织？ | PO 定原则（即 68-②） |
| d | HMW 同一页在电脑全屏和手机上都好读？ | 写成验收标准，Developer 做 |
| e | 视觉方向用 frontend-design 做；什么样算好看，是研究题 | 照 PO 定的，用五模式在冲刺里做，PO 挑 |
| f | 用户项目条目很少、甚至一张白纸时，也要好看 | Developer 拿 Sprint 19 的两份夹具验 |

**⑤ 切成两块**

- **68-a 原型**：用本仓库现状的一份数据，第一轮做 2～3 个风格方向的静态 HTML。PO 挑一个，在它上面一轮一轮改，每轮只改 PO 点到的地方。PO 说「就这个」才算完。轮次记在第 4 章。
- **68-b 模板和约定**：照选定的样子重做 `board-template.html` 和 `board.md`，写进概括的规矩；用便宜的模型照新模板真生成一次，并核对。

**验收标准（草稿）**

- 68-1 样子是 PO 在原型轮里选定的；
- 68-2 电脑全屏和 375px 宽各截图、各验收一遍，不横向溢出，窄屏时卡片排成一列；
- 68-3 架构图、路线图是重新组织的概括，不照抄日志里的图；
- 68-4 承诺原文、编号、状态和日志一致，核对方法由 Developer 提（第 6 步时写进来）；
- 68-5 守住只读日志、不存状态；
- 68-6 PO 看过本仓库现状生成的真实看板，说行。

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |

**Key choices**

**Risks and open points**

Go-ahead: 尚无

## 4. Increment notes

- **开冲刺**（2026-11-14）：Developer 读过产品日志 PBI-68、64、62、63 的备注，和反馈区里关于看板的三条（电脑与手机都要适配、模板用 frontend-design 重做、只概括不搬细节；记忆里 `FeedBack/IDEO-Scrum/2026-11-14-board-*`）——这三条是做 68 时的常设要求。1.1 的 Goal 是 PO 认可的草稿原文；1.2 是 Developer 的提议，只挑本冲刺碰得到的项（可导航、描述长度这次不动，没挑）；2.1 四行取自产品日志，已用脚本逐格核对。三处现在都定了：1.1 草稿即定稿，1.2 由 Master 照 PO 的交代挑定（第 1 章末行），2.1 的选定和顺序是 PO 2026-11-14 在产品日志里定的。
- **PO 的开工指令**（2026-11-14，原话）：「先做 68：用五模式做原型，PO 直接跟你一轮一轮改，记在冲刺日志里。开做前先确认 frontend-design 技能在哪。这次授权不延续，每个阶段都由 PO 定。」Master 主持 Planning、记录和审阅；每个阶段的末尾由 PO 定，Master 不代过关卡。
- **frontend-design 在哪**（产品日志 PBI-68 的开放点，2026-11-14 查）：Claude Code 里叫 `seapawn:frontend-design`，来自已装的插件 seapawn@seapawn，文件在 `C:\Users\seapawn\.claude\plugins\cache\seapawn\seapawn\c3b29aa5f394\skills\frontend-design\SKILL.md`。官方 `claude-plugins-official` 市场里有同名插件但没装；两份 SKILL.md 去掉换行符后逐字相同。PO 助手记的 `anthropic-skills:frontend-design`，在 Claude Code 的技能清单和 `~/.claude/plugins` 里都查不到（PO 助手是 Claude Desktop 会话，推测它指的是 Desktop 里的那份，未证实）。反馈区写明「动手前跟 PO 核对是不是指它」，所以放进 Waiting for PO。PO 说刚让助手装过，多半就是这份（Master 2026-11-14 转告），Master 去向 PO 确认；`installed_plugins.json` 里 seapawn@seapawn 的更新时间是 2026-11-14 02:34（UTC+8），对得上「刚装过」。
- **本机能截图**：Edge 与 Chrome 都装了，可以无头截图；做 68 时桌面全屏与 375px 宽各截一张给 PO，再各验收一遍（反馈区第一条的做法）。
- **Why 的决定怎么到我这里的**（2026-11-14）：PO 在 Master 会话里定，Master 用跨会话消息转来。PO 的原话：「可以，我觉得目标可以的。DOD 你来挑吧，我就不关心了，中字名也没问题我们现在先往下进入第2阶段吧」（「中字名」，Master 按冲刺名理解）。精化的第 1～5 步同样是 Master 领着 PO 在它的会话里过的，转来后原样写进 2.2。Master 还交代：64、62、63 先别动，精化到哪条再拿出来；还没放行，别开做。
- **分支名覆盖了约定**：sprint-log 第 1 条要分支与文件夹同名，这里分支叫 `worktree-sprint-20-presentable`，文件夹叫 `sprint-20-presentable`。照 overview 第 15 条覆盖了约定，原因：CLAUDE.md 规定 worktree 用原生方式建，原生方式给分支名自动加 `worktree-` 前缀。收官时 tag 仍叫 `sprint-20-presentable`，合入 main 后删这条分支。

## 5. Test
