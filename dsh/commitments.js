import { closeSync, lstatSync, openSync, readSync, readdirSync } from 'node:fs'
import { dirname, join } from 'node:path'

const HEADER_LIMIT = 128 * 1024

function stat(path) {
  return lstatSync(path, { throwIfNoEntry: false })
}

function projectLogs(cwd) {
  // Stay in the nearest checkout/worktree. Do not follow links to unrelated logs.
  for (let dir = cwd, depth = 0; depth < 64; depth++) {
    const logs = join(dir, 'scrum')
    if (stat(logs)?.isDirectory() && stat(join(logs, 'ProductBacklog.md'))?.isFile()) return logs
    const parent = dirname(dir)
    if (parent === dir || stat(join(dir, '.git'))) break
    dir = parent
  }
}

function headingKind(heading) {
  if (/Sprint Goal|冲刺目标/i.test(heading)) return 'sprintGoal'
  if (/Product Goal|产品目标/i.test(heading)) return 'productGoal'
  if (/Product|产品/i.test(heading)) return 'product'
}

function logCommitments(path) {
  // Only the top of a log is relevant. Ignore a possibly partial last line.
  const fd = openSync(path, 'r')
  const bytes = Buffer.alloc(HEADER_LIMIT)
  let length
  try {
    length = readSync(fd, bytes, 0, bytes.length, 0)
  } finally {
    closeSync(fd)
  }
  const lines = bytes.toString('utf8', 0, length).replace(/^\uFEFF/, '').split(/\r?\n/)
  if (length === HEADER_LIMIT) lines.pop()
  const fields = new Map()
  let kind
  for (const line of lines) {
    if (/^#{1,6}[ \t]/.test(line)) kind = headingKind(line)
    if (!kind || fields.has(kind)) continue
    const match = /^\|[ \t]*(Commitment|承诺)[ \t]*\|[ \t]*(.*?)[ \t]*\|[ \t]*$/.exec(line)
    if (match) fields.set(kind, { key: match[1], text: match[2] })
  }
  return fields
}

function filled(fields, kind) {
  const text = fields.get(kind)?.text
  return text && !/^<.*>$/.test(text) ? text : ''
}

function optional(read) {
  try {
    return read()
  } catch {
    // An unreadable secondary log does not invalidate the product commitments.
    return undefined
  }
}

export function readCommitments(cwd) {
  try {
    const logs = projectLogs(cwd)
    if (!logs) return ''
    const fields = logCommitments(join(logs, 'ProductBacklog.md'))
    const product = filled(fields, 'product')
    const goal = filled(fields, 'productGoal')
    if (!product && !goal) return ''
    const zh = (fields.get('product') ?? fields.get('productGoal')).key === '承诺'
    const colon = zh ? '：' : ': '
    const lines = [zh ? '本项目日志里的承诺（原文）：' : "Commitments from this project's logs (verbatim):"]
    if (product) lines.push(`Product${colon}${product}`)
    if (goal) lines.push(`Product Goal${colon}${goal}`)

    const dirs = optional(() => readdirSync(logs, { withFileTypes: true }))?.filter(entry => entry.isDirectory()) ?? []
    const open = dirs.filter(({ name }) => name.startsWith('sprint-') && optional(() => stat(join(logs, name, 'SprintBacklog.md')))?.isFile())
    if (open.length > 1) {
      lines.push(zh ? `有 ${open.length} 个冲刺开着，见看板` : `${open.length} Sprints are open; see the board`)
    }
    if (open.length === 1) {
      const name = open[0].name
      const text = optional(() => filled(logCommitments(join(logs, name, 'SprintBacklog.md')), 'sprintGoal'))
      if (text) lines.push(zh ? `Sprint Goal（${name}）${colon}${text}` : `Sprint Goal (${name})${colon}${text}`)
    }
    return lines.join('\n')
  } catch {
    // Commitment reminders are optional; unreadable/missing logs must not stop a model turn.
    return ''
  }
}
