#!env/bin/python3.5

import threading, random
import animations, renderer, opc
from colour_store import colours

triangles = []
for _ in range(2):
    triangles.append(renderer.Renderer())

client = opc.Client('localhost:7890')

animation_types = [
                   animations.FullFlash,
                   animations.Sparkle,
                   animations.BorderFlash,
                   animations.FillBottomUp,
                   animations.FillTopDown,
                   animations.DrainBottomUp,
                   animations.DrainTopDown,
                   animations.MiddleOut,
                  ]

def animate():
    leds = []
    for triangle in triangles:
        leds.extend(triangle.render())
        leds.extend([(0,0,0)] * (64 - 25))
        if not triangle.layers:
            colour = random.choice(list(colours.keys()))
            frames = random.randint(180, 600)
            animation = random.choice(animation_types)
            triangle.add_layer(animation(colour=colour, frames=frames))

    client.put_pixels(leds) 

    threading.Timer(1/60, animate).start()

animate()
