import assert from 'node:assert/strict'
import fs, { mkdirSync, mkdtempSync, readFileSync, rmSync, symlinkSync, writeFileSync } from 'node:fs'
import { syncBuiltinESMExports } from 'node:module'
import { tmpdir } from 'node:os'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'
import { test } from 'node:test'
import { apply } from '../dsh/index.js'
import { readCommitments } from '../dsh/commitments.js'

const root = fileURLToPath(new URL('../', import.meta.url))
const plugin = join(root, 'plugins', 'ideo-scrum')
const roles = ['scrum-master', 'developer', 'designer', 'stakeholder']
const kernels = ['ideo-kernel', 'scrum-kernel', 'sprint-kernel', 'design-kernel']

function mount() {
  const skills = new Map()
  const contexts = new Map()
  const register = bucket => entry => {
    assert.ok(!bucket.has(entry.name))
    bucket.set(entry.name, entry)
    return () => bucket.delete(entry.name)
  }
  const effects = []
  apply({
    effect: install => effects.push(install()),
    skills: { register: register(skills) },
    systemPrompt: { context: register(contexts) },
    workingDirectory: { get: session => session.cwd },
  })
  return { skills, contexts, dispose: () => effects.reverse().forEach(dispose => dispose()) }
}

function fixture(t) {
  const dir = mkdtempSync(join(tmpdir(), 'ideo-scrum-dsh-'))
  t.after(() => rmSync(dir, { recursive: true, force: true }))
  return { dir, put: (path, text) => {
    const dest = join(dir, path)
    mkdirSync(dirname(dest), { recursive: true })
    writeFileSync(dest, text)
  } }
}

function canonical(path) {
  const [, description, content] = /^---\r?\n(?:name: [^\r\n]+\r?\n)?description: (.+)\r?\n---\r?\n([\s\S]*)$/.exec(readFileSync(path, 'utf8'))
  return { description: JSON.parse(description), content }
}

test('register the original four role bodies and kernels with resolvable resource bases', () => {
  const { skills, contexts, dispose } = mount()
  assert.deepEqual([...skills.keys()], [...kernels, ...roles])
  for (const [name, entry] of skills) {
    const role = roles.includes(name)
    const expected = canonical(entry.path)
    assert.equal(entry.path, role ? join(plugin, 'commands', `${name}.md`) : join(plugin, 'skills', name, 'SKILL.md'))
    assert.deepEqual(entry.resourceBase, { kind: 'directory', path: dirname(entry.path) })
    assert.equal(entry.description, expected.description)
    assert.equal(entry.content.slice(-expected.content.length), expected.content)
    if (role) {
      assert.deepEqual(entry.invocation, { userInvocable: true, modelInvocable: false })
      const ideo = canonical(join(plugin, 'skills', 'ideo-kernel', 'SKILL.md')).content
      const scrum = canonical(join(plugin, 'skills', 'scrum-kernel', 'SKILL.md')).content
      const i = entry.content.indexOf(ideo)
      const s = entry.content.indexOf(scrum)
      assert.ok(i >= 0 && s > i, `${name} must preload the two verbatim bodies in order`)
      assert.doesNotMatch(entry.content, /Preloaded kernel: (?:sprint|design)-kernel/)
    }
    if (!role && name !== 'design-kernel') assert.equal(entry.content, expected.content)
  }
  const design = skills.get('design-kernel')
  assert.match(readFileSync(join(design.resourceBase.path, '..', 'ideo-kernel', 'IDEO-modes', 'empathize.md'), 'utf8'), /Empathize/i)
  dispose()
  assert.equal(skills.size + contexts.size, 0)
})

test('keep the loaded Sprint Backlog excerpt identical to its SGEP reference', () => {
  const skills = join(plugin, 'skills')
  const refPath = join(skills, 'scrum-kernel', 'references', 'scrum-artifact-sprint-backlog.md')
  const reference = readFileSync(refPath, 'utf8').replaceAll('\r\n', '\n')
  const body = canonical(join(skills, 'sprint-kernel', 'SKILL.md')).content.replaceAll('\r\n', '\n')
  const heading = '\n## Sprint Backlog\n'
  const start = reference.indexOf(heading)
  const inline = body.indexOf(heading)
  assert.ok(start !== -1 && inline !== -1, 'The reference and the skill must both contain the Sprint Backlog section')
  assert.ok(reference.includes('\n### Commitment: Sprint Goal\n', start))
  // The excerpt is the last section in both files. Ignore only different line endings.
  assert.equal(body.slice(inline), reference.slice(start))
  const attribution = reference.match(/^> Source: .+\n> License: .+$/m)?.[0]
  const headerStart = body.lastIndexOf('\n---', inline)
  const excerptHeader = body.slice(headerStart === -1 ? 0 : headerStart, inline)
  assert.ok(attribution && excerptHeader.includes(attribution), 'The inline excerpt must carry its source and license')
  const refLink = excerptHeader.match(/^> Local reference: \[[^\]]+\]\(([^)#\s]+)\)/m)?.[1]
  assert.ok(refLink && join(skills, 'sprint-kernel', refLink) === refPath, 'The inline excerpt must link to its local reference')
  const centralAttribution = readFileSync(join(root, 'ATTRIBUTION.md'), 'utf8')
  assert.match(centralAttribution, /plugins\/ideo-scrum\/skills\/sprint-kernel\/SKILL\.md/)
})

test('bundle, Claude version, existing icon and two locale exports agree', () => {
  const read = path => readFileSync(join(root, path))
  const manifest = JSON.parse(read('package.json'))
  assert.equal(manifest.version, JSON.parse(read('plugins/ideo-scrum/.claude-plugin/plugin.json')).version)
  assert.ok(!manifest.dependencies && !manifest.scripts)
  assert.match(read(manifest.dsh.bundle.patch).toString(), /name: '@seapawn\/ideo-scrum'/)
  assert.equal(read(manifest.exports['./icon']).subarray(0, 8).toString('hex'), '89504e470d0a1a0a')
  for (const language of ['en', 'zh']) {
    const { meta } = JSON.parse(read(manifest.exports['./locale/*.json'].replace('*', language)))
    assert.equal(meta.title, 'IDEO-Scrum')
    assert.ok(roles.every(name => meta.description.includes(`/${name}`)))
  }
})

test('keep verbatim commitments from a bilingual log set and a nested working directory', t => {
  const { dir, put } = fixture(t)
  put('scrum/ProductBacklog.md', '\uFEFF### 1.1 产品\r\n| 承诺 | A  \\|  B |\r\n### 1.2 产品目标\r\n| 承诺 | Keep `{{literal}}`  unchanged. |\r\n')
  put('scrum/sprint-one/SprintBacklog.md', '### 冲刺目标\n| 承诺 | 当前冲刺，不约定截止日。 |\n')
  put('scrum/design-one/DesignBacklog.md', '### 1.2 Design goal\n| Commitment | Check one assumption. |\n')
  put('scrum/documents/design-archived/DesignBacklog.md', '### Design goal\n| Commitment | Do not read this. |\n')
  const text = readCommitments(join(dir, 'scrum', 'sprint-one'))
  assert.equal(text, [
    '本项目日志里的承诺（原文）：', 'Product：A  \\|  B', 'Product Goal：Keep `{{literal}}`  unchanged.',
    'Sprint Goal（sprint-one）：当前冲刺，不约定截止日。', '设计目标（design-one）：Check one assumption.',
  ].join('\n'))
  put('scrum/sprint-another/SprintBacklog.md', '### Sprint Goal\n| Commitment | Different goal. |\n')
  assert.match(readCommitments(dir), /有 2 个冲刺开着，见看板/)
  assert.doesNotMatch(readCommitments(dir), /Different goal|当前冲刺/)
})

test('skip absent logs, empty placeholders, nested Git checkouts and linked log files', t => {
  const { dir, put } = fixture(t)
  assert.equal(readCommitments(dir), '')
  put('scrum/ProductBacklog.md', '# Product\n| Commitment | <Product> |\n')
  assert.equal(readCommitments(dir), '')
  put('scrum/ProductBacklog.md', '# Product\n| Commitment | Visible. |\n')
  put('subproject/.git', 'gitdir: somewhere\n')
  assert.equal(readCommitments(join(dir, 'subproject')), '')
  put('outside/scrum/ProductBacklog.md', '# Product\n| Commitment | Private. |\n')
  symlinkSync(join(dir, 'outside', 'scrum'), join(dir, 'subproject', 'scrum'), process.platform === 'win32' ? 'junction' : 'dir')
  assert.equal(readCommitments(join(dir, 'subproject')), '')
})

test('an unreadable Sprint log does not drop the product or design commitments', t => {
  const { dir, put } = fixture(t)
  const file = join(dir, 'scrum', 'sprint-one', 'SprintBacklog.md')
  put('scrum/ProductBacklog.md', '# Product\n| Commitment | Product stays visible. |\n')
  put('scrum/sprint-one/SprintBacklog.md', '## Sprint Goal\n| Commitment | Sprint text is unavailable. |\n')
  put('scrum/design-one/DesignBacklog.md', '## Design Goal\n| Commitment | Design stays visible. |\n')
  const open = fs.openSync
  const stub = t.mock.method(fs, 'openSync', (path, ...args) => {
    if (path === file) throw Object.assign(new Error('read denied'), { code: 'EACCES' })
    return open(path, ...args)
  })
  syncBuiltinESMExports()
  try {
    const text = readCommitments(dir)
    assert.match(text, /Product: Product stays visible\./)
    assert.match(text, /Design goal \(design-one\): Design stays visible\./)
    assert.doesNotMatch(text, /Sprint text is unavailable/)
    assert.ok(stub.mock.calls.some(call => call.arguments[0] === file))
  } finally {
    stub.mock.restore()
    syncBuiltinESMExports()
  }
})

test('runtime section re-reads current workspace, preserves braces and respects opt-out', t => {
  const { dir, put } = fixture(t)
  const existing = process.env.IDEO_SCRUM_COMMITMENTS
  t.after(() => {
    if (existing === undefined) delete process.env.IDEO_SCRUM_COMMITMENTS
    else process.env.IDEO_SCRUM_COMMITMENTS = existing
  })
  delete process.env.IDEO_SCRUM_COMMITMENTS
  const { contexts } = mount()
  const section = contexts.get('ideo-scrum:commitments')
  assert.equal(section.interpolate, false)
  assert.equal(section.text({}), '')
  const context = { agent: { session: { cwd: dir } } }
  put('scrum/ProductBacklog.md', '# Product Goal\n| Commitment | {{First}}. |\n')
  assert.match(section.text(context), /Product Goal: \{\{First\}\}\./)
  put('scrum/ProductBacklog.md', '# Product Goal\n| Commitment | Second. |\n')
  assert.match(section.text(context), /Product Goal: Second\./)
  process.env.IDEO_SCRUM_COMMITMENTS = 'off'
  assert.equal(section.text(context), '')
})
