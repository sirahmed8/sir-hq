#!/usr/bin/env node
// Helper for all agent chats to send clean, human Arabic updates to Ahmed.
// Rule (Ahmed, 2026-11-09): 2 to 4 lines, no jargon, no commit hashes, no file names.
//
// Usage:
//   node send-owner-brief.mjs "<project>" "<done>" "<next>" ["<action>"]
//
// Example:
//   node send-owner-brief.mjs "غرفة التحكم" "تم تحديث لوحة المتابعة وتأكيد عمل روابط الهاتف" "متابعة فحوصات الأمان" "لا شيء، كل الأنظمة تعمل بسلاسة"

import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const SEND_TELEGRAM = path.join(HERE, 'send-telegram.mjs');

const args = process.argv.slice(2);
if (args.length < 2) {
  console.log('Usage: node send-owner-brief.mjs "<project>" "<done>" "<next>" ["<action>"]');
  process.exit(1);
}

const project = args[0].replace(/^\[+|\]+$/g, '').trim();
const done = args[1].trim();
const next = args[2] ? args[2].trim() : 'مواصلة العمل المخطط له';
const action = args[3] ? args[3].trim() : 'لا شيء، كل شيء يعمل بسلاسة';

const message = `[${project}]
تم اليوم: ${done}.
الخطوة التالية: ${next}.
المطلوب منك: ${action}.`;

console.log('Formatting brief for Ahmed:');
console.log(message);
console.log('---');

const res = spawnSync('node', [SEND_TELEGRAM, message], {
  encoding: 'utf-8',
  stdio: 'inherit'
});

process.exit(res.status ?? 0);
