#!/usr/bin/env python3
"""SIR Control Room dashboard server on port 8899.
Serves only ops/public, binds loopback, and enforces Host allow-list.
"""
from __future__ import annotations

import json
import logging
import os
import sys
import time
import datetime
import threading
import subprocess
import socket
import msvcrt
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, unquote

HERE = os.path.dirname(os.path.abspath(__file__))
OPS_DIR = os.path.normpath(os.path.join(HERE, "..", "ops"))
PUBLIC_DIR = os.path.join(OPS_DIR, "public")
LOG_FILE = os.path.join(OPS_DIR, "control-room-server.log")
HEALTH_FILE = os.path.join(OPS_DIR, "control-room-health.json")
LOCK_FILE = os.path.join(OPS_DIR, "control-room.lock")
REFRESH_SCRIPT = os.path.join(HERE, "refresh-control-room.py")
PORT = 8899
HOST = "127.0.0.1"
ALLOWED_HOSTS = {"127.0.0.1", "localhost", "ahmed.tail9e9aa7.ts.net", "[::1]", "::1"}
INSTANCE_LOCK_FH = None

_state_lock = threading.Lock()
_state = {
    "last_refresh_ok": None,
    "last_refresh_time": None,
    "last_error": None,
}


class FileLoggerStream:
    def __init__(self, logger: logging.Logger, level: int):
        self.logger = logger
        self.level = level
        self._buf = ""

    def write(self, message: str) -> None:
        if not message:
            return
        self._buf += message
        while "\n" in self._buf:
            line, self._buf = self._buf.split("\n", 1)
            line = line.strip()
            if line:
                self.logger.log(self.level, line)

    def flush(self) -> None:
        if self._buf.strip():
            self.logger.log(self.level, self._buf.strip())
            self._buf = ""


def setup_logging() -> logging.Logger:
    logger = logging.getLogger("ControlRoomServer")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        os.makedirs(OPS_DIR, exist_ok=True)
        fh = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    sys.stdout = FileLoggerStream(logger, logging.INFO)
    sys.stderr = FileLoggerStream(logger, logging.ERROR)
    return logger


LOGGER = setup_logging()
START_TIME = datetime.datetime.now(datetime.timezone.utc).isoformat()


def _now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def update_health(status: str = "ok") -> dict:
    with _state_lock:
        data = {
            "service": "SIR Control Room",
            "task_name": "SIR_ControlRoom_Server",
            "port": PORT,
            "host": HOST,
            "pid": os.getpid(),
            "status": status,
            "mode": "detached_daemon",
            "started_at": START_TIME,
            "last_heartbeat": _now_iso(),
            "last_refresh_ok": _state.get("last_refresh_ok"),
            "last_refresh_time": _state.get("last_refresh_time"),
            "last_error": _state.get("last_error"),
        }
    try:
        tmp_file = HEALTH_FILE + ".tmp"
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp_file, HEALTH_FILE)
    except Exception as exc:
        LOGGER.warning("Could not update health file: %s", exc)
    return data


def compute_health_status() -> tuple[str, int, dict]:
    data = update_health("ok")
    lrt = data.get("last_refresh_time")
    last_ok = data.get("last_refresh_ok")
    stale = False
    degraded = False
    if lrt:
        try:
            t = datetime.datetime.fromisoformat(lrt.replace("Z", "+00:00"))
            age = (datetime.datetime.now(datetime.timezone.utc) - t).total_seconds()
            if age > 1800:
                stale = True
        except Exception:
            stale = True
    else:
        stale = True
    if last_ok is False:
        degraded = True
    if stale:
        data["status"] = "stale"
        code = 503
    elif degraded:
        data["status"] = "degraded"
        code = 200
    else:
        data["status"] = "healthy"
        code = 200
    update_health(data["status"])
    return data["status"], code, data


def record_refresh(ok: bool, error: str | None = None) -> None:
    with _state_lock:
        _state["last_refresh_ok"] = ok
        _state["last_refresh_time"] = _now_iso()
        _state["last_error"] = error
    update_health("degraded" if not ok else "healthy")


def _host_allowed(raw: str | None) -> bool:
    if not raw:
        return False
    host = raw.strip().lower()
    # strip port; handle [::1]:port
    if host.startswith("["):
        end = host.find("]")
        if end != -1:
            host = host[1:end]
        else:
            host = host.strip("[]")
    elif ":" in host:
        # take before last : if looks like host:port and not bare ipv6
        if host.count(":") == 1:
            host = host.split(":", 1)[0]
    return host in ALLOWED_HOSTS


def take_instance_lock() -> bool:
    global INSTANCE_LOCK_FH
    try:
        os.makedirs(OPS_DIR, exist_ok=True)
        INSTANCE_LOCK_FH = open(LOCK_FILE, "a+b")
        msvcrt.locking(INSTANCE_LOCK_FH.fileno(), msvcrt.LK_NBLCK, 1)
        INSTANCE_LOCK_FH.seek(0)
        INSTANCE_LOCK_FH.truncate()
        INSTANCE_LOCK_FH.write(str(os.getpid()).encode())
        INSTANCE_LOCK_FH.flush()
        return True
    except Exception:
        LOGGER.info("another instance runs")
        return False


class ControlRoomHandler(BaseHTTPRequestHandler):
    server_version = "SIRControlRoom/1.0"
    timeout = 15

    def setup(self):
        super().setup()
        try:
            self.connection.settimeout(15)
        except Exception:
            pass

    def log_message(self, fmt: str, *args) -> None:
        LOGGER.info("%s - %s", self.address_string(), fmt % args)

    def _gate(self) -> bool:
        if not _host_allowed(self.headers.get("Host")):
            self._send_simple(403, "Forbidden")
            return False
        return True

    def _send_simple(self, code: int, text: str) -> None:
        body = text.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("Permissions-Policy", "geolocation=(), camera=(), microphone=()")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _send_json(self, code: int, payload: dict) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _serve_file(self, rel: str) -> None:
        # only allow specific files in PUBLIC_DIR root
        allowed = {"dashboard.html", "favicon.ico", "favicon.svg", "manifest.json", "health.json"}
        name = os.path.basename(rel)
        if rel not in allowed and name not in allowed:
            self._send_simple(404, "Not Found")
            return
        path = os.path.join(PUBLIC_DIR, name)
        if not os.path.isfile(path):
            self._send_simple(404, "Not Found")
            return
        ctype = "text/plain; charset=utf-8"
        if name.endswith(".html"):
            ctype = "text/html; charset=utf-8"
        elif name.endswith(".json"):
            ctype = "application/json; charset=utf-8"
        elif name.endswith(".svg"):
            ctype = "image/svg+xml"
        elif name.endswith(".ico"):
            ctype = "image/x-icon"
        try:
            with open(path, "rb") as f:
                body = f.read()
        except Exception:
            self._send_simple(404, "Not Found")
            return
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("Permissions-Policy", "geolocation=(), camera=(), microphone=()")
        if name.endswith(".html"):
            self.send_header("Cache-Control", "no-cache, must-revalidate")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def do_GET(self):
        if not self._gate():
            return
        parsed = urlparse(self.path)
        path = unquote(parsed.path)
        if path in ("/", "/index.html", "/app"):
            self.send_response(302)
            self.send_header("Location", "/dashboard.html")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            return
        if path in ("/health", "/api/health", "/health.json", "/control-room-health.json"):
            _, code, payload = compute_health_status()
            self._send_json(code, payload)
            return
        if path == "/refresh-now":
            # loopback-only endpoint; gate already enforced host
            threading.Thread(target=run_refresh_once, daemon=True).start()
            self._send_json(200, {"ok": True, "message": "refresh started"})
            return
        # only serve known public files at root
        if path.startswith("/"):
            rel = path.lstrip("/")
        else:
            rel = path
        self._serve_file(rel)

    def do_HEAD(self):
        if not self._gate():
            return
        # reuse GET logic but no body
        self.do_GET()

    def do_POST(self):
        if not self._gate():
            return
        self._send_simple(405, "Method Not Allowed")

    def handle_one_request(self):
        try:
            super().handle_one_request()
        except (ConnectionResetError, BrokenPipeError, ConnectionAbortedError, TimeoutError, OSError, socket.timeout):
            pass

    def handle(self):
        try:
            super().handle()
        except (ConnectionResetError, BrokenPipeError, ConnectionAbortedError, TimeoutError, OSError, socket.timeout):
            pass


class Server(ThreadingHTTPServer):
    allow_reuse_address = False
    daemon_threads = True


def run_refresh_once() -> None:
    flags = 0x08000000 if sys.platform == "win32" else 0
    py_exec = sys.executable or "python.exe"
    try:
        res = subprocess.run(
            [py_exec, REFRESH_SCRIPT],
            capture_output=True,
            text=True,
            timeout=120,
            creationflags=flags,
        )
        if res.returncode == 0:
            record_refresh(True, None)
        else:
            err = (res.stderr or res.stdout or "refresh failed")[-500:]
            record_refresh(False, err)
            LOGGER.error("refresh failed: %s", err)
    except Exception as e:
        record_refresh(False, str(e)[:500])
        LOGGER.error("refresh error: %s", e)


def heartbeat_loop():
    while True:
        time.sleep(60)
        compute_health_status()


def run_server():
    LOGGER.info("SIR Control Room Daemon initializing (PID %s).", os.getpid())
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    update_health("starting")
    t_heartbeat = threading.Thread(target=heartbeat_loop, daemon=True, name="ControlRoomHeartbeat")
    t_heartbeat.start()
    retry_count = 0
    while True:
        try:
            server = Server((HOST, PORT), ControlRoomHandler)
            LOGGER.info("HTTP Server listening successfully on http://%s:%s", HOST, PORT)
            retry_count = 0
            server.serve_forever()
        except KeyboardInterrupt:
            LOGGER.info("Shutdown signal received. Exiting.")
            update_health("stopped")
            break
        except Exception as exc:
            retry_count += 1
            LOGGER.error("Supervisor error (attempt #%s): %s", retry_count, exc, exc_info=True)
            update_health("restarting")
            time.sleep(3)


def main():
    if not take_instance_lock():
        return
    run_server()


if __name__ == "__main__":
    main()
