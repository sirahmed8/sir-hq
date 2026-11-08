import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import {
  getExpectedContent,
  inspectProjectPointers,
  writeProjectPointers,
  runSync,
  MARKER
} from './sync-agent-files.mjs';

test('getExpectedContent contains marker and canonical instruction', () => {
  const claude = getExpectedContent('CLAUDE.md');
  assert.ok(claude.includes(MARKER));
  assert.ok(claude.includes('@AGENTS.md'));
  assert.ok(claude.includes('Read AGENTS.md completely first, then .sir/CHECKPOINT.md.'));

  const gemini = getExpectedContent('GEMINI.md');
  assert.ok(gemini.includes(MARKER));
  assert.ok(gemini.includes('Read AGENTS.md completely first, then .sir/CHECKPOINT.md.'));
});

test('inspectProjectPointers detects missing and divergent files in a temp project', () => {
  const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'sir-test-proj-'));
  fs.mkdirSync(path.join(tempDir, '.sir'), { recursive: true });
  fs.writeFileSync(path.join(tempDir, 'AGENTS.md'), '# Test Project Agents\n');

  // Both CLAUDE.md and GEMINI.md missing initially
  let issues = inspectProjectPointers(tempDir);
  assert.equal(issues.length, 2);
  assert.equal(issues[0].type, 'missing');
  assert.equal(issues[1].type, 'missing');

  // Create divergent CLAUDE.md
  fs.writeFileSync(path.join(tempDir, 'CLAUDE.md'), '# Divergent rules\nDo something else.\n');
  issues = inspectProjectPointers(tempDir);
  const claudeIssue = issues.find(i => i.path.endsWith('CLAUDE.md'));
  assert.ok(claudeIssue);
  assert.equal(claudeIssue.type, 'divergent');

  // Write pointers
  const actions = writeProjectPointers(tempDir, false);
  assert.equal(actions.length, 2);

  // Re-inspect: now zero issues
  issues = inspectProjectPointers(tempDir);
  assert.equal(issues.length, 0);

  // Check backup created for divergent file
  const backupDir = path.join(tempDir, '.sir', 'backups', 'agent-pointers');
  assert.ok(fs.existsSync(backupDir));
  const backups = fs.readdirSync(backupDir);
  assert.ok(backups.length > 0);

  // Cleanup
  fs.rmSync(tempDir, { recursive: true, force: true });
});

test('runSync works with custom workspace in dry-run and write modes', () => {
  const tempWs = fs.mkdtempSync(path.join(os.tmpdir(), 'sir-test-ws-'));
  const projA = path.join(tempWs, 'ProjA');
  fs.mkdirSync(path.join(projA, '.sir'), { recursive: true });
  fs.writeFileSync(path.join(projA, 'AGENTS.md'), '# ProjA\n');

  // Dry run
  const dryRes = runSync({ workspace: tempWs, check: false, write: false });
  assert.equal(dryRes.projectsCount, 1);
  assert.equal(dryRes.totalIssues, 2);

  // Write
  const writeRes = runSync({ workspace: tempWs, write: true });
  assert.equal(writeRes.totalIssues, 2);

  // Check mode: should pass now
  const checkRes = runSync({ workspace: tempWs, check: true });
  assert.equal(checkRes.totalIssues, 0);

  fs.rmSync(tempWs, { recursive: true, force: true });
});
