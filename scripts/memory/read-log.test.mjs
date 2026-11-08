import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import {
  extractNextStep,
  extractFilesRead,
  appendReadLog,
  parseReadLog,
  verifyTodaySessions
} from './read-log.mjs';

test('extractNextStep extracts correctly from checkpoint formats', () => {
  const cp1 = '## Status\nActive\n\nNext step: Implement M2 read-log\n\n## History';
  assert.equal(extractNextStep(cp1), 'Implement M2 read-log');

  const cp2 = '### Next step\nRun test suite and verify';
  assert.equal(extractNextStep(cp2), 'Run test suite and verify');

  const cp3 = 'No clear markers here';
  assert.equal(extractNextStep(cp3), 'Continue task');
});

test('extractFilesRead rejects prose, paragraphs and runaway text after Re-read reset', () => {
  const cpWithProse = `## Current state
Working on memory system.

Re-read after a reset:
- _SIR/START_ANY_AI.md
- AGENTS.md

This is an unheaded paragraph that contains narrative prose about the project.
It mentions various things, sentences with spaces, and should NEVER be captured as files!
`;
  const files = extractFilesRead(cpWithProse, { mode: 'hq' });
  const fileNames = files.map(f => f.split('@')[0]);
  assert.ok(fileNames.includes('AGENTS.md'));
  assert.ok(fileNames.includes('_SIR/START_ANY_AI.md'));
  // None of the words from the prose paragraph should be in files
  assert.ok(!fileNames.some(f => f.includes('unheaded') || f.includes('narrative') || f.includes('paragraph')));
});

test('appendReadLog and parseReadLog work end-to-end', () => {
  const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'sir-read-log-'));
  const logFile = path.join(tempDir, 'READ_LOG.md');

  const line1 = appendReadLog({
    time: '2026-11-08T10:00:00Z',
    tool: 'claude-code',
    agent: 'pm',
    project: 'HQ',
    filesRead: ['AGENTS.md@2026-11-08'],
    nextStep: 'Initial step',
  }, logFile);

  assert.ok(line1.includes('2026-11-08T10:00:00Z | claude-code | pm | HQ | AGENTS.md@2026-11-08 | Initial step'));

  const parsed = parseReadLog(logFile);
  assert.equal(parsed.length, 1);
  assert.equal(parsed[0].agent, 'pm');
  assert.equal(parsed[0].project, 'HQ');
  assert.equal(parsed[0].nextStep, 'Initial step');

  fs.rmSync(tempDir, { recursive: true, force: true });
});

test('verifyTodaySessions passes with clean log and ignores idle roster stubs', () => {
  const result = verifyTodaySessions();
  assert.equal(typeof result.today, 'string');
  assert.equal(typeof result.todayEntriesCount, 'number');
  assert.ok(result.todayEntriesCount > 0);
  assert.equal(result.unverified.length, 0, 'Clean log should produce 0 unverified sessions');
});

test('verifyTodaySessions catches unlogged active agents while ignoring idle stubs', () => {
  const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'sir-verify-test-'));
  const emptyLog = path.join(tempDir, 'EMPTY_READ_LOG.md');
  fs.writeFileSync(emptyLog, '# READ LOG\n\n', 'utf8');

  const result = verifyTodaySessions(emptyLog);
  // Idle stubs should NOT be flagged
  const idleStubsFlagged = result.unverified.filter(u =>
    ['ai-engineer', 'architect-refactor', 'backend-dev'].includes(u.agent)
  );
  assert.equal(idleStubsFlagged.length, 0, 'Idle stubs must never be flagged as unverified');

  // Active agents (like builder, reviewer, or pm who modified their profile with real actions today) SHOULD be caught
  assert.ok(result.unverified.length > 0, 'Unlogged active agents should be detected');
  const agentsFlagged = result.unverified.map(u => u.agent || u.project);
  assert.ok(agentsFlagged.includes('builder') || agentsFlagged.includes('reviewer') || agentsFlagged.includes('pm') || agentsFlagged.includes('HQ'));

  fs.rmSync(tempDir, { recursive: true, force: true });
});
