# Closing a Sprint

Read this file when you close a Sprint: the Review, the Retrospective and the closing commit. The list lines that point here are `review-at-close`, `fresh-at-review`, `retro-in-memory` and `one-closing-commit`. The text is the old rules word for word, cut into bullets; the old pointers to convention numbers became handles.

## Review (`review-at-close`)

- Close with a Review: compress the sprint log to its key decisions, rename it `sprint-NN-<suffix>.md`, and move it into `scrum/documents/` or the project’s existing archive subfolder there.
- **Ended designs.** An ended design is archived by the first Review that can read its complete log and all original material in its own checkout. Without that complete set, leave the design pending archival and do not move its log or material from another worktree. Archive its log as `design-<suffix>.md` and keep its original material together in a folder beside it, out of the active design path. Preserve the decision trail and verify that the archive is readable before updating references in this checkout.
- **A Sprint working elsewhere that builds on the design.** Hand off the old and new paths to any receiving Sprint; that Sprint first checks that the originals are readable at the new path in its own checkout, then updates its references there. While building, keep a readable old reference until the new one is available in that checkout. When the design is already archived on the target base (`main`), in this checkout, or in an integration branch ready alongside this Sprint, before the receiving Sprint closes check its actual material references — including those in its log being archived — and the originals against that combined target state, and update broken links before closing; an old link that works only in the current worktree is not sufficient.
- If the receiving Sprint closes while the design is still pending archival everywhere, keep the usable active reference, note the pending archival, and merge to `main`; the later archiving Review searches the whole project before its closing commit (`one-closing-commit`, step 1) so those archived Sprint references are updated too, and reports any unmerged branches still holding stale active paths to the Scrum Master.
- Leave verbatim historical commitment snapshots unchanged. Report stale active paths on other branches to the Scrum Master, rather than changing those branches.
- Archive ended IDEO logs as `ideo-<suffix>.md`, handling their prototypes as `ideo-log-ends` says.
- Clean up ordinary working files in `scrum/`, including outdated ones in `scrum/documents/`; check that this does not remove design originals or break links to them, even when the receiving Sprint closes.
- Write the Stakeholders’ views and any changes to the product log or Product Goal into the product log and refresh it (`fresh-at-review`). For an outside view, the Product Owner or the Scrum Master — never the builder — summons Stakeholders from the product log’s table.

## Fresh at every Review (`fresh-at-review`)

- At every Review, move done items to section 3.2 of the product log, one line each, with the source, usually the archived sprint log in `scrum/documents/`; send unfinished items back to section 3.1.
- Delete outdated architecture text and resolved open points; what counts as outdated is set out in *Review* above.
- Keep no revision record; version control keeps the history.
- Fresh means more than the items: the Review keeps the rest of `scrum/` fresh too (*Review* above).

## Retrospective (`retro-in-memory`)

- Hold it as an action at close, with no chapter in the log.
- The Developer saves only the important, reusable lessons, one independently findable entry per lesson, in the project’s memory. Write enough to use each principle on its own: what broke or worked, why, and what to do next time.
- If the tool has no project memory, use the repository notes the project keeps for lessons, still one separately findable entry per lesson.
- Do not write a Sprint Retro summary, put lessons in `CLAUDE.md` or `AGENTS.md` or any other instructions file, or mix them with the plugin’s conventions. An index may point to the entries, not copy their text.
- If there is no important lesson, write no entry. Discard the rest: one-off session details, passing friction, and notes without a demonstrated reusable reason are not lessons; do not infer a cause to turn every remark into a principle.
- An especially good improvement goes into the Definition of Done with the Product Owner’s consent.
- Check whether the product log is still fresh.
- *Supplement:* ask where the Product Owner held up the AI — waiting for a decision, waiting for a go-ahead.

## One closing commit (`one-closing-commit`)

Close in this order:

1. Before the closing commit, search the whole project for old paths until none remain; the fixes go into that same commit.
2. Make one closing commit with the changes Review and Retro actually made inside the repository. If project memory is outside it, or there is no important lesson, do not copy outside memory or create a Retro file to make the commit appear to contain both.
3. Tag it with the Sprint folder's name; the tag's message says what the Sprint achieved.
4. Merge into the main branch.
5. Close the working copy.
6. Delete the branch of the same name.

Judge the project's health by `scrum/` alone: it holds all of the Scrum work (`scrum-folders`); elsewhere, usually only the README needs updating. Pushing and other outward actions need the Product Owner's consent (`outward-needs-po`).

## Open points for the Product Owner

- The *Supplement* sentence about asking where the PO held up the AI was inferred by the assistant and never confirmed; kept here with its label so the PO decides.
