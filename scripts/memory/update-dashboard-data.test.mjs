import test from 'node:test';
import assert from 'node:assert/strict';
import {
  computeReadStatus,
  countOpenTasks,
  updateDashboardData,
  DASHBOARD_HTML,
} from './update-dashboard-data.mjs';

test('computeReadStatus returns green for today and amber/red accordingly', () => {
  const entries = [
    { time: new Date().toISOString(), project: 'SIR Study' },
    { time: '2026-10-01T00:00:00Z', project: 'Old Project' },
  ];

  const s1 = computeReadStatus(entries, 'SIR Study', 'sir-study');
  assert.equal(s1.status, 'green');
  assert.equal(s1.label, 'Read today');

  const s2 = computeReadStatus(entries, 'Unknown', 'unknown');
  assert.equal(s2.status, 'red');
  assert.equal(s2.label, 'No read log');
});

test('updateDashboardData enriches dashboard.html without syntax errors', () => {
  const res = updateDashboardData();
  assert.ok(res.updatedProjects > 0);
  assert.ok(res.generated);
});
