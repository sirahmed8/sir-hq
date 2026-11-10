// Send a Telegram message with tap buttons to Ahmed.
// Usage: node send-buttons.mjs "<text>" "<label>=<action>" ["<label>=<action>" ...]   (two buttons per row)
// A tap is received by telegram-inbox.mjs, which runs the action named in ops/telegram-actions.json.
import { execFileSync } from 'node:child_process';

function userEnv(name) {
  if (process.env[name]) return process.env[name];
  try {
    return execFileSync('powershell', ['-NoProfile', '-Command', `[Environment]::GetEnvironmentVariable('${name}','User')`], { encoding: 'utf8', windowsHide: true }).trim();
  } catch { return ''; }
}
const [text, ...pairs] = process.argv.slice(2);
const token = userEnv('SIR_TELEGRAM_BOT_TOKEN');
const chatId = userEnv('SIR_TELEGRAM_CHAT_ID');
if (!token || !chatId || !text) { console.log('usage: send-buttons.mjs "<text>" "<label>=<action>" ...'); process.exit(2); }
const rows = [];
for (let i = 0; i < pairs.length; i += 2) {
  rows.push(pairs.slice(i, i + 2).map(p => { const k = p.lastIndexOf('='); return { text: p.slice(0, k), callback_data: p.slice(k + 1) }; }));
}
const res = await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
  method: 'POST', headers: { 'content-type': 'application/json' },
  body: JSON.stringify({ chat_id: chatId, text, reply_markup: { inline_keyboard: rows } }),
});
const data = await res.json();
console.log(data.ok ? 'ok' : 'failed: ' + JSON.stringify(data));
process.exit(data.ok ? 0 : 1);
