import os
import http.server
import socketserver
cd = os.getcwd()
if not os.path.isdir(f"{cd}/gweb-site"):
  raise FileNotFoundError(f"Could not locate gweb site at {cd}")
PORT = 5020
Handler = http.server.SimpleHTTPRequestHandler
os.chdir(cd + "/gweb-site")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
os.chdir(cd)