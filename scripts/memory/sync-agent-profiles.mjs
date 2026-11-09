#!/usr/bin/env node
// Generates and syncs ops/agents/<name>.md for every agent in ROSTER.md plus pm.
// Preserves existing actions, lessons, and current tasks.
// Spec: _SIR/plans/MEMORY_AND_SYNC_SYSTEM.md section 1 & M3 brief.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { SIR_ROOT } from './lib.mjs';

export const ROSTER_FILE = path.join(SIR_ROOT, 'standard', 'roles', 'ROSTER.md');
export const AGENTS_DIR = path.join(SIR_ROOT, 'ops', 'agents');

export function parseRoster(rosterPath = ROSTER_FILE) {
  if (!fs.existsSync(rosterPath)) return [];
  const content = fs.readFileSync(rosterPath, 'utf8');
  const lines = content.split('\n');
  const agents = [];

  for (const l of lines) {
    const trimmed = l.trim();
    if (!trimmed.startsWith('|') || trimmed.includes('| Specialist |') || trimmed.includes('|---|')) continue;
    const parts = trimmed.split('|').map(p => p.trim()).filter(Boolean);
    if (parts.length >= 3) {
      agents.push({
        name: parts[0],
        role: parts[1],
        description: parts[2],
      });
    }
  }
  return agents;
}

export function getDefaultModel(name) {
  if (name === 'pm') return 'Claude Sonnet 5.5 (Manager & Reviewer)';
  if (['reviewer', 'architect', 'security-auditor', 'security-shield-auditor'].includes(name)) {
    return 'Claude Sonnet / Gemini Pro (High thinking)';
  }
  if (['explorer', 'scout', 'growth-operator', 'seo-specialist'].includes(name)) {
    return 'Claude Haiku / Gemini Flash (Fast/Bulk)';
  }
  return 'Gemini 3.8 Flash / Antigravity (Standard)';
}

export function ensureAgentProfile(agent, agentsDir = AGENTS_DIR, today = new Date().toISOString().slice(0, 10)) {
  fs.mkdirSync(agentsDir, { recursive: true });
  const filePath = path.join(agentsDir, `${agent.name}.md`);

  if (fs.existsSync(filePath)) {
    return { name: agent.name, path: filePath, created: false };
  }

  const model = getDefaultModel(agent.name);
  const content = `# ${agent.name} (specialist, ${model})
Role: ${agent.description}

## Current task
Idle / Ready for assignment.

## Last actions
- ${today} Initialized agent profile.

## Lessons
- Follow AGENTS.md, weak-model playbook, and verify before completion.

## Owes
- None.
`;

  fs.writeFileSync(filePath, content, 'utf8');
  return { name: agent.name, path: filePath, created: true };
}

export function syncAllAgentProfiles({ rosterPath = ROSTER_FILE, agentsDir = AGENTS_DIR } = {}) {
  const agents = parseRoster(rosterPath);
  // Ensure pm is included
  if (!agents.some(a => a.name === 'pm')) {
    agents.unshift({
      name: 'pm',
      role: 'sir-pm',
      description: 'Manager: runs the company under Ahmed; plans, assigns, reviews.',
    });
  }

  const results = [];
  for (const a of agents) {
    results.push(ensureAgentProfile(a, agentsDir));
  }
  return results;
}

function main() {
  const res = syncAllAgentProfiles();
  console.log(`sync-agent-profiles: processed ${res.length} agents in ${AGENTS_DIR}`);
  const created = res.filter(r => r.created);
  console.log(`Created ${created.length} new profiles. ${res.length - created.length} existing profiles preserved.`);
  for (const c of created) {
    console.log(`  + ${c.name} -> ${c.path}`);
  }
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  main();
}
