#!/usr/bin/env python

import time, random
from colour_store import colours

# Globals (I know, bad)

NUMLEDS = 25

# Helper functions

def dim_colour(colour, brightness):
    return tuple(int(x*brightness) for x in colour)

# Animations

class Animation():

    def __init__(self, frames=60, colour="white"):
        self.leds = [(0,0,0)] * NUMLEDS
        self.frames_remaining = self.frames = frames
        self.colour = colours[colour]

    def finished(self):
        return self.frames_remaining < 0


class FullFlash(Animation):

    def animate(self):
        brightness = self.frames_remaining / self.frames
        dimmed_colour = dim_colour(self.colour, brightness)
        for i in range(len(self.leds)):
            self.leds[i] = dimmed_colour 

        self.frames_remaining -= 1
        return Frame(self.leds, brightness)

class Sparkle(Animation):

    # def __init__(self, density=1):
    #     self.density = density

    def animate(self):
        brightness = self.frames_remaining / self.frames
        for _ in range(4):
            choice = random.randrange(0, NUMLEDS)
            self.leds[choice] = self.colour
        for i in range(len(self.leds)):
            self.leds[i] = dim_colour(self.leds[i], brightness)
        
        self.frames_remaining -= 1
        return Frame(self.leds, brightness)
        

class Frame():

    def __init__(self, leds, opacity):
        self.leds = leds
        self.opacity = opacity

class BottomUp(Animation):

    def animate():
        brightness = self.frames_remaining / self.frames

        for i in range(total):
            self.leds[i] = self.colour
        row_size -= 2
        total += row_size
        return Frame(self.leds, brightness)


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



def clear(client):
    client.put_pixels([(0,0,0)] * NUMLEDS)
