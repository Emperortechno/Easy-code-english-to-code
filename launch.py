import http.server
import socketserver
import webbrowser
import threading
import time
import os

# Configuration
PORT = 8080
FILENAME = "index.html" # Ensure your translator file is named this

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Keeps the console clean
        return

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🚀 Consortium Translator is live at http://localhost:{PORT}")
        print("Story Mode: Enabled (Techno, Dark Lambo, Anti-Dragons)")
        print("Press Ctrl+C to stop the server.")
        httpd.serve_forever()

def open_browser():
    # Wait a moment for the server to start
    time.sleep(1)
    webbrowser.open(f"http://localhost:{PORT}")

if __name__ == "__main__":
    # Check if index.html exists
    if not os.path.exists(FILENAME):
        print(f"❌ Error: {FILENAME} not found in this folder!")
    else:
        # Start server in a separate thread so it doesn't block the script
        threading.Thread(target=start_server, daemon=True).start()
        open_browser()
        
        # Keep the main thread alive
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nShutting down server. Goodbye!")
