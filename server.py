import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'<h1>Subdomain Takeover By Abir</h1>')


httpd = socketserver.TCPServer(('', 8001), Handler)
httpd.serve_forever()
