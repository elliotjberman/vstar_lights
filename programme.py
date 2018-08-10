import math
from collections import namedtuple

def vel_scale(vel):
    k = 0.1
    c = math.exp(k*127/2)

    result = 1/(1+c/math.exp(k*vel))
    return result

def scale_to_x(x, value, bottom, top):
    if value < bottom or value > top:
        return -1

    return int((value-bottom) / (top-bottom-1) * x)



class Programme:

    def __init__(self, triggers):
        self.triggers = triggers
        self.persisted_layers = {}
        for key, animation in self.triggers.items():
            if 'persistent' in animation.kwargs:
                self.persisted_layers[key] = {}

    def read_message(self, trigger_message):
        note = int(trigger_message['note'][0])
        name = trigger_message['name'][0]
        vel = max(0, int(trigger_message['velocity'][0]))
        return note, name, vel

    def handle_message(self, trigger_message, triangles):
        note, name, vel = self.read_message(trigger_message)

        animation = self.triggers[name]
        animation.kwargs['bright_level'] = vel_scale(vel)
        animation.kwargs['note'] = note
        for i in animation.triangles:
            instance = animation.animation(**animation.kwargs)
            if 'persistent' in animation.kwargs:
                if self.persisted_layers[name].get(i):
                    self.persisted_layers[name][i].value.reset_frames(animation.kwargs['bright_level'])
                else:
                    self.persisted_layers[name][i] = triangles[i].add_layer(instance)
            else:
                triangles[i].add_layer(instance)


Layer = namedtuple('Layer', ['animation', 'kwargs', 'triangles'])

class ComplexLayer:

    def __init__(self, bottom=0, top=0, scale_layers=None, explicit_layers=None):
        self.bottom = bottom
        self.top = top
        self.scale_layers = scale_layers or []
        self.explicit_layers = explicit_layers or {}

    def read_note(self, note):
        if note in self.explicit_layers:
            return explicit_layers[note]
        scaled_note = scale_to_x(len(self.scale_layers),note, self.top, self.bottom)
        return self.scale_layers[scaled_note]

