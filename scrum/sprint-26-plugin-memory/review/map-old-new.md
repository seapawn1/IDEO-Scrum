# 旧规矩 ↔ Memory 对照表

由 `scripts/assemble_memory.py` 生成。每条旧规矩一行：它去了哪一行（handle）、并入了谁、或删在哪里；再反过来，每个 handle 来自哪几条旧规矩。

## 旧 → 新

| 旧规矩 | 处理 | 去向 |
| --- | --- | --- |
| overview#1 | 留 | `one-product-log` |
| overview#2 | 改 | `designs-beside-sprints`（长文件 `folders`） |
| overview#3 | 改 | `three-layers`（长文件 `folders`） |
| overview#4 | 留 | `scrum-folders`（长文件 `folders`） |
| overview#5 | 改 | `where-files-go`（长文件 `folders`） |
| overview#6 | 改 | `working-material` |
| overview#7 | 改 | `names`、`fresh-subagent`（长文件 `names`） |
| overview#8 | 改 | `role-entry`（长文件 `roles`） |
| overview#9 | 留 | `only-po-human` |
| overview#10 | 留 | `ask-the-po`（长文件 `roles`） |
| overview#11 | 留 | `po-as-developer` |
| overview#12 | 留 | `stage-gates`（长文件 `gates`） |
| overview#13 | 留 | `one-scrum-master` |
| overview#14 | 改 | `who-gets-which-work`、`answers-back`、`po-word-relayed`、`relay-limits`（长文件 `roles`） |
| overview#15 | 改 | `rule-labels` |
| overview#16 | 改 | `templates-record-outputs` |
| overview#17 | 改 | `goal-fixed`、`po-owns-commitments`、`commitment-table`（长文件 `goal-fixed`） |
| product-log#1 | 留 | `write-product-log` |
| product-log#2 | 留 | `blank-page`（长文件 `product-log`） |
| product-log#3 | 留 | `facts-then-questions` |
| product-log#4 | 改 | `product-log-header` |
| product-log#5 | 改 | `dod-in-product-log`、`dod-standards` |
| product-log#6 | 留 | `stakeholder-table` |
| product-log#7 | 改 | `architecture-map` |
| product-log#8 | 留 | `no-tbd` |
| product-log#9 | 留 | `no-technical-design` |
| product-log#10 | 留 | `item-columns`（长文件 `product-log`） |
| product-log#11 | 留 | `numbers-not-ranks` |
| product-log#12 | 留 | `items-with-sm` |
| product-log#13 | 留 | `status-lives-here` |
| product-log#14 | 留 | `refine-in-sprint` |
| product-log#15 | 改 | `acceptance-written-once` |
| product-log#16 | 留 | `where-refined-content` |
| product-log#17 | 留 | `fresh-at-review` |
| product-log#18 | 留 | `product-log-changes` |
| sprint-log#1 | 留 | `sprint-folder`（长文件 `sprint`） |
| sprint-log#2 | 改 | `no-end-date` |
| sprint-log#3 | 改 | `small-sprint` |
| sprint-log#4 | 改 | `sprint-goal`、`share-goal-and-checks` |
| sprint-log#5 | 改 | `select-items` |
| sprint-log#6 | 改 | `refinement`（长文件 `refinement`） |
| sprint-log#7 | 改 | `how-is-a-plan`、`no-steps`（长文件 `sprint`） |
| sprint-log#8 | 留 | `go-ahead`、`review-handover`（长文件 `sprint`） |
| sprint-log#9 | 改 | `increment-notes`、`mark-done` |
| sprint-log#10 | 改 | `checkpoints`（长文件 `sprint`） |
| sprint-log#11 | 留 | `outline-first` |
| sprint-log#12 | 留 | `full-text-review` |
| sprint-log#13 | 改 | `tests-criteria-first`、`check-script-misses` |
| sprint-log#14 | 改 | `reviewer-required`（长文件 `sprint`） |
| sprint-log#15 | 改 | `acceptance-when-written` |
| sprint-log#16 | 改 | `record-the-tests`（长文件 `sprint`） |
| sprint-log#17 | 改 | `review-at-close`（长文件 `closing`） |
| sprint-log#18 | 改 | `retro-in-memory`（长文件 `closing`） |
| sprint-log#19 | 改 | `one-closing-commit`、`outward-needs-po`（长文件 `closing`） |
| sprint-log#20 | 并 | 并入 overview#17 `goal-fixed`、`po-owns-commitments`、`commitment-table` |
| sprint-log#21 | 留 | `new-work-registered` |
| sprint-log#22 | 改 | `log-is-the-handoff`（长文件 `handoff`） |
| sprint-log#23 | 留 | `outside-blocker`、`mid-sprint-release` |
| sprint-log#24 | 改 | `read-the-goal`（长文件 `gates`） |
| sprint-log#25 | 并 | 并入 overview#10 `ask-the-po` |
| sprint-log#26 | 改 | `developer-elsewhere`（长文件 `handoff`） |
| design-log#1 | 改 | `question-needs-design`、`open-a-design` |
| design-log#2 | 留 | `hard-point-only` |
| design-log#3 | 改 | `design-roles`、`one-session-both-roles` |
| design-log#4 | 改 | `design-branch` |
| design-log#5 | 改 | `design-folder` |
| design-log#6 | 改 | `design-stages`（长文件 `design`） |
| design-log#7 | 留 | 只在长文件 `design`，由 `design-stages` 一行索引 |
| design-log#8 | 改 | 只在长文件 `design`，由 `design-stages` 一行索引 |
| design-log#9 | 改 | 只在长文件 `design`，由 `design-stages` 一行索引 |
| design-log#10 | 留 | `diverge-first`（长文件 `design`） |
| design-log#11 | 改 | 只在长文件 `design`，由 `design-stages` 一行索引 |
| design-log#12 | 留 | `talk-with-po` |
| design-log#13 | 改 | `choose-with-po` |
| design-log#14 | 留 | `combine-or-rumble` |
| design-log#15 | 留 | `storyboard` |
| design-log#16 | 改 | 只在长文件 `design`，由 `design-stages` 一行索引 |
| design-log#17 | 改 | 只在长文件 `design`，由 `design-stages` 一行索引 |
| design-log#18 | 留 | `criteria-before-test` |
| design-log#19 | 改 | `design-ends`、`design-conclusions`（长文件 `design-ending`） |
| design-log#20 | 留 | `ideo-in-every-stage` |
| design-log#21 | 并 | 并入 overview#10 `ask-the-po` |
| design-log#22 | 删 | plugins/ideo-scrum/template/design-backlog-template.md has the five chapters, one per stage, and says each records what its stage produced, not the steps taken (line 8). |
| design-log#23 | 删 | plugins/ideo-scrum/skills/design-kernel/SKILL.md, first paragraph, lists the renamed terms. |
| design-log#24 | 并 | 并入 sprint-log#22 `log-is-the-handoff` |
| design-log#25 | 并 | 并入 overview#17 `goal-fixed`、`po-owns-commitments`、`commitment-table` |
| design-log#26 | 改 | `ideate-arrangement`（长文件 `gates`） |
| design-log#27 | 留 | `small-design` |
| ideo-log#1 | 改 | `sprint-or-modes` |
| ideo-log#2 | 改 | `modes-are-not-the-sprint`、`research-as-empathize` |
| ideo-log#3 | 留 | `open-ideo-log`、`read-mode-file` |
| ideo-log#4 | 改 | `ideo-log-home`、`ideo-log-ends`（长文件 `ideo-ending`） |
| board-log#1 | 改 | `one-board` |
| board-log#2 | 留 | `board-owns-nothing` |
| board-log#3 | 改 | `board-writer`、`board-rules`（长文件 `board-log`） |
| board-log#4 | 留 | 只在长文件 `board-log`，由 `board-rules` 一行索引 |
| board-log#5 | 留 | 只在长文件 `board-log`，由 `board-rules` 一行索引 |
| board-log#6 | 留 | 只在长文件 `board-log`，由 `board-rules` 一行索引 |
| board-log#7 | 删 | plugins/ideo-scrum/board/scrum-board-template.html draws the overview (flow, lighting, colours); the layout reasons are in the design archive of the board. |
| board-log#8 | 改 | 只在长文件 `board-log`，由 `board-rules` 一行索引 |
| board-log#9 | 留 | 只在长文件 `board-log`，由 `board-rules` 一行索引 |
| board-log#10 | 留 | 只在长文件 `board-log`，由 `board-rules` 一行索引 |
| board-log#11 | 留 | 只在长文件 `board-log`，由 `board-rules` 一行索引 |
| board-log#12 | 改 | 只在长文件 `board-log`，由 `board-rules` 一行索引 |
| board-log#13 | 留 | 只在长文件 `board-log`，由 `board-rules` 一行索引 |
| board-log#14 | 删 | plugins/ideo-scrum/board/scrum-board-template.html: names() (lines 283-289) and the no-bar case (lines 538-539) implement it. |
| board-log#15 | 删 | The template's header comment says to write every < as \u003c. |
| board-log#16 | 改 | 只在长文件 `board-log`，由 `board-rules` 一行索引 |
| board-log#17 | 改 | 只在长文件 `board-log`，由 `board-rules` 一行索引 |
| board-log#18 | 改 | 只在长文件 `board-log`，由 `board-rules` 一行索引 |
| board-log#19 | 并 | 并入 board-log#2 `board-owns-nothing` |

## 非编号块（引言、署名、图、Departures 表）

| 块 | 去向 |
| --- | --- |
| overview@1 | The MEMORY.md header carries it: working conventions, follow what fits, override what doesn't, say why in the log's notes. |
| overview@2 | The Source and License lines are at the top of each long file that quotes a guide (departures, goal-fixed, sprint-stages); ATTRIBUTION.md holds the registry. |
| overview@3 | The line rule-labels explains the labels; the pointer to a convention number goes with the numbers. |
| overview@4 | A pointer list to the other convention files and templates; the sections and long files of MEMORY.md replace it. Since Sprint 27 the four log templates sit together in the plugin's template/ folder and the board's files in board/. |
| overview@5 | `flow-maps`（长文件 `flow-maps`） |
| overview@6 | In details/departures.md, as its intro. |
| overview@7 | `departures`（长文件 `departures`） |
| product-log@1 | The MEMORY.md header carries it: working conventions, follow what fits, override what doesn't, say why in the log's notes. |
| product-log@2 | details/goal-fixed.md carries the Scrum Guide quotations with their Source and License lines. |
| product-log@3 | The line write-product-log (the template; the Scrum Master usually writes the product log with the PO). |
| product-log@4 | Drawn in details/flow-maps.md, with the handles in the boxes; the list line flow-maps points there. |
| product-log@5 | Dropped: a pointer to 'Throughout', which the numbering of the old file made. |
| sprint-log@1 | The MEMORY.md header carries it: working conventions, follow what fits, override what doesn't, say why in the log's notes. |
| sprint-log@2 | details/sprint.md carries the Scrum Guide quotation (rule 7) with its Source and License lines. |
| sprint-log@3 | Dropped: the sprint log template's section comments say who writes each section; that a Sprint turns selected items into an Increment is the Scrum Guide's own definition. |
| sprint-log@4 | Drawn in details/flow-maps.md, with the handles in the boxes; the list line flow-maps points there. |
| sprint-log@5 | details/gates.md, Sprint part: closing is a separate decision from the stage transitions. |
| design-log@1 | The MEMORY.md header carries it: working conventions, follow what fits, override what doesn't, say why in the log's notes. |
| design-log@2 | The first section of details/design.md: the template, and where the book describes its room (whiteboards, sticky notes, dot voting, a team at a table) these rules say how a solo + AI team does that step. |
| design-log@3 | Drawn in details/flow-maps.md, with the handles in the boxes; the list line flow-maps points there. |
| design-log@4 | The section The three loops of details/design.md, word for word. |
| design-log@5 | Dropped: a pointer to 'Throughout'; the entry and return rules at each transition are the stage-gates line and details/gates.md. |
| design-log@6 | The first section of details/design.md: these rules cover only what differs from the book or adds what it leaves out; for the rest follow the book's excerpts. |
| ideo-log@1 | The MEMORY.md header carries it: working conventions, follow what fits, override what doesn't, say why in the log's notes. |
| ideo-log@2 | Dropped: the paths are relative to the skill folders; which kernel owns what is in the SKILL.md files. |
| ideo-log@3 | Drawn in details/flow-maps.md, with the handles in the boxes; the list line flow-maps points there. |
| board-log@1 | The MEMORY.md header carries it: working conventions, follow what fits, override what doesn't, say why in the log's notes. |
| board-log@2 | The intro of board-log.md itself, which stays in place in the plugin's board/ folder as the board's long file (the board is one page; its template; this brief). |
| board-log@3 | Drawn in details/flow-maps.md, with the handles in the boxes; the list line flow-maps points there. |

## 新 → 旧

| handle | 来自的旧规矩 |
| --- | --- |
| `acceptance-when-written` | sprint-log#15 |
| `acceptance-written-once` | product-log#15 |
| `answers-back` | overview#14 |
| `architecture-map` | product-log#7 |
| `ask-the-po` | overview#10、sprint-log#25、design-log#21 |
| `blank-page` | product-log#2 |
| `board-owns-nothing` | board-log#2、board-log#19 |
| `board-rules` | board-log#3 |
| `board-writer` | board-log#3 |
| `check-script-misses` | sprint-log#13 |
| `checkpoints` | sprint-log#10 |
| `choose-with-po` | design-log#13 |
| `combine-or-rumble` | design-log#14 |
| `commitment-table` | overview#17、sprint-log#20、design-log#25 |
| `criteria-before-test` | design-log#18 |
| `departures` | overview@7 |
| `design-branch` | design-log#4 |
| `design-conclusions` | design-log#19 |
| `design-ends` | design-log#19 |
| `design-folder` | design-log#5 |
| `design-roles` | design-log#3 |
| `design-stages` | design-log#6 |
| `designs-beside-sprints` | overview#2 |
| `developer-elsewhere` | sprint-log#26 |
| `diverge-first` | design-log#10 |
| `dod-in-product-log` | product-log#5 |
| `dod-standards` | product-log#5 |
| `facts-then-questions` | product-log#3 |
| `flow-maps` | overview@5 |
| `fresh-at-review` | product-log#17 |
| `fresh-subagent` | overview#7 |
| `full-text-review` | sprint-log#12 |
| `go-ahead` | sprint-log#8 |
| `goal-fixed` | overview#17、sprint-log#20、design-log#25 |
| `hard-point-only` | design-log#2 |
| `how-is-a-plan` | sprint-log#7 |
| `ideate-arrangement` | design-log#26 |
| `ideo-in-every-stage` | design-log#20 |
| `ideo-log-ends` | ideo-log#4 |
| `ideo-log-home` | ideo-log#4 |
| `increment-notes` | sprint-log#9 |
| `item-columns` | product-log#10 |
| `items-with-sm` | product-log#12 |
| `log-is-the-handoff` | sprint-log#22、design-log#24 |
| `mark-done` | sprint-log#9 |
| `mid-sprint-release` | sprint-log#23 |
| `modes-are-not-the-sprint` | ideo-log#2 |
| `names` | overview#7 |
| `new-work-registered` | sprint-log#21 |
| `no-end-date` | sprint-log#2 |
| `no-steps` | sprint-log#7 |
| `no-tbd` | product-log#8 |
| `no-technical-design` | product-log#9 |
| `numbers-not-ranks` | product-log#11 |
| `one-board` | board-log#1 |
| `one-closing-commit` | sprint-log#19 |
| `one-product-log` | overview#1 |
| `one-scrum-master` | overview#13 |
| `one-session-both-roles` | design-log#3 |
| `only-po-human` | overview#9 |
| `open-a-design` | design-log#1 |
| `open-ideo-log` | ideo-log#3 |
| `outline-first` | sprint-log#11 |
| `outside-blocker` | sprint-log#23 |
| `outward-needs-po` | sprint-log#19 |
| `po-as-developer` | overview#11 |
| `po-owns-commitments` | overview#17、sprint-log#20、design-log#25 |
| `po-word-relayed` | overview#14 |
| `product-log-changes` | product-log#18 |
| `product-log-header` | product-log#4 |
| `question-needs-design` | design-log#1 |
| `read-mode-file` | ideo-log#3 |
| `read-the-goal` | sprint-log#24 |
| `record-the-tests` | sprint-log#16 |
| `refine-in-sprint` | product-log#14 |
| `refinement` | sprint-log#6 |
| `relay-limits` | overview#14 |
| `research-as-empathize` | ideo-log#2 |
| `retro-in-memory` | sprint-log#18 |
| `review-at-close` | sprint-log#17 |
| `review-handover` | sprint-log#8 |
| `reviewer-required` | sprint-log#14 |
| `role-entry` | overview#8 |
| `rule-labels` | overview#15 |
| `scrum-folders` | overview#4 |
| `select-items` | sprint-log#5 |
| `share-goal-and-checks` | sprint-log#4 |
| `small-design` | design-log#27 |
| `small-sprint` | sprint-log#3 |
| `sprint-folder` | sprint-log#1 |
| `sprint-goal` | sprint-log#4 |
| `sprint-or-modes` | ideo-log#1 |
| `stage-gates` | overview#12 |
| `stakeholder-table` | product-log#6 |
| `status-lives-here` | product-log#13 |
| `storyboard` | design-log#15 |
| `talk-with-po` | design-log#12 |
| `templates-record-outputs` | overview#16 |
| `tests-criteria-first` | sprint-log#13 |
| `three-layers` | overview#3 |
| `where-files-go` | overview#5 |
| `where-refined-content` | product-log#16 |
| `who-gets-which-work` | overview#14 |
| `working-material` | overview#6 |
| `write-product-log` | product-log#1 |
