import { readFileSync } from 'node:fs'
import { basename, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'
import { readCommitments } from './commitments.js'

export const name = 'ideo-scrum'
export const inject = ['skills', 'systemPrompt', 'workingDirectory']

const plugin = new URL('../plugins/ideo-scrum/', import.meta.url)
const kernels = ['ideo-kernel', 'scrum-kernel', 'sprint-kernel', 'design-kernel', 'memory']
const roles = ['scrum-master', 'developer', 'designer', 'stakeholder', 'supporter']
const toolMapping = 'DSH host adapter: Use `skill` with `{"name":"<skill-name>"}` for Skill calls. Drop the `ideo-scrum:` prefix from the name. Resolve resources relative to the base directory of the skill that references them.'
const roleRouting = 'The IDEO and Scrum kernels and the Memory are already loaded below, in that order; do not call `skill` again for those. Load `sprint-kernel` for Scrum Sprint work and `design-kernel` for design sprint work, unless their instructions are already in the conversation. When the work needs both, wait for `sprint-kernel` before loading `design-kernel`. Use `read` with an absolute file path based on the kernel that named the resource, not a search of the project.'

function readEntry(url, skillName) {
  const path = fileURLToPath(url)
  const text = readFileSync(path, 'utf8')
  const match = /^(?:\uFEFF)?---\r?\n(.*?)\r?\n---[ \t]*\r?\n/s.exec(text)
  // The shared headers use one double-quoted, JSON-compatible description line.
  const description = match?.[1].match(/^description:[ \t]*("[^\r\n]*")[ \t]*\r?$/m)
  if (!description) throw new Error(`Expected a quoted description in ${path}`)
  const declaredName = match[1].match(/^name:[ \t]*([a-z-]+)[ \t]*\r?$/m)?.[1]
  if (basename(path) === 'SKILL.md' && declaredName !== skillName) {
    throw new Error(`Expected skill ${skillName} in ${path}`)
  }
  return {
    name: skillName,
    description: JSON.parse(description[1]),
    path,
    resourceBase: { kind: 'directory', path: dirname(path) },
    source: 'runtime',
    content: text.slice(match[0].length),
  }
}

function rolePrelude(entries) {
  return ['ideo-kernel', 'scrum-kernel', 'memory'].map(name => entries.find(entry => entry.name === name)).map(entry => [
    `Preloaded kernel: ${entry.name}`,
    `Base directory: ${entry.resourceBase.path.replaceAll('\\', '/')}`,
    entry.content,
  ].join('\n')).join('\n\n---\n\n')
}

export function apply(ctx) {
  const entries = kernels.map(kernel => readEntry(new URL(`skills/${kernel}/SKILL.md`, plugin), kernel))
  for (const entry of entries) {
    // The canonical design entry also contains a namespaced tool call.
    if (entry.name === 'design-kernel') entry.content = `${toolMapping}\n${entry.content}`
    ctx.effect(() => ctx.skills.register(entry))
  }
  const prelude = rolePrelude(entries)
  for (const role of roles) {
    const entry = readEntry(new URL(`commands/${role}.md`, plugin), role)
    ctx.effect(() => ctx.skills.register({
      ...entry,
      invocation: { userInvocable: true, modelInvocable: false },
      content: `${toolMapping}\n${roleRouting}\n\n${prelude}\n\n---\n\nRole instructions:\n${entry.content}`,
    }))
  }
  // DSH owns admission, deduplication and replay of named runtime snapshots.
  ctx.effect(() => ctx.systemPrompt.context({
    name: 'ideo-scrum:commitments',
    order: 130,
    interpolate: false,
    text: ({ agent }) => {
      if (!agent || process.env.IDEO_SCRUM_COMMITMENTS === 'off') return ''
      return readCommitments(ctx.workingDirectory.get(agent.session))
    },
  }))
  // DSH replays a named runtime context every turn, also after a compaction has replaced the role text with a summary;
  // the hint to call `memory` again lives here and not in the role routing, which the summary would swallow.
  ctx.effect(() => ctx.systemPrompt.context({
    name: 'ideo-scrum:memory',
    order: 120,
    interpolate: false,
    text: ({ agent }) => agent
      ? 'ideo-scrum Memory: if you are working as an ideo-scrum role and the text of the `memory` skill is no longer in this conversation, for example because the conversation was compacted, call the `skill` tool with `{"name":"memory"}` before going on.'
      : '',
  }))
}
