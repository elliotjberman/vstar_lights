#!env/bin/python3.5

import urllib, threading, sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from setproctitle import setproctitle
from pynput import keyboard
import opc, renderer
from songs import *

PORT_NUMBER = 8000
client = opc.Client('localhost:7890')
triangles = []
for _ in range(5):
    triangles.append(renderer.Renderer())

# Global crap
i=0
set_list = [beg, europe, teenager, blinds, jellyfish, waited]

def reset_crap():
    for j in range(len(set_list)):
        for key in set_list[j].persisted_layers.keys():
            set_list[j].persisted_layers[key] = {}
    for triangle in triangles:
        triangle.clear_layers()

class TriggerHandler(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        BaseHTTPRequestHandler.__init__(self, *args, **kwargs)

    # Don't log successful messages (there's way too many)
    def log_message(self, format, *args):
        if args[1] != '200':
            super(TriggerHandler, self).log_message(format, *args)
        return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(self.rfile.read(content_length).decode())

        global i
        programme = set_list[i]
        programme.handle_message(post_data, triangles)

        self.send_response(200)

server = HTTPServer(('0.0.0.0', PORT_NUMBER), TriggerHandler)
def animate():
    leds = []
    for triangle in triangles:
        leds.extend(triangle.render())
        leds.extend([(0,0,0)] * (64 - 25))

    client.put_pixels(leds)

    # 30 fps is fine
    threading.Timer(1/30, animate).start()

# Keyboard crap
def on_press(key):
    global i
    try:
        if int(key.char) in range(len(set_list)+1):
            i=int(key.char) - 1
            print(set_list[i].name)
    except Exception as e:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()        # Thread 1
animate()               # Thread 2
server.serve_forever()  # Thread 3
