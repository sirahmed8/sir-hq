#!/usr/bin/env node
// Extends _SIR/ops/dashboard.html const D = {...} with per-project checkpoint time,
// read-status (from READ_LOG), open tasks (from TASKS.md), and running agents.
// Spec: _SIR/plans/MEMORY_AND_SYNC_SYSTEM.md section 4 & M6 brief.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { SIR_ROOT, WORKSPACE } from './lib.mjs';
import { parseReadLog } from './read-log.mjs';
import { runStructureCheck } from './structure-check.mjs';

export const DASHBOARD_HTML = path.join(SIR_ROOT, 'ops', 'dashboard.html');
export const HEALTH_JSON = path.join(SIR_ROOT, 'ops', 'health.json');

export function countOpenTasks(tasksFile) {
  if (!fs.existsSync(tasksFile)) return 0;
  const content = fs.readFileSync(tasksFile, 'utf8');
  const lines = content.split('\n');
  let open = 0;
  for (const l of lines) {
    if (/^\s*-\s*\[\s*\]/i.test(l) || /^\s*-\s*T-\d+.*done:\s*false/i.test(l)) {
      open++;
    }
  }
  return open;
}

export function computeReadStatus(readLogEntries, projectName, slug) {
  const now = Date.now();
  const ONE_DAY_MS = 24 * 60 * 60 * 1000;
  const SEVEN_DAYS_MS = 7 * ONE_DAY_MS;

  const matches = readLogEntries.filter(e => {
    const p = e.project.toLowerCase();
    const nameMatch = p === projectName.toLowerCase();
    const slugMatch = slug && p === slug.toLowerCase().replace(/^sir-/, '');
    const containsMatch = projectName.toLowerCase().includes(p) || (slug && slug.toLowerCase().includes(p));
    return nameMatch || slugMatch || containsMatch;
  });

  if (matches.length === 0) {
    return { status: 'red', label: 'No read log', time: null, ageDays: 999 };
  }

  const latest = matches[matches.length - 1];
  const t = new Date(latest.time).getTime();
  const diff = now - t;
  const ageDays = (diff / ONE_DAY_MS).toFixed(1);

  if (diff < ONE_DAY_MS) {
    return { status: 'green', label: 'Read today', time: latest.time, ageDays };
  } else if (diff < SEVEN_DAYS_MS) {
    return { status: 'amber', label: `${ageDays}d ago`, time: latest.time, ageDays };
  } else {
    return { status: 'red', label: `Stale (${ageDays}d)`, time: latest.time, ageDays };
  }
}

export function getRunningAgents(projectName, slug) {
  const activePath = path.join(SIR_ROOT, 'ops', 'active.json');
  const agents = [];
  try {
    if (fs.existsSync(activePath)) {
      const active = JSON.parse(fs.readFileSync(activePath, 'utf8'));
      for (const a of (Array.isArray(active) ? active : [])) {
        if (a.project && (a.project.toLowerCase() === projectName.toLowerCase() || (slug && a.project.toLowerCase() === slug.toLowerCase()))) {
          agents.push(a.agent || a.name || 'active-agent');
        }
      }
    }
  } catch {
    // fallback
  }
  return agents;
}

export function updateDashboardData({ dashboardPath = DASHBOARD_HTML, healthJsonPath = HEALTH_JSON } = {}) {
  let health;
  if (fs.existsSync(healthJsonPath)) {
    health = JSON.parse(fs.readFileSync(healthJsonPath, 'utf8'));
  } else {
    health = runStructureCheck();
  }

  const readLogEntries = parseReadLog();
  const healthByProject = Object.fromEntries((health.projects || []).map(p => [p.name.toLowerCase(), p]));

  const html = fs.readFileSync(dashboardPath, 'utf8');
  const scriptRegex = /const D = ({[\s\S]*?});\s*const \$ =/;
  const match = html.match(scriptRegex);
  if (!match) {
    throw new Error('Could not find "const D = {...};" block in dashboard.html');
  }

  const D = JSON.parse(match[1]);
  D.generated = new Date().toISOString().replace('T', ' ').slice(0, 16);

  for (const p of D.projects) {
    const projName = p.name ? p.name.replace(/\s*\(.*?\)/, '').trim() : p.slug;
    const h = healthByProject[projName.toLowerCase()] ||
              healthByProject[p.slug.toLowerCase()] ||
              healthByProject[p.slug.replace(/^sir-/, '').toLowerCase()];

    p.lastCheckpoint = h && h.checkpointMtime ? h.checkpointMtime.replace('T', ' ').slice(0, 16) : null;
    p.checkpointAgeDays = h ? h.checkpointAgeDays : null;

    p.readStatus = computeReadStatus(readLogEntries, projName, p.slug);
    p.lastReadLog = p.readStatus.time ? p.readStatus.time.replace('T', ' ').slice(0, 16) : null;

    const projFolder = p.folder && fs.existsSync(p.folder) ? p.folder : path.join(WORKSPACE, projName);
    const tasksFile = path.join(projFolder, '.sir', 'TASKS.md');
    const openFromTasks = fs.existsSync(tasksFile) ? countOpenTasks(tasksFile) : (p.total - p.done);
    p.openTasks = openFromTasks > 0 ? openFromTasks : Math.max(0, p.total - p.done);

    p.runningAgents = getRunningAgents(projName, p.slug);
  }

  let updatedHtml = html.replace(scriptRegex, `const D = ${JSON.stringify(D)};\nconst $ =`);

  // Ensure render logic displays read-status & checkpoint
  if (!updatedHtml.includes('p.readStatus.label')) {
    const summaryTarget = `<span class="sub syn num">\${esc(p.commit)}\${p.sync ? " · " + esc(p.sync) : ""}</span>`;
    const summaryReplacement = `<span class="sub syn num">\${esc(p.commit)}\${p.sync ? " · " + esc(p.sync) : ""}\${p.readStatus ? \` · <span class="pill \${p.readStatus.status === "green" ? "ok" : p.readStatus.status === "amber" ? "warn" : "bad"}" style="font-size:10px;padding:1px 5px">\${esc(p.readStatus.label)}</span>\` : ""}</span>`;
    if (updatedHtml.includes(summaryTarget)) {
      updatedHtml = updatedHtml.replace(summaryTarget, summaryReplacement);
    }

    const detailTarget = `<h3>Where it stands</h3><p style="margin:0 0 8px">\${esc(p.now || "Setup is ready; no chat has started it yet.")}</p>`;
    const detailReplacement = `<h3>Where it stands</h3><p style="margin:0 0 8px">\${esc(p.now || "Setup is ready; no chat has started it yet.")}</p><div class="sub" style="margin-bottom:8px"><b>Checkpoint:</b> \${esc(p.lastCheckpoint || "n/a")} · <b>Read Log:</b> <span class="pill \${p.readStatus && p.readStatus.status === "green" ? "ok" : p.readStatus && p.readStatus.status === "amber" ? "warn" : "bad"}" style="font-size:10px;padding:1px 5px">\${esc(p.readStatus ? p.readStatus.label : "none")}</span> · <b>Open Tasks:</b> \${p.openTasks}</div>`;
    if (updatedHtml.includes(detailTarget)) {
      updatedHtml = updatedHtml.replace(detailTarget, detailReplacement);
    }
  }

  fs.writeFileSync(dashboardPath, updatedHtml, 'utf8');
  return { updatedProjects: D.projects.length, generated: D.generated };
}

function main() {
  const res = updateDashboardData();
  console.log(`Updated dashboard.html successfully (${res.updatedProjects} projects, timestamp: ${res.generated}).`);
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  main();
}
