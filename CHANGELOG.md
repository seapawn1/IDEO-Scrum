# Changelog

What changed in each release of IDEO-Scrum, newest first. Every release is a git tag named `vX.Y.Z`; the 1.x line is the tag `v1`. To upgrade, see the [README](README.md).

## [Unreleased]

- **Distribution**: added DeepSeek Harness (DSH) alongside Claude Code and retired the Codex distribution.
- **Version**: the Claude Code plugin and DSH bundle both use `0.6.3`. This is the IDEO-Scrum version, not a change to the DSH host version.
- **Supporter**: a fifth role, `/ideo-scrum:supporter` (DSH: `/supporter`), for the chores that touch no source: the board, summaries, relaying what is already decided, explaining how the plugin works. It is also the Product Owner's contact point: it gathers what waits for the Product Owner into one list, sends back what is not theirs, and carries their answers back word for word; what it relays marked as the Product Owner's own words, with the date, counts as theirs. It decides nothing, ranks nothing and reviews nothing, and anything that needs the Product Owner in person (tool permissions and settings, `CLAUDE.md` or `AGENTS.md`, a push or a release) is not covered. The role is the Scrum Guide Expansion Pack's Supporter (a Stakeholder type), taking only its "doing what is requested" side.
- **Who gets which question**: `overview.md`, convention 14, now says it in three steps: a role decides what it can itself; process questions and anything inside a written handover go to the Scrum Master; what only the Product Owner can decide goes to the Supporter, who puts it to them in one go. The role entries point to it instead of each saying it again.
- **Stakeholder and Scrum Master entries**: the `stakeholder` entry now gives only an outside view (it used to double as a standing "PO assistant"); the `scrum-master` entry says the Master guards the process, reviews, and decides for the Product Owner within a written handover, and hands the chores to the Supporter.
- **Where the templates and the board live**: the four log templates are now in `template/` and the board's files (`board-log.md`, `scrum-board-template.html`) in `board/`, both at the plugin root; skills point to them as `../../template/…` and `../../board/…`, and the DSH package lists the two folders. If you have scripts or notes that point at the old places, inside each kernel's `conventions/` folder, update them.
- **Board**: the board checker now recognizes a Sprint or design that has ended and awaits archiving (`收官 · …` without the 已, or `Test: Concluded — awaiting archive`), so an IDEO log is no longer shown under a host that has ended; one stage of work ending is still not the host ending. The board conventions say `solution: null` means no `story` either, and the IDEO log template's `For` field names a Sprint log or a design log as well as the product log.
- **Attribution**: each of the five IDEO mode files and `ATTRIBUTION.md` now name both sources of their text: the 2010 *Design Process Mini-Guide* (CC BY-NC-SA 3.0 Unported, via the d.school's archived wiki) as the base, and the 2018 *Design Thinking Bootleg* (CC BY-NC-SA 4.0) for the added passages. The excerpts themselves are unchanged.
- **Project agents and second opinions**: the `second-opinion` entry takes a `model:` argument and says what happens when Fable is not available; the project-stakeholder entry has an `argument-hint`, says what to do when a role card has no "when to summon" cell, and mentions the host's own permission prompt for `.claude/`; the quick start links to the guide.

## [6.0.3] — 2026-11-14

Sprint 20 ("presentable"): getting the plugin ready for people who did not build it.

- **Board**: redesigned. `scrum/ScrumBoard.html` (it was `Board.html`) is now one fixed page that draws itself from a block of data the AI writes from your logs: a flow diagram of the product, the items not done, and the Sprints and designs they flow into, with a card for each. It reads on a wide screen, a portrait screen and a phone, follows the system's light or dark setting, and needs no network. A check script, `scripts/board_check/check.py`, compares the data with the logs. **Renamed:** `conventions/board.md` is now `board-log.md`, and `board-template.html` is now `scrum-board-template.html`.
- **Conventions, seven small fixes**: a prototype follows its conclusions into the Sprint that builds them, as that Sprint's specification; at a gate the AI reads the commitment and writes it into the log instead of reading it out to you; a design's Empathize and Define are settled by you with the Scrum Master session, and the Designer takes over at Ideate; a design's map draws the experience you want, not today's; a test uses only the role cards that matter; Lightning Demos and subagent sketches are optional; the Retrospective writes its lessons into the project's memory, never an instructions file.
- **Docs**: a README in English and Chinese, a one-page quick start in both, a glossary of the plugin's own terms, and a `Board and hook` section.
- **Release packaging**: this changelog; upgrade, license and feedback notes in the README; a plugin icon.
- **Test**: a simulated first-time user walks the plugin from install to the first Sprint close; the scripts are in `scripts/stranger_test/`.

## Earlier releases

- **6.0.2** (2026-11-14): log headers unified (`Now`, `Waiting for PO`); the scrum, sprint and design kernels load only when summoned; the Scrum Master acts within a written handover; the first version of the board, a one-page view of where the project stands; a hook that puts the product, the Product Goal and the open Sprint Goal into the context. There is no 6.0.1: the work of two Sprints shipped together as 6.0.2.
- **6.0.0** (2026-11-13): four kernels with on-demand loading (a new sprint-kernel; the design steps in `steps/`; ideo-kernel gains the IDEO log and the boundary between a design sprint and the five modes); conventions straightened: a `Now` line in the sprint log, what "stuck" and "stale" mean, eight points in the design conventions, how a Developer working in another tool collaborates; "the IDEO five-stage method" is named as the five modes.
- **5.2.0** (2026-11-10): conventions tuned: each opens with one diagram and every rule is written once; the sprint log and the design log have five chapters; a design does not run Review and Retro; the Product Owner decides between stages; a blank-page entry for new projects; IDEO methods are used in every design stage. The first release that carries the Codex package (`codex/plugins/ideo-scrum/`), generated from the Claude Code plugin and numbered with it.
- **5.1.2** (2026-11-09): `overview.md` moves next to scrum-kernel's `SKILL.md`.
- **5.1.1** (2026-11-09): conventions revised after the Product Owner's review.
- **5.1.0** (2026-11-08): the whole process ships in the plugin: scrum-kernel gains `conventions/` (overview, product log and sprint log conventions and templates); design-kernel gains "open a design" and "pick one up"; the four role commands follow the conventions.
- **5.0.1** (2026-11-08): the design log template corrected.
- **5.0.0** (2026-11-08): design-kernel is split out again and now covers the design sprint only; the five modes and the method library stay in ideo-kernel. The name `design-kernel` comes back with a new meaning.
- **4.0.0** (2026-10-25): ideo-kernel renamed, and its two "five steps" told apart (the IDEO five modes, the design sprint's five stages); roles redefined (only the Product Owner must be human; the stakeholder is one command with several identities); role commands load the kernels automatically; ideo-kernel triggers more reliably; the plugin is written in English throughout. **Breaking:** the skill `ideo-scrum:design-kernel` is now `ideo-scrum:ideo-kernel`.
- **3.2.0** (2026-10-13): the stakeholder becomes an outside view; the three role descriptions gain a boundary sentence.
- **3.1.0** (2026-10-04): a fourth command, `stakeholder`; the Scrum Master and Developer commands rebuilt from the text of the Scrum Guide 2020; the Scrum Guide Expansion Pack's roles chapter restored in full as an asset.
- **3.0.0** (2026-09-23): the three roles change from output styles to commands, so a role is injected into the conversation you choose.
- **2.0.1** (2026-09-08): the Scrum Master role drops its coding instructions; the role definitions are written in English.
- **2.0.0** (2026-08-31): role descriptions rewritten as "use when…" triggers; every method file carries its own Source and License header.
- **1.0.2** (2026-08-30, tag `v1`): the close of the 1.x line (Sprints 01 to 05): the design kernel rebuilt on the IDEO five modes, and the Scrum kernel's agents replaced by excerpts from the Scrum Guide Expansion Pack.

The Codex edition lived on a separate `codex` branch until Sprint 13 (last released as 3.2.0, tag `codex-v3.2.0`). From 5.2.0 until its retirement, it was generated from `main`.
