#!/usr/bin/env node
// Helper to append an action note to an agent's ops/agents/<name>.md and trim to 20 actions.
// Spec: _SIR/plans/MEMORY_AND_SYNC_SYSTEM.md section 1 & M3 brief.
// Usage: node agent-note.mjs <name> "<action text>"
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { SIR_ROOT } from './lib.mjs';

export const AGENTS_DIR = path.join(SIR_ROOT, 'ops', 'agents');
const MAX_ACTIONS = 20;

export function addAgentAction(name, actionText, { agentsDir = AGENTS_DIR, dateStr = new Date().toISOString().slice(0, 10) } = {}) {
  const filePath = path.join(agentsDir, `${name}.md`);
  if (!fs.existsSync(filePath)) {
    throw new Error(`Agent profile not found: ${filePath}`);
  }

  const content = fs.readFileSync(filePath, 'utf8');
  const actionRegex = /## Last actions([\s\S]*?)(?=\n##|$)/i;
  const match = content.match(actionRegex);

  if (!match) {
    throw new Error(`"## Last actions" section not found in ${filePath}`);
  }

  const existingRaw = match[1].trim();
  const existingLines = existingRaw
    ? existingRaw.split('\n').map(l => l.trim()).filter(l => l.startsWith('-') || l.startsWith('*'))
    : [];

  const newAction = `- ${dateStr} ${actionText.trim()}`;
  // Add new action at the top of the action list
  const updatedLines = [newAction, ...existingLines].slice(0, MAX_ACTIONS);

  const replacement = `## Last actions\n${updatedLines.join('\n')}\n`;
  const updatedContent = content.replace(actionRegex, replacement.trim());

  fs.writeFileSync(filePath, updatedContent.trim() + '\n', 'utf8');
  return { path: filePath, actionCount: updatedLines.length, added: newAction };
}

function main() {
  const args = process.argv.slice(2);
  if (args.length < 2) {
    console.error('Usage: node agent-note.mjs <name> "<action>"');
    process.exit(1);
  }

  const [name, ...actionParts] = args;
  const action = actionParts.join(' ');

  try {
    const res = addAgentAction(name, action);
    console.log(`Updated ${res.path} (${res.actionCount} actions recorded). Added: ${res.added}`);
  } catch (err) {
    console.error(`Error: ${err.message}`);
    process.exit(1);
  }
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  main();
}
