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

    def do_GET(self):
        # Redirect root / to dashboard.html
        if self.path in ("/", "/index.html", "/app"):
            self.send_response(302)
            self.send_header("Location", "/dashboard.html")
            self.end_headers()
            return
        super().do_GET()


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

    server = HTTPServer(("127.0.0.1", 8899), ControlRoomHandler)
    print(f"Serving SIR Control Room on http://127.0.0.1:8899 from {OPS_DIR} (15-min auto-refresh active)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
