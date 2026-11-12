#!/usr/bin/env python3
"""Daily scout for sir-jobs (thin wrapper around scripts/scout.py; see that file for the rules)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scout

if __name__ == "__main__":
    sys.exit(scout.main(["sir-jobs"] + sys.argv[1:]))
