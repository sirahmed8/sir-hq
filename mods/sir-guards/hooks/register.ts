import type { Register } from 'claude-code'

const PR = /\bgh\s+pr\s+create\b/i
const DELETE_LEGACY = /(\brm\b|\brmdir\b|\bdel\b|\berase\b|remove-item|git\s+clean|shutil\.rmtree)[^\n;&|]*\blegacy\b/i
const AHOME = /[\\/]AHome[\\/](?!\.sir\b|\.claude\b|AGENTS\.md|CLAUDE\.md|GEMINI\.md)/i
const AHOME_CHAT = /[\\/]AHome$/i

export const register: Register = on => {
  on('tool.call', { tool: 'Bash' }, async ($, e, next) => {
    if (PR.test(e.command)) {
      return { deny: `${$.plugin.name}: no pull requests (Ahmed, 2026-10-30). Commit and push straight to main.` }
    }
    if (DELETE_LEGACY.test(e.command)) {
      return { deny: `${$.plugin.name}: legacy/ is the source code every build ports from and is never deleted. At M6 it is moved to D:/Projects/old projects, not removed.` }
    }
    if (AHOME.test(e.command) && !AHOME_CHAT.test(await $.session.cwd())) {
      return { deny: `${$.plugin.name}: AHome's files are private and stay out of every chat except the one opened in the AHome folder.` }
    }

    return next(e)
  }).catch(($, e, next) => (next.called ? next(e) : { deny: `${$.plugin.name}: its guard failed, so the command was stopped.` }))

  for (const tool of ['Read', 'Edit', 'Write'] as const) {
    on('tool.call', { tool }, async ($, e, next) => {
      if (AHOME.test(e.file_path) && !AHOME_CHAT.test(await $.session.cwd())) {
        return { deny: `${$.plugin.name}: AHome's files are private and stay out of every chat except the one opened in the AHome folder.` }
      }

      return next(e)
    }).catch(($, e, next) => (next.called ? next(e) : { deny: `${$.plugin.name}: its guard failed, so the call was stopped.` }))
  }
}
