#!/usr/bin/env node
// SIR Memory: session read logger and verifier.
// Appends read proof lines to _SIR/ops/READ_LOG.md and verifies sessions.
// Spec: _SIR/plans/MEMORY_AND_SYNC_SYSTEM.md section 3.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { SIR_ROOT, WORKSPACE, resolveContext, mtime, readText } from './lib.mjs';

export const LOG_FILE = path.join(SIR_ROOT, 'ops', 'READ_LOG.md');

export function extractNextStep(checkpointText) {
  if (!checkpointText) return 'Initial session / no checkpoint';
  const match = checkpointText.match(/(?:Next(?:\s+step)?|### Next step|## Next step)[:\s]+([^\r\n]+)/i);
  if (match) return match[1].trim();
  const lines = checkpointText.split('\n');
  for (const l of lines) {
    if (/next step/i.test(l)) return l.replace(/^[^a-zA-Z0-9]+/, '').trim();
  }
  return 'Continue task';
}

export function extractFilesRead(checkpointText, ctx, defaultFiles = []) {
  const files = [...defaultFiles];
  if (ctx && ctx.mode === 'hq') {
    files.push(path.join(SIR_ROOT, 'START_ANY_AI.md'));
    files.push(path.join(WORKSPACE, 'AGENTS.md'));
  } else if (ctx && ctx.name) {
    files.push(path.join(WORKSPACE, ctx.name, 'AGENTS.md'));
  }
  if (checkpointText) {
    const section = checkpointText.match(/Re-read after a reset[:\s]*([\s\S]*?)(?:\n##|\n#|$)/i);
    if (section) {
      const items = section[1].split(/[\n,]+/).map(s => s.replace(/^[-*`\s]+|[`\s]+$/g, '').trim()).filter(Boolean);
      for (const it of items) {
        if (!files.includes(it)) files.push(it);
      }
    }
  }

  return files.map(f => {
    let rel = f;
    let full = path.isAbsolute(f) ? f : path.join(WORKSPACE, f);
    if (isInside(full, WORKSPACE)) {
      rel = path.relative(WORKSPACE, full).replace(/\\/g, '/');
    }
    const t = mtime(full);
    const dateStr = t ? new Date(t).toISOString().slice(0, 10) : new Date().toISOString().slice(0, 10);
    return `${rel}@${dateStr}`;
  });
}

function isInside(child, parent) {
  const rel = path.relative(parent, child);
  return rel === '' || (!rel.startsWith('..') && !path.isAbsolute(rel));
}

export function appendReadLog(entry, logPath = LOG_FILE) {
  const now = entry.time || new Date().toISOString();
  const tool = entry.tool || 'unknown-tool';
  const agent = entry.agent || 'unknown-agent';
  const project = entry.project || 'HQ';
  const filesStr = Array.isArray(entry.filesRead) ? entry.filesRead.join(', ') : (entry.filesRead || '');
  const nextStep = entry.nextStep || 'Continue task';

  const line = `${now} | ${tool} | ${agent} | ${project} | ${filesStr} | ${nextStep}\n`;

  fs.mkdirSync(path.dirname(logPath), { recursive: true });
  if (!fs.existsSync(logPath)) {
    fs.writeFileSync(logPath, '# READ LOG (one line per session start, newest at the bottom)\n\n', 'utf8');
  }
  fs.appendFileSync(logPath, line, 'utf8');
  return line;
}

export function logSessionStart({ tool = 'claude-code', agent = 'claude', cwd = process.cwd(), ctx = null, files = [] } = {}) {
  const resolved = ctx || resolveContext(cwd);
  const cpText = resolved && resolved.checkpoint ? readText(resolved.checkpoint) : '';
  const nextStep = extractNextStep(cpText);
  const filesRead = extractFilesRead(cpText, resolved, files);

  return appendReadLog({
    time: new Date().toISOString(),
    tool,
    agent,
    project: resolved ? (resolved.mode === 'hq' ? 'HQ' : resolved.name) : 'HQ',
    filesRead,
    nextStep,
  });
}

export function parseReadLog(logPath = LOG_FILE) {
  if (!fs.existsSync(logPath)) return [];
  const text = fs.readFileSync(logPath, 'utf8');
  const lines = text.split('\n');
  const entries = [];
  for (const l of lines) {
    const trimmed = l.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    const parts = trimmed.split('|').map(p => p.trim());
    if (parts.length >= 6) {
      entries.push({
        time: parts[0],
        date: parts[0].slice(0, 10),
        tool: parts[1],
        agent: parts[2],
        project: parts[3],
        filesRead: parts[4],
        nextStep: parts.slice(5).join(' | '),
      });
    }
  }
  return entries;
}

export function verifyTodaySessions(logPath = LOG_FILE) {
  const today = new Date().toISOString().slice(0, 10);
  const entries = parseReadLog(logPath);
  const todayEntries = entries.filter(e => e.date === today);

  const loggedProjects = new Set(todayEntries.map(e => e.project.toLowerCase()));
  const loggedAgents = new Set(todayEntries.map(e => {
    const raw = e.agent.toLowerCase();
    const m = raw.match(/([a-z0-9_-]+)/);
    return m ? m[1] : raw;
  }));

  const unverified = [];

  // Check HQ Checkpoint
  const hqCp = path.join(SIR_ROOT, 'ops', 'HQ_CHECKPOINT.md');
  if (fs.existsSync(hqCp)) {
    const d = new Date(fs.statSync(hqCp).mtimeMs).toISOString().slice(0, 10);
    if (d === today && !loggedProjects.has('hq')) {
      unverified.push({ target: 'HQ_CHECKPOINT.md', type: 'checkpoint', project: 'HQ', date: d });
    }
  }

  // Check Project Checkpoints
  const entriesDir = fs.readdirSync(WORKSPACE, { withFileTypes: true });
  for (const ent of entriesDir) {
    if (!ent.isDirectory() || ent.name.startsWith('.') || ent.name.startsWith('_')) continue;
    const cp = path.join(WORKSPACE, ent.name, '.sir', 'CHECKPOINT.md');
    if (fs.existsSync(cp)) {
      const d = new Date(fs.statSync(cp).mtimeMs).toISOString().slice(0, 10);
      if (d === today && !loggedProjects.has(ent.name.toLowerCase())) {
        unverified.push({ target: `${ent.name}/.sir/CHECKPOINT.md`, type: 'checkpoint', project: ent.name, date: d });
      }
    }
  }

  // Check Agent profiles in _SIR/ops/agents/*.md
  const agentsDir = path.join(SIR_ROOT, 'ops', 'agents');
  if (fs.existsSync(agentsDir)) {
    const aFiles = fs.readdirSync(agentsDir).filter(f => f.endsWith('.md'));
    for (const af of aFiles) {
      const aPath = path.join(agentsDir, af);
      const aName = path.basename(af, '.md').toLowerCase();
      const content = fs.readFileSync(aPath, 'utf8');
      const statDate = new Date(fs.statSync(aPath).mtimeMs).toISOString().slice(0, 10);
      const wroteToday = statDate === today || content.includes(today);
      if (wroteToday && !loggedAgents.has(aName)) {
        unverified.push({ target: `_SIR/ops/agents/${af}`, type: 'agent', agent: aName, date: statDate });
      }
    }
  }

  return { today, todayEntriesCount: todayEntries.length, unverified };
}

function main() {
  const args = process.argv.slice(2);
  if (args.includes('--verify')) {
    const v = verifyTodaySessions();
    console.log(`read-log --verify (Date: ${v.today}): ${v.todayEntriesCount} session(s) logged today.`);
    if (v.unverified.length === 0) {
      console.log('PASS: All sessions that updated checkpoints or agent profiles today have logged read entries.');
      process.exit(0);
    } else {
      console.log(`WARN: Found ${v.unverified.length} session(s) with modifications today but no read line:`);
      for (const u of v.unverified) {
        console.log(`  - [${u.type}] ${u.target} (project/agent: ${u.project || u.agent})`);
      }
      process.exit(1);
    }
  }

  // CLI read-log logging mode
  let tool = 'cli';
  let agent = 'agent';
  let project = null;
  let next = null;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--tool' && args[i + 1]) tool = args[++i];
    else if (args[i] === '--agent' && args[i + 1]) agent = args[++i];
    else if (args[i] === '--project' && args[i + 1]) project = args[++i];
    else if (args[i] === '--next' && args[i + 1]) next = args[++i];
  }

  const ctx = resolveContext(process.cwd());
  const entry = logSessionStart({
    tool,
    agent,
    cwd: process.cwd(),
    ctx: project ? { mode: project.toLowerCase() === 'hq' ? 'hq' : 'project', name: project } : ctx,
    files: [],
  });
  console.log(`Logged session start to ${LOG_FILE}:\n${entry.trim()}`);
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  main();
}
