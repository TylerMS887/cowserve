import argparse
import questionary
maze = """
--------+-------+
        |       |
| --+-+ | ----+ |
|   | | |     | |
| + | | +---- | |
|   | |       | | 
+-- | +----+- | |
|   | |    |  | | 
| --+ | ++ | -+
|     | ++    |  
+-----+-++----+--
""" # https://codegolf.stackexchange.com/q/162403
parser = argparse.ArgumentParser(description='The free and open-source Project Cowserve web server.', prog="cowserve")
parser.add_argument('--port', metavar='port', type=int, nargs='+', default=4000,
                    help='Tell Cowserve where to start the server (site will be located at localhost:<port>)')
arg = parser.parse_args()
questionary.print("             PROJECT COWSERVE - cross-platform web server\n                     Current Cowserve Version: 1.0\n                      Press Ctrl+C to stop server", style="italic")
import os
import http.server
import socketserver
PORT = str(arg.port)
PORT = PORT.replace("[", "")
PORT = PORT.replace("]", "")
PORT = int(PORT)
if not os.path.isfile(f"{os.getcwd()}/index.html"):
 addindex = questionary.confirm("Add an index.html?").ask()
 if addindex:
   with open(f"{os.getcwd()}/index.html", "w") as file:
     email = input("Please enter your email: ")
     file.write(f"""
          <title>Cowserve</title>
          <div align='center'>
          <h1>It works!</h1>
          </div>
          This page is used to test proper installation of Cowserve. You should edit this file, <code>index.html</code>, before continuing.
          If you are a regular user of this website, and did not expect this page, contact the <a href='mailto:{email}'>site's admin</a>.
          <h2>About Cowserve</h2>
          <b>Cowserve</b> (also known as <b>Project Cowserve</b>) is a <a href='https://en.wikipedia.org/wiki/Free_and_open-source_software'>free and open-source</a>
          web server written in a free and open-source programming language, Python. It supports many features, including:
          <li>
          PHP support (if installed)
          </li><li>
          SQL databases
          </li><li>
          Servers at any port
          </li>
          <h2>Getting started</h2>
          <p>
          We can create a new "hello" folder, then add a hello.html to it, then add some HTML syntax to it.
          </p>
          <p>
          Then, if we go to <code>hello/hello.html</code>, our HTML syntax is shown. Going only to <code>hello</code>
          will just show a link to our <code>hello.html</code>. Cowserve by default displays a list of files
          in a folder if there is no <code>index.html</code>.
          </p>
          <h2>Bugs</h2>
          If you find any bugs, please use the <a href='https://github.com/Tyler887/cowserve/issues'>issue tracker on GitHub</a>. Remember to search for
          existing issues before opening a new one.
    """)

class Handler(http.server.SimpleHTTPRequestHandler):
    def send_error(self, code, message=None):
        if code = 404:
          if os.path.isfile(f"{os.getcwd()}/404.html"):
            with open(f"{os.getcwd()}/404.html", "r") as NotFoundPage:
              self.error_message_format = NotFoundPage.read()
          else:
             print("To customise your 404 page, just create 404.html in your server directory!")
             self.error_message_format = f"""
             <title>Maze found - Cowserve</title>
             <pre>
             {maze}<br />
                   404 Not Found. Contact the admin for more info.
             </pre>
             <a href="https://codegolf.stackexchange.com/q/162403">Thanks Stack Exchange</a> for the maze! :)
             """
        else:
          self.error_message_format = "Error %(code)d: %(message)s. Contact the admin for more info. :("
        http.server.SimpleHTTPRequestHandler.send_error(self, code, message)
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Starting up site at port", str(PORT) + ".")
    try:
      httpd.serve_forever()
    except Exception as e:
      print(f"cowserve: {e}")
