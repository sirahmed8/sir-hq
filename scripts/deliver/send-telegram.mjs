#!/usr/bin/env node
// Usage: node send-telegram.mjs <file|text> [caption]
// Sends a file (sendDocument) or text (sendMessage) from the SIR delivery bot to Ahmed.
import { readFile, stat } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import { basename, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const LIMIT_BYTES = 50 * 1024 * 1024;
const CHUNK = 4000;
const TEXT_EXT = /\.(md|txt)$/i;
const BLOCKED_DIR = 'd:/projects/ahome';

class Refusal extends Error {}

function fail(reason) {
  console.log(`FAILED ${reason}`);
  process.exit(1);
}

export function isBlockedPath(p) {
  const norm = resolve(p).replaceAll('\\', '/').toLowerCase();
  return norm === BLOCKED_DIR || norm.startsWith(`${BLOCKED_DIR}/`);
}

export function splitText(text, size = CHUNK) {
  const parts = [];
  let rest = text;
  while (rest.length > size) {
    let cut = rest.lastIndexOf('\n', size);
    if (cut < size / 2) cut = size;
    parts.push(rest.slice(0, cut));
    rest = rest.slice(cut).replace(/^\n/, '');
  }
  if (rest.length || !parts.length) parts.push(rest);
  return parts;
}

async function call(base, token, method, body) {
  let lastErr;
  for (let attempt = 1; attempt <= 3; attempt++) {
    try {
      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), 15000);
      const res = await fetch(`${base}/bot${token}/${method}`, { method: 'POST', body, signal: controller.signal });
      clearTimeout(timer);
      let data;
      try { data = await res.json(); } catch { throw new Error(`bad response HTTP ${res.status}`); }
      if (!data.ok) throw new Error(`API ${data.error_code ?? res.status}: ${data.description ?? 'unknown error'}`);
      return data.result;
    } catch (e) {
      lastErr = e;
      if (attempt < 3) await new Promise((r) => setTimeout(r, 1000));
    }
  }
  throw new Error(`network error (${lastErr?.cause?.code || lastErr?.name || lastErr?.message})`);
}

function form(fields) {
  const f = new FormData();
  for (const [k, v] of Object.entries(fields)) f.append(k, v);
  return f;
}

// Consoles started before the user env vars were set do not see them: read the Windows user scope.
export function readUserEnv(name) {
  if (process.platform !== 'win32' || !/^[A-Z_]+$/.test(name)) return '';
  try {
    const cmd = `[Environment]::GetEnvironmentVariable('${name}','User')`;
    return execFileSync('powershell', ['-NoProfile', '-Command', cmd], { encoding: 'utf8', timeout: 15000 }).trim();
  } catch { return ''; }
}

export async function send(args, env = process.env, readUser = readUserEnv) {
  const cache = {};
  const get = (n) => env[n] || (cache[n] ??= readUser(n));
  const token = get('SIR_TELEGRAM_BOT_TOKEN');
  const chat = get('SIR_TELEGRAM_CHAT_ID');
  if (!token || !chat) throw new Error('missing env SIR_TELEGRAM_BOT_TOKEN or SIR_TELEGRAM_CHAT_ID');
  const base = (env.SIR_TELEGRAM_API_BASE || 'https://api.telegram.org').replace(/\/$/, '');
  const [target, caption = ''] = args;
  if (!target) throw new Error('usage: send-telegram.mjs <file|text> [caption]');

  if (isBlockedPath(target)) throw new Refusal('refused: path is in a private project folder');
  let isFile = false;
  try { isFile = (await stat(target)).isFile(); } catch { /* plain text */ }

  if (!isFile) {
    if (/habiba/i.test(target)) throw new Refusal('refused: text mentions private AHome data');
    let id;
    for (const part of splitText(target)) id = (await call(base, token, 'sendMessage', form({ chat_id: chat, text: part }))).message_id;
    return `sent text message_id=${id}`;
  }

  const buf = await readFile(target);
  const name = basename(target);
  if (/habiba/i.test(buf.toString('utf8')) || /habiba/i.test(caption) || /habiba/i.test(name)) {
    throw new Refusal('refused: content mentions private AHome data');
  }
  if (TEXT_EXT.test(name) && buf.length <= CHUNK * 3 && !caption) {
    let id;
    for (const part of splitText(buf.toString('utf8'))) id = (await call(base, token, 'sendMessage', form({ chat_id: chat, text: part }))).message_id;
    return `sent ${name} message_id=${id}`;
  }
  if (buf.length > LIMIT_BYTES) throw new Error(`file is ${(buf.length / 1048576).toFixed(1)} MB, limit is 50 MB`);
  const f = form({ chat_id: chat });
  if (caption) f.append('caption', caption.slice(0, 1024));
  f.append('document', new Blob([buf]), name);
  const r = await call(base, token, 'sendDocument', f);
  return `sent ${name} message_id=${r.message_id}`;
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  try {
    console.log(await send(process.argv.slice(2)));
  } catch (e) {
    const token = process.env.SIR_TELEGRAM_BOT_TOKEN || readUserEnv('SIR_TELEGRAM_BOT_TOKEN');
    const chat = process.env.SIR_TELEGRAM_CHAT_ID || readUserEnv('SIR_TELEGRAM_CHAT_ID');
    let msg = String(e.message);
    for (const secret of [token, chat]) if (secret) msg = msg.split(secret).join('***');
    fail(msg);
  }
}
