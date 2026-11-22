# Writing the Scrum board

This file is the brief for whoever writes the board page: what the board is, what it reads from the logs, the data it holds, what it leaves out, the steps to write it, and the check. Read it in full before you write or refresh `scrum/ScrumBoard.html`. The list lines that point here are `board-writer` and `board-rules`.

## What the board is and who writes it

The Scrum board is one page that shows where the project stands. Its template is `scrum-board-template.html`, in the scrum-kernel skill's `conventions/` folder; this file is also the brief for whoever writes the page.

Keep one page for the whole project: the product, the items not done, and every open Sprint and design. It answers one question without opening a log: where does the project stand, and what is each line of work doing. It is meant to be glanced at — hung on a screen, read from a few steps away, on a wide screen, a portrait screen, or a phone — so it shows few things, and shows them large.

The board only reads the logs. It keeps no state, and no log is ever changed from it. Delete it and write it again, and every fact is the same; only the time it was made differs. For that reason the page need not go into version control; the project decides, for example with a `.gitignore` entry.

Nothing on it changes anything: an item lights up where it goes, a node opens a card, and that is all. It edits no log and keeps no state between pages. Nothing becomes true because it is on the board.

Name it `scrum/ScrumBoard.html`, beside the product log. A cheap model writes it, because the work is copying and summarizing, not judging: a fresh subagent told to read this file and the template and to follow them, or a standing helper session of the Product Owner's. Write it when the Product Owner wants to look, or after a log has changed.

## What it reads

The product log is `scrum/ProductBacklog.md`. The open logs are `scrum/sprint-*/SprintBacklog.md`, `scrum/design-*/DesignBacklog.md`, and `scrum/ideo-*/IdeoBacklog.md`; nothing in `scrum/documents/`, which holds the archive. A Sprint or design that is open on another branch counts too: read its log as committed on that branch (git can show a file at a branch's latest commit), and give `branch <name> @ <commit>` as its source, the commit as its first seven characters. A log that is in this working copy is read from the working copy, with any change not yet committed, and its source is `working copy`. If one log is found on several branches, use the version with the newest commit.

Read these where the logs keep them, and look for nothing else:
- the commitments: a one-row table whose first cell is `Commitment` (`承诺` in a Chinese log) and whose second cell is the exact text; the heading above it says which one it is (`commitment-table`): the Product, the Product Goal, the Sprint Goal, the design goal;
- `> Now:` in a Sprint log, a design log, and an IDEO log (`log-is-the-handoff`, `ideo-log-home`); the product log has none;
- in the product log, section 3.1: the item table has seven columns (`item-columns`); take the number, title, status, and size of each row and leave the rest in the log; and the number of rows in section 3.2;
- in a Sprint log, section 2.1: the numbers of the items it took, in the order the table lists them; and chapter 3: each row's `#` cell, its Work item cell, and whether its Done when cell begins with `✓` (`mark-done`);
- in a design log: the `From` field of the header, which says what the design is for; section 3.1, the chosen solution; and section 3.2, the storyboard, if there is one in the log;
- in an IDEO log: its `For` field, which points to the log it serves, and its Now line.

The product log's map is the Mermaid diagram in section 2.2; a design log's map is the one in its section 2.1. A node's label is the text inside the quotation marks of `["…"]`, `("…")`, or `{"…"}`; arrows and their labels are not nodes.

## The data

The page draws itself from one JSON object in `<script type="application/json" id="board-data">`. These are its fields; those marked with a star are copied from a log, the others are summaries or plain values (the copying rules follow the table):

| Field | What it holds |
| --- | --- |
| `lang` | `zh` when the logs are written in Chinese, otherwise `en`; the labels on the page follow it |
| `generated` | when the page was made, `YYYY-MM-DD HH:MM` |
| `product.name` | the words before the first colon of the Product commitment, or the whole commitment when it has none |
| `product.statement`, `product.goal` ★ | the Product and the Product Goal commitments |
| `product.source` | `working copy`, or `branch <name> @ <commit>` |
| `product.map` | the architecture as a list of stops: `{"text", "note", "here", "branch"}`; `note`, `here`, and `branch` are optional |
| `product.closed` | the number of rows in section 3.2 of the product log; the page calls them "done groups", because a row can be a Sprint, or a clean-up |
| `items` | each item not done: `{"id", "title", "status", "size", "group"}`; the first four ★ |
| `sprints` | each open Sprint: `{"id", "goal", "now", "items", "blocks", "source", "ideo"}`; `id` is the folder's name; `goal` and `now` ★; `items` lists the numbers in section 2.1; `blocks` is `[{"n", "title", "done"}]` for each row of chapter 3, `n` and `title` ★; `ideo` is optional |
| `designs` | each open design: `{"id", "for", "goal", "now", "map", "solution", "story", "source", "ideo"}`; `goal` and `now` ★; `for` lists the item numbers the `From` field names; `map` is a list of stop texts; `solution` is `{"title", "text"}` or `null` when no solution has been chosen; `story` and `ideo` are optional |
| `ideo` | nested in a Sprint or design: `[{"id", "now"}]`, `now` ★; include a still-open IDEO log exactly once, under the open Sprint or design log its `For` header field points to. A mention of `For:` inside the question is not the field; a folder name alone does not identify the host. |

What is marked ★ goes into the data exactly as the log has it: the same characters, the same language; never reworded, shortened, translated, or tidied. A long text such as a Now line is copied mechanically — with a command or a script — rather than retyped: a long text copied by hand loses a character. Only `product.map` and a design's `map`, `solution`, and `story` are summaries. A map stop's text is a few words cut from one node's label: leave out the step number (①, ②), anything in brackets (item numbers, file names), and the explanation after a colon; never reword. So `③ 写产品日志：Product · 架构 · PBI（product-log）` becomes `写产品日志`, and `⑥ 施工（sprint-log）` becomes `施工`. Keep the main line only — five to eight stops, none longer than about twenty characters — and leave out the people at the top, the ending, and every side branch except the design sprint, which is a stop of its own. The steps a Sprint goes through, one after another, are one stop, joined with ` → ` (`Planning → PO 放行 → 施工 → Test`). A design's `map` comes from its own section 2.1, in source order, without people, the ending, or side branches: five or six stops when the map has them, no invented stops; omit it when no map is recorded. On the product map, `note` holds the item numbers in the brackets of the stop's label, as `62 · 64`. `here` lists the ids of open Sprints and designs at that stop: a Sprint at the stop its Now line names (planning, building, or testing), a design at the design sprint stop; leave `here` out when no stop fits. `branch` is true for a stop beside the main line. A design's `solution` summarizes section 3.1: a short `title` for what was chosen and a short `text` for how it is used. Leave out a part the log does not give; a recorded choice without usage details is still a choice. Write `null` when no choice is recorded: drafts, sketches, or a storyboard alone are not a choice. Optional `story` is a short ordered list of `{"title", "text"}` frames from section 3.2 that illustrate the chosen solution; omit it without a storyboard. Add no facts to fill either field.

An item's `group` is `sprint` when its number is in an open Sprint's section 2.1; otherwise `design` when an open design's `From` field names it; otherwise `later` when its status says it is for later; otherwise `next`. Keep the items in the product log's order: the page puts the items of a Sprint or a design in that Sprint's or design's own order.

## What the page works out itself, and how cards link

These are never written in the data, so they cannot be wrong: a Sprint's name from its folder (`sprint-20-presentable` is Sprint 20); a short name from the text before the first colon of a goal, and from the text before the first `——` of an item's title; a design with no colon in its goal is named by its folder's suffix; the count of work items and how many are done; the order of the items; the links.

The page is written to `scrum/ScrumBoard.html`, so a card links to its log relative to the `scrum/` folder (`sprint-01-alpha/SprintBacklog.md`), and only when its source is `working copy`. When the log is only on another branch, the card names the branch and the commit instead, so that no link is dead. Every card's foot starts with its folder's name.

Each card has three layers. The product card: the Product and the Product Goal, word for word; the architecture as one line of a few stops, with "here" at the stop where the open Sprint is; the items not done, grouped. A Sprint card: the Sprint Goal, word for word; the route, its items in order with how many of their work items are done; the work items of chapter 3, done ones marked. A design card: only its own design goal (section 1.2), word for word; its own map as a short line of stops; an independent solution section. Show what was chosen and how it is used, even without a storyboard. When no solution is chosen, keep the section and say so. The foot of a card holds the Now line, folded away until opened, any IDEO log that serves it (the `ideo` field in the table above), and where the log was read.

## What the board leaves out

The page does not show what waits for the Product Owner, nor the five stages a Sprint passes through: the Product Owner asks the Scrum Master for those, and they change faster than a page is written. Items in the product log's section 3.2 are done or closed and are not shown, only counted. Leave out IDEO logs that serve only the product log, have no open host, or have concluded even if not yet archived. Read the state of the IDEO run itself from the `Now` line (for example, `本轮五模式已收尾` or `The IDEO run has concluded`, optionally after the mode); a next step such as `待收尾` or a mention of closed items is not a concluded run. A host whose own `Now` explicitly says the Sprint or design has ended is no longer open, even while its log awaits archiving; finishing one of its stages is not ending the host. This affects only nested IDEO entries, not the discovery of Sprint and design cards (see What it reads). Do not add a card or a new log field.

## How to write it

Follow these steps:
1. Read `scrum-board-template.html`; its first comment says how to use it.
2. Find the logs and read what each one holds (see What it reads).
3. Copy the template to `scrum/ScrumBoard.html` with a command (`cp`, `Copy-Item`), replacing the old page. Do not retype it.
4. Write the data (The data, What the page works out itself, What the board leaves out; write every `<` in the JSON as `\u003c`, so that no text can end the script early, as the template's first comment says) and put it in place of the single placeholder line in the data block. Change nothing else on the page.
5. Check the page, as below.

Check the page against the logs: the JSON reads; every ★ field is found in its log, character for character; every stop of a map is found in the log's map; every number in `items`, `for`, and `here` exists; open the page and see that it shows the board, not a message. Fix what is not.

## Open points for the Product Owner

- The wording of who writes the board ("a standing helper session of the Product Owner's") waits for the secretary role of Sprint 27 (PBI-86).
- The rule that the JSON writes every `<` as `\u003c` was a separate rule (board-log#15) that the verifiers wanted dropped because the template's first comment says it; the step above keeps one clause of it, so the writer is not sent to a rule that is gone.
- The overview layout (board-log#7) is not carried here: the template draws it. The cards rule (board-log#8) is carried in full although only its sentence about the design card's solution section is needed; the PO may cut the rest.
