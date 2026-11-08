r"""Replaces the old D:\Projects\Backups and D:\Projects\Android paths with their new places inside D:\Projects in the _SIR docs and scripts."""

import io
import os

OLD = [
    "D:" + chr(92) + "Backups",
    "D:" + chr(92) + "Android",
    "D:/Projects/Backups",
    "D:/Projects/Android",
]
NEW = [
    "D:" + chr(92) + "Projects" + chr(92) + "Backups",
    "D:" + chr(92) + "Projects" + chr(92) + "Android",
    "D:/Projects/Backups",
    "D:/Projects/Android",
]
n = 0
for root, dirs, files in os.walk("D:/Projects/_SIR"):
    dirs[:] = [
        d for d in dirs if d not in (".claude", "archive", ".git", "node_modules")
    ]
    for f in files:
        if f.endswith((".md", ".ps1", ".py", ".json", ".txt")):
            p = os.path.join(root, f)
            try:
                s = io.open(p, encoding="utf-8").read()
            except Exception:
                continue
            t = s
            for a, b in zip(OLD, NEW):
                t = t.replace(a, b)
            if t != s:
                io.open(p, "w", encoding="utf-8", newline="\n").write(t)
                n += 1
print("files updated:", n)
