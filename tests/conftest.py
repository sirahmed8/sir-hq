"""Test setup shared by every test module.

The Windows Playwright build needs a Node.js executable. The path is set here, before any test
module imports Playwright, so every browser test finds it the same way.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from playwright_support import node_path  # noqa: E402

_NODE = node_path()
if _NODE:
    os.environ.setdefault("PLAYWRIGHT_NODEJS_PATH", _NODE)
