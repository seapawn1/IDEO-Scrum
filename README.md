<p align="center"><img src="plugins/ideo-scrum/icon.png" width="96" alt="IDEO-Scrum icon: a loop around a diamond"></p>

# IDEO-Scrum

A Claude Code plugin that brings Design Thinking and Scrum Sprints to a project you build alone with AI. **v6.0.2**

[中文](README.zh-CN.md) · [Install](#install) · [Quick start](docs/quick-start.md) · [Glossary](docs/glossary.md) · [Changelog](CHANGELOG.md)

> **License note.** The d.school material in this plugin is licensed for non-commercial use only, so this repository is not open-source software in the OSI sense. See [License and attribution](#license-and-attribution).

## What it is

When you build a project alone with an AI, the rules and the state of the work live in your head and in the chat. A session ends or is compacted, and they go with it. The AI can drift, and no one but the builder looks at what it built.

IDEO-Scrum puts a Scrum team around the work. You are the Product Owner: you decide the direction, the goals, which items enter a Sprint, and when building may start. The AI plays the Scrum Master, the Developer, the Designer and the Stakeholder, one role per command. When the question is what people want, or what counts as good, it brings the design thinking of IDEO and Stanford's d.school: the five modes, or a design sprint. Everything is written into plain Markdown logs in your repository, so a new session reads the log and carries on.

It is not a project-management tool: no JIRA or Linear integration, and not a platform for a team.

## A session, shortened

Illustrative and shortened, not a transcript; the wording will differ. The stops are the point: at the end of each stage the work waits for you.

```text
You:            /ideo-scrum:scrum-master
                I'm building a small CLI that prints one quote a day. Help me get started.
Scrum Master:   First the product log: what is the product, and what should it achieve next?
You:            It prints a quote every morning. Done means I still enjoy it after a month.
Scrum Master:   Written to scrum/ProductBacklog.md: the product, the Product Goal, three items.
                Shall we open a Sprint?
You:            Yes.
Scrum Master:   Why, the Sprint Goal: "Daily quote: it prints one quote from a list; adding a quote
                takes one command." That is the goal. Do you decide it, and move on to What?
You:            Yes.
                ... What: you pick and refine the items. How: the Developer writes a plan ...
Developer:      The plan is in chapter 3 of the sprint log. I won't build until you give the go-ahead.
You:            Go ahead.
                ... the Developer builds and keeps notes; someone else reviews; you decide when to close ...
```

What this leaves in your repository is plain Markdown you can read and edit: `scrum/ProductBacklog.md` and `scrum/sprint-01-<name>/SprintBacklog.md`. The [quick start](docs/quick-start.md) walks through the whole thing, step by step.

## Who it is for

A good fit:

- You build your own project with Claude Code, and you know Scrum, or will read the Scrum Guide beside this plugin (it ships with it).
- You want the rules to follow the plugin instead of being dictated again in every session, and a session that breaks off or is compacted to pick up where it stopped.

Not a fit:

- You need JIRA or Linear integration, or a platform for a whole team.
- You want the AI to run a project on its own: by default the work stops for you at the end of every stage.
- You want Scrum to the letter of the Scrum Guide: see [How it differs from textbook Scrum](#how-it-differs-from-textbook-scrum).

## Install

You need Claude Code. A git repository for your project is recommended; the Scrum Master can set one up for you.

In a Claude Code session:

```text
/plugin marketplace add seapawn1/IDEO-Scrum
/plugin install ideo-scrum@ideo-scrum
/reload-plugins
```

To check, run `claude plugin list` in a terminal: it shows `ideo-scrum@ideo-scrum` as enabled.

Codex is a companion edition, generated from the same source; the first-Sprint walkthrough is tested on Claude Code only. In a terminal:

```sh
codex plugin marketplace add seapawn1/IDEO-Scrum
codex plugin add ideo-scrum@ideo-scrum
```

Then, in a new Codex session, type `$` and pick a role from the skill menu: `$scrum-master`, `$designer`, `$developer`, `$stakeholder`.

## Upgrade

```sh
claude plugin update ideo-scrum@ideo-scrum
```

Run it in a terminal, then `/reload-plugins` in a session that is already open. Third-party marketplaces do not update themselves by default: to have Claude Code do it, open `/plugin`, go to Marketplaces, select `ideo-scrum` and choose Enable auto-update. What changed in each release is in the [changelog](CHANGELOG.md).

On Codex, refresh the marketplace, then remove the plugin and add it again. We have not tested this path end to end.

```sh
codex plugin marketplace upgrade ideo-scrum
codex plugin remove ideo-scrum@ideo-scrum
codex plugin add ideo-scrum@ideo-scrum
```

## Your first sentence

In a Claude Code session, call a role:

```text
/ideo-scrum:scrum-master    # facilitates Planning, checkpoints, Review and Retro; reviews the work; serves you, the Product Owner
/ideo-scrum:developer       # runs a Sprint: the plan, the Increment, the sprint log
/ideo-scrum:designer        # research and prototypes: the five modes and design sprints; builds nothing before you decide
/ideo-scrum:stakeholder     # an outside view of the product, or a standing assistant for chores such as the board
```

Or say it in your own words:

```text
Use ideo-scrum to plan the next Sprint; I have five items to refine.
I'm not sure this feature is worth building. Run a round of user research first.
```

What loads, and when: the Scrum, Sprint and design-sprint material comes only when summoned, by a role command, by naming ideo-scrum or one of its kernels, or by asking to create or change its logs; a general question about Scrum is answered as usual. The IDEO methods often step in by themselves for prototyping and testing. For brainstorming and defining a problem the model usually answers directly: name `ideo-kernel` if you want its methods (a known limitation).

## How it differs from textbook Scrum

The plugin departs from the official guides in seven places, on purpose. Each is stated once, with its reason, in [`overview.md`](plugins/ideo-scrum/skills/scrum-kernel/overview.md#departures-from-the-official-guides); this is the short version.

| Here | Why |
| --- | --- |
| Only the Product Owner must be human | One person works with AI and keeps the value decisions |
| Designs sit beside Sprints | A design delivers no Increment, may span several Sprints, and the Designer and the Developer are peers |
| The Product Owner decides the items with the Scrum Master | The Product Owner sets the value direction, and the others say how much fits |
| The How is a plan, and building waits for the go-ahead | The Scrum Master and the Product Owner check the plan, because AI may drift |
| Checkpoints replace the Daily Scrum | AI works by session, not by day |
| A reviewer is required | A Developer may drift, and a second look catches it |
| No Sprint end date | AI works by session, so the Product Owner watches at checkpoints for a Sprint that drags on |

## Where the work lives

Your project grows a `scrum/` folder. This is the author's layout; use your project's own places if it has them.

| Path | What it holds |
| --- | --- |
| `scrum/ProductBacklog.md` | The product log: the product, the Product Goal, the items |
| `scrum/sprint-NN-<name>/SprintBacklog.md` | One Sprint, from Why to Test, with its notes |
| `scrum/design-<name>/DesignBacklog.md` | One design: research and prototypes |
| `scrum/ideo-<name>/IdeoBacklog.md` | One run of the five modes |
| `scrum/ScrumBoard.html` | The board: a one-page view of where the project stands, written from the logs; it keeps no state of its own |
| `scrum/documents/` | Archives of finished Sprints and designs, and files that serve the whole project |

The plugin calls these files logs: the product log is the Product Backlog, the sprint log is the Sprint Backlog. A real example is this repository's own `scrum/` folder, written in Chinese: start with [`ProductBacklog.md`](scrum/ProductBacklog.md) and one archived sprint log, [`sprint-19-board-hook.md`](scrum/documents/sprint/sprint-19-board-hook.md).

## Learn more

- [Quick start](docs/quick-start.md): one page, from installing to your first closed Sprint
- [Glossary](docs/glossary.md): the plugin's own terms
- [`overview.md`](plugins/ideo-scrum/skills/scrum-kernel/overview.md): how the pieces fit, and every departure from the official guides
- [Changelog](CHANGELOG.md): what changed in each release

## License and attribution

The original parts of this repository (the plugin's structure, how its skills are organized, and the work records in `scrum/`) are released under the [MIT license](LICENSE). The methods the plugin carries come from four sources, each under its own terms, which MIT does not cover:

| Source | License |
| --- | --- |
| *The Scrum Guide* 2020, Ken Schwaber and Jeff Sutherland | CC BY-SA 4.0 |
| *Scrum Guide Expansion Pack* 2026.1, Ralph Jocham, John Coleman and Jeff Sutherland | CC BY-SA 4.0 |
| *Design Thinking Bootleg*, Stanford d.school | CC BY-NC-SA 4.0 (non-commercial) |
| *Sprint*, Jake Knapp with John Zeratsky and Braden Kowitz (Simon & Schuster, 2016) | All rights reserved |

The d.school license forbids commercial use, so this repository is not open-source software in the OSI sense. If you plan a commercial use, read [ATTRIBUTION.md](ATTRIBUTION.md) first (it is in Chinese).

From *Sprint* the plugin carries cut-down excerpts of the chapters that describe the method, with no illustrations and not the whole book; if the method helps you, please buy the book. Every excerpt names its source and license, and [ATTRIBUTION.md](ATTRIBUTION.md) lists where each one lives. IDEO-Scrum is an independent work, not affiliated with Scrum.org, scrumexpansion.org, Stanford d.school, IDEO or Simon & Schuster.

## Feedback

Found a problem, or have an idea? Open an [issue](https://github.com/seapawn1/IDEO-Scrum/issues). It helps to say where you run it (Claude Code or Codex, its version, your operating system), what you said, and what you saw.

## Files

| Path | What it is |
| --- | --- |
| `plugins/ideo-scrum/` | The plugin: the four roles in `commands/`, the four kernels in `skills/` (ideo, scrum, sprint, design), and `hooks/` |
| `codex/plugins/ideo-scrum/` | The Codex edition, generated from the plugin by `scripts/sync_codex.py`; do not edit it by hand |
| `docs/` | The quick start and the glossary |
| `scrum/` | This project's own Scrum work, in Chinese: its product log and its archived sprint logs |
| `scripts/` | Scripts that generate and check the Codex edition and the docs |
| `.claude-plugin/`, `.agents/plugins/` | The marketplace lists for Claude Code and Codex |
| `LICENSE`, `ATTRIBUTION.md`, `CHANGELOG.md`, `CLAUDE.md` | The license, the sources and their terms, the release notes, and the instructions for working on this repository |
