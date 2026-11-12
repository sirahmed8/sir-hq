"""Usage windows and heavy-round scheduling plan (r42 item 6).

Reads the real usage rows in ops/ACCOUNT_LEDGER.md (they are written by reading the tool's own usage banner,
never by sending a test message), keeps the newest reading per account and model family, and writes the
scheduling plan into ops/RUNNING_STATE.md between two markers.

Rule used for the plan: a heavy round (verification, full audit, UI overhaul) goes only to an account with at
least 50 percent left in both windows. Accounts with less stay on light work or wait for the reset.

Usage: python hq_usage_plan.py [--dry]
Exit code 0 when the plan was written (or would be, with --dry).
"""
import re
import sys
import time
from pathlib import Path

from hq_team import OPS, game_mode_active, log, read_text

NAME = "usage"
LEDGER = OPS / "ACCOUNT_LEDGER.md"
STATE = OPS / "RUNNING_STATE.md"
START = "<!-- r42-usage:start -->"
END = "<!-- r42-usage:end -->"
HEAVY_FLOOR = 50
# Reset facts the owner confirmed (kept here so the plan text never invents a time).
RESET_NOTES = [
    "Five-hour window resets at 10:00 (owner).",
    "Claude weekly resets 02:00 (owner).",
    "Antigravity free accounts reset weekly around 2026-11-17.",
    "Codex monthly limit resets around 2026-11-27.",
    "NotebookLM daily limit resets around 05:49.",
]


def percent(cell: str) -> int:
    """Read '65%' as 65; anything unreadable as -1 (unknown, never treated as room)."""
    match = re.search(r"(\d{1,3})\s*%", cell or "")
    if not match:
        return -1
    return max(0, min(100, int(match.group(1))))


def parse_ledger(text: str) -> list:
    """Newest reading per (account, models) from the ledger table."""
    rows = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 8 or cells[0].lower() == "time":
            continue
        if set(cells[1]) <= {"-", ":"} or set(cells[2]) <= {"-", ":"}:
            continue  # separator row
        rows.append({
            "time": cells[0],
            "account": cells[1],
            "models": cells[2],
            "five_hour": percent(cells[3]),
            "weekly": percent(cells[4]),
            "five_reset": cells[5],
            "weekly_reset": cells[6],
            "note": cells[7],
        })
    newest = {}
    for row in rows:
        key = (row["account"], row["models"])
        newest[key] = row  # file is appended newest last
    return list(newest.values())


def reading_age_days(time_cell: str) -> float:
    """Days since the reading was written, from the ledger's own time cell. -1 when unreadable."""
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})", time_cell or "")
    if not match:
        return -1
    try:
        read_at = time.mktime(time.strptime("-".join(match.groups()), "%Y-%m-%d"))
    except ValueError:
        return -1
    return (time.time() - read_at) / 86400


def plan_rows(rows: list, max_age_days: float = 2) -> tuple:
    heavy, light, stale = [], [], []
    for row in rows:
        if row["five_hour"] < 0 or row["weekly"] < 0:
            stale.append(row)
            continue
        age = reading_age_days(row["time"])
        if age < 0 or age > max_age_days:
            stale.append(row)
            continue
        if row["five_hour"] >= HEAVY_FLOOR and row["weekly"] >= HEAVY_FLOOR:
            heavy.append(row)
        else:
            light.append(row)
    return heavy, light, stale


def describe(row: dict) -> str:
    five = f"{row['five_hour']}%" if row["five_hour"] >= 0 else "unknown"
    weekly = f"{row['weekly']}%" if row["weekly"] >= 0 else "unknown"
    return f"{row['account']} / {row['models']}: 5h {five}, weekly {weekly} (read {row['time']})"


def build_section(rows: list) -> str:
    heavy, light, stale = plan_rows(rows)
    lines = [START, "## Usage windows & heavy-round plan (r42)", ""]
    lines.append("How the numbers are read: from the tool's own usage banner, never by sending a test message.")
    lines.extend(f"- {note}" for note in RESET_NOTES)
    lines.append("")
    if heavy:
        lines.append(f"Heavy rounds go to (at least {HEAVY_FLOOR}% left in both windows, read within 2 days):")
        lines.extend(f"- {describe(row)}" for row in heavy[:4])
    else:
        lines.append("Heavy rounds: no account has a fresh reading above the floor in both windows, so heavy work "
                     "waits for the next reset and only light work runs.")
    if light:
        lines.append("")
        lines.append("Light work only (one window is low):")
        lines.extend(f"- {describe(row)}" for row in light[:4])
    if stale:
        lines.append("")
        lines.append("Stale or unreadable: read the banner again before using these.")
        lines.extend(f"- {describe(row)}" for row in stale[:5])
    lines.append("")
    lines.append("Free CLI pool (kilo, opencode, devin, codex): separate from these accounts and used first for "
                 "verification and scout rounds.")
    lines.append(f"Plan written {time.strftime('%Y-%m-%d %H:%M')} by scripts/hq_usage_plan.py.")
    lines.append(END)
    return "\n".join(lines)


def write_plan(section: str, dry: bool) -> str:
    text = read_text(STATE)
    if START in text and END in text:
        head, rest = text.split(START, 1)
        _old, tail = rest.split(END, 1)
        new_text = head + section + tail
    else:
        new_text = text.rstrip() + "\n\n" + section + "\n"
    if not dry:
        STATE.write_text(new_text, encoding="utf-8")
    return new_text


def main(argv: list) -> int:
    if game_mode_active():
        log(NAME, "skip: game mode active")
        print("skip: game mode active")
        return 0
    dry = "--dry" in argv
    rows = parse_ledger(read_text(LEDGER))
    if not rows:
        print("no usage rows in ops/ACCOUNT_LEDGER.md")
        return 1
    section = build_section(rows)
    write_plan(section, dry)
    heavy, light, stale = plan_rows(rows)
    log(NAME, f"plan written: heavy {len(heavy)}, light {len(light)}, stale {len(stale)}")
    print(f"heavy={len(heavy)} light={len(light)} stale={len(stale)} dry={dry}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
