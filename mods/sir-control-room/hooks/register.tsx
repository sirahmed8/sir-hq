import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import type { Row } from '../types'

const PANE = 'sir-control-room'
const ROOT = 'D:/Projects'
const EVERY_MS = 30_000
const BAR = 12

// Change the tag when a row's fields change: it declines what an earlier
// version stored, which outlives a reload.
const rows = atom({ plugin: 'sir-control-room', key: 'rows' } as const, [], { shape: 'rows-2' })
const stamp = atom({ plugin: 'sir-control-room', key: 'stamp' } as const, 0, { shape: 'stamp-1' })

async function text($: EngineInterface, path: string): Promise<string> {
  try {
    return String(await $.fs.read(path))
  } catch {
    return ''
  }
}

function field(yml: string, key: string): string {
  const hit = yml.match(new RegExp(`^${key}:\\s*(.+)$`, 'm'))
  return hit ? hit[1].trim() : ''
}

async function collect($: EngineInterface): Promise<Row[]> {
  let waves: Record<string, number> = {}
  try {
    waves = JSON.parse(await text($, `${ROOT}/_SIR/plans/waves.json`))
  } catch {
    waves = {}
  }
  const entries = await $.fs.list(ROOT)
  const dirs = entries.filter(e => e.kind === 'dir' && (e.name.startsWith('SIR ') || e.name === 'AHome'))
  const out: Row[] = []
  for (const dir of dirs) {
    const tasks = await text($, `${ROOT}/${dir.name}/.sir/TASKS.md`)
    if (!tasks) continue
    const yml = await text($, `${ROOT}/${dir.name}/.sir/project.yml`)
    const lines = tasks.split('\n').filter(l => /^- \[[ x]\] T-\d+/.test(l))
    const open = lines.find(l => l.startsWith('- [ ]'))
    const id = field(yml, 'id')
    const isPrivate = id === 'ahome'
    out.push({
      name: isPrivate ? 'AHome (private)' : field(yml, 'name') || dir.name,
      wave: waves[id] ?? 9,
      done: lines.filter(l => l.startsWith('- [x]')).length,
      total: lines.length,
      next: isPrivate || !open ? '' : open.replace(/^- \[ \] (T-\d+) \| owner: [^|]+\| (\(kit\) )?/, '$1 ').replace(/\s*\| depends:.*$/, '').slice(0, 90),
      isPrivate,
      inbox: (await text($, `${ROOT}/_SIR/ops/bus/${id}.md`)).split(String.fromCharCode(10)).filter(l => l.startsWith('- [ ]')).length,
      folder: dir.name,
    })
  }
  return out.sort((a, b) => a.wave - b.wave || a.name.localeCompare(b.name))
}

const bar = (done: number, total: number) => {
  const filled = total === 0 ? 0 : Math.round((BAR * done) / total)
  return '█'.repeat(filled) + '░'.repeat(BAR - filled)
}

async function refresh($: EngineInterface): Promise<void> {
  const fresh = await collect($)
  await update($, rows, () => fresh)
  await update($, stamp, () => Date.now())
  const done = fresh.reduce((n, r) => n + r.done, 0)
  const total = fresh.reduce((n, r) => n + r.total, 0)
  $.ui.status(`SIR ${done}/${total} tasks`)
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'sir', description: 'Open the SIR Control Room pane (all projects, live)' })
    void $.ui.open({ id: PANE, title: 'SIR Control Room' })
    await refresh($)
    $.clock.every(EVERY_MS, () => void refresh($))

    return next(e)
  })

  on('command.run', { command: 'sir' }, async $ => {
    await $.ui.open({ id: PANE, title: 'SIR Control Room' })
    await refresh($)

    return { text: 'SIR Control Room opened. It refreshes every 30 seconds from the project files.' }
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text } = $.ui.resolve(e)
    const list = await read($, rows)
    const at = await read($, stamp)
    const done = list.reduce((n, r) => n + r.done, 0)
    const total = list.reduce((n, r) => n + r.total, 0)
    const room = Math.max(3, Math.floor(((e.viewport?.rows ?? 30) - 6) / 2))
    const when = at ? new Date(at).toLocaleTimeString() : 'loading'

    return (
      <Box flexDirection="column">
        <Text bold>SIR Control Room</Text>
        <Text>
          {bar(done, total)} {done}/{total} tasks done <Text dimColor>(updated {when})</Text>
        </Text>
        {list.length === 0 && <Text dimColor>No project files found under {ROOT}.</Text>}
        {list.slice(0, room).map(r => (
          <Box flexDirection="column">
            <Text bold={r.done > 0}>
              W{r.wave} {r.name} {bar(r.done, r.total)} {r.done}/{r.total}{r.inbox > 0 ? `  inbox ${r.inbox}` : ''}
            </Text>
            {r.next !== '' && <Text dimColor>   next: {r.next}</Text>}
          </Box>
        ))}
        {list.length > room && <Text dimColor>+{list.length - room} more: make the pane taller</Text>}
      </Box>
    )
  })
}
