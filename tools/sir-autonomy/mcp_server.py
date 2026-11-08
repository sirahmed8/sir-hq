import sys
import os
import json
import subprocess
import time
import urllib.request
import urllib.error

# Ensure directory is on sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
import computer_engine

BRIDGE_URL = "http://127.0.0.1:18991"
VENV_PYTHON = os.path.join(BASE_DIR, ".venv", "Scripts", "python.exe")


def is_bridge_running():
    try:
        with urllib.request.urlopen(f"{BRIDGE_URL}/health", timeout=1.0) as resp:
            data = json.loads(resp.read().decode())
            return data.get("status") == "ok"
    except Exception:
        return False


def ensure_bridge_running():
    if is_bridge_running():
        return True

    # Spawn bridge_server.py in background
    py_exec = VENV_PYTHON if os.path.exists(VENV_PYTHON) else sys.executable
    bridge_script = os.path.join(BASE_DIR, "bridge_server.py")
    flags = (subprocess.CREATE_NO_WINDOW | 0x00000008) if os.name == "nt" else 0
    subprocess.Popen(
        [py_exec, bridge_script],
        cwd=BASE_DIR,
        creationflags=flags,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        close_fds=True,
    )
    # Wait up to 3 seconds for it to bind
    for _ in range(30):
        time.sleep(0.1)
        if is_bridge_running():
            return True
    return False


def call_bridge_browser(cmd, params, timeout=15.0):
    ensure_bridge_running()
    payload = json.dumps({"command": cmd, "params": params, "timeout": timeout}).encode(
        "utf-8"
    )
    req = urllib.request.Request(
        f"{BRIDGE_URL}/browser",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout + 2.0) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        try:
            return json.loads(err_body)
        except Exception:
            return {"success": False, "error": f"HTTP {e.code}: {err_body}"}
    except Exception as e:
        return {"success": False, "error": str(e)}


TOOLS = [
    # Browser tools
    {
        "name": "sir_browser_tabs",
        "description": "List open Chrome tabs.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "sir_browser_open",
        "description": "Open URL in Chrome.",
        "inputSchema": {
            "type": "object",
            "properties": {"url": {"type": "string"}},
            "required": ["url"],
        },
    },
    {
        "name": "sir_browser_navigate",
        "description": "Navigate Chrome tab to URL.",
        "inputSchema": {
            "type": "object",
            "properties": {"url": {"type": "string"}, "tabId": {"type": "integer"}},
            "required": ["url"],
        },
    },
    {
        "name": "sir_browser_snapshot",
        "description": "Get accessibility DOM tree with refs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "tabId": {"type": "integer"},
                "maxChars": {"type": "integer"},
            },
        },
    },
    {
        "name": "sir_browser_click",
        "description": "Click element by ref or CSS selector.",
        "inputSchema": {
            "type": "object",
            "properties": {"target": {"type": "string"}, "tabId": {"type": "integer"}},
            "required": ["target"],
        },
    },
    {
        "name": "sir_browser_fill",
        "description": "Fill input element with text.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target": {"type": "string"},
                "value": {"type": "string"},
                "tabId": {"type": "integer"},
            },
            "required": ["target", "value"],
        },
    },
    {
        "name": "sir_browser_scroll",
        "description": "Scroll active page or element.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target": {"type": "string"},
                "dx": {"type": "integer"},
                "dy": {"type": "integer"},
                "tabId": {"type": "integer"},
            },
        },
    },
    {
        "name": "sir_browser_eval",
        "description": "Evaluate JavaScript in tab context.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "expression": {"type": "string"},
                "tabId": {"type": "integer"},
            },
            "required": ["expression"],
        },
    },
    {
        "name": "sir_browser_screenshot",
        "description": "Capture visible tab screenshot.",
        "inputSchema": {"type": "object", "properties": {"tabId": {"type": "integer"}}},
    },
    {
        "name": "sir_browser_close",
        "description": "Close a Chrome tab.",
        "inputSchema": {
            "type": "object",
            "properties": {"tabId": {"type": "integer"}},
            "required": ["tabId"],
        },
    },
    # Computer Use tools
    {
        "name": "sir_computer_screenshot",
        "description": "Capture primary desktop screenshot.",
        "inputSchema": {
            "type": "object",
            "properties": {"save_path": {"type": "string"}},
        },
    },
    {
        "name": "sir_computer_click",
        "description": "Click mouse at desktop coordinates.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "x": {"type": "integer"},
                "y": {"type": "integer"},
                "button": {"type": "string"},
                "clicks": {"type": "integer"},
            },
        },
    },
    {
        "name": "sir_computer_move",
        "description": "Move mouse cursor to coordinates.",
        "inputSchema": {
            "type": "object",
            "properties": {"x": {"type": "integer"}, "y": {"type": "integer"}},
            "required": ["x", "y"],
        },
    },
    {
        "name": "sir_computer_drag",
        "description": "Drag mouse from (x1, y1) to (x2, y2).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "x1": {"type": "integer"},
                "y1": {"type": "integer"},
                "x2": {"type": "integer"},
                "y2": {"type": "integer"},
            },
            "required": ["x1", "y1", "x2", "y2"],
        },
    },
    {
        "name": "sir_computer_scroll",
        "description": "Scroll desktop mouse wheel.",
        "inputSchema": {
            "type": "object",
            "properties": {"dy": {"type": "integer"}, "dx": {"type": "integer"}},
        },
    },
    {
        "name": "sir_computer_type",
        "description": "Type text into active desktop window.",
        "inputSchema": {
            "type": "object",
            "properties": {"text": {"type": "string"}},
            "required": ["text"],
        },
    },
    {
        "name": "sir_computer_key",
        "description": "Press special keyboard key.",
        "inputSchema": {
            "type": "object",
            "properties": {"key": {"type": "string"}},
            "required": ["key"],
        },
    },
    {
        "name": "sir_computer_hotkey",
        "description": "Press keyboard shortcut keys.",
        "inputSchema": {
            "type": "object",
            "properties": {"keys": {"type": "array", "items": {"type": "string"}}},
            "required": ["keys"],
        },
    },
    {
        "name": "sir_computer_windows",
        "description": "List open desktop application windows.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "sir_computer_focus_window",
        "description": "Bring application window to foreground.",
        "inputSchema": {
            "type": "object",
            "properties": {"title_or_hwnd": {"type": "string"}},
            "required": ["title_or_hwnd"],
        },
    },
    {
        "name": "sir_computer_open_app",
        "description": "Launch desktop application or command.",
        "inputSchema": {
            "type": "object",
            "properties": {"target": {"type": "string"}},
            "required": ["target"],
        },
    },
    {
        "name": "sir_computer_batch",
        "description": "Execute batch of computer actions.",
        "inputSchema": {
            "type": "object",
            "properties": {"actions": {"type": "array", "items": {"type": "object"}}},
            "required": ["actions"],
        },
    },
]


def handle_call(name, args):
    if name.startswith("sir_browser_"):
        cmd_name = name.replace("sir_browser_", "")
        if cmd_name == "tabs":
            cmd_name = "tabs_list"
        elif cmd_name == "open":
            cmd_name = "tab_new"
        elif cmd_name == "close":
            cmd_name = "tab_close"
        return call_bridge_browser(cmd_name, args)

    elif name.startswith("sir_computer_"):
        action = name.replace("sir_computer_", "")
        if action == "screenshot":
            return computer_engine.take_screenshot(args.get("save_path"))
        elif action == "click":
            return computer_engine.click_mouse(**args)
        elif action == "move":
            return computer_engine.move_mouse(**args)
        elif action == "drag":
            return computer_engine.drag_mouse(**args)
        elif action == "scroll":
            return computer_engine.scroll_mouse(**args)
        elif action == "type":
            return computer_engine.type_text(args.get("text", ""))
        elif action == "key":
            return computer_engine.press_key(args.get("key", ""))
        elif action == "hotkey":
            return computer_engine.hotkey(args.get("keys", []))
        elif action == "windows":
            return computer_engine.list_windows()
        elif action == "focus_window":
            return computer_engine.focus_window(args.get("title_or_hwnd"))
        elif action == "open_app":
            return computer_engine.open_app(args.get("target"))
        elif action == "batch":
            return computer_engine.batch(args.get("actions", []))
        else:
            return {"error": f"Unknown computer action: {action}"}

    return {"error": f"Unknown tool: {name}"}


def main():
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            line = line.strip()
            if not line:
                continue

            msg = json.loads(line)
            msg_id = msg.get("id")
            method = msg.get("method")
            params = msg.get("params", {})

            if method == "initialize":
                res = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {"tools": {}},
                        "serverInfo": {"name": "sir-autonomy", "version": "1.0.0"},
                    },
                }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()

            elif method == "notifications/initialized":
                continue

            elif method == "tools/list":
                res = {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS}}
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()

            elif method == "tools/call":
                t_name = params.get("name")
                t_args = params.get("arguments", {})
                result_data = handle_call(t_name, t_args)

                # Return as MCP tool response
                content_text = json.dumps(result_data, indent=2, ensure_ascii=False)
                res = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {"content": [{"type": "text", "text": content_text}]},
                }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()

            elif method == "ping":
                res = {"jsonrpc": "2.0", "id": msg_id, "result": {}}
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()

            else:
                res = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "error": {"code": -32601, "message": f"Method not found: {method}"},
                }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()

        except Exception as e:
            err_res = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32603, "message": str(e)},
            }
            sys.stdout.write(json.dumps(err_res) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
