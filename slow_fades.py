#!env/bin/python3.5

import threading, random, atexit
import animations, renderer, opc
from colour_store import colours

triangles = []
for _ in range(7):
    triangles.append(renderer.Renderer())

client = opc.Client('localhost:7890')
atexit.register(lambda: animations.clear_all(client))

animation_types = [
                   animations.FullFlash,
                   animations.Sparkle,
                   animations.BorderFlash,
                   animations.FillBottomUp,
                   animations.FillTopDown,
                   animations.DrainBottomUp,
                   animations.DrainTopDown,
                   animations.FillMiddleOut,
                   animations.FillOutsideIn,
                   animations.DrainMiddleOut,
                   animations.DrainOutsideIn,
                  ]

def animate():
    leds = []
    for triangle in triangles:
        leds.extend(triangle.render())
        leds.extend([(0,0,0)] * (64 - 25))
        if not triangle.layers:
            colour = random.choice(list(colours.keys()))
            frames = random.randint(5, 12)
            animation = random.choice(animation_types)
            triangle.add_layer(animation(colour=colour, frames=frames))

    client.put_pixels(leds) 
    threading.Timer(2/3, animate).start()

animate()
