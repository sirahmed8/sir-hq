"""Backup HQ manager behind the Telegram bot (owner order 2026-11-12, r64).

Started by scripts/deliver/telegram-inbox.mjs with ONE job file:
  ops/backup-manager/job-<ts>.json = {"items": [{id, kind, text, file_id, ...}, ...]}
(A legacy single-message file {"id","kind","text","file_id"} is still accepted.)

One job = one burst of Ahmed's messages (text + voice + photos, grouped by the
listener's 8 s debounce and media_group_id). Flow:
  download media -> transcribe every voice note and describe every photo IN
  PARALLEL -> one ordered prompt (persona + recent chat + everything Ahmed sent)
  -> walk the ordered model chain (CHAIN below, best to worst, one provider per
  step), 40 s per attempt inside a 180 s cap; a quota/limit/401/timeout/empty
  reply only moves the chain to the next model -> answer goes back to Telegram.

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
BRAIN_TOOLS = {"kilo", "opencode", "devin", "agy", "aider", "pi", "cline"}
# small free models mix Chinese, Russian and English into Arabic (owner complaint 2026-11-12): never use them to talk to him
WEAK_MODELS = ("nemotron-3.5-lightning", "mimo", "longcat", "minimax", "lightning")
BAD_SCRIPT = re.compile(r"[぀-ヿ㐀-鿿가-힯Ѐ-ӿ฀-๿]")
# Ordered fallback chain (owner order 2026-11-13): the best model answers first; when its
# usage limit dies, a 401/403 appears, it times out or it writes no valid reply, the next
# model in the list takes over by itself, best to worst, so Ahmed always gets an answer and
# work keeps going. One entry per upstream provider/account: every step is a real second
# chance and two steps can never spend the same quota.
ATTEMPT_TIMEOUT = 40       # seconds for ONE chain step (owner: 25-40 s per attempt)
MAX_TOTAL = 180            # hard cap for the whole chain, then the honest fallback line
CHAIN = [
    ("agy", "claude-sonnet-4-6", "claude via antigravity"),
    ("aider", "groq/openai/gpt-oss-120b", "groq gpt-oss 120b"),
    ("kilo", "kilo/kilo-auto/free", "kilo free router"),
    ("aider", "nvidia_nim/nvidia/nemotron-3-ultra-550b-a55b", "nvidia nemotron ultra"),
    ("devin", "swe-2-flash-medium", "devin swe-2"),
    ("aider", "openai/@cf/openai/gpt-oss-120b", "cloudflare gpt-oss 120b"),
    ("opencode", "opencode/big-pickle", "opencode big-pickle"),
    ("cline", "reflection/beam-free", "beam via cline"),
    ("pi", "radius/recursive/flint", "flint via radius"),
]


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


def clean_error(exc: Exception) -> str:
    text = re.sub(r"\s+", " ", str(exc)).strip()
    if TOKEN:
        text = text.replace(TOKEN, "***")
    return text[:180]


def download(file_id: str, dest: Path) -> Path:
    info = tg("getFile", file_id=file_id)
    url = f"https://api.telegram.org/file/bot{TOKEN}/{info['file_path']}"
    dest = dest.with_suffix(Path(info["file_path"]).suffix or dest.suffix)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as r:
        dest.write_bytes(r.read())
    return dest


def download_with_retry(file_id: str, dest: Path, tries: int = 2) -> Path:
    last = None
    for attempt in range(1, tries + 1):
        try:
            return download(file_id, dest)
        except Exception as e:  # noqa: BLE001
            last = e
            log(f"download attempt {attempt}/{tries} failed for {dest.name}: {clean_error(e)}")
            if attempt < tries:
                time.sleep(2)
    raise last


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


def chain_entries() -> list[tuple[str, str, str, str]]:
    """The ordered chain minus the entries the shared pool knows are cooling down.
    Returns (entry, tool, model, label) in quality order, best first."""
    data = cli_pool.load()
    now = time.time()
    out = []
    for tool, model, label in CHAIN:
        entry = f"{tool}|{model}"
        if tool not in BRAIN_TOOLS or any(w in model for w in WEAK_MODELS):
            continue
        rec = data.get(entry, {})
        if rec.get("until", 0) > now:
            left = int((rec["until"] - now) / 60) + 1
            log(f"chain skips {entry} ({left} min cooling: {rec.get('why', '')})")
            continue
        out.append((entry, tool, model, label))
    return out


# Full paths: the listener may run with a PATH that lacks the npm and user bin folders, and a
# tool that cannot be found exits before it ever sees the prompt (that is how the old race
# wasted whole attempts on "not recognized"). Keys come from the ignored _local/api-keys.env.
NPM_BIN = Path(os.environ.get("APPDATA") or r"C:\Users\a7med\AppData\Roaming") / "npm"
AGY_EXE = Path(os.environ.get("LOCALAPPDATA") or r"C:\Users\a7med\AppData\Local") / "agy" / "bin" / "agy.exe"
PI_EXE = Path(os.environ.get("USERPROFILE") or r"C:\Users\a7med") / ".pi" / "agent" / "bin" / "pi.cmd"
AIDER_EXE = Path(os.environ.get("USERPROFILE") or r"C:\Users\a7med") / ".local" / "bin" / "aider.exe"


def agent_cmd(tool: str, model: str, msg: str) -> tuple[list[str], dict]:
    """Command + extra environment for one chain entry (mirrors scripts/cli-run2.sh)."""
    env = dict(KEYS)
    if tool == "aider":
        env["BROWSER"] = "true"
        if model.startswith("nvidia_nim/"):
            env["NVIDIA_NIM_API_KEY"] = KEYS.get("NVIDIA_API_KEY", "")
        elif model.startswith("gemini/"):
            env["GEMINI_API_KEY"] = KEYS.get("GOOGLE_AI_STUDIO_KEY", "")
        elif model.startswith("openai/@cf/"):
            env["OPENAI_API_BASE"] = ("https://api.cloudflare.com/client/v4/accounts/"
                                      f"{KEYS.get('CLOUDFLARE_ACCOUNT_ID', '')}/ai/v1")
            env["OPENAI_API_KEY"] = KEYS.get("CLOUDFLARE_API_TOKEN", "")
        return ([str(AIDER_EXE), "--model", model, "--yes-always", "--no-detect-urls", "--no-browser",
                 "--no-auto-commits", "--no-show-model-warnings", "--message", msg], env)
    cmds = {
        "kilo": [str(NPM_BIN / "kilo.cmd"), "run", "--auto", "-m", model, msg],
        "opencode": [str(NPM_BIN / "opencode.cmd"), "run", "-m", model, msg],
        "devin": [str(DEVIN), "-p", "--model", model, "--permission-mode", "dangerous",
                  "--respect-workspace-trust", "false", "--", msg],
        "agy": [str(AGY_EXE), "--print", msg, "--model", model, "--dangerously-skip-permissions"],
        "pi": [str(PI_EXE), "-p", "--no-session", "--model", model, msg],
        "cline": [str(NPM_BIN / "cline.cmd"), "-P", "cline", "--thinking", "high", "-p", "--yolo",
                  "-m", model, msg],
    }
    return cmds[tool], env


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


def try_entry(entry: str, prompt_file: Path, tag: str, index: int, budget: float) -> str:
    """Run ONE chain entry and wait up to min(ATTEMPT_TIMEOUT, budget) seconds for its
    valid reply file. Returns the reply text, or "" when this entry could not answer
    (quota/limit/401, timeout, crash, empty or unusable reply). The entry is reported
    to the shared pool once so its cooldown is remembered."""
    tool, _, model = entry.partition("|")
    reply_file = DIR / f"reply-{tag}-{index}.txt"
    reply_file.unlink(missing_ok=True)
    msg = (f"Read the file {prompt_file.as_posix()} and do exactly what it says. "
           f"Your final action is to write the reply to the reply file {reply_file.as_posix()}")
    cmd, extra_env = agent_cmd(tool, model, msg)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    base_offset = LOG.stat().st_size if LOG.exists() else 0
    wait_for = max(5.0, min(ATTEMPT_TIMEOUT, budget))
    t0 = time.time()
    lf = LOG.open("ab")
    try:
        p = subprocess.Popen(cmd, cwd=str(ROOT), stdout=lf, stderr=subprocess.STDOUT,
                             env={**os.environ, **extra_env},
                             shell=(os.name == "nt" and cmd[0].lower().endswith((".cmd", ".bat"))),
                             creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0)
    except OSError as e:
        log(f"chain step {entry}: spawn failed: {e}")
        lf.close()
        cli_pool.report(entry, 1, str(LOG), base_offset, 0.1)
        return ""
    deadline = t0 + wait_for
    text = ""
    while time.time() < deadline:
        text = valid_reply(reply_file)
        if text or p.poll() is not None:
            break
        time.sleep(1)
    elapsed = time.time() - t0
    if p.poll() is None:
        try:
            p.terminate()
        except OSError:
            pass
        try:
            p.wait(timeout=8)
        except subprocess.TimeoutExpired:
            try:
                p.kill()
            except OSError:
                pass
    lf.close()
    text = valid_reply(reply_file)
    cli_pool.report(entry, 0 if text else 1, str(LOG), base_offset, elapsed)
    record_latency(entry, elapsed, bool(text))
    if text:
        log(f"chain answered by {entry} in {elapsed:.0f}s")
        return text
    log(f"chain step {entry} gave no valid reply in {elapsed:.0f}s, moving to the next")
    return ""


def brain(prompt_file: Path, reply_tag: str) -> bool:
    """Walk the ordered chain once, best model first, and stop at the first valid reply.
    A dead quota, 401, timeout, crash or empty reply on one step only moves the chain on.
    The whole walk is capped at MAX_TOTAL seconds (owner: bounded latency)."""
    entries = chain_entries()
    if not entries:
        log("chain empty: every free tool is cooling down")
        return False
    deadline = time.time() + MAX_TOTAL
    for i, (entry, _tool, _model, label) in enumerate(entries):
        budget = deadline - time.time()
        if budget < 5:
            log("chain budget used up, stopping")
            break
        log(f"chain step {i + 1}/{len(entries)}: {entry} ({label})")
        stage("thinking", f"{i + 1}/{len(entries)} {label}")
        text = try_entry(entry, prompt_file, reply_tag, i, budget)
        if text:
            (DIR / f"reply-{reply_tag}.txt").write_text(text, encoding="utf-8")
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
        f = download_with_retry(file_id, MEDIA / f"voice-{tag}-{item.get('id', 'x')}.ogg")
        heard = transcribe(f)
        if not heard:
            lines.append("[voice message - transcription failed, ask him to resend or type it]")
        else:
            text = (heard + ("\n" + text if text else "")).strip()
            lines.append(f"[voice message, transcribed from Egyptian Arabic/English, can contain small errors - understand the intent: {heard}]")
            note = f"(voice note transcribed automatically, audio saved at {f.as_posix()})"
    elif kind == "photo" and file_id:
        f = download_with_retry(file_id, MEDIA / f"photo-{tag}-{item.get('id', 'x')}.jpg")
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
        f = download_with_retry(file_id, MEDIA / f"doc-{tag}-{item.get('file_name') or item.get('id', 'x')}")
        lines.append(f"[document Ahmed sent: {item.get('file_name', f.name)}, saved at {f.as_posix()}]")
        if text:
            lines.append(f"[text with the document: {text}]")
        note = f"(document saved at {f.as_posix()})"
    elif text:
        lines.append(f"[text: {text}]")
    else:
        lines.append("[message with no readable text]")
    return {"lines": lines, "note": note, "kind": kind, "text": text}


def prepare_failure(item: dict, exc: Exception) -> dict:
    kind = item.get("kind", "text")
    text = item.get("text", "") or item.get("caption", "")
    lines = [f"[message could not be prepared: kind={kind}; error={clean_error(exc)}]"]
    if text:
        lines.append(f"[text fallback: {text}]")
    return {"lines": lines, "note": "", "kind": kind,
            "text": text or f"[{kind} message - preparation failed: {clean_error(exc)}]"}


def ack_text(items: list[dict]) -> str:
    kinds = {str(it.get("kind", "text")) for it in items}
    if kinds == {"voice"}:
        return "وصلت الفويس. بفهمه وأرد عليك."
    if kinds == {"photo"}:
        return "وصلت الصورة. بفهمها وأرد عليك."
    if kinds == {"document"}:
        return "وصلت الملف. بفهمه وأرد عليك."
    if kinds <= {"voice", "photo", "document"}:
        return "وصلت الرسايل. بفهمها وأرد عليك."
    return "تمام، وصلت رسالتك."


def _google_chat(model: str, system: str, user: str) -> str:
    """Google AI Studio chat through its own generateContent shape (the OpenAI-compatible
    path proved unreliable, its alias answer is the same state text either way)."""
    key = KEYS.get("GOOGLE_AI_STUDIO_KEY", "")
    body = json.dumps({
        "systemInstruction": {"parts": [{"text": system}]},
        "contents": [{"role": "user", "parts": [{"text": user}]}],
        "generationConfig": {"temperature": 0.3, "maxOutputTokens": 1200},
    }).encode("utf-8")
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}",
        data=body, headers={"Content-Type": "application/json", "User-Agent": "sir-hq/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    return data["candidates"][0]["content"]["parts"][0]["text"].strip()


def _llm_chat(url: str, key: str, model: str, system: str, user: str) -> str:
    body = json.dumps({"model": model, "temperature": 0.3, "max_tokens": 1200,
                       "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]}).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json", "User-Agent": "sir-hq/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))["choices"][0]["message"]["content"].strip()


def direct_reply(body: str, notes: str):
    """Fast conversational answer (a few seconds) from a strong free model with no tools, so the owner is never left waiting
    while an agent with file tools starts up. It also says whether real work is needed (then the agent path runs after it)."""
    try:
        state = ""
        for rel, n in (("ops/HQ_CHECKPOINT.md", 3500), (".sir/CHECKPOINT.md", 2000)):
            p = ROOT / rel
            if p.exists():
                state += f"\n--- {rel} (tail)\n" + p.read_text(encoding="utf-8", errors="ignore")[-n:]
        board = subprocess.run([sys.executable, str(ROOT / "scripts" / "taskboard.py"), "list"], capture_output=True, text=True, timeout=20).stdout[-1500:]
        live = subprocess.run([sys.executable, str(ROOT / "scripts" / "ai-status.py")], capture_output=True, text=True, timeout=40).stdout[:3500]
        state += "\n--- LIVE STATUS right now (trust this over any older text; the free tools are working when runner pids are listed; a model cooling down is normal and the next one takes over)\n" + live
        system = (PERSONA.read_text(encoding="utf-8") +
                  "\n\n## Mode: fast chat answer\nYou cannot run tools in this step. Answer Ahmed directly and honestly from the state below. "
                  "If he asks for work to be done or checked on the computer, say what you will do and set needs_agent true. "
                  'Output ONLY compact JSON: {"reply": "<Egyptian Arabic, short, ends with the line المطلوب منك: ...>", "needs_agent": true or false}.\n'
                  f"\n## Current state\n{state}\n## Task board\n{board}\n")
        user = f"Recent chat:\n{history()}\n\nNew burst from Ahmed (oldest first):\n{body}\n{notes}"
        # ordered best to worst as well: the first healthy provider answers the fast line,
        # the next takes over on its own when a limit or an error appears (owner order 2026-11-13)
        providers = []
        if KEYS.get("GROQ_API_KEY"):
            providers.append(("https://api.groq.com/openai/v1/chat/completions", KEYS["GROQ_API_KEY"], "openai/gpt-oss-120b"))
        if KEYS.get("OPENROUTER_API_KEY"):
            providers.append(("https://openrouter.ai/api/v1/chat/completions", KEYS["OPENROUTER_API_KEY"], "nvidia/nemotron-3-ultra-550b-a55b:free"))
        if KEYS.get("NVIDIA_API_KEY"):
            providers.append(("https://integrate.api.nvidia.com/v1/chat/completions", KEYS["NVIDIA_API_KEY"], "nvidia/nemotron-3-ultra-550b-a55b"))
        if KEYS.get("GOOGLE_AI_STUDIO_KEY"):
            providers.append(("google-generateContent", KEYS["GOOGLE_AI_STUDIO_KEY"], "gemini-3.8-flash"))
        for url, key, model in providers:
            try:
                if url == "google-generateContent":
                    raw = _google_chat(model, system, user)
                else:
                    raw = _llm_chat(url, key, model, system, user)
                m = re.search(r"\{.*\}", raw, re.S)
                data = json.loads(m.group(0)) if m else {"reply": raw, "needs_agent": False}
                reply = str(data.get("reply", "")).strip()
                bad = reply_problem(reply) if reply else "empty"
                if bad:
                    log(f"direct reply rejected from {model}: {bad}")
                    continue
                log(f"direct reply from {model}")
                return {"reply": reply, "needs_agent": bool(data.get("needs_agent"))}
            except Exception as e:  # noqa: BLE001
                log(f"direct reply {model} failed: {clean_error(e)}")
    except Exception as e:  # noqa: BLE001
        log(f"direct reply error: {clean_error(e)}")
    return None


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
            stage("direct", "fast answer from a strong model")
            direct = direct_reply(body, notes)
            if direct:
                send(direct["reply"])
                remember("Manager", direct["reply"])
                if not direct.get("needs_agent"):
                    return 0
                send("بنفذ الشغل ده دلوقتي بأداة بتشتغل على الملفات وهبلغك أول ما يخلص.")
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
