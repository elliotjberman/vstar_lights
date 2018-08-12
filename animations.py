#!/usr/bin/env python

import time, random
from colour_store import colours

# Globals (I know, bad)
NUM_TRIANGLES = 5

# Helper functions and classes

def dim_colour(colour, progress):
    return tuple(int(x*progress) for x in colour)

def clear_all(client):
    client.put_pixels([(0,0,0)] * 64 * NUM_TRIANGLES)

class Frame():

    def __init__(self, leds, opacity):
        self.leds = leds
        self.opacity = opacity

# Animations

class Animation():

    def __init__(self, *args, persistent=False, **kwargs):
        self.row_counts = [9,7,5,3,1]
        self.leds = [(0,0,0)] * sum(self.row_counts)
        self.colour = colours[kwargs['colour']]
        self.persistent = persistent
        self.frames = kwargs['frames']
        self.brightness = kwargs.get('brightness', 1) if not persistent else 1
        self.frames_remaining = self.frames if not persistent else 0 # fucking hack
        self.padding = min(self.frames, kwargs.get('padding', 0))

    def reset_frames(self, proportion=1):
        self.frames_remaining = int(proportion * self.frames)

    def animate(self):
        self.progress = abs(self.frames_remaining) / self.frames

        frame = self.animate_inner()
        if not self.persistent:
            self.frames_remaining -= 1

        return frame

    def finished(self):
        return self.frames_remaining < 0 and abs(self.frames_remaining) >= self.padding and not self.persistent


class FullFlash(Animation):

    def animate_inner(self):
        dimmed_colour = dim_colour(self.colour, self.progress * self.brightness)
        for i in range(len(self.leds)):
            self.leds[i] = dimmed_colour 

        return Frame(self.leds, self.progress)

class TopFlash(Animation):

    def animate_inner(self):
        self.progress = self.frames_remaining / self.frames
        dimmed_colour = dim_colour(self.colour, self.progress * self.brightness)
        for i in range(2 * self.row_counts[0] - 2, sum(self.row_counts)):
            self.leds[i] = dimmed_colour 

        return Frame(self.leds, self.progress)

class BottomFlash(Animation):

    def animate_inner(self):
        dimmed_colour = dim_colour(self.colour, self.progress * self.brightness)
        for i in range(self.row_counts[0] * 2 - 2):
            self.leds[i] = dimmed_colour 

        return Frame(self.leds, self.progress)

class BorderFlash(Animation):

    def animate_inner(self):
        dimmed_colour = dim_colour(self.colour, self.progress * self.brightness)
        
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

        return Frame(self.leds, self.progress)

class RowFlash(Animation):

    def __init__(self, *args, **kwargs):
        super(RowFlash, self).__init__(*args, **kwargs)
        scale = kwargs.get('scale', (0, 127)) 
        self.row = kwargs.get('row', 0)

    def animate_inner(self):
        start = sum(self.row_counts[:self.row])
        row = range(start, start + self.row_counts[self.row])
        dimmed_colour = dim_colour(self.colour, self.progress)

        for i in row:
            self.leds[i] = dimmed_colour

        return Frame(self.leds, self.progress)

class Sparkle(Animation):

    def __init__(self, *args, **kwargs):
        super(Sparkle, self).__init__(*args, **kwargs)
        self.density = kwargs.get('density', 1) # 1-25 is valid

    def animate_inner(self):
        for _ in range(self.density):
            choice = random.randrange(0, sum(self.row_counts))
            self.leds[choice] = self.colour
        for i in range(len(self.leds)):
            self.leds[i] = dim_colour(self.leds[i], self.progress * self.brightness)
        
        return Frame(self.leds, self.progress)
        

class RandomLines(Animation):

    def __init__(self, *args, **kwargs):
        super(RandomLines, self).__init__(*args, **kwargs)
        self.ranges = [range(0, 9), range(9, 16), range(16, 21), range(21, 24), range(24, 25)]

    def animate_inner(self):
        rand_range = random.choice(self.ranges)
        for i in rand_range:
            self.leds[i] = self.colour
        for i in range(len(self.leds)):
            self.leds[i] = dim_colour(self.leds[i], self.progress * self.brightness)

        return Frame(self.leds, self.progress)
        

class FillBottomUp(Animation):

    def animate_inner(self):
        index = 0
        for i in range(len(self.row_counts)):
            colour = dim_colour(self.colour,
                                max(0, 1 - self.progress - i/len(self.row_counts) + 0.5 * (1-self.progress)) * self.brightness)
                
            for j in range(index, index+self.row_counts[i]):
                self.leds[j] = colour
            index += self.row_counts[i]

        return Frame(self.leds, self.progress)

class FillTopDown(Animation):

    def animate_inner(self):
        index = 0
        for i in range(len(self.row_counts)):
            colour = dim_colour(self.colour,
                                max(0, i/len(self.row_counts) - self.progress + 0.5 * (1-self.progress)) * self.brightness)
            for j in range(index, index+self.row_counts[i]):
                self.leds[j] = colour

            index += self.row_counts[i]

        return Frame(self.leds, self.progress)


class DrainBottomUp(Animation):

    def animate_inner(self):
        index = 0
        for i in range(len(self.row_counts)):
            colour = dim_colour(self.colour,
                                max(0, 2 * self.progress - (1 - i/len(self.row_counts))) * self.brightness)
                
            for j in range(index, index+self.row_counts[i]):
                self.leds[j] = colour
            index += self.row_counts[i]

        return Frame(self.leds, self.progress)


class DrainTopDown(Animation):

    def animate_inner(self):
        index = 0
        for i in range(len(self.row_counts)):
            colour = dim_colour(self.colour,
                                max(0, self.progress - (i)/len(self.row_counts) + 0.5 * self.progress) * self.brightness)
                
            for j in range(index, index+self.row_counts[i]):
                self.leds[j] = colour
            index += self.row_counts[i]

        return Frame(self.leds, self.progress)


class FillMiddleOut(Animation):

    def animate_inner(self):
        middle_row = len(self.row_counts)//2
        index = 0
        for i in range(len(self.row_counts)):
            colour = dim_colour(self.colour,
                                max(0, 1 - (abs(i - middle_row)/middle_row) - self.progress + 0.8 * (1 - self.progress)) * self.brightness)
            for j in range(index, index+self.row_counts[i]):
                self.leds[j] = colour
            index += self.row_counts[i]

        return Frame(self.leds, self.progress)


class FillOutsideIn(Animation):

    def animate_inner(self):
        middle_row = len(self.row_counts)//2
        index = 0
        for i in range(len(self.row_counts)):
            colour = dim_colour(self.colour,
                                max(0, (abs(i - middle_row)/middle_row) - self.progress + 0.5 * (1 - self.progress)) * self.brightness)
            for j in range(index, index+self.row_counts[i]):
                self.leds[j] = colour
            index += self.row_counts[i]

        return Frame(self.leds, self.progress)


class DrainMiddleOut(Animation):

    def animate_inner(self):
        middle_row = len(self.row_counts)//2

        index = 0
        for i in range(len(self.row_counts)):
            colour = dim_colour(self.colour,
                                max(0, (abs(i - middle_row)/middle_row) + self.progress - 1 + 0.8 * self.progress) * self.brightness)
            for j in range(index, index+self.row_counts[i]):
                self.leds[j] = colour
            index += self.row_counts[i]

        return Frame(self.leds, self.progress)


class DrainOutsideIn(Animation):

    def animate_inner(self):
        middle_row = len(self.row_counts)//2

        index = 0
        for i in range(len(self.row_counts)):
            colour = dim_colour(self.colour,
                                max(0, self.progress - (abs(i - middle_row)/middle_row) + 0.5 * self.progress) * self.brightness)
            for j in range(index, index+self.row_counts[i]):
                self.leds[j] = colour
            index += self.row_counts[i]

        return Frame(self.leds, self.progress)
