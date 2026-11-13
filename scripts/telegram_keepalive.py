"""Keep the SIR Telegram manager listener alive (one instance).

Runs hidden every minute from the SIR_Telegram_KeepAlive scheduled task.
Starts node scripts/deliver/telegram-inbox.mjs with the bot token and chat id
taken from the user environment, detached, and writes ops/telegram-listener.pid.
If a live listener already answers, it does nothing.
"""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path("D:/Projects/_SIR")
OPS = ROOT / "ops"
PID = OPS / "telegram-listener.pid"
SCRIPT = ROOT / "scripts" / "deliver" / "telegram-inbox.mjs"
NODE = r"C:\Program Files\nodejs\node.exe"
NO_WINDOW = 0x08000000
DETACHED = 0x00000008


def user_env(name: str) -> str:
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as key:
            value, _ = winreg.QueryValueEx(key, name)
            return (value or "").strip()
    except Exception:
        return (os.environ.get(name) or "").strip()


def alive(pid: int) -> bool:
    try:
        import ctypes
        PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
        handle = ctypes.windll.kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
        if not handle:
            return False
        code = ctypes.c_ulong()
        ok = ctypes.windll.kernel32.GetExitCodeProcess(handle, ctypes.byref(code))
        ctypes.windll.kernel32.CloseHandle(handle)
        return bool(ok) and code.value == 259  # STILL_ACTIVE
    except Exception:
        return False


def main() -> int:
    token = user_env("SIR_TELEGRAM_BOT_TOKEN")
    chat = user_env("SIR_TELEGRAM_CHAT_ID")
    if not token or not chat:
        print("keepalive: token or chat id missing in the user environment", file=sys.stderr)
        return 1
    try:
        pid = int(PID.read_text().strip())
        if alive(pid):
            return 0
    except Exception:
        pass
    env = dict(os.environ)
    env["SIR_TELEGRAM_BOT_TOKEN"] = token
    env["SIR_TELEGRAM_CHAT_ID"] = chat
    env["PATH"] = r"C:\Windows\System32;C:\Program Files\nodejs;C:\Windows"
    with open(OPS / "telegram-listener.log", "ab") as log:
        p = subprocess.Popen(
            [NODE, str(SCRIPT)],
            cwd=str(ROOT),
            env=env,
            creationflags=NO_WINDOW | DETACHED,
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=subprocess.STDOUT,
        )
    PID.write_text(str(p.pid), encoding="utf-8")
    print("keepalive: started listener pid", p.pid)
    return 0


if __name__ == "__main__":
    sys.exit(main())
