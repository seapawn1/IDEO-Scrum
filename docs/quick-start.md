# Quick start

One page, from an installed plugin to your first closed Sprint. You work in one Claude Code or DeepSeek Harness (DSH) session as the Product Owner, with the Scrum Master at your side. It assumes you know Scrum; the [glossary](glossary.md) explains the plugin's own terms.

## Before you start

- The plugin is installed ([README](../README.md#install)); if you already have an older version, follow the [upgrade instructions](../README.md#upgrade).
- Your project is a git repository. If it is not, ask the Scrum Master to run `git init` for you; this is a suggestion, not a rule.

## 1. Call the Scrum Master

In a Claude Code session:

```text
/ideo-scrum:scrum-master
```

This Claude Code command calls the IDEO, Scrum, Sprint, and Design kernels in that order before starting work; you don't need to call them yourself. See the [role convention](../plugins/ideo-scrum/skills/scrum-kernel/overview.md#who-does-what) for the other roles.

In a new DSH **Standard** session opened in your project directory:

```text
/scrum-master
```

Say what you are building. In DSH, you can put the request after `/scrum-master` in the same message. You are the Product Owner: you decide the value and the direction, and the Scrum Master serves you.

## 2. Write the product log

The Scrum Master writes `scrum/ProductBacklog.md` with you: the product, the Product Goal, and a few items. Usually it looks up the facts itself and puts what only you can decide into one numbered message, each question with a recommended answer. The top of the file looks like this:

```markdown
### 1.1 Product

| Commitment | Daily Quote: a small command that prints one quote a day. |
| --- | --- |

### 1.2 Product Goal

| Commitment | A morning ritual: a command you enjoy running every day. |
| --- | --- |
```

The Commitment rows hold your product statement and your goal word for word. They stay fixed, and only you change them. An optional explanation below the table is not part of the commitment. If you cannot say yet what the product is or what its Product Goal should be, the Scrum Master works with you on a design once you authorize Empathize.

## 3. Open a Sprint

Ask the Scrum Master to open a Sprint and authorize Why. It gets a branch and a folder, `scrum/sprint-01-<name>/`, and goes through five stages. You settle each result, and explicitly authorize starting or returning to a stage; approving a result alone does not start the next one:

| Stage | What happens | You decide |
| --- | --- | --- |
| Why | The Sprint Goal and verification priorities are set; the full DoD still applies | The Sprint Goal; whether What may start |
| What | Items are selected from the product log and refined | That refinement is over; whether How may start |
| How | A plan is written, not steps | The go-ahead |
| Increment | The work is built, with notes in the sprint log | That it can go into testing |
| Test | The work is tested and reviewed | To close, or to go back |

Read the plan, then say "go ahead". Approving a plan is not a go-ahead: building starts only after it. The Scrum Master may hand the plan, or the building, to a Developer working in the background; if it takes long, ask "Is the plan ready?", or tell the Scrum Master to write it itself. Your first Sprint can be small; even half an hour's work gets one, with each step shrunk to a line or two.

## 4. Build and test

A Developer session (`/ideo-scrum:developer` in Claude Code, `/developer` in DSH) builds, or the Scrum Master does. Whoever builds, someone else reviews: when the Scrum Master built the work, a fresh subagent reviews it. Write the Test method and pass lines before Test. Building checks are not the Sprint Test: ask for permission to start it. The log traces every Output Done standard and item criterion to evidence — even if it was not a focus — including earlier evidence and why it still holds, or a stated condition that did not arise and why it did not apply. Record outcome signals separately; those required for this Test must be supported by evidence that they were met. The Scrum Master can do the git work for you.

## 5. Close

When the Test stage is done, say "close". Review compresses and archives the sprint log in `scrum/documents/` and refreshes the product log. Retro saves only important lessons as separately findable entries in project memory, or in repository lesson notes (still one separately findable entry per lesson) if the tool has no project memory, never in an instructions file or a Sprint Retro summary. With no important lesson, save no entry. One closing commit holds only the changes Review and Retro actually made inside the repository; do not copy outside memory or invent a Retro file for it. Finished designs keep their original material with their archived logs; a Sprint using it as a specification links to it rather than deleting it at close. The commit is tagged with the Sprint folder's name and merged into the main branch; the Scrum Master can do this for you. Pushing waits for your consent.

## Rules worth keeping

1. You settle stage results and explicitly authorize entry or return ([overview](../plugins/ideo-scrum/skills/scrum-kernel/overview.md), convention 12).
2. Building starts only after your go-ahead ([sprint log](../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md), convention 8).
3. The Sprint Goal stays fixed; the plan can change (overview, convention 17).
4. Someone other than the builder reviews (sprint log, convention 14).
5. The log is the handoff: the `Now` and `Waiting for PO` lines at the top of the sprint log say where the Sprint stands and what waits for you (sprint log, convention 22).

## Handing over in writing

You can hand some of your decisions to the Scrum Master in writing: one line in the sprint log's Increment notes saying who, what it covers, and which stages. Include any stage permission you hand over explicitly; handing over a review or a choice within a stage is not permission to move on. For example:

```text
Handover, 2026-11-14: the Product Owner hands the Scrum Master settling the results of Why and What, and authorizing entry into What and How. The Product Owner keeps changing a commitment, cancelling the Sprint, and consenting to a push.
```

## When you are lost

- Ask "Where are we?": the Scrum Master reads `Now` and `Waiting for PO` and tells you.
- Ask for the board: a one-page view of where the project stands, written from the logs into `scrum/ScrumBoard.html`.
- To find out what people want, call the Designer: `/ideo-scrum:designer` in Claude Code, `/designer` in DSH.
