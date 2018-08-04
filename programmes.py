from collections import namedtuple
import animations

class Programme:

    def __init__(self, triggers):
        self.triggers = triggers

    def handle_message(self, trigger_message, triangles):
        animation = self.triggers[trigger_message['name'][0]]
        instance = animation.animation(**animation.kwargs)
        for i in animation.triangles:
            triangles[i].add_layer(instance)

Layer = namedtuple('Layer', ['animation', 'kwargs', 'triangles'])

europe = Programme({
    'juno': Layer(animations.FullFlash, {'colour': "blue", 'frames': 40}, [0]),
    'mini': Layer(animations.DrainBottomUp, {'colour': "light-blue", 'frames': 40}, [1, 3]),
    'kick': Layer(animations.DrainTopDown, {'colour': "white", 'frames': 7}, [2]),
    'snare': Layer(animations.Sparkle, {'colour': "off-white", 'frames': 7}, [2]),
    '202': Layer(animations.Sparkle, {'colour': "mint", 'frames': 20}, [4]),
    'blip': Layer(animations.DrainTopDown, {'colour': "blue", 'frames': 10}, [4]),
    'demon': Layer(animations.BorderFlash, {'colour': "red", 'frames': 200}, [0,4]),
    'verb': Layer(animations.Sparkle, {'colour': "violet", 'frames': 5}, [x for x in range(5)]),
})

red_europe = Programme({
    'juno': Layer(animations.FullFlash, {'colour': "red", 'frames': 40}, [0]),
    'mini': Layer(animations.DrainBottomUp, {'colour': "orange", 'frames': 40}, [1, 3]),
    'kick': Layer(animations.DrainTopDown, {'colour': "white", 'frames': 7}, [2]),
    'snare': Layer(animations.Sparkle, {'colour': "off-white", 'frames': 7}, [2]),
    '202': Layer(animations.Sparkle, {'colour': "yellow", 'frames': 20}, [4]),
    'blip': Layer(animations.DrainTopDown, {'colour': "red", 'frames': 10}, [4]),
    'demon': Layer(animations.BorderFlash, {'colour': "blue", 'frames': 200}, [0,4]),
    'verb': Layer(animations.Sparkle, {'colour': "peach", 'frames': 5}, [x for x in range(0,5)]),
})
