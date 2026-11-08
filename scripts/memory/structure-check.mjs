#!/usr/bin/env node
// SIR Memory: nightly & on-demand structure integrity check.
// Validates projects, required non-empty files, checkpoints, pointers, manager state, READ_LOG, agent profiles.
// Writes _SIR/ops/HEALTH_REPORT.md and _SIR/ops/health.json.
// Spec: _SIR/plans/MEMORY_AND_SYNC_SYSTEM.md section 4.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { SIR_ROOT, WORKSPACE, mtime } from './lib.mjs';
import { getProjectDirs, inspectProjectPointers } from '../agent-config/sync-agent-files.mjs';
import { parseReadLog } from './read-log.mjs';
import { parseRoster } from './sync-agent-profiles.mjs';

export const HEALTH_REPORT_MD = path.join(SIR_ROOT, 'ops', 'HEALTH_REPORT.md');
export const HEALTH_JSON = path.join(SIR_ROOT, 'ops', 'health.json');

const REQUIRED_FILES = [
  'AGENTS.md',
  'CLAUDE.md',
  'GEMINI.md',
  path.join('.sir', 'CHECKPOINT.md'),
  path.join('.sir', 'PLAN.md'),
  path.join('.sir', 'TASKS.md'),
  path.join('.sir', 'BOARD.md'),
  path.join('.sir', 'ARCHITECTURE.md'),
  path.join('.sir', 'DESIGN.md'),
  path.join('.sir', 'QUALITY.md'),
  path.join('.sir', 'PRODUCTION.md'),
  path.join('.sir', 'PLATFORMS.md'),
  path.join('.sir', 'BENCHMARK.md'),
];

export function checkProject(projectDir) {
  const name = path.basename(projectDir);
  const fileIssues = [];
  const now = Date.now();
  const THREE_DAYS_MS = 3 * 24 * 60 * 60 * 1000;

  for (const rel of REQUIRED_FILES) {
    const full = path.join(projectDir, rel);
    if (!fs.existsSync(full)) {
      fileIssues.push({ file: rel, issue: 'missing' });
    } else {
      const stat = fs.statSync(full);
      if (stat.size === 0) {
        fileIssues.push({ file: rel, issue: 'zero_byte' });
      }
    }
  }

  const cpPath = path.join(projectDir, '.sir', 'CHECKPOINT.md');
  const cpTime = mtime(cpPath);
  const cpAgeDays = cpTime ? ((now - cpTime) / (24 * 60 * 60 * 1000)).toFixed(1) : null;
  const cpStale = !cpTime || (now - cpTime > THREE_DAYS_MS);

  const pointerIssues = inspectProjectPointers(projectDir);

  let status = 'GREEN';
  if (fileIssues.some(f => f.issue === 'zero_byte') || pointerIssues.length > 0) {
    status = 'RED';
  } else if (fileIssues.length > 0 || cpStale) {
    status = 'AMBER';
  }

  return {
    name,
    status,
    fileIssues,
    pointerIssuesCount: pointerIssues.length,
    checkpointMtime: cpTime ? new Date(cpTime).toISOString() : null,
    checkpointAgeDays: cpAgeDays,
    checkpointStale: cpStale,
  };
}

export function checkManagerState() {
  const now = Date.now();
  const TWENTY_FOUR_HOURS = 24 * 60 * 60 * 1000;
  const stateFile = path.join(SIR_ROOT, 'ops', 'MANAGER_STATE.md');
  const memoryFile = path.join(SIR_ROOT, 'ops', 'MANAGER_MEMORY.md');

  const sTime = mtime(stateFile);
  const mTime = mtime(memoryFile);

  const sFresh = sTime > 0 && (now - sTime < TWENTY_FOUR_HOURS);
  const mFresh = mTime > 0 && (now - mTime < TWENTY_FOUR_HOURS);

  const status = (sFresh && mFresh) ? 'GREEN' : (sTime > 0 && mTime > 0) ? 'AMBER' : 'RED';
  return {
    status,
    managerState: { exists: sTime > 0, mtime: sTime ? new Date(sTime).toISOString() : null, fresh: sFresh },
    managerMemory: { exists: mTime > 0, mtime: mTime ? new Date(mTime).toISOString() : null, fresh: mFresh },
  };
}

export function checkReadLog() {
  const entries = parseReadLog();
  const now = Date.now();
  const last = entries.length > 0 ? entries[entries.length - 1] : null;
  const lastTime = last ? new Date(last.time).getTime() : 0;
  const ageDays = lastTime ? (now - lastTime) / (24 * 60 * 60 * 1000) : 999;

  let status = 'GREEN';
  if (!last || ageDays > 7) status = 'RED';
  else if (ageDays > 1) status = 'AMBER';

  return { status, count: entries.length, lastEntry: last, ageDays: ageDays.toFixed(1) };
}

export function checkAgentsProfiles() {
  const roster = parseRoster();
  const agentsDir = path.join(SIR_ROOT, 'ops', 'agents');
  const missing = [];
  const empty = [];

  for (const a of roster) {
    const f = path.join(agentsDir, `${a.name}.md`);
    if (!fs.existsSync(f)) missing.push(a.name);
    else if (fs.statSync(f).size === 0) empty.push(a.name);
  }

  const status = (missing.length === 0 && empty.length === 0) ? 'GREEN' : 'RED';
  return { status, totalAgents: roster.length, missing, empty };
}

export function runStructureCheck() {
  const projects = getProjectDirs(WORKSPACE);
  const projectResults = projects.map(checkProject);
  const managerResult = checkManagerState();
  const readLogResult = checkReadLog();
  const agentsResult = checkAgentsProfiles();

  const overallRed = projectResults.some(p => p.status === 'RED') || managerResult.status === 'RED' || readLogResult.status === 'RED' || agentsResult.status === 'RED';
  const overallAmber = projectResults.some(p => p.status === 'AMBER') || managerResult.status === 'AMBER' || readLogResult.status === 'AMBER';
  const overallStatus = overallRed ? 'RED' : overallAmber ? 'AMBER' : 'GREEN';

  const data = {
    timestamp: new Date().toISOString(),
    overallStatus,
    manager: managerResult,
    readLog: readLogResult,
    agents: agentsResult,
    projects: projectResults,
  };

  // Write health.json
  fs.writeFileSync(HEALTH_JSON, JSON.stringify(data, null, 2), 'utf8');

  // Write HEALTH_REPORT.md
  const lines = [
    '# SIR HEALTH REPORT',
    '',
    `Generated at: **${data.timestamp}** | Overall Status: **${overallStatus}**`,
    '',
    '## System Summary',
    `- **Manager State/Memory**: ${managerResult.status} (State: ${managerResult.managerState.fresh ? 'Fresh' : 'Stale'}, Memory: ${managerResult.managerMemory.fresh ? 'Fresh' : 'Stale'})`,
    `- **READ_LOG Freshness**: ${readLogResult.status} (${readLogResult.count} total lines, last ${readLogResult.ageDays} days ago)`,
    `- **Agent Profiles**: ${agentsResult.status} (${agentsResult.totalAgents} roster agents verified)`,
    '',
    '## Projects Health Table',
    '| Project | Status | Required Files Issues | Pointers | Checkpoint Age (Stale >3d) |',
    '|---|---|---|---|---|',
  ];

  for (const p of projectResults) {
    const fileText = p.fileIssues.length === 0 ? '✓ None' : p.fileIssues.map(i => `${i.file} (${i.issue})`).join(', ');
    const ptrText = p.pointerIssuesCount === 0 ? '✓ In Sync' : `⚠ ${p.pointerIssuesCount} divergent`;
    const cpText = p.checkpointAgeDays !== null ? `${p.checkpointAgeDays}d` : 'None';
    lines.push(`| **${p.name}** | **${p.status}** | ${fileText} | ${ptrText} | ${cpText} |`);
  }

  lines.push('');
  fs.writeFileSync(HEALTH_REPORT_MD, lines.join('\n'), 'utf8');

  return data;
}

function main() {
  const data = runStructureCheck();
  console.log(`Structure Check Completed at ${data.timestamp}: Overall Status = ${data.overallStatus}`);
  console.log(`Report written to ${HEALTH_REPORT_MD}`);
  console.log(`JSON written to ${HEALTH_JSON}`);
  if (data.overallStatus === 'RED') {
    process.exit(1);
  }
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  main();
}
