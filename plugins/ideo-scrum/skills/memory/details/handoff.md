# Handing a log over

How a Sprint or an IDEO run passes from one session to another, or from one tool to another, without losing anything. Read this file when you pause or end a session in the middle of one, pick one up, or work with a Developer in another session or tool. The list lines that point here are `log-is-the-handoff` and `developer-elsewhere`.

## The log is the handoff (`log-is-the-handoff`)

- The header carries `Now` with the stage the Sprint is in (or the mode and next step of an IDEO log) and the last decision the Product Owner made, followed immediately by `Waiting for PO` with each pending decision's number and short question, separated by semicolons, or `None` (each log's template has the format).
- Update both with the log change that causes them.
- A session that picks up the log reads them first, then checks the recorded permission for the stage and scope; the header is not itself permission to act (`stage-gates`).
- Write no separate handoff documents: before a session ends or its context is shortened, write what matters into the log and update the header.

### At a handoff or a pause

- Commit within the authorized scope only if that commit is permitted; otherwise keep the uncommitted changes and record that status and where to resume.
- This handoff rule does not waive the required pre-Test freeze commit (`tests-criteria-first`) or the closing commit (`one-closing-commit`): if commit permission is not recorded for those gates, ask for it before running the Test or closing.
- Stop at a complete point.

## A Developer in another session or tool (`developer-elsewhere`)

The Developer may work in another session or another tool. The sprint log stays the record in both cases.

- **When the two sessions can talk directly** — another session in the same tool, or a Developer forked from the Scrum Master's session — they talk directly; a long review is written as a file and the message gives its path.
- **When they cannot** — the Developer is in another tool — the sprint log is the only channel. The two keep one working copy and take turns. Whoever holds the turn commits within the authorized scope only if permitted — otherwise keeps the changes uncommitted (as in "At a handoff or a pause") — writes in the notes what was done, and says whose turn is next. What the reviewer finds goes to the Developer as a file the Product Owner passes on, and the Developer copies it into the log; the Product Owner carries only the word that it is the other side's turn.

(These are examples, not rules.)
