#!env/bin/python3.5

import argparse, atexit
import animations, renderer, opc

triangles = []
for _ in range(5):
    triangles.append(renderer.Renderer())

client = opc.Client('localhost:7890')

def main():

    atexit.register(lambda: animations.clear(client))

    parser = argparse.ArgumentParser(description='Light All Triangles with colour from colour store')
    parser.add_argument('colour', type=str,
                        help='Colour to test')

    args = parser.parse_args()

    leds = []
    for triangle in triangles:
        triangle.add_layer(animations.FullFlash(colour=args.colour, frames=60))
        leds.extend(triangle.render())
        leds.extend([(0,0,0)] * (64 - 25))

    print("Testing Colour '{}'. Exit program to turn off triangles".format(args.colour))
    while True:
        client.put_pixels(leds) 

main()
