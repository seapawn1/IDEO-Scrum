# 三份大纲，PO 一次看完（块 4）

> 2026-11-14，Developer 写。要你做的四件事：① README、快速上手的大纲说行（或指出要改）；② 词汇表的词条清单说行；③ 定 README 的文件地图收不收（D）；④ 从三张图标里挑一张（E）。你说行，我再写全文（sprint-log 第 11、12 条）。
> 写法：每行是「将来文档里的英文标题 —— 这一节会写什么」；英文为准，中文版标题一一对应。

## A. README（`README.md` 英文，`README.zh-CN.md` 中文）

- `# IDEO-Scrum` —— 图标、一句话说它是什么、版本号（首行）；紧接着一句醒目的授权提示：d.school 的材料有非商业限制，本仓库不算 OSI 意义上的开源软件，细节见 License。
- `## What it is` —— 把 Design Thinking 与 Scrum Sprint 装进 Claude Code（Codex 是附带包）：四个角色、四个内核各是什么；不做什么（不是项目管理工具、不接 JIRA 和 Linear）；写给谁（懂 Scrum、一个人加 AI 做项目的人）。
- `## Install` —— Claude Code 三行命令；Codex 两行（附带，写短）。旧 `codex` 分支迁移那一段对新用户没用，建议挪进 CHANGELOG 的升级提示，不留在这里。
- `## Upgrade` —— `claude plugin update ideo-scrum@ideo-scrum`，或在 `/plugin` 里打开自动更新（第三方市场默认不自动更新）；指向 CHANGELOG。Codex 的升级办法我查了再写，查不实就写明没验证。
- `## Your first sentence` —— 入口要教：怎么叫出四个角色（`/ideo-scrum:scrum-master` 等），怎么直接说（「用 ideo-scrum 帮我……」两三个例句），怎么叫出 ideo（发散、定义问题时模型多半直接作答，点名 ideo-kernel 才用它的方法，这是已知的限制）；链到快速上手。
- `## How it differs from textbook Scrum` —— 一张小表（来自 `overview.md` 的 Departures）：这里怎么做 / 官方怎么说 / 为什么，七行：只有 PO 必须是人；设计与冲刺并列；PO 和 Scrum Master 定条目；How 是计划、放行才动手；检查点代替 Daily Scrum；审阅者必须有；没有冲刺截止日；链到 `overview.md`。
- `## Where the work lives` —— 你的项目里会长出 `scrum/`：产品日志、冲刺日志、设计日志、IDEO 日志、看板各放哪；真实的示例就是本仓库的 `scrum/`（中文的），看哪几份（`ProductBacklog.md`、一份归档的冲刺日志）。
- `## Board and hook` —— （62-d，68 做完再写）hook：做什么、`IDEO_SCRUM_COMMITMENTS=off` 关掉、Windows 要装 Git for Windows、macOS 没实测、Codex 要先在 `/hooks` 里信任；看板：怎么叫它生成、长什么样（放一张图）。
- `## Learn more` —— 链到快速上手、词汇表、CHANGELOG、`overview.md`。
- `## License and attribution` —— 原创部分 MIT；Scrum Guide、SGEP 是 CC BY-SA 4.0；d.school 是 CC BY-NC-SA 4.0（非商业）；《Sprint》全版权，只记方法流程；链到 `ATTRIBUTION.md`（和它对得上）。
- `## Feedback` —— GitHub Issues 的链接，写什么进去（装的环境、你说了什么、看到什么）；不做模板。
- `## Files` —— 文件地图（收不收见 D）。

## B. 快速上手（`docs/quick-start.md`、`docs/quick-start.zh-CN.md`，一页，约 80 行内）

- `# Quick start` —— 读完你手里有什么：一个走完的 Sprint；一个会话、你当 Product Owner、Scrum Master 陪你。
- `## Before you start` —— 装好插件（链 README）；项目是 git 仓库（不是的话，可以让 Master 代你 `git init`，这是建议）。
- `## 1. Call the Scrum Master` —— 输入 `/ideo-scrum:scrum-master`；你就是 PO，你说了算价值和方向。
- `## 2. Write the product log` —— 跟 Master 写 `scrum/ProductBacklog.md`：产品、Product Goal、几条条目；一小段真实的样子（出自示例）。
- `## 3. Open a Sprint` —— Why（Sprint Goal）→ What（选条目、精化）→ How（计划，不是步骤）；每个阶段结束你说一声才往下走；你说「放行」才动手。
- `## 4. Build and test` —— 动手、检查点、测试；有 Developer 角色就叫它，没有就 Master 做（可以让 Master 代做 git 的活）；审阅者不能是做的人。
- `## 5. Close` —— 说「收官」：Review 和 Retro、一个收官提交、tag、合并（可以让 Master 做）；推送要你点头。
- `## Rules worth keeping` —— 五条：每个阶段结束 PO 定（overview 12）；放行才动手（sprint-log 8）；Sprint Goal 不变、计划可调（overview 17）；审阅者不是做的人（sprint-log 14）；日志就是交接——`Now` 和 `Waiting for PO`（sprint-log 22）。每条后面标约定里的位置。
- `## Handing over in writing` —— 书面授权最简写法：日志里一行，写谁、范围、覆盖哪些阶段；给一行示例。
- `## When you are lost` —— 问「现在到哪了」（Master 读 `Now` 和 `Waiting for PO`）；要看板就说「生成看板」；要做研究就叫 Designer。

## C. 词汇表（`docs/glossary.md`，一张表：Term | 中文 | Meaning | 含义 | See）

只收插件里会撞上的词；《Sprint》里的词用自己的话写一两句，指到 `design-kernel/steps/` 里对应的文件，不抄书。

- **日志和文件**：product log 产品日志；sprint log 冲刺日志；design log 设计日志；IDEO log IDEO 日志；PBI（产品日志条目）；Commitment 承诺（一行小表：Product Goal、Sprint Goal、设计目标）；Now / Waiting for PO（日志头部两行）；Increment notes 增量笔记（冲刺日志第 4 章）；role card 角色卡（产品日志里利益相关者表的一行）；the Map 架构图（产品日志 2.2）；board 看板；`scrum/documents/` 归档。
- **角色和分工**：Product Owner；Scrum Master；Developer；Designer（设计结对，插件自己的角色）；Stakeholder（外部视角，或常驻做非源码杂务）；PO assistant PO 助手；fresh subagent 全新子代理；written handover 书面授权；go-ahead 放行；checkpoint 检查点。
- **流程**：the five stages of a Sprint（Why、What、How、Increment、Test）；refinement 精化（七步）；Review、Retro 与收官提交；small Sprint 小冲刺；kernel 内核（ideo、scrum、sprint、design 四个技能）；commitments hook 承诺 hook；design sprint 设计冲刺 与 the five modes 五模式（两件不同的事，名字都带「五」，这条最重要）。
- **来自 d.school 与《Sprint》**：Empathize、Define、Ideate、Prototype、Test；Point of View；How Might We；Five-Act Interview；rumble；Lightning Demos；Make a Map。

共约 35 条。你说行，我就按这份写；想加想减，直接说。

## D. README 的文件地图：收不收（要你定）

- 现状：占 README 近一半（约 100 行），逐条列了每份归档的冲刺日志，还夹着作者自己的东西（`.claude/`、记忆路径）；两种语言就是两份要同步，每次收官都要改。
- 建议：收到文件夹一级，约 15 行：根目录（README 两份、CHANGELOG、LICENSE、ATTRIBUTION、`docs/`、`scripts/`）、`plugins/ideo-scrum/`（`commands/`、`skills/` 四个内核、`hooks/`）、`codex/`（生成的 Codex 包）、`scrum/`（本项目自己的 Scrum 工作，也是示例）。归档的冲刺日志不逐条列。
- 连带：CHANGELOG 和 README 的版本号只剩两份 README 的首行；CLAUDE.md 里「README 是文件索引」「两处版本号」的说法要改（收官时由 Master 在你的会话里改）。
- 你的三个选择：① 收到文件夹一级（我推荐）；② 照现在逐条列，中英各一份；③ 删掉文件地图，只留一句指向 `scrum/` 和 `plugins/`。

## E. 图标：挑一个（要你定）

看 `scrum/sprint-20-presentable/icon-candidates/sheet.png`（浅色、深色背景，200、64、32 像素）；三张都是 SVG，挑定后我导出 PNG 放进插件。

1. **冲刺的环绕着设计的菱形**：深蓝底、奶白的环带箭头、琥珀色菱形。一眼两半都有：环是 Sprint，菱形是设计。缺点：环带箭头有点像「刷新」。
2. **三张便利贴**：浅灰底，蓝、粉、黄三张叠着，最前面一张有两行字。IDEO 工作坊的味道，亲切。缺点：像个通用的笔记应用。
3. **双钻石带一个箭头**：蓝底，一空一实两个白菱形，接缝处一个琥珀色箭头。设计过程里常见的「双钻石」，加上交付的箭头。缺点：懂设计的人才一眼认得。

我倾向 1：小到 32 像素还认得出，两半都在。口味归你。
