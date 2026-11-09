#!/usr/bin/env python3
"""Lightweight sovereign daemon for SIR Control Room dashboard on port 8899.
Runs detached and windowless under wscript.exe + pythonw.exe at user logon.
Features:
- Dedicated file logging to ops/control-room-server.log
- Live JSON health telemetry at /health and ops/control-room-health.json
- Self-healing supervisor loop with automatic restart on unexpected exit
- Background 15-minute telemetry refresh worker for artifact & static files
- Strict security headers & ETag cache validation
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
from http.server import HTTPServer, SimpleHTTPRequestHandler

HERE = os.path.dirname(os.path.abspath(__file__))
OPS_DIR = os.path.normpath(os.path.join(HERE, "..", "ops"))
LOG_FILE = os.path.join(OPS_DIR, "control-room-server.log")
HEALTH_FILE = os.path.join(OPS_DIR, "control-room-health.json")
REFRESH_SCRIPT = os.path.join(HERE, "refresh-control-room.py")
PORT = 8899
HOST = "127.0.0.1"


class FileLoggerStream:
    """Safe stream wrapper redirecting stdout/stderr to disk when running under pythonw."""
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
    """Configures structured file logging and guards against pythonw NoneType stdout."""
    logger = logging.getLogger("ControlRoomServer")
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers on supervisor restart
    if not logger.handlers:
        os.makedirs(OPS_DIR, exist_ok=True)
        fh = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    # Redirect stdout and stderr safely
    sys.stdout = FileLoggerStream(logger, logging.INFO)
    sys.stderr = FileLoggerStream(logger, logging.ERROR)

    return logger


LOGGER = setup_logging()
START_TIME = datetime.datetime.now(datetime.timezone.utc).isoformat()


def write_health_file(status: str = "healthy") -> None:
    """Writes live telemetry state for Laptop Manager and status dashboards."""
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    health_data = {
        "service": "SIR Control Room",
        "task_name": "SIR_ControlRoom_Server",
        "port": PORT,
        "host": HOST,
        "pid": os.getpid(),
        "status": status,
        "mode": "detached_daemon",
        "started_at": START_TIME,
        "last_heartbeat": now_iso,
        "tailscale_proxy": "https://ahmed.tail9e9aa7.ts.net:8899",
        "refresh_interval_sec": 900,
    }
    try:
        tmp_file = HEALTH_FILE + ".tmp"
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(health_data, f, indent=2)
        os.replace(tmp_file, HEALTH_FILE)
    except Exception as exc:
        LOGGER.warning(f"Could not update health file: {exc}")


class ControlRoomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=OPS_DIR, **kwargs)

    def log_message(self, format: str, *args) -> None:
        # Route standard request access logs directly through our file logger
        LOGGER.info(f"{self.address_string()} - {format % args}")

    def end_headers(self):
        # Strict security headers & cache controls
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("Permissions-Policy", "geolocation=(), camera=(), microphone=()")
        if getattr(self, "_current_etag", None):
            self.send_header("ETag", self._current_etag)
        if self.path.endswith((".html", "/")):
            self.send_header("Cache-Control", "no-cache, must-revalidate")
        super().end_headers()

    def do_GET(self):
        # Redirect root / to dashboard.html
        if self.path in ("/", "/index.html", "/app"):
            self.send_response(302)
            self.send_header("Location", "/dashboard.html")
            self.end_headers()
            return

        # Dedicated live health telemetry endpoint
        if self.path in ("/health", "/api/health", "/health.json", "/control-room-health.json"):
            payload = {
                "service": "SIR Control Room",
                "task_name": "SIR_ControlRoom_Server",
                "port": PORT,
                "host": HOST,
                "pid": os.getpid(),
                "status": "healthy",
                "mode": "detached_daemon",
                "started_at": START_TIME,
                "last_heartbeat": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "tailscale_proxy": "https://ahmed.tail9e9aa7.ts.net:8899",
            }
            body = json.dumps(payload, indent=2).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
            return

        # ETag conditional validation for dashboard.html
        clean_path = self.path.split("?")[0]
        if clean_path == "/dashboard.html":
            hash_file = os.path.join(OPS_DIR, "artifact", "CHANGED.txt")
            if os.path.exists(hash_file):
                try:
                    with open(hash_file, "r", encoding="utf-8") as f:
                        current_etag = f'"{f.read().strip()}"'
                    client_etag = self.headers.get("If-None-Match", "").strip()
                    if client_etag and client_etag == current_etag:
                        self.send_response(304)
                        self.send_header("ETag", current_etag)
                        self.send_header("Cache-Control", "no-cache, must-revalidate")
                        self.end_headers()
                        return
                    self._current_etag = current_etag
                except Exception:
                    pass
        super().do_GET()

    def handle_one_request(self):
        try:
            super().handle_one_request()
        except (ConnectionResetError, BrokenPipeError, ConnectionAbortedError, TimeoutError, OSError):
            pass

    def handle(self):
        try:
            super().handle()
        except (ConnectionResetError, BrokenPipeError, ConnectionAbortedError, TimeoutError, OSError):
            pass


class RobustHTTPServer(HTTPServer):
    def handle_error(self, request, client_address):
        exc_type, exc_val, _ = sys.exc_info()
        if exc_type in (ConnectionResetError, BrokenPipeError, ConnectionAbortedError, TimeoutError):
            return
        if isinstance(exc_val, OSError) and getattr(exc_val, "winerror", None) in (10053, 10054):
            return
        super().handle_error(request, client_address)


def refresh_loop():
    """Background worker that refreshes dashboard and artifact every 15 minutes."""
    time.sleep(10)
    flags = 0x08000000 if sys.platform == "win32" else 0
    py_exec = sys.executable or "python.exe"
    while True:
        try:
            subprocess.run([py_exec, REFRESH_SCRIPT], capture_output=True, text=True, creationflags=flags)
            LOGGER.info("[refresh_loop] Successfully executed background telemetry refresh")
        except Exception as e:
            LOGGER.error(f"[refresh_loop] Error during refresh: {e}")
        time.sleep(900)  # 15 minutes


def heartbeat_loop():
    """Background worker that maintains health telemetry timestamps."""
    while True:
        time.sleep(60)
        write_health_file("healthy")


def run_server_supervised():
    """Supervisor loop: maintains server lifecycle with automatic recovery on unexpected failures."""
    LOGGER.info(f"SIR Control Room Daemon initializing (PID {os.getpid()}).")
    LOGGER.info(f"Binding listener to {HOST}:{PORT} (serving {OPS_DIR}).")

    write_health_file("healthy")

    # Start background threads
    t_refresh = threading.Thread(target=refresh_loop, daemon=True, name="ControlRoomRefreshWorker")
    t_refresh.start()

    t_heartbeat = threading.Thread(target=heartbeat_loop, daemon=True, name="ControlRoomHeartbeatWorker")
    t_heartbeat.start()

    retry_count = 0
    while True:
        try:
            server = RobustHTTPServer((HOST, PORT), ControlRoomHandler)
            LOGGER.info(f"HTTP Server listening successfully on http://{HOST}:{PORT}")
            retry_count = 0
            server.serve_forever()
        except KeyboardInterrupt:
            LOGGER.info("Shutdown signal received (KeyboardInterrupt). Exiting cleanly.")
            write_health_file("stopped")
            break
        except Exception as exc:
            retry_count += 1
            LOGGER.error(f"Supervisor detected server error (attempt #{retry_count}): {exc}", exc_info=True)
            write_health_file("restarting")
            time.sleep(3)
            LOGGER.info("Supervisor restarting HTTP server...")


def main():
    run_server_supervised()


if __name__ == "__main__":
    main()
