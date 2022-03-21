import argparse
parser = argparse.ArgumentParser(description='The free and open-source Project Cowserve web server.')
parser.add_argument('port', metavar='port', type=int, nargs='+',
                    help='Tell Cowserver where to start the server (site will be located at localhost:<port>)')
arg = parse.parse_args()
print("             PROJECT COWSERVE - cross-platform web server\n                     Current Cowserve Version: 1.0\n                      Press Ctrl+C to stop server")
import os
import sys
import http.server
import socketserver
PORT = arg.port()
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Starting up at port", PORT = ".")
    try:
      httpd.serve_forever()
    except KeyboardInterrupt:
      print("Shutting down.")
      sys.exit()
