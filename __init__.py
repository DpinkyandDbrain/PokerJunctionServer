__author__ = 'DpinkyandDbrain'

#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from cgi import parse_header, parse_multipart, parse, parse_qsl
from Room import Room
PORT_NUMBER = 8080
ROOM = None

# This class will handles any incoming request from
# the browser


# Subclass HTTPServer with some additional callbacks
class CallbackHTTPServer(HTTPServer):

    def server_activate(self):
        ROOM = self.RequestHandlerClass.pre_start()
        HTTPServer.server_activate(self)
        self.RequestHandlerClass.post_start()

    def server_close(self):
        self.RequestHandlerClass.pre_stop()
        HTTPServer.server_close(self)
        self.RequestHandlerClass.post_stop()


# HTTP request handler
class PokerJunctionHandler(BaseHTTPRequestHandler):

    @staticmethod
    def pre_start():
        print 'Setting up the room'
        return Room(2)

    @staticmethod
    def post_start():
        print 'Placing chips and assigning dealers to tables'

    @staticmethod
    def pre_stop():
        print 'Before putting chips and cards away'

    @staticmethod
    def post_stop():
        print 'After putting chips and cards away'

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("Hello World !")
        return

    def do_POST(self):
        ctype, pdict = parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            postvars = parse(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}
        return

try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = CallbackHTTPServer(('', PORT_NUMBER), PokerJunctionHandler)
    print 'The Poker Junction Server has started on port ', PORT_NUMBER
    # Wait forever for incoming http requests
    server.serve_forever()
except KeyboardInterrupt:
    print 'Interrupt received, shutting down the web server'
    server.server_close()
