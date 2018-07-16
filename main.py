#!env/bin/python3.5

import urllib, threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import opc, animations, renderer

PORT_NUMBER = 8000
client = opc.Client('localhost:7890')
triangles = []
for _ in range(2):
    triangles.append(renderer.Renderer())

class DemoHandler(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self.channels = [
            animations.BottomFlash(colour="mint", frames=15),
            animations.TopFlash(colour="off-white", frames=15),
            animations.BorderFlash(colour="mint", frames=180),
            animations.Sparkle(colour="yellow", frames=80),
            animations.FullFlash(colour="light-blue", frames=40),
            None,
            None,
            animations.Sparkle(colour="yellow", frames=60),
        ]
        BaseHTTPRequestHandler.__init__(self, *args, **kwargs)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(self.rfile.read(content_length).decode())

        i =  int(post_data['channel'][0])

        if self.channels[i]:
            triangles[1 if i > 1 else 0].add_layer(self.channels[i])
            if i == 7:
                triangles[0].add_layer(self.channels[i])

        self.send_response(200)

server = HTTPServer(('0.0.0.0', PORT_NUMBER), DemoHandler)

def animate():
    leds = []
    for triangle in triangles:
        leds.extend(triangle.render())
        leds.extend([(0,0,0)] * (64 - 25))

    client.put_pixels(leds) 

    threading.Timer(1/60, animate).start()

animate()               # Thread 1
server.serve_forever()  # Thread 2
