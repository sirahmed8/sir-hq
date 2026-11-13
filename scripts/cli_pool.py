"""Shared pool of free coding models for scripts/cli-run2.sh (one state file for every task).

pick [local]              -> prints "tool|model" of the first model not cooling down, or "WAIT <seconds>".
                             "local" lists only local Ollama models (private work, e.g. AHome: never an outside provider)
report <entry> <code> <log> <offset> <seconds>
                          -> reads the log from byte <offset>; only error lines are read for limits and setup
                             problems (worker output that merely mentions "quota" or "unauthorized" is ignored).
                             Usage-limit text puts the entry on a 60 minute cooldown; the OpenRouter daily free
                             cap ("free-models-per-day") puts every openrouter/ entry on cooldown until 00:00 UTC
                             (all :free models of one OpenRouter account share one daily cap); a run that failed
                             within 90 seconds on 15 minutes; a refusal to run tools (permission rejected) or
                             auth/missing setup on 6 hours; a good run clears the cooldown
status                    -> table of every entry with its cooldown
State: ops/agy-runs/model-pool.json. Order = strongest first. Edit POOL to add or remove models.
"""
import nowindow  # noqa: F401  (no console windows for child processes)
import json
import re
import sys
import time
from pathlib import Path

STATE = Path("D:/Projects/_SIR/ops/agy-runs/model-pool.json")
POOL = [
    "kilo|kilo/kilo-auto/free",
    "opencode|opencode/big-pickle",
    "devin|swe-2-flash-medium",
    "cursor|auto",
    "pi|groq/openai/gpt-oss-120b",
    "pi|radius/recursive/flint",
    "kilo|kilo/nvidia/nemotron-3-ultra-550b-a55b:free",
    "opencode|opencode/glm-5.3-flash-free",
    "opencode|opencode/deepseek-v4.1-flash-free",
    "opencode|opencode/minimax-m3.1-flash-free",
    "opencode|opencode/mimo-v2.6-flash-free",
    "opencode|opencode/nemotron-3.5-lightning-free",
    "opencode|opencode/flint-40b-free",
    "opencode|opencode/longcat-2.5-free",
    "opencode|opencode/beam-free",
    "agy|gemini-3.8-flash-low",
    "agy|gemini-3.8-flash-medium",
    "agy|gemini-3.8-flash-high",
    "agy|gpt-oss-120b-medium",
    "agy|claude-sonnet-4-6",
    "cline|reflection/beam-free",
    "aider|groq/openai/gpt-oss-120b",
    "aider|nvidia_nim/nvidia/nemotron-3-ultra-550b-a55b",
    "aider|openai/@cf/openai/gpt-oss-120b",
    "aider|gemini/gemini-flash-lite-latest",
    "aider|gemini/gemini-flash-latest",
]
LOCAL_TOOLS = {"qwen", "goose", "crush"}
LIMIT = re.compile(r"usage limit|rate limit|too many requests|quota|out of credits|hit your usage limit|\b429\b", re.I)
OPENROUTER_DAY = re.compile(r"free-models-per-day", re.I)
REFUSED = re.compile(r"rejected a tool call that requires confirmation", re.I)
ERROR_LINE = re.compile(
    r"error|retrying|exceeded|hit your|usage limit|no model configured|no auth type|no providers configured|"
    r"command not found|not recognized as|No such file",
    re.I,
)
NEEDS_SETUP = re.compile(
    r"no auth type is selected|no providers configured|unauthorized|please .*re-?authenticate|"
    r"no model configured|run [`']?kimi[`']? and use /login|not supported for gemini code assist|"
    r"client is no longer supported|command not found|is not recognized as|No such file or directory",
    re.I,
)


def load() -> dict:
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save(data: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2), encoding="utf-8")
    tmp.replace(STATE)


def is_local(entry: str) -> bool:
    tool, _, model = entry.partition("|")
    return tool in LOCAL_TOOLS and (model.startswith("ollama/") or ":" in model)


def next_utc_midnight(now: float) -> float:
    return (int(now // 86400) + 1) * 86400


def pick(local_only: bool = False) -> str:
    data, now = load(), time.time()
    entries = [e for e in POOL if is_local(e)] if local_only else POOL
    if not entries:
        return "WAIT 3600"
    # load balancing (owner, 2026-11-12): the free tools must all work, so choose the available entry used longest ago
    # instead of always the first one (the first one, Devin, was doing nearly everything while the others sat idle)
    available = [e for e in entries if data.get(e, {}).get("until", 0) <= now]
    if available:
        entry = min(available, key=lambda e: (data.get(e, {}).get("last_pick", 0), POOL.index(e)))
        data.setdefault(entry, {})["last_pick"] = now
        save(data)
        return entry
    soonest = min(data.get(e, {}).get("until", 0) for e in entries)
    return f"WAIT {int(max(soonest - now, 60))}"


def report(entry: str, code: int, log: str, offset: int, seconds: float) -> str:
    data, now = load(), time.time()
    rec = data.setdefault(entry, {})
    try:
        with open(log, "rb") as fh:
            fh.seek(offset)
            text = fh.read().decode("utf-8", "ignore")
    except OSError:
        text = ""
    errtext = "\n".join(line for line in text[-20000:].splitlines() if ERROR_LINE.search(line))[-8000:]
    refused = len(REFUSED.findall(text))
    limited = len(LIMIT.findall(errtext)) >= 1 and code != 0
    needs_setup = len(NEEDS_SETUP.findall(errtext)) >= 1 and code != 0
    if refused >= 3 or needs_setup:
        rec.update(until=now + 6 * 3600, why="needs setup/auth or tools refused")
    elif code != 0 and OPENROUTER_DAY.search(errtext):
        end = next_utc_midnight(now)
        for other in POOL:
            if "openrouter/" in other:
                cur = data.setdefault(other, {})
                cur.update(until=max(cur.get("until", 0), end), why="openrouter daily free cap (shared)")
        rec.update(until=end, why="openrouter daily free cap (shared)")
    elif limited:
        rec.update(until=now + 3600, why="usage limit")
    elif code != 0 and seconds < 90:
        rec.update(until=now + 900, why=f"failed fast (exit {code})")
    else:
        rec.update(until=0, why="ok", last_ok=now)
    save(data)
    return rec["why"]


def status() -> None:
    data, now = load(), time.time()
    for entry in POOL:
        r = data.get(entry, {})
        left = int(max(r.get("until", 0) - now, 0) / 60)
        print(f"{'cooling ' + str(left) + ' min' if left else 'available':16} {entry:55} {r.get('why', '')}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "pick":
        print(pick(local_only="local" in sys.argv[2:]))
    elif cmd == "report":
        print(report(sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]), float(sys.argv[6])))
    else:
        status()
