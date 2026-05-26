import http.server
import socketserver
import os

PORT = 3003

class ExtensionlessRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        elif '.' not in self.path:
            possible_html = self.path + '.html'
            if os.path.exists(possible_html.lstrip('/')):
                self.path = possible_html
        return super().do_GET()

class ReuseAddrTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    with ReuseAddrTCPServer(("", PORT), ExtensionlessRequestHandler) as httpd:
        print(f"Serving PORTFOLIO at http://localhost:{PORT}")
        httpd.serve_forever()
