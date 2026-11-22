# DSH 要测的内容（Sprint 26 行 4，判据⑥）

给秘书会话（`IDEO # [supporter]-[main]-[support PO]`）在本机 DSH（0.2.2-rc.5，web profile 在 127.0.0.1:3080）上测，只读探测即可，**不改仓库里任何文件**。这页在 Claude Code 一侧出结果之后定稿：只保留还在选项里的案子。先写的是共同前提和每个案子在 DSH 里的做法。

## 共同前提（我已读 `dsh/index.js`、`scripts/check_dsh.mjs` 得到的事实）

- DSH 适配器只用 `ctx.skills.register`（注册四个内核和四个角色入口）与 `ctx.systemPrompt.context`（一段命名上下文 `ideo-scrum:commitments`，order 130，`text: ({ agent }) => …`）。没有“叫出角色时触发”的钩子可用。
- 角色入口（`/scrum-master`、`/developer`、`/designer`、`/stakeholder`）在 DSH 里是用户可叫、模型不可叫的技能；它的正文＝工具映射＋路由说明＋**预载的 ideo-kernel 与 scrum-kernel 正文（逐字）**＋角色命令正文。`sprint-kernel`、`design-kernel` 按需另载。
- `scripts/check_dsh.mjs` 断言：注册的技能名＝四内核＋四角色；每个角色的正文里按序含 ideo、scrum 两个内核正文，且不含 sprint／design 内核。
- 命令文件里写着“DSH 一侧照宿主适配器的预载与路由，不照 Claude Code 的 Skill 调用序列”，所以**无论哪个案子，DSH 带上 Memory 的方式都是适配器的预载，不是调 Skill**。

## 每个案子在 DSH 里怎么做（我的读法，待你们的实测证实或推翻）

| 案子 | DSH 要做的 | 要改的地方 |
| --- | --- | --- |
| A1 独立 `memory` 技能 | 适配器把 `memory` 也注册为技能，并在角色正文的预载里加上它 | `dsh/index.js`（内核列表、`rolePrelude`）、`scripts/check_dsh.mjs`（内核列表、“预载两个内核”的断言改成三个） |
| A2 并入 `scrum-kernel` | 不用改：DSH 本来就逐字预载 `scrum-kernel` | 无（`check_dsh` 照过）；代价：Stakeholder 也预载了 |
| B hook | DSH 没有这个钩子；等价的做法是适配器按角色把 Memory 的角色段拼进角色正文（不是钩子），或走 `systemPrompt.context` | `dsh/index.js` 里加读 Memory、按角色选段的代码；`check_dsh` 加断言；Claude Code 一侧的 hook 脚本在 DSH 里用不上，所以是**两套实现** |
| C 合用 | DSH 一侧同 A1；压缩后补注靠 DSH 自己的回放 | 同 A1，另要确认 DSH 压缩后角色正文还在 |

## 请你们实测的问题（每条给“是／否／不确定”和一句证据）

1. 在 DSH 里叫出一个角色（如 `/developer`），预载的内核正文是否真的在会话上下文里？（用会话日志里 `user/message` 的 `skill-invocation` 来源核对，不靠模型复述。）
2. DSH 压缩上下文之后，这份角色正文（含预载内核）还在吗？还是只剩摘要？对 A1：压缩后另一个按名字注册的技能还在吗？
3. `ctx.systemPrompt.context` 的 `text` 回调拿到的 `agent` 里，能不能知道这个会话**叫过哪个角色**？能的话，B 在 DSH 里可以做“只在叫过角色的会话里注入”；不能的话 B 只能拼进角色正文。
4. 模型能不能在一个角色会话里自己用 `skill` 工具按名字调用一个**模型可调用**的技能（如将来的 `memory`）？调用成功后正文进上下文吗？
5. DSH 里新增一个模型可调用的技能，会不会让技能清单（描述）变长到影响别的技能的触发？（只报清单里每条描述的长度上限。）
6. 子代理：DSH 里模型派出的子代理会不会继承角色正文？（对应判据③。）

## 回给我的格式

每题一行：`题号｜是／否／不确定｜证据：日志里的哪一条／哪个文件`。不要贴模型的原话当证据；查变量只列名字，不打印值；原始日志放仓库外，别把提供方地址、凭据写进回复。
