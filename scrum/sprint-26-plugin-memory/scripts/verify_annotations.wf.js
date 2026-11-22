export const meta = {
  name: 's26-verify-annotations',
  description: 'Sprint 26 row 2: two read-only lenses (facts, loss) check the 111 rule annotations chunk by chunk; each agent writes one JSON file outside the repository',
  phases: [
    {
      title: 'Verify',
      detail: '26 agents (13 chunks x 2 lenses: facts, loss) - model haiku; run under claude-magpie, which maps it to its own cheap model, so it is magpie cheap model and not Haiku - reason: lowest tier by the standing rule; the first-pass annotations came from the same tier and a spot check found factual errors, so this is a second look with the originals and the brief, not a re-draft; results are spot-checked, and a climb is only possible outside magpie',
    },
  ],
}

// Run by scripts/run_workflow.py (claude-magpie -p "/s26-verify-annotations") in a neutral project folder.
// A workflow script has no file access: every agent writes its own JSON file under OUT; the return value is only a tally.
const ROOT = 'S:/IDEO-Scrum/.claude/worktrees/sprint-26-plugin-memory'
const OUT = 'S:/IDEO-Scrum-Archives/sprint-26-plugin-memory/verify'
const BRIEF = ROOT + '/scrum/sprint-26-plugin-memory/review/verify-brief.md'

// Set to a list of "<chunk key>.<lens key>" to re-run only those (empty = all).
const ONLY = []

const CHUNKS = [
  { key: 'overview-1-9', ids: 'overview#1-9', n: 9, note: '' },
  { key: 'overview-10-17', ids: 'overview#10-17', n: 8, note: '' },
  { key: 'product-log-1-9', ids: 'product-log#1-9', n: 9, note: 'Rule product-log#1 and rule overview#1 are annotated as merging into each other: check whether that is a cycle.' },
  { key: 'product-log-10-18', ids: 'product-log#10-18', n: 9, note: '' },
  { key: 'ideo-log-1-4', ids: 'ideo-log#1-4', n: 4, note: '' },
  {
    key: 'board-log-1-10',
    ids: 'board-log#1-10',
    n: 10,
    note: 'board-log says of itself that it is also the brief for whoever writes the board page. The annotator recommends deleting many of these rules because the template (plugins/ideo-scrum/skills/scrum-kernel/conventions/scrum-board-template.html) and the check script (scripts/board_check/check.py) already cover them. Open both and decide whether a person who reads only those two could really write the page; if not, the deletion loses a rule.',
  },
  {
    key: 'board-log-11-19',
    ids: 'board-log#11-19',
    n: 9,
    note: 'board-log says of itself that it is also the brief for whoever writes the board page. The annotator recommends deleting many of these rules because the template (plugins/ideo-scrum/skills/scrum-kernel/conventions/scrum-board-template.html) and the check script (scripts/board_check/check.py) already cover them. Open both and decide whether a person who reads only those two could really write the page; if not, the deletion loses a rule. Rule 11 is the field table of the data block: check carefully where else the fields are listed.',
  },
  { key: 'sprint-log-1-9', ids: 'sprint-log#1-9', n: 9, note: '' },
  { key: 'sprint-log-10-18', ids: 'sprint-log#10-18', n: 9, note: '' },
  { key: 'sprint-log-19-26', ids: 'sprint-log#19-26', n: 8, note: 'Rules 20, 24 and 25 are annotated as merging into overview rules: open those and check that they really say the same thing.' },
  { key: 'design-log-1-9', ids: 'design-log#1-9', n: 9, note: '' },
  { key: 'design-log-10-18', ids: 'design-log#10-18', n: 9, note: '' },
  { key: 'design-log-19-27', ids: 'design-log#19-27', n: 9, note: 'Rule 25 is annotated as merging into overview#17: open it and check that it really says the same thing.' },
]

const LENSES = [
  {
    key: 'facts',
    title: 'facts',
    text: 'This round you look at check 1 (are the facts in the reason right) and check 3 (is the source label right). Checks 2 and 4 are done by someone else; skip them.',
  },
  {
    key: 'loss',
    title: 'loss',
    text: 'This round you look at check 2 (does the recommendation lose a behavioural requirement) and check 4 (are kind and home reasonable), plus: does the rule it merges into really say the same thing, is there any merge cycle, and where a reason says that the same content already exists elsewhere, open that place and write down the file and the position. Checks 1 and 3 are done by someone else; skip them.',
  },
]

const SUMMARY = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    n: { type: 'number' },
    ok: { type: 'number' },
    fix: { type: 'number' },
    doubt: { type: 'number' },
  },
  required: ['file', 'n', 'ok', 'fix', 'doubt'],
}

function prompt(c, l) {
  const file = OUT + '/' + c.key + '.' + l.key + '.json'
  return [
    'You are a verifier (lens: ' + l.title + '). First read ' + BRIEF + ' in full with the Read tool and follow it. In it, the repository root is ' + ROOT + '.',
    '',
    'Rules to verify: ' + c.ids + ' (' + c.n + ' rules). ' + c.note,
    '',
    l.text,
    '',
    'Output file: ' + file + '. Write it once with the Write tool: a JSON array with one object per rule (id, verdict, issues, fix), in id order. After writing, Read it back and confirm that it is valid JSON and that the number of objects is ' + c.n + '.',
    '',
    'Finish with the structured result: the file path, n, and how many rules got ok, fix and doubt. Write the issues and fix text inside the file in Chinese, as the brief says.',
  ].join('\n')
}

phase('Verify')
const jobs = []
for (const c of CHUNKS) {
  for (const l of LENSES) {
    if (ONLY.length === 0 || ONLY.indexOf(c.key + '.' + l.key) >= 0) jobs.push({ c, l })
  }
}
log(jobs.length + ' verifier agents')
const results = await parallel(
  jobs.map(j => () => agent(prompt(j.c, j.l), { model: 'haiku', label: j.c.key + '/' + j.l.key, phase: 'Verify', schema: SUMMARY })),
)
const done = results.filter(Boolean)
log(done.length + ' of ' + jobs.length + ' agents returned')
return done
