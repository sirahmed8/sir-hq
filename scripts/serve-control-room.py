#!/usr/bin/env python3
"""Lightweight local server for SIR Control Room dashboard on port 8899."""
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

OPS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "ops"))

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

def main():
    server = HTTPServer(("127.0.0.1", 8899), ControlRoomHandler)
    print(f"Serving SIR Control Room on http://127.0.0.1:8899 from {OPS_DIR}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
