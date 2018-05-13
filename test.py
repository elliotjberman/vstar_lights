#!/usr/bin/python3.5

import opc, time, atexit
from animations import *

numLEDs = 25
client = opc.Client('localhost:7890')

atexit.register(lambda: clear(client))


triangle = FullFlash(colour="peach", frames=20)

while True:
    # bottom_up(client, 0.05, "peach")
    # top_down(client, 0.05, "mint")
    # sparkle(client, 0.05, "peach", 1)
    
    if not triangle.finished():
        client.put_pixels(triangle.animate())

    time.sleep(1/60) # 60 FPS
