#!/usr/bin/env python3
"""Lightweight local server for SIR Control Room dashboard on port 8899.
Includes automated 15-minute telemetry refresh loop for website & Claude artifact.
"""
import os
import sys
import time
import threading
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler

HERE = os.path.dirname(os.path.abspath(__file__))
OPS_DIR = os.path.normpath(os.path.join(HERE, "..", "ops"))
REFRESH_SCRIPT = os.path.join(HERE, "refresh-control-room.py")


class ControlRoomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=OPS_DIR, **kwargs)

    def end_headers(self):
        # Strict security headers & cache controls
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("Permissions-Policy", "geolocation=(), camera=(), microphone=()")
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
    # Initial sleep of 10 seconds after server launch
    time.sleep(10)
    while True:
        try:
            subprocess.run([sys.executable, REFRESH_SCRIPT], capture_output=True, text=True)
        except Exception as e:
            print(f"[refresh_loop] Error during refresh: {e}")
        time.sleep(900)  # 15 minutes


def main():
    # Start background refresh worker daemon thread
    t = threading.Thread(target=refresh_loop, daemon=True, name="ControlRoomRefreshWorker")
    t.start()

    server = RobustHTTPServer(("127.0.0.1", 8899), ControlRoomHandler)
    print(f"Serving SIR Control Room on http://127.0.0.1:8899 from {OPS_DIR} (15-min auto-refresh active)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
