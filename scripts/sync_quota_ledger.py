#!/usr/bin/env python3
"""
sync_quota_ledger.py - Automated Quota Ledger Sync Daemon (Task HQ-02)
Target: ops/ACCOUNT_LEDGER.md & ops/ACCOUNT_ROTATION.md
Maintains immutable ledger of AI provider quotas, evaluates 15% thresholds,
and recommends next rotation candidate.
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path
from datetime import datetime, timezone

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DEFAULT_LEDGER_PATH = REPO_ROOT / "ops" / "ACCOUNT_LEDGER.md"

# Priority rotation candidate list per ops/ACCOUNT_ROTATION.md
ROTATION_PRIORITY = [
    "a7medorabe7",
    "ahmedalaa2006.7.6",
    "1sir1ahmed1",
    "a01083835229"
]

def parse_percentage(val_str: str) -> float | None:
    """Parses '15%' or '15' into float 15.0."""
    if not val_str:
        return None
    m = re.search(r"(\d+(?:\.\d+)?)\s*%", val_str)
    if m:
        return float(m.group(1))
    try:
        return float(val_str)
    except ValueError:
        return None

def append_ledger_entry(
    ledger_path: Path,
    account: str,
    models: str,
    five_hour_left: str,
    weekly_left: str,
    five_hour_resets: str = "-",
    weekly_resets: str = "-",
    note: str = ""
) -> bool:
    """Appends a formatted row to ops/ACCOUNT_LEDGER.md table."""
    if not ledger_path.exists():
        header = (
            "# Account ledger (usage and reset times)\n"
            "Updated by the Haiku operator at every check (append rows; newest last). "
            "Columns: time, account, model family, 5h left, weekly left, 5h resets in, weekly resets in, note.\n"
            "| time | account | models | 5h left | weekly left | 5h resets | weekly resets | note |\n"
            "|---|---|---|---|---|---|---|---|\n"
        )
        ledger_path.write_text(header, encoding="utf-8")

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    row = f"| {now_str} | {account} | {models} | {five_hour_left} | {weekly_left} | {five_hour_resets} | {weekly_resets} | {note} |\n"

    with open(ledger_path, "a", encoding="utf-8") as f:
        f.write(row)
    return True

def evaluate_rotation_needed(weekly_left_str: str, five_hour_left_str: str, threshold: float = 15.0) -> tuple[bool, str]:
    """
    Evaluates whether quota requires account rotation.
    Returns (needs_rotation, reason).
    """
    w_pct = parse_percentage(weekly_left_str)
    h_pct = parse_percentage(five_hour_left_str)

    reasons = []
    if w_pct is not None and w_pct <= threshold:
        reasons.append(f"Weekly quota is {w_pct:.0f}% (threshold <= {threshold:.0f}%)")
    if h_pct is not None and h_pct <= threshold:
        reasons.append(f"5-hour quota is {h_pct:.0f}% (threshold <= {threshold:.0f}%)")

    if reasons:
        return True, " AND ".join(reasons)
    return False, "Quota healthy (> 15%)"

def main():
    parser = argparse.ArgumentParser(description="Synchronize and evaluate AI quota ledger.")
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER_PATH, help="Path to ACCOUNT_LEDGER.md")
    parser.add_argument("--account", type=str, required=True, help="Account label (e.g. ahmedalaa2006.7.6)")
    parser.add_argument("--models", type=str, default="Gemini 3.8", help="Model family")
    parser.add_argument("--five-hour", type=str, required=True, help="5-hour quota remaining (e.g. '80%%' or '80')")
    parser.add_argument("--weekly", type=str, required=True, help="Weekly quota remaining (e.g. '24%%' or '24')")
    parser.add_argument("--resets-5h", type=str, default="-", help="Time until 5h reset")
    parser.add_argument("--resets-weekly", type=str, default="-", help="Time until weekly reset")
    parser.add_argument("--note", type=str, default="", help="Optional notes on account state")
    parser.add_argument("--check-only", action="store_true", help="Only check rotation status without appending row")

    args = parser.parse_args()

    needs_rot, reason = evaluate_rotation_needed(args.weekly, args.five_hour)

    if not args.check_only:
        append_ledger_entry(
            ledger_path=args.ledger,
            account=args.account,
            models=args.models,
            five_hour_left=args.five_hour if "%" in args.five_hour else f"{args.five_hour}%",
            weekly_left=args.weekly if "%" in args.weekly else f"{args.weekly}%",
            five_hour_resets=args.resets_5h,
            weekly_resets=args.resets_weekly,
            note=args.note
        )
        print(f"Logged entry for {args.account} in {args.ledger.name}")

    if needs_rot:
        print(f"[ALERT: ROTATION REQUIRED] {reason}")
        print(f"Action: Rotate account immediately per ops/ACCOUNT_ROTATION.md")
        sys.exit(2)
    else:
        print(f"[STATUS: HEALTHY] {reason}")
        sys.exit(0)

if __name__ == "__main__":
    main()
