from llist import dllist
import opc
import sys

class Renderer:

    def __init__(self, client_address='localhost:7890'):
        self.client = opc.Client(client_address)
        self.layers = dllist()

    def add_layer(self, layer):
        self.layers.append(layer)

    def blend_layers(self, frame_layers):
        # Mutability will save space over creating a new tuple per layer
        final_leds = []
        for i in range(25):
            final_leds.append([0,0,0])

        total = 0
        for frame in frame_layers:
            total += frame.opacity

            
        if not total: return final_leds

        
        for frame in frame_layers:
            for i in range(len(frame.leds)):
                for j in range(3):
                    final_leds[i][j] += int(frame.leds[i][j] * frame.opacity/total)

        return final_leds


    def render(self):
        frame_layers = []

        node = self.layers.first
        while node:
            layer = node.value
            frame_layers.append(layer.animate())
            
            next_node = node.next
            if layer.finished():
                self.layers.remove(node)
            node = next_node

        leds = self.blend_layers(frame_layers)

        self.client.put_pixels(leds)
