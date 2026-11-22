# 快速上手

一页，从装好插件到你的第一个冲刺收官。你在一个 Claude Code 或 DeepSeek Harness（DSH）会话里当 Product Owner，Scrum Master 陪在旁边。默认你懂 Scrum；插件自己的词，[词汇表](glossary.md)里有解释。

## 开始之前

- 插件已经装好（[README](../README.zh-CN.md#安装)）；已经装过旧版的，看[升级说明](../README.zh-CN.md#升级)。
- 你的项目是个 git 仓库。不是的话，可以让 Scrum Master 替你运行 `git init`；这只是建议，不是规定。

## 1. 叫出 Scrum Master

在 Claude Code 会话里：

```text
/ideo-scrum:scrum-master
```

这个 Claude Code 命令先依次调用 IDEO、Scrum、Sprint 和 Design 内核，再调用 Memory，然后开始工作；不用你逐个调用。其他角色的顺序见[角色规矩](../plugins/ideo-scrum/skills/memory/details/roles.md)。

在项目目录里新开的 DSH **Standard** 会话中：

```text
/scrum-master
```

说你在做什么。在 DSH 里，任务可以和 `/scrum-master` 写在同一条消息里，跟在它后面。你是 Product Owner：价值和方向由你定，Scrum Master 为你服务。

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

「Commitment」那几行逐字写着你的产品陈述和目标。它们保持不变，只有你能改。表下可以写解释，但解释不是承诺的一部分。如果你还说不出产品是什么、Product Goal 该是什么，Scrum Master 会和你一起开一个设计，等你放行后再开始共情。

## 3. 开一个冲刺

请 Scrum Master 开一个冲刺，并放行 Why。它会有一条分支和一个文件夹 `scrum/sprint-01-<名字>/`，要过五个阶段。阶段结果由你定，进入或返回阶段也等你明确放行；只认可结果不算开始下一阶段：

| 阶段 | 做什么 | 你定什么 |
| --- | --- | --- |
| Why | 定下 Sprint Goal 与核验重点，完整 DoD 仍生效 | Sprint Goal；是否开始 What |
| What | 从产品日志里选条目，并精化 | 精化到此为止；是否开始 How |
| How | 写一份计划，不写步骤 | 放行 |
| Increment | 动手做，笔记记在冲刺日志里 | 可以进入测试了 |
| Test | 测试和审阅 | 收官，或者回去再做 |

看过计划，再说「放行」。认可计划不算放行：放行之后才动手。Scrum Master 可能把写计划或施工交给在后台干活的 Developer；等得久了，就问「计划好了吗？」，或者叫 Scrum Master 自己来写。你的第一个冲刺可以很小；半小时的活也开一个，每一步缩成一两行。

## 4. 做和测

由一个 Developer 会话（Claude Code 用 `/ideo-scrum:developer`，DSH 用 `/developer`）来做，或者由 Scrum Master 来做。不管谁做，都由别人审阅：Scrum Master 自己做的，就由一个全新子代理审阅。Test 的方法和过线标准先写下来。施工自检不等于 Sprint Test，进入仍要等你放行。日志逐项追溯 Output Done 与条目判据的证据——即使不是本期重点也不豁免——包括旧证据及仍有效的原因，或明确的条件未触发及未适用的原因。Outcome 信号另记；事前约定本期必须验证的信号，要有达标证据才能判 Test 通过。git 的活可以让 Scrum Master 替你做。

## 5. 收官

Test 阶段完成后，说「收官」。Review 把冲刺日志压缩后归档到 `scrum/documents/`，刷新产品日志。Retro 只把重要教训一条一条写进项目记忆；工具没有项目记忆时，存入仓库里逐条可找回的教训笔记，不写指令文件或每期 Retro 汇总。没有重要教训就不写条目。一个收官提交只装 Review 和 Retro 实际产生的仓内改动，不复制仓外记忆，也不为提交凑 Retro 文件。已结束设计的原始材料随日志归档；承接其结论的冲刺只引用它，不在收官时删掉原件。这个提交打上冲刺文件夹的名字作 tag，合并进主分支；这些 Scrum Master 可以替你做。推送要等你点头。

## 值得记住的规矩

1. 阶段结果由你定；进入或返回阶段等你明确放行（[Memory](../plugins/ideo-scrum/skills/memory/SKILL.md) 的 `stage-gates`）。
2. 你放行之后才动手（[Memory](../plugins/ideo-scrum/skills/memory/SKILL.md) 的 `go-ahead`、`review-handover`）。
3. Sprint Goal 不变，计划可以调（Memory 的 `goal-fixed`、`commitment-table`）。
4. 审阅的人不是做的人（Memory 的 `reviewer-required`）。
5. 日志就是交接：冲刺日志开头的 `Now` 和 `Waiting for PO` 两行，写着冲刺到哪了、什么在等你（Memory 的 `log-is-the-handoff`）。

## 书面授权

你可以把自己的一部分决定书面交给 Scrum Master：在冲刺日志的增量笔记里写一行，说清谁、管什么、覆盖哪几个阶段。交出的阶段放行权要明确写出；交审阅或阶段内选择，不等于交出进入下一阶段的决定权。例如：

```text
书面授权，2026-11-14：Product Owner 把定 Why 和 What 的结果、放行进入 What 和 How 的决定交给 Scrum Master。改承诺、取消冲刺、同意推送，仍由 Product Owner 定。
```

## 迷路了怎么办

- 问「现在到哪了？」：Scrum Master 读 `Now` 和 `Waiting for PO` 两行，告诉你。
- 要看板：一页看清项目走到哪，由日志写成 `scrum/ScrumBoard.html`。交给 supporter（秘书）：Claude Code 用 `/ideo-scrum:supporter`，DSH 用 `/supporter`。
- 想弄清人要什么，叫 Designer：Claude Code 用 `/ideo-scrum:designer`，DSH 用 `/designer`。
- 想请一个外面的视角，或请参谋给第二意见，见[项目 Agent](project-agents.zh-CN.md)。
