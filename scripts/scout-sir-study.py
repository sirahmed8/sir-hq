#!/usr/bin/env python3
"""Daily scout for sir-study (thin wrapper around scripts/scout.py; see that file for the rules)."""
import nowindow  # noqa: F401  (no console windows for child processes)
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scout

if __name__ == "__main__":
    sys.exit(scout.main(["sir-study"] + sys.argv[1:]))
