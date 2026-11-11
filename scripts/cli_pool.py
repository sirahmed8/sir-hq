"""Shared pool of free coding models for scripts/cli-run2.sh (one state file for every task).

pick                      -> prints "tool|model" of the first model not cooling down, or "WAIT <seconds>"
report <entry> <code> <log> <offset> <seconds>
                          -> reads the log from byte <offset>; usage-limit text puts the entry on a 60 minute
                             cooldown, a run that failed within 90 seconds on 15 minutes, a refusal to run tools
                             (permission rejected) on 6 hours; a good run clears the cooldown
status                    -> table of every entry with its cooldown
State: ops/agy-runs/model-pool.json. Order = strongest first. Edit POOL to add or remove models.
"""
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
    "kilo|kilo/nvidia/nemotron-3-ultra-550b-a55b:free",
    "opencode|opencode/glm-5.3-flash-free",
    "opencode|opencode/deepseek-v4.1-flash-free",
    "opencode|opencode/minimax-m3.1-flash-free",
    "opencode|opencode/mimo-v2.6-flash-free",
    "opencode|opencode/flint-40b-free",
    "opencode|opencode/longcat-2.5-free",
    "kilo|kilo/openrouter/free",
    "opencode|openrouter/openrouter/free",
    "agy|gemini-3.8-flash-low",
    "agy|gemini-3.8-flash-medium",
    "agy|gemini-3.8-flash-high",
    "agy|gpt-oss-120b-medium",
    "agy|claude-sonnet-4-6",
    "qwen|qwen3:8b",
    "goose|qwen3:8b",
    "qwen|qwen3:4b",
    "goose|qwen3:4b",
]
LIMIT = re.compile(r"usage limit|rate limit|too many requests|quota|out of credits|\b429\b", re.I)
REFUSED = re.compile(r"rejected a tool call that requires confirmation", re.I)


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


def pick() -> str:
    data, now = load(), time.time()
    for entry in POOL:
        if data.get(entry, {}).get("until", 0) <= now:
            return entry
    soonest = min(data.get(e, {}).get("until", 0) for e in POOL)
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
    refused = len(REFUSED.findall(text))
    limited = len(LIMIT.findall(text[-6000:])) >= 1 and code != 0
    if refused >= 3:
        rec.update(until=now + 6 * 3600, why="tool calls refused (permission mode)")
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
        print(pick())
    elif cmd == "report":
        print(report(sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]), float(sys.argv[6])))
    else:
        status()
