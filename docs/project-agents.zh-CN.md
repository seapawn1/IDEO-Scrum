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
- **上下文是干净的。** 入口只传你的问题、你的约束和文件路径，不传此前讨论、不传草拟的答案、也不传你的倾向。
- **答案是参谋的。** 它带着结论和依据回来，决定仍归你。

**关于模型。** 参谋的定义请求 Fable。若你在这次调用里点名别的模型，只对这一次生效，不保存任何设置。宿主实际跑的是不是那个模型，**本入口不验证**——请求、被替换、不可用这三种情况的核对属于后续配置项；在那之前，答案不会被说成是某个具体模型的成果。

## 从产品日志登记 Stakeholder

```text
/ideo-scrum:project-stakeholder
```

1. Product Owner 在产品日志 `scrum/ProductBacklog.md` §2.1 的 Stakeholder 表里点名一个 Stakeholder——表可以是任意语言，角色排在行上或排在列上都行。
2. 登记那张角色卡；入口先展示要写的定义文件、以及要加的那一行相对引用，你接受之前什么都不写。
3. 拒绝则两处都不动。名字已被占用时只报告、不覆盖，也不靠改另一个作用域来清重名。
4. 更新时，旧定义保持原样，直到新的定义被接受；写到一半失败，逐项报告哪一处成了、哪一处没成。

## 按名召唤

登记之后，同一份文件供两个入口使用：

```text
Agent, subagent_type: "security-reviewer"
```

- **普通 Agent 按名调用**，来自 Claude Code 或 Developer 会话。
- **Workflow 的 agent 步骤**，写同一个 agent 类型，不把角色正文粘贴进脚本。
- **临时看一眼**，由 `stakeholder` 入口按同一张角色卡起一个新子代理，不落任何文件。

刚写好的定义在同一轮里看不到：它在那个会话的下一条用户消息边界生效。Workflow 还会把触发它的请求一并交给子代理，所以启动一次评议的那段提示也不要夹带倾向。

## 宿主边界

- **Claude Code** 是这两处入口的建成与实测宿主；上面引用的宿主行为测于 2.1.329 版。
- **DSH 不包含这两处入口。** 它的包只带四个内核和四个角色命令，本文不为「项目级 Agent 在 DSH 上可用」作任何声明。
- **没有 Workflow 的项目**照样能按名普通召唤已登记的角色；Workflow 只是第二个入口，不是前提。
