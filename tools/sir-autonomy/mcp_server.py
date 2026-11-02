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
    subprocess.Popen(
        [py_exec, bridge_script],
        cwd=BASE_DIR,
        creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    # Wait up to 3 seconds for it to bind
    for _ in range(30):
        time.sleep(0.1)
        if is_bridge_running():
            return True
    return False

def call_bridge_browser(cmd, params, timeout=15.0):
    ensure_bridge_running()
    payload = json.dumps({"command": cmd, "params": params, "timeout": timeout}).encode("utf-8")
    req = urllib.request.Request(
        f"{BRIDGE_URL}/browser",
        data=payload,
        headers={"Content-Type": "application/json"}
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
        "description": "List all open Chrome tabs with their titles, URLs, and active status",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "sir_browser_open",
        "description": "Open a URL in a new tab or navigate the current tab in Ahmed's Chrome",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "URL to open"}
            },
            "required": ["url"]
        }
    },
    {
        "name": "sir_browser_navigate",
        "description": "Navigate the active or specified tab to a new URL",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Destination URL"},
                "tabId": {"type": "integer", "description": "Optional tab ID"}
            },
            "required": ["url"]
        }
    },
    {
        "name": "sir_browser_snapshot",
        "description": "Get structured accessibility DOM tree of the active tab with numbered ref tags ([ref_1], [ref_2])",
        "inputSchema": {
            "type": "object",
            "properties": {
                "tabId": {"type": "integer", "description": "Optional tab ID"},
                "maxChars": {"type": "integer", "description": "Max text characters to return", "default": 40000}
            }
        }
    },
    {
        "name": "sir_browser_click",
        "description": "Click an interactive element in the tab by ref ID (e.g. 'ref_1') or CSS selector",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target": {"type": "string", "description": "Element ref ID (e.g. 'ref_1') or CSS selector"},
                "tabId": {"type": "integer", "description": "Optional tab ID"}
            },
            "required": ["target"]
        }
    },
    {
        "name": "sir_browser_fill",
        "description": "Fill an input field or textarea with text by ref ID or CSS selector",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target": {"type": "string", "description": "Input ref ID (e.g. 'ref_2') or CSS selector"},
                "value": {"type": "string", "description": "Text value to fill"},
                "tabId": {"type": "integer", "description": "Optional tab ID"}
            },
            "required": ["target", "value"]
        }
    },
    {
        "name": "sir_browser_scroll",
        "description": "Scroll the active page or element",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target": {"type": "string", "description": "Optional element ref/selector, or 'window'"},
                "dx": {"type": "integer", "description": "Horizontal scroll delta", "default": 0},
                "dy": {"type": "integer", "description": "Vertical scroll delta", "default": 300},
                "tabId": {"type": "integer", "description": "Optional tab ID"}
            }
        }
    },
    {
        "name": "sir_browser_eval",
        "description": "Evaluate arbitrary JavaScript inside the tab context and return the result",
        "inputSchema": {
            "type": "object",
            "properties": {
                "expression": {"type": "string", "description": "JavaScript expression to evaluate"},
                "tabId": {"type": "integer", "description": "Optional tab ID"}
            },
            "required": ["expression"]
        }
    },
    {
        "name": "sir_browser_screenshot",
        "description": "Capture visible tab screenshot as base64 PNG",
        "inputSchema": {
            "type": "object",
            "properties": {
                "tabId": {"type": "integer", "description": "Optional tab ID"}
            }
        }
    },
    {
        "name": "sir_browser_close",
        "description": "Close a Chrome tab",
        "inputSchema": {
            "type": "object",
            "properties": {
                "tabId": {"type": "integer", "description": "Tab ID to close"}
            },
            "required": ["tabId"]
        }
    },
    # Computer Use tools
    {
        "name": "sir_computer_screenshot",
        "description": "Capture the primary Windows desktop screen (returns image data or saves to path)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "save_path": {"type": "string", "description": "Optional path to save PNG file"}
            }
        }
    },
    {
        "name": "sir_computer_click",
        "description": "Click mouse at desktop coordinates (x, y) with left, right, or double click",
        "inputSchema": {
            "type": "object",
            "properties": {
                "x": {"type": "integer", "description": "Screen X coordinate"},
                "y": {"type": "integer", "description": "Screen Y coordinate"},
                "button": {"type": "string", "enum": ["left", "right", "middle"], "default": "left"},
                "clicks": {"type": "integer", "default": 1}
            }
        }
    },
    {
        "name": "sir_computer_move",
        "description": "Move the mouse cursor to (x, y)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "x": {"type": "integer", "description": "Screen X coordinate"},
                "y": {"type": "integer", "description": "Screen Y coordinate"}
            },
            "required": ["x", "y"]
        }
    },
    {
        "name": "sir_computer_drag",
        "description": "Click and drag mouse from (x1, y1) to (x2, y2)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "x1": {"type": "integer", "description": "Start X coordinate"},
                "y1": {"type": "integer", "description": "Start Y coordinate"},
                "x2": {"type": "integer", "description": "End X coordinate"},
                "y2": {"type": "integer", "description": "End Y coordinate"},
                "duration": {"type": "number", "default": 0.2}
            },
            "required": ["x1", "y1", "x2", "y2"]
        }
    },
    {
        "name": "sir_computer_scroll",
        "description": "Scroll mouse wheel vertically or horizontally",
        "inputSchema": {
            "type": "object",
            "properties": {
                "dx": {"type": "integer", "default": 0},
                "dy": {"type": "integer", "default": 0},
                "x": {"type": "integer", "description": "Optional X coordinate to scroll at"},
                "y": {"type": "integer", "description": "Optional Y coordinate to scroll at"}
            }
        }
    },
    {
        "name": "sir_computer_type",
        "description": "Type text into the currently active desktop window (supports Unicode & Arabic)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "Text to type"}
            },
            "required": ["text"]
        }
    },
    {
        "name": "sir_computer_key",
        "description": "Press a special keyboard key (enter, esc, tab, win, backspace, etc.)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "key": {"type": "string", "description": "Key name (e.g. enter, esc, win, tab, f5)"}
            },
            "required": ["key"]
        }
    },
    {
        "name": "sir_computer_hotkey",
        "description": "Press a keyboard shortcut combination (e.g. ['ctrl', 'c'] or ['win', 'r'])",
        "inputSchema": {
            "type": "object",
            "properties": {
                "keys": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of keys to press together"
                }
            },
            "required": ["keys"]
        }
    },
    {
        "name": "sir_computer_windows",
        "description": "List all open desktop application windows with their titles, bounds, and handles",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "sir_computer_focus_window",
        "description": "Bring a desktop application window to the foreground by title or HWND",
        "inputSchema": {
            "type": "object",
            "properties": {
                "title_or_hwnd": {"type": "string", "description": "Window title substring or numeric HWND"}
            },
            "required": ["title_or_hwnd"]
        }
    },
    {
        "name": "sir_computer_open_app",
        "description": "Launch any Windows desktop application or file",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target": {"type": "string", "description": "Application command, executable, or file path"}
            },
            "required": ["target"]
        }
    },
    {
        "name": "sir_computer_batch",
        "description": "Execute a batch sequence of computer actions atomically with delays",
        "inputSchema": {
            "type": "object",
            "properties": {
                "actions": {
                    "type": "array",
                    "items": {"type": "object"},
                    "description": "List of action objects: [{action: 'click', params: {x: 100, y: 100}}, {action: 'type', params: {text: 'hi'}}]"
                }
            },
            "required": ["actions"]
        }
    }
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
                        "capabilities": {
                            "tools": {}
                        },
                        "serverInfo": {
                            "name": "sir-autonomy",
                            "version": "1.0.0"
                        }
                    }
                }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()

            elif method == "notifications/initialized":
                continue

            elif method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "tools": TOOLS
                    }
                }
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
                    "result": {
                        "content": [
                            {
                                "type": "text",
                                "text": content_text
                            }
                        ]
                    }
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
                    "error": {
                        "code": -32601,
                        "message": f"Method not found: {method}"
                    }
                }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()

        except Exception as e:
            err_res = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32603,
                    "message": str(e)
                }
            }
            sys.stdout.write(json.dumps(err_res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
