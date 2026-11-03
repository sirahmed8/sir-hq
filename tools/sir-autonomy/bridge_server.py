import asyncio
import json
import uuid
import os
import sys
import urllib.request
from aiohttp import web

# Ensure local imports and shared packages work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_SHARED_SP = r"D:\Projects\AHome\apps\local-core\.venv\Lib\site-packages"
if os.path.isdir(_SHARED_SP) and _SHARED_SP not in sys.path:
    sys.path.insert(0, _SHARED_SP)

if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")
import computer_engine

HOST = "127.0.0.1"
PORT = 18991

connected_extensions = set()
pending_requests = {}

@web.middleware
async def cors_middleware(request, handler):
    if request.method == "OPTIONS":
        response = web.Response(status=204)
    else:
        try:
            response = await handler(request)
        except web.HTTPException as ex:
            response = ex
        except Exception as e:
            response = web.json_response({"success": False, "error": str(e)}, status=500)

    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-Requested-With"
    return response

async def websocket_handler(request):
    ws = web.WebSocketResponse(max_msg_size=32 * 1024 * 1024, heartbeat=20.0)
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
    # Quick probe of Ollama
    ollama_ok = False
    try:
        req = urllib.request.Request("http://localhost:11434/api/tags", headers={"User-Agent": "SIR-Autonomy"})
        with urllib.request.urlopen(req, timeout=1.0) as resp:
            ollama_ok = resp.status == 200
    except Exception:
        pass

    return web.json_response({
        "status": "ok",
        "service": "sir-autonomy-bridge",
        "port": PORT,
        "extension_connected": len(connected_extensions) > 0,
        "connected_clients": len(connected_extensions),
        "ollama_available": ollama_ok
    })

async def dispatch_browser_cmd(cmd, params, timeout=15.0):
    if not connected_extensions:
        raise RuntimeError("No Chrome extension connected. Please load the SIR Autonomy extension in Chrome.")

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
        return resp
    finally:
        pending_requests.pop(req_id, None)

async def browser_handler(request):
    try:
        body = await request.json()
    except Exception as e:
        return web.json_response({"success": False, "error": f"Invalid JSON: {e}"}, status=400)

    cmd = body.get("command")
    params = body.get("params", {})
    timeout = body.get("timeout", 15.0)

    try:
        resp = await dispatch_browser_cmd(cmd, params, timeout)
        return web.json_response(resp)
    except asyncio.TimeoutError:
        return web.json_response({
            "success": False,
            "error": f"Timed out waiting for response from extension ({timeout}s)"
        }, status=504)
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)

async def execute_computer_action(action, params):
    if action == "screenshot":
        return computer_engine.take_screenshot(params.get("save_path"))
    elif action == "click":
        return computer_engine.click_mouse(**params)
    elif action == "move":
        return computer_engine.move_mouse(**params)
    elif action == "drag":
        return computer_engine.drag_mouse(**params)
    elif action == "scroll":
        return computer_engine.scroll_mouse(**params)
    elif action == "type":
        return computer_engine.type_text(params.get("text", ""))
    elif action == "press":
        return computer_engine.press_key(params.get("key", ""))
    elif action == "hotkey":
        return computer_engine.hotkey(params.get("keys", []))
    elif action == "windows":
        return computer_engine.list_windows()
    elif action == "focus_window":
        return computer_engine.focus_window(params.get("title_or_hwnd"))
    elif action == "open_app":
        return computer_engine.open_app(params.get("target"))
    elif action == "batch":
        return computer_engine.batch(params.get("actions", []))
    else:
        raise ValueError(f"Unknown action: {action}")

async def computer_handler(request):
    try:
        body = await request.json()
    except Exception as e:
        return web.json_response({"success": False, "error": f"Invalid JSON: {e}"}, status=400)

    action = body.get("action")
    params = body.get("params", {})

    try:
        res = await execute_computer_action(action, params)
        return web.json_response({"success": True, "result": res})
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)

async def ask_handler(request):
    try:
        body = await request.json()
    except Exception as e:
        return web.json_response({"success": False, "error": f"Invalid JSON: {e}"}, status=400)

    prompt = body.get("prompt", "")
    page_context = body.get("page_context", "")
    model = body.get("model", "qwen2.5:1.5b")

    system_prompt = (
        "You are Antigravity, an elite autonomous browser and companion assistant created by Sir Ahmed. "
        "You help the user understand pages, extract data, solve problems, and execute browser actions. "
        "Be concise, actionable, and formatted in clean markdown."
    )

    full_prompt = f"{system_prompt}\n\n"
    if page_context:
        full_prompt += f"--- CURRENT WEBPAGE CONTEXT ---\n{page_context[:8000]}\n-------------------------------\n\n"
    full_prompt += f"User: {prompt}\n\nAntigravity:"

    # Call local Ollama
    loop = asyncio.get_running_loop()
    def query_ollama():
        req_data = json.dumps({
            "model": model,
            "prompt": full_prompt,
            "stream": False
        }).encode("utf-8")
        req = urllib.request.Request(
            "http://localhost:11434/api/generate",
            data=req_data,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=30.0) as resp:
            return json.loads(resp.read().decode("utf-8"))

    try:
        res = await loop.run_in_executor(None, query_ollama)
        answer = res.get("response", "").strip()
        return web.json_response({"success": True, "answer": answer, "model": model})
    except Exception as err:
        return web.json_response({
            "success": False,
            "error": f"Ollama error: {err}",
            "fallback": "Could not connect to local model. Please ensure Ollama is running."
        }, status=502)

async def synthesize_handler(request):
    try:
        data = await request.json()
        text = (data.get("text") or "").strip()
        voice = data.get("voice") or "ar-EG-SalmaNeural"
        if not text:
            return web.json_response({"error": "Text is required"}, status=400)

        import edge_tts
        comm = edge_tts.Communicate(text, voice)
        chunks = []
        async for chunk in comm.stream():
            if chunk.get("type") == "audio" and "data" in chunk:
                chunks.append(chunk["data"])

        audio_bytes = b"".join(chunks)
        return web.Response(
            body=audio_bytes,
            content_type="audio/mpeg",
            headers={
                "Cache-Control": "public, max-age=86400",
                "Access-Control-Allow-Origin": "*"
            }
        )
    except Exception as err:
        return web.json_response({"error": str(err)}, status=500)

def create_app():
    app = web.Application(middlewares=[cors_middleware])
    app.router.add_get("/ws", websocket_handler)
    app.router.add_get("/health", health_handler)
    app.router.add_post("/browser", browser_handler)
    app.router.add_post("/computer", computer_handler)
    app.router.add_post("/ask", ask_handler)
    app.router.add_post("/synthesize", synthesize_handler)
    return app

if __name__ == "__main__":
    try:
        app = create_app()
        web.run_app(app, host=HOST, port=PORT, access_log=None, print=lambda *args: None)
    except Exception as e:
        with open(os.path.join(os.path.dirname(__file__), "bridge_crash.log"), "w", encoding="utf-8") as f:
            import traceback
            traceback.print_exc(file=f)
