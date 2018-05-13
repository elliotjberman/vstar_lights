#!/usr/bin/env python

import time, random
from colour_store import colours

# Globals (I know, bad)

NUMLEDS = 25

# Helper functions

def dim_colour(colour, brightness):
    return tuple(int(x*brightness) for x in colour)

# Animations

class Frame():

    def __init__(self, leds, opacity):
        self.leds = leds
        self.opacity = opacity

class FullFlash():

    def __init__(self, frames=60, colour="white"):
        self.leds = [(0,0,0)] * NUMLEDS
        self.frames_remaining = self.frames = frames
        self.colour = colours[colour]

    def finished(self):
        return self.frames_remaining < 0

    def animate(self):
        brightness = self.frames_remaining / self.frames
        dimmed_colour = dim_colour(self.colour, brightness)
        for i in range(len(self.leds)):
            self.leds[i] = dimmed_colour 

        self.frames_remaining -= 1
        return Frame(self.leds, brightness)

def bottom_up(client, speed, colour):
    colour_rgb = colours[colour]

    total=9
    row_size=9
    while row_size>0:
        client.put_pixels([colour_rgb] * total)
        time.sleep(speed)
        row_size -= 2
        total += row_size

    total=9
    row_size=9
    while row_size>0:
        client.put_pixels([(0,0,0)] * total)
        time.sleep(speed)
        row_size -= 2
        total += row_size

def top_down(client, speed, colour):
    colour_rgb = colours[colour]

    total=1
    row_size=1
    while row_size <= 9:
        frame = [(0,0,0)] * NUMLEDS
        i = total
        while i:
            frame[-i] = colour_rgb
            i -=1
        client.put_pixels(frame)
        time.sleep(speed)
        row_size += 2
        total += row_size

    total=1
    row_size=1
    while row_size <= 9:
        frame = [colour_rgb] * NUMLEDS
        i = total
        while i:
            frame[-i] = (0,0,0)
            i -=1
        client.put_pixels(frame)
        time.sleep(speed)
        row_size += 2
        total += row_size

def sparkle(client, speed, colour, density=1):
    while True:
        frame = [(0,0,0)] * NUMLEDS
        for _ in range(density):
            choice = random.randrange(0, NUMLEDS)
            frame[choice] = colours[colour]
        client.put_pixels(frame)
        time.sleep(speed)


def clear(client):
    client.put_pixels([(0,0,0)] * NUMLEDS)
