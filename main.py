#!env/bin/python3.5

import urllib, threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import animations, renderer

PORT_NUMBER = 8000

class DemoHandler(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self.channels = [
            animations.BottomFlash(colour="mint", frames=15),
            animations.TopFlash(colour="off-white", frames=15),
            animations.BorderFlash(colour="light-blue", frames=25),
            animations.Sparkle(colour="yellow", frames=80),
            None,
            None,
            None
        ]
        BaseHTTPRequestHandler.__init__(self, *args, **kwargs)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(self.rfile.read(content_length).decode())

        i =  int(post_data['channel'][0])

        if self.channels[i]:
            triangle_1.add_layer(self.channels[i])
        self.send_response(200)

server = HTTPServer(('0.0.0.0', PORT_NUMBER), DemoHandler)
triangle_1 = renderer.Renderer()

def animate():
    triangle_1.render()
    threading.Timer(1/60, animate).start()

animate()               # Thread 1
server.serve_forever()  # Thread 2
