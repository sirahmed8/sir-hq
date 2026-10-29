#!/usr/bin/env node
// SIR memory: SubagentStop hook. When a subagent finishes, log it and remind the orchestrator
// to read the new report (full notes go to .sir/reports/ or _SIR/ops/). Never blocks, never fails.
import fs from 'node:fs';
import path from 'node:path';
import { readInput, resolveContext } from './lib.mjs';

function main() {
  const input = readInput();
  const ctx = resolveContext(input.cwd);
  if (!ctx) return;
  const agent = input.agent_type || input.subagent_type || 'subagent';
  fs.mkdirSync(ctx.stateDir, { recursive: true });
  fs.appendFileSync(path.join(ctx.stateDir, 'subagent.log'), `- ${new Date().toISOString()} · ${agent} finished · ${ctx.name}\n`);
  const where = ctx.mode === 'hq' ? '_SIR/ops/' : '.sir/reports/';
  process.stdout.write(JSON.stringify({
    systemMessage: `Subagent "${agent}" finished. Read its summary and any report under ${where} before acting on it, then update the BOARD/checkpoint.`,
  }));
}

try {
  main();
} catch {
  // never block a subagent from stopping
}
