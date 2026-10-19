"""
BlockTrack Local Server Runner.
Launches a lightweight local HTTP server and opens the DApp in your browser.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    os.chdir(DIRECTORY)
    server_address = ("", PORT)

    # Allow port reuse
    socketserver.TCPServer.allow_reuse_address = True

    try:
        with socketserver.TCPServer(server_address, Handler) as httpd:
            url = f"http://localhost:{PORT}"
            print("=" * 60)
            print(" BLOCKTRACK DAPP SERVER RUNNING")
            print("=" * 60)
            print(f" URL: {url}")
            print(f" Serving Directory: {DIRECTORY}")
            print(" Opening web browser automatically...")
            print(" Press Ctrl+C in this window to stop the server.")
            print("=" * 60)

            # Open browser automatically
            webbrowser.open(url)

            # Start serving requests
            httpd.serve_forever()
    except OSError as e:
        if "already in use" in str(e).lower() or e.errno == 98 or e.errno == 10048:
            alt_port = 8080
            print(f" Port {PORT} is busy, switching to http://localhost:{alt_port}...")
            with socketserver.TCPServer(("", alt_port), Handler) as httpd:
                webbrowser.open(f"http://localhost:{alt_port}")
                httpd.serve_forever()
        else:
            raise e

if __name__ == "__main__":
    start_server()
