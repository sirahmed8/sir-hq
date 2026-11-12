"""Backup HQ manager behind the Telegram bot (owner order 2026-11-12).

Started by scripts/deliver/telegram-inbox.mjs for ONE message from Ahmed while backup mode is on (ops/backup-manager.json).
Usage: python backup_manager.py <payload.json>   payload = {id, kind: text|voice|photo|document, text, file_id, file_name}

Flow: download media -> voice is transcribed (Groq whisper, Cloudflare whisper as fallback) -> photos are described
(Gemini vision) and saved -> a prompt with the persona (ops/BACKUP_MANAGER_PROMPT.md), recent chat and the new message is
handed to the first free coding agent from the shared pool that can use tools (kilo, opencode, devin, agy) -> the agent
writes its answer to ops/backup-manager/reply-<id>.txt -> the answer goes back to Telegram.
Private content (AHome, Habiba) never goes through here; the persona forbids it.
"""
import nowindow  # noqa: F401
import base64
import json
import os
import re
import subprocess
import sys
import threading
import time
import urllib.request
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import cli_pool  # noqa: E402

ROOT = Path("D:/Projects/_SIR")
DIR = ROOT / "ops" / "backup-manager"
MEDIA = ROOT / "ops" / "telegram-media"
CHAT = ROOT / "ops" / "backup-manager-chat.jsonl"
LOCK = DIR / "busy.lock"
LOG = ROOT / "ops" / "agy-runs" / "backup-manager.log"
PERSONA = ROOT / "ops" / "BACKUP_MANAGER_PROMPT.md"
DEVIN = Path(os.environ.get("LOCALAPPDATA", "")) / "devin/cli/bin/devin.exe"
TOKEN = os.environ.get("SIR_TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.environ.get("SIR_TELEGRAM_CHAT_ID", "")
BRAIN_TOOLS = {"kilo", "opencode", "devin", "agy"}
# small free models mix Chinese, Russian and English into Arabic (owner complaint 2026-11-12): never use them to talk to him
WEAK_MODELS = ("nemotron-3.5-lightning", "beam-free", "flint", "mimo", "longcat", "minimax", "lightning")
BAD_SCRIPT = re.compile(r"[぀-ヿ㐀-鿿가-힯Ѐ-ӿ฀-๿]")


def reply_problem(text: str) -> str:
    """Return why a reply to the owner is unacceptable, or an empty string. Arabic with a few English technical words is fine."""
    if BAD_SCRIPT.search(text):
        return "contains Chinese, Russian or other foreign script"
    letters = [c for c in text if c.isalpha()]
    if len(letters) > 80:
        arabic = sum(1 for c in letters if "؀" <= c <= "ۿ")
        if arabic / len(letters) < 0.45:
            return "not mostly Arabic"
    if re.search(r"[A-Za-z]{3,}[؀-ۿ]{2,}[A-Za-z]{3,}[؀-ۿ]{2,}[A-Za-z]{3,}", text):
        return "words mix Arabic and Latin letters inside a sentence"
    return ""


def keys() -> dict:
    out = {}
    try:
        for line in (ROOT / "_local" / "api-keys.env").read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                out[k.strip()] = v.strip().strip('"').strip("'")
    except OSError:
        pass
    return out


KEYS = keys()


def tg(method: str, **params):
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{TOKEN}/{method}",
        data=json.dumps(params).encode("utf-8"),
        headers={"content-type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def clean(text: str) -> str:
    """Telegram shows the reply as plain text (no markdown is parsed): strip decoration
    symbols so nothing changes the shape of a word, and keep spacing tidy."""
    text = re.sub(r"[*`~]+", "", text)
    text = re.sub(r"(?m)^\s{0,3}#{1,6}\s*", "", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def send(text: str) -> None:
    text = clean(text) or "تم."
    for i in range(0, len(text), 3800):
        try:
            tg("sendMessage", chat_id=CHAT_ID, text=text[i:i + 3800])
        except Exception as e:  # noqa: BLE001
            log(f"send failed: {e}")


def log(msg: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%H:%M:%S')} {msg}\n")


def download(file_id: str, dest: Path) -> Path:
    info = tg("getFile", file_id=file_id)["result"]
    url = f"https://api.telegram.org/file/bot{TOKEN}/{info['file_path']}"
    dest = dest.with_suffix(Path(info["file_path"]).suffix or dest.suffix)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as r:
        dest.write_bytes(r.read())
    return dest


def _transcribe_inner(path: Path) -> str:
    """Groq whisper first, Cloudflare whisper second. Short timeouts so a stalled
    call cannot hold the owner for minutes (owner complaint 2026-11-12)."""
    data = path.read_bytes()
    if KEYS.get("GROQ_API_KEY"):
        try:
            boundary = uuid.uuid4().hex
            parts = []
            for name, value in (("model", "whisper-large-v3"), ("response_format", "json"), ("temperature", "0"),
                                ("prompt", "كلام مصري بالعامية، أحياناً كلمات إنجليزي عن شغل ودراسة وكومبيوتر ومشاريع")):
                parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"\r\n\r\n{value}\r\n'.encode("utf-8"))
            parts.append((f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{path.stem}.ogg"\r\n'
                          "Content-Type: application/octet-stream\r\n\r\n").encode("utf-8") + data + b"\r\n")
            parts.append(f"--{boundary}--\r\n".encode("utf-8"))
            req = urllib.request.Request(
                "https://api.groq.com/openai/v1/audio/transcriptions", data=b"".join(parts),
                headers={"Authorization": f"Bearer {KEYS['GROQ_API_KEY']}", "Content-Type": f"multipart/form-data; boundary={boundary}",
                         "User-Agent": "sir-hq/1.0"})
            with urllib.request.urlopen(req, timeout=75) as r:
                text = json.loads(r.read().decode("utf-8")).get("text", "").strip()
            if text:
                return text
        except Exception as e:  # noqa: BLE001
            log(f"groq whisper failed: {e}")
    token = KEYS.get("CF_AI_TOKEN_HQ") or KEYS.get("CLOUDFLARE_API_TOKEN")
    account = KEYS.get("CLOUDFLARE_ACCOUNT_ID")
    if token and account:
        try:
            body = json.dumps({"audio": base64.b64encode(data).decode("ascii")}).encode("utf-8")
            req = urllib.request.Request(
                f"https://api.cloudflare.com/client/v4/accounts/{account}/ai/run/@cf/openai/whisper-large-v3-turbo", data=body,
                headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode("utf-8"))["result"].get("text", "").strip()
        except Exception as e:  # noqa: BLE001
            log(f"cloudflare whisper failed: {e}")
    return ""


def transcribe(path: Path) -> str:
    """Hard-capped wrapper: even if a provider socket stalls, the owner waits
    at most TRANSCRIBE_BUDGET seconds before the fallback message is sent."""
    TRANSCRIBE_BUDGET = 210
    box: dict = {}

    def work():
        try:
            box["text"] = _transcribe_inner(path)
        except Exception as e:  # noqa: BLE001
            log(f"transcribe crashed: {e}")

    t = threading.Thread(target=work, daemon=True)
    t.start()
    t.join(TRANSCRIBE_BUDGET)
    if t.is_alive():
        log("transcribe timed out, giving up on this voice")
        return ""
    return box.get("text", "")


def describe_image(path: Path) -> str:
    key = KEYS.get("GOOGLE_AI_STUDIO_KEY")
    if not key:
        return ""
    for model in ("gemini-flash-lite-latest", "gemini-flash-latest"):
        try:
            body = json.dumps({"contents": [{"parts": [
                {"text": "Describe this image for a project manager in detail. Copy every visible text exactly (Arabic or English). "
                         "If it is a screenshot of an app, website or error, say what screen it is and what looks wrong."},
                {"inline_data": {"mime_type": "image/jpeg", "data": base64.b64encode(path.read_bytes()).decode("ascii")}}]}]}).encode("utf-8")
            req = urllib.request.Request(
                f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}", data=body,
                headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read().decode("utf-8"))["candidates"][0]["content"]["parts"][0]["text"].strip()
        except Exception as e:  # noqa: BLE001
            log(f"vision {model} failed: {e}")
    return ""


def history(n: int = 16) -> str:
    try:
        rows = [json.loads(x) for x in CHAT.read_text(encoding="utf-8").splitlines()[-n:]]
    except (OSError, ValueError):
        return "(no earlier messages in backup mode)"
    return "\n".join(f"[{r['t']}] {r['who']}: {r['text'][:700]}" for r in rows)


def remember(who: str, text: str) -> None:
    with CHAT.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"t": time.strftime("%m-%d %H:%M"), "who": who, "text": text}, ensure_ascii=False) + "\n")


def brain(prompt_file: Path, reply_file: Path) -> bool:
    """Give the prompt to the free agents one after another until one writes the reply file."""
    msg = f"Read the file {prompt_file.as_posix()} and do exactly what it says. Your final action is to write the reply to {reply_file.as_posix()}."
    tried = 0
    skipped = 0
    while tried < 5 and skipped < 30:
        pick = cli_pool.pick()
        if pick.startswith("WAIT"):
            log("pool empty: " + pick)
            return False
        tool, _, model = pick.partition("|")
        if tool not in BRAIN_TOOLS or any(w in model for w in WEAK_MODELS):
            skipped += 1
            continue
        tried += 1
        log(f"attempt {tried}: {pick}")
        LOG.parent.mkdir(parents=True, exist_ok=True)
        offset = LOG.stat().st_size if LOG.exists() else 0
        t0 = time.time()
        cmd = {
            "kilo": ["kilo", "run", "--auto", "-m", model, msg],
            "opencode": ["opencode", "run", "-m", model, msg],
            "devin": [str(DEVIN), "-p", "--model", model, "--permission-mode", "dangerous", "--respect-workspace-trust", "false", "--", msg],
            "agy": ["agy", "--print", msg, "--model", model, "--dangerously-skip-permissions"],
        }[tool]
        code = 1
        try:
            with LOG.open("ab") as lf:
                code = subprocess.run(cmd, cwd=str(ROOT), stdout=lf, stderr=subprocess.STDOUT, timeout=1200,
                                      shell=(os.name == "nt" and tool != "devin")).returncode
        except (subprocess.TimeoutExpired, OSError) as e:
            log(f"run error: {e}")
        cli_pool.report(pick, code if not reply_file.exists() else 0, str(LOG), offset, time.time() - t0)
        if reply_file.exists() and reply_file.read_text(encoding="utf-8").strip():
            bad = reply_problem(reply_file.read_text(encoding="utf-8"))
            if not bad:
                return True
            log(f"reply rejected from {pick}: {bad}")
            reply_file.rename(reply_file.with_suffix(f".rejected{tried}"))
    return False


def acquire() -> bool:
    DIR.mkdir(parents=True, exist_ok=True)
    for _ in range(900):  # wait up to 30 minutes so messages are answered in order
        try:
            fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.close(fd)
            return True
        except FileExistsError:
            if time.time() - LOCK.stat().st_mtime > 1500:
                LOCK.unlink(missing_ok=True)
            time.sleep(2)
    return False


def main() -> int:
    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    pid = str(payload["id"])
    if not TOKEN or not CHAT_ID:
        return 1
    stop = threading.Event()

    def typing():
        while not stop.is_set():
            try:
                tg("sendChatAction", chat_id=CHAT_ID, action="typing")
            except Exception:  # noqa: BLE001
                pass
            stop.wait(4)

    threading.Thread(target=typing, daemon=True).start()
    try:
        kind, text = payload.get("kind", "text"), payload.get("text", "")
        note = ""
        if kind == "voice":
            f = download(payload["file_id"], MEDIA / f"voice-{pid}.ogg")
            send("[بسمع الفويس]")
            heard = transcribe(f)
            if not heard:
                send("[المدير الاحتياطي] مقدرتش أسمع الفويس كويس. ابعته تاني أو اكتبها.")
                return 0
            text = heard + ("\n" + text if text else "")
            note = f"(this was a voice message, transcribed automatically from Egyptian Arabic and English; it can contain small errors, understand the intent: {f.as_posix()})"
            send(f"[سمعت] {heard[:900]}")
        elif kind in ("photo", "document"):
            f = download(payload["file_id"], MEDIA / f"{kind}-{pid}.jpg")
            desc = describe_image(f) if f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp") else ""
            note = f"(Ahmed sent a {kind}, saved at {f.as_posix()}" + (f"; automatic description of the image: {desc}" if desc else "; open the file yourself if your tool can read it") + ")"
        if not acquire():
            send("[المدير الاحتياطي] فيه شغل طويل شغال، رسالتك لسه في الدور.")
            return 1
        try:
            remember("Ahmed", (text + " " + note).strip())
            prompt_file, reply_file = DIR / f"prompt-{pid}.txt", DIR / f"reply-{pid}.txt"
            reply_file.unlink(missing_ok=True)
            prompt_file.write_text(
                PERSONA.read_text(encoding="utf-8") +
                f"\n\n## Recent chat with Ahmed (newest last)\n{history()}\n\n## New message from Ahmed now\n{text}\n{note}\n\n"
                f"## Your output\nDo the work he asked (files, queue briefs, checks). Then write your reply to him (Egyptian Arabic, short, ends with the line starting المطلوب منك:) "
                f"to this file with a file-writing tool: {reply_file.as_posix()}\nOnly that file is sent to him.\n", encoding="utf-8")
            ok = brain(prompt_file, reply_file)
            answer = reply_file.read_text(encoding="utf-8").strip() if ok else \
                "[المدير الاحتياطي] كل الأدوات المجانية واقفة دلوقتي (حدود الاستخدام). رسالتك اتسجلت وهتتنفذ أول ما أداة تفتح.\nالمطلوب منك: لا شيء."
            remember("Manager", answer)
            send(answer)
        finally:
            LOCK.unlink(missing_ok=True)
    finally:
        stop.set()
    return 0


if __name__ == "__main__":
    sys.exit(main())
