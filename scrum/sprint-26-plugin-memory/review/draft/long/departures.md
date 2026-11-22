# Departures from the official guides

> Source: quotations from The Scrum Guide 2020 (Ken Schwaber & Jeff Sutherland) and the Scrum Guide Expansion Pack v2026.1 (Ralph Jocham, John Coleman, Jeff Sutherland), marked where they appear; the rest is the author's working conventions.
> License: the quotations are CC BY-SA 4.0 (© 2020 Ken Schwaber and Jeff Sutherland; © 2025 Ralph Jocham, John Coleman, and Jeff Sutherland).

Where a rule departs from the official guide on purpose, this table says so and gives the reason. Read it when someone asks why the plugin does not follow the Scrum Guide on a point, or before you change one of these rules. Each departure is stated here once, with its reason; the rule named in the last column points back to this table.

| Here | The official guide | Why | See |
| --- | --- | --- | --- |
| Only the Product Owner must be human | SGEP: the Product Owner and the Scrum Master "must be human", and "At least one Product Developer should be human" | One person works with AI and keeps the value decisions | ‹overview#9› |
| Designs sit beside Sprints | Scrum Guide: all the work "happen within Sprints" | A design delivers no Increment, may span several Sprints, and the Designer and the Developer are peers | ‹overview#2› |
| The Product Owner decides the items with the Scrum Master | Scrum Guide: "the Developers select items from the Product Backlog" | The Product Owner sets the value direction, and the others say how much fits | ‹product-log#12› |
| The How is a plan, and building waits for the go-ahead | Scrum Guide: how to build is "at the sole discretion of the Developers" | The Scrum Master and the Product Owner check the plan, because AI may drift | ‹sprint-log#7›, ‹sprint-log#8› |
| Checkpoints replace the Daily Scrum | Scrum Guide: the Daily Scrum is "a 15-minute event for the Developers" | AI works by session, not by day | ‹sprint-log#10› |
| A reviewer is required | Scrum Guide: the Developers are accountable for "Instilling quality by adhering to a Definition of Done" | A Developer may drift, and a second look catches it | ‹sprint-log#14› |
| No Sprint end date | Scrum Guide: Sprints are "fixed length events of one month or less" | AI works by session, so the Product Owner watches at checkpoints for a Sprint that drags on | ‹sprint-log#2› |

## Open points for the Product Owner

- The README's "How it differs" table repeats the Here and Why columns of this table word for word, and the docs check (`scripts/check_docs.py`) compares the two; when this file replaces `overview.md`, the README link and the check follow it (a migration task, listed in the reference inventory).
- The last column used to name a convention number; it now names the line (handle) that carries the rule.
