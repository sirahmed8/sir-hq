#!/usr/bin/env node
// SIR memory: SessionStart hook (startup, resume, clear, compact).
// Prints the session's checkpoint and the never-forget list, so a new, resumed, cleared or
// compacted session starts oriented. Claude Code adds this output to the context.
// It never fails a session: on any error it ends quietly with exit code 0.
import path from 'node:path';
import { SIR_ROOT, readInput, readText, resolveContext } from './lib.mjs';

const LIMIT = 9500; // Claude Code caps hook-added context at 10,000 characters

function main() {
  const input = readInput();
  const ctx = resolveContext(input.cwd);
  if (!ctx) return;
  const source = input.source || 'startup';
  const parts = [];

  parts.push(`## SIR memory reload (${ctx.mode === 'hq' ? 'HQ session' : `project session: ${ctx.name}`}; ${source})`);
  if (source === 'compact') {
    parts.push('The conversation was just compacted, so earlier details survive only as a summary. The files below are the source of truth.');
  } else if (source === 'clear' || source === 'resume') {
    parts.push('This session was cleared or resumed. Continue from the files below, not from memory.');
  }
  const guide = ctx.mode === 'hq' ? path.join(SIR_ROOT, 'START_HERE.md') : 'AGENTS.md (already loaded)';
  parts.push(`Next: re-read ${guide} and the files under "Re-read after a reset" in the checkpoint, then continue from "Next step". Update the checkpoint after every finished step.`);

  const start = readText(path.join(SIR_ROOT, 'START_HERE.md'));
  const never = start && start.match(/<!-- NEVER_FORGET:START -->([\s\S]*?)<!-- NEVER_FORGET:END -->/);
  if (never) parts.push(`### Never forget\n${never[1].trim()}`);

  const checkpoint = readText(ctx.checkpoint, 4200);
  parts.push(`### Checkpoint: ${ctx.checkpoint}\n${checkpoint ? checkpoint.trim()
    : 'No checkpoint yet. Create it now (HQ format: _SIR/core/04-memory.md; project format: _SIR/standard/project-templates.md).'}`);

  if (source === 'compact') {
    const bridge = readText(ctx.bridge, 1800);
    if (bridge) parts.push(`### Last steps before the compaction: ${ctx.bridge}\n${bridge.trim()}`);
  }

  let text = parts.join('\n\n');
  if (text.length > LIMIT) text = `${text.slice(0, LIMIT)}\n…(cut to fit; open the files above)`;
  process.stdout.write(`${text}\n`);
}

try {
  main();
} catch {
  // stay silent: a memory hook must never break a session
}
