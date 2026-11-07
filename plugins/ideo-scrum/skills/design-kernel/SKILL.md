---
name: design-kernel
description: "Use when the user wants a design sprint or a design — \"run a design sprint\", \"open a design for this\", \"this needs designing before we build\" — or works in a design log (DesignBacklog), or when a challenge is still undefined and needs research before any execution; load it before answering. Covers the design sprint from Knapp's Sprint, organized by the five IDEO stages instead of five days: Empathize (challenge, design goal, design questions, ask the experts), Define (map, How Might We, target), Ideate (sketch solutions, choose one, storyboard), Prototype, and Test (interviews, learn). Each stage takes its methods from the ideo-kernel skill, the plugin's shared toolbox; a design's conclusions flow back to the product backlog and to the scrum-kernel Sprint that asked for it."
---

# Design Kernel

A design answers a hard question before the team builds: it starts from a challenge and ends with a tested prototype and conclusions. The method is the design sprint from Knapp, Zeratsky & Kowitz, _Sprint_ (2016), regrouped under the five IDEO stages. The book runs the sprint Monday to Friday with a team in one room; here the stages run as fast as the work allows, not by day. Day names left in the source text are the book's schedule, not an instruction.

Each stage maps to an IDEO mode. The mode's guide and its methods live in the ideo-kernel skill, the plugin's shared toolbox, and are not repeated here — read the mode file named in the table when you need them.

**IDEO methods are always in play.** The book's methods excerpted here are added so the design sprint runs as one piece; they do not limit what you use. In any stage, use any method from the ideo-kernel toolbox whenever the work needs it — for example, Interview for Empathy while asking the experts, or Brainstorming and Analogous Empathy while ideating — even where the book prefers a different technique.

*(Author's methodology design for solo + AI teams, 2026-11-08; source excerpts are cited per file.)*

## Five Stages

| Stage | IDEO mode (ideo-kernel) | What happens | Source excerpts |
| --- | --- | --- | --- |
| **Empathize** | `../ideo-kernel/IDEO-modes/empathize.md` | Write the challenge, the design goal, and the design questions; then ask the experts and research | `empathize/define-the-challenge.md`, `empathize/start-at-the-end.md`, `empathize/ask-the-experts.md` |
| **Define** | `../ideo-kernel/IDEO-modes/define.md` | Make a map; turn what you learned into How Might We questions; pick a target if the challenge is too wide | `define/make-a-map.md`, `define/how-might-we.md`, `define/pick-a-target.md` |
| **Ideate** | `../ideo-kernel/IDEO-modes/ideate.md` | Gather existing ideas; each person sketches one solution alone; decide which to prototype; rumble if two winners conflict; storyboard the winner | `ideate/remix-and-improve.md`, `ideate/sketch.md`, `ideate/decide.md`, `ideate/rumble.md`, `ideate/storyboard.md` |
| **Prototype** | `../ideo-kernel/IDEO-modes/prototype.md` | Adopt the prototype mindset and build a realistic facade of the storyboard — just enough to learn; divide the work, stitch it together, do a trial run | `prototype/fake-it.md`, `prototype/prototype.md` |
| **Test** | `../ideo-kernel/IDEO-modes/test.md` | Interview five target users one at a time with the Five-Act Interview; watch together, look for patterns, and answer the design questions | `test/small-data.md`, `test/interview.md`, `test/learn.md` |

## Conventions

How a solo + AI team runs a design — where the design log lives, who decides, how each stage works with subagents and role cards, and how a design closes — is in `conventions/design-log.md`. The design log template is `conventions/design-backlog-template.md`. These are working conventions, not source text: follow what fits, override what doesn't, and note why.

## Use Protocol

1. Work in the design log — `scrum/design-<suffix>/DesignBacklog.md`, started from the template. Read the conventions once when the design opens.
2. Identify the current stage. Keep to the stage order — Empathize, Define, Ideate, Prototype, Test — and go back when a later stage shows that an earlier answer was wrong.
3. Read the stage's source excerpts before running it, and treat them as source text.
4. Use the IDEO methods whenever the work needs them — first from the mode the stage maps to, but from any mode if it helps — following the ideo-kernel skill's Use Protocol.
5. The Product Owner decides the design goal, the chosen solution, and when the design is done.
6. When the design questions are answered, the conclusions flow back to the product backlog and to the Sprint that asked for the design (scrum-kernel skill).
