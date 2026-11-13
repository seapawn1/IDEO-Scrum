# 快速上手

一页，从装好插件到你的第一个冲刺收官。你在一个 Claude Code 会话里当 Product Owner，Scrum Master 陪在旁边。默认你懂 Scrum；插件自己的词，[词汇表](glossary.md)里有解释。

## 开始之前

- 插件已经装好（[README](../README.zh-CN.md#安装)）。
- 你的项目是个 git 仓库。不是的话，可以让 Scrum Master 替你运行 `git init`；这只是建议，不是规定。

## 1. 叫出 Scrum Master

在 Claude Code 会话里：

```text
/ideo-scrum:scrum-master
```

然后说你在做什么。你是 Product Owner：价值和方向由你定，Scrum Master 为你服务。

## 2. 写产品日志

Scrum Master 和你一起写 `scrum/ProductBacklog.md`：产品、Product Goal，还有几条条目。通常它会自己先把事实查清，再把只有你能定的事放进一条带编号的消息里，每个问题都附上推荐的答案。文件开头是这样的：

```markdown
### 1.1 Product

| Commitment | Daily Quote: a small command that prints one quote a day. |
| --- | --- |

### 1.2 Product Goal

| Commitment | A morning ritual: a command you enjoy running every day. |
| --- | --- |
```

「Commitment」那几行逐字写着你的目标。它们保持不变，只有你能改。

## 3. 开一个冲刺

请 Scrum Master 开一个冲刺。它会有一条分支和一个文件夹 `scrum/sprint-01-<名字>/`，要过五个阶段。每个阶段结束，由你决定往不往下走：

| 阶段 | 做什么 | 你定什么 |
| --- | --- | --- |
| Why | 定下 Sprint Goal | Sprint Goal |
| What | 从产品日志里选条目，并精化 | 精化到此为止 |
| How | 写一份计划，不写步骤 | 放行 |
| Increment | 动手做，笔记记在冲刺日志里 | 可以进入测试了 |
| Test | 测试和审阅 | 收官，或者回去再做 |

看过计划，再说「放行」。认可计划不算放行：放行之后才动手。你的第一个冲刺可以很小；半小时的活也开一个，每一步缩成一两行。

## 4. 做和测

由一个 Developer 会话（`/ideo-scrum:developer`）来做，或者由 Scrum Master 来做。不管谁做，都由别人审阅：Scrum Master 自己做的，就由一个全新子代理审阅。测试的方法和过线的标准，先写下来，再跑测试。git 的活可以让 Scrum Master 替你做。

## 5. 收官

Test 阶段完成后，说「收官」。Review 和 Retro 装进一个收官提交：冲刺日志压缩后归档到 `scrum/documents/`，产品日志刷新一遍，教训写进项目的记忆或指令文件。这个提交打上冲刺文件夹的名字作 tag，合并进主分支；这些 Scrum Master 可以替你做。推送要等你点头。

## 值得记住的规矩

1. 每个阶段结束，由你决定往不往下走（[overview](../plugins/ideo-scrum/skills/scrum-kernel/overview.md)，第 12 条）。
2. 你放行之后才动手（[冲刺日志约定](../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md)，第 8 条）。
3. Sprint Goal 不变，计划可以调（overview，第 17 条）。
4. 审阅的人不是做的人（冲刺日志约定，第 14 条）。
5. 日志就是交接：冲刺日志开头的 `Now` 和 `Waiting for PO` 两行，写着冲刺到哪了、什么在等你（冲刺日志约定，第 22 条）。

## 书面授权

你可以把自己的一部分决定书面交给 Scrum Master：在冲刺日志的增量笔记里写一行，说清谁、管什么、覆盖哪几个阶段。例如：

```text
书面授权，2026-11-14：Product Owner 把 Why 和 What 两个阶段结束时的决定交给 Scrum Master。改承诺、取消冲刺、同意推送，仍由 Product Owner 定。
```

## 迷路了怎么办

- 问「现在到哪了？」：Scrum Master 读 `Now` 和 `Waiting for PO` 两行，告诉你。
- 要看板：一页看清项目走到哪，由日志写成 `scrum/Board.html`。
- 想弄清人要什么，叫 Designer：`/ideo-scrum:designer`。
