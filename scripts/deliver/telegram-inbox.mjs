// Poll Ahmed's Telegram bot for messages and button presses FROM Ahmed.
// Only the chat id in SIR_TELEGRAM_CHAT_ID is accepted. Text and button presses are appended to ops/bus/ahmed-telegram.md.
// Buttons:
//   - callback_data "<action>" runs ops/telegram-actions.json[action] = {cmd:[...], reply:"text"}.
//   - callback_data "ok:<id>" or "no:<id>" records an approval answer in ops/approvals.jsonl (read by scripts/deliver/approval.py).
//   - any other callback_data is routed to the backup manager AI (it decides the buttons, r64).
// After a press the buttons are removed from the message, so one message is answered once.
// One instance only: the pid is written to ops/telegram-listener.pid (hq_autopilot.py restarts it when it dies).
//
// Backup manager mode (ops/backup-manager.json active):
//   Incoming messages are collected into ONE burst job: an 8 second debounce after the
//   last message groups text + voice + photos (+ media_group_id albums) so the manager
//   sees everything together. The queue survives restarts (ops/backup-manager/queue.json).
//   While a job runs, new messages wait in the queue and start the next job when it ends.
//   Ack is instant (reaction + typing) so Ahmed always sees the bot is alive.
// Usage: node telegram-inbox.mjs   (runs until stopped; long-polls the Bot API)
import { execFile, execFileSync, spawn } from 'node:child_process';
import { appendFileSync, existsSync, readFileSync, writeFileSync, renameSync, mkdirSync, unlinkSync } from 'node:fs';
import { TelegramBot } from '../telegram_lib.mjs';

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
const BM_STATE = `${OPS}/backup-manager.json`;
const BM_DIR = `${OPS}/backup-manager`;
const BM_SCRIPT = 'D:/Projects/_SIR/scripts/backup_manager.py';
const BM_QUEUE = `${BM_DIR}/queue.json`;
const BM_JOB = `${BM_DIR}/job.json`;
const BM_STAGE = `${BM_DIR}/job-state.json`;
const BURST_MS = 8000;          // one context per burst: 8 s after the last message
const WATCHDOG_MS = 3 * 60 * 1000; // warn Ahmed if a job runs longer than 3 minutes

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

const tg = new TelegramBot({ token, chatId });

function bmActive() { try { return !!JSON.parse(readFileSync(BM_STATE, 'utf8')).active; } catch { return false; } }
function bmSet(active) {
  // atomic write: a half-written state file must never flip the mode by accident
  const tmp = BM_STATE + '.tmp';
  writeFileSync(tmp, JSON.stringify({ active, since: new Date().toISOString() }));
  renameSync(tmp, BM_STATE);
}

// ---------- backup-manager queue (restart safe) ----------
function loadJson(file, fallback) { try { return JSON.parse(readFileSync(file, 'utf8')); } catch { return fallback; } }
function saveJson(file, data) {
  mkdirSync(BM_DIR, { recursive: true });
  const tmp = file + '.tmp';
  writeFileSync(tmp, JSON.stringify(data));
  renameSync(tmp, file);
}
function loadQueue() { return loadJson(BM_QUEUE, { items: [] }); }
function saveQueue(q) { saveJson(BM_QUEUE, q); }

let flushTimer = null;
let jobChild = null;      // ChildProcess of the running backup_manager.py, if we spawned it
let jobInfo = null;       // {pid, startedAt, count}
let watchdogTimer = null;
let lastIdleNote = 0;

function bmEnqueue(item) {
  const q = loadQueue();
  q.items.push(item);
  q.updatedAt = new Date().toISOString();
  saveQueue(q);
  // instant ack: reaction + typing so Ahmed sees the bot heard him (< 2 s)
  if (item.message_id) tg.setMessageReaction(item.message_id, '👍').catch(() => {});
  tg.sendChatAction('typing').catch(() => {});
  if (!jobInfo) scheduleFlush(BURST_MS);
}

function scheduleFlush(ms) {
  if (flushTimer) clearTimeout(flushTimer);
  flushTimer = setTimeout(flushQueue, ms);
  flushTimer.unref?.();
}

function flushQueue() {
  flushTimer = null;
  if (jobInfo) return; // a job is running; exit handler will reschedule
  const q = loadQueue();
  if (!q.items.length) return;
  const items = q.items.splice(0, q.items.length);
  saveQueue(q);
  mkdirSync(BM_DIR, { recursive: true });
  const jobFile = `${BM_DIR}/job-${Date.now()}.json`;
  saveJson(jobFile, { items, created: new Date().toISOString() });
  const child = spawn('python', [BM_SCRIPT, jobFile], {
    detached: true, stdio: 'ignore', windowsHide: true,
    env: { ...process.env, SIR_TELEGRAM_BOT_TOKEN: token, SIR_TELEGRAM_CHAT_ID: chatId, PYTHONUTF8: '1' },
  });
  child.unref();
  jobChild = child;
  jobInfo = { pid: child.pid, startedAt: Date.now(), count: items.length };
  saveJson(BM_JOB, jobInfo);
  armWatchdog();
  child.on('exit', () => {
    jobChild = null;
    jobInfo = null;
    try { unlinkSync(BM_JOB); } catch {}
    if (watchdogTimer) { clearInterval(watchdogTimer); watchdogTimer = null; }
    // short debounce so a trailing message joins the next burst instead of a lone job
    scheduleFlush(BURST_MS);
  });
}

function armWatchdog() {
  if (watchdogTimer) clearInterval(watchdogTimer);
  let warned = false;
  watchdogTimer = setInterval(() => {
    if (!jobInfo) { clearInterval(watchdogTimer); watchdogTimer = null; return; }
    const stage = loadJson(BM_STAGE, {});
    const stageTxt = stage.stage ? ` (${stage.stage})` : '';
    if (!warned && Date.now() - jobInfo.startedAt > WATCHDOG_MS) {
      warned = true;
      tg.sendMessage(`[المدير الاحتياطي] لسه بشغال على رسالتك${stageTxt}، يستنى شوية.`).catch(() => {});
    }
  }, 30000);
  watchdogTimer.unref?.();
}

// On startup: adopt a job we did not spawn (listener restarted mid-job).
function adoptRunningJob() {
  const j = loadJson(BM_JOB, null);
  if (!j || !j.pid) return;
  try { process.kill(j.pid, 0); } catch { // dead: clear and flush whatever queued
    try { unlinkSync(BM_JOB); } catch {}
    if (loadQueue().items.length) scheduleFlush(1000);
    return;
  }
  jobInfo = { pid: j.pid, startedAt: j.startedAt || Date.now(), count: j.count || 0 };
  const check = setInterval(() => {
    try { process.kill(j.pid, 0); } catch {
      clearInterval(check);
      jobInfo = null;
      try { unlinkSync(BM_JOB); } catch {}
      if (watchdogTimer) { clearInterval(watchdogTimer); watchdogTimer = null; }
      scheduleFlush(BURST_MS);
    }
  }, 5000);
  check.unref?.();
  armWatchdog();
}

function bmStatusText() {
  const q = loadQueue();
  const job = loadJson(BM_JOB, null);
  const stage = loadJson(BM_STAGE, {});
  const lines = ['[المدير الاحتياطي] الحالة:'];
  lines.push(`رسائل مستنية: ${q.items.length}`);
  if (job) {
    const mins = ((Date.now() - (job.startedAt || Date.now())) / 60000).toFixed(1);
    lines.push(`شغال من ${mins} دقيقة على ${job.count || '?'} رسالة${stage.stage ? ` - المرحلة: ${stage.stage}` : ''}`);
  } else lines.push('مفيش شغل شغال دلوقتي');
  const lat = loadJson(`${BM_DIR}/latency.json`, {});
  const best = Object.entries(lat).filter(([, v]) => v.wins > 0).sort((a, b) => (a[1].avg_ms || 1e9) - (b[1].avg_ms || 1e9)).slice(0, 3);
  if (best.length) lines.push('أسرع النماذج: ' + best.map(([k, v]) => `${k} (${Math.round(v.avg_ms / 1000)}s)`).join('، '));
  return lines.join('\n');
}

async function takeover(on) {
  bmSet(on); // written BEFORE anything async: the state flip must never be lost
  if (on) {
    await sendText('[المدير الاحتياطي] استلمت. من دلوقتي كلمني هنا (كتابة، فويس، صور) وأنا بكمل من مكان كلود وبوزع المهام وبتابع. للرجوع لكلود ابعت /handback.');
    bmEnqueue({ id: `takeover-${Date.now()}`, kind: 'text', text: 'Ahmed switched you on as the manager. Read the checkpoints and the queue, tell him the current state in a few lines, and continue the HQ duty.', message_id: 0 });
  } else {
    await sendText('[المدير الاحتياطي] رجعت الإدارة لكلود. الرسائل هتتسجل بس لحد ما كلود يقراها.');
  }
}

async function sendText(text) {
  const { err } = await run('node', [SEND, text]);
  if (err) console.log('send failed: ' + err.message);
}

function run(file, args, timeout = 60000) {
  return new Promise((resolve) => {
    execFile(file, args, { encoding: 'utf8', timeout, windowsHide: true, maxBuffer: 4 * 1024 * 1024, env: { ...process.env, PYTHONUTF8: '1' } },
      (err, stdout) => resolve({ err, out: String(stdout || '').trim() }));
  });
}

function loadActions() {
  try { return JSON.parse(readFileSync(ACTIONS, 'utf8')); } catch { return {}; }
}

async function runAction(name, msgText = '') {
  const def = loadActions()[name];
  if (!def || !Array.isArray(def.cmd)) {
    // no fixed command for this button: the AI manager decides what it means and does it (owner order 2026-11-12)
    if (bmActive()) {
      bmEnqueue({ id: `btn-${Date.now()}`, kind: 'text', message_id: 0,
        text: `Ahmed pressed the Telegram button "${name}" on this message of yours: "${String(msgText).slice(0, 600)}". Work out what the button means and do it (for example record that he exercised in the health log, move or cancel the reminder, mark the task, adjust the next reminder), then answer him in one short line.` });
    } else {
      bmEnqueue({ id: `btn-${Date.now()}`, kind: 'text', message_id: 0,
        text: `[زر ${name}] ${String(msgText).slice(0, 600)} — سجّلها في ahmed-telegram.md بس (المدير الاحتياطي مش شغال).` });
    }
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

const running = new Set(); // actions in progress, so a double tap does not start the same command twice

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
  await tg.editMessageReplyMarkup(cq.message.message_id, []).catch(() => {});
  const approval = /^(ok|no):([\w.-]{1,60})$/.exec(data);
  if (approval) {
    const answer = approval[1] === 'ok' ? 'approved' : 'rejected';
    const result = recordApproval(approval[2], answer);
    if (result === 'ok') {
      appendFileSync(APPROVALS, JSON.stringify({ id: approval[2], answer, at: new Date().toISOString() }) + '\n');
      await tg.answerCallbackQuery(cq.id, answer === 'approved' ? 'تمت الموافقة' : 'تم الرفض');
      await sendText(answer === 'approved' ? '[الإدارة] تم تسجيل موافقتك.' : '[الإدارة] تم تسجيل رفضك، ومش هيتنفذ.');
    } else {
      await tg.answerCallbackQuery(cq.id, 'الطلب ده مش موجود أو انتهت صلاحيته');
    }
    return;
  }
  const appApproval = /^(approve_ok|approve_no):([\w.-]{1,50})$/.exec(data);
  if (appApproval) {
    const answer = appApproval[1] === 'approve_ok' ? 'approved' : 'rejected';
    const result = recordApproval(appApproval[2], answer);
    if (result === 'ok') {
      await tg.answerCallbackQuery(cq.id, answer === 'approved' ? 'تمت الموافقة' : 'تم الرفض');
      await sendText(answer === 'approved' ? '[الإدارة] تم تسجيل موافقتك.' : '[الإدارة] تم تسجيل رفضك، ومش هيتنفذ.');
    } else {
      await tg.answerCallbackQuery(cq.id, 'الطلب ده مش موجود أو انتهت صلاحيته');
    }
    return;
  }

  // Apply pipeline: a_<jobId> = apply, s_<jobId> = skip
  const applyMatch = /^a_([\w.-]{1,50})$/.exec(data);
  if (applyMatch) {
    const jobId = applyMatch[1];
    await tg.answerCallbackQuery(cq.id, 'جاري التقديم...');
    run('node', ['D:/Projects/SIR Jobs/scripts/apply/handler.mjs', 'apply', jobId], 180000);
    return;
  }

  const skipMatch = /^s_([\w.-]{1,50})$/.exec(data);
  if (skipMatch) {
    const jobId = skipMatch[1];
    await tg.answerCallbackQuery(cq.id, 'تم التخطي');
    run('node', ['D:/Projects/SIR Jobs/scripts/apply/handler.mjs', 'skip', jobId], 60000);
    return;
  }

  // Reply pipeline: reply_<threadId> = send suggested reply
  const replyMatch = /^reply_([\w.-]{1,50})$/.exec(data);
  if (replyMatch) {
    const threadId = replyMatch[1];
    await tg.answerCallbackQuery(cq.id, 'جاري الإرسال...');
    run('node', ['D:/Projects/SIR Jobs/scripts/apply/reply-handler.mjs', threadId], 60000);
    return;
  }

  if (data === 'takeover' || data === 'handback') { await tg.answerCallbackQuery(cq.id, 'تمام'); await takeover(data === 'takeover'); return; }
  await tg.answerCallbackQuery(cq.id, 'تمام، بنفذ');
  runAction(data, cq.message?.text || ''); // not awaited: polling continues while the command runs
}

// Strip a leading bot mention so "/takeover@SomeBot" still works.
function commandOf(text) {
  const first = String(text || '').trim().split(/\s+/)[0] || '';
  return first.split('@')[0].toLowerCase();
}

async function poll() {
  const url = `https://api.telegram.org/bot${token}/getUpdates?timeout=50&offset=${offset}&allowed_updates=%5B%22message%22%2C%22callback_query%22%5D`;
  const res = await tg.fetchImpl(url);
  const data = await res.json();
  if (!data.ok) throw new Error('getUpdates failed: ' + (data.description || res.status));
  for (const u of data.result) {
    // advance the offset only AFTER the update is handled: a crash mid-batch
    // must not lose messages (r64: /takeover once vanished this way)
    try {
      if (u.callback_query) { await handleButton(u.callback_query); }
      else await handleMessage(u);
      offset = u.update_id + 1;
      writeFileSync(OFFSET_FILE, String(offset));
    } catch (e) {
      console.log(`update ${u.update_id} failed, will retry: ${e.message}`);
      // do not advance offset: Telegram resends this update on the next poll
      break;
    }
  }
}

async function handleMessage(u) {
  const m = u.message;
  if (!m || String(m.chat?.id) !== String(chatId)) return;
  const rawText = m.text || m.caption || '';
  const text = (rawText || (m.voice ? '[voice message]' : m.photo ? '[photo]' : m.document ? '[file ' + (m.document.file_name || '') + ']' : '[unsupported message]')).replace(/\s+/g, ' ').trim();
  const stamp = new Date(m.date * 1000).toISOString();
  appendFileSync(INBOX, `- ${stamp} from Ahmed (Telegram): ${text}\n`);
  console.log(`AHMED (Telegram ${stamp}): ${text}`);
  const cmd = commandOf(rawText);
  if (cmd === '/takeover' || cmd === '/manager' || /^(استلم|المدير الاحتياطي|كمل انت|كمّل انت)\s*$/i.test(text)) await takeover(true);
  else if (cmd === '/handback' || /^(رجع الإدارة لكلود|رجوع لكلود)\s*$/i.test(text)) await takeover(false);
  else if (cmd === '/status' || /^\/حالة/.test(cmd)) {
    if (bmActive()) await sendText(bmStatusText());
    else runAction('status');
  }
  else if (cmd === '/queue') runAction('queue');
  else if (/^\/(menu|start|help)/.test(cmd)) {
    const { err } = await run('node', [SEND_BUTTONS, ...MENU]);
    if (err) console.log('menu failed: ' + err.message);
  } else if (!bmActive() && (m.text || m.voice || m.photo) && Date.now() - lastIdleNote > 3600000) {
    lastIdleNote = Date.now();
    await sendText('[الإدارة] وصلتني رسالتك وهي متسجلة. كلود هو المدير دلوقتي. لو عايز المدير الاحتياطي (الأدوات المجانية) يرد عليك ابعت /takeover.');
  } else if (bmActive()) {
    const kind = m.voice || m.audio ? 'voice' : m.photo ? 'photo' : m.document ? 'document' : m.text ? 'text' : '';
    const fileId = m.voice?.file_id || m.audio?.file_id || (m.photo ? m.photo[m.photo.length - 1].file_id : '') || m.document?.file_id || '';
    if (!kind) await sendText('[المدير الاحتياطي] النوع ده من الرسايل مش مدعوم، ابعت كتابة أو فويس أو صورة.');
    else bmEnqueue({
      id: `${u.update_id}`, kind, text: m.text || m.caption || '', file_id: fileId,
      file_name: m.document?.file_name || '', media_group_id: m.media_group_id || '',
      message_id: m.message_id || 0, date: m.date || 0,
    });
  }
}

adoptRunningJob();
// resume a queue left behind by a restart
if (!jobInfo && loadQueue().items.length) scheduleFlush(1500);

let backoff = 15000;
for (;;) {
  // A game is running (SIR game-mode marker): pause polling. Messages queue on
  // Telegram's servers and are picked up when the game ends. Alerts still send.
  if (existsSync(GAME_SNAPSHOT)) { await new Promise(r => setTimeout(r, 30000)); continue; }
  try {
    await poll();
    backoff = 15000;
  } catch (e) {
    console.log('telegram-inbox error: ' + e.message);
    await new Promise(r => setTimeout(r, backoff));
    backoff = Math.min(backoff * 2, 120000); // exponential backoff up to 2 min on network drops
  }
}
