#!/usr/bin/env python

# Burn-in test: Keep LEDs at full brightness most of the time, but dim periodically
# so it's clear when there's a problem.

import opc, time, math

numLEDs = 25
client = opc.Client('localhost:7890')

while True:
    client.put_pixels([(0, 0, 0)] * numLEDs)
