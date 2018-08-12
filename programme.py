import math
from collections import namedtuple


# Helper functions

def vel_scale(vel):
    k = 0.1
    c = math.exp(k*127/2)

    result = 1/(1+c/math.exp(k*vel))
    return result

def scale_to_x(x, value, bottom, top):
    if value < bottom or value > top:
        return -1

    return min(x-1, int((value-bottom) / (top-bottom-1) * x))

# Classes

Layer = namedtuple('Layer', ['animation', 'kwargs', 'triangles'])

class ComplexLayer:

    def __init__(self, bottom=0, top=0, scale_layers=None, explicit_layers=None):
        self.bottom = bottom
        self.top = top
        self.scale_layers = scale_layers or []
        self.explicit_layers = explicit_layers or {}

    def read_note(self, note):
        if note in self.explicit_layers:
            return self.explicit_layers[note]

        scaled_note = scale_to_x(len(self.scale_layers), note, self.bottom, self.top)
        if scaled_note == -1:
            return None
        return self.scale_layers[scaled_note]

class Programme:

    def __init__(self, name, triggers):
        self.name = name
        self.triggers = triggers
        self.persisted_layers = {}
        for key, layer in self.triggers.items():
            if not isinstance(layer, ComplexLayer):
                if 'persistent' in layer.kwargs:
                    self.persisted_layers[key] = {}

    def read_message(self, trigger_message):
        note = int(trigger_message['note'][0])
        name = trigger_message['name'][0]
        vel = max(0, int(trigger_message['velocity'][0]))
        return note, name, vel

    def handle_message(self, trigger_message, triangles):
        note, name, vel = self.read_message(trigger_message)

        layer = self.triggers[name]
        if isinstance(layer, ComplexLayer):
            layer = layer.read_note(note)
        if not layer: return

        layer.kwargs['brightness'] = vel_scale(vel)
        for i in layer.triangles:
            instance = layer.animation(**layer.kwargs)
            if 'persistent' in layer.kwargs:
                if self.persisted_layers[name].get(i):
                    self.persisted_layers[name][i].value.reset_frames(layer.kwargs['brightness'])
                else:
                    self.persisted_layers[name][i] = triangles[i].add_layer(instance)
            else:
                triangles[i].add_layer(instance)
