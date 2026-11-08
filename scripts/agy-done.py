"""Completion signal for an Antigravity chat or CLI worker.

Usage: python agy-done.py <name> <ok|fail|blocked> "<one-line summary>"
Writes D:/Projects/_SIR/ops/agy-runs/done/<name>.done. The manager's watcher (Monitor) wakes on that file,
so nobody has to poll the chat.
"""

import sys, pathlib, datetime, json

DONE = pathlib.Path("D:/Projects/_SIR/ops/agy-runs/done")


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    name, status = sys.argv[1], sys.argv[2]
    summary = " ".join(sys.argv[3:])[:600]
    DONE.mkdir(parents=True, exist_ok=True)
    payload = {
        "name": name,
        "status": status,
        "summary": summary,
        "at": datetime.datetime.now().isoformat(timespec="seconds"),
    }
    (DONE / (name + ".done")).write_text(
        json.dumps(payload, ensure_ascii=False), encoding="utf-8"
    )
    print("signalled", name, status)
    return 0


if __name__ == "__main__":
    sys.exit(main())
