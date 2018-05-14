#!env/bin/python3.5

import urllib, threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import animations, renderer

PORT_NUMBER = 8000

class DemoHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(self.rfile.read(content_length).decode())

        print(post_data)

        if post_data['channel'][0] == "0":
            triangle = animations.BottomFlash(colour="white", frames=10)

        elif post_data['channel'][0] == "4":
            triangle = animations.TopFlash(colour="peach", frames=10)

        elif post_data['channel'][0] == "6":
            triangle = animations.Sparkle(colour="peach", frames=40)

        else:
            triangle = animations.TopFlash(colour="mint", frames=10)

        triangle_1.add_layer(triangle)
        self.send_response(200)

server = HTTPServer(('0.0.0.0', PORT_NUMBER), DemoHandler)
triangle_1 = renderer.Renderer()

def animate():
    triangle_1.render()
    threading.Timer(1/60, animate).start()

animate()               # Thread 1
server.serve_forever()  # Thread 2
