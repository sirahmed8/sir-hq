"""Builds D:/Projects/_SIR/ops/dashboard.html (the SIR Control Room page) from the real project files.
Run: python D:/Projects/_SIR/plans/generate_dashboard.py, then HQ republishes the artifact (same file path).
AHome is private: counts and status only, never task text or notes.
Truth rule: Every project is being rebuilt from zero. A project is only 'verified' if verified end-to-end today."""
import os
from dashboard_main import main as _main
from dashboard_main import parse_suggestions as _parse_suggestions
from dashboard_main import parse_verifications as _parse_verifications

OPS = os.environ.get("SIR_OPS", os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "ops")))

__all__ = ["OPS", "main", "parse_suggestions", "parse_verifications"]


def main():
    _main()


def parse_verifications():
    return _parse_verifications(OPS)


def parse_suggestions():
    return _parse_suggestions(OPS)


if __name__ == "__main__":
    main()
