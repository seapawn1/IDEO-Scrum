---
name: project-stakeholder
description: "Use when the user wants to turn a role card the Product Owner already agreed in the product log's stakeholder table into a project-level agent, so that this project can summon that stakeholder by name — first registration, an update, or a re-check for a name clash. It shows the exact file it would write and the product-log reference it would add, and writes nothing until the user accepts; declining leaves both untouched. Not for an ad-hoc Stakeholder view (the `stakeholder` entry does that), not for ranking or deciding, and not for changing the shared Stakeholder command."
---

# Project Stakeholder

A role card agreed in the product log can also live as an agent definition inside this project, so Claude Code and a Workflow can summon that stakeholder by name, each time in a fresh context. This entry is the only place that writes such a definition, and it writes it with the user's explicit agreement.

## 1. Find the card, and the file it would become

- Read `scrum/ProductBacklog.md` and take the row of the stakeholder table in §2.1 that the user names. The table has a `Who`, a `What they want` and a `When to summon` column; do not assume any other shape, and do not invent a row.
- If the table is empty, or the user has not said which row, stop and ask. The Product Owner names stakeholders; you do not.
- The target is `.claude/agents/<name>.md` at **this project's root** — the same folder the product log sits under. Never write into `~/.claude/agents/`, and never into another project.

## 2. Check for a name clash before anything else

- Look for an existing definition with the same name in every scope that could shadow this one: the project's `.claude/agents/`, the user's `~/.claude/agents/`, and any plugin agent of the same name.
- **A clash is reported, never silently overwritten.** If another definition already answers to that name, say which file wins today, and let the user decide whether to rename, replace it, or stop.
- Never delete or edit a definition in another scope to clear a clash.

## 3. Show the whole change, then ask

Show, as one proposed change:

- **The definition file**: its full path and its full text.
- **The product-log reference**: the relative path `.claude/agents/<name>.md` added to the `When to summon` cell of that row, so the log points at the definition.

Wait for an explicit yes. "Show me" is not a yes, and a permission to write files is not an agreement to this content. If the user declines, write nothing — neither the file nor the reference — and say that both are unchanged.

## 4. Write what was agreed, and only that

- **The definition carries the card and nothing else**: the identity the card states, the existing outside-feedback boundary from the Stakeholder command, and the kernel entry. Keep what the card leaves open open — do not fill gaps with invented wants.
- **Do not put earlier reviews, opinions or meeting notes into the definition.** A definition that carries old verdicts stops being an independent view.
- **Keep the Review summoning right where it is.** At Sprint Review the Product Owner or Scrum Master summons the Stakeholder through a fresh subagent; registering a definition does not make the builder its summoner, and does not turn a standing PO assistant into an independent reviewer.
- If a write fails halfway, say exactly which of the two parts landed and which did not, and bring them back into agreement before continuing. Do not report the change as complete while the file and the reference disagree.

## 5. How the two entries reach it

- A **plain agent call by name** and a **Workflow's agent step** both read the same file; neither needs a copy of its text, and neither should be given the role's content inline instead.
- **Host behaviour measured on Claude Code 2.1.329** (Sprint 22, H2): a newly written `.claude/agents/<name>.md` is not picked up in the same turn. It takes effect at the **next user-message boundary in the same session** — no restart needed. Tell the user this when a summon right after writing reports the agent as not found.
- **A Workflow passes the request that triggered it to its agent** as `[Workflow harness — user request]`. So whoever writes the prompt that starts a Workflow-based review must keep leanings and earlier opinions out of that prompt, or they travel with it.

## Not for this entry

- A one-off outside view, or the PO assistant's chores — the `stakeholder` entry covers both.
- Writing to the shared `commands/stakeholder.md`, the kernels, or the DSH bundle. This entry only adds a project-level definition and its product-log reference.
