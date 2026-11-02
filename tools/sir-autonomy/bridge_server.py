import asyncio
import json
import uuid
import os
import sys
from aiohttp import web

# Ensure local imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import computer_engine

HOST = "127.0.0.1"
PORT = 18991

connected_extensions = set()
pending_requests = {}

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    connected_extensions.add(ws)
    print(f"[Bridge] Extension connected from {request.remote}")

    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                try:
                    data = json.loads(msg.data)
                except Exception:
                    continue

                req_id = data.get("id")
                if req_id and req_id in pending_requests:
                    fut = pending_requests[req_id]
                    if not fut.done():
                        fut.set_result(data)
                elif data.get("type") == "register":
                    print(f"[Bridge] Registered client: {data.get('client')} v{data.get('version')}")
            elif msg.type == web.WSMsgType.ERROR:
                print(f"[Bridge] WebSocket connection error: {ws.exception()}")
    finally:
        connected_extensions.discard(ws)
        print("[Bridge] Extension disconnected")

    return ws

async def health_handler(request):
    return web.json_response({
        "status": "ok",
        "service": "sir-autonomy-bridge",
        "port": PORT,
        "extension_connected": len(connected_extensions) > 0,
        "connected_clients": len(connected_extensions)
    })

async def browser_handler(request):
    try:
        body = await request.json()
    except Exception as e:
        return web.json_response({"success": False, "error": f"Invalid JSON: {e}"}, status=400)

    if not connected_extensions:
        return web.json_response({
            "success": False,
            "error": "No Chrome extension connected. Please load the SIR Autonomy extension in Chrome."
        }, status=503)

    cmd = body.get("command")
    params = body.get("params", {})
    timeout = body.get("timeout", 15.0)

    req_id = str(uuid.uuid4())
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    pending_requests[req_id] = fut

    # Send command to first active extension
    target_ws = next(iter(connected_extensions))
    payload = json.dumps({"id": req_id, "command": cmd, "params": params})

    try:
        await target_ws.send_str(payload)
        resp = await asyncio.wait_for(fut, timeout=timeout)
        return web.json_response(resp)
    except asyncio.TimeoutError:
        return web.json_response({
            "success": False,
            "error": f"Timed out waiting for response from extension ({timeout}s)"
        }, status=504)
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)
    finally:
        pending_requests.pop(req_id, None)

async def computer_handler(request):
    try:
        body = await request.json()
    except Exception as e:
        return web.json_response({"success": False, "error": f"Invalid JSON: {e}"}, status=400)

    action = body.get("action")
    params = body.get("params", {})

    try:
        if action == "screenshot":
            res = computer_engine.take_screenshot(params.get("save_path"))
        elif action == "click":
            res = computer_engine.click_mouse(**params)
        elif action == "move":
            res = computer_engine.move_mouse(**params)
        elif action == "drag":
            res = computer_engine.drag_mouse(**params)
        elif action == "scroll":
            res = computer_engine.scroll_mouse(**params)
        elif action == "type":
            res = computer_engine.type_text(params.get("text", ""))
        elif action == "press":
            res = computer_engine.press_key(params.get("key", ""))
        elif action == "hotkey":
            res = computer_engine.hotkey(params.get("keys", []))
        elif action == "windows":
            res = computer_engine.list_windows()
        elif action == "focus_window":
            res = computer_engine.focus_window(params.get("title_or_hwnd"))
        elif action == "open_app":
            res = computer_engine.open_app(params.get("target"))
        elif action == "batch":
            res = computer_engine.batch(params.get("actions", []))
        else:
            return web.json_response({"success": False, "error": f"Unknown action: {action}"}, status=400)

        return web.json_response({"success": True, "result": res})
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)

def create_app():
    app = web.Application()
    app.router.add_get("/ws", websocket_handler)
    app.router.add_get("/health", health_handler)
    app.router.add_post("/browser", browser_handler)
    app.router.add_post("/computer", computer_handler)
    return app

if __name__ == "__main__":
    app = create_app()
    print(f"[Bridge] Starting SIR Autonomy Bridge on http://{HOST}:{PORT}")
    web.run_app(app, host=HOST, port=PORT, access_log=None)
