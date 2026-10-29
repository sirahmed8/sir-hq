#!/usr/bin/env node
// SIR memory: Stop hook. If the session did real work after the checkpoint was last
// updated, and that update is more than 20 minutes old, it asks Claude once to update the
// checkpoint before stopping. It never asks twice for the same session within 30 minutes,
// skips short runs, and is off when SIR_MEMORY_GUARD=0 (set that for automation runs such as
// n8n calling `claude -p`). On any error it exits quietly and lets the session stop.
import fs from 'node:fs';
import path from 'node:path';
import { mtime, readInput, resolveContext } from './lib.mjs';

const STALE_MS = 20 * 60 * 1000;
const REPEAT_MS = 30 * 60 * 1000;
const MIN_TRANSCRIPT_BYTES = 150_000;

function main() {
  if (process.env.SIR_MEMORY_GUARD === '0') return;
  const input = readInput();
  if (input.stop_hook_active) return;
  const ctx = resolveContext(input.cwd);
  if (!ctx || !input.transcript_path) return;

  let transcript;
  try { transcript = fs.statSync(input.transcript_path); } catch { return; }
  if (transcript.size < MIN_TRANSCRIPT_BYTES) return;

  const now = Date.now();
  const checkpointTime = mtime(ctx.checkpoint);
  if (checkpointTime && now - checkpointTime < STALE_MS) return; // fresh enough
  if (checkpointTime && transcript.mtimeMs <= checkpointTime) return; // nothing new since

  const marker = path.join(ctx.stateDir, 'stop-guard.json');
  try {
    const last = JSON.parse(fs.readFileSync(marker, 'utf8'));
    if (last.session === input.session_id && now - last.at < REPEAT_MS) return;
  } catch {
    // no marker yet
  }
  fs.mkdirSync(ctx.stateDir, { recursive: true });
  fs.writeFileSync(marker, JSON.stringify({ session: input.session_id, at: now }));

  const log = ctx.mode === 'hq' ? '_SIR/ops/MISSION_LOG.md' : 'CHANGELOG.md (Unreleased) or .sir/reports/';
  const reason = `Before you stop: update ${ctx.checkpoint} (Now, Next step with the exact command or file, `
    + `Open promises, Re-read after a reset) and add a line to ${log}. Then stop. This reminder appears once.`;
  process.stdout.write(JSON.stringify({ decision: 'block', reason }));
}

try {
  main();
} catch {
  // let the session stop normally
}
