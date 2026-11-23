---
name: project-stakeholder
argument-hint: "<name of the role card in the product log's stakeholder table>"
description: "Use when the user wants to turn a role card the Product Owner already agreed in the product log's stakeholder table into a project-level agent, so that this project can summon that stakeholder by name — first registration, an update, or a re-check for a name clash. The table may be in any language, with roles down the rows or across the columns; it finds the card either way. It shows the exact file it would write and the product-log reference it would add, and writes nothing until the user accepts; declining leaves both untouched. Not for an ad-hoc Stakeholder view (the `stakeholder` entry does that), not for ranking or deciding, and not for changing the shared Stakeholder command."
---

# Project Stakeholder

A role card agreed in the product log can also live as an agent definition inside this project, so Claude Code and a Workflow can summon that stakeholder by name, each time in a fresh context. This entry is the only place that writes such a definition, and it writes it with the user's explicit agreement.

The user can also start it directly with `/ideo-scrum:project-stakeholder`.

## 1. Find the card, whatever shape the table has

Read `scrum/ProductBacklog.md` and work from §2.1, the stakeholder table. **Its shape differs from project to project, and all of these are normal:**

- **Roles across the rows** — one row per stakeholder, with columns such as who / what they want / when to summon.
- **Roles down the columns** — one column per stakeholder, with a row per fact (this repository's own product log is written this way).
- **Any language, and any set of facts.** A card may carry rows the template never had, such as what counts as a good outcome, what it may see, or what it is responsible for.

So find the card by what it says, not by a fixed position: the **card** is the cell holding the stakeholder the user named, and its **facts** are the cells that line up with it — down its column when roles sit in columns, across its row when roles sit in rows. The cell that says when to summon it is the one whose companion label means that, in whatever language the table uses; if no such cell exists, say so rather than inventing one, and follow section 3 for what happens next.

- Take only what the card actually states. Do not fill a fact the card leaves blank, do not normalise its wording away, and do not assume a field the table does not have.
- If §2.1 is empty, or the user has not said which card, stop and ask. The Product Owner names stakeholders; you do not.
- The target is `.claude/agents/<name>.md` at **this project's root** — the same folder the product log sits under. Never `~/.claude/agents/`, and never another project.

## 2. Check for a name clash before anything else

- Look for an existing definition with the same name in every scope that could shadow this one: the project's `.claude/agents/`, the user's `~/.claude/agents/`, and any plugin agent of the same name.
- **A clash is reported, never silently overwritten.** Say which file answers to that name today, and let the user decide whether to rename, replace it, or stop.
- Never delete or edit a definition in another scope to clear a clash.

## 3. Show the whole change, then ask

Show, as one proposed change:

- **The definition file**: its full path and its full text.
- **The product-log change**: the relative path `.claude/agents/<name>.md` added to that card's when-to-summon cell — the one belonging to that stakeholder, in whichever direction the table runs.

Wait for an explicit yes. "Show me" is not a yes, and a permission to write files is not an agreement to this content. If the user declines, write nothing — neither the file nor the reference — and say that both are unchanged.

**When updating an existing definition**, also show a **diff** against the file and the reference as they stand now.

**When the card has no when-to-summon cell**, show the definition file alone and say that the product log gets no reference because there is no cell to put it in. The user chooses: write the file without the reference, or stop until the Product Owner adds the cell. Never add a cell, row or column to the table yourself.

## 4. Write what was agreed, and only that

**The definition's shape** — the least a working project agent needs:

```yaml
---
name: <card-name-in-kebab-case>
description: "Use when <this stakeholder should be summoned>, in one line"
tools: Read, Grep, Glob, Skill
---
```

- `name` matches the file name, both kebab-case, so the card name and the invocation name cannot drift apart.
- `description` is a **single-line, double-quoted** string of at most 1024 characters, and it says when to summon this stakeholder — that is what the host shows before anyone reads the body.
- **No permission to change the product's source.** The definition keeps the boundary the `stakeholder` entry states: feedback goes to the Product Owner, source belongs to the Developer. Do not grant `Write`, `Edit`, `NotebookEdit`, re-delegation or MCP; a card that has to try the product (a stranger's first-run test, say) may get `Bash` only when the user asks for it explicitly.

**The body** carries, in this order:

1. The role card's identity, in the card's own words.
2. The kernel entry: invoke `ideo-scrum:ideo-kernel` and then `ideo-scrum:scrum-kernel` with the `Skill` tool, in that order; load `ideo-scrum:sprint-kernel` only when the work involves a Sprint. Reading a file is not invoking a skill.
3. The card's stated boundaries — what it may see, what it is responsible for, and what it is not.

**Do not put earlier reviews, opinions or meeting notes into the definition.** A definition that carries old verdicts stops being an independent view.

**Keep the Review summoning right where it is.** At Sprint Review the Product Owner or Scrum Master summons the Stakeholder through a fresh subagent; registering a definition does not make the builder its summoner, and does not turn a standing Supporter into an independent reviewer.

**Expect the host's own prompt.** Claude Code may ask separately for permission to write under `.claude/`. That prompt is the host's and does not replace the user's yes to the preview: get the yes here first, then let the write reach the host's prompt.

**Before writing, look again.** Re-read the target file and the product log's §2.1 and confirm neither changed since you showed the preview. If one did, stop and show the new difference instead of overwriting it.

If a write fails halfway, say exactly which of the two parts landed and which did not, and bring them back into agreement before continuing. Do not report the change as complete while the file and the reference disagree.

## 5. How the two entries reach it

- A **plain agent call by name** and a **Workflow's agent step** both read the same file; neither needs a copy of its text, and neither should be given the role's content inline instead.
- **Host behaviour measured on Claude Code 2.1.329** (Sprint 22, H2 and H7): in an interactive session, a newly written `.claude/agents/<name>.md` was picked up at the **next user-message boundary in that session**, not in the same turn, without a restart. In the tested headless `-p` streaming session, the new definition was not picked up at that boundary. If a summon reports the agent as not found just after writing, explain the distinction rather than promising a reload on the next turn in headless mode.
- **A Workflow passes the request that triggered it to its agent** as `[Workflow harness — user request]`. So whoever writes the prompt that starts a Workflow-based review must keep leanings and earlier opinions out of that prompt, or they travel with it.

## Not for this entry

- A one-off outside view — the `stakeholder` entry covers it; the Supporter's chores — the `supporter` entry covers them.
- Writing to the shared `commands/stakeholder.md`, the kernels, or the DSH bundle. This entry only adds a project-level definition and its product-log reference.
