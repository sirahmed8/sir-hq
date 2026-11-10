# Memory: how the team remembers, and survives compaction

> **Status 2026-11-10.** The checkpoint rules below apply to every tool, not only Claude. A checkpoint stays small: `ops/HQ_CHECKPOINT.md` must stay under 6 KB (the hook prints its top into every session); older blocks go to `ops/archive/`. The save rule (commit, push, update the checkpoint after every finished step) is in `D:\Projects\AGENTS.md`.

Long sessions get **compacted**: when the context fills up, Claude Code replaces the conversation with a summary, and details are lost. Usage-limit pauses, crashes, `/clear` and new sessions cause the same loss. The fix has three parts: keep memory in files, keep those files current, and reload them automatically. The chat is never the source of truth.

## What survives compaction in Claude Code

Checked in October 2026 at code.claude.com/docs (context-window, memory and hooks pages). Re-verify when Claude Code updates.

- **Re-injected from disk:** the project-root `CLAUDE.md` and unscoped `.claude/rules/` files, auto memory (`MEMORY.md`: first 200 lines or 25 KB), skill descriptions, and the plan written in plan mode.
- **Re-read automatically:** up to five of the most recently read or edited files (large ones come back only as a path).
- **Lost into the summary:** everything said in the conversation, tool output, context that hooks added earlier, path-scoped rules and nested `CLAUDE.md` files (these reload only when a matching file is touched again).
- **Hooks:** `SessionStart` hooks run again after a compaction (source `compact`), and their output is added to the new context, capped at 10,000 characters. `PreCompact` runs just before it.

So anything that must survive goes into a file that is either re-injected automatically or printed by a hook.

## The memory layers

| Layer | File | Written by | Why it survives |
|---|---|---|---|
| Permanent rules | `D:\Projects\CLAUDE.md` (workspace) and each project's `CLAUDE.md` → `AGENTS.md` | You, at setup | Re-injected from disk after every compaction |
| Current state | `_SIR/ops/HQ_CHECKPOINT.md`; per project `.sir/CHECKPOINT.md` | The session doing the work, after every step | Printed by the `SessionStart` hook |
| Bridge (last steps) | `_SIR/ops/LAST_CONTEXT.md`; per project `.sir/LAST_CONTEXT.md` | The `PreCompact` hook | Printed after each compaction |
| History | `_SIR/ops/MISSION_LOG.md` (append-only); per project `CHANGELOG.md` and `.sir/reports/` | Everyone | Read on demand |
| Decisions | `.sir/decisions/ADR-*.md`; small ones in the log | Whoever decides | Read on demand |
| Requirements | `_SIR/REQUIREMENTS.md` | HQ | Reviewed weekly and at every milestone |
| Verified facts | `_SIR/knowledge/<topic>.md` | Whoever verifies | Read on demand |
| Tasks | `.sir/BOARD.md`, `.sir/tasks/T-NNN.md` | PMs | Read on demand |

## Rules

1. **Write-ahead.** Update the checkpoint after every finished step, not only at milestones or at the end of a session, and before starting anything long (a big build, a fan-out, long research). A compaction should never cost more than the current step.
2. **Small and current.** A checkpoint stays under about 100 lines and says what's true now. Finished items move to `MISSION_LOG.md` or the project's `CHANGELOG.md`.
3. **Exact next step.** "Next step" names the command, file or task ID precisely enough that a fresh agent can continue without guessing.
4. **Decisions are written when they're made:** one line in the log, or an ADR, with the reason.
5. **Promises are tracked.** Anything started or promised goes under "Open promises" until it's finished.
6. **Keep the main context lean.** HQ and PMs delegate big reads, searches, logs and research to subagents, which work in their own context and return short summaries. Read files in line ranges; don't paste long outputs; don't re-read what the checkpoint or `_SIR/knowledge/` already says. Read only the phase file and modules the current step needs.
7. **Rotate sessions.** Prefer fresh sessions over one endless one: each big unit of work gets its own background session (`claude --bg`, see A2) that starts from the checkpoint and ends with it updated. If Ahmed sees a session getting slow or confused, he can type `/clear` and then `continue`: the hook reloads everything.
8. **Compact earlier, with room to spare.** Set the auto-compact window below the maximum (the `/autocompact` command or its setting; check the current docs for both; the older `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` variable has been unreliable). Every turn re-sends the whole context, so a smaller context makes each turn cheaper in usage, and this memory system makes frequent compaction safe. On a 1M-token window, a few hundred thousand tokens is a sensible limit for HQ.
9. **Auto memory is a convenience, not the truth.** Claude Code's own `MEMORY.md` can stay on for small learnings; don't copy checkpoint content into it.
10. **Same protocol in every tool.** Antigravity, Codex, OpenCode and Kilo follow the same files: their always-on rules say to read the checkpoint at the start of every task and after any context reset (Phase 1.13).

## Set it up (Phase 0, first step)

1. Create `_SIR/ops/` with `HQ_CHECKPOINT.md` (format below) and `MISSION_LOG.md`.
2. Copy `core/workspace-CLAUDE.md` to `D:\Projects\CLAUDE.md`. Claude Code loads it in every session under `D:\Projects` and re-injects it after compaction, so it holds the short, permanent rules. Keep it under 200 lines.
3. Check Node.js (`node --version`, 18 or newer). The scripts in `_SIR/scripts/memory/` need nothing else.
4. Merge these hooks into the user settings (`~/.claude/settings.json`) without removing existing entries, then confirm them with `/hooks`. No matcher means every source (startup, resume, clear, compact):

```json
{
  "hooks": {
    "SessionStart": [
      { "hooks": [ { "type": "command", "command": "node \"D:/Projects/_SIR/scripts/memory/session-start.mjs\"", "timeout": 30 } ] }
    ],
    "PreCompact": [
      { "hooks": [ { "type": "command", "command": "node \"D:/Projects/_SIR/scripts/memory/pre-compact.mjs\"", "timeout": 30 } ] }
    ],
    "Stop": [
      { "hooks": [ { "type": "command", "command": "node \"D:/Projects/_SIR/scripts/memory/stop-guard.mjs\"", "timeout": 30 } ] }
    ]
  }
}
```

5. Test each script before relying on it (Git Bash shown; PowerShell works the same way):

```bash
echo '{"cwd":"D:/Projects","source":"compact"}' | node "D:/Projects/_SIR/scripts/memory/session-start.mjs"
echo '{"cwd":"D:/Projects","trigger":"manual","transcript_path":"<a real transcript .jsonl from ~/.claude/projects/>"}' | node "D:/Projects/_SIR/scripts/memory/pre-compact.mjs"
```

   The first prints the reload block; the second writes `_SIR/ops/LAST_CONTEXT.md`, a snapshot in `_SIR/ops/snapshots/` and a line in `_SIR/ops/memory.log`. After the first real compaction, check that the reload appeared in the context and that `memory.log` has the entry. Record the results in `MISSION_LOG.md`.
6. Projects need no extra setup: the same user-level hooks serve every session, and the scripts recognize a project by its `.sir/CHECKPOINT.md`. Add `.sir/.memory/` and `.sir/LAST_CONTEXT.md` to every project's `.gitignore`.
7. Back up the mission state off the laptop every day, so a disk failure can't erase it: make `_SIR` a private git repo (`sir-hq`) and push it (keep `platform/` and `standard/` as their own repos, ignored here; also ignore `ops/LAST_CONTEXT.md`, `ops/snapshots/`, `ops/memory.log` and `ops/stop-guard.json`).
8. Automations that call `claude -p` (n8n, scheduled scripts) set `SIR_MEMORY_GUARD=0`, so the stop guard never adds turns to them.

## HQ checkpoint format (`_SIR/ops/HQ_CHECKPOINT.md`)

```markdown
# HQ CHECKPOINT — updated <YYYY-MM-DD HH:mm>
## Phase and step
Phase N (`phases/NN-….md`), step N.x: <name>
## Now
<what is in progress and exactly where it stands>
## Next step
<exact command, file or task>, then the 2 after it
## Running in the background
- <session, subagent or build> · <what> · started <time>
## Decisions since the last milestone
- <one line each, with an ADR or log link>
## Open promises
- <started or promised, not finished>
## Owner actions listed (never blocking)
- <count and the newest items>
## Usage
<last /usage reading and what it means for pacing>
## Re-read after a reset
- START_HERE.md · phases/NN-….md · <any other file that matters right now>
```

Project checkpoints use the template in `standard/project-templates.md`, which has the same "Now", "Next step", "Open promises" and "Re-read after a reset" sections.

## What the scripts do

- **`session-start.mjs`** (`SessionStart`): finds the session's checkpoint (a project's `.sir/CHECKPOINT.md`, searching up from the working folder, or `_SIR/ops/HQ_CHECKPOINT.md` for other sessions under `D:\Projects`) and prints a short reload notice, the never-forget list from `START_HERE.md`, the checkpoint and, after a compaction, the bridge of the last steps. The whole block stays under 9,500 characters. Outside `D:\Projects` it prints nothing.
- **`pre-compact.mjs`** (`PreCompact`): appends a line to `memory.log`, snapshots the checkpoint (keeps the last 20), and writes the bridge file from the end of the session transcript: the latest requests, messages and tool calls, trimmed. It never blocks compaction.
- **`stop-guard.mjs`** (`Stop`): if real work happened after the checkpoint was last saved and that save is more than 20 minutes old, it blocks the stop once and asks Claude to update the checkpoint and the log. It never asks twice for the same session within 30 minutes, skips short runs, and is off when `SIR_MEMORY_GUARD=0`.
- **`lib.mjs`:** shared helpers.

All of them are plain Node.js with no dependencies, and they exit quietly on any error, so they can never break a session. Improve them when needed, keep those properties, and re-test after every change.

## If memory still slips

- Hooks not running: check `/hooks`, then run `claude --debug` and look for hook errors. On Windows, hook commands run through Git Bash, or PowerShell if Git Bash is missing; `node "<path>"` works in both.
- The reload is cut short: the checkpoint is too long. Trim it (rule 2).
- The agent repeats finished work: "Next step" was vague, or the checkpoint wasn't updated after the last step. Fix the habit and write it in `_SIR/knowledge/memory-lessons.md`.
- Use `/context` to see what's filling the context, and move anything heavy into subagents.
