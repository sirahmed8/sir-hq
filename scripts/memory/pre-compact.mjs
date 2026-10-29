#!/usr/bin/env node
// SIR memory: PreCompact hook. Before Claude Code compacts the conversation it
// 1) logs the compaction, 2) snapshots the checkpoint (keeps the last 20), and
// 3) writes a short bridge of the latest requests, messages and tool calls from the
//    transcript, which session-start.mjs prints right after the compaction.
// It never blocks compaction: it always exits 0, even on errors.
import fs from 'node:fs';
import path from 'node:path';
import { readInput, resolveContext } from './lib.mjs';

const KEEP_SNAPSHOTS = 20;
const TAIL_BYTES = 1_500_000;
const MAX_ITEMS = 24;
const MAX_CHARS = 1700;

const clip = (value, n) => {
  const t = String(value ?? '').replace(/\s+/g, ' ').trim();
  return t.length > n ? `${t.slice(0, n - 1)}…` : t;
};
const isNoise = (t) => !t || /^\s*</.test(t) || t.includes('Caveat:');

function tailLines(file) {
  const fd = fs.openSync(file, 'r');
  try {
    const size = fs.fstatSync(fd).size;
    const start = Math.max(0, size - TAIL_BYTES);
    const buf = Buffer.alloc(size - start);
    fs.readSync(fd, buf, 0, buf.length, start);
    let text = buf.toString('utf8');
    if (start > 0) text = text.slice(text.indexOf('\n') + 1); // drop the partial first line
    return text.split('\n').filter(Boolean);
  } finally {
    fs.closeSync(fd);
  }
}

function describeTool(input = {}) {
  return input.command || input.file_path || input.path || input.pattern || input.url
    || input.description || input.prompt || JSON.stringify(input);
}

function bridgeFrom(lines) {
  const items = [];
  for (const line of lines) {
    let entry;
    try { entry = JSON.parse(line); } catch { continue; }
    if (!entry || entry.isMeta || entry.isCompactSummary || !entry.message) continue;
    const { role, content } = entry.message;
    if (role === 'user') {
      if (typeof content === 'string') {
        if (!isNoise(content)) items.push(`- Request: ${clip(content, 280)}`);
      } else if (Array.isArray(content)) {
        for (const c of content) if (c?.type === 'text' && !isNoise(c.text)) items.push(`- Request: ${clip(c.text, 280)}`);
      }
    } else if (role === 'assistant' && Array.isArray(content)) {
      for (const c of content) {
        if (c?.type === 'text' && c.text?.trim()) items.push(`- You: ${clip(c.text, 280)}`);
        else if (c?.type === 'tool_use') items.push(`- Tool ${c.name}: ${clip(describeTool(c.input), 150)}`);
      }
    }
  }
  const kept = []; // newest items that fit the budget, kept in time order
  let size = 0;
  for (let i = items.length - 1; i >= 0 && kept.length < MAX_ITEMS; i--) {
    if (size + items[i].length > MAX_CHARS) break;
    kept.unshift(items[i]);
    size += items[i].length + 1;
  }
  return kept;
}

function main() {
  const input = readInput();
  const ctx = resolveContext(input.cwd);
  if (!ctx) return;
  fs.mkdirSync(ctx.stateDir, { recursive: true });
  const now = new Date();

  fs.appendFileSync(path.join(ctx.stateDir, 'memory.log'),
    `- ${now.toISOString()} · compaction (${input.trigger || 'unknown'}) · ${ctx.name}\n`);

  if (fs.existsSync(ctx.checkpoint)) {
    const dir = path.join(ctx.stateDir, 'snapshots');
    fs.mkdirSync(dir, { recursive: true });
    fs.copyFileSync(ctx.checkpoint, path.join(dir, `CHECKPOINT-${now.toISOString().replace(/[:.]/g, '-')}.md`));
    const all = fs.readdirSync(dir).filter((f) => f.startsWith('CHECKPOINT-')).sort();
    for (const f of all.slice(0, Math.max(0, all.length - KEEP_SNAPSHOTS))) fs.rmSync(path.join(dir, f), { force: true });
  }

  if (input.transcript_path && fs.existsSync(input.transcript_path)) {
    const items = bridgeFrom(tailLines(input.transcript_path));
    if (items.length) {
      fs.writeFileSync(ctx.bridge, `# Last steps before the compaction (${now.toISOString()})\n`
        + 'Oldest first. Written by _SIR/scripts/memory/pre-compact.mjs. Local only: never commit it.\n\n'
        + `${items.join('\n')}\n`);
    }
  }
}

try {
  main();
} catch {
  // never block compaction
}
