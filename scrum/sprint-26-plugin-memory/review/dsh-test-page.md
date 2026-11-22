# DSH 要测的内容（Sprint 26 行 4，判据⑥，只测 A1）

给秘书会话（`IDEO # [supporter]-[main]-[support PO]`）在本机 DSH（0.2.2-rc.5，web profile 在 127.0.0.1:3080）上测。**只读探测：不改仓库里任何文件，不动现有 profile。** PO 2026-11-23 选定 A1（「26那就选择A1把，然后dsh要支持要记得」），这页只写 A1。

## A1 在 DSH 里是什么（我读了 `dsh/index.js`、`scripts/check_dsh.mjs`，并在副本上做过）

- **现状**：适配器把四个内核注册成技能；四个角色入口（`/scrum-master`、`/developer`、`/designer`、`/stakeholder`，用户可叫、模型不可叫）的正文＝工具映射＋路由说明＋**预载 ideo、scrum 两个内核正文（各带一行 `Base directory`）**＋角色命令正文。没有「叫出角色时触发」的钩子可用，所以 DSH 带上东西只能靠适配器预载，不是调 Skill。
- **A1 要改的**：`memory` 也当内核注册，并排在预载的第三位。`dsh/index.js` 3 行加 3 行删（内核列表加一项；预载按名字取 ideo、scrum、memory；路由说明里提一句 Memory）；`scripts/check_dsh.mjs` 4 行加 2 行删（内核列表；预载断言改成按序含 ideo、scrum、memory）；新增技能目录 `plugins/ideo-scrum/skills/memory/`（SKILL.md＋`long/`）。
- **在 HEAD 的副本上做过**：`node --test scripts/check_dsh.mjs` 改前 7/7、改后 7/7。副本在 `S:\IDEO-Scrum-Archives\sprint-26-plugin-memory\dsh-a1-copy\`（仓库外）。
- **DSH 侧没有新机制**：与 Claude Code 的差别只是「入口按序调 Skill」换成「适配器预载」。清单里的 `→ long/<文件>.md` 靠预载里那行 `Base directory` 解析，同现在内核里 `references/` 的路径一样。
- **体量**：角色正文现在约 26k 字符（两个内核），A1 加清单约 14.7k，到约 41k。

## 请测的问题（每条给「是／否／不确定」和一句证据）

1. 在 DSH 里叫出一个角色（如 `/developer`），预载的内核正文是否真的在会话上下文里，而且完整（正文最后一段也在）？用会话日志里 `user/message` 的 `skill-invocation` 来源核对，不靠模型复述。
2. DSH 压缩上下文之后，这份角色正文（含预载内核）还在吗：完整、被截，还是只剩摘要？A1 会让它涨到约 41k 字符，请顺带报：DSH 有没有给单个技能正文或预载总量设上限（配置里、日志里的截断标记）。
3. 在角色会话里，让模型按预载里的 `Base directory` 读技能目录下的一个文件（如 `scrum-kernel` 的 `references/` 下任一份），读成功了吗？（A1 的 `long/` 走的是同一条路。）
4. 新增一个模型可调用的技能（`memory`）会不会让技能清单变长到影响别的技能触发？只报清单里每条描述的长度上限。
5. 子代理（对应判据③，只报）：模型在角色会话里派出的子代理会不会继承角色正文？

## 可选：真跑 A1（Master 定要不要）

上面五条测的是 A1 靠的机制。想看 A1 真跑，要一份带改动的包，就是上面的副本。**另建一个临时 profile 指向副本，试完删；不要动现在的 profile，不要用 `dsh plugin add`**（它会重写 profile，丢掉其他 bundle）。真跑时看：

- 叫 `/developer` 后，上下文里有没有 Memory 的开头（`# IDEO-Scrum Memory`）和结尾（最后一行 `departures`）；
- 发一次压缩，再问一个答案只在清单里的问题，如「清单里 `outward-needs-po` 那一行怎么说」（原句：`Push, release and other outward actions need the PO's consent; a stage permission never covers commit, merge or push.`）和「`departures` 那一行说什么」，对照原句，看开头、结尾都还在。

## 回给我的格式

每题一行：`题号｜是／否／不确定｜证据：日志里的哪一条／哪个文件`。不要贴模型的原话当证据；查环境变量只列名字，不打印值；原始日志放仓库外，别把提供方地址、凭据写进回复。
