import sys
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
import mcp_server
import computer_engine

def print_help():
    print("""
SIR Autonomy CLI (Browser & Computer Control)

Usage:
  sir_ctl.py browser tabs
  sir_ctl.py browser open <url>
  sir_ctl.py browser navigate <url> [tab_id]
  sir_ctl.py browser snapshot [tab_id]
  sir_ctl.py browser click <target> [tab_id]
  sir_ctl.py browser fill <target> <value> [tab_id]
  sir_ctl.py browser scroll [target] [dx] [dy]
  sir_ctl.py browser eval <js_code>
  sir_ctl.py browser screenshot [tab_id]
  sir_ctl.py browser close <tab_id>

  sir_ctl.py computer screenshot [save_path]
  sir_ctl.py computer click <x> <y> [button] [clicks]
  sir_ctl.py computer move <x> <y>
  sir_ctl.py computer drag <x1> <y1> <x2> <y2>
  sir_ctl.py computer scroll <dy> [dx]
  sir_ctl.py computer type <text>
  sir_ctl.py computer key <key>
  sir_ctl.py computer hotkey <key1> <key2> ...
  sir_ctl.py computer windows
  sir_ctl.py computer focus <title_or_hwnd>
  sir_ctl.py computer open <target>
""")

def main():
    if len(sys.argv) < 3:
        print_help()
        sys.exit(1)

    domain = sys.argv[1].lower()
    cmd = sys.argv[2].lower()
    args = sys.argv[3:]

    if domain == "browser":
        if cmd == "tabs":
            res = mcp_server.call_bridge_browser("tabs_list", {})
        elif cmd in ("open", "tab_new"):
            res = mcp_server.call_bridge_browser("tab_new", {"url": args[0] if args else "about:blank"})
        elif cmd == "navigate":
            tab_id = int(args[1]) if len(args) > 1 else None
            res = mcp_server.call_bridge_browser("navigate", {"url": args[0], "tabId": tab_id})
        elif cmd == "snapshot":
            tab_id = int(args[0]) if args else None
            res = mcp_server.call_bridge_browser("snapshot", {"tabId": tab_id})
        elif cmd == "click":
            tab_id = int(args[1]) if len(args) > 1 else None
            res = mcp_server.call_bridge_browser("click", {"target": args[0], "tabId": tab_id})
        elif cmd == "fill":
            tab_id = int(args[2]) if len(args) > 2 else None
            res = mcp_server.call_bridge_browser("fill", {"target": args[0], "value": args[1], "tabId": tab_id})
        elif cmd == "scroll":
            target = args[0] if len(args) > 0 else "window"
            dx = int(args[1]) if len(args) > 1 else 0
            dy = int(args[2]) if len(args) > 2 else 300
            res = mcp_server.call_bridge_browser("scroll", {"target": target, "dx": dx, "dy": dy})
        elif cmd == "eval":
            res = mcp_server.call_bridge_browser("eval", {"expression": args[0]})
        elif cmd == "screenshot":
            tab_id = int(args[0]) if args else None
            res = mcp_server.call_bridge_browser("screenshot", {"tabId": tab_id})
        elif cmd == "close":
            res = mcp_server.call_bridge_browser("tab_close", {"tabId": int(args[0])})
        else:
            print(f"Unknown browser command: {cmd}")
            sys.exit(1)

        print(json.dumps(res, indent=2, ensure_ascii=False))

    elif domain == "computer":
        if cmd == "screenshot":
            path = args[0] if args else None
            res = computer_engine.take_screenshot(path)
        elif cmd == "click":
            x = int(args[0])
            y = int(args[1])
            btn = args[2] if len(args) > 2 else "left"
            clicks = int(args[3]) if len(args) > 3 else 1
            res = computer_engine.click_mouse(x, y, btn, clicks)
        elif cmd == "move":
            res = computer_engine.move_mouse(int(args[0]), int(args[1]))
        elif cmd == "drag":
            res = computer_engine.drag_mouse(int(args[0]), int(args[1]), int(args[2]), int(args[3]))
        elif cmd == "scroll":
            dy = int(args[0])
            dx = int(args[1]) if len(args) > 1 else 0
            res = computer_engine.scroll_mouse(dx, dy)
        elif cmd == "type":
            res = computer_engine.type_text(" ".join(args))
        elif cmd == "key":
            res = computer_engine.press_key(args[0])
        elif cmd == "hotkey":
            res = computer_engine.hotkey(args)
        elif cmd == "windows":
            res = computer_engine.list_windows()
        elif cmd == "focus":
            res = computer_engine.focus_window(" ".join(args))
        elif cmd == "open":
            res = computer_engine.open_app(" ".join(args))
        else:
            print(f"Unknown computer command: {cmd}")
            sys.exit(1)

        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print_help()

if __name__ == "__main__":
    main()
