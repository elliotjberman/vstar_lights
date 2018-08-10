import animations
import random
from programme import Programme, Layer

test = Programme({
    'kick': Layer(animations.BottomFlash, {'colour': "off-white", 'frames': 10}, [2]),
    'snare': Layer(animations.DrainBottomUp, {'colour': "yellow", 'frames': 10}, [1]),
    'weird': Layer(animations.DrainMiddleOut, {'colour': "orange", 'frames': 40}, [3]),
    'verb': Layer(animations.Sparkle, {'colour': "orange", 'frames': 2, 'persistent': True}, [x for x in range(5)]),
    'mini': Layer(animations.BorderFlash, {'colour': "red", 'frames': 3000, 'persistent': True}, [4]),
    'juno': Layer(animations.DrainOutsideIn, {'colour': "peach", 'frames': 3000, 'persistent': True}, [2]),
    'moog': Layer(animations.BorderFlash, {'colour': "magenta", 'frames': 60, }, [0]),
})

europe = Programme({
    'juno': Layer(animations.FullFlash, {'colour': "royal-blue", 'frames': 60, 'persistent': True}, [0]),
    'mini': Layer(animations.DrainBottomUp, {'colour': "light-blue", 'frames': 30}, [1, 3]),
    'kick': Layer(animations.BottomFlash, {'colour': "white", 'frames': 3}, [2]),
    'snare': Layer(animations.TopFlash, {'colour': "off-white", 'frames': 3}, [2]),
    '202': Layer(animations.Sparkle, {'colour': "mint", 'frames': 5}, [4]),
    'blip': Layer(animations.DrainTopDown, {'colour': "violet", 'frames': 10}, [4]),
    'demon': Layer(animations.BorderFlash, {'colour': "red", 'frames': 25}, [0,4]),
    'verb': Layer(animations.Sparkle, {'colour': "blue", 'frames': 5, 'density': 2}, [x for x in range(5)]),
})

late_ambient = Programme({
    '202': Layer(animations.BorderFlash, {'colour': "orange", 'frames': 30}, [0, 4]),
    'mini': Layer(animations.DrainTopDown, {'colour': "yellow", 'frames': 10, 'persistent': True}, [1,2,3]),
})

plain = Programme({
    'jsample': Layer(animations.DrainOutsideIn, {'colour': 'yellow', 'frames': 60}, [2]),
    'crash': Layer(animations.DrainMiddleOut, {'colour': 'lime', 'frames': 60}, [0,4]),
    'verb': Layer(animations.DrainMiddleOut, {'colour': 'lime', 'frames': 40, 'persistent': True}, [0,1,3,4]),
    'mini': Layer(animations.FullFlash, {'colour': 'neon', 'frames': 40, 'persistent': True}, [1,3]),
    'windy': Layer(animations.RandomLines, {'colour': 'royal-blue', 'frames': 5}, [x for x in range(5)]),
    'boards': Layer(animations.DrainOutsideIn, {'colour': 'off-white', 'frames': 100, 'persistent': True}, [2]),
    'a-section': Layer(animations.Sparkle, {'colour': 'pastel-blue', 'frames': 240, 'density': 25}, [0,2,4]),
    'swipe': Layer(animations.DrainBottomUp, {'colour': 'white', 'frames': 10}, [0,4]),
})


