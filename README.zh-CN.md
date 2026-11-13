<p align="center"><img src="plugins/ideo-scrum/icon.png" width="96" alt="IDEO-Scrum 图标：一个环绕着菱形的环"></p>

# IDEO-Scrum

一个 Claude Code 插件：把 Design Thinking 与 Scrum Sprint 带给你一个人加 AI 做的项目。**v6.0.2**

[English](README.md) · [安装](#安装) · [快速上手](docs/quick-start.zh-CN.md) · [词汇表](docs/glossary.md) · [更新记录](CHANGELOG.md)（英文）

> **授权提示。** 本插件里 d.school 的材料只许非商业使用，所以本仓库不算 OSI 意义上的开源软件。见[授权与署名](#授权与署名)。

## 这是什么

一个人带着 AI 做项目，规矩和工作的进度都在你脑子里和聊天里。会话结束，或者被压缩，它们就跟着没了。AI 会跑偏，除了做的那一个，没有别人看它做了什么。

IDEO-Scrum 给这份工作配一支 Scrum 团队。你当 Product Owner：方向、目标、哪些条目进冲刺、什么时候可以动手，都由你定。AI 扮演 Scrum Master、Developer、Designer 和 Stakeholder，一个角色一个命令。遇到「人要什么」「什么样算好」这类问题，它会带上 IDEO 和斯坦福 d.school 的设计思维：五模式，或者一次设计冲刺。所有东西都写进你仓库里的纯 Markdown 日志，换一个新会话，读日志就能接着干。

它不是项目管理工具：不接 JIRA 或 Linear，也不是给团队用的平台。

## 一次会话大概什么样

示意，已缩短，不是实录；措辞会不一样。要看的是它在哪儿停：每个阶段结束，工作都等你。

```text
你：           /ideo-scrum:scrum-master
               我想一个人做个小命令行工具，每天打印一句名言。帮我起个头。
Scrum Master： 先写产品日志：这个产品是什么，接下来要做到什么？
你：           每天早上打印一句名言。一个月后我还乐意用，就算做到了。
Scrum Master： 已写进 scrum/ProductBacklog.md：产品、Product Goal、三条条目。
               要开一个冲刺吗？
你：           开。
Scrum Master： Why，Sprint Goal：「每日一句：从清单里打印一句名言；加一句名言只要一条命令。」
               这就是目标。你来定，然后进 What？
你：           定了。
               ……What：你选条目、一起精化。How：Developer 写计划……
Developer：    计划写在冲刺日志第 3 章。你说「放行」之前，我不动手。
你：           放行。
               ……Developer 动手、记笔记；别人来审阅；你定什么时候收官……
```

留在你仓库里的是可以直接读、直接改的纯 Markdown：`scrum/ProductBacklog.md` 和 `scrum/sprint-01-<名字>/SprintBacklog.md`。[快速上手](docs/quick-start.zh-CN.md)一步一步带你走完全程。

## 适合谁

适合：

- 你用 Claude Code 做自己的项目，懂 Scrum，或者愿意把 Scrum Guide 放在旁边读（插件自带）。
- 你想让规矩跟着插件走，不用每个会话重新口述；会话断了、被压缩了，能从停下的地方接上。

不适合：

- 你要接 JIRA 或 Linear，或者要一个给整个团队用的平台。
- 你想让 AI 自己把项目跑完：默认每个阶段结束，工作都停下来等你。
- 你要一字不差的 Scrum Guide：见[和教科书上的 Scrum 有什么不同](#和教科书上的-scrum-有什么不同)。

## 安装

需要 Claude Code。你的项目最好是个 git 仓库；没有的话，Scrum Master 可以替你建。在 Claude Code 会话里：

```text
/plugin marketplace add seapawn1/IDEO-Scrum
/plugin install ideo-scrum@ideo-scrum
/reload-plugins
```

检查：在终端里运行 `claude plugin list`，里面 `ideo-scrum@ideo-scrum` 显示已启用。

Codex 是附带的版本，由同一份源生成；第一个冲刺的走法只在 Claude Code 上测过。在终端里：

```sh
codex plugin marketplace add seapawn1/IDEO-Scrum
codex plugin add ideo-scrum@ideo-scrum
```

然后在新的 Codex 会话里输入 `$`，从技能菜单里选角色：`$scrum-master`、`$designer`、`$developer`、`$stakeholder`。

## 升级

```sh
claude plugin update ideo-scrum@ideo-scrum
```

在终端里运行，然后在已经打开的会话里运行 `/reload-plugins`。第三方市场默认不会自动更新：想让 Claude Code 代劳，打开 `/plugin`，进 Marketplaces，选 `ideo-scrum`，选 Enable auto-update。每个版本改了什么，见[更新记录](CHANGELOG.md)（英文）。

Codex 上，先刷新市场，再把插件移除、重新装一遍。这条路我们没有完整测过。

```sh
codex plugin marketplace upgrade ideo-scrum
codex plugin remove ideo-scrum@ideo-scrum
codex plugin add ideo-scrum@ideo-scrum
```

## 第一句话怎么说

在 Claude Code 会话里，叫出一个角色：

```text
/ideo-scrum:scrum-master    # 主持 Planning、检查点、Review 和 Retro；审阅工作；服务你这位 Product Owner
/ideo-scrum:developer       # 跑一个冲刺：计划、增量、冲刺日志
/ideo-scrum:designer        # 研究与原型：五模式和设计冲刺；你没定之前不动手做
/ideo-scrum:stakeholder     # 对产品的外部视角，或者常驻做看板之类杂务的助手
```

或者用自己的话说：

```text
用 ideo-scrum 帮我规划下个冲刺，我们有 5 个待办项要精化
这个功能要不要做我拿不准，先做一轮用户访谈的设计
```

什么时候加载什么：Scrum、冲刺、设计冲刺的材料只有召唤才来——用角色命令，点名 ideo-scrum 或它的某个内核，或者要求建改它的日志；泛泛问 Scrum，照常回答。做原型、做测试时，IDEO 的方法常会自己介入；发散、定义问题时，模型多半直接作答，想用它的方法就点名 `ideo-kernel`（已知的限制）。

## 和教科书上的 Scrum 有什么不同

插件有意在七处和官方指南不一样。每一处在 [`overview.md`](plugins/ideo-scrum/skills/scrum-kernel/overview.md#departures-from-the-official-guides) 里只写一次，连同理由（英文）；这里是简版。

| 这里 | 为什么 |
| --- | --- |
| 只有 Product Owner 必须是人 | 一个人和 AI 一起干活，价值上的决定留在他手里 |
| 设计和冲刺并列 | 设计不交付增量，可以跨好几个冲刺，Designer 和 Developer 是平级 |
| 条目由 Product Owner 和 Scrum Master 一起定 | Product Owner 定价值方向，其他人说一次装得下多少 |
| How 是计划，放行之后才动手 | Scrum Master 和 Product Owner 查计划，因为 AI 可能跑偏 |
| 检查点代替 Daily Scrum | AI 按会话干活，不按天 |
| 必须有审阅者 | Developer 可能跑偏，再看一眼能抓住 |
| 没有冲刺截止日 | AI 按会话干活，所以由 Product Owner 在检查点盯着有没有冲刺拖太久 |

## 工作成果放在哪

你的项目里会长出一个 `scrum/` 文件夹。这是作者的布局；你的项目自己有地方放，就用自己的。

| 路径 | 里面放什么 |
| --- | --- |
| `scrum/ProductBacklog.md` | 产品日志：产品、Product Goal、条目 |
| `scrum/sprint-NN-<名字>/SprintBacklog.md` | 一个冲刺，从 Why 到 Test，连同它的笔记 |
| `scrum/design-<名字>/DesignBacklog.md` | 一次设计：研究和原型 |
| `scrum/ideo-<名字>/IdeoBacklog.md` | 一轮五模式 |
| `scrum/Board.html` | 看板：一页看清项目走到哪，由日志写成，自己不存状态 |
| `scrum/documents/` | 已结束的冲刺和设计的归档，以及整个项目共用的文件 |

插件把这些文件叫日志：产品日志就是 Product Backlog，冲刺日志就是 Sprint Backlog。真实的例子就是本仓库自己的 `scrum/` 文件夹，中文写的：先看 [`ProductBacklog.md`](scrum/ProductBacklog.md) 和一份归档的冲刺日志 [`sprint-19-board-hook.md`](scrum/documents/sprint/sprint-19-board-hook.md)。

## 了解更多

- [快速上手](docs/quick-start.zh-CN.md)：一页，从装好到走完你的第一个冲刺
- [词汇表](docs/glossary.md)：插件自己的词
- [`overview.md`](plugins/ideo-scrum/skills/scrum-kernel/overview.md)：各部分怎么配合，以及和官方指南的每一处不同（英文）
- [更新记录](CHANGELOG.md)：每个版本改了什么（英文）

## 授权与署名

本仓库的原创部分（插件的结构、技能的组织方式、`scrum/` 里的工作记录）以 [MIT 许可](LICENSE)发布。插件里带的方法来自四个来源，各有各的条款，MIT 不覆盖它们：

| 来源 | 许可 |
| --- | --- |
| *The Scrum Guide* 2020，Ken Schwaber 与 Jeff Sutherland | CC BY-SA 4.0 |
| *Scrum Guide Expansion Pack* 2026.1，Ralph Jocham、John Coleman 与 Jeff Sutherland | CC BY-SA 4.0 |
| *Design Thinking Bootleg*，Stanford d.school | CC BY-NC-SA 4.0（非商业） |
| *Sprint*，Jake Knapp 与 John Zeratsky、Braden Kowitz（Simon & Schuster，2016） | 保留全部权利 |

d.school 的许可禁止商业使用，所以本仓库不算 OSI 意义上的开源软件。打算商业使用的话，先读 [ATTRIBUTION.md](ATTRIBUTION.md)。

《Sprint》一书，插件里带的是讲方法的那几章的删节摘录，没有插图，也不是全书；这套方法对你有用的话，请买原书。每一份摘录都写明了出处和许可，[ATTRIBUTION.md](ATTRIBUTION.md) 列出了它们各在哪里。IDEO-Scrum 是独立的作品，和 Scrum.org、scrumexpansion.org、Stanford d.school、IDEO、Simon & Schuster 都没有关联。

## 反馈

发现了问题，或者有想法？开一个 [issue](https://github.com/seapawn1/IDEO-Scrum/issues)。写上你在哪里用（Claude Code 还是 Codex、它的版本、你的操作系统）、你说了什么、你看到了什么，会有帮助。

## 文件

| 路径 | 是什么 |
| --- | --- |
| `plugins/ideo-scrum/` | 插件本体：`commands/` 里四个角色，`skills/` 里四个内核（ideo、scrum、sprint、design），还有 `hooks/` |
| `codex/plugins/ideo-scrum/` | Codex 版，由 `scripts/sync_codex.py` 从插件本体生成，不要手改 |
| `docs/` | 快速上手和词汇表 |
| `scrum/` | 本项目自己的 Scrum 工作，中文写的：它的产品日志和归档的冲刺日志 |
| `scripts/` | 生成、核对 Codex 版和文档的脚本 |
| `.claude-plugin/`、`.agents/plugins/` | Claude Code 和 Codex 的市场清单 |
| `LICENSE`、`ATTRIBUTION.md`、`CHANGELOG.md`、`CLAUDE.md` | 许可、来源和它们的条款、更新记录、改这个仓库时用的指令 |
