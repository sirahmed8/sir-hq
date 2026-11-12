// Poll Ahmed's Telegram bot for messages and button presses FROM Ahmed.
// Only the chat id in SIR_TELEGRAM_CHAT_ID is accepted. Text and button presses are appended to ops/bus/ahmed-telegram.md.
// Buttons:
//   - callback_data "<action>" runs ops/telegram-actions.json[action] = {cmd:[...], reply:"text"}.
//   - callback_data "ok:<id>" or "no:<id>" records an approval answer in ops/approvals.jsonl (read by scripts/deliver/approval.py).
// After a press the buttons are removed from the message, so one message is answered once.
// One instance only: the pid is written to ops/telegram-listener.pid (hq_autopilot.py restarts it when it dies).
// Usage: node telegram-inbox.mjs   (runs until stopped; long-polls the Bot API)
import { execFile, execFileSync, spawn } from 'node:child_process';
import { appendFileSync, existsSync, readFileSync, writeFileSync, renameSync, mkdirSync } from 'node:fs';

const OPS = 'D:/Projects/_SIR/ops';
const OFFSET_FILE = `${OPS}/telegram-offset.txt`;
const INBOX = `${OPS}/bus/ahmed-telegram.md`;
const ACTIONS = `${OPS}/telegram-actions.json`;
const APPROVALS = `${OPS}/approvals.jsonl`;
const APPROVALS_JSON = `${OPS}/bus/approvals.json`;
const PID_FILE = `${OPS}/telegram-listener.pid`;
const GAME_SNAPSHOT = 'D:/Projects/SIR Laptop Manager/.sir/game_mode_snapshot.json';
const SEND = 'D:/Projects/_SIR/scripts/deliver/send-telegram.mjs';
const SEND_BUTTONS = 'D:/Projects/_SIR/scripts/deliver/send-buttons.mjs';
const MENU = ['[الإدارة] اختار:', 'الحالة=status', 'تنضيف المساحة=clean_disk', 'إطفاء الألعاب=game_off', 'استلام المدير الاحتياطي=takeover', 'رجوع لكلود=handback'];
// Backup manager (owner, 2026-11-12): while on, every message goes to scripts/backup_manager.py (see ops/BACKUP_MANAGER.md)
let lastIdleNote = 0;
const BM_STATE = `${OPS}/backup-manager.json`;
const BM_DIR = `${OPS}/backup-manager`;
const BM_SCRIPT = 'D:/Projects/_SIR/scripts/backup_manager.py';
function bmActive() { try { return !!JSON.parse(readFileSync(BM_STATE, 'utf8')).active; } catch { return false; } }
function bmSet(active) { writeFileSync(BM_STATE, JSON.stringify({ active, since: new Date().toISOString() })); }
function bmDispatch(payload) {
  mkdirSync(BM_DIR, { recursive: true });
  const file = `${BM_DIR}/in-${payload.id}.json`;
  writeFileSync(file, JSON.stringify(payload));
  const child = spawn('python', [BM_SCRIPT, file], { detached: true, stdio: 'ignore', windowsHide: true,
    env: { ...process.env, SIR_TELEGRAM_BOT_TOKEN: token, SIR_TELEGRAM_CHAT_ID: chatId, PYTHONUTF8: '1' } });
  child.unref();
}
async function takeover(on) {
  bmSet(on);
  if (on) {
    await sendText('[المدير الاحتياطي] استلمت. من دلوقتي كلمني هنا (كتابة، فويس، صور) وأنا بكمل من مكان كلود وبوزع المهام وبتابع. للرجوع لكلود ابعت /handback.');
    bmDispatch({ id: `takeover-${Date.now()}`, kind: 'text', text: 'Ahmed switched you on as the manager. Read the checkpoints and the queue, tell him the current state in a few lines, and continue the HQ duty.' });
  } else await sendText('[المدير الاحتياطي] رجعت الإدارة لكلود. الرسائل هتتسجل بس لحد ما كلود يقراها.');
}

function userEnv(name) {
  if (process.env[name]) return process.env[name];
  try {
    return execFileSync('powershell', ['-NoProfile', '-Command', `[Environment]::GetEnvironmentVariable('${name}','User')`], { encoding: 'utf8', windowsHide: true }).trim();
  } catch { return ''; }
}

const token = userEnv('SIR_TELEGRAM_BOT_TOKEN');
const chatId = userEnv('SIR_TELEGRAM_CHAT_ID');
if (!token || !chatId) { console.log('telegram-inbox: token or chat id missing'); process.exit(1); }
writeFileSync(PID_FILE, String(process.pid));

let offset = existsSync(OFFSET_FILE) ? Number(readFileSync(OFFSET_FILE, 'utf8')) || 0 : 0;
const running = new Set(); // actions in progress, so a double tap does not start the same command twice

async function api(method, body) {
  const res = await fetch(`https://api.telegram.org/bot${token}/${method}`, {
    method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body || {}),
  });
  return res.json();
}

function run(file, args, timeout = 60000) {
  return new Promise((resolve) => {
    execFile(file, args, { encoding: 'utf8', timeout, windowsHide: true, maxBuffer: 4 * 1024 * 1024, env: { ...process.env, PYTHONUTF8: '1' } },
      (err, stdout) => resolve({ err, out: String(stdout || '').trim() }));
  });
}

async function sendText(text) {
  const { err } = await run('node', [SEND, text]);
  if (err) console.log('send failed: ' + err.message);
}

function loadActions() {
  try { return JSON.parse(readFileSync(ACTIONS, 'utf8')); } catch { return {}; }
}

async function runAction(name, msgText = '') {
  const def = loadActions()[name];
  if (!def || !Array.isArray(def.cmd)) {
    // no fixed command for this button: the AI manager decides what it means and does it (owner order 2026-11-12)
    bmDispatch({ id: `btn-${Date.now()}`, kind: 'text', text: `Ahmed pressed the Telegram button "${name}" on this message of yours: "${String(msgText).slice(0, 600)}". Work out what the button means and do it (for example record that he exercised in the health log, move or cancel the reminder, mark the task, adjust the next reminder), then answer him in one short line.` });
    return;
  }
  if (running.has(name)) { await sendText('[الإدارة] الأمر ده شغال دلوقتي، استنى لما يخلص.'); return; }
  running.add(name);
  try {
    const { err, out } = await run(def.cmd[0], def.cmd.slice(1), 600000);
    if (err) await sendText(`[الإدارة] فشل تنفيذ "${name}": ${String(err.message).slice(0, 200)}`);
    else await sendText(def.reply ? def.reply : (out ? out.slice(0, 1500) : `[الإدارة] تم تنفيذ: ${name}`));
  } finally { running.delete(name); }
}

function readApprovals() {
  try { return JSON.parse(readFileSync(APPROVALS_JSON, 'utf8')); } catch { return []; }
}

function isExpired(row) {
  if (!row || !row.created_at) return true;
  const created = new Date(row.created_at);
  const now = new Date();
  const ageHours = (now - created) / (1000 * 60 * 60);
  return ageHours > 24;
}

// Returns 'ok' when the answer was recorded, otherwise the rejection reason.
// Only ids registered as pending in approvals.json, younger than 24 h and not
// yet answered are accepted; anything else (forged, stale or replayed ids) is ignored.
function recordApproval(id, answer) {
  const rows = readApprovals();
  const now = new Date().toISOString();
  const existing = rows.find((row) => row && row.id === id);
  if (!existing) {
    console.log(`Approval ${id} not registered, ignoring`);
    return 'unknown';
  }
  if (existing.status === 'approved' || existing.status === 'rejected' || existing.answered_at && existing.answer) {
    console.log(`Approval ${id} already answered, ignoring`);
    return 'answered';
  }
  if (existing.status !== 'pending' || isExpired(existing)) {
    console.log(`Approval ${id} expired or not pending, ignoring`);
    return 'expired';
  }
  existing.answer = answer;
  existing.status = answer;
  existing.answered_at = now;
  const tmp = APPROVALS_JSON + '.tmp';
  writeFileSync(tmp, JSON.stringify(rows, null, 2) + '\n', 'utf8');
  try { renameSync(tmp, APPROVALS_JSON); } catch { writeFileSync(APPROVALS_JSON, JSON.stringify(rows, null, 2) + '\n', 'utf8'); }
  return 'ok';
}

async function handleButton(cq) {
  if (String(cq.message?.chat?.id) !== String(chatId) || String(cq.from?.id) !== String(chatId)) return;
  const data = String(cq.data || '').slice(0, 80);
  appendFileSync(INBOX, `- ${new Date().toISOString()} from Ahmed (Telegram button): ${data}\n`);
  console.log(`AHMED BUTTON: ${data}`);
  // remove the buttons so the same message cannot be answered twice
  await api('editMessageReplyMarkup', { chat_id: chatId, message_id: cq.message.message_id, reply_markup: { inline_keyboard: [] } });
  const approval = /^(ok|no):([\w.-]{1,60})$/.exec(data);
  if (approval) {
    const answer = approval[1] === 'ok' ? 'approved' : 'rejected';
    const result = recordApproval(approval[2], answer);
    if (result === 'ok') {
      appendFileSync(APPROVALS, JSON.stringify({ id: approval[2], answer, at: new Date().toISOString() }) + '\n');
      await api('answerCallbackQuery', { callback_query_id: cq.id, text: answer === 'approved' ? 'تمت الموافقة' : 'تم الرفض' });
      await sendText(answer === 'approved' ? '[الإدارة] تم تسجيل موافقتك.' : '[الإدارة] تم تسجيل رفضك، ومش هيتنفذ.');
    } else {
      await api('answerCallbackQuery', { callback_query_id: cq.id, text: 'الطلب ده مش موجود أو انتهت صلاحيته' });
    }
    return;
  }
  const appApproval = /^(approve_ok|approve_no):([\w.-]{1,50})$/.exec(data);
  if (appApproval) {
    const answer = appApproval[1] === 'approve_ok' ? 'approved' : 'rejected';
    const result = recordApproval(appApproval[2], answer);
    if (result === 'ok') {
      await api('answerCallbackQuery', { callback_query_id: cq.id, text: answer === 'approved' ? 'تمت الموافقة' : 'تم الرفض' });
      await sendText(answer === 'approved' ? '[الإدارة] تم تسجيل موافقتك.' : '[الإدارة] تم تسجيل رفضك، ومش هيتنفذ.');
    } else {
      await api('answerCallbackQuery', { callback_query_id: cq.id, text: 'الطلب ده مش موجود أو انتهت صلاحيته' });
    }
    return;
  }

  // Apply pipeline: a_<jobId> = apply, s_<jobId> = skip
  const applyMatch = /^a_([\w.-]{1,50})$/.exec(data);
  if (applyMatch) {
    const jobId = applyMatch[1];
    await api('answerCallbackQuery', { callback_query_id: cq.id, text: 'جاري التقديم...' });
    run('node', ['D:/Projects/SIR Jobs/scripts/apply/handler.mjs', 'apply', jobId], 180000);
    return;
  }

  const skipMatch = /^s_([\w.-]{1,50})$/.exec(data);
  if (skipMatch) {
    const jobId = skipMatch[1];
    await api('answerCallbackQuery', { callback_query_id: cq.id, text: 'تم التخطي' });
    run('node', ['D:/Projects/SIR Jobs/scripts/apply/handler.mjs', 'skip', jobId], 60000);
    return;
  }

  // Reply pipeline: reply_<threadId> = send suggested reply
  const replyMatch = /^reply_([\w.-]{1,50})$/.exec(data);
  if (replyMatch) {
    const threadId = replyMatch[1];
    await api('answerCallbackQuery', { callback_query_id: cq.id, text: 'جاري الإرسال...' });
    run('node', ['D:/Projects/SIR Jobs/scripts/apply/reply-handler.mjs', threadId], 60000);
    return;
  }

  if (data === 'takeover' || data === 'handback') { await api('answerCallbackQuery', { callback_query_id: cq.id, text: 'تمام' }); await takeover(data === 'takeover'); return; }
  await api('answerCallbackQuery', { callback_query_id: cq.id, text: 'تمام، بنفذ' });
  runAction(data, cq.message?.text || ''); // not awaited: polling continues while the command runs
}

async function poll() {
  const url = `https://api.telegram.org/bot${token}/getUpdates?timeout=50&offset=${offset}&allowed_updates=%5B%22message%22%2C%22callback_query%22%5D`;
  const res = await fetch(url);
  const data = await res.json();
  if (!data.ok) throw new Error('getUpdates failed: ' + (data.description || res.status));
  for (const u of data.result) {
    offset = u.update_id + 1;
    writeFileSync(OFFSET_FILE, String(offset));
    if (u.callback_query) { await handleButton(u.callback_query); continue; }
    const m = u.message;
    if (!m || String(m.chat?.id) !== String(chatId)) continue;
    const text = (m.text || m.caption || (m.voice ? '[voice message]' : m.photo ? '[photo]' : m.document ? '[file ' + (m.document.file_name || '') + ']' : '[unsupported message]')).replace(/\s+/g, ' ').trim();
    const stamp = new Date(m.date * 1000).toISOString();
    appendFileSync(INBOX, `- ${stamp} from Ahmed (Telegram): ${text}\n`);
    console.log(`AHMED (Telegram ${stamp}): ${text}`);
    if (/^\/(takeover|manager)|^(استلم|المدير الاحتياطي|كمل انت|كمّل انت)\s*$/i.test(text)) await takeover(true);
    else if (/^\/handback|^(رجع الإدارة لكلود|رجوع لكلود)\s*$/i.test(text)) await takeover(false);
    else if (/^\/status/i.test(text)) runAction('status');
    else if (/^\/queue/i.test(text)) runAction('queue');
    else if (/^\/(menu|start|help)/i.test(text)) {
      const { err } = await run('node', [SEND_BUTTONS, ...MENU]);
      if (err) console.log('menu failed: ' + err.message);
    } else if (!bmActive() && (m.text || m.voice || m.photo) && Date.now() - lastIdleNote > 3600000) {
      lastIdleNote = Date.now();
      await sendText('[الإدارة] وصلتني رسالتك وهي متسجلة. كلود هو المدير دلوقتي. لو عايز المدير الاحتياطي (الأدوات المجانية) يرد عليك ابعت /takeover.');
    } else if (bmActive()) {
      const kind = m.voice || m.audio ? 'voice' : m.photo ? 'photo' : m.document ? 'document' : 'text';
      const fileId = m.voice?.file_id || m.audio?.file_id || (m.photo ? m.photo[m.photo.length - 1].file_id : '') || m.document?.file_id || '';
      if (kind === 'text' && !m.text) await sendText('[المدير الاحتياطي] النوع ده من الرسايل مش مدعوم، ابعت كتابة أو فويس أو صورة.');
      else bmDispatch({ id: `${u.update_id}`, kind, text: m.text || m.caption || '', file_id: fileId, file_name: m.document?.file_name || '' });
    }
  }
}

for (;;) {
  // A game is running (SIR game-mode marker): pause polling. Messages queue on
  // Telegram's servers and are picked up when the game ends. Alerts still send.
  if (existsSync(GAME_SNAPSHOT)) { await new Promise(r => setTimeout(r, 30000)); continue; }
  try { await poll(); } catch (e) { console.log('telegram-inbox error: ' + e.message); await new Promise(r => setTimeout(r, 15000)); }
}
