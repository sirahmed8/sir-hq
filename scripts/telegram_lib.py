"""Shared Telegram Bot API kit for the Python side of SIR bots (r64, plans/TELEGRAM_BOT_KIT.md).

Mirror of scripts/telegram_lib.mjs: one client with retries + exponential
backoff (429 retry_after honoured), HTML escaping, and the methods the SIR bots
need. Stdlib only.

Usage:
    from telegram_lib import TelegramBot, escape_html
    tg = TelegramBot(token, chat_id)
    tg.send_message("hi")
    tg.edit_message_text(message_id, "done")
"""
import json
import time
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_RETRIES = 4
RETRY_BASE_S = 0.8
API_BASE = "https://api.telegram.org"


def escape_html(text) -> str:
    return (
        str(text if text is not None else "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


class TelegramError(Exception):
    def __init__(self, method, description, code=None, retry_after=None):
        super().__init__(f"telegram {method}: {description}")
        self.method = method
        self.code = code
        self.retry_after = retry_after


class TelegramBot:
    def __init__(self, token, chat_id="", api_base=API_BASE, opener=None, retries=DEFAULT_RETRIES):
        if not token:
            raise ValueError("TelegramBot: token is required")
        self.token = token
        self.chat_id = str(chat_id)
        self.base = f"{api_base.rstrip('/')}/bot{token}"
        self.file_base = f"{api_base.rstrip('/')}/file/bot{token}"
        self._open = opener or urllib.request.urlopen
        self.retries = retries

    def call(self, method, params=None, _multipart=None):
        """Call a Bot API method. Retries network errors, HTTP 429 (retry_after)
        and 5xx with exponential backoff; other API errors raise TelegramError."""
        url = f"{self.base}/{method}"
        body = None
        headers = {}
        if _multipart is not None:
            boundary = "----sir" + str(int(time.time() * 1000))
            body = _multipart(boundary)
            headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
        else:
            body = json.dumps(params or {}).encode("utf-8")
            headers["Content-Type"] = "application/json"
        attempt = 0
        while True:
            attempt += 1
            try:
                req = urllib.request.Request(url, data=body, headers=headers, method="POST")
                with self._open(req, timeout=60) as r:
                    data = json.loads(r.read().decode("utf-8"))
            except urllib.error.HTTPError as e:
                data = None
                desc = f"HTTP {e.code}"
                try:
                    errbody = json.loads(e.read().decode("utf-8"))
                    desc = errbody.get("description") or desc
                    ra = (errbody.get("parameters") or {}).get("retry_after")
                except Exception:
                    ra = None
                if e.code == 429 or e.code >= 500:
                    if attempt <= self.retries:
                        wait = min(float(ra), 30) if ra else RETRY_BASE_S * (2 ** (attempt - 1))
                        time.sleep(wait)
                        continue
                raise TelegramError(method, desc, code=e.code, retry_after=ra)
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                if attempt > self.retries:
                    raise TelegramError(method, f"network error after {attempt} tries ({e})")
                time.sleep(RETRY_BASE_S * (2 ** (attempt - 1)))
                continue
            if data.get("ok"):
                return data.get("result")
            desc = data.get("description") or "unknown error"
            params_err = data.get("parameters") or {}
            raise TelegramError(method, desc, code=data.get("error_code"), retry_after=params_err.get("retry_after"))

    # --- messaging ---
    def send_message(self, text, chat_id=None, parse_mode="", reply_to=0, disable_notification=False):
        body = {"chat_id": str(chat_id or self.chat_id), "text": str(text)[:4096]}
        if parse_mode:
            body["parse_mode"] = parse_mode
        if reply_to:
            body["reply_parameters"] = {"message_id": reply_to}
        if disable_notification:
            body["disable_notification"] = True
        return self.call("sendMessage", body)

    def send_html(self, text, **kw):
        return self.send_message(escape_html(text), parse_mode="HTML", **kw)

    def edit_message_text(self, message_id, text, chat_id=None, parse_mode=""):
        body = {"chat_id": str(chat_id or self.chat_id), "message_id": message_id,
                "text": str(text)[:4096]}
        if parse_mode:
            body["parse_mode"] = parse_mode
        return self.call("editMessageText", body)

    def edit_message_reply_markup(self, message_id, inline_keyboard=None, chat_id=None):
        return self.call("editMessageReplyMarkup", {
            "chat_id": str(chat_id or self.chat_id), "message_id": message_id,
            "reply_markup": {"inline_keyboard": inline_keyboard or []}})

    def delete_message(self, message_id, chat_id=None):
        return self.call("deleteMessage", {"chat_id": str(chat_id or self.chat_id), "message_id": message_id})

    def send_chat_action(self, action="typing", chat_id=None):
        return self.call("sendChatAction", {"chat_id": str(chat_id or self.chat_id), "action": action})

    def set_message_reaction(self, message_id, emoji="👍", chat_id=None):
        return self.call("setMessageReaction", {
            "chat_id": str(chat_id or self.chat_id), "message_id": message_id,
            "reaction": [{"type": "emoji", "emoji": emoji}]})

    def send_media_group(self, media, chat_id=None):
        return self.call("sendMediaGroup", {"chat_id": str(chat_id or self.chat_id), "media": media})

    def send_document(self, file, chat_id=None, caption="", file_name=None):
        path = Path(file)
        data = path.read_bytes()
        name = file_name or path.name

        def build(boundary):
            head = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"chat_id\"\r\n\r\n"
                    f"{chat_id or self.chat_id}\r\n")
            if caption:
                head += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"caption\"\r\n\r\n"
                         f"{str(caption)[:1024]}\r\n")
            head += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"document\"; "
                     f"filename=\"{name}\"\r\nContent-Type: application/octet-stream\r\n\r\n")
            return head.encode("utf-8") + data + f"\r\n--{boundary}--\r\n".encode("utf-8")

        return self.call("sendDocument", _multipart=build)

    def send_photo(self, file_id_or_path, chat_id=None, caption=""):
        s = str(file_id_or_path)
        looks_like_id = not Path(s).exists() and "." not in Path(s).name
        if looks_like_id:
            body = {"chat_id": str(chat_id or self.chat_id), "photo": s}
            if caption:
                body["caption"] = str(caption)[:1024]
            return self.call("sendPhoto", body)
        data = Path(file_id_or_path).read_bytes()

        def build(boundary):
            head = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"chat_id\"\r\n\r\n"
                    f"{chat_id or self.chat_id}\r\n")
            if caption:
                head += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"caption\"\r\n\r\n"
                         f"{str(caption)[:1024]}\r\n")
            head += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"photo\"; "
                     f"filename=\"photo.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n")
            return head.encode("utf-8") + data + f"\r\n--{boundary}--\r\n".encode("utf-8")

        return self.call("sendPhoto", _multipart=build)

    def answer_callback_query(self, callback_query_id, text="", show_alert=False):
        return self.call("answerCallbackQuery", {
            "callback_query_id": callback_query_id, "text": str(text)[:200], "show_alert": show_alert})

    def get_file(self, file_id):
        return self.call("getFile", {"file_id": file_id})

    def download_file(self, file_path, dest):
        dest = Path(dest)
        dest.parent.mkdir(parents=True, exist_ok=True)
        url = f"{self.file_base}/{file_path}"
        req = urllib.request.Request(url)
        with self._open(req, timeout=120) as r:
            dest.write_bytes(r.read())
        return dest

    # --- bot profile (Bot API 8.x+) ---
    def set_my_commands(self, commands):
        return self.call("setMyCommands", {"commands": commands})

    def set_my_description(self, description):
        return self.call("setMyDescription", {"description": str(description)[:512]})

    def set_my_short_description(self, description):
        return self.call("setMyShortDescription", {"short_description": str(description)[:120]})

    def set_my_profile_photo(self, photo):
        """photo: path/bytes -> multipart upload, or dict InputProfilePhoto."""
        if isinstance(photo, dict):
            return self.call("setMyProfilePhoto", {"photo": photo})
        data = Path(photo).read_bytes() if not isinstance(photo, (bytes, bytearray)) else bytes(photo)

        def build(boundary):
            head = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"photo\"\r\n\r\n"
                    '{"type":"static","photo":"attach://file"}\r\n')
            head += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; "
                     f"filename=\"avatar.png\"\r\nContent-Type: image/png\r\n\r\n")
            return head.encode("utf-8") + data + f"\r\n--{boundary}--\r\n".encode("utf-8")

        return self.call("setMyProfilePhoto", _multipart=build)
