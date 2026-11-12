"""Import this first in every script that runs under pythonw: every child process (git, gh, python, bash) is started
without a console window, so no black CMD windows flash on the owner's screen (Ahmed, 2026-11-12)."""
import os
import subprocess

_CREATE_NO_WINDOW = 0x08000000
_DETACHED_PROCESS = 0x00000008
_CREATE_NEW_CONSOLE = 0x00000010

if os.name == "nt" and not getattr(subprocess, "_sir_nowindow", False):
    _orig_init = subprocess.Popen.__init__

    def _init(self, *args, **kwargs):
        flags = kwargs.get("creationflags", 0) or 0
        if not flags & (_DETACHED_PROCESS | _CREATE_NEW_CONSOLE):
            kwargs["creationflags"] = flags | _CREATE_NO_WINDOW
        _orig_init(self, *args, **kwargs)

    subprocess.Popen.__init__ = _init
    subprocess._sir_nowindow = True
