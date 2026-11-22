# DSH 要测的内容（Sprint 26 行 14，真插件）

给秘书会话（`IDEO # [supporter]-[main]-[support PO]`）在本机 DSH 上测，经 Master 转。载体测试那次（`review/memory-outline.md` 第 10 节，DSH 0.2.3-alpha.2）测的是副本和机制；这次测落盘之后的**真插件**。**只读探测：不改仓库里任何文件，不动现有 profile，不用 `dsh plugin add`**（它会重写 profile、丢掉其他 bundle）。

## 先备好

- **临时 profile 指向我的工作树**：`S:\IDEO-Scrum\.claude\worktrees\sprint-26-plugin-memory`（分支 `worktree-sprint-26-plugin-memory`，插件树在它的 HEAD）。做法照 `dsh-profile-link-change` 的老办法（手改 package.json＋junction＋锁文件，测完删）。测的过程中我不动 `plugins/` 与 `dsh/`；若要动，会先通知。
- 版本与日期随结果记：DSH 版本、包版本（现在的 `plugin.json` 还是升版前的）。
- 原始日志放仓库外，别把提供方地址、凭据写进回复；查环境变量只列名字，不打印值。

## 请测的问题（每条给「是／否／不确定」和一句证据）

1. **五个入口预载齐全**：`/scrum-master`、`/developer`、`/designer`、`/stakeholder`、`/supporter` 各叫 **3 个新会话**。每个会话的 `user/message`（`skill-invocation` 来源）里，三份预载内核——ideo、scrum、**memory**——都在，memory 完整：开头 `# IDEO-Scrum Memory`，结尾是 `departures` 那一行（`**departures** The plugin departs from the Scrum Guide on purpose in seven places…`）；且这条消息在模型做任何别的事之前。过线：每个入口 3/3。（角色入口正文里有一行「**Memory**: …」，可顺带看到。）
2. **压缩后没人问起清单时，模型会自己重载吗**：叫 `/developer`，发一次压缩，然后发一个**与清单无关的普通任务**，但做对它要用清单里的规矩，例如「要开一个新冲刺，做登录页的重做，帮我定一下它的文件夹叫什么」（Memory 的 `sprint-folder` 一行：`scrum/sprint-NN-<后缀>/`）。看模型在回答之前有没有调 `skill`（`{"name":"memory"}`）。**3 个会话，只报 n/3**。另看命名上下文 `ideo-scrum:memory`（那句「压缩后重新调用 memory」的提示）是否在压缩后的每一轮都回放。
3. **子代理（只报）**：叫 `/developer`，让模型派一个子代理做一件事（如「给一个关于登录页重做的新冲刺起个文件夹名，只回名字」），看：子代理有没有加载 memory（它自己的 `skill(memory)` 调用）；主会话写给子代理的委托消息里有没有写「先加载 ideo、scrum、memory」。**3 个会话**。载体测试那次的结论是：DSH 的子代理只拿到委托消息、技能清单和运行时上下文，不继承角色正文。
4. **技能清单（只报）**：memory 的描述（353 字符）放得下；四个内核的描述被截到 500 字符的情况照旧（不是本期的事，Master 已另登记）。

## 回给我的格式

每题一行：`题号｜是／否／不确定｜n/m｜证据：日志里的哪一条／哪个文件`。不要贴模型的原话当证据。
