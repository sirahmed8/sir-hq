import { expect, test } from 'claude-code/testing'

test('a pull request command is stopped and a plain push goes through', async ($, on) => {
  on('session.cwd', () => ({ value: 'D:/Projects/SIR Obour Hub' }))
  on('tool.call', () => ({ result: {} }))

  const pr = await $.tool.call({ tool: 'Bash', command: 'gh pr create --fill' })
  expect(pr.deny).toContain('no pull requests')

  const push = await $.tool.call({ tool: 'Bash', command: 'git push origin main' })
  expect(push.deny).toBeUndefined()
})

test('deleting legacy is stopped, moving it is not', async ($, on) => {
  on('session.cwd', () => ({ value: 'D:/Projects/SIR Obour Hub' }))
  on('tool.call', () => ({ result: {} }))

  const rm = await $.tool.call({ tool: 'Bash', command: 'rm -rf "D:/Projects/SIR Obour Hub/legacy"' })
  expect(rm.deny).toContain('legacy')

  const mv = await $.tool.call({ tool: 'Bash', command: 'mv legacy "D:/Projects/old projects/x"' })
  expect(mv.deny).toBeUndefined()
})

test('AHome files are fenced off outside the AHome chat', async ($, on) => {
  on('session.cwd', () => ({ value: 'D:/Projects/SIR Jobs' }))
  on('tool.call', () => ({ result: {} }))

  const read = await $.tool.call({ tool: 'Read', file_path: 'D:/Projects/AHome/data/notes.db' })
  expect(read.deny).toContain('private')

  const kit = await $.tool.call({ tool: 'Read', file_path: 'D:/Projects/AHome/.sir/PLAN.md' })
  expect(kit.deny).toBeUndefined()
})
