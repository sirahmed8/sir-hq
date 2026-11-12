"""The Control Room page template lives in plans/dashboard_parts/*.html, one concern per file.

This module joins the parts in order and keeps plans/dashboard_template.html (the assembled
mirror, kept so the whole page can be read and diffed as one file) identical to the parts.
The parts are the source of truth: edit them, never the mirror.
"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS_DIR = os.path.join(HERE, "dashboard_parts")
MIRROR = os.path.join(HERE, "dashboard_template.html")
PARTS = (
    "head.html",
    "style.html",
    "body.html",
    "script_data.html",
    "script_ui.html",
    "script_boot.html",
)
PLACEHOLDER = "/*__DATA__*/{}"


def assemble():
    """Return the whole page template, parts joined in order."""
    chunks = []
    for name in PARTS:
        with io.open(os.path.join(PARTS_DIR, name), "r", encoding="utf-8", newline="") as f:
            chunks.append(f.read())
    return "".join(chunks)


def mirror_text():
    """Return the mirror file content (empty string when it does not exist yet)."""
    if not os.path.exists(MIRROR):
        return ""
    with io.open(MIRROR, "r", encoding="utf-8", newline="") as f:
        return f.read()


def write_mirror():
    """Write the assembled mirror when it differs from the parts. Returns True when it changed."""
    text = assemble()
    if mirror_text() == text:
        return False
    tmp = MIRROR + ".tmp"
    with io.open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp, MIRROR)
    return True


if __name__ == "__main__":
    changed = write_mirror()
    print("mirror", MIRROR, "updated" if changed else "already current")
