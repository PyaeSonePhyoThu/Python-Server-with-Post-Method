from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        print("Exfiltrated data:")
        print(post_data.decode('utf-8'))
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Data received\n")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()