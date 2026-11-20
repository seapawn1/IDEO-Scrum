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
- **The context is clean.** The entry passes only your question, your constraints and the file paths — not the discussion so far, not a draft answer, and not a leaning of yours.
- **The answer is the advisor's.** It comes back with the verdict and the evidence, and the decision stays yours.

**On the model.** The advisor's definition asks for Fable. If you name another model in the call, that model is used for this call only, and no setting is saved. Whether the host actually ran that model is **not verified** by this entry — the three-case check (requested, substituted, unavailable) is a later configuration item, and until then the answer is not presented as a particular model's work.

## Register a stakeholder from the product log

1. The Product Owner names a stakeholder in the product log's stakeholder table, in `scrum/ProductBacklog.md` §2.1.
2. Ask the plugin to register that row; it shows the definition file and the one-line reference it would add to the table, and writes nothing until you accept.
3. Declining leaves both untouched. A name already in use is reported, never overwritten, and never cleared by editing another scope.
4. After a change, the old definition stays as it was until the new one is accepted; a half-finished write is reported part by part.

## Summon it by name

Once registered, the same file serves both entries:

```text
Agent, subagent_type: "security-reviewer"
```

- **A plain agent call by name**, from Claude Code or from a Developer session.
- **A Workflow's agent step**, naming the same agent type, without pasting the role's text into the script.
- **A temporary view**, where the `stakeholder` entry summons a fresh subagent with the same role card, without any file.

A definition written just now is not visible in the same turn: it takes effect at the next user message boundary in that session. A Workflow also passes the request that started it to its agent, so keep leanings out of the prompt that starts a review.

## Host boundaries

- **Claude Code** is the host these two entries were built and measured on; the host behaviour quoted above was measured on version 2.1.329.
- **DSH** does not get these entries. Its bundle carries the four kernels and the four role commands, and nothing here claims project-level agents work there.
- **A project without Workflows** still summons a registered stakeholder as a plain agent by name; Workflows add a second entry, not a requirement.
