#!env/bin/python3.5

import argparse, atexit, threading
import animations, renderer, opc

triangles = []
for _ in range(5):
    triangles.append(renderer.Renderer())

client = opc.Client('localhost:7890')
parser = argparse.ArgumentParser(description='Light All Triangles with colour from colour store')

def main():
    atexit.register(lambda: animations.clear_all(client))

    parser.add_argument('-c', '--colour', type=str, default='white', nargs='?',
                        help='Colour to test')
    parser.add_argument('-p', '--programme', type=str, default='FullFlash', nargs='?',
                        help='Programme to test')
    parser.add_argument('-f', '--freeze', action='store_true',
                        help='Freeze first frame of animation (good for checking colours)')
    parser.set_defaults(freeze=False)

    args = parser.parse_args()
    print("Testing Colour '{}' with Programme '{}'. Exit program to turn off triangles".format(args.colour, args.programme))
    animate_with_args(args)

def animate_with_args(args):
    leds = []
    for triangle in triangles:
        if not triangle.layers:
            animation = getattr(animations, args.programme)
            triangle.add_layer(animation(colour=args.colour, frames=60))
        leds.extend(triangle.render())
        leds.extend([(0,0,0)] * (64 - 25))

    client.put_pixels(leds) 
    while args.freeze:
        client.put_pixels(leds) 
    threading.Timer(1/60, lambda: animate_with_args(args)).start()

main()
