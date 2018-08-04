#!env/bin/python3.5

import urllib, threading, sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pynput import keyboard
import opc, renderer
from programmes import *

PORT_NUMBER = 8000
client = opc.Client('localhost:7890')
triangles = []
for _ in range(5):
    triangles.append(renderer.Renderer())

# Global crap
i=0
programmes = {
    'europe': europe,
    'red_europe': red_europe
}
set_list = ['europe', 'red_europe']


class TriggerHandler(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        BaseHTTPRequestHandler.__init__(self, *args, **kwargs)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(self.rfile.read(content_length).decode())

        global i
        programme = programmes[set_list[i]]
        programme.handle_message(post_data, triangles)

        self.send_response(200)

server = HTTPServer(('0.0.0.0', PORT_NUMBER), TriggerHandler)
def animate():
    leds = []
    for triangle in triangles:
        leds.extend(triangle.render())
        leds.extend([(0,0,0)] * (64 - 25))

    client.put_pixels(leds)

    threading.Timer(1/60, animate).start()

# Keyboard crap
def on_press(key):
    if key == keyboard.Key.right:
        global i
        if i < len(set_list)-1:
            i+=1
        print(set_list[i])
    if key == keyboard.Key.left:
        if i > 0:
            i-=1
        print(set_list[i])
    elif key == keyboard.Key.esc:
        sys.exit()

listener = keyboard.Listener(on_press=on_press)
listener.start()        # Thread 0
animate()               # Thread 1
server.serve_forever()  # Thread 2
