import type { EngineInterface, Register } from 'claude-code'

const ROOT = 'D:/Projects'
const SIR = `${ROOT}/_SIR`
const RULES =
  'Rules from Ahmed: no pull requests (push straight to main); never delete legacy/ (it is the source code to port from); never stop at "I cannot": try another way, use the computer, browser and apps yourself (plans/COMPUTER_USE.md, plans/WORKFORCE.md); premium quality from every model (plans/WEAK_MODEL_PLAYBOOK.md); AHome and Habiba data never leave AHome; HQ manages and reviews, project chats build and report to ops/bus/sir-hq.md.'

async function text($: EngineInterface, path: string): Promise<string> {
  try {
    return String(await $.fs.read(path))
  } catch {
    return ''
  }
}

const field = (yml: string, key: string) => yml.match(new RegExp(`^${key}:[ ]*(.+)$`, 'm'))?.[1]?.trim() ?? ''

async function dashboardUrl($: EngineInterface): Promise<string> {
  return (await text($, `${SIR}/ops/DASHBOARD_URL.txt`)).trim() || 'not published yet'
}

async function digest($: EngineInterface): Promise<string> {
  const cwd = (await $.session.cwd()).split(String.fromCharCode(92)).join('/')
  const hit = cwd.startsWith(`${ROOT}/`) ? cwd.slice(ROOT.length + 1).split('/')[0] : ''
  const base = [
    `SIR main plan: ${SIR}/plans/MAIN_PLAN.md. Build order: ${SIR}/plans/WAVE_STUDY.md. Lifecycle and reviews: ${SIR}/plans/HQ_PROTOCOL.md. Start prompt: ${SIR}/plans/START_PROMPT.md.`,
    `Ahmed's dashboard page (SIR Control Room): ${await dashboardUrl($)}. Mods live in ${SIR}/mods.`,
  ]
  const yml = hit && hit !== '_SIR' ? await text($, `${ROOT}/${hit}/.sir/project.yml`) : ''
  if (!yml) return [...base, 'This chat is the HQ manager: it plans, reviews project chats and opens the next project after Ahmed approves; it does not build products.', RULES].join('\n')
  const id = field(yml, 'id')
  let wave = '?'
  try {
    wave = String((JSON.parse(await text($, `${SIR}/plans/waves.json`)) as Record<string, number>)[id] ?? '?')
  } catch {
    wave = '?'
  }
  const tasks = (await text($, `${ROOT}/${hit}/.sir/TASKS.md`)).split(String.fromCharCode(10)).filter(l => /^- \[[ x]\] T-\d+/.test(l))
  const next = tasks.find(l => l.startsWith('- [ ]'))?.replace(/^- \[ \] (T-\d+) \| owner: [^|]+\| (\(kit\) )?/, '$1 ').slice(0, 140) ?? 'none'
  const unread = (await text($, `${SIR}/ops/bus/${id}.md`)).split(String.fromCharCode(10)).filter(l => l.startsWith('- [ ]')).length
  return [
    ...base,
    `This chat builds ${field(yml, 'name')} (wave ${wave}, ${tasks.filter(l => l.startsWith('- [x]')).length}/${tasks.length} tasks). Next task: ${next}.`,
    `Messages for you: ${unread} unread in ${SIR}/ops/bus/${id}.md. Report to HQ in ${SIR}/ops/bus/sir-hq.md; write to another project in ${SIR}/ops/bus/<slug>.md; talk live with ListAgents and SendMessage.`,
    'First: analyse the whole project, then make the plan 100x better, then build.',
    RULES,
  ].join('\n')
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'sir', description: 'Show the link to the SIR Control Room page' })

    return next(e)
  })

  on('command.run', { command: 'sir' }, async $ => ({ text: `SIR Control Room: ${await dashboardUrl($)} (pinned in the sidebar; type /sir any time).` }))

  on('prompt.compose', async ($, e, next) => {
    const out = await next(e)

    return { sections: [...out.sections, { id: 'sir:context', text: await digest($), scope: 'session' }] }
  })
}
