// Ask Ahmed for a one-tap approval on Telegram.
// Usage: node ask-approval.mjs <id> "<text in simple Arabic>"
// Sends two buttons (approve_ok:<id> / approve_no:<id>) through send-buttons.mjs.
// telegram-inbox.mjs records the answer in ops/bus/approvals.json so other chats can read it.
// The id must be unique per question (letters, digits, dot, dash, underscore; up to 50 chars,
// so approve_ok:<id> stays inside Telegram's 64-byte callback_data limit).
// Never put AHome or Habiba private content in the id or text.
import { execFileSync, spawnSync } from 'node:child_process';
import { mkdirSync, readFileSync, renameSync, writeFileSync } from 'node:fs';

const OPS = 'D:/Projects/_SIR/ops';
const APPROVALS_JSON = `${OPS}/bus/approvals.json`;
const SEND_BUTTONS = 'D:/Projects/_SIR/scripts/deliver/send-buttons.mjs';
const PRIVATE_RE = /ahome|habiba/i;

function userEnv(name) {
  if (process.env[name]) return process.env[name];
  try {
    return execFileSync('powershell', ['-NoProfile', '-Command', `[Environment]::GetEnvironmentVariable('${name}','User')`], { encoding: 'utf8', windowsHide: true }).trim();
  } catch { return ''; }
}

function readApprovals() {
  try { return JSON.parse(readFileSync(APPROVALS_JSON, 'utf8')); } catch { return []; }
}

function writeApprovals(rows) {
  mkdirSync(`${OPS}/bus`, { recursive: true });
  const tmp = APPROVALS_JSON + '.tmp';
  writeFileSync(tmp, JSON.stringify(rows, null, 2) + '\n', 'utf8');
  try { renameSync(tmp, APPROVALS_JSON); } catch { writeFileSync(APPROVALS_JSON, JSON.stringify(rows, null, 2) + '\n', 'utf8'); }
}

function upsertPending(id, text) {
  const rows = readApprovals();
  const now = new Date().toISOString();
  const existing = rows.find((row) => row && row.id === id);
  if (existing) {
    existing.text = text;
    existing.status = 'pending';
    existing.answer = null;
    existing.created_at = now;
    existing.answered_at = null;
  } else {
    rows.push({ id, text, status: 'pending', answer: null, created_at: now, answered_at: null });
  }
  writeApprovals(rows);
}

function markSendFailed(id) {
  const rows = readApprovals();
  const row = rows.find((item) => item && item.id === id);
  if (row) {
    row.status = 'send_failed';
    row.answered_at = new Date().toISOString();
    writeApprovals(rows);
  }
}

const [id, ...rest] = process.argv.slice(2);
const text = rest.join(' ').trim();
if (!id || !text || !/^[\w.-]{1,50}$/.test(id) || PRIVATE_RE.test(id) || PRIVATE_RE.test(text) || text.length > 1000) {
  console.log('usage: ask-approval.mjs <id> "<text>"  (id: letters, digits, . - _, up to 50 chars; no private names; text up to 1000 chars)');
  process.exit(2);
}

if (!userEnv('SIR_TELEGRAM_BOT_TOKEN') || !userEnv('SIR_TELEGRAM_CHAT_ID')) {
  console.log('ask-approval: SIR_TELEGRAM_BOT_TOKEN or SIR_TELEGRAM_CHAT_ID missing');
  process.exit(1);
}

upsertPending(id, text);
const sent = spawnSync(process.execPath, [SEND_BUTTONS, text, `موافق=approve_ok:${id}`, `رفض=approve_no:${id}`], {
  encoding: 'utf8',
  windowsHide: true,
  maxBuffer: 4 * 1024 * 1024,
});
if (sent.error || sent.status !== 0) {
  markSendFailed(id);
  const detail = sent.error ? sent.error.message : String(sent.stderr || sent.stdout || `exit ${sent.status}`).trim();
  console.log('ask-approval: send failed: ' + detail.slice(0, 300));
  process.exit(1);
}
console.log(sent.stdout.trim() || 'ok');
