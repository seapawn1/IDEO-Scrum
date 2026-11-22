# When a design ends

Read this file when you end a design, decide what happens to its material, or hand its conclusions to a Sprint. The list lines that point here are `design-ends` and `design-conclusions`. The text is the old rule word for word, cut into bullets.

## Ending

- End the design when the Product Owner decides its questions are answered, or stops it (`ask-the-po`, `ideate-arrangement`).
- A design has no Review or Retro of its own.

## Conclusions

- Write the conclusions into the product log as `blank-page` says, and pass them to the Sprint that asked.
- For a blank page, pick the target (`design-kernel/steps/2-3-pick-a-target.md`), split it into items, and let the Product Owner order them.
- Next to the ending decision, leave a line or two on what the design taught about how to work, as input to the Retrospective of the Sprint that archives it, not as the Retro record itself.

## The material

- Mark the design concluded and awaiting archival in its existing `Now` line.
- Keep the log and all original design working material together until archival: prototypes, sketches and rejected options, demos, reviews, synthesis, and other material used in the design.
- From the relevant chapter, link to the originals or the folder that holds them; a summary or a commit ID alone is not enough.
- If a Sprint builds the conclusions, link from that Sprint to the prototype as a specification; do not leave its only copy in a Sprint working folder.
- Keep the material whether or not a Sprint will build the conclusions. It is design evidence, never an Increment.

## The branch

When the Product Owner explicitly permits the commit, merge, and branch cleanup, handle the branch as `one-closing-commit`, `outward-needs-po` says: merge into its base (`design-branch`), then delete it; pushing and other outward actions require the Product Owner's explicit consent.

## Archiving

- After it ends, the first Sprint Review that can read its complete log and all original material in its own checkout archives them (`review-at-close`).
- A Review without that complete set leaves the design pending archival; it does not move material from another worktree.

## Handing off to a Sprint working elsewhere

The hand-off of changed paths to a receiving Sprint, the check of its material references before it closes, and what to do when it closes while the design is still pending archival are in `details/closing.md` (Review): the two old rules said the same thing, and the Review's text is kept there once. Do not close with broken material links or rewrite verbatim historical commitment snapshots.

## Open points for the Product Owner

- The old design rule and the Review rule both described how a receiving Sprint takes over changed paths; the text is kept once, in `details/closing.md`, and this file points there.
