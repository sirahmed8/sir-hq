// Poll Ahmed's Telegram bot for messages FROM Ahmed and print one line per message (for the Monitor tool).
// Only the chat id in SIR_TELEGRAM_CHAT_ID is accepted; everything else is ignored. Text is appended to ops/bus/ahmed-telegram.md.
// Usage: node telegram-inbox.mjs   (runs until stopped; long-polls the Bot API)
import { execFileSync } from 'node:child_process';
import { appendFileSync, existsSync, readFileSync, writeFileSync } from 'node:fs';

const OFFSET_FILE = 'D:/Projects/_SIR/ops/telegram-offset.txt';
const INBOX = 'D:/Projects/_SIR/ops/bus/ahmed-telegram.md';

function userEnv(name) {
  if (process.env[name]) return process.env[name];
  try {
    return execFileSync('powershell', ['-NoProfile', '-Command', `[Environment]::GetEnvironmentVariable('${name}','User')`], { encoding: 'utf8' }).trim();
  } catch { return ''; }
}

const token = userEnv('SIR_TELEGRAM_BOT_TOKEN');
const chatId = userEnv('SIR_TELEGRAM_CHAT_ID');
if (!token || !chatId) { console.log('telegram-inbox: token or chat id missing'); process.exit(1); }

let offset = existsSync(OFFSET_FILE) ? Number(readFileSync(OFFSET_FILE, 'utf8')) || 0 : 0;

async function poll() {
  const url = `https://api.telegram.org/bot${token}/getUpdates?timeout=50&offset=${offset}&allowed_updates=%5B%22message%22%5D`;
  const res = await fetch(url);
  const data = await res.json();
  if (!data.ok) throw new Error('getUpdates failed: ' + (data.description || res.status));
  for (const u of data.result) {
    offset = u.update_id + 1;
    writeFileSync(OFFSET_FILE, String(offset));
    const m = u.message;
    if (!m || String(m.chat?.id) !== String(chatId)) continue;
    const text = (m.text || m.caption || (m.voice ? '[voice message]' : m.photo ? '[photo]' : m.document ? '[file ' + (m.document.file_name || '') + ']' : '[unsupported message]')).replace(/\s+/g, ' ').trim();
    const stamp = new Date(m.date * 1000).toISOString();
    appendFileSync(INBOX, `- ${stamp} from Ahmed (Telegram): ${text}\n`);
    console.log(`AHMED (Telegram ${stamp}): ${text}`);
    if (/^\/status/i.test(text)) {
      try {
        const brief = execFileSync('python', ['D:/Projects/_SIR/scripts/deliver/status-brief.py'], { encoding: 'utf8', timeout: 90000 });
        execFileSync('node', ['D:/Projects/_SIR/scripts/deliver/send-telegram.mjs', brief], { encoding: 'utf8' });
      } catch (e) { console.log('status reply failed: ' + e.message); }
    }
  }
}

for (;;) {
  try { await poll(); } catch (e) { console.log('telegram-inbox error: ' + e.message); await new Promise(r => setTimeout(r, 15000)); }
}
