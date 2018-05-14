#!env/bin/python3.5

import urllib, threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import animations, renderer

PORT_NUMBER = 8000

class MidiHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(self.rfile.read(content_length).decode())
        print(post_data)
        if post_data['channel'][0] == "0":
            triangle = animations.FullFlash(colour="white", frames=5)
        else:
            triangle = animations.FullFlash(colour="mint", frames=10)

        triangle_1.add_layer(triangle)
        self.send_response(200)

server = HTTPServer(('0.0.0.0', PORT_NUMBER), MidiHandler)
triangle_1 = renderer.Renderer()

def animate():
    triangle_1.render()
    threading.Timer(1/60, animate).start()

animate()
server.serve_forever()
