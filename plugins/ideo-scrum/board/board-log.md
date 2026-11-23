# Scrum Board Conventions

> Working conventions: reference, not law — follow what fits, depart from what doesn't, note why. Source labels and short names are explained in Memory `rule-labels` (`../skills/memory/details/names.md`). A convention with no label is the author's practice.
>
> **Scope & transparency:** This board focuses strictly on the **Product and Scrum Sprints** (product card and open Sprint cards). It does **not** cover standalone IDEO five-modes discovery logs (`scrum/ideo-*/IdeoBacklog.md`). Check `scrum/ideo-*/` or ask the Scrum Master when inspecting IDEO research state.

The Scrum board is one page that shows where the project stands. Its template is `scrum-board-template.html`, beside this file in `board/`; this file is also the brief for whoever writes the page.

```mermaid
flowchart TD
    L["The logs<br/>product log and open Sprint logs"] --> R["Read<br/>conventions 4–6"]
    R --> D["Write the data<br/>conventions 11–16"]
    D --> G["Put it in the template<br/>convention 17"]
    G --> B["scrum/ScrumBoard.html<br/>conventions 1–3, 7–10"]
    B -. "delete it, write it again" .-> L
```

## What the board is

1. **One board for the project** — Keep one page for the whole project: the product, the items not done, and every open Sprint. It answers one question without opening a log: where does the project stand, and what is each Sprint doing. It is meant to be glanced at — hung on a screen, read from a few steps away, on a wide screen, a portrait screen, or a phone — so it shows few things, and shows them large.
2. **It owns nothing** — The board only reads the logs. It keeps no state, and no log is ever changed from it. Delete it and write it again, and every fact is the same; only the time it was made differs. For that reason the page need not go into version control; the project decides, for example with a `.gitignore` entry.
3. **Where it lives, who writes it, and when** — Name it `scrum/ScrumBoard.html`, beside the product log. A cheap model writes it, because the work is copying and summarizing, not judging: a fresh subagent told to read this file and the template and to follow them, or the Supporter (the `supporter` entry). Write it when the Product Owner wants to look, or after a log has changed.

## What it reads

4. **The logs** — The product log is `scrum/ProductBacklog.md`. The open Sprint logs are `scrum/sprint-*/SprintBacklog.md`; nothing in `scrum/documents/`, which holds the archive, and nothing in `scrum/ideo-*/`, which the board does not track. A Sprint that is open on another branch counts too: read its log as committed on that branch (git can show a file at a branch's latest commit), and give `branch <name> @ <commit>` as its source, the commit as its first seven characters. A log that is in this working copy is read from the working copy, with any change not yet committed, and its source is `working copy`. If one log is found on several branches, use the version with the newest commit. The product log is read the same way when it is not in this working copy; how to write its source is in convention 11 (`product.source`).
5. **What it takes from a log** — Read these where the conventions say they are, and look for nothing else:
    - the commitments: a one-row table whose first cell is `Commitment` (`承诺` in a Chinese log) and whose second cell is the exact text; the heading above it says which one it is (Memory `goal-fixed`, `commitment-table`): the Product, the Product Goal, and each Sprint Goal;
    - `> Now:` in each Sprint log (Memory `log-is-the-handoff`); the product log has none;
    - in the product log, section 3.1: the item table has seven columns (Memory `item-columns`); take the number, title, status, and size of each row and leave the rest in the log; and the number of rows in section 3.2;
    - in a Sprint log, section 2.1: the numbers of the items it took, in the order the table lists them; and in chapter 3 (`## 3. How`), the four-column work-item table whose header names `Work item` (`工作项`) and `Done when` (`完成条件`): take each row's `#` cell, its Work item cell, and whether its Done when cell begins with `✓` (Memory `how-is-a-plan`, `mark-done`). Skip any other prose or comparison tables in chapter 3; if chapter 3 has no matching work-item table, write `blocks: []`.
6. **Maps** — The product log's map is the Mermaid diagram in section 2.2. A node's label is the text inside the quotation marks of `["…"]`, `("…")`, or `{"…"}`; arrows and their labels are not nodes.

## What the page shows

7. **The overview** — A tall flow diagram. At the top, a circle for the product. Below it, the items that are not done, in three groups: in a Sprint, up next, and later; the later ones fade. Each item that sits in a Sprint is joined by a blue line to that Sprint's node on the right. Pressing an item lights up where it goes. Pressing the circle or a Sprint opens its card. One colour, amber, is kept for "here": where the open work stands on the map.
8. **The cards** — Each card has three layers. The product card: the Product and the Product Goal, word for word; the architecture as one line of a few stops, with "here" at the stop where the open Sprint is; the items not done, grouped. A Sprint card: the Sprint Goal, word for word; the route, its items in order with how many of their work items are done; the work items of chapter 3, done ones marked (hidden automatically when `blocks` is empty). The foot of a Sprint card holds the Now line, folded away until opened, and where the log was read.
9. **What the page works out itself** — These are never written in the data, so they cannot be wrong: a Sprint's name from its folder (`sprint-20-presentable` is Sprint 20); a short name from the text before the first colon of a goal, and from the text before the first `——` of an item's title; the count of work items and how many are done; the order of the items; the links.
10. **Links and sources** — The page is written to `scrum/ScrumBoard.html`, so a card links to its log relative to the `scrum/` folder (`sprint-01-alpha/SprintBacklog.md`), and only when its source is `working copy`. When the log is only on another branch, the card names the branch and the commit instead, so that no link is dead. Every card's foot starts with its folder's name.

## The data

11. **One block of data** — The page draws itself from one JSON object in `<script type="application/json" id="board-data">`. These are its fields; those marked with a star are copied from a log, the others are summaries or plain values (convention 12):

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
    | `sprints` | each open Sprint: `{"id", "goal", "now", "items", "blocks", "source"}`; `id` is the folder's name; `goal` and `now` ★; `items` lists the numbers in section 2.1; `blocks` is `[{"n", "title", "done"}]` for each row of the chapter 3 work-item table, `n` and `title` ★ (`[]` when no work-item table is present) |

12. **Copied, and summarized** — What is marked ★ goes into the data exactly as the log has it: the same characters, the same language; never reworded, shortened, translated, or tidied. A long text such as a Now line is copied mechanically — with a command or a script — rather than retyped: a long text copied by hand loses a character. Only `product.map` is a summary. A map stop's text is a few words cut from one node's label: leave out the step number (①, ②), anything in brackets (item numbers, file names), and the explanation after a colon; never reword. So `③ 写产品日志：Product · 架构 · PBI（product-log）` becomes `写产品日志`, and `⑥ 施工（sprint-log）` becomes `施工`. Keep the main line only — five to eight stops, none longer than about twenty characters — and leave out the people at the top, the ending, and side branches unless one is worth showing (`branch: true`). The steps a Sprint goes through, one after another, are one stop, joined with ` → ` (`Planning → PO 放行 → 施工 → Test`). On the product map, `note` holds the item numbers in the brackets of the stop's label, as `62 · 64`. `here` lists the ids of open Sprints at that stop (the stop its Now line names: planning, building, or testing); leave `here` out when no stop fits.
13. **Groups and order** — An item's `group` is `sprint` when its number is in an open Sprint's section 2.1; otherwise `later` when its status says it is for later; otherwise `next`. Keep the items in the product log's order: the page puts the items of a Sprint in that Sprint's own order.
14. **Work items and items** — A work item belongs to an item when its Work item cell names the item's number as written, or the number alone, as `68-a`. A work item that names no item belongs to none. The page counts only these; when no work item of a Sprint names one of its items, that Sprint's route lists the items without a bar.
15. **Escaping** — In the JSON, write every `<` as `\u003c`, so that no text can end the script early.
16. **Left out on purpose** — The page does not show what waits for the Product Owner, nor the five stages a Sprint passes through: the Product Owner asks the Scrum Master for those, and they change faster than a page is written. Items in the product log's section 3.2 are done or closed and are not shown, only counted. Standalone IDEO discovery logs (`scrum/ideo-*/IdeoBacklog.md`) are left out on purpose; the board covers only the product and Scrum Sprints. Do not add a card or a new log field.

## How to write it

17. **Steps** — Follow these steps:
    1. Read `scrum-board-template.html`; its first comment says how to use it.
    2. Find the logs (convention 4) and read what each one holds (conventions 5 and 6).
    3. Copy the template to `scrum/ScrumBoard.html` with a command (`cp`, `Copy-Item`), replacing the old page. Do not retype it.
    4. Write the data (conventions 11–16) and put it in place of the single placeholder line in the data block. Change nothing else on the page.
    5. Check the page (convention 18).
18. **Check** — Check the page against the logs: the JSON reads; every ★ field is found in its log, character for character; every stop of `product.map` is found in the product log's map; every number in `items` and `here` exists; open the page and see that it shows the board, not a message. Fix what is not.
19. **What the board does not do** — Nothing on it changes anything: an item lights up where it goes, a node opens a card, and that is all. It edits no log and keeps no state between pages. Nothing becomes true because it is on the board.
