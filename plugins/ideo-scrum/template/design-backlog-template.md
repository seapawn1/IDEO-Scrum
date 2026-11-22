# Design Backlog — <suffix>

> Opened <date> | From: <the product backlog item, the Sprint and the hard point that raised it, or the blank page> | Branch: <branch> | Product Owner: <name> | Designer: <who; takes over at Ideate> | Scrum Master: <who; settles Empathize and Define with the Product Owner and writes them down>
> Now: <the stage the design is in, and the next step> — keep it current; a session that picks up the design reads this first, then checks the recorded stage and git permissions (Memory `log-is-the-handoff`, `stage-gates`); neither `Now` nor stage permission authorizes committing by itself.
> Waiting for PO: <number and short question; separate several with a semicolon; None when there are none>
> Ends when the Product Owner decides the design questions are answered, or stops it (Memory `design-ends`, `design-conclusions`); its conclusions flow back to the product log — a blank page's design fills it — and the first Sprint Review that can read the complete log and original material in its own checkout archives them (Memory `review-at-close`, `disputed-points`). Until then use `Now` to show that the design has ended and awaits archival.
> Methods: the stage excerpts in the design-kernel skill (excerpt paths below are relative to that skill's folder), and in every stage the ideo-kernel's IDEO mode and methods, as the design-kernel `SKILL.md` requires.
> This log records what each stage produced, not every step taken to get there.
> How to write this log: the Memory's *Running a design sprint* section (the memory skill's `SKILL.md`).

## 1. Empathize

<!-- Excerpts: steps/1-1-define-the-challenge.md, steps/1-2-start-at-the-end.md, steps/1-3-ask-the-experts.md. IDEO mode: empathize. Record permission to start Empathize when opening (Memory `stage-gates`). Once authorized, start with the people concerned (Memory `design-stages`); write the challenge, the design goal, and the design questions from what they told you, each finding with its source (Memory `design-stages`); ask the experts and research only when needed (Memory `design-stages`); write what they change into the sections below and into the map. The chapter ends with the Product Owner's decision on its result (Memory `stage-gates`). -->

### 1.1 Challenge

<!-- The big challenge, in a sentence or two. Why now: high stakes, not enough time, or just plain stuck. The situation today and where it hurts go here too, each with its source (Memory `design-stages`); the map in chapter 2 draws the experience we want, not today (Memory `design-stages`). -->

### 1.2 Design goal

| Commitment | <design goal> |
| --- | --- |

<!-- Optimistic: why are we doing this, and where do we want to be? The Product Owner decides. A vision, not how (Memory `design-stages`). An optional explanation can follow the table; it is not part of the goal. -->

### 1.3 Design questions

<!-- Pessimistic: how could this fail? Turn each fear and assumption into a question this design can answer. -->

## 2. Define

<!-- Excerpts: steps/2-1-make-a-map.md, steps/2-2-how-might-we.md. IDEO mode: define. Write the How Might We questions against the map, with the challenge, the design goal, and the design questions of chapter 1 beside it (Memory `design-stages`). The chapter ends with the Product Owner's decision on its result (Memory `stage-gates`). -->

### 2.1 Map

<!-- Actors on top, the ending at the bottom. Mermaid, flowchart TD. The experience we want to reach, not what happens now — that goes in chapter 1: five or six boxes and one loop; branches and solutions stay out (Memory `design-stages`). If you ask the experts, draft it before you do, then fix it as you learn; redraw it after the experts or the research (Memory `design-stages`). -->

### 2.2 How Might We

<!-- HMW questions grouped by theme; mark the ones the Product Owner picked. -->

## 3. Ideate

<!-- Excerpts: steps/3-1-remix-and-improve.md, steps/3-2-sketch.md, steps/3-3-decide.md, steps/3-4-rumble.md, steps/3-5-storyboard.md. IDEO mode: ideate. The book's steps are one way to reach a solution, not the only one: use the ideo-kernel's Ideate methods as `SKILL.md` requires, and have whoever sketches diverge before converging (Memory `diverge-first`); Before doing the work, record how the Product Owner decided to run this round of divergence and whether Ideate is authorized (Memory `stage-gates`). Lightning Demos and subagent sketches are optional (Memory `design-stages`). The chapter ends with the Product Owner's decision on its result (Memory `stage-gates`). -->

### 3.1 Solution

<!-- The solution the Product Owner chose (both, if two go to a rumble — Memory `combine-or-rumble`): a title, and how it works step by step. -->

### 3.2 Storyboard (optional)

<!-- The chosen solution as about fifteen steps, from an opening scene to the end — a step toward the prototype. -->

## 4. Prototype

<!-- Excerpts: steps/4-1-fake-it.md, steps/4-2-prototype.md. IDEO mode: prototype. A chosen solution alone does not start Prototype; check its permission (Memory `stage-gates`). The chapter ends with the Product Owner's decision on its result (Memory `stage-gates`). -->

<!-- List each prototype part, the question it tests, and the usable path to the preserved original. When archiving, verify that the original is readable at its new path before updating the reference. A commit ID or a summary alone is not the location (Memory `design-stages`, `design-ends`, `design-conclusions`). -->

| Part | The design question it tests | Where it is |
| --- | --- | --- |

## 5. Test

<!-- Excerpts: steps/5-1-small-data.md, steps/5-2-interview.md, steps/5-3-learn.md. IDEO mode: test. A trial run does not start Test; check its permission (Memory `stage-gates`). Write the criteria here before testing (Memory `criteria-before-test`), with the role cards you will test with and why (Memory `design-stages`). The chapter ends with the Product Owner's decision: end the design, or go back to the stage whose answer was wrong (Memory `stage-gates`). Next to it, a line or two on what the design taught about how to work, as input to the Retrospective of the Sprint that archives this log (Memory `design-ends`, `design-conclusions`). Link to the working material in the chapters it belongs to; keep it whether the conclusions will be built or not. -->

<!-- Who tested and what showed up, and what the trial run found; then answer each design question in 1.3 — yes, no, or not yet, with the evidence — and say where each conclusion flows back. -->
