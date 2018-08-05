from collections import namedtuple
import animations

def vel_scale(vel):
    return min(1, 2 * vel / (127/1.5))

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
                if self.persisted_layers[name].get(i, False):
                    self.persisted_layers[name][i].value.reset_frames(animation.kwargs['bright_level'])
                else:
                    self.persisted_layers[name][i] = triangles[i].add_layer(instance)
            else:
                triangles[i].add_layer(instance)


Layer = namedtuple('Layer', ['animation', 'kwargs', 'triangles'])

europe = Programme({
    'juno': Layer(animations.FullFlash, {'colour': "blue", 'frames': 120, 'persistent': True}, [0]),
    'mini': Layer(animations.DrainBottomUp, {'colour': "light-blue", 'frames': 40}, [1, 3]),
    'kick': Layer(animations.DrainTopDown, {'colour': "white", 'frames': 7}, [2]),
    'snare': Layer(animations.DrainBottomUp, {'colour': "off-white", 'frames': 7}, [2]),
    '202': Layer(animations.Sparkle, {'colour': "mint", 'frames': 10}, [4]),
    'blip': Layer(animations.DrainTopDown, {'colour': "blue", 'frames': 10}, [4]),
    'demon': Layer(animations.BorderFlash, {'colour': "red", 'frames': 50}, [0,4]),
    'verb': Layer(animations.Sparkle, {'colour': "violet", 'frames': 5}, [x for x in range(5)]),
})

red_europe = Programme({
    'juno': Layer(animations.FullFlash, {'colour': "red", 'frames': 120}, [0]),
    'mini': Layer(animations.DrainBottomUp, {'colour': "orange", 'frames': 40}, [1, 3]),
    'kick': Layer(animations.DrainTopDown, {'colour': "white", 'frames': 7}, [2]),
    'snare': Layer(animations.DrainBottomUp, {'colour': "off-white", 'frames': 7}, [2]),
    '202': Layer(animations.Sparkle, {'colour': "yellow", 'frames': 10}, [4]),
    'blip': Layer(animations.DrainTopDown, {'colour': "red", 'frames': 10}, [4]),
    'demon': Layer(animations.BorderFlash, {'colour': "blue", 'frames': 50}, [0,4]),
    'verb': Layer(animations.Sparkle, {'colour': "peach", 'frames': 5}, [x for x in range(0,5)]),
})
