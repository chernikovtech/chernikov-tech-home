import http.server, os, functools

PORT = int(os.environ.get("PORT", 8080))
ROOT = os.path.dirname(os.path.abspath(__file__))

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)
    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("Cache-Control", "public, max-age=300")
        super().end_headers()

http.server.ThreadingHTTPServer(("0.0.0.0", PORT), H).serve_forever()
