#!env/bin/python3.5

import atexit, time
import animations, renderer, opc

client = opc.Client('localhost:7890')

atexit.register(lambda: animations.clear_all(client))

while True:
    leds = []
    for i in range(5):
        print("Triangle Index " + str(i))
        leds.extend([(255, 255, 255)] * 64)
        client.put_pixels(leds)
        time.sleep(0.5)

    print("All off")
    client.put_pixels([(0,0,0)] * 64 * 5)
    time.sleep(0.5)
