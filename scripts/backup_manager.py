"""Backup HQ manager behind the Telegram bot (owner order 2026-11-12, r64).

Started by scripts/deliver/telegram-inbox.mjs with ONE job file:
  ops/backup-manager/job-<ts>.json = {"items": [{id, kind, text, file_id, ...}, ...]}
(A legacy single-message file {"id","kind","text","file_id"} is still accepted.)

One job = one burst of Ahmed's messages (text + voice + photos, grouped by the
listener's 8 s debounce and media_group_id). Flow:
  download media -> transcribe every voice note and describe every photo IN
  PARALLEL -> one ordered prompt (persona + recent chat + everything Ahmed sent)
  -> race TWO free coding agents from the shared pool, first valid reply file
  wins, 150 s per attempt -> answer goes back to Telegram.

Speed contract (r64): instant ack is the listener's job (reaction + typing);
this script sends a short "got it" line, keeps typing alive, and answers as
fast as the fastest healthy model allows. Long work still ends in one reply;
ops/backup-manager/latency.json remembers which entries answer fastest.
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
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import cli_pool  # noqa: E402
from telegram_lib import TelegramBot  # noqa: E402

ROOT = Path("D:/Projects/_SIR")
DIR = ROOT / "ops" / "backup-manager"
MEDIA = ROOT / "ops" / "telegram-media"
CHAT = ROOT / "ops" / "backup-manager-chat.jsonl"
LOCK = DIR / "busy.lock"
LOG = ROOT / "ops" / "agy-runs" / "backup-manager.log"
STAGE = DIR / "job-state.json"
LATENCY = DIR / "latency.json"
PERSONA = ROOT / "ops" / "BACKUP_MANAGER_PROMPT.md"
DEVIN = Path(os.environ.get("LOCALAPPDATA", "")) / "devin/cli/bin/devin.exe"
TOKEN = os.environ.get("SIR_TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.environ.get("SIR_TELEGRAM_CHAT_ID", "")
BRAIN_TOOLS = {"kilo", "opencode", "devin", "agy"}
# small free models mix Chinese, Russian and English into Arabic (owner complaint 2026-11-12): never use them to talk to him
WEAK_MODELS = ("nemotron-3.5-lightning", "beam-free", "flint", "mimo", "longcat", "minimax", "lightning")
BAD_SCRIPT = re.compile(r"[぀-ヿ㐀-鿿가-힯Ѐ-ӿ฀-๿]")
ATTEMPT_TIMEOUT = 150      # seconds per racing pair (r64: was 20 minutes)
MAX_ATTEMPTS = 4
RACE_SIZE = 2


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
TG = TelegramBot(TOKEN, CHAT_ID) if TOKEN and CHAT_ID else None


def tg(method: str, **params):
    if TG is None:
        raise RuntimeError("telegram not configured")
    # thin shim kept for the transcribe/download helpers; new code uses TG.* directly
    return TG.call(method, params)


def clean(text: str) -> str:
    """Telegram shows the reply as plain text (no markdown is parsed): strip decoration
    symbols so nothing changes the shape of a word, and keep spacing tidy."""
    text = re.sub(r"[*`~\[\]]+", "", text)
    text = re.sub(r"(?m)^\s{0,3}#{1,6}\s*", "", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def send(text: str) -> None:
    if TG is None:
        return
    text = clean(text) or "تم."
    for i in range(0, len(text), 3800):
        try:
            TG.send_message(text[i:i + 3800])
        except Exception as e:  # noqa: BLE001
            log(f"send failed: {e}")


def stage(name: str, detail: str = "") -> None:
    try:
        STAGE.write_text(json.dumps({"stage": name, "detail": detail, "at": time.time()}), encoding="utf-8")
    except OSError:
        pass


def log(msg: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%H:%M:%S')} {msg}\n")


def download(file_id: str, dest: Path) -> Path:
    info = tg("getFile", file_id=file_id)
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


def load_latency() -> dict:
    try:
        return json.loads(LATENCY.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def record_latency(entry: str, seconds: float, won: bool) -> None:
    data = load_latency()
    rec = data.setdefault(entry, {"wins": 0, "fails": 0, "total_ms": 0, "runs": 0})
    rec["runs"] += 1
    rec["total_ms"] += int(seconds * 1000)
    rec["avg_ms"] = rec["total_ms"] // max(rec["runs"], 1)
    if won:
        rec["wins"] += 1
    else:
        rec["fails"] += 1
    try:
        LATENCY.write_text(json.dumps(data, indent=1), encoding="utf-8")
    except OSError:
        pass


def pick_brain() -> list[str]:
    """Two distinct pool entries for the next race. Entries that have answered
    fast before are preferred (latency.json), but a cooling entry is never picked."""
    lat = load_latency()
    out = []
    skipped = 0
    while len(out) < RACE_SIZE and skipped < 40:
        pick = cli_pool.pick()
        if pick.startswith("WAIT"):
            log("pool empty: " + pick)
            break
        tool, _, model = pick.partition("|")
        if tool not in BRAIN_TOOLS or any(w in model for w in WEAK_MODELS):
            skipped += 1
            continue
        if pick in out:
            skipped += 1
            continue
        out.append(pick)
    return out


def agent_cmd(tool: str, model: str, msg: str) -> list[str]:
    return {
        "kilo": ["kilo", "run", "--auto", "-m", model, msg],
        "opencode": ["opencode", "run", "-m", model, msg],
        "devin": [str(DEVIN), "-p", "--model", model, "--permission-mode", "dangerous", "--respect-workspace-trust", "false", "--", msg],
        "agy": ["agy", "--print", msg, "--model", model, "--dangerously-skip-permissions"],
    }[tool]


def valid_reply(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8").strip()
    except OSError:
        return ""
    if not text:
        return ""
    if reply_problem(text):
        return ""
    return text


def race(entries: list[str], prompt_file: Path, tag: str) -> str | None:
    """Run up to RACE_SIZE agents in parallel; first valid reply file wins.
    Per-attempt wall clock is ATTEMPT_TIMEOUT seconds. Returns the winning entry
    or None. Every entry is reported to cli_pool exactly once."""
    procs = []
    reply_files = []
    t0 = time.time()
    msg = (f"Read the file {prompt_file.as_posix()} and do exactly what it says. "
           f"Your final action is to write the reply to the reply file named in it.")
    LOG.parent.mkdir(parents=True, exist_ok=True)
    base_offset = LOG.stat().st_size if LOG.exists() else 0
    for i, entry in enumerate(entries):
        tool, _, model = entry.partition("|")
        reply_file = DIR / f"reply-{tag}-{i}.txt"
        reply_file.unlink(missing_ok=True)
        reply_files.append(reply_file)
        # the prompt file itself names ONE reply path; give each racer its own by suffixing the instruction
        m = msg + f" Write it to {reply_file.as_posix()}"
        cmd = agent_cmd(tool, model, m)
        try:
            lf = LOG.open("ab")
            p = subprocess.Popen(cmd, cwd=str(ROOT), stdout=lf, stderr=subprocess.STDOUT,
                                 shell=(os.name == "nt" and tool != "devin"),
                                 creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0)
            procs.append((entry, p, reply_file, lf))
        except OSError as e:
            log(f"spawn failed for {entry}: {e}")
            cli_pool.report(entry, 1, str(LOG), base_offset, 0.1)
    winner = None
    winner_text = ""
    deadline = t0 + ATTEMPT_TIMEOUT
    while time.time() < deadline:
        for entry, p, rf, _lf in procs:
            text = valid_reply(rf)
            if text:
                winner, winner_text = entry, text
                break
        if winner:
            break
        if all(p.poll() is not None for _, p, _, _ in procs):
            break  # everyone exited without a reply
        time.sleep(2)
    elapsed = time.time() - t0
    # collect results and report each entry once
    for i, (entry, p, rf, lf) in enumerate(procs):
        if p.poll() is None:
            try:
                p.terminate()
            except OSError:
                pass
            try:
                p.wait(timeout=10)
            except subprocess.TimeoutExpired:
                try:
                    p.kill()
                except OSError:
                    pass
        lf.close()
        text = valid_reply(rf)
        won = winner == entry
        cli_pool.report(entry, 0 if (won or text) else 1, str(LOG), base_offset, elapsed)
        record_latency(entry, elapsed, won)
        if won:
            log(f"race won by {entry} in {elapsed:.0f}s")
        elif text:
            log(f"{entry} wrote a reply but lost the race")
        else:
            log(f"{entry} produced no valid reply in {elapsed:.0f}s")
    if winner_text:
        # hand the winning reply to the caller through a stable name
        (DIR / f"reply-{tag}.txt").write_text(winner_text, encoding="utf-8")
    return winner


def brain(prompt_file: Path, reply_tag: str) -> bool:
    """Race pairs of free agents until one writes a valid reply."""
    tried = 0
    while tried < MAX_ATTEMPTS:
        entries = pick_brain()
        if not entries:
            return False
        tried += 1
        log(f"attempt {tried}: race {' vs '.join(entries)}")
        stage("thinking", f"attempt {tried}")
        if race(entries, prompt_file, reply_tag):
            return True
    return False


def acquire() -> bool:
    DIR.mkdir(parents=True, exist_ok=True)
    for _ in range(900):  # wait up to 30 minutes so bursts are answered in order
        try:
            fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.close(fd)
            return True
        except FileExistsError:
            if time.time() - LOCK.stat().st_mtime > 1800:
                LOCK.unlink(missing_ok=True)
            time.sleep(2)
    return False


def load_items(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict) and isinstance(data.get("items"), list):
        return data["items"]
    if isinstance(data, dict) and "id" in data:  # legacy single-message payload
        return [data]
    return []


def prepare_item(item: dict, tag: str) -> dict:
    """Download + transcribe/describe one burst item. Returns prompt lines + notes."""
    kind, text = item.get("kind", "text"), item.get("text", "") or item.get("caption", "")
    file_id = item.get("file_id", "")
    note = ""
    lines = []
    if kind == "voice" and file_id:
        f = download(file_id, MEDIA / f"voice-{tag}-{item.get('id', 'x')}.ogg")
        heard = transcribe(f)
        if not heard:
            lines.append("[voice message - transcription failed, ask him to resend or type it]")
        else:
            text = (heard + ("\n" + text if text else "")).strip()
            lines.append(f"[voice message, transcribed from Egyptian Arabic/English, can contain small errors - understand the intent: {heard}]")
            note = f"(voice note transcribed automatically, audio saved at {f.as_posix()})"
    elif kind == "photo" and file_id:
        f = download(file_id, MEDIA / f"photo-{tag}-{item.get('id', 'x')}.jpg")
        desc = describe_image(f) if f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp") else ""
        head = f"[photo Ahmed sent, saved at {f.as_posix()}"
        if desc:
            head += f"; automatic description: {desc}"
        else:
            head += "; open the file yourself if your tool can read it"
        lines.append(head + "]")
        note = f"(photo saved at {f.as_posix()})"
        if text:
            lines.append(f"[caption/text with the photo: {text}]")
    elif kind == "document" and file_id:
        f = download(file_id, MEDIA / f"doc-{tag}-{item.get('file_name') or item.get('id', 'x')}")
        lines.append(f"[document Ahmed sent: {item.get('file_name', f.name)}, saved at {f.as_posix()}]")
        if text:
            lines.append(f"[text with the document: {text}]")
        note = f"(document saved at {f.as_posix()})"
    elif text:
        lines.append(f"[text: {text}]")
    else:
        lines.append("[message with no readable text]")
    return {"lines": lines, "note": note, "kind": kind, "text": text}


def main() -> int:
    payload_path = Path(sys.argv[1])
    tag = payload_path.stem.replace("job-", "") or payload_path.stem
    items = load_items(payload_path)
    if not TOKEN or not CHAT_ID or not items:
        return 1
    stop = threading.Event()

    def typing():
        while not stop.is_set():
            try:
                if TG:
                    TG.send_chat_action("typing")
                else:
                    tg("sendChatAction", chat_id=CHAT_ID, action="typing")
            except Exception:  # noqa: BLE001
                pass
            stop.wait(4)

    threading.Thread(target=typing, daemon=True).start()
    try:
        stage("queued", f"{len(items)} message(s)")
        # quick ack: the owner sees he was heard, the real answer follows (r64)
        send("تمام، قريت رسالتك. بشوف وأرد عليك.")
        # media prep: transcribe every voice and describe every photo IN PARALLEL
        stage("media", f"{len(items)} item(s)")
        results = [None] * len(items)
        with ThreadPoolExecutor(max_workers=min(6, max(1, len(items)))) as ex:
            futs = {ex.submit(prepare_item, it, f"{tag}-{i}"): i for i, it in enumerate(items)}
            for fut, i in futs.items():
                try:
                    results[i] = fut.result()
                except Exception as e:  # noqa: BLE001
                    log(f"prepare item failed: {e}")
                    results[i] = {"lines": ["[message could not be prepared]"], "note": "", "kind": "text", "text": ""}
        stage("prompt", "writing prompt")
        ordered = []
        all_notes = []
        for i, r in enumerate(results):
            if not r:
                continue
            ordered.extend(r["lines"])
            if r["note"]:
                all_notes.append(r["note"])
            remember("Ahmed", (r["text"] or " ").strip() + " " + r["note"])
        body = "\n".join(f"{i + 1}. {line}" for i, line in enumerate(ordered))
        notes = "\n".join(all_notes)
        if not acquire():
            send("[المدير الاحتياطي] فيه شغل طويل شغال، رسالتك لسه في الدور.")
            return 1
        try:
            prompt_file = DIR / f"prompt-{tag}.txt"
            prompt_file.write_text(
                PERSONA.read_text(encoding="utf-8") +
                f"\n\n## Recent chat with Ahmed (newest last)\n{history()}\n\n"
                f"## New burst from Ahmed now ({len(items)} message(s), oldest first, ONE context - understand text, voice and photos together)\n{body}\n{notes}\n\n"
                f"## Your output\nDo the work he asked (files, queue briefs, checks). Then write your reply to him (Egyptian Arabic, short, ends with the line starting المطلوب منك:) "
                f"to the reply file path given in your task message (each runner has its own). Only that file is sent to him.\n", encoding="utf-8")
            stage("brain", "racing agents")
            ok = brain(prompt_file, tag)
            reply_path = DIR / f"reply-{tag}.txt"
            answer = reply_path.read_text(encoding="utf-8").strip() if ok and reply_path.exists() else \
                "[المدير الاحتياطي] كل الأدوات المجانية واقفة دلوقتي (حدود الاستخدام). رسالتك اتسجلت وهتتنفذ أول ما أداة تفتح.\nالمطلوب منك: لا شيء."
            remember("Manager", answer)
            stage("sending", "answer ready")
            send(answer)
        finally:
            LOCK.unlink(missing_ok=True)
    finally:
        stop.set()
        try:
            STAGE.unlink(missing_ok=True)
        except OSError:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
