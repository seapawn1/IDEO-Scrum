export const meta = {
  name: 's26-draft-rules',
  description: 'Sprint 26 rows 6-8: draft the one-line Memory entry for each of the 111 old rules, chunk by chunk; each agent writes one JSON file outside the repository',
  phases: [
    {
      title: 'Draft',
      detail: '13 agents (one per chunk of at most 10 rules) - model haiku; run under claude-magpie, which maps it to its own cheap model, so it is magpie cheap model and not Haiku - reason: lowest tier by the standing rule; the task is a constrained rewrite with a brief, annotations and the verbatim originals in front of the agent; I review every drafted line afterwards and fix or redo the weak ones; a climb is only possible outside magpie',
    },
  ],
}

// Run by scripts/run_workflow.py (claude-magpie -p "/s26-draft-rules") in a neutral project folder.
// A workflow script has no file access: every agent writes its own JSON file under OUT; the return value is only a tally.
const ROOT = 'S:/IDEO-Scrum/.claude/worktrees/sprint-26-plugin-memory'
const OUT = 'S:/IDEO-Scrum-Archives/sprint-26-plugin-memory/draft'
const BRIEF = ROOT + '/scrum/sprint-26-plugin-memory/review/draft-brief.md'

// Set to a list of chunk keys to re-run only those (empty = all).
const ONLY = []

const CHUNKS = [
  { key: 'overview-1-9', ids: 'overview#1-9', n: 9, note: 'Rule overview#8 (Roles) is long; its table goes to long/roles-and-routing.md and the list gets one index line.' },
  { key: 'overview-10-17', ids: 'overview#10-17', n: 8, note: 'Rules 10, 12 and 14 will change when Sprint 27 merges; draft them from the current text anyway, I will sync them later. Rule 17 carries Scrum Guide quotations: they stay out of the line and go to long/goal-fixed.md word for word.' },
  { key: 'product-log-1-9', ids: 'product-log#1-9', n: 9, note: '' },
  { key: 'product-log-10-18', ids: 'product-log#10-18', n: 9, note: '' },
  { key: 'ideo-log-1-4', ids: 'ideo-log#1-4', n: 4, note: '' },
  { key: 'board-log-1-10', ids: 'board-log#1-10', n: 10, note: 'board-log is also the brief for the cheap model that writes the board page; the field table and data rules are not to be lost: where the annotation says home long-file, they go to long/board-writing.md and the list gets an index line.' },
  { key: 'board-log-11-19', ids: 'board-log#11-19', n: 9, note: 'board-log is also the brief for the cheap model that writes the board page; the field table and data rules are not to be lost: where the annotation says home long-file, they go to long/board-writing.md and the list gets an index line.' },
  { key: 'sprint-log-1-9', ids: 'sprint-log#1-9', n: 9, note: '' },
  { key: 'sprint-log-10-18', ids: 'sprint-log#10-18', n: 9, note: '' },
  { key: 'sprint-log-19-26', ids: 'sprint-log#19-26', n: 8, note: 'Rules 20, 24 and 25 merge into overview rules: write null for the line and put what is unique in adds_to_target.' },
  { key: 'design-log-1-9', ids: 'design-log#1-9', n: 9, note: '' },
  { key: 'design-log-10-18', ids: 'design-log#10-18', n: 9, note: '' },
  { key: 'design-log-19-27', ids: 'design-log#19-27', n: 9, note: 'Rules 19 and 26 are very long; their detail goes to long files and the list gets one index line each.' },
]

const SUMMARY = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    n: { type: 'number' },
    lines: { type: 'number' },
    merged: { type: 'number' },
    deleted: { type: 'number' },
    long_index: { type: 'number' },
  },
  required: ['file', 'n', 'lines', 'merged', 'deleted', 'long_index'],
}

function prompt(c) {
  const file = OUT + '/' + c.key + '.json'
  return [
    'You are a drafter. First read ' + BRIEF + ' in full with the Read tool and follow it. In it, the repository root is ' + ROOT + '.',
    '',
    'Rules to draft: ' + c.ids + ' (' + c.n + ' rules). ' + c.note,
    '',
    'Output file: ' + file + '. Write it once with the Write tool: a JSON array with one object per rule, in id order, in the format the brief gives. After writing, Read it back and confirm that it is valid JSON and that the number of objects is ' + c.n + '.',
    '',
    'Write the Memory lines in English; write note and where_else in Chinese. Finish with the structured result: the file path, n, how many rules got a line (count each element of lines too), how many are merged, how many deleted, and how many lines are long-file index lines.',
  ].join('\n')
}

phase('Draft')
const jobs = CHUNKS.filter(c => ONLY.length === 0 || ONLY.indexOf(c.key) >= 0)
log(jobs.length + ' drafter agents')
const results = await parallel(
  jobs.map(c => () => agent(prompt(c), { model: 'haiku', label: c.key, phase: 'Draft', schema: SUMMARY })),
)
const done = results.filter(Boolean)
log(done.length + ' of ' + jobs.length + ' agents returned')
return done
