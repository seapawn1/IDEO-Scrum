export const meta = {
  name: 's26-draft-long',
  description: 'Sprint 26 rows 6-8, second step: write each long Memory file from the old rules assigned to it; each agent writes one Markdown file outside the repository',
  phases: [
    {
      title: 'Long files',
      detail: '13 agents (one per long file; run in batches of at most 4) - model haiku; run under claude-magpie, which maps it to its own cheap model, so it is magpie cheap model and not Haiku - reason: lowest tier by the standing rule; each agent has the verbatim originals, the annotations and the one-line drafts in front of it; I read every long file against its sources afterwards and fix or rewrite the weak ones myself; a climb is only possible outside magpie',
    },
  ],
}

// Run by scripts/run_workflow.py (claude-magpie -p "/s26-draft-long") in a neutral project folder.
// A workflow script has no file access: every agent writes its own file under OUT; the return value is only a tally.
const ROOT = 'S:/IDEO-Scrum/.claude/worktrees/sprint-26-plugin-memory'
const OUT = 'S:/IDEO-Scrum-Archives/sprint-26-plugin-memory/draft/long'
const BRIEF = ROOT + '/scrum/sprint-26-plugin-memory/review/long-brief.md'

// Set to a list of long file names to re-run only those (empty = all).
const ONLY = []

const FILES = [
  { name: 'roles-and-routing', note: 'The role table of overview rule 8 and the routing of work in rule 14. Sprint 27 is changing both (a new Supporter role, a three-step routing of questions); draft from the current text, I will sync later.' },
  { name: 'stage-gates', note: 'The Product Owner decides between stages: overview rule 12, sprint-log rule 24, and design-log rule 26 with its four-row table of what the log holds and the check at each stage. Put the common rule first, then the Sprint part, then the design part with the table word for word.' },
  { name: 'goal-fixed', note: 'Goal fixed, plan flexible: overview rule 17 with its Scrum Guide quotations word for word (and the Source and License lines), plus what design-log rule 25 and product-log rule 18 add.' },
  { name: 'layers-and-folders', note: 'Overview rules 3 to 6: the three layers table, the folders under scrum/, where files go, and working material.' },
  { name: 'sprint-closing', note: 'Closing a Sprint: sprint-log rules 17 (Review), 18 (Retrospective) and 19 (one closing commit), including the archiving of designs and IDEO logs.' },
  { name: 'sprint-refinement', note: 'Refinement: sprint-log rule 6 (the seven steps) and rule 5, and product-log rules 14 to 16 on refining and where refined content goes.' },
  { name: 'product-log-details', note: 'Two product-log rules whose bodies are tables: rule 2 (writing the product log from a blank page: the six-row table of design log to product log, the IDEO methods alone not being enough, the stakeholder table written first) and rule 10 (the seven item columns and what goes in each, the S, M, L sizes). Keep both tables word for word; put rule 2 first.' },
  { name: 'ideo-ending', note: 'Ideo-log rule 4 without its header-format sentences (the template has them): where an IDEO log lives, that it has no commitment of its own and its For cell points to the log it serves, how conclusions flow back and the PO decides what changes, that the first Review after the work is done archives the log, and what happens to a prototype (built by a Sprint as its specification, kept in the IDEO folder until that Sprint opens, otherwise deleted when the work is done).' },
  { name: 'handoff', note: 'Handing a Sprint over: sprint-log rule 22 (the log is the handoff: the header, a session that picks the Sprint up reads it first and then checks the recorded permission, no separate handoff documents, what to do at a pause about commits, the pre-Test freeze commit and the closing commit still need their permission, stop at a complete point; leave out only the header format the template has) and rule 26 (a Developer in another session or tool: talking directly versus the log as the only channel, taking turns on one working copy; give it without tool names).' },
  { name: 'design-ending', note: 'Design-log rule 19: when a design ends, what is kept, archiving, and the hand-off to the Sprint that builds the conclusions.' },
  { name: 'design-stages', note: 'The stage details of the design log where the annotations say long file or the draft line points here: Empathize (rules 6, 7), Define (rule 8), Ideate (rules 9 to 15: isolated solutions, diverge before converge), Prototype (rule 16), Test (rule 17), and the design-log paragraph The three loops. One section per stage, in order.' },
  { name: 'board-writing', note: 'The board: board-log is also the brief for the cheap model that writes the board page. Keep the field table of the data block (rule 11), the copy and summary rules (12), what the page leaves out (16), and every other data rule whose annotation says long file. The field table must be complete: nothing else in the repository lists the fields.' },
  { name: 'departures', note: 'The Departures table of overview.md (a non-numbered block: see the blocks of overview in review/ledger.json) with the reason of each departure. The README compares its own table to this one word for word, so keep every row word for word, and the Source and License lines of overview.md.' },
]

const SUMMARY = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    lines: { type: 'number' },
    sources: { type: 'array', items: { type: 'string' } },
    open_points: { type: 'number' },
  },
  required: ['file', 'lines', 'sources', 'open_points'],
}

function prompt(f) {
  const file = OUT + '/' + f.name + '.md'
  return [
    'You are a drafter. First read ' + BRIEF + ' in full with the Read tool and follow it. In it, the repository root is ' + ROOT + '.',
    '',
    'Your long file: ' + f.name + '. ' + f.note,
    '',
    'Output file: ' + file + '. Write it once with the Write tool, then Read it back and confirm that it is complete.',
    '',
    'Finish with the structured result: the file path, the number of lines, the ids of the source rules you used, and the number of open points.',
  ].join('\n')
}

phase('Long files')
const jobs = FILES.filter(f => ONLY.length === 0 || ONLY.indexOf(f.name) >= 0)
log(jobs.length + ' long-file agents')
const results = await parallel(
  jobs.map(f => () => agent(prompt(f), { model: 'haiku', label: f.name, phase: 'Long files', schema: SUMMARY })),
)
const done = results.filter(Boolean)
log(done.length + ' of ' + jobs.length + ' agents returned')
return done
