from llist import dllist
import opc

class Renderer:

    def __init__(self):
        self.layers = dllist()

    def add_layer(self, layer):
        return self.layers.append(layer)

    def clear_layers(self):
        self.layers.clear()

    def blend_layers(self, frame_layers):
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

    def blend_layers_additive(self, frame_layers):
        final_leds = []
        for i in range(25):
            final_leds.append([0,0,0])
        
        for frame in frame_layers:
            for i in range(len(frame.leds)):
                for j in range(3):
                    final_leds[i][j] = min(final_leds[i][j] + frame.leds[i][j], 255)

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

        leds = self.blend_layers_additive(frame_layers)

        return leds
