#!/usr/bin/env python

import time, random
from colour_store import colours

# Globals (I know, bad)
NUM_TRIANGLES = 5
NUM_LEDS = 25

# Helper functions and classes

def dim_colour(colour, brightness):
    return tuple(int(x*brightness) for x in colour)

def clear_all(client):
    client.put_pixels([(0,0,0)] * 64 * NUM_TRIANGLES)

class Frame():

    def __init__(self, leds, opacity):
        self.leds = leds
        self.opacity = opacity

# Animations

class Animation():

    def __init__(self, frames=60, colour="white"):
        self.leds = [(0,0,0)] * NUM_LEDS
        self.frames_remaining = self.frames = frames
        self.colour = colours[colour]
        self.row_counts = [9,7,5,3,1]

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

class TopFlash(Animation):

    def animate(self):
        brightness = self.frames_remaining / self.frames
        dimmed_colour = dim_colour(self.colour, brightness)
        for i in range(2 * self.row_counts[0] - 2, NUM_LEDS):
            self.leds[i] = dimmed_colour 

        self.frames_remaining -= 1
        return Frame(self.leds, brightness)

class BottomFlash(Animation):

    def animate(self):
        brightness = self.frames_remaining / self.frames
        dimmed_colour = dim_colour(self.colour, brightness)
        for i in range(self.row_counts[0] * 2 - 2):
            self.leds[i] = dimmed_colour 

        self.frames_remaining -= 1
        return Frame(self.leds, brightness)

class BorderFlash(Animation):

    def animate(self):
        brightness = self.frames_remaining / self.frames
        dimmed_colour = dim_colour(self.colour, brightness)
        
        row = self.row_counts[0]
        i = 0
        for i in range(row):
            self.leds[i] = dimmed_colour
        i = row
        row -= 2

        while row > 0:
            self.leds[i] = dimmed_colour 
            self.leds[i+row-1] = dimmed_colour

            i += row
            row -= 2

        self.frames_remaining -= 1
        return Frame(self.leds, brightness)

class Sparkle(Animation):

    def __init__(self, *args, **kwargs):
        super(Sparkle, self).__init__(*args, **kwargs)
        self.density = kwargs.get('density', 1)

    def animate(self):
        brightness = self.frames_remaining / self.frames
        for _ in range(1):
            choice = random.randrange(0, NUM_LEDS)
            self.leds[choice] = self.colour
        for i in range(len(self.leds)):
            self.leds[i] = dim_colour(self.leds[i], brightness)
        
        self.frames_remaining -= 1
        return Frame(self.leds, brightness)
        

class FillBottomUp(Animation):

    def animate(self):
        brightness = self.frames_remaining / self.frames

        index = 0
        for i in range(len(self.row_counts)):
            # i+2 allows final row to get some time
            colour = dim_colour(self.colour,
                                max(0, 1 - brightness - (i-2)/len(self.row_counts)))
                
            for j in range(index, index+self.row_counts[i]):
                self.leds[j] = colour
            index += self.row_counts[i]

        self.frames_remaining -= 1
        return Frame(self.leds, brightness)

class FillTopDown(Animation):

    def animate(self):
        brightness = self.frames_remaining / self.frames

        index = 0
        for i in range(len(self.row_counts)):
            # i+2 allows final row to get some time
            colour = dim_colour(self.colour,
                                max(0, (i+2)/len(self.row_counts) - brightness))
            for j in range(index, index+self.row_counts[i]):
                self.leds[j] = colour

            index += self.row_counts[i]

        self.frames_remaining -= 1
        return Frame(self.leds, brightness)


class DrainBottomUp(Animation):

    def animate(self):
        brightness = self.frames_remaining / self.frames

        index = 0
        for i in range(len(self.row_counts)):
            colour = dim_colour(self.colour,
                                max(0, brightness - (1 - (i+1)/len(self.row_counts))))
                
            for j in range(index, index+self.row_counts[i]):
                self.leds[j] = colour
            index += self.row_counts[i]

        self.frames_remaining -= 1
        return Frame(self.leds, brightness)


class DrainTopDown(Animation):

    def animate(self):
        brightness = self.frames_remaining / self.frames

        index = 0
        for i in range(len(self.row_counts)):
            colour = dim_colour(self.colour,
                                max(0, brightness - (i-1)/len(self.row_counts)))
                
            for j in range(index, index+self.row_counts[i]):
                self.leds[j] = colour
            index += self.row_counts[i]

        self.frames_remaining -= 1
        return Frame(self.leds, brightness)


class MiddleOut(Animation):

    def animate(self):
        brightness = self.frames_remaining / self.frames
        middle_row = len(self.row_counts)//2

        index = 0
        for i in range(len(self.row_counts)):
            colour = dim_colour(self.colour,
                                min(1, 1.4 - (abs(i - middle_row)/middle_row) - brightness))
            for j in range(index, index+self.row_counts[i]):
                self.leds[j] = colour
            index += self.row_counts[i]

        self.frames_remaining -= 1
        return Frame(self.leds, brightness)
