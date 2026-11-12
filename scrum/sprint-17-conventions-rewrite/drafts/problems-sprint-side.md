# 冲刺侧全文：找到的问题与每处的建议

> 照 sprint-log 第 12 条：全文附问题与建议，交 Master 审。文件都在 `drafts/` 里，按新布局放。

## 改了什么（对照 outline.md）

| 文件 | 改动 |
| --- | --- |
| `drafts/sprint-kernel/conventions/sprint-log.md` | 第 5 条加「照抄 2.1 时查够不够」（54 ④）；第 6 条第 4 步改指 ideo 约定第 1 条（56 连带）；第 10 条写明什么算卡住（54 ②）；第 17 条写明怎么判过时（54 ③）；第 22 条加 Now 行（54 ①）；新增第 26 条（53）；贯穿全程的范围写到 26；跨技能路径改 `../scrum-kernel/…`、`../ideo-kernel/SKILL.md`，开头改「相对 sprint-kernel 技能文件夹」 |
| `drafts/sprint-kernel/conventions/sprint-backlog-template.md` | 头部加 Now 行（54 ①，注释指向第 22 条）；头部路径改 sprint-kernel、overview 与 product-log 改 `../scrum-kernel/…` |
| `drafts/scrum-kernel/conventions/product-log.md` | 第 2 条加指向 ideo 约定（56 连带）；第 12 条收成指向 sprint-log 第 5 条（54 ④）；第 17 条指向 sprint-log 第 17 条（54 ③）；sprint-log 路径改 `../sprint-kernel/…`；design 的 pick-a-target 路径改 `steps/2-3-…`（Sprint 16）；裸写的 overview 改 `../overview.md` |
| `drafts/scrum-kernel/overview.md` | 第 2 条加指向 ideo 约定（56 连带）；第 7 条定义「全新子代理」（46 ③）；第 12 条 design-log 条号 25→26（改号）；第 14 条加指向 sprint-log 第 26 条（53）；全部 sprint-log 路径改 `../sprint-kernel/…`；「other files」一行改 |

## 问题与建议

1. **sprint-log 搬家后的路径**：Sprint 16 的清单只写了「开头改 sprint-kernel」，但正文里裸写的 `overview.md`、`product-log.md`、`SKILL.md` 搬过去会失效。建议：跨技能的一律写 `../scrum-kernel/…`、`../ideo-kernel/SKILL.md`；同文件夹的 `sprint-log.md`、模板不变。已按此写，搬运时与 Sprint 16 的版本对一遍。
2. **54 ④ 的落点**：查够不够写进 sprint-log 第 5 条；product-log 第 12 条原来那句「The measure is the Sprint Goal…」收成指向，一条规矩只写一处。建议：保持。
3. **54 ② 的五种卡住**：等 PO 的决定或信息、外部阻塞、同一做法试两次不行、照现在的 How 看不出怎么达成 Sprint Goal；其余算计划内的调整。建议：保持。
4. **54 ③ 的过时定义**：现在不真了，或现在没人要读（历史在 git，删了不丢）；product-log 第 17 条指向这里。建议：保持。
5. **54 ① 的 Now 行**：模板头部加一行，第 22 条写明接手先读它；与设计模板的写法一致。建议：保持。
6. **53 写成角色和步骤**：谁在什么时候做什么；工具做法只在括号里当例子（两个会话直接发消息、从 Master 会话 fork 出的 Developer）。建议：保持；「PO 只传一句轮到谁」照 Sprint 13 的做法。
7. **46 ③ 的定义放 overview 第 7 条**：只从简报起步；fork、复制都不算；没有子代理的工具开一个只给简报的新会话。sprint-log 第 14 条不动，命令里用同一个词。建议：保持。
8. **56 的连带**：sprint-log 第 6 条第 4 步、overview 第 2 条、product-log 第 2 条都改成指向 ideo 约定第 1 条，不重复分界；scrum-kernel 的 SKILL.md 在上一批。建议：保持。
9. **改号**：overview 第 12 条的 design-log 条号 25→26 已按新号写；design-kernel `SKILL.md` 五阶段表的条号在搬运时进改号提交（见 `problems-design-side.md`）。建议：保持。
10. **模板章节清单不变**：只加头部 Now 行，其余章节与注释不增不减（54 ④ 的规矩在第 5 条，不在模板里重写）。建议：保持。
