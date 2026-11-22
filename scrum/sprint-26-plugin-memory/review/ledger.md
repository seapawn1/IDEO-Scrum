# 台账：六份约定文件的编号规矩（Sprint 26 行 1）

由 `scripts/extract_rules.py` 生成；基线提交 `fa40fa4`。合计 **111** 条编号规矩、**29** 个非编号块。
覆盖检查：每个文件的每个非空行恰属于「标题」「一条规矩」「一个非编号块」之一，没有丢行、没有重复；编号连续；条数与 `grep` 一致。
旧条的完整原文在 `ledger.json`（逐字），不抄进这里。

| 文件 | 条数 | 非编号块 | 行数 | 字符 |
| --- | --- | --- | --- | --- |
| `scrum-kernel/overview.md` | 17 | 7 | 127 | 21,471 |
| `scrum-kernel/conventions/product-log.md` | 18 | 5 | 79 | 7,942 |
| `board/board-log.md` | 19 | 3 | 74 | 14,407 |
| `sprint-kernel/conventions/sprint-log.md` | 26 | 5 | 97 | 20,098 |
| `design-kernel/conventions/design-log.md` | 27 | 6 | 91 | 21,097 |
| `ideo-kernel/conventions/ideo-log.md` | 4 | 3 | 31 | 4,444 |

## overview（17 条）

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` · blob `bf00e4f2fc`

| id | 名称 | 所在节 | 行 | 字符 | 标记 | 引用其他约定 |
| --- | --- | --- | --- | --- | --- | --- |
| overview#1 | One product log | Conventions / Where things live | 48–48 | 79 | — | 0 |
| overview#2 | Sprints and designs side by side | Conventions / Where things live | 49–49 | 729 | Departs | 2 |
| overview#3 | Three layers | Conventions / Where things live | 50–60 | 1060 | — | 2 |
| overview#4 | Folders | Conventions / Where things live | 61–61 | 659 | — | 1 |
| overview#5 | Where files go | Conventions / Where things live | 62–62 | 698 | — | 2 |
| overview#6 | Working material | Conventions / Where things live | 63–63 | 383 | — | 2 |
| overview#7 | Names | Conventions / Where things live | 64–69 | 790 | — | 0 |
| overview#8 | Roles | Conventions / Who does what | 73–86 | 2459 | — | 1 |
| overview#9 | Only the Product Owner must be human | Conventions / Who does what | 87–87 | 142 | Departs | 0 |
| overview#10 | Ask the Product Owner | Conventions / Who does what | 88–88 | 181 | — | 1 |
| overview#11 | Product Owner as Developer | Conventions / Who does what | 89–89 | 135 | — | 0 |
| overview#12 | Product Owner decides between stages | Conventions / Who does what | 90–90 | 1451 | — | 3 |
| overview#13 | One Scrum Master per project | Conventions / Sessions | 94–94 | 232 | — | 0 |
| overview#14 | Who gets which work | Conventions / Sessions | 95–102 | 4132 | quote | 3 |
| overview#15 | Working conventions | Conventions / About these conventions | 106–106 | 692 | Supplement、Decide on the spot | 0 |
| overview#16 | Templates record outputs | Conventions / About these conventions | 107–107 | 499 | — | 1 |
| overview#17 | Goal fixed, plan flexible | Conventions / What stays fixed | 111–113 | 1752 | quote、CJK | 0 |

非编号块（7 个）：

| 种类 | 行 | 所在节 | 首行 |
| --- | --- | --- | --- |
| quote | 3–3 | （文件头） | > These are working conventions — the author's reading of Scrum and de |
| quote | 5–6 | （文件头） | > Source: quotations from The Scrum Guide 2020 (Ken Schwaber & Jeff Su |
| paragraph | 8–8 | （文件头） | Source labels and short names are explained in convention 15. |
| paragraph | 10–10 | （文件头） | The other files: `conventions/product-log.md` and `../../template/prod |
| fence:mermaid | 14–42 | The map | ```mermaid |
| paragraph | 117–117 | Departures from the official guides | Each departure is stated here once, with its reason; the convention na |
| table | 119–127 | Departures from the official guides | \| Here \| The official guide \| Why \| See \| |

## product-log（18 条）

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` · blob `13b79d5c5c`

| id | 名称 | 所在节 | 行 | 字符 | 标记 | 引用其他约定 |
| --- | --- | --- | --- | --- | --- | --- |
| product-log#1 | One product log | Starting | 26–26 | 287 | — | 2 |
| product-log#2 | Blank page | Starting | 27–38 | 1266 | — | 1 |
| product-log#3 | Facts first, then questions | Starting | 39–39 | 207 | Supplement | 0 |
| product-log#4 | Product and Product Goal | Each part | 43–43 | 375 | — | 0 |
| product-log#5 | Two kinds of Done | Each part | 44–44 | 494 | — | 0 |
| product-log#6 | Stakeholders in a short table | Each part | 45–45 | 292 | — | 0 |
| product-log#7 | Architecture as a map | Each part | 46–46 | 301 | — | 0 |
| product-log#8 | No TBD | Each part | 47–47 | 86 | — | 0 |
| product-log#9 | Technical design stays out | Each part | 48–48 | 134 | — | 0 |
| product-log#10 | Seven columns | Items | 52–62 | 597 | quote | 0 |
| product-log#11 | Numbers, not ranks | Items | 63–63 | 198 | — | 0 |
| product-log#12 | Items with the Scrum Master | Items | 64–64 | 614 | Departs | 1 |
| product-log#13 | Status lives here | Items | 65–65 | 111 | — | 0 |
| product-log#14 | Refine any time, finish in the Sprint | Refinement | 69–69 | 252 | — | 1 |
| product-log#15 | Seven steps | Refinement | 70–70 | 214 | — | 1 |
| product-log#16 | Where refined content goes | Refinement | 71–71 | 318 | — | 1 |
| product-log#17 | Fresh at every Review | Keeping it fresh | 75–75 | 563 | — | 2 |
| product-log#18 | Goal fixed, plan flexible | Throughout | 79–79 | 320 | — | 1 |

非编号块（5 个）：

| 种类 | 行 | 所在节 | 首行 |
| --- | --- | --- | --- |
| quote | 3–3 | （文件头） | > Working conventions: reference, not law — follow what fits, override |
| quote | 5–6 | （文件头） | > Source: quotations from The Scrum Guide 2020 (Ken Schwaber & Jeff Su |
| paragraph | 8–8 | （文件头） | The product log is the first layer. Its template is `../../template/pr |
| fence:mermaid | 10–20 | （文件头） | ```mermaid |
| paragraph | 22–22 | （文件头） | Convention 18 holds at every step; see Throughout, below. |

## board-log（19 条）

`plugins/ideo-scrum/board/board-log.md` · blob `1bde5c807b`

| id | 名称 | 所在节 | 行 | 字符 | 标记 | 引用其他约定 |
| --- | --- | --- | --- | --- | --- | --- |
| board-log#1 | One board for the project | What the board is | 18–18 | 425 | — | 0 |
| board-log#2 | It owns nothing | What the board is | 19–19 | 322 | — | 0 |
| board-log#3 | Where it lives, who writes it, and when | What the board is | 20–20 | 382 | — | 0 |
| board-log#4 | The logs | What it reads | 24–24 | 843 | — | 1 |
| board-log#5 | What it takes from a log | What it reads | 25–31 | 1442 | CJK | 6 |
| board-log#6 | Maps | What it reads | 32–32 | 250 | — | 0 |
| board-log#7 | The overview | What the page shows | 36–36 | 604 | — | 0 |
| board-log#8 | The cards | What the page shows | 37–37 | 809 | — | 1 |
| board-log#9 | What the page works out itself | What the page shows | 38–38 | 444 | — | 0 |
| board-log#10 | Links and sources | What the page shows | 39–39 | 380 | — | 0 |
| board-log#11 | One block of data | The data | 43–57 | 2089 | quote | 1 |
| board-log#12 | Copied, and summarized | The data | 59–59 | 2201 | CJK | 0 |
| board-log#13 | Groups and order | The data | 60–60 | 377 | — | 0 |
| board-log#14 | Work items and items | The data | 61–61 | 334 | — | 0 |
| board-log#15 | Escaping | The data | 62–62 | 102 | — | 0 |
| board-log#16 | Left out on purpose | The data | 63–63 | 1203 | CJK | 1 |
| board-log#17 | Steps | How to write it | 67–72 | 516 | — | 4 |
| board-log#18 | Check | How to write it | 73–73 | 301 | — | 0 |
| board-log#19 | What the board does not do | How to write it | 74–74 | 238 | — | 0 |

非编号块（3 个）：

| 种类 | 行 | 所在节 | 首行 |
| --- | --- | --- | --- |
| quote | 3–3 | （文件头） | > Working conventions: reference, not law — follow what fits, override |
| paragraph | 5–5 | （文件头） | The Scrum board is one page that shows where the project stands. Its t |
| fence:mermaid | 7–14 | （文件头） | ```mermaid |

## sprint-log（26 条）

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` · blob `9f08a8aa9e`

| id | 名称 | 所在节 | 行 | 字符 | 标记 | 引用其他约定 |
| --- | --- | --- | --- | --- | --- | --- |
| sprint-log#1 | One branch, one folder | Opening | 28–28 | 330 | — | 0 |
| sprint-log#2 | No end date | Opening | 29–29 | 252 | Departs | 0 |
| sprint-log#3 | Small work, small Sprint | Opening | 30–30 | 221 | — | 1 |
| sprint-log#4 | Set the Sprint Goal | Stages / Why | 36–36 | 764 | — | 0 |
| sprint-log#5 | Select the items | Stages / What | 40–40 | 362 | — | 0 |
| sprint-log#6 | Refine in seven steps | Stages / What | 41–48 | 1152 | — | 1 |
| sprint-log#7 | How is a plan, not steps | Stages / How | 52–52 | 819 | Departs、quote | 0 |
| sprint-log#8 | Go-ahead | Stages / How | 53–53 | 444 | — | 1 |
| sprint-log#9 | Notes as you go | Stages / Increment | 57–57 | 548 | — | 0 |
| sprint-log#10 | Checkpoints, not stand-ups | Stages / Increment | 58–58 | 612 | Departs | 1 |
| sprint-log#11 | Outline before full text | Stages / Increment | 59–59 | 321 | — | 1 |
| sprint-log#12 | Full text for review | Stages / Increment | 60–60 | 311 | — | 1 |
| sprint-log#13 | Tests: criteria first | Stages / Test | 64–64 | 367 | — | 0 |
| sprint-log#14 | A reviewer is required | Stages / Test | 65–65 | 850 | Departs | 0 |
| sprint-log#15 | Product Owner acceptance when written | Stages / Test | 66–66 | 176 | — | 0 |
| sprint-log#16 | Record the tests | Stages / Test | 67–67 | 1123 | — | 1 |
| sprint-log#17 | Review | Closing | 71–71 | 2638 | — | 3 |
| sprint-log#18 | Retrospective | Closing | 72–73 | 1150 | Supplement | 0 |
| sprint-log#19 | One closing commit | Closing | 74–82 | 889 | — | 1 |
| sprint-log#20 | Goal fixed, plan flexible | Throughout | 86–86 | 501 | — | 1 |
| sprint-log#21 | New work gets registered | Throughout | 87–87 | 198 | — | 0 |
| sprint-log#22 | The log is the handoff | Throughout | 88–88 | 1065 | — | 3 |
| sprint-log#23 | Special cases | Throughout | 89–94 | 353 | — | 1 |
| sprint-log#24 | The Product Owner decides at the end of each stage | Throughout | 95–95 | 1238 | — | 1 |
| sprint-log#25 | Ask the PO | Throughout | 96–96 | 735 | — | 11 |
| sprint-log#26 | Developer in another session or tool | Throughout | 97–97 | 931 | — | 1 |

非编号块（5 个）：

| 种类 | 行 | 所在节 | 首行 |
| --- | --- | --- | --- |
| quote | 3–3 | （文件头） | > Working conventions: reference, not law — follow what fits, override |
| quote | 5–6 | （文件头） | > Source: quotations from The Scrum Guide 2020 (Ken Schwaber & Jeff Su |
| paragraph | 8–8 | （文件头） | A Sprint turns selected items into an Increment. Its template is `../. |
| fence:mermaid | 10–22 | （文件头） | ```mermaid |
| paragraph | 24–24 | （文件头） | Conventions 20–26 hold at every step; see Throughout, below. Read each |

## design-log（27 条）

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` · blob `632611c38f`

| id | 名称 | 所在节 | 行 | 字符 | 标记 | 引用其他约定 |
| --- | --- | --- | --- | --- | --- | --- |
| design-log#1 | Open a design for a question with no ready answer | Opening | 25–25 | 628 | — | 3 |
| design-log#2 | Hard point, not the whole item | Opening | 26–26 | 134 | — | 0 |
| design-log#3 | Who | Opening | 27–27 | 731 | — | 1 |
| design-log#4 | Branch | Opening | 28–28 | 226 | — | 0 |
| design-log#5 | Open a design | Opening | 29–29 | 526 | — | 2 |
| design-log#6 | Start from the people | Stages / Empathize | 37–37 | 882 | — | 0 |
| design-log#7 | Experts when needed | Stages / Empathize | 38–38 | 657 | — | 2 |
| design-log#8 | Map and questions in the log | Stages / Define | 42–42 | 1258 | Departs | 2 |
| design-log#9 | Lightning Demos (optional) | Stages / Ideate: diverge | 46–46 | 276 | — | 1 |
| design-log#10 | Diverge before you converge | Stages / Ideate: diverge | 47–47 | 572 | — | 2 |
| design-log#11 | Isolated solutions (optional) | Stages / Ideate: converge | 51–52 | 1163 | Decide on the spot | 3 |
| design-log#12 | Talk with the Product Owner | Stages / Ideate: converge | 53–53 | 526 | — | 2 |
| design-log#13 | Choosing is the key step | Stages / Ideate: converge | 54–54 | 323 | — | 0 |
| design-log#14 | Combine or rumble | Stages / Ideate: converge | 55–55 | 178 | — | 0 |
| design-log#15 | Storyboard | Stages / Ideate: converge | 56–56 | 184 | — | 0 |
| design-log#16 | Just enough prototype | Stages / Prototype | 60–61 | 772 | Supplement、Decide on the spot | 1 |
| design-log#17 | Role-card test | Stages / Test | 65–65 | 639 | — | 0 |
| design-log#18 | Write the criteria before the test | Stages / Test | 66–66 | 241 | — | 0 |
| design-log#19 | When the design ends | Ending | 70–70 | 3050 | — | 6 |
| design-log#20 | IDEO in every stage | Throughout | 74–74 | 264 | — | 1 |
| design-log#21 | Ask the PO | Throughout | 75–75 | 650 | — | 8 |
| design-log#22 | Five chapters, not five days | Throughout | 76–76 | 235 | — | 0 |
| design-log#23 | Renamed terms | Throughout | 77–77 | 62 | — | 0 |
| design-log#24 | Resume from the header | Throughout | 78–78 | 888 | — | 2 |
| design-log#25 | Goal fixed, plan flexible | Throughout | 79–79 | 310 | — | 1 |
| design-log#26 | Gates between stages | Throughout | 80–90 | 2941 | — | 0 |
| design-log#27 | A small design is still a design | Throughout | 91–91 | 433 | — | 3 |

非编号块（6 个）：

| 种类 | 行 | 所在节 | 首行 |
| --- | --- | --- | --- |
| quote | 3–3 | （文件头） | > Working conventions: reference, not law — follow what fits, override |
| paragraph | 5–5 | （文件头） | The design log template is `../../template/design-backlog-template.md` |
| fence:mermaid | 7–17 | （文件头） | ```mermaid |
| paragraph | 19–19 | （文件头） | **The three loops.** Empathize and Define: the Product Owner and the S |
| paragraph | 21–21 | （文件头） | Conventions 20–27 hold at every step; see Throughout, below. Apply the |
| paragraph | 33–33 | Stages | The conventions under Stages cover only what differs from the book or  |

## ideo-log（4 条）

`plugins/ideo-scrum/skills/ideo-kernel/conventions/ideo-log.md` · blob `52df86def0`

| id | 名称 | 所在节 | 行 | 字符 | 标记 | 引用其他约定 |
| --- | --- | --- | --- | --- | --- | --- |
| ideo-log#1 | Design sprint or the five modes | The Boundary | 22–22 | 557 | — | 2 |
| ideo-log#2 | The five modes and the design sprint | The Two Together | 26–26 | 958 | quote | 1 |
| ideo-log#3 | When to open an IDEO log | The IDEO Log | 30–30 | 646 | — | 1 |
| ideo-log#4 | Where it lives and how it ends | The IDEO Log | 31–31 | 1172 | — | 1 |

非编号块（3 个）：

| 种类 | 行 | 所在节 | 首行 |
| --- | --- | --- | --- |
| quote | 3–3 | （文件头） | > Working conventions: reference, not law — follow what fits, override |
| paragraph | 5–5 | （文件头） | Paths here are relative to the ideo-kernel skill folder. The five mode |
| fence:mermaid | 7–18 | （文件头） | ```mermaid |
