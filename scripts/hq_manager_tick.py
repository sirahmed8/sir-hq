"""Hourly fallback HQ manager (scheduled task SIR_HQ_ManagerTick).
If no manager note was appended to ops/HQ_CHECKPOINT.md for 50 minutes (Claude gone or asleep), a free model from the shared pool
runs ops/MANAGER_PROMPT.md in D:/Projects/_SIR. Usage: python hq_manager_tick.py [--dry]"""
import nowindow  # noqa: F401  (no console windows for child processes)
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path("D:/Projects/_SIR")
CHECKPOINT = ROOT / "ops" / "HQ_CHECKPOINT.md"
LOG = ROOT / "ops" / "manager_tick.log"
LOCK = ROOT / "ops" / "locks" / "hq-manager-tick.lock"
NO_WINDOW = 0x08000000


def log(msg: str) -> None:
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")


def main() -> None:
    if Path("D:/Projects/SIR Optimizer/.sir/game_mode_snapshot.json").exists():  # a game is running: stay quiet
        log("skip: game mode active")
        return
    dry = "--dry" in sys.argv
    age = (time.time() - CHECKPOINT.stat().st_mtime) / 60
    if age < 50 and not dry:
        log(f"skip: manager note {age:.0f} min old")
        return
    if LOCK.exists() and time.time() - LOCK.stat().st_mtime < 3000:
        log("skip: previous tick still running")
        return
    pick = subprocess.run([sys.executable, str(ROOT / "scripts/cli_pool.py"), "pick"], capture_output=True, text=True).stdout.strip()
    if pick.startswith("WAIT") or "|" not in pick:
        log(f"no model available: {pick}")
        return
    tool, model = pick.split("|", 1)
    prompt = (ROOT / "ops" / "MANAGER_PROMPT.md").read_text(encoding="utf-8")
    cmd = {
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
        "cline": ["cline", "-p", "--yolo", "-m", model, prompt],
        "gemini": ["gemini", "-p", prompt, "--yolo", "--skip-trust"],
        "aider": [
            "aider", "--model", model, "--yes-always",
            "--no-show-model-warnings", "--no-show-release-notes",
            "--no-check-update", "--no-detect-urls", "--no-browser",
            "--analytics-disable", "--message", prompt,
        ],
        "kimi": ["kimi", "-p", prompt, "--yolo"],
    }.get(tool)
    if cmd is None:
        log(f"skip: {tool} has no manager command")
        return
    # Windows CreateProcess does not apply PATHEXT, so a bare "opencode" fails; resolve the real file.
    cmd = [cmd[0] if Path(cmd[0]).is_absolute() else (shutil.which(cmd[0]) or cmd[0])] + cmd[1:]
    import os
    env = os.environ.copy()
    env["BROWSER"] = r"D:\Projects\_SIR\scripts\noop-browser.exe"
    if tool in ("qwen", "goose"):
        if tool == "qwen":
            env.update({"OPENAI_BASE_URL": "http://localhost:11434/v1", "OPENAI_API_KEY": "ollama", "OPENAI_MODEL": model})
        else:
            env.update({"GOOSE_PROVIDER": "ollama", "GOOSE_MODEL": model})
    log(f"{'DRY ' if dry else ''}start with {pick} (note age {age:.0f} min)")
    if dry:
        return
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    LOCK.write_text(pick)
    t0 = time.time()
    try:
        res = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, timeout=1500, creationflags=NO_WINDOW, env=env)
        out, code = (res.stdout + res.stderr), res.returncode
    except FileNotFoundError as e:
        out, code = str(e), 127
    except subprocess.TimeoutExpired:
        out, code = "usage timeout", 124
    LOCK.unlink(missing_ok=True)
    offset = 0
    tmp = ROOT / "ops" / "agy-runs" / "manager-last.log"
    tmp.write_text(out, encoding="utf-8")
    why = subprocess.run([sys.executable, str(ROOT / "scripts/cli_pool.py"), "report", pick, str(code), str(tmp), str(offset),
                          str(time.time() - t0)], capture_output=True, text=True).stdout.strip()
    log(f"finished code {code} ({why}) in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
