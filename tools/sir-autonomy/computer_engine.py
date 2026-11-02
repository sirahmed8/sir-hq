import ctypes
from ctypes import wintypes
import time
import os
import subprocess
import io
import base64
from PIL import ImageGrab

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# Attach to interactive Windows desktop station WinSta0\Default
def attach_to_interactive_desktop():
    try:
        hwinsta = user32.OpenWindowStationW("WinSta0", False, 0x0000037F)
        if hwinsta:
            user32.SetProcessWindowStation(hwinsta)
            hdesk = user32.OpenDesktopW("Default", 0, False, 0x000001FF)
            if hdesk:
                user32.SetThreadDesktop(hdesk)
    except Exception:
        pass

attach_to_interactive_desktop()

# Virtual key mappings
VK_CODES = {
    "enter": 0x0D, "return": 0x0D,
    "tab": 0x09,
    "space": 0x20,
    "backspace": 0x08, "bksp": 0x08,
    "delete": 0x2E, "del": 0x2E,
    "escape": 0x1B, "esc": 0x1B,
    "shift": 0x10, "lshift": 0xA0, "rshift": 0xA1,
    "ctrl": 0x11, "control": 0x11, "lctrl": 0xA2, "rctrl": 0xA3,
    "alt": 0x12, "lalt": 0xA4, "ralt": 0xA5,
    "win": 0x5B, "windows": 0x5B, "cmd": 0x5B,
    "up": 0x26, "down": 0x28, "left": 0x25, "right": 0x27,
    "home": 0x24, "end": 0x23, "pageup": 0x21, "pagedown": 0x22,
    "insert": 0x2D,
    "f1": 0x70, "f2": 0x71, "f3": 0x72, "f4": 0x73, "f5": 0x74,
    "f6": 0x75, "f7": 0x76, "f8": 0x77, "f9": 0x78, "f10": 0x79,
    "f11": 0x7A, "f12": 0x7B
}

MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x000A
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040
MOUSEEVENTF_WHEEL = 0x0800
MOUSEEVENTF_HWHEEL = 0x01000

class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", wintypes.WORD),
        ("wScan", wintypes.WORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.c_size_t)
    ]

class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.c_size_t)
    ]

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = [
        ("uMsg", wintypes.DWORD),
        ("wParamL", wintypes.WORD),
        ("wParamH", wintypes.WORD)
    ]

class INPUT_UNION(ctypes.Union):
    _fields_ = [
        ("mi", MOUSEINPUT),
        ("ki", KEYBDINPUT),
        ("hi", HARDWAREINPUT)
    ]

class INPUT(ctypes.Structure):
    _fields_ = [
        ("type", wintypes.DWORD),
        ("union", INPUT_UNION)
    ]

INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004

def get_screen_size():
    attach_to_interactive_desktop()
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def get_mouse_pos():
    attach_to_interactive_desktop()
    pt = wintypes.POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

def move_mouse(x, y):
    attach_to_interactive_desktop()
    user32.SetCursorPos(int(x), int(y))
    return {"x": int(x), "y": int(y)}

def click_mouse(x=None, y=None, button="left", clicks=1):
    attach_to_interactive_desktop()
    if x is not None and y is not None:
        move_mouse(x, y)
        time.sleep(0.02)
    
    b = button.lower()
    if b == "left":
        down_flag, up_flag = MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
    elif b == "right":
        down_flag, up_flag = MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP
    elif b == "middle":
        down_flag, up_flag = MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP
    else:
        down_flag, up_flag = MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP

    for _ in range(clicks):
        user32.mouse_event(down_flag, 0, 0, 0, 0)
        time.sleep(0.02)
        user32.mouse_event(up_flag, 0, 0, 0, 0)
        if clicks > 1:
            time.sleep(0.05)

    pos = get_mouse_pos()
    return {"action": "click", "button": b, "clicks": clicks, "x": pos[0], "y": pos[1]}

def drag_mouse(x1, y1, x2, y2, duration=0.2):
    attach_to_interactive_desktop()
    move_mouse(x1, y1)
    time.sleep(0.03)
    user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    steps = max(5, int(duration * 60))
    for i in range(1, steps + 1):
        cur_x = x1 + (x2 - x1) * i / steps
        cur_y = y1 + (y2 - y1) * i / steps
        move_mouse(cur_x, cur_y)
        time.sleep(duration / steps)
    user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    return {"action": "drag", "from": [x1, y1], "to": [x2, y2]}

def scroll_mouse(dx=0, dy=0, x=None, y=None):
    attach_to_interactive_desktop()
    if x is not None and y is not None:
        move_mouse(x, y)
    if dy != 0:
        user32.mouse_event(MOUSEEVENTF_WHEEL, 0, 0, int(dy * 120), 0)
    if dx != 0:
        user32.mouse_event(MOUSEEVENTF_HWHEEL, 0, 0, int(dx * 120), 0)
    return {"action": "scroll", "dx": dx, "dy": dy}

def type_text(text):
    attach_to_interactive_desktop()
    for char in text:
        code = ord(char)
        inp_down = INPUT()
        inp_down.type = INPUT_KEYBOARD
        inp_down.union.ki = KEYBDINPUT(0, code, KEYEVENTF_UNICODE, 0, 0)

        inp_up = INPUT()
        inp_up.type = INPUT_KEYBOARD
        inp_up.union.ki = KEYBDINPUT(0, code, KEYEVENTF_UNICODE | KEYEVENTF_KEYUP, 0, 0)

        inputs = (INPUT * 2)(inp_down, inp_up)
        user32.SendInput(2, inputs, ctypes.sizeof(INPUT))
        time.sleep(0.005)
    return {"action": "type_text", "length": len(text)}

def press_key(key):
    attach_to_interactive_desktop()
    k = key.lower().strip()
    vk = VK_CODES.get(k)
    if vk is None and len(k) == 1:
        vk = user32.VkKeyScanW(ord(k)) & 0xFF
    if vk is None:
        raise ValueError(f"Unknown key: {key}")

    user32.keybd_event(vk, 0, 0, 0)
    time.sleep(0.02)
    user32.keybd_event(vk, 0, KEYEVENTF_KEYUP, 0)
    return {"action": "press_key", "key": key}

def hotkey(keys):
    attach_to_interactive_desktop()
    vks = []
    for k in keys:
        kl = k.lower().strip()
        vk = VK_CODES.get(kl)
        if vk is None and len(kl) == 1:
            vk = user32.VkKeyScanW(ord(kl)) & 0xFF
        if vk is None:
            raise ValueError(f"Unknown key in hotkey: {k}")
        vks.append(vk)

    for vk in vks:
        user32.keybd_event(vk, 0, 0, 0)
        time.sleep(0.01)

    time.sleep(0.03)

    for vk in reversed(vks):
        user32.keybd_event(vk, 0, KEYEVENTF_KEYUP, 0)
        time.sleep(0.01)

    return {"action": "hotkey", "keys": keys}

def take_screenshot(save_path=None):
    attach_to_interactive_desktop()
    img = ImageGrab.grab()
    if save_path:
        os.makedirs(os.path.dirname(os.path.abspath(save_path)), exist_ok=True)
        img.save(save_path, "PNG")
        return {"action": "screenshot", "path": save_path, "width": img.width, "height": img.height}
    else:
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        b64 = base64.b64encode(buf.getvalue()).decode("ascii")
        return {"action": "screenshot", "width": img.width, "height": img.height, "data": b64}

def list_windows():
    attach_to_interactive_desktop()
    windows = []
    def enum_cb(hwnd, extra):
        length = user32.GetWindowTextLengthW(hwnd)
        if length > 0:
            buff = ctypes.create_unicode_buffer(length + 1)
            user32.GetWindowTextW(hwnd, buff, length + 1)
            title = buff.value.strip()
            # Filter internal invisible/helper classes
            if title and not title.startswith("Default IME") and not title.startswith("MSCTFIME") and not title.startswith("BroadcastListener"):
                rect = wintypes.RECT()
                user32.GetWindowRect(hwnd, ctypes.byref(rect))
                w = rect.right - rect.left
                h = rect.bottom - rect.top
                windows.append({
                    "hwnd": hwnd,
                    "title": title,
                    "x": rect.left,
                    "y": rect.top,
                    "width": w,
                    "height": h
                })
        return True

    ENUM_WINDOWS_PROC = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
    user32.EnumWindows(ENUM_WINDOWS_PROC(enum_cb), 0)
    return windows

def focus_window(title_or_hwnd):
    attach_to_interactive_desktop()
    target_hwnd = None
    if isinstance(title_or_hwnd, int):
        target_hwnd = title_or_hwnd
    else:
        target_title = str(title_or_hwnd).lower()
        for w in list_windows():
            if target_title in w["title"].lower():
                target_hwnd = w["hwnd"]
                break

    if not target_hwnd:
        raise ValueError(f"Window not found matching: {title_or_hwnd}")

    user32.ShowWindow(target_hwnd, 9)
    user32.SetForegroundWindow(target_hwnd)
    return {"action": "focus_window", "hwnd": target_hwnd}

def open_app(command_or_path):
    subprocess.Popen(command_or_path, shell=True)
    return {"action": "open_app", "target": command_or_path}

def batch(actions):
    results = []
    for act in actions:
        fn = act.get("action")
        params = act.get("params", {})
        if fn == "click":
            res = click_mouse(**params)
        elif fn == "move":
            res = move_mouse(**params)
        elif fn == "drag":
            res = drag_mouse(**params)
        elif fn == "scroll":
            res = scroll_mouse(**params)
        elif fn == "type":
            res = type_text(**params)
        elif fn == "key":
            res = press_key(**params)
        elif fn == "hotkey":
            res = hotkey(**params)
        elif fn == "sleep":
            time.sleep(params.get("seconds", 0.5))
            res = {"action": "sleep", "seconds": params.get("seconds", 0.5)}
        else:
            res = {"action": fn, "error": f"Unknown action: {fn}"}
        results.append(res)
    return results
