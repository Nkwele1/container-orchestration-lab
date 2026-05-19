from http.server import HTTPServer, BaseHTTPRequestHandler
import platform
import os
import json
from datetime import datetime

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Build system info response
        info = {
            "app": "SwoopOS Lab",
            "version": "1.0.0",
            "hostname": platform.node(),
            "os": platform.system(),
            "python_version": platform.python_version(),
            "timestamp": datetime.utcnow().isoformat(),
            "environment": os.environ.get("APP_ENV", "development")
        }

        # Send response
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(info, indent=2).encode())

    def log_message(self, format, *args):
        print(f"[{datetime.utcnow().isoformat()}] {format % args}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"Starting SwoopOS Lab server on port {port}")
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()