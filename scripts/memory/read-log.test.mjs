import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import {
  extractNextStep,
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

test('verifyTodaySessions returns status', () => {
  const result = verifyTodaySessions();
  assert.ok(typeof result.today === 'string');
  assert.ok(Array.isArray(result.unverified));
});
