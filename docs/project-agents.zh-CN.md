# 项目 Agent

插件有两处新东西，让项目随时能请到一个外面的视角：一个只读的**参谋**，用来复核待定的决定；一个按角色卡**登记的项目 Stakeholder**，角色卡由 Product Owner 在产品日志里定过。两处都在 Claude Code 里工作；DeepSeek Harness（DSH）那侧的情况放在最后说明。

## 参谋还是项目 Stakeholder

它们回答的是不同的问题，要哪个由 Product Owner 定。

| | 参谋 | 项目 Stakeholder |
| --- | --- | --- |
| 要问的事 | 「照这些材料看，这个决定站得住吗？」 | 「这个人或这类人怎么看这个产品？」 |
| 身份从哪来 | 没有身份，只读你点名的文件 | 产品日志 Stakeholder 表里的一张角色卡 |
| 怎么请 | 每次都走 `/ideo-scrum:second-opinion` | 项目里留一份文件，按名召唤 |
| 它能做什么 | 读点名文件、加载内核 | 与 `stakeholder` 入口给出的同一个外部视角 |

## 请参谋

入口收三样：待定的问题、约束、要读的确切文件。

```text
/ideo-scrum:second-opinion Can we switch the library's door system next Monday? constraints: decide from the originals only | files: materials/launch-checklist.md
```

- **只能手动发起。** Claude 不会自己去请它，入口也不在 Claude 可自动调用的技能列表里；由你启动。
- **交给参谋的说明是干净的。** 入口只传你的问题、你的约束和文件路径，不传此前讨论、不传草拟的答案、也不传你的倾向。
- **答案是参谋的。** 它带着结论和依据回来，决定仍归你。

**关于模型。** 参谋的定义请求 Fable，要你的账号有权限。想用别的模型，在请求后面加上 `| model: opus`（或别的名字）；入口只在本次调用中请求该模型，不更改任何设置。若你的账号用不了 Fable，入口会说明并问你换哪个模型。**本入口不验证**宿主实际用了哪个模型。指定模型是否实际运行、被替换或不可用，留待后续核对；入口不把答案归给某个具体模型。

## 从产品日志登记 Stakeholder

```text
/ideo-scrum:project-stakeholder
```

1. Product Owner 在产品日志 `scrum/ProductBacklog.md` §2.1 的 Stakeholder 表里点名一个 Stakeholder——表可以是任意语言，角色排在行上或排在列上都行。
2. 登记那张角色卡；入口先展示要写的定义文件、以及要加的那一行相对引用，你接受之前什么都不写。写 `.claude/` 时 Claude Code 还可能另外问一次写入权限；那是宿主自己的提示，和你对预览的接受是两回事。
3. 拒绝则两处都不动。名字已被占用时只报告、不覆盖，也不靠改另一个作用域来清重名。
4. 更新时，旧定义保持原样，直到新的定义被接受；写到一半失败，逐项报告哪一处成了、哪一处没成。

## 按名召唤

登记之后，同一份文件供下面前两种用法使用，第三种不需要文件：

```text
Agent, subagent_type: "security-reviewer"
```

- **普通 Agent 按名调用**，来自 Claude Code 会话或 Developer 会话；Review 的外部视角仍只由 PO 或 Scrum Master 召唤。
- **Workflow 的 agent 步骤**，写同一个 agent 类型，不把角色正文粘贴进脚本。
- **临时看一眼**，由 `stakeholder` 入口按同一张角色卡起一个新子代理，不落任何文件。

实测的交互会话中，新写的定义在下一条用户消息时生效，同一轮内不可调用。本次无头 `-p` 流式会话实测未在下一轮加载新定义。Workflow 还会把触发它的请求一并交给子代理，所以启动一次评议的那段提示也不要夹带倾向。

## 宿主边界

- **Claude Code** 是这两处入口的建成与实测宿主；上面引用的宿主行为测于 2.1.329 版。
- **DSH 不包含这两处入口。** 它的包只带三个内核和四个角色命令，本文不为「项目级 Agent 在 DSH 上可用」作任何声明。
- **没有 Workflow 的项目**照样能按名普通召唤已登记的角色；Workflow 只是第二个入口，不是前提。
