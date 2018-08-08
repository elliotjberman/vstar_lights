from collections import namedtuple

def vel_scale(vel):
    return min(1, (vel ** 2.1) / (127**2))

class Programme:

    def __init__(self, triggers):
        self.triggers = triggers
        self.persisted_layers = {}
        for key, animation in self.triggers.items():
            if 'persistent' in animation.kwargs:
                self.persisted_layers[key] = {}

    def read_message(self, trigger_message):
        note = trigger_message['name'][0]
        name = trigger_message['name'][0]
        vel = max(0, int(trigger_message['velocity'][0]))
        return note, name, vel

    def handle_message(self, trigger_message, triangles):
        note, name, vel = self.read_message(trigger_message)

        animation = self.triggers[name]
        animation.kwargs['bright_level'] = vel_scale(vel)
        for i in animation.triangles:
            instance = animation.animation(**animation.kwargs)
            if 'persistent' in animation.kwargs:
                if self.persisted_layers[name].get(i, False) and not self.persisted_layers[name][i]:
                    self.persisted_layers[name][i].value.reset_frames(animation.kwargs['bright_level'])
                else:
                    self.persisted_layers[name][i] = triangles[i].add_layer(instance)
            else:
                triangles[i].add_layer(instance)


Layer = namedtuple('Layer', ['animation', 'kwargs', 'triangles'])
