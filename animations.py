#!/usr/bin/env python

import time
from colour_store import colours

def bottom_up(client, speed, colour):
    colour_rgb = colours[colour]

    total=9
    row_size=9
    while row_size>0:
        client.put_pixels([colour_rgb] * total)
        time.sleep(speed)
        row_size -= 2
        total += row_size

def top_down(client, speed, colour):
    colour_rgb = colours[colour]

    total=1
    row_size=1
    while row_size <= 9:
        frame = [(0,0,0)] * 25
        i = total
        while i:
            frame[-i] = (colour_rgb)
            i -=1
        client.put_pixels(frame)
        time.sleep(speed)
        row_size += 2
        total += row_size

def clear(client):
    client.put_pixels([(0,0,0)] * 25)
