import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { parseRoster, ensureAgentProfile, syncAllAgentProfiles } from './sync-agent-profiles.mjs';
import { addAgentAction } from './agent-note.mjs';

test('parseRoster extracts specialists from ROSTER.md', () => {
  const agents = parseRoster();
  assert.ok(agents.length >= 20);
  const builder = agents.find(a => a.name === 'builder');
  assert.ok(builder);
  assert.equal(builder.role, 'sir-builder');
});

test('ensureAgentProfile and addAgentAction work and trim to 20 actions', () => {
  const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'sir-agent-test-'));

  const created = ensureAgentProfile({
    name: 'test-agent',
    role: 'sir-test-agent',
    description: 'A test agent role',
  }, tempDir, '2026-11-08');

  assert.equal(created.created, true);
  assert.ok(fs.existsSync(created.path));

  // Add 25 actions and verify it caps at 20
  for (let i = 1; i <= 25; i++) {
    addAgentAction('test-agent', `Action number ${i}`, { agentsDir: tempDir, dateStr: '2026-11-08' });
  }

  const finalContent = fs.readFileSync(created.path, 'utf8');
  const actionLines = finalContent.match(/## Last actions([\s\S]*?)(?=\n##|$)/)[1].trim().split('\n').filter(Boolean);
  assert.equal(actionLines.length, 20);
  assert.ok(actionLines[0].includes('Action number 25'));

  fs.rmSync(tempDir, { recursive: true, force: true });
});
