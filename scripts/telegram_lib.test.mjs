import test from 'node:test';
import assert from 'node:assert/strict';
import { TelegramBot, escapeHtml, sleep } from './telegram_lib.mjs';

function mockFetch(responses) {
  const calls = [];
  const fn = async (url, opts) => {
    calls.push({ url, opts });
    const next = responses.length > 1 ? responses.shift() : responses[0];
    if (next instanceof Error) throw next;
    return {
      ok: next.status ? next.status < 400 : true,
      status: next.status || 200,
      json: async () => next.body,
    };
  };
  fn.calls = calls;
  return fn;
}

const ok = (result = { message_id: 1 }) => ({ body: { ok: true, result } });

test('escapeHtml escapes &, <, >', () => {
  assert.equal(escapeHtml('a<b>&"c"'), 'a&lt;b&gt;&amp;"c"');
});

test('sendMessage posts JSON with chat_id and text', async () => {
  const f = mockFetch([ok({ message_id: 42 })]);
  const tg = new TelegramBot({ token: 'T', chatId: 'C', fetchImpl: f });
  const r = await tg.sendMessage('hello');
  assert.equal(r.message_id, 42);
  const body = JSON.parse(f.calls[0].opts.body);
  assert.equal(body.chat_id, 'C');
  assert.equal(body.text, 'hello');
  assert.match(f.calls[0].url, /\/botT\/sendMessage$/);
});

test('editMessageText sends message_id', async () => {
  const f = mockFetch([ok()]);
  const tg = new TelegramBot({ token: 'T', chatId: 'C', fetchImpl: f });
  await tg.editMessageText(7, 'final answer');
  const body = JSON.parse(f.calls[0].opts.body);
  assert.equal(body.message_id, 7);
  assert.equal(body.text, 'final answer');
});

test('setMessageReaction sends emoji reaction array', async () => {
  const f = mockFetch([ok(true)]);
  const tg = new TelegramBot({ token: 'T', chatId: 'C', fetchImpl: f });
  await tg.setMessageReaction(9, '🔥');
  const body = JSON.parse(f.calls[0].opts.body);
  assert.deepEqual(body.reaction, [{ type: 'emoji', emoji: '🔥' }]);
});

test('retries on network error then succeeds', async () => {
  const f = mockFetch([new Error('fetch failed'), ok({ message_id: 5 })]);
  const tg = new TelegramBot({ token: 'T', chatId: 'C', fetchImpl: f, retries: 3 });
  const r = await tg.sendMessage('hi');
  assert.equal(r.message_id, 5);
  assert.equal(f.calls.length, 2);
});

test('honours retry_after on 429', async () => {
  const f = mockFetch([
    { status: 429, body: { ok: false, error_code: 429, description: 'Too Many Requests', parameters: { retry_after: 0 } } },
    ok({ message_id: 6 }),
  ]);
  const tg = new TelegramBot({ token: 'T', chatId: 'C', fetchImpl: f, retries: 2 });
  const r = await tg.sendMessage('hi');
  assert.equal(r.message_id, 6);
  assert.equal(f.calls.length, 2);
});

test('non-retryable API error throws TelegramApiError-like', async () => {
  const f = mockFetch([{ status: 400, body: { ok: false, error_code: 400, description: 'Bad Request: chat not found' } }]);
  const tg = new TelegramBot({ token: 'T', chatId: 'C', fetchImpl: f, retries: 0 });
  await assert.rejects(() => tg.sendMessage('hi'), /chat not found/);
});

test('sendChatAction and answerCallbackQuery shapes', async () => {
  const f = mockFetch([ok(true), ok(true)]);
  const tg = new TelegramBot({ token: 'T', chatId: 'C', fetchImpl: f });
  await tg.sendChatAction('typing');
  await tg.answerCallbackQuery('cb1', 'ok');
  assert.equal(JSON.parse(f.calls[0].opts.body).action, 'typing');
  assert.equal(JSON.parse(f.calls[1].opts.body).callback_query_id, 'cb1');
});

test('sendMessage truncates to 4096 chars', async () => {
  const f = mockFetch([ok()]);
  const tg = new TelegramBot({ token: 'T', chatId: 'C', fetchImpl: f });
  await tg.sendMessage('x'.repeat(5000));
  assert.equal(JSON.parse(f.calls[0].opts.body).text.length, 4096);
});

test('sleep resolves', async () => {
  await sleep(1);
});
