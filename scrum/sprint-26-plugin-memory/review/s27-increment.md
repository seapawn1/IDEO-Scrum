# 27 增量表（Sprint 26 行 11 的底稿）

依据：Master 2026-11-23 给的「27 改了哪些」，加我对着 `git diff 2cb9420 2572530`（main 的 `2572530`，tag `sprint-27-wrap-up`）读到的最终文字。**这是同步前的预读，草稿本体和插件都没动**；按 Master 的顺序，先跑完 A1 正式测，再把 main 同步进分支，同步后照这张表逐项改，并重跑台账抽取与逐条文本比对（不靠这页）。

## 一、规矩变了的

| 27 改了什么 | 对草稿的影响 | 同步后怎么办 | 含义变了？ |
| --- | --- | --- | --- |
| `overview.md` 约定 8：角色表加 Supporter 一行（杂活、PO 的联络点；加载 ideo → scrum）；Stakeholder 一行缩成「An outside view」 | `role-entry` 一行字不变；`roles-and-routing.md` 的角色表过时 | 长文件角色表加 Supporter、改 Stakeholder 行；加载数 Master 5、Developer 4、Designer 4、Stakeholder 3、Supporter 3（ideo → scrum → memory） | 是（新增一个角色），交 Master 审 |
| 约定 10：句末加「convention 14 says where each kind goes」 | `ask-the-po`（待 27）要重写 | 见下面约定 14 | 是 |
| 约定 12：「stage permission（不是工具权限）」；新句：Supporter 按约定 14 转达的 PO 原话算数 | `stage-gates` 一行与 `stage-gates.md` 长文件缺这一句 | 行里「permission」改「stage permission」；长文件加那一句并指向 `po-word-relayed` | 是（新增一句），交 Master 审 |
| 约定 14 整条重写：杂活（看板、汇总、产品日志整理）归 Supporter，外部视角仍来自全新子代理；新增四小条：**Supporter 做什么**、**问题往哪走**（自己定 → 问 Master → 经 Supporter 交 PO；没有 Master 会话就直接问 PO，没有 Supporter 会话就直接问 PO）、**答复怎么回**（原话带回；PO 对范围、条目、放行的决定交 Master 记）、**PO 的话经转达算数**（要标明是 PO 的意见、带原话、日期、在哪里说的；接收方记成 `PO (via Supporter): <原话>`；不含工具权限与设置、CLAUDE.md／AGENTS.md、推送与发布） | `who-gets-which-work`、`ask-the-po`（都标待 27）要重写；四小条是新规矩，清单里没有 | 重写两行，新增两行，把细节放进 `roles-and-routing.md`（草案见下） | 是（整条新），交 Master 审 |
| `board-log.md` 搬到 `plugins/ideo-scrum/board/`；第 3 条「常驻助手会话」改成「the Supporter」；第 4 条加指向第 11 条；第 12 条 `solution` 为 `null` 时也省略 `story`；第 16 条「待归档」要明确写出 | `board-writer`（待 27）要重写；其余在留在原处的文件里，清单不用动 | 见第三节（board-log 的去处） | 第 3 条是 |
| `ideo-log.md` 约定 4：For 可以指向 `DesignBacklog.md`；结论可回产品日志、冲刺日志或设计日志 | `ideo-log-home`、`ideo-log-ends` 两行原句已泛指「它服务的日志」，不用改 | `ideo-ending.md` 长文件（手写）逐字跟新文 | 小，列入改动清单 |
| `product-log.md`、`sprint-log.md`、`design-log.md`：只改了模板路径（`../../template/…`）；四份模板搬到插件根的 `template/`，design 与 ideo 两份的 For 占位改了 | 清单与长文件里提到模板文件名的地方 | 同步后 grep 模板文件名，改路径 | 否 |
| `overview.md` 的「The other files」块与约定 4（文件夹）：模板在 `template/`，看板文件在 `board/` | `layers-and-folders.md` 长文件里的路径 | 改路径，板子的指向改成 `../../board/board-log.md` | 否 |

## 二、入口与外围（行 12–14 要对）

- **`commands/supporter.md` 新增**：Claude Code 加载序列 ideo → scrum（3 个技能含 memory，A1）；四个旧入口的「Ask the Product Owner」一条都改成指向约定 14，行 13 把它们迁成指向 Memory 句柄（`ask-the-po` 等）。
- **DSH**：`dsh/index.js` 角色表 5 个并加 locale，`check_dsh` 8 项。我在副本上做的 A1 改动（`rolePrelude` 预载 ideo、scrum、memory）要按新的 `dsh/index.js` 与 `check_dsh` 重做并重跑，supporter 入口也要预载 memory。
- **DSH 压缩后重载那句，备两种写法**（秘书实测：DSH 压缩把角色正文换成摘要，要模型自己重载 memory；Master 2026-11-23 定「到时候他定」）：
  - 写法 A，放 `dsh/index.js` 的 `roleRouting`（在角色正文里，压缩后可能跟着没了）：`The IDEO and Scrum kernels and the Memory are already loaded below, in that order; do not call `skill` again for those, except that after the conversation has been compacted you call `memory` again before going on.`
  - 写法 B，放 DSH 一直回放的命名上下文（`ctx.systemPrompt.context`，如 `ideo-scrum:memory-reload`，顺序排在 `ideo-scrum:commitments` 之后），有条件的写法，普通会话里不误触发：`If you loaded the `memory` skill in this conversation and the conversation has since been compacted, call `memory` again before going on.`；`check_dsh` 加一项断言（上下文在、文字对、不依赖会话里叫过哪个角色）。
  - 行 14 的 DSH 验证加一项：压缩后没人问起清单内容时，模型会不会自己重载；A 不稳就换 B（或 A＋B 都放）。
- **测试装置**：`scripts/stranger_test/driver.py` 在 27 里改了（`carrier_test.py` 在用它），同步后重跑 `carrier_test.py selftest`。
- **检查脚本与文档**：`check.py`、`check_docs.py`、glossary、quick-start、README 都被改过，行 13 用同步后的文件重新生成 `refs_inventory.py` 与 `ref_migration_table.py`。

## 三、board-log 的去处（Master 2026-11-23 改了说法）

不并进 Memory 的长文件，也不删，留在 `plugins/ideo-scrum/board/board-log.md`，当写看板的长文件用；清单里写看板的 4 行（`one-board`、`board-owns-nothing`、`board-writer`、`board-rules`）直接指向 `../../board/board-log.md`。后果：

- 草稿里的 `long/board-writing.md`（由 board-log 的 19 条改写）**我建议去掉**，不留只放索引的空壳：四行已直接指向原文件，原文件 27 已更新（第 3、4、12、16 条），留一份会过时。`board-rules` 的 `via` 指向改成原文件；`check_drafts.py` 要允许一行指向仓内的非 `long/` 路径。
- board-log 的编号引用不再迁（文件还在，只是路径已由 27 改好）；要迁的旧约定缩成五份：`overview`、`product-log`、`sprint-log`、`design-log`、`ideo-log`。五份照删，`board-log.md` 例外（记在 2.2 的 P3）。
- 流程图长文件里的看板图是否保留，同步后定（我倾向保留：它是整体地图的一部分，板子本身的图仍在原文件里）。

## 四、清单里 Supporter 这一块的草案（同步后量字数、定稿）

约定 14 的四小条若各占一行，清单净增约 4 行、约 600 字符，会顶到 16,000 字符的上限边上。我的草案是**重写两行、净增两行**，细节放 `roles-and-routing.md`：

| 句柄 | 草案（≤150 字符，同步后量） | 去向 |
| --- | --- | --- |
| `who-gets-which-work`（重写） | Review goes to the Scrum Master; board, summaries and product-log upkeep to the Supporter; a Developer never reviews itself. | 长文件 |
| `ask-the-po`（重写，合并三级分流） | Decide what is yours; process questions go to the Scrum Master; what only the PO decides goes to the Supporter, who asks in one go. | 长文件 |
| `answers-back`（新） | The Supporter carries the PO's answers back word for word; what the PO decided on scope, items or a go-ahead goes to the Scrum Master to record. | 清单 |
| `po-word-relayed`（新） | A PO opinion relayed by the Supporter counts as theirs if marked, worded, dated and placed; record it as `PO (via Supporter): …`; never for push, release, tool permissions. | 长文件（例外全文） |
| `stage-gates`（改一词） | Wait for the PO's explicit stage permission to start or return to a stage; approving a result is not permission. | 长文件 |
| `board-writer`（重写） | A cheap model or the Supporter writes scrum/ScrumBoard.html when the PO wants to look or a log changed. | `../../board/board-log.md` |

## 五、同步后的顺序

1. `git merge main`（或 Master 指定的办法），解决冲突；只会碰 `scrum/ProductBacklog.md`、`scrum/documents/`，我的文件夹 `scrum/sprint-26-plugin-memory/` 与插件文件在 27 里没有交集的部分。
2. 重跑 `extract_rules.py`（board-log 的路径要改），与旧台账逐条文本比对，确认变的只有上面第一节；差出来的列入改动清单。
3. 照第一、三、四节改草稿与长文件，重跑 `check_drafts.py`、`assemble_memory.py`、`make_review.py`；改了含义的列单交 Master 审。
4. DSH 副本重做；然后落盘（行 12）。
