# Sprint Backlog — Sprint 20 (presentable)

> Started: 2026-11-14 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: worktree-sprint-20-presentable | Product Owner: SeaPawn | Scrum Master: 会话 IDEO # [master]-[main]-[management sprint] | Developer: Claude Code（会话 IDEO # [developer]-[sprint-20]-[do presentable]，原生 worktree sprint-20-presentable）
> Now: What：精化 68、64，第 1～5 步 PO 已在 Master 会话里过了，第 6 步 Developer 已复述，等 PO 认可；62 由 Master 接着领 PO 精化，63 随后；第 7 步等 64、62、63 都精化完再一起定 · 最近一次 PO 决定：2026-11-14 过完 64 的第 1～5 步（图标做，CHANGELOG 等交 Master 定）
> Waiting for PO: 68 第 6 步：Developer 的复述对不对；64 第 6 步：Developer 的复述对不对
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

> 精化由 Master 主持。PBI-68、64 的第 1～5 步是 Master 领着 PO 在它的会话里过的，2026-11-14 转来，下面原样写进；68-①② PO 已答（见下），68、64 的第 6 步 Developer 已复述，等 PO 认可；第 7 步由 PO 说精化结束，要等 64、62、63 都精化完再一起定。62 由 Master 接着领 PO 精化，63 随后，精化到哪条再拿出来跟 PO 定。

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
- 68-4 承诺原文、编号、状态和日志一致。核对方法（Developer 提，Master 2026-11-14 同意；68-② 定了照抄的范围后写成这样）：新模板保留 `data-fact` 标记；检查脚本把标记里的文字（承诺原文、编号、标题、状态、日期、Now、Waiting）逐条对回日志，不许有一条出入；每个链接逐个点开，都要打得开；重新组织过的地图，每个节点名要能在日志的地图里找到（产品日志 2.2、设计日志 2.1）；路线图的每个条目编号和标题要能在产品日志 3.1 里找到。概括的文字有没有加日志里没有的事实，脚本查不了，靠生成时的约定和 PO 看（68-6）。脚本沿用 Sprint 19 的 `board_check.py`（`git show 1bf5a94:scrum/sprint-19-board-hook/tests/board_check.py`），改成读新模板的标记；先拿真仓库的状态和夹具过一遍，再用它核对生成的页面。过线：照抄项全部一致，链接全部打得开，节点名和条目全部找得到；
- 68-5 守住只读日志、不存状态；
- 68-6 PO 看过本仓库现状生成的真实看板，说行。

**PO 的答复**（2026-11-14，Master 转来，原话）：「原型看吧，回头我肯定是要跟他设计的。或者说我给你设计也可以，或者说我去建一个设计的对话也可以，都是可以。不过我觉得应该不需要，应该我我跟你，然后我们结合辅助对话就可以了。不过这个不着急，到时候看吧。其他的我觉得还可以的。你让我定的三点骨架。至于怎么排？不好说，他不好说。我觉得你其他的建议都都挺对的，没问题。」

**PO 的补充**（2026-11-14，Master 转来，原话）：「反正对于我们这个看板。我们是要先开一次设计的，这个我觉得是毋庸置疑的……当然这个设计反正就是怎么说呢，原型嘛，原型那当然也是一个设计了，也没问题。」

**据此定案**（Master）

| 点 | 定案 |
| --- | --- |
| 68-① 骨架 | 现在不定，放到原型轮里定。第一轮的几个方向里，既要有沿用第 1 版骨架的，也要有放开重排的 |
| 68-② 照抄和概括的分界 | PO 认可 Master 的建议：承诺原文、编号、标题、状态、日期、Now、Waiting 照抄；架构图、路线图、说明文字由 LLM 重新组织成概括 |
| frontend-design | 用 `seapawn:frontend-design`，PO 认可 |
| 新的开放点 | 68-a 的原型由谁跟 PO 做，现在不定，开做 68-a 时再看。PO 列的做法：跟 Developer 做、跟 Master 做、另开一个设计会话；他倾向于 PO 加 Master，再配上辅助会话 |
| 先开设计 | Master 的理解：68-a 的原型轮就是这次看板的设计，一定排在 68-b 前面，照旧记在冲刺日志里，不开设计冲刺 |
| 其余各点 | PO 说「还可以」「没问题」 |

**第 6 步 · Developer 的复述**（2026-11-14，待 PO 认可）

用自己的话把每一点说一遍：我听到的是什么，我要做什么。

- **①② 立足点**：看板是给 PO 本人用的：打开就一眼看清项目走到哪、有什么在等他拍板，并拿它拍板；电脑全屏和手机上都读得顺；原型他亲自参与。
- **a 放什么**：最上面是等他拍板的，其次是正在做的；其余放什么、不放什么，第 1 版的骨架留不留，现在不定，由 PO 在原型轮里看着定（68-①）。所以第一轮的几个方向里，既有沿用第 1 版骨架的，也有放开重排的，让他在看得见的东西里挑。
- **b 架构图**：做成一眼看懂的概括：从原图里挑主干节点、省去细节，节点名取自原图、不另造词（核对要靠这个）。怎么画由我在原型里提方案：直接用 HTML/SVG，不再靠 Mermaid 的 CDN；PO 挑。
- **c 照抄和概括的分界**（68-②，PO 已认可）：照抄的是事实——承诺原文、编号、标题、状态、日期、Now、Waiting；由 LLM 重新组织成概括的是架构图、路线图、说明文字。我补两处理解，请 PO 看对不对：（1）Sprint 卡上第 3 章的工作块名，和条目标题一样算标题，照抄，做完的标记照 `✓`；（2）路线图指产品卡上没做完的条目，和冲刺卡上条目的走向：编号、标题、状态照抄，怎么分组、怎么排由 LLM 重新组织，但分组的依据只能是日志里写着的（状态、所属冲刺、主线/副线/以后），不推算完成度和优先级；概括的文字不加日志里没有的事实。
- **d 电脑和手机**：同一页，电脑全屏（我截 1440 宽）和手机（375 宽）都好读；窄屏时卡片排成一列，不横向溢出；两种宽度各截图给 PO、各验一遍（验收 68-2）。
- **e 好看**：视觉方向用 frontend-design（`seapawn:frontend-design`），先定设计方向、再落页面；什么样算好看是研究题，不是我说了算：每轮给 PO 看截图，他点到哪，我改哪，由他挑。
- **f 条目少、白纸也好看**：夹具 A、B 是同一个小项目（Acme 订单台：5 条条目、2 个冲刺、1 个设计、1 个 IDEO 日志），只是 git 状态不同——A 的日志只在分支上，B 的工作区里有没提交的改动；拿它们验「条目少」。「白纸」（只有 Product 和 Product Goal，没有条目、没有开着的冲刺和设计、没有等 PO 的事）夹具里没有，我另造一份。没有冲刺、没有设计、没人等 PO 这几种空的样子也要设计过，不是一片空白。
- **68-a 原型**：这一轮就是这次看板的设计（PO 的补充：「我们是要先开一次设计的」；Master 的理解：原型轮就是设计），一定排在 68-b 前面，记在本日志里，不开设计冲刺。数据用本仓库现状。现状里 Sprint 20 的第 3 章还空着，卡上看不到工作块，所以另拿 Sprint 19 收官前的日志（`git show 1bf5a94:scrum/sprint-19-board-hook/SprintBacklog.md`）当第二份样本，看有工作块和 `✓` 的冲刺卡。第一轮 2～3 个方向（至少一个沿用第 1 版骨架、至少一个放开重排），静态 HTML；PO 挑一个后，每轮只改他点到的地方，他说「就这个」才算完；轮次记在第 4 章；用五模式，每个方法用之前先读 ideo-kernel 的 `methods/` 里它的文档。原型放在本冲刺的文件夹里，收官时删，git 留着。谁跟 PO 做，开做时再看。
- **68-b 模板和约定**：照选定的样子重做 `board-template.html` 和 `board.md`；`board.md` 第 13、15 条（逐字抄、抄地图源）改成：事实照抄，概括的部分怎么生成、怎么核对；用便宜的模型照新模板真生成一次本仓库现状的看板，再用 68-4 的方法核对。
- **Sprint 19 的两条已知限制**（产品日志 PBI-68：不单列，新样子顺带解决的就算解决）：地图靠 CDN，随 HTML/SVG 一起没了；「生成后插件里没有自动核对」这次不解决——检查脚本只用来验收本冲刺，不放进插件，仍记作已知限制；PO 若要把核对放进插件，那是另一条条目，不在 68 的范围。
- **验收标准 68-1～68-6**：照上面的理解做；68-4 的核对方法写在上面的 68-4 里。

**PBI-64 发布包装**

第 1～5 步是 Master 领着 PO 在它的会话里过的，2026-11-14 转来，原样写进；第 6 步的复述在最后，等 PO 认可。

**事实**（Master 查过）

- 图标：`plugin.json` 的 `icon` 字段只有 Anthropic 官方目录收录时才读，Claude Code 加载时忽略；CLI 2.1.323 不会因为它报 `--strict` 失败。PO 说 Claude Desktop 里看得到图标，所以要做。
- 升级：第三方 marketplace 默认不自动更新，用户要跑 `claude plugin update ideo-scrum@ideo-scrum`，或者在 `/plugin` 里打开自动更新。
- 授权：README 已经有「来源与授权」一节和非商业警示，ATTRIBUTION.md 也齐。
- 反馈：仓库公开，Issues 开着。
- CHANGELOG：根目录还没有。

**①② 立足点**（照抄用户故事）：「作为懂 Scrum 的陌生人，我想要插件有版本记录、发布渠道、授权说明、反馈渠道和图标，以便放心装、知道怎么升级和反馈」

**③④ 定案**

| 点 | 定案（谁定） |
| --- | --- |
| 图标 | 做（PO：「桌面端是能看到的……我觉得其实是可以做的」）。出几张给 PO 挑，放进插件，`plugin.json` 的 `icon` 指向它，README 顶部也用；提交官方目录不在这次 |
| CHANGELOG | PO 交给 Master 定（「修改日志……你来决定吧。其他的你都可以来决定」）。Master 定：放根目录，用英文（照 62「英文为准」）；6.0.3 一节详写，之前的版本每版一行，照 tag 列 |
| 反馈 | 只放 GitHub Issues 的链接，不做模板（Master 定） |
| 发布 | 推送 main 和 tag v6.0.3（PO 已定），收官时再请 PO 点头 |
| Codex 的两处 | Master 请 Developer 查，2026-11-14 查得：Codex 有放图标的地方——`.codex-plugin/plugin.json` 的 `interface.logo`、`interface.composerIcon`，路径相对插件根（依据是本机 Codex 插件缓存里的 Superpowers 示例，不是官方规范）。但同步脚本现在只把四个内核、`hooks/`、四个角色技能、清单、LICENSE、ATTRIBUTION.md、README 带进包：放在 `plugins/ideo-scrum/` 里的图标和根目录的 CHANGELOG 都不会自动进包，`check_codex.py` 也不会因此报错。要进包得改两个脚本（同步脚本多拷一份、`check_codex.py` 的预期清单多一项；图标另在 `scripts/codex_interface.json` 里写 `logo`）。另有一处：同步脚本把 Claude 的 `plugin.json` 整份带进 Codex 的清单，Claude 清单加了 `icon` 字段后，Codex 清单里会多出一个指向包里没有的文件的 `icon`，脚本要把它去掉（一行）。Developer 的建议：Codex 先不带图标和 CHANGELOG（Codex 不是核心，PO 2026-11-13），只加去掉 `icon` 字段这一行；要带再加。待 Master 定 |

**⑤ 切成两块**

- **64-a 包装**：CHANGELOG；README 补升级、授权、反馈三段；图标。
- **64-b 发版**：63 测完以后、收官时做。版本号改成 6.0.3，README 两处同步，跑 `sync_codex` 和 `check_codex`，跑 `--strict`。

**验收标准（草稿）**

- 64-1 根目录有 CHANGELOG：6.0.3 写清改了什么，之前每版一行，和 tag 对得上；
- 64-2 README 写清怎么升级（命令和自动更新开关）、授权（显眼处一句话说非商业限制，链到 ATTRIBUTION）、反馈（Issues 链接）；
- 64-3 图标是 PO 选定的，放在插件里，`plugin.json` 指向它，`--strict` 通过；
- 64-4 6.0.3 的版本号各处一致，Codex 包核对通过，推送经 PO 点头。

**第 6 步 · Developer 的复述**（2026-11-14，待 PO 认可）

- **立足点**：陌生人装之前、装之后都要放心：看得到版本记录，知道怎么升级、授权有什么限制、在哪反馈，看得到图标。
- **图标**：我出 3 张给 PO 挑——样子是 PO 的口味，我不替他定；放进插件，`plugin.json` 的 `icon` 指向它，README 顶部也用；提交官方目录不在这次。`icon` 字段的写法（路径、尺寸、格式）做的时候先查 docs MCP。验收（64-3）只能验到「放进去、`--strict` 通过、README 里看得到」：Claude Code 忽略这个字段，官方目录这次不提交，它在 Claude Desktop 里显不显示我验不了。
- **CHANGELOG**：根目录，英文；6.0.3 一节详写，6.0.2 及以前每版一行，照 `git tag` 列；我写，给 Master 审。
- **反馈**：README 里放 GitHub Issues 的链接，不做模板。
- **README 三段**：升级（`claude plugin update ideo-scrum@ideo-scrum`，或在 `/plugin` 里打开自动更新）、授权（显眼处一句话说 d.school 的非商业限制，链到 ATTRIBUTION.md）、反馈（Issues 链接）。62 要把 README 改成中英两份、英文为准，和这三段碰同一个文件：我打算让三段跟着 62 的 README 一起写（先定英文版的结构，再写中文），CHANGELOG 和图标先做。
- **发布**：64-b 在 63 测完以后、收官时做：版本号 6.0.3，README 两处同步，跑 `sync_codex.py`、`check_codex.py`、`--strict`；推送 main 和 tag `v6.0.3`，收官时请 PO 点头。
- **Codex**：见上表，待 Master 定。

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |

**Key choices**

**Risks and open points**

Go-ahead: 尚无

## 4. Increment notes

- **开冲刺**（2026-11-14）：Developer 读过产品日志 PBI-68、64、62、63 的备注，和反馈区里关于看板的三条（电脑与手机都要适配、模板用 frontend-design 重做、只概括不搬细节；记忆里 `FeedBack/IDEO-Scrum/2026-11-14-board-*`）——这三条是做 68 时的常设要求。1.1 的 Goal 是 PO 认可的草稿原文；1.2 是 Developer 的提议，只挑本冲刺碰得到的项（可导航、描述长度这次不动，没挑）；2.1 四行取自产品日志，已用脚本逐格核对。三处现在都定了：1.1 草稿即定稿，1.2 由 Master 照 PO 的交代挑定（第 1 章末行），2.1 的选定和顺序是 PO 2026-11-14 在产品日志里定的。
- **PO 的开工指令**（2026-11-14，原话）：「先做 68：用五模式做原型，PO 直接跟你一轮一轮改，记在冲刺日志里。开做前先确认 frontend-design 技能在哪。这次授权不延续，每个阶段都由 PO 定。」Master 主持 Planning、记录和审阅；每个阶段的末尾由 PO 定，Master 不代过关卡。
- **frontend-design 在哪**（产品日志 PBI-68 的开放点，2026-11-14 查）：Claude Code 里叫 `seapawn:frontend-design`，来自已装的插件 seapawn@seapawn，文件在 `C:\Users\seapawn\.claude\plugins\cache\seapawn\seapawn\c3b29aa5f394\skills\frontend-design\SKILL.md`。官方 `claude-plugins-official` 市场里有同名插件但没装；两份 SKILL.md 去掉换行符后逐字相同。PO 助手记的 `anthropic-skills:frontend-design`，在 Claude Code 的技能清单和 `~/.claude/plugins` 里都查不到（PO 助手是 Claude Desktop 会话，推测它指的是 Desktop 里的那份，未证实）。反馈区写明「动手前跟 PO 核对是不是指它」，所以放进过 Waiting for PO。PO 说刚让助手装过（Master 2026-11-14 转告），并认可用这份（Master 转来，见 2.2），已从 Waiting 去掉；`installed_plugins.json` 里 seapawn@seapawn 的更新时间是 2026-11-14 02:34（UTC+8），对得上「刚装过」。
- **本机能截图**：Edge 与 Chrome 都装了，可以无头截图；做 68 时桌面全屏与 375px 宽各截一张给 PO，再各验收一遍（反馈区第一条的做法）。
- **Why 的决定怎么到我这里的**（2026-11-14）：PO 在 Master 会话里定，Master 用跨会话消息转来。PO 的原话：「可以，我觉得目标可以的。DOD 你来挑吧，我就不关心了，中字名也没问题我们现在先往下进入第2阶段吧」（「中字名」，Master 按冲刺名理解）。精化的第 1～5 步同样是 Master 领着 PO 在它的会话里过的，转来后原样写进 2.2。Master 还交代：64、62、63 先别动，精化到哪条再拿出来；还没放行，别开做。
- **分支名覆盖了约定**：sprint-log 第 1 条要分支与文件夹同名，这里分支叫 `worktree-sprint-20-presentable`，文件夹叫 `sprint-20-presentable`。照 overview 第 15 条覆盖了约定，原因：CLAUDE.md 规定 worktree 用原生方式建，原生方式给分支名自动加 `worktree-` 前缀。收官时 tag 仍叫 `sprint-20-presentable`，合入 main 后删这条分支。
- **68-①② 的答复**（2026-11-14，Master 转来，原话在 2.2）：骨架放到原型轮里定，照抄与概括的分界认可，frontend-design 认可；新开放点：68-a 的原型由谁跟 PO 做，开做时再看。第 6 步的复述已写进 2.2，等 PO 认可。写复述时查出：Sprint 19 的夹具 A、B 是同一个小项目（5 条条目、2 个冲刺、1 个设计、1 个 IDEO 日志）的两种 git 状态，不含「白纸」，f 点的复述据此写成：夹具验「条目少」，另造一份白纸夹具。
- **64 的授权范围**（2026-11-14，Master 转来）：PO 在精化 64 时说「修改日志……你来决定吧。其他的你都可以来决定」。授权的是 PO，被授权的是 Master，管 64 的细节——这次用在 CHANGELOG 的放法和写法、反馈只放 Issues 链接；不包括关卡（阶段末尾仍由 PO 定），也不包括推送（收官时再请 PO 点头）。
- **68 补记**（2026-11-14，Master 转来）：PO 说「我们是要先开一次设计的」，又说原型「那当然也是一个设计了」；Master 的理解是 68-a 的原型轮就是这次的设计，不开设计冲刺。原话和这层理解已写进 2.2。
- **64 的第 1～5 步和我查的两处**（2026-11-14）：64 的第 1～5 步原样写进 2.2，并附 Developer 的复述。Master 让查的两处：Codex 有放图标的地方（`interface.logo`、`interface.composerIcon`），但同步脚本现在不会把图标和 CHANGELOG 带进包；Claude 清单加 `icon` 后会被原样带进 Codex 清单，需要脚本去掉。详见 2.2 的 64 表，Codex 带不带待 Master 定。

## 5. Test
