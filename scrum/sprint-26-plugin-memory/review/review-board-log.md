# 审阅：board-log.md（scrum-kernel）

每条旧规矩一节：先是原文（逐字），再是出处与依据、核验后的建议与理由，最后是它现在的样子（清单里的一行，或并到哪、删在哪）。
读法：只看「旧规矩原文」和「新行」两块就能审；出处、理由是我和核验员写的依据，供你判断「留不留、改得对不对」。

本文件 19 条：删 3、并 1、改 7、留 8；另有 3 个非编号块（文末）。

---

### board-log#1 · One board for the project

`plugins/ideo-scrum/board/board-log.md` 第 18–18 行

**旧规矩原文**

> 1. **One board for the project** — Keep one page for the whole project: the product, the items not done, and every open Sprint and design. It answers one question without opening a log: where does the project stand, and what is each line of work doing. It is meant to be glanced at — hung on a screen, read from a few steps away, on a wide screen, a portrait screen, or a phone — so it shows few things, and shows them large.

**出处与依据**：作者（把握：高）；种类：说明
- commit 1c2cdb2 feat(Sprint 19): 块 7——看板约定 board.md（16 条，自带给子代理的简报）与模板 board-template.html
- archive scrum/documents/design/design-board.md：设计目标「看板挂在 PO 的屏上」

**建议**：改；去处：清单（一行）

**理由**：目的只要一句：一张页面看全项目，一眼看清。原文后半「few things, large」是版式，归模板，删去。

**新行**

```text
- **one-board** Keep one board page for the whole project that shows at a glance where it stands and what each line of work is doing.
```

**备注**：The second half of the old rule (few things, shown large, for a screen read from a few steps away) is layout and stays with the template.

---

### board-log#2 · It owns nothing

`plugins/ideo-scrum/board/board-log.md` 第 19–19 行

**旧规矩原文**

> 2. **It owns nothing** — The board only reads the logs. It keeps no state, and no log is ever changed from it. Delete it and write it again, and every fact is the same; only the time it was made differs. For that reason the page need not go into version control; the project decides, for example with a `.gitignore` entry.

**出处与依据**：作者（把握：高）；种类：规矩
- commit 1c2cdb2 feat(Sprint 19): 块 7——看板约定 board.md（16 条，自带给子代理的简报）与模板 board-template.html
- archive scrum/ProductBacklog.md 边界：「看板只读日志、不另存状态」

**建议**：留；去处：清单（一行）

**理由**：看板删了重写结果一致，所以不进版本库、不存状态；这是看板可信的前提，删了就没人知道能随手丢。

**与它重复或相邻**：board-log#19

**新行**

```text
- **board-owns-nothing** The board only reads the logs: no state, no log changed from it; whether to commit it is the project's call.
```

**备注**：board-log#19 adds: nothing becomes true because it is on the board; it goes into board-log.md (kept in place as the board's long file). The reason for not committing it (delete it and write it again, every fact is the same; only the time differs) also goes there.

---

### board-log#3 · Where it lives, who writes it, and when

`plugins/ideo-scrum/board/board-log.md` 第 20–20 行

**旧规矩原文**

> 3. **Where it lives, who writes it, and when** — Name it `scrum/ScrumBoard.html`, beside the product log. A cheap model writes it, because the work is copying and summarizing, not judging: a fresh subagent told to read this file and the template and to follow them, or the Supporter (the `supporter` entry). Write it when the Product Owner wants to look, or after a log has changed.

**出处与依据**：作者（把握：中）；种类：规矩
- commit e578214 feat(Sprint 20): 块 9——看板新模板；看板改名 ScrumBoard.html / board-log.md / scrum-board-template.html
- po scrum/ProductBacklog.md：「就是它一般用非常便宜的模型嘛」

**建议**：改；去处：清单（一行）

**理由**：位置（scrum/ScrumBoard.html）、「便宜的模型写」并要它读本约定与模板、以及「PO 想看时或日志变了就写」都留；「PO 的常驻辅助会话」待 PBI-86 的秘书角色定下后按新说法改。

**新行**（长文件 `board-log`）

```text
- **board-writer** A cheap model or the Supporter writes scrum/ScrumBoard.html when the PO wants to look or a log changed.
- **board-rules** What the board reads, the data it holds, how to copy and check it; the brief for its writer. Read ../../board/board-log.md first.
```

**备注**：The writer is now a cheap model or the Supporter (Sprint 27). The board conventions stay in place as the board's long file (Master 2026-11-23: board-log.md is not merged into a Memory long file and not deleted); board-rules points at it, and the other rules of that file are indexed by board-rules.

---

### board-log#4 · The logs

`plugins/ideo-scrum/board/board-log.md` 第 24–24 行

**旧规矩原文**

> 4. **The logs** — The product log is `scrum/ProductBacklog.md`. The open logs are `scrum/sprint-*/SprintBacklog.md`, `scrum/design-*/DesignBacklog.md`, and `scrum/ideo-*/IdeoBacklog.md`; nothing in `scrum/documents/`, which holds the archive. A Sprint or design that is open on another branch counts too: read its log as committed on that branch (git can show a file at a branch's latest commit), and give `branch <name> @ <commit>` as its source, the commit as its first seven characters. A log that is in this working copy is read from the working copy, with any change not yet committed, and its source is `working copy`. If one log is found on several branches, use the version with the newest commit. The product log is read the same way when it is not in this working copy; how to write its source is in convention 11 (`product.source`).

**出处与依据**：作者（把握：中）；种类：格式
- commit ed53e1c feat(Sprint 20): 块 10——board-log.md 重写（19 条：数据的字段表、概括的规矩）
- archive scrum/documents/sprint/sprint-20-presentable.md：「重写成 19 条」

**建议**：留；去处：长文件

**理由**：Developer 改：进 board-writing 长文件。核验把去处写成 check.py，但它在仓库根 scripts/ 里，不在 plugins/ideo-scrum 里，装插件的人没有；board-log.md 同时是写看板那个模型的简报，日志在哪些路径、别的分支上的日志怎么读、来源怎么写，只在本条。

**与它重复或相邻**：board-log#5

**新**：只在长文件 `board-log`，清单里由 `board-rules` 一行索引。

**备注**：The log paths, the rule that a Sprint or design open on another branch counts (read as committed there; source `branch <name> @ <commit>`), the working-copy rule and the newest-commit rule go into the long file word for word. My override of the verifiers: they pointed at the board check script, which is not in the plugin.

---

### board-log#5 · What it takes from a log

`plugins/ideo-scrum/board/board-log.md` 第 25–31 行 · 标记：CJK

**旧规矩原文**

> 5. **What it takes from a log** — Read these where the conventions say they are, and look for nothing else:
>     - the commitments: a one-row table whose first cell is `Commitment` (`承诺` in a Chinese log) and whose second cell is the exact text; the heading above it says which one it is (`overview.md`, convention 17): the Product, the Product Goal, the Sprint Goal, the design goal;
>     - `> Now:` in a Sprint log (`../sprint-kernel/conventions/sprint-log.md`, convention 22), a design log (`../design-kernel/conventions/design-log.md`, convention 24), and an IDEO log (`../ideo-kernel/conventions/ideo-log.md`, convention 4); the product log has none;
>     - in the product log, section 3.1: the item table has seven columns (`conventions/product-log.md`, convention 10); take the number, title, status, and size of each row and leave the rest in the log; and the number of rows in section 3.2;
>     - in a Sprint log, section 2.1: the numbers of the items it took, in the order the table lists them; and chapter 3: each row's `#` cell, its Work item cell, and whether its Done when cell begins with `✓` (`../sprint-kernel/conventions/sprint-log.md`, convention 9);
>     - in a design log: the `From` field of the header, which says what the design is for; section 3.1, the chosen solution; and section 3.2, the storyboard, if there is one in the log;
>     - in an IDEO log: its `For` field, which points to the log it serves, and its Now line.

**出处与依据**：作者（把握：中）；种类：格式
- commit ed53e1c feat(Sprint 20): 块 10——board-log.md 重写（19 条：数据的字段表、概括的规矩）
- commit f030513 fix(PBI-71): 修正 IDEO 收尾、宿主状态和头部字段判定

**建议**：留；去处：长文件

**理由**：Developer 改：进 board-writing 长文件。核验写「check.py 与字段表已覆盖」，但 check.py 不在插件里；字段表只说取哪些字段、不说从日志的哪一节取（产品日志 3.1/3.2、冲刺日志 2.1 与第 3 章、设计日志 From/3.1/3.2、IDEO 日志 For 与 Now），写看板的模型要靠本条。

**与它重复或相邻**：board-log#4、board-log#11

**新**：只在长文件 `board-log`，清单里由 `board-rules` 一行索引。

**备注**：What to take from each log (six bullets) goes into the long file, convention numbers replaced by handles. My override of the verifiers, as for board-log#4.

---

### board-log#6 · Maps

`plugins/ideo-scrum/board/board-log.md` 第 32–32 行

**旧规矩原文**

> 6. **Maps** — The product log's map is the Mermaid diagram in section 2.2; a design log's map is the one in its section 2.1. A node's label is the text inside the quotation marks of `["…"]`, `("…")`, or `{"…"}`; arrows and their labels are not nodes.

**出处与依据**：作者（把握：中）；种类：格式
- commit ed53e1c feat(Sprint 20): 块 10——board-log.md 重写（19 条：数据的字段表、概括的规矩）

**建议**：留；去处：长文件

**理由**：说明地图从产品日志 2.2 节、设计日志 2.1 节取，以及节点标签怎么取；地图概括与逐字核对都依赖它，不能只靠脚本。

**新**：只在长文件 `board-log`，清单里由 `board-rules` 一行索引。

**备注**：Maps: the product log's map is the Mermaid diagram in section 2.2, a design log's the one in its 2.1; a node's label is the text inside the quotation marks of the three bracket forms; arrows and their labels are not nodes.

---

### board-log#7 · The overview

`plugins/ideo-scrum/board/board-log.md` 第 36–36 行

**旧规矩原文**

> 7. **The overview** — A tall flow diagram. At the top, a circle for the product. Below it, the items that are not done, in four groups: in a Sprint, in a design, up next, later; the later ones fade. Each item that sits in a Sprint or a design is joined by a line to that Sprint's or design's node on the right: blue to a Sprint, purple to a design, and a dashed line between a Sprint and the design made for one of its items. Pressing an item lights up where it goes. Pressing the circle, a Sprint, or a design opens its card. One colour, amber, is kept for "here": where the open work stands on the map.

**出处与依据**：作者（把握：高）；种类：规矩
- commit ed53e1c feat(Sprint 20): 块 10——board-log.md 重写（19 条：数据的字段表、概括的规矩）
- archive scrum/documents/design/design-board.md：故事板第 3 版（固定页面 + 一块数据）为版式依据

**建议**：删；去处：不进 Memory

**理由**：总览的版式与交互（流向、点亮去向、颜色）已由模板实现，check.py 对页面与模板逐字比。删了 Memory 不丢做事的规矩，版式依据留在设计卡里。

**新**：不进清单。去处或不要的理由：plugins/ideo-scrum/board/scrum-board-template.html draws the overview (flow, lighting, colours); the layout reasons are in the design archive of the board.

---

### board-log#8 · The cards

`plugins/ideo-scrum/board/board-log.md` 第 37–37 行

**旧规矩原文**

> 8. **The cards** — Each card has three layers. The product card: the Product and the Product Goal, word for word; the architecture as one line of a few stops, with "here" at the stop where the open Sprint is; the items not done, grouped. A Sprint card: the Sprint Goal, word for word; the route, its items in order with how many of their work items are done; the work items of chapter 3, done ones marked. A design card: only its own design goal (section 1.2), word for word; its own map as a short line of stops; an independent solution section. Show what was chosen and how it is used, even without a storyboard. When no solution is chosen, keep the section and say so. The foot of a card holds the Now line, folded away until opened, any IDEO log that serves it (convention 11), and where the log was read.

**出处与依据**：作者（把握：中）；种类：规矩
- commit ed53e1c feat(Sprint 20): 块 10——board-log.md 重写（19 条：数据的字段表、概括的规矩）

**建议**：改；去处：清单（一行）

**理由**：卡片三层的版式归模板。只留一条：设计卡的方案区，未选定就写明未选定，不编造故事板。其余删去。

**与它重复或相邻**：board-log#12

**新**：只在长文件 `board-log`，清单里由 `board-rules` 一行索引。

**备注**：Only the kept part goes into the long file: a design card has its own solution section that shows what was chosen and how it is used, even without a storyboard, or says that none is chosen; it invents no storyboard. The three-layer card layout stays with the template.

---

### board-log#9 · What the page works out itself

`plugins/ideo-scrum/board/board-log.md` 第 38–38 行

**旧规矩原文**

> 9. **What the page works out itself** — These are never written in the data, so they cannot be wrong: a Sprint's name from its folder (`sprint-20-presentable` is Sprint 20); a short name from the text before the first colon of a goal, and from the text before the first `——` of an item's title; a design with no colon in its goal is named by its folder's suffix; the count of work items and how many are done; the order of the items; the links.

**出处与依据**：作者（把握：中）；种类：格式
- commit ed53e1c feat(Sprint 20): 块 10——board-log.md 重写（19 条：数据的字段表、概括的规矩）

**建议**：留；去处：长文件

**理由**：Developer 改：进 board-writing 长文件，压成一两句。页面自算项的实现在模板脚本里，但「这些不写进数据」只在本条，写看板的模型不知道就可能多写字段。

**新**：只在长文件 `board-log`，清单里由 `board-rules` 一行索引。

**备注**：One or two sentences in the long file: the page works out a Sprint's name, short names, counts, order and links itself, so none of that is written in the data. My override of the verifiers' delete: that sentence is only here.

---

### board-log#10 · Links and sources

`plugins/ideo-scrum/board/board-log.md` 第 39–39 行

**旧规矩原文**

> 10. **Links and sources** — The page is written to `scrum/ScrumBoard.html`, so a card links to its log relative to the `scrum/` folder (`sprint-01-alpha/SprintBacklog.md`), and only when its source is `working copy`. When the log is only on another branch, the card names the branch and the commit instead, so that no link is dead. Every card's foot starts with its folder's name.

**出处与依据**：作者（把握：高）；种类：规矩
- commit 930c065 feat(Sprint 19): 块 9、10——board.md 补「长文照抄会丢字」；本仓库现状的生成改按「还开着冲刺文件夹的分支」建
- archive scrum/documents/sprint/sprint-19-board-hook.md：「链接写成」的死链被检查脚本抓到

**建议**：留；去处：清单（一行）

**理由**：分支上的日志不做死链，卡片写分支名与提交号，这是看板会不会坏的规矩。一行即可说清。

**新**：只在长文件 `board-log`，清单里由 `board-rules` 一行索引。

**备注**：A card links to its log relative to scrum/ only when its source is the working copy; a log only on another branch shows the branch and the commit, so no link is dead; every card's foot starts with its folder's name.

---

### board-log#11 · One block of data

`plugins/ideo-scrum/board/board-log.md` 第 43–57 行 · 标记：quote

**旧规矩原文**

> 11. **One block of data** — The page draws itself from one JSON object in `<script type="application/json" id="board-data">`. These are its fields; those marked with a star are copied from a log, the others are summaries or plain values (convention 12):
>
>     | Field | What it holds |
>     | --- | --- |
>     | `lang` | `zh` when the logs are written in Chinese, otherwise `en`; the labels on the page follow it |
>     | `generated` | when the page was made, `YYYY-MM-DD HH:MM` |
>     | `product.name` | the words before the first colon of the Product commitment, or the whole commitment when it has none |
>     | `product.statement`, `product.goal` ★ | the Product and the Product Goal commitments |
>     | `product.source` | `working copy`, or `branch <name> @ <commit>` |
>     | `product.map` | the architecture as a list of stops: `{"text", "note", "here", "branch"}`; `note`, `here`, and `branch` are optional |
>     | `product.closed` | the number of rows in section 3.2 of the product log; the page calls them "done groups", because a row can be a Sprint, or a clean-up |
>     | `items` | each item not done: `{"id", "title", "status", "size", "group"}`; the first four ★ |
>     | `sprints` | each open Sprint: `{"id", "goal", "now", "items", "blocks", "source", "ideo"}`; `id` is the folder's name; `goal` and `now` ★; `items` lists the numbers in section 2.1; `blocks` is `[{"n", "title", "done"}]` for each row of chapter 3, `n` and `title` ★; `ideo` is optional |
>     | `designs` | each open design: `{"id", "for", "goal", "now", "map", "solution", "story", "source", "ideo"}`; `goal` and `now` ★; `for` lists the item numbers the `From` field names; `map` is a list of stop texts; `solution` is `{"title", "text"}` or `null` when no solution has been chosen; `story` and `ideo` are optional |
>     | `ideo` | nested in a Sprint or design: `[{"id", "now"}]`, `now` ★; include a still-open IDEO log exactly once, under the open Sprint or design log its `For` header field points to. A mention of `For:` inside the question is not the field; a folder name alone does not identify the host. |

**出处与依据**：作者（把握：高）；种类：格式
- commit ed53e1c feat(Sprint 20): 块 10——board-log.md 重写（19 条：数据的字段表、概括的规矩）
- archive scrum/documents/sprint/sprint-20-presentable.md：「重写成 19 条」

**建议**：留；去处：长文件

**理由**：字段表只在这一条（board-log.md 第45-57行）：模板头注与占位符都只说“board-log.md lists the fields”（scrum-board-template.html 第3、7行；check.py 第30行），check.py 只核部分字段（第361-378、381-401、430-491行），product.name、lang 的取法只在 reference_data 代码里（第545-547、567行），note、branch 的取法全仓库只有本表。删了没人知道 note 取方括号里的条目号、branch 是主线旁的站、here 落在哪个站，须整表进长文件。 另：check.py 第 377 行要求 product.source 恒为 working copy，与本条允许 branch 写法不符，留给 Sprint 27 的 PBI-89 或 PO 定。

**与它重复或相邻**：board-log#5

**新**：只在长文件 `board-log`，清单里由 `board-rules` 一行索引。

**备注**：The whole field table stays in board-log.md, which is not copied or deleted (Master 2026-11-23): nothing else in the repository lists the fields. The old open point (the board check script required product.source to be 'working copy' always, but the table also allows 'branch <name> @ <commit>') was closed by Sprint 27: check.py now accepts both.

---

### board-log#12 · Copied, and summarized

`plugins/ideo-scrum/board/board-log.md` 第 59–59 行 · 标记：CJK

**旧规矩原文**

> 12. **Copied, and summarized** — What is marked ★ goes into the data exactly as the log has it: the same characters, the same language; never reworded, shortened, translated, or tidied. A long text such as a Now line is copied mechanically — with a command or a script — rather than retyped: a long text copied by hand loses a character. Only `product.map` and a design's `map`, `solution`, and `story` are summaries. A map stop's text is a few words cut from one node's label: leave out the step number (①, ②), anything in brackets (item numbers, file names), and the explanation after a colon; never reword. So `③ 写产品日志：Product · 架构 · PBI（product-log）` becomes `写产品日志`, and `⑥ 施工（sprint-log）` becomes `施工`. Keep the main line only — five to eight stops, none longer than about twenty characters — and leave out the people at the top, the ending, and every side branch except the design sprint, which is a stop of its own. The steps a Sprint goes through, one after another, are one stop, joined with ` → ` (`Planning → PO 放行 → 施工 → Test`). A design's `map` comes from its own section 2.1, in source order, without people, the ending, or side branches: five or six stops when the map has them, no invented stops; omit it when no map is recorded. On the product map, `note` holds the item numbers in the brackets of the stop's label, as `62 · 64`. `here` lists the ids of open Sprints and designs at that stop: a Sprint at the stop its Now line names (planning, building, or testing), a design at the design sprint stop; leave `here` out when no stop fits. `branch` is true for a stop beside the main line. A design's `solution` summarizes section 3.1: a short `title` for what was chosen and a short `text` for how it is used. Leave out a part the log does not give; a recorded choice without usage details is still a choice. Write `null` when no choice is recorded: drafts, sketches, or a storyboard alone are not a choice. Optional `story` is a short ordered list of `{"title", "text"}` frames from section 3.2 that illustrate the chosen solution; omit it without a storyboard, and omit it when `solution` is `null`, because a story illustrates a chosen solution. Add no facts to fill either field.

**出处与依据**：作者（把握：高）；种类：规矩
- archive scrum/documents/sprint/sprint-19-board-hook.md：「长文手抄丢一个字符」
- commit 930c065 feat(Sprint 19): 块 9、10——board.md 补「长文照抄会丢字，对地图逐行读回」

**建议**：改；去处：长文件

**理由**：★ 逐字照抄、长文用命令复制只是开头；地图主线的取舍（五到八站、去序号/括号/冒号后解释）、note 与 here 怎么写、solution 的 null 与“有选择无用法仍算选定”只有本条有，check.py 只核站名出自日志和 solution/story 结构（第414-423、467-491行），模板只显示（第508-514、565-581行）。细则多，整条进长文件，清单留一行索引。

**与它重复或相邻**：board-log#17、board-log#8

**新**：只在长文件 `board-log`，清单里由 `board-rules` 一行索引。

**备注**：The whole rule goes into the long file: the map-stop rules (five to eight stops, no step numbers, brackets or explanation after a colon, the examples), note and here, branch, a design's map, the solution with its null case, story.

---

### board-log#13 · Groups and order

`plugins/ideo-scrum/board/board-log.md` 第 60–60 行

**旧规矩原文**

> 13. **Groups and order** — An item's `group` is `sprint` when its number is in an open Sprint's section 2.1; otherwise `design` when an open design's `From` field names it; otherwise `later` when its status says it is for later; otherwise `next`. Keep the items in the product log's order: the page puts the items of a Sprint or a design in that Sprint's or design's own order.

**出处与依据**：作者（把握：高）；种类：格式
- commit ed53e1c feat(Sprint 20): 块 10——board-log.md 重写（19 条：数据的字段表、概括的规矩）

**建议**：留；去处：清单（一行）

**理由**：group 是写进数据的字段（#11 字段表），不是页面自算；check.py 只核 group 与冲刺/设计一致（第394-401行），不核 later/next，只有参考生成器按状态推 later（第545行）。删了会丢“状态说以后才是 later，否则 next”这一句，留一行即可。

**新**：只在长文件 `board-log`，清单里由 `board-rules` 一行索引。

**备注**：The page puts the items of a Sprint or a design in that Sprint's or design's own order.

---

### board-log#14 · Work items and items

`plugins/ideo-scrum/board/board-log.md` 第 61–61 行

**旧规矩原文**

> 14. **Work items and items** — A work item belongs to an item when its Work item cell names the item's number as written, or the number alone, as `68-a`. A work item that names no item belongs to none. The page counts only these; when no work item of a Sprint names one of its items, that Sprint's route lists the items without a bar.

**出处与依据**：作者（把握：高）；种类：格式
- commit ed53e1c feat(Sprint 20): 块 10——board-log.md 重写（19 条：数据的字段表、概括的规矩）

**建议**：删；去处：不进 Memory

**理由**：工作项归属与“没有工作项命名条目就不画进度条”由模板脚本实现（scrum-board-template.html 第283-289行 names()、第538-539行），check.py 并不统计工作项（只取 3.1 表的号、标题、状态、大小，第252-253行）。删了不丢行为，模板还在。

**新**：不进清单。去处或不要的理由：plugins/ideo-scrum/board/scrum-board-template.html: names() (lines 283-289) and the no-bar case (lines 538-539) implement it.

---

### board-log#15 · Escaping

`plugins/ideo-scrum/board/board-log.md` 第 62–62 行

**旧规矩原文**

> 15. **Escaping** — In the JSON, write every `<` as `\u003c`, so that no text can end the script early.

**出处与依据**：作者（把握：高）；种类：格式
- commit e578214 feat(Sprint 20): 块 9——看板新模板；看板改名 ScrumBoard.html / board-log.md / scrum-board-template.html

**建议**：删；去处：不进 Memory

**理由**：模板文件头注释已写明「每个 < 写成 \u003c」，check.py 核对，Memory 不留。

**新**：不进清单。去处或不要的理由：The template's header comment says to write every < as \u003c.

---

### board-log#16 · Left out on purpose

`plugins/ideo-scrum/board/board-log.md` 第 63–63 行 · 标记：CJK

**旧规矩原文**

> 16. **Left out on purpose** — The page does not show what waits for the Product Owner, nor the five stages a Sprint passes through: the Product Owner asks the Scrum Master for those, and they change faster than a page is written. Items in the product log's section 3.2 are done or closed and are not shown, only counted. Leave out IDEO logs that serve only the product log, have no open host, or have concluded even if not yet archived. Read the state of the IDEO run itself from the `Now` line (for example, `本轮五模式已收尾` or `The IDEO run has concluded`, optionally after the mode); a next step such as `待收尾` or a mention of closed items is not a concluded run. A host whose own `Now` explicitly says the Sprint or design has ended is no longer open, even while its log awaits archiving: for example `已收官 · 2026-11-21`, `收官 · 2026-11-14`, `Sprint 01 has ended`, or, after a stage name, a line that also says the log awaits archiving, such as `Test: Concluded — awaiting archive`. Finishing one of its stages is not ending the host (`Prototype: concluded; Test next`). This affects only nested IDEO entries, not the discovery of Sprint and design cards (convention 4). Do not add a card or a new log field.

**出处与依据**：PO 原话（把握：中）；种类：规矩
- po scrum/documents/design/design-board.md：「那种都是众所周知的呀」
- archive scrum/documents/sprint/sprint-21-design-board.md：PBI-71 按 For 实际宿主与 Now 收尾态判定 IDEO 归属

**建议**：改；去处：清单（一行）

**理由**：不画五个阶段、不显示等 PO 的事、IDEO 收尾看 Now 行保留；IDEO 归属与收尾判定已由 check.py 实现（第280-290、493-518行，判定见第161-186行），3.2 只计数见第255行。但“不新增卡片或日志字段”两处都没有（check.py 只拒多出的卡，第432、451行），一行里要保留这句。

**新**：只在长文件 `board-log`，清单里由 `board-rules` 一行索引。

**备注**：The whole rule, including how a concluded IDEO run is read from its Now line and when a host counts as ended, is in board-log.md (kept in place as the board's long file) word for word.

---

### board-log#17 · Steps

`plugins/ideo-scrum/board/board-log.md` 第 67–72 行

**旧规矩原文**

> 17. **Steps** — Follow these steps:
>     1. Read `scrum-board-template.html`; its first comment says how to use it.
>     2. Find the logs (convention 4) and read what each one holds (conventions 5 and 6).
>     3. Copy the template to `scrum/ScrumBoard.html` with a command (`cp`, `Copy-Item`), replacing the old page. Do not retype it.
>     4. Write the data (conventions 11–16) and put it in place of the single placeholder line in the data block. Change nothing else on the page.
>     5. Check the page (convention 18).

**出处与依据**：作者（把握：中）；种类：规矩
- commit ed53e1c feat(Sprint 20): 块 10——board-log.md 重写（19 条：数据的字段表、概括的规矩）

**建议**：改；去处：长文件

**理由**：模板注释只讲复制、替换占位行、不改别的（scrum-board-template.html 第6-8行），开头还把用法指向 board-log.md（第3行）；第2步“找日志、读什么”和第5步“跑 check.py”不在模板里，#12 讲的是长文用命令复制、不是复制模板，并入 #12 会丢掉第2、3步。五步是流程，归长文件。

**与它重复或相邻**：board-log#12

**新**：只在长文件 `board-log`，清单里由 `board-rules` 一行索引。

**备注**：The five steps go word for word into the long file, with the convention numbers replaced by handles.

---

### board-log#18 · Check

`plugins/ideo-scrum/board/board-log.md` 第 73–73 行

**旧规矩原文**

> 18. **Check** — Check the page against the logs: the JSON reads; every ★ field is found in its log, character for character; every stop of a map is found in the log's map; every number in `items`, `for`, and `here` exists; open the page and see that it shows the board, not a message. Fix what is not.

**出处与依据**：作者（把握：高）；种类：规矩
- commit ed53e1c feat(Sprint 20): 块 10——board-log.md 重写（19 条：数据的字段表、概括的规矩）
- memory S:/SeaPawn-Memory/memory/IDEO-Scrum/board-check-only-what-conventions-ask.md：看板检查只查约定要求的

**建议**：改；去处：清单（一行）

**理由**：写完跑 scripts/board_check/check.py 并打开页面，确认是看板而不是报错页。核对项由脚本负责，不在 Memory 里重列。

**新**：只在长文件 `board-log`，清单里由 `board-rules` 一行索引。

**备注**：The annotation proposed pointing to the board check script, but it sits in the repository's scripts/, outside plugins/ideo-scrum, so an installed plugin does not have it; board-log.md (kept in place as the board's long file) keeps the original check list.

---

### board-log#19 · What the board does not do

`plugins/ideo-scrum/board/board-log.md` 第 74–74 行

**旧规矩原文**

> 19. **What the board does not do** — Nothing on it changes anything: an item lights up where it goes, a node opens a card, and that is all. It edits no log and keeps no state between pages. Nothing becomes true because it is on the board.

**出处与依据**：作者（把握：高）；种类：规矩
- commit ed53e1c feat(Sprint 20): 块 10——board-log.md 重写（19 条：数据的字段表、概括的规矩）

**建议**：并 → board-log#2；去处：清单（一行）

**理由**：与 #2 同一件事（不改日志、不存状态）。只多一句「挂上看板不等于事实」，并入 #2 时保留这句。

**与它重复或相邻**：board-log#2

**新**：并入 `board-log#2`。这条独有、要带过去的内容：Nothing becomes true because it is on the board.

**备注**：board-log#2 is drafted (board-owns-nothing); the sentence goes into board-log.md (kept in place as the board's long file).

---

## 非编号块（引言、署名、图、表）

### board-log@1 · quote（第 3–3 行）

> > Working conventions: reference, not law — follow what fits, override what doesn't, note why. Source labels and short names are explained in convention 15 of `overview.md`, in the scrum-kernel skill folder, beside its `SKILL.md`. A convention with no label is the author's practice.

**新**：不进清单。去处或不要的理由：The MEMORY.md header carries it: working conventions, follow what fits, depart from what doesn't, say why in the log's notes.

---

### board-log@2 · paragraph（第 5–5 行）

> The Scrum board is one page that shows where the project stands. Its template is `scrum-board-template.html`, beside this file in `board/`; this file is also the brief for whoever writes the page. Paths in this file, such as `overview.md`, `conventions/product-log.md` and those starting with `../`, are relative to the scrum-kernel skill folder, not to `board/`.

**新**：不进清单。去处或不要的理由：The intro of board-log.md itself, which stays in place in the plugin's board/ folder as the board's long file (the board is one page; its template; this brief).

---

### board-log@3 · fence:mermaid（第 7–14 行）

> ```mermaid
> flowchart TD
>     L["The logs<br/>product log, open Sprint, design, and IDEO logs"] --> R["Read<br/>conventions 4–6"]
>     R --> D["Write the data<br/>conventions 11–16"]
>     D --> G["Put it in the template<br/>convention 17"]
>     G --> B["scrum/ScrumBoard.html<br/>conventions 1–3, 7–10"]
>     B -. "delete it, write it again" .-> L
> ```

**新**：不进清单。去处或不要的理由：Drawn in details/flow-maps.md, with the handles in the boxes; the list line flow-maps points there.

---
