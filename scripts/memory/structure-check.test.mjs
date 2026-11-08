import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {
  checkProject,
  checkManagerState,
  checkReadLog,
  checkAgentsProfiles,
  runStructureCheck,
  HEALTH_REPORT_MD,
  HEALTH_JSON,
} from './structure-check.mjs';

test('checkProject checks existing project and detects missing/zero-byte files', () => {
  const result = checkProject('D:/Projects/SIR Negm Furniture');
  assert.equal(result.name, 'SIR Negm Furniture');
  // Check no zero-byte files
  assert.ok(!result.fileIssues.some(f => f.issue === 'zero_byte'));
});

test('checkManagerState verifies freshness', () => {
  const m = checkManagerState();
  assert.ok(['GREEN', 'AMBER', 'RED'].includes(m.status));
  assert.ok(m.managerState.exists);
});

test('checkReadLog returns logged count and status', () => {
  const r = checkReadLog();
  assert.ok(r.count > 0);
  assert.equal(r.status, 'GREEN');
});

test('checkAgentsProfiles verifies roster agents are present', () => {
  const a = checkAgentsProfiles();
  assert.equal(a.status, 'GREEN');
  assert.equal(a.missing.length, 0);
  assert.equal(a.empty.length, 0);
});

test('runStructureCheck writes HEALTH_REPORT.md and health.json', () => {
  const data = runStructureCheck();
  assert.ok(fs.existsSync(HEALTH_REPORT_MD));
  assert.ok(fs.existsSync(HEALTH_JSON));
  assert.ok(data.projects.length >= 16);
});
