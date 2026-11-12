"""Shared Playwright helpers for the tests.

The Windows Playwright build needs a Node.js executable and a Chromium build. Both are optional:
the helpers answer what is available so a test can skip instead of failing on a machine that has
neither.
"""
import os
import shutil


def node_path():
    """Path of a Node.js executable on this machine, or an empty string."""
    found = shutil.which("node")
    if found:
        return found
    for candidate in (r"C:\Program Files\nodejs\node.exe", r"C:\Program Files (x86)\nodejs\node.exe"):
        if os.path.exists(candidate):
            return candidate
    return ""


def chromium_ready():
    """True when Playwright and a Chromium build are both available."""
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        return False
    try:
        with sync_playwright() as p:
            path = p.chromium.executable_path
            return bool(path) and os.path.exists(path)
    except Exception:
        return False
