#!/usr/bin/env node
/**
 * test-format-briefing.mjs - Unit tests for format-briefing.mjs (HQ-04)
 */

import assert from 'node:assert/strict';
import { stripEmojis, stripTechnicalDetails, parseReportToBrief, formatTelegramBrief } from './format-briefing.mjs';

console.log('Running format-briefing tests...');

// 1. Test emoji stripping
const emojiInput = '🚀 Launching SIR Platform with 100% speed! 🔥✨';
const emojiOutput = stripEmojis(emojiInput);
assert.equal(emojiOutput, 'Launching SIR Platform with 100% speed!');
console.log('✓ Emoji stripping verified');

// 2. Test technical hashes & file path stripping
const techInput = 'Commit 3a074ca and sha 43f0e5f992a83b1c pushed to D:\\Projects\\_SIR\\plans\\plan.md';
const techOutput = stripTechnicalDetails(techInput);
assert.ok(!techOutput.includes('3a074ca'), 'Should strip 7-char commit hash');
assert.ok(!techOutput.includes('43f0e5f'), 'Should strip long sha');
assert.ok(!techOutput.includes('D:\\Projects'), 'Should strip Windows file paths');
console.log('✓ Technical hashes and paths stripping verified');

// 3. Test markdown report parsing with mock content
const mockReport = `# SIR PLANNER EXECUTION REPORT: PASS 3
Session: sir-planner
Date: 2026-11-09T20:52:45+02:00

## 1. Executive Summary
Pass 3 complete across all projects. All 17 competitor studies finished and verified on disk.

## Next step (exact):
Wait for Claude Manager third review of elevated plans.

## Owner action:
لا شيء، كل الأنظمة تعمل بسلاسة.
`;

const brief = parseReportToBrief(mockReport);
assert.equal(brief.project, 'المخطط الاستراتيجي');
assert.ok(brief.done.includes('تم إكمال مرحلة التخطيط الشامل'), 'Should translate Pass 3 complete');
assert.ok(!brief.done.includes('🚀'), 'Zero emoji in brief');
assert.ok(brief.next.length > 5, 'Should extract next step');

const telegramText = formatTelegramBrief(brief);
const lines = telegramText.split('\n');
assert.ok(lines.length >= 3 && lines.length <= 4, 'Must be between 3 and 4 lines');
assert.ok(lines[0].startsWith('[المخطط الاستراتيجي]'));
console.log('✓ Canonical Telegram format verified:');
console.log(telegramText);

console.log('\nAll 3 test suites passed successfully!');
