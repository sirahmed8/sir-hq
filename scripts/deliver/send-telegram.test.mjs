import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import http from 'node:http';
import { spawn } from 'node:child_process';
import { writeFileSync, mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const script = join(dirname(fileURLToPath(import.meta.url)), 'send-telegram.mjs');
let server, base, dir, calls, mode;

before(async () => {
  dir = mkdtempSync(join(tmpdir(), 'sirtg-'));
  calls = [];
  mode = 'ok';
  server = http.createServer((req, res) => {
    req.on('data', () => {});
    req.on('end', async () => {
      calls.push(req.url.split('/').pop());
      res.setHeader('content-type', 'application/json');
      if (mode === 'err') return res.end(JSON.stringify({ ok: false, error_code: 403, description: 'Forbidden: bot was blocked' }));
      res.end(JSON.stringify({ ok: true, result: { message_id: 42 } }));
    });
  });
  await new Promise((r) => server.listen(0, '127.0.0.1', r));
  base = `http://127.0.0.1:${server.address().port}`;
});
after(() => {
  server.closeAllConnections();
  server.close();
  rmSync(dir, { recursive: true, force: true });
});

const run = (args, env = {}) =>
  new Promise((done) => {
    const c = spawn(process.execPath, [script, ...args], {
      env: { ...process.env, SIR_TELEGRAM_BOT_TOKEN: 'TESTTOKEN123', SIR_TELEGRAM_CHAT_ID: '777', SIR_TELEGRAM_API_BASE: base, ...env },
    });
    let stdout = '';
    c.stdout.on('data', (d) => (stdout += d));
    c.on('close', (status) => done({ status, stdout }));
  });

test('sends a document and prints only the summary', async () => {
  const f = join(dir, 'report.html');
  writeFileSync(f, '<h1>hello</h1>');
  const r = await run([f, 'caption']);
  assert.equal(r.status, 0);
  assert.equal(r.stdout.trim(), 'sent report.html message_id=42');
  assert.ok(calls.includes('sendDocument'));
  assert.ok(!r.stdout.includes('TESTTOKEN123') && !r.stdout.includes('777'));
});

test('sends plain text via sendMessage, split over 4000 chars', async () => {
  calls.length = 0;
  const r = await run(['x'.repeat(9000)]);
  assert.equal(r.status, 0);
  assert.equal(calls.filter((c) => c === 'sendMessage').length, 3);
});

test('API error gives FAILED and exit 1 without leaking secrets', async () => {
  mode = 'err';
  const r = await run(['hello']);
  mode = 'ok';
  assert.equal(r.status, 1);
  assert.match(r.stdout, /^FAILED API 403: Forbidden/);
  assert.ok(!r.stdout.includes('TESTTOKEN123'));
});

test('missing env fails when the user-scope reader finds nothing', async () => {
  const { send } = await import('./send-telegram.mjs');
  await assert.rejects(send(['hello'], { SIR_TELEGRAM_API_BASE: base }, () => ''), /missing env/);
});

test('falls back to the user-scope reader when process env lacks the vars', async () => {
  const { send } = await import('./send-telegram.mjs');
  calls.length = 0;
  const asked = [];
  const reader = (n) => (asked.push(n), n === 'SIR_TELEGRAM_BOT_TOKEN' ? 'STUBTOKEN' : '555');
  const out = await send(['hello'], { SIR_TELEGRAM_API_BASE: base }, reader);
  assert.equal(out, 'sent text message_id=42');
  assert.deepEqual(asked.sort(), ['SIR_TELEGRAM_BOT_TOKEN', 'SIR_TELEGRAM_CHAT_ID']);
  assert.ok(calls.includes('sendMessage'));
});

test('refuses files that mention private data and private-project paths', async () => {
  calls.length = 0;
  const f = join(dir, 'note.txt');
  writeFileSync(f, 'notes about Habiba');
  const r = await run([f]);
  assert.equal(r.status, 1);
  assert.match(r.stdout, /^FAILED refused/);
  const privateDir = ['D:', 'Projects', 'AH' + 'ome'].join('/');
  const r2 = await run([`${privateDir}/README.md`]);
  assert.equal(r2.status, 1);
  assert.match(r2.stdout, /^FAILED /);
  assert.equal(calls.length, 0);
});
