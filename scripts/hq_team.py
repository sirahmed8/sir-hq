"""Shared helpers for the r42 free-agent team (verifier, scouts, review loop, notifications).

Everything here runs on free models through the shared pool (scripts/cli_pool.py), never on Claude.
No secrets are printed. AHome private content is never read: only source, tests and screenshots.

Usage from the other r42 scripts:
    from hq_team import ROOT, OPS, PROJECTS, log, pool_pick, pool_report, run_agent
"""
import nowindow  # noqa: F401  (no console windows for child processes)
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(os.environ.get("SIR_ROOT", "D:/Projects/_SIR"))
OPS = ROOT / "ops"
LOCAL = ROOT / "_local"
QUEUE_FILE = OPS / "AUTOPILOT_QUEUE.json"
SUGGESTIONS_FILE = OPS / "SUGGESTIONS.md"
LESSONS_FILE = OPS / "LESSONS.md"
REJECTS_FILE = OPS / "suggestion-rejects.json"
OUTBOX = OPS / "bus" / "telegram-outbox.md"
GAME_FILE = Path("D:/Projects/SIR Laptop Manager/.sir/game_mode_snapshot.json")
POOL_SCRIPT = ROOT / "scripts" / "cli_pool.py"
QUEUE_ADD = ROOT / "scripts" / "queue-add.py"
NO_WINDOW = 0x08000000

# One entry per scout (brief item 2). key -> (display name, project folder)
PROJECTS = {
    "ahome": ("AHome", "D:/Projects/AHome"),
    "sir-study": ("SIR Study", "D:/Projects/SIR Study"),
    "sir-jobs": ("SIR Jobs", "D:/Projects/SIR Jobs"),
    "sir-laptop-manager": ("SIR Laptop Manager", "D:/Projects/SIR Laptop Manager"),
    "sir-ai": ("SIR AI", "D:/Projects/SIR AI"),
    "sir-portfolio": ("SIR Portfolio", "D:/Projects/SIR Portfolio"),
    "sir-hq": ("_SIR", "D:/Projects/_SIR"),
}


def log(name: str, msg: str) -> None:
    """Append one timestamped line to ops/<name>.log."""
    path = OPS / f"{name}.log"
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")
    except OSError:
        pass


def read_text(path, default: str = "") -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return default


def load_json(path, default):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def save_json(path, data) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def game_mode_active() -> bool:
    """True while a game runs: every automation pauses (owner rule 2026-11-11)."""
    return GAME_FILE.exists()


def lower_priority() -> None:
    """Run this process at below-normal priority so the owner's work stays smooth (Windows only)."""
    if os.name != "nt":
        return
    try:
        import ctypes

        below_normal = 0x00004000
        handle = ctypes.windll.kernel32.GetCurrentProcess()
        ctypes.windll.kernel32.SetPriorityClass(handle, below_normal)
    except Exception:
        pass


def load_queue() -> list:
    rows = load_json(QUEUE_FILE, [])
    return rows if isinstance(rows, list) else []


def save_queue(queue: list) -> None:
    save_json(QUEUE_FILE, queue)


def queue_names() -> set:
    return {str(t.get("name", "")).lower() for t in load_queue()}


def pool_pick(exclude: tuple = ()) -> str:
    """Return '<tool>|<model>' from the shared pool, or '' when every model is cooling down."""
    try:
        args = [sys.executable, str(POOL_SCRIPT), "pick"]
        if exclude:
            args.append("--exclude=" + ",".join(exclude))
        res = subprocess.run(args, capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired) as exc:
        log("team", f"pool pick failed: {exc!r}")
        return ""
    pick = (res.stdout or "").strip().splitlines()
    value = pick[0].strip() if pick else ""
    if not value or value.startswith("WAIT") or "|" not in value:
        return ""
    return value


def pool_report(pick: str, code: int, log_file: Path, offset: int = 0, seconds: float = 0) -> None:
    try:
        subprocess.run([sys.executable, str(POOL_SCRIPT), "report", pick, str(code), str(log_file),
                        str(offset), str(seconds)], capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        pass


def _exe(name: str) -> str:
    """Resolve a CLI name to a real file. Windows does not apply PATHEXT in CreateProcess, so 'opencode'
    fails while 'opencode.cmd' works; shutil.which fixes that for every pool tool."""
    if os.path.isabs(name):
        return name
    return shutil.which(name) or name


def agent_command(pick: str, prompt: str) -> list:
    """Build the headless command for a pool entry. Same table as scripts/cli-run2.sh."""
    tool, model = pick.split("|", 1)
    commands = {
        "kilo": ["kilo", "run", "--auto", "-m", model, prompt],
        "opencode": ["opencode", "run", "-m", model, prompt],
        "devin": [str(Path.home() / "AppData/Local/devin/cli/bin/devin.exe"), "-p", "--model", model,
                  "--permission-mode", "dangerous", "--respect-workspace-trust", "false", "--", prompt],
        "codex": ["codex", "exec", "--skip-git-repo-check", "--dangerously-bypass-approvals-and-sandbox",
                  "-m", model, prompt],
        "agy": ["agy", "--print", prompt, "--model", model, "--dangerously-skip-permissions"],
        "qwen": ["qwen", "-p", prompt, "--auth-type", "openai"],
        "goose": ["goose", "run", "-t", prompt],
        "crush": ["crush", "run", "-m", model, prompt],
        "cline": ["cline", "-P", "cline", "--thinking", "high", "-p", "--yolo", "-m", model, prompt],
        "gemini": ["gemini", "-p", prompt, "--yolo", "--skip-trust"],
        "aider": [
            "aider", "--model", model, "--yes-always",
            "--no-show-model-warnings", "--no-show-release-notes",
            "--no-check-update", "--no-detect-urls", "--no-browser",
            "--analytics-disable", "--message", prompt,
        ],
        "kimi": ["kimi", "-p", prompt, "--yolo"],
        "pi": [str(Path.home() / ".pi/agent/bin/pi.cmd"), "-p", "--no-session", "--model", model, prompt],
    }
    cmd = commands.get(tool, [])
    if cmd:
        cmd = [_exe(cmd[0])] + cmd[1:]
    return cmd


def run_agent(pick: str, prompt: str, cwd, tag: str, timeout: int = 1800) -> tuple:
    """Run one free model headless. Returns (code, combined output, log path)."""
    cmd = agent_command(pick, prompt)
    log_file = OPS / "agy-runs" / f"{tag}-{int(time.time())}.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    if not cmd:
        log("team", f"unknown tool in pool entry: {pick}")
        return 127, f"unknown tool: {pick}", log_file

    env = os.environ.copy()
    tool, model = pick.split("|", 1)
    if tool == "aider":
        keys = {}
        try:
            for line in open("D:/Projects/_SIR/_local/api-keys.env", encoding="utf-8"):
                if "=" in line:
                    k, v = line.strip().split("=", 1)
                    keys[k] = v
        except OSError:
            pass
        if model.startswith("gemini/"):
            env["GEMINI_API_KEY"] = keys.get("GOOGLE_AI_STUDIO_KEY", "")
        elif model.startswith("nvidia_nim/"):
            env["NVIDIA_NIM_API_KEY"] = keys.get("NVIDIA_API_KEY", "")
        elif model.startswith("openai/@cf/"):
            env["OPENAI_API_BASE"] = f"https://api.cloudflare.com/client/v4/accounts/{keys.get('CLOUDFLARE_ACCOUNT_ID', '')}/ai/v1"
            env["OPENAI_API_KEY"] = keys.get("CLOUDFLARE_API_TOKEN", "")
        elif model == "openai/GLM-5.3":
            env["OPENAI_API_BASE"] = "https://api.sambanova.ai/v1"
            env["OPENAI_API_KEY"] = keys.get("SAMBANOVA_API_KEY", "")
        for k in ("GROQ_API_KEY", "CEREBRAS_API_KEY", "MISTRAL_API_KEY", "COHERE_API_KEY", "OPENROUTER_API_KEY"):
            if k in keys:
                env[k] = keys[k]
        env["BROWSER"] = "true"
    if tool == "qwen":
        env.update({"OPENAI_BASE_URL": "http://localhost:11434/v1", "OPENAI_API_KEY": "ollama",
                    "OPENAI_MODEL": model})
    elif tool == "goose":
        env.update({"GOOSE_PROVIDER": "ollama", "GOOSE_MODEL": model})

    started = time.time()
    try:
        res = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=timeout, env=env,
                             creationflags=NO_WINDOW)
        code, out = res.returncode, (res.stdout or "") + (res.stderr or "")
    except subprocess.TimeoutExpired:
        code, out = 124, "timeout"
    except (OSError, FileNotFoundError) as exc:
        code, out = 127, f"{exc!r}"
    log_file.write_text(out, encoding="utf-8", errors="replace")
    pool_report(pick, code, log_file, 0, time.time() - started)
    return code, out, log_file


def lessons_text(limit: int = 9000) -> str:
    """The shared cross-project rules every verifier and scout checks against."""
    text = read_text(LESSONS_FILE)
    return text[:limit] if text else "NO LESSONS FILE"


def normalize(text: str) -> str:
    """Lowercase alphanumeric key used for dedupe."""
    return re.sub(r"[^a-z0-9\u0600-\u06ff]+", " ", (text or "").lower()).strip()


def finding_key(finding: str) -> str:
    return hashlib.sha1(normalize(finding).encode("utf-8")).hexdigest()[:8]


def suggestion_id(finding: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", (finding or "").lower()).strip("-")[:32] or "finding"
    return f"sug-{slug}-{finding_key(finding)}"


FIELD_ORDER = ("Finding", "Evidence", "Proposed Brief", "Project", "Severity", "Category", "Status",
               "HQ Note", "Id")


def parse_suggestions(text: str) -> list:
    """Split ops/SUGGESTIONS.md into entries. Keeps unknown lines in 'extra' so rewrites lose nothing."""
    entries = []
    blocks = re.split(r"(?m)^## ", text)
    for block in blocks[1:]:
        lines = block.splitlines()
        header = lines[0].strip()
        fields, extra = {}, []
        for line in lines[1:]:
            m = re.match(r"\*\*([A-Za-z ]+):\*\*\s*(.*)$", line.strip())
            if m and m.group(1).strip() in FIELD_ORDER:
                fields[m.group(1).strip()] = m.group(2).strip()
            elif line.strip() not in ("---", ""):
                extra.append(line.rstrip())
        finding = fields.get("Finding", "")
        if not finding or finding.startswith("<") or "<" in header:
            continue
        entries.append({
            "header": header,
            "fields": fields,
            "extra": extra,
            "id": fields.get("Id") or suggestion_id(finding),
        })
    return entries


def render_entry(entry: dict) -> str:
    fields = dict(entry["fields"])
    fields.setdefault("Status", "pending")
    fields["Id"] = entry["id"]
    lines = [f"## {entry['header']}", ""]
    for name in FIELD_ORDER:
        if name in fields and fields[name] != "":
            lines.append(f"**{name}:** {fields[name]}")
    lines.extend(entry.get("extra", []))
    lines.extend(["", "---", ""])
    return "\n".join(lines)


def rewrite_suggestions(entries: list) -> None:
    head = ("# Suggestions from Scouts (HQ)\n\n"
            "Scouts append findings here daily. HQ (manager) reads each watch, approves good items by running "
            "`scripts/queue-add.py`, and rejects the rest with a reason in this same file. Items the owner rejects "
            "through Telegram buttons are recorded in `ops/suggestion-rejects.json` and never proposed again.\n\n"
            "Format: `## <timestamp> | <project> | <severity>` then Finding, Evidence, Proposed Brief, Project, "
            "Severity, Category, Status (pending/approved/rejected), HQ Note, Id.\n\n---\n\n")
    body = "".join(render_entry(entry) for entry in entries)
    SUGGESTIONS_FILE.parent.mkdir(parents=True, exist_ok=True)
    SUGGESTIONS_FILE.write_text(head + body, encoding="utf-8")


def load_suggestions() -> list:
    return parse_suggestions(read_text(SUGGESTIONS_FILE))


def load_rejects() -> list:
    rows = load_json(REJECTS_FILE, [])
    return rows if isinstance(rows, list) else []


def add_reject(finding: str, reason: str) -> None:
    rows = load_rejects()
    key = finding_key(finding)
    if any(r.get("key") == key for r in rows):
        return
    rows.append({"key": key, "finding": finding, "reason": reason,
                 "at": time.strftime("%Y-%m-%dT%H:%M:%S")})
    save_json(REJECTS_FILE, rows)


def is_rejected(finding: str) -> bool:
    key = finding_key(finding)
    norm = normalize(finding)
    for row in load_rejects():
        if row.get("key") == key or (norm and norm == normalize(row.get("finding", ""))):
            return True
    return False


def dedupe_index() -> list:
    """Normalized keys of everything already known: open queue names/titles, suggestions, rejects."""
    keys = []
    for task in load_queue():
        keys.append(normalize(task.get("name", "")))
        keys.append(normalize(task.get("title", "")))
    for entry in load_suggestions():
        keys.append(normalize(entry["fields"].get("Finding", "")))
        keys.append(normalize(entry["fields"].get("Proposed Brief", "")))
    for row in load_rejects():
        keys.append(normalize(row.get("finding", "")))
    return [k for k in keys if k]


def is_duplicate(finding: str, proposed_brief: str = "") -> bool:
    """True when a scout finding is already an open task, a recorded suggestion or a rejected item."""
    norm = normalize(finding)
    brief = normalize(proposed_brief)
    if not norm:
        return True
    for key in dedupe_index():
        if key == brief and brief:
            return True
        shorter, longer = (norm, key) if len(norm) <= len(key) else (key, norm)
        if len(shorter) >= 24 and shorter in longer:
            return True
    return False


def notify_owner(text: str, tag: str, hours: int = 3) -> bool:
    """Send one plain message to Ahmed, unless the same tag was sent in the last hours.

    Format rules (WORKER_PREAMBLE 12): short title first, at most 5 one-fact lines, plain words.
    """
    recent = read_text(OUTBOX).splitlines()[-15:]
    cutoff = time.time() - hours * 3600
    for line in recent:
        if f"| {tag} |" in line:
            try:
                stamp = line.split("|")[0].strip().replace("Z", "+00:00")
                from datetime import datetime
                sent = datetime.fromisoformat(stamp).timestamp()
            except (ValueError, IndexError):
                sent = time.time()
            if sent >= cutoff:
                log("notify", f"skip: {tag} already sent recently")
                return False
    script = ROOT / "scripts" / "deliver" / "send-telegram.mjs"
    if not script.exists():
        log("notify", "send-telegram.mjs missing")
        return False
    try:
        res = subprocess.run(["node", str(script), text], capture_output=True, text=True, timeout=120,
                             creationflags=NO_WINDOW)
    except (OSError, subprocess.TimeoutExpired) as exc:
        log("notify", f"send failed: {exc!r}")
        return False
    ok = res.returncode == 0 and "FAILED" not in (res.stdout or "")
    if ok:
        stamp = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
        summary = text.splitlines()[0][:90] if text.strip() else tag
        try:
            with open(OUTBOX, "a", encoding="utf-8") as fh:
                fh.write(f"{stamp} | {tag} | {summary}\n")
        except OSError:
            pass
    log("notify", f"{tag}: {'sent' if ok else 'failed ' + (res.stdout or '')[:120]}")
    return ok
