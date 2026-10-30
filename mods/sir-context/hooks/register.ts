import type { EngineInterface, Register } from 'claude-code'

const ROOT = 'D:/Projects'
const SIR = `${ROOT}/_SIR`
const RULES =
  'Rules from Ahmed: no pull requests (push straight to main); never delete legacy/ (it is the source code to port from); use the computer, browser and apps yourself for any task and work out how (plans/COMPUTER_USE.md); AHome and Habiba data never leave AHome; HQ prepares, project chats build.'

async function text($: EngineInterface, path: string): Promise<string> {
  try {
    return String(await $.fs.read(path))
  } catch {
    return ''
  }
}

const field = (yml: string, key: string) => yml.match(new RegExp(`^${key}:[ ]*(.+)$`, 'm'))?.[1]?.trim() ?? ''

async function digest($: EngineInterface): Promise<string> {
  const cwd = (await $.session.cwd()).split(String.fromCharCode(92)).join('/')
  const hit = cwd.startsWith(`${ROOT}/`) ? cwd.slice(ROOT.length + 1).split('/')[0] : ''
  const base = [`SIR main plan: ${SIR}/plans/MAIN_PLAN.md. Studied order: ${SIR}/plans/WAVE_STUDY.md. Dashboard mods: ${SIR}/mods (any chat may improve them or add a pane for its project).`]
  const yml = hit && hit !== '_SIR' ? await text($, `${ROOT}/${hit}/.sir/project.yml`) : ''
  if (!yml) return [...base, 'This chat is the HQ manager: it prepares plans, kits, repos and tools and does not build products.', RULES].join('\n')
  const id = field(yml, 'id')
  let wave = '?'
  try {
    wave = String((JSON.parse(await text($, `${SIR}/plans/waves.json`)) as Record<string, number>)[id] ?? '?')
  } catch {
    wave = '?'
  }
  const tasks = (await text($, `${ROOT}/${hit}/.sir/TASKS.md`)).split('\n').filter(l => /^- \[[ x]\] T-\d+/.test(l))
  const next = tasks.find(l => l.startsWith('- [ ]'))?.replace(/^- \[ \] (T-\d+) \| owner: [^|]+\| (\(kit\) )?/, '$1 ').slice(0, 140) ?? 'none'
  const unread = (await text($, `${SIR}/ops/bus/${id}.md`)).split('\n').filter(l => l.startsWith('- [ ]')).length
  return [
    ...base,
    `This chat builds ${field(yml, 'name')} (wave ${wave}, ${tasks.filter(l => l.startsWith('- [x]')).length}/${tasks.length} tasks). Next task: ${next}.`,
    `Messages from other projects: ${unread} unread in ${SIR}/ops/bus/${id}.md. Write to another project in ${SIR}/ops/bus/<slug>.md; talk live with ListAgents and SendMessage.`,
    'Start with the first task: a deep scan of legacy/ and the plan, then improve the plan.',
    RULES,
  ].join('\n')
}

export const register: Register = on => {
  on('prompt.compose', async ($, e, next) => {
    const out = await next(e)

    return { sections: [...out.sections, { id: 'sir:context', text: await digest($), scope: 'session' }] }
  })
}
