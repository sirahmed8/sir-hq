import fs from 'node:fs';
import path from 'node:path';

function getConfig() {
  const cfgPath = 'D:/Projects/SIR AI/legacy/SIR Tele Gateway/config/gateway_config.json';
  if (fs.existsSync(cfgPath)) {
    const raw = JSON.parse(fs.readFileSync(cfgPath, 'utf8'));
    return {
      token: process.env.SIR_TELEGRAM_BOT_TOKEN || raw.bot_token,
      chatId: process.env.SIR_TELEGRAM_CHAT_ID || String(raw.authorized_chat_id || '1947329340')
    };
  }
  return {
    token: process.env.SIR_TELEGRAM_BOT_TOKEN,
    chatId: process.env.SIR_TELEGRAM_CHAT_ID || '1947329340'
  };
}

export async function sendTelegramFile(filePath, caption = '') {
  const { token, chatId } = getConfig();
  if (!token) throw new Error('Missing Telegram Bot Token');

  const fileBuffer = fs.readFileSync(filePath);
  const fileName = path.basename(filePath);
  const blob = new Blob([fileBuffer]);

  const form = new FormData();
  form.append('chat_id', chatId);
  form.append('document', blob, fileName);
  if (caption) {
    form.append('caption', caption);
    form.append('parse_mode', 'HTML');
  }

  const res = await fetch(`https://api.telegram.org/bot${token}/sendDocument`, {
    method: 'POST',
    body: form
  });

  const data = await res.json();
  if (!data.ok) {
    throw new Error(`Telegram API Error: ${data.description}`);
  }
  return data.result;
}

export async function sendTelegramMessage(text) {
  const { token, chatId } = getConfig();
  if (!token) throw new Error('Missing Telegram Bot Token');

  const res = await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      chat_id: chatId,
      text: text,
      parse_mode: 'HTML'
    })
  });

  const data = await res.json();
  if (!data.ok) {
    throw new Error(`Telegram API Error: ${data.description}`);
  }
  return data.result;
}

// CLI entry point
if (process.argv[1] && process.argv[1].endsWith('send.mjs')) {
  const args = process.argv.slice(2);
  const fileIdx = args.indexOf('--file');
  const textIdx = args.indexOf('--text');
  const captionIdx = args.indexOf('--caption');

  if (fileIdx !== -1 && args[fileIdx + 1]) {
    const filePath = args[fileIdx + 1];
    const caption = captionIdx !== -1 && args[captionIdx + 1] ? args[captionIdx + 1] : '';
    sendTelegramFile(filePath, caption)
      .then(res => {
        console.log(`[Telegram OK] Document sent: ${path.basename(filePath)} (MsgId: ${res.message_id})`);
      })
      .catch(err => {
        console.error(`[Telegram Error] Failed to send document: ${err.message}`);
        process.exit(1);
      });
  } else if (textIdx !== -1 && args[textIdx + 1]) {
    const text = args[textIdx + 1];
    sendTelegramMessage(text)
      .then(res => {
        console.log(`[Telegram OK] Message sent (MsgId: ${res.message_id})`);
      })
      .catch(err => {
        console.error(`[Telegram Error] Failed to send message: ${err.message}`);
        process.exit(1);
      });
  } else {
    console.log('Usage: node send.mjs --file <path> [--caption <text>] | --text <message>');
  }
}
