# Project agents

Two additions to the plugin let a project keep an outside view at hand: a read-only **advisor** you call for a second opinion, and a **project stakeholder** registered from a role card the Product Owner already agreed. Both work in Claude Code; the DeepSeek Harness (DSH) side is covered at the end.

## Advisor or project stakeholder

They answer different questions, and the Product Owner decides which one is wanted.

| | Advisor | Project stakeholder |
| --- | --- | --- |
| The question | "Is this decision sound, given these materials?" | "What does this person or group think of the product?" |
| Where the identity comes from | None — it reads the files you name | A role card in the product log's stakeholder table |
| How it is called | `/ideo-scrum:second-opinion`, every time | A file the project keeps, summoned by name |
| What it may do | Read the named files, and load the kernels | The same outside view the `stakeholder` entry gives |

## Ask for a second opinion

The entry takes the open question, the constraints, and the exact files to read:

```text
/ideo-scrum:second-opinion Can we switch the library's door system next Monday? constraints: decide from the originals only | files: materials/launch-checklist.md
```

- **It is manual by design.** Claude does not reach for it on its own, and the entry is not in Claude's list of invocable skills; you start it.
- **The brief is clean.** The entry passes only your question, your constraints and the file paths — not the discussion so far, not a draft answer, and not a leaning of yours.
- **The answer is the advisor's.** It comes back with the verdict and the evidence, and the decision stays yours.

**On the model.** The advisor's definition asks for Fable, which needs access on your account. To use another model, add `| model: opus` (or another name) to the request; the entry requests it for that call only and changes no settings. If Fable is not available to your account, the entry says so and asks which model to use. It **does not verify** which model the host actually ran. Checking whether the requested model ran, was substituted, or was unavailable is left for later; the entry does not attribute the answer to a specific model.

## Register a stakeholder from the product log

```text
/ideo-scrum:project-stakeholder
```

1. The Product Owner names a stakeholder in the product log's stakeholder table, in `scrum/ProductBacklog.md` §2.1 — in any language, with roles down the rows or across the columns.
2. Register that role card; the entry shows the definition file and the one-line reference it would add, and writes nothing until you accept. Claude Code may also ask for its own permission to write under `.claude/`; that prompt is separate from your acceptance.
3. Declining leaves both untouched. A name already in use is reported, never overwritten, and never cleared by editing another scope.
4. After a change, the old definition stays as it was until the new one is accepted; a half-finished write is reported part by part.

## Summon it by name

Once registered, the same file serves the first two of these; the third needs no file:

```text
Agent, subagent_type: "security-reviewer"
```

- **A plain agent call by name**, from a Claude Code session or a Developer session; the outside view at Sprint Review is still summoned only by the Product Owner or the Scrum Master.
- **A Workflow's agent step**, naming the same agent type, without pasting the role's text into the script.
- **A temporary view**, where the `stakeholder` entry summons a fresh subagent with the same role card, without any file.

In the tested interactive session, a newly written definition became available at the next user message, not in the same turn. The tested headless `-p` streaming session did not load the new definition at that boundary. A Workflow also passes the request that started it to its agent, so keep leanings out of the prompt that starts a review.

## Host boundaries

- **Claude Code** is the host these two entries were built and measured on; the host behaviour quoted above was measured on version 2.1.329.
- **DSH** does not get these entries. Its bundle carries the three kernels and the four role commands, and nothing here claims project-level agents work there.
- **A project without Workflows** still summons a registered stakeholder as a plain agent by name; Workflows add a second entry, not a requirement.
