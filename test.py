#!/usr/bin/env python

import opc, time, atexit
from animations import *

numLEDs = 25
client = opc.Client('localhost:7890')

atexit.register(lambda: clear(client))


while True:
    bottom_up(client, 0.1, "peach")
    top_down(client, 0.1, "mint")

