// Shared Telegram Bot API kit for every SIR bot (r64, plans/TELEGRAM_BOT_KIT.md).
// One client with retries + backoff, HTML escaping, and the methods the SIR bots need:
// send/edit/delete messages, chat actions, reactions, media groups, documents,
// callback answers, bot profile (commands, descriptions, profile photo).
// Usage:
//   import { TelegramBot, escapeHtml } from './telegram_lib.mjs';
//   const tg = new TelegramBot({ token, chatId });
//   await tg.sendMessage('hi'); await tg.editMessageText(id, 'done');
// fetchImpl is injectable for tests; apiBase allows a local Bot API server.

export function escapeHtml(text) {
  return String(text ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;');
}

export function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

const DEFAULT_RETRIES = 4;
const RETRY_BASE_MS = 800;

export class TelegramBot {
  constructor({ token, chatId = '', apiBase = 'https://api.telegram.org', fetchImpl = null, retries = DEFAULT_RETRIES } = {}) {
    if (!token) throw new Error('TelegramBot: token is required');
    this.token = token;
    this.chatId = chatId;
    this.base = `${String(apiBase).replace(/\/+$/, '')}/bot${token}`;
    this.fetchImpl = fetchImpl || fetch;
    this.retries = retries;
  }

  // Low-level call with exponential backoff. Retries network errors, HTTP 429
  // (honours retry_after) and 5xx. Other API errors throw TelegramApiError.
  async call(method, body = {}, { retries = this.retries, form = null } = {}) {
    let attempt = 0;
    for (;;) {
      attempt += 1;
      let res;
      try {
        res = await this.fetchImpl(`${this.base}/${method}`, form
          ? { method: 'POST', body: form }
          : { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body) });
      } catch (e) {
        if (attempt > retries) throw new Error(`telegram ${method}: network error after ${attempt} tries (${e.cause?.code || e.name})`);
        await sleep(RETRY_BASE_MS * 2 ** (attempt - 1));
        continue;
      }
      let data;
      try { data = await res.json(); } catch {
        if (attempt > retries) throw new Error(`telegram ${method}: bad response HTTP ${res.status}`);
        await sleep(RETRY_BASE_MS * 2 ** (attempt - 1));
        continue;
      }
      if (data.ok) return data.result;
      const desc = data.description || `HTTP ${res.status}`;
      const retryAfter = data.parameters?.retry_after;
      if ((res.status === 429 || res.status >= 500) && attempt <= retries) {
        await sleep(Math.min((retryAfter ? retryAfter * 1000 : RETRY_BASE_MS * 2 ** (attempt - 1)), 30000));
        continue;
      }
      const err = new Error(`telegram ${method}: ${desc}`);
      err.code = data.error_code;
      err.retryAfter = retryAfter;
      throw err;
    }
  }

  // --- messaging ---
  async sendMessage(text, { chatId = this.chatId, parseMode = '', replyTo = 0, disableNotification = false } = {}) {
    const body = { chat_id: chatId, text: String(text).slice(0, 4096) };
    if (parseMode) body.parse_mode = parseMode;
    if (replyTo) body.reply_parameters = { message_id: replyTo };
    if (disableNotification) body.disable_notification = true;
    return this.call('sendMessage', body);
  }

  async sendHtml(text, opts = {}) {
    return this.sendMessage(escapeHtml(text), { ...opts, parseMode: 'HTML' });
  }

  async editMessageText(messageId, text, { chatId = this.chatId, parseMode = '' } = {}) {
    const body = { chat_id: chatId, message_id: messageId, text: String(text).slice(0, 4096) };
    if (parseMode) body.parse_mode = parseMode;
    return this.call('editMessageText', body);
  }

  async editMessageReplyMarkup(messageId, inlineKeyboard, { chatId = this.chatId } = {}) {
    return this.call('editMessageReplyMarkup', {
      chat_id: chatId, message_id: messageId,
      reply_markup: { inline_keyboard: inlineKeyboard || [] },
    });
  }

  async deleteMessage(messageId, { chatId = this.chatId } = {}) {
    return this.call('deleteMessage', { chat_id: chatId, message_id: messageId });
  }

  async sendChatAction(action = 'typing', { chatId = this.chatId } = {}) {
    return this.call('sendChatAction', { chat_id: chatId, action });
  }

  async setMessageReaction(messageId, emoji = '👍', { chatId = this.chatId } = {}) {
    return this.call('setMessageReaction', {
      chat_id: chatId, message_id: messageId,
      reaction: [{ type: 'emoji', emoji }],
    });
  }

  async sendMediaGroup(media, { chatId = this.chatId } = {}) {
    return this.call('sendMediaGroup', { chat_id: chatId, media });
  }

  async sendDocument(file, { chatId = this.chatId, caption = '', fileName = '' } = {}) {
    const { readFile } = await import('node:fs/promises');
    const { basename } = await import('node:path');
    const buf = Buffer.isBuffer(file) ? file : await readFile(file);
    const name = fileName || (typeof file === 'string' ? basename(file) : 'file.bin');
    const form = new FormData();
    form.append('chat_id', String(chatId));
    if (caption) form.append('caption', String(caption).slice(0, 1024));
    form.append('document', new Blob([buf]), name);
    return this.call('sendDocument', {}, { form });
  }

  async sendPhoto(fileIdOrPath, { chatId = this.chatId, caption = '' } = {}) {
    const body = { chat_id: chatId, caption: String(caption).slice(0, 1024) };
    if (typeof fileIdOrPath === 'string' && !fileIdOrPath.startsWith('/') && !fileIdOrPath.includes('\\') && !/\.[a-z0-9]{2,5}$/i.test(fileIdOrPath)) {
      body.photo = fileIdOrPath;
    } else {
      const { readFile } = await import('node:fs/promises');
      const buf = Buffer.isBuffer(fileIdOrPath) ? fileIdOrPath : await readFile(fileIdOrPath);
      const form = new FormData();
      form.append('chat_id', String(chatId));
      if (caption) form.append('caption', body.caption);
      form.append('photo', new Blob([buf]), 'photo.jpg');
      return this.call('sendPhoto', {}, { form });
    }
    return this.call('sendPhoto', body);
  }

  async answerCallbackQuery(id, text = '', { showAlert = false } = {}) {
    return this.call('answerCallbackQuery', { callback_query_id: id, text: String(text).slice(0, 200), show_alert: showAlert });
  }

  async getFile(fileId) {
    return this.call('getFile', { file_id: fileId });
  }

  async downloadFile(filePath, dest) {
    const res = await this.fetchImpl(`https://api.telegram.org/file/bot${this.token}/${filePath}`);
    if (!res.ok) throw new Error(`telegram download ${filePath}: HTTP ${res.status}`);
    const { writeFile, mkdir } = await import('node:fs/promises');
    const { dirname } = await import('node:path');
    await mkdir(dirname(dest), { recursive: true });
    await writeFile(dest, Buffer.from(await res.arrayBuffer()));
    return dest;
  }

  // --- bot profile (Bot API 8.x+) ---
  async setMyCommands(commands) {
    return this.call('setMyCommands', { commands });
  }

  async setMyDescription(description) {
    return this.call('setMyDescription', { description: String(description).slice(0, 512) });
  }

  async setMyShortDescription(description) {
    return this.call('setMyShortDescription', { short_description: String(description).slice(0, 120) });
  }

  async setMyProfilePhoto(photo) {
    // photo: file path, Buffer, or {type:'static', photo:'<file_id|multipart>'}
    if (photo && typeof photo === 'object' && photo.type) {
      return this.call('setMyProfilePhoto', { photo });
    }
    const { readFile } = await import('node:fs/promises');
    const buf = Buffer.isBuffer(photo) ? photo : await readFile(photo);
    const form = new FormData();
    form.append('photo', JSON.stringify({ type: 'static', photo: 'attach://file' }));
    form.append('file', new Blob([buf]), 'avatar.png');
    return this.call('setMyProfilePhoto', {}, { form });
  }
}
