import animations
from programme import Programme, Layer

test = Programme({
    'kick': Layer(animations.FullFlash, {'colour': "blue", 'frames': 5}, [x for x in range(5)]),
    'snare': Layer(animations.FullFlash, {'colour': "orange", 'frames': 5}, [x for x in range(5)]),
    'verb': Layer(animations.Sparkle, {'colour': "blue", 'frames': 5, 'persistent': True}, [x for x in range(5)]),
})

europe = Programme({
    'juno': Layer(animations.FullFlash, {'colour': "royal-blue", 'frames': 120, 'persistent': True}, [0]),
    'mini': Layer(animations.DrainBottomUp, {'colour': "light-blue", 'frames': 40}, [1, 3]),
    'kick': Layer(animations.DrainTopDown, {'colour': "white", 'frames': 7}, [2]),
    'snare': Layer(animations.DrainBottomUp, {'colour': "off-white", 'frames': 7}, [2]),
    '202': Layer(animations.Sparkle, {'colour': "mint", 'frames': 10}, [4]),
    'blip': Layer(animations.DrainTopDown, {'colour': "violet", 'frames': 10}, [4]),
    'demon': Layer(animations.BorderFlash, {'colour': "red", 'frames': 50}, [0,4]),
    'verb': Layer(animations.Sparkle, {'colour': "blue", 'frames': 5}, [x for x in range(5)]),
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

late_ambient = Programme({
    '202': Layer(animations.BorderFlash, {'colour': "orange", 'frames': 30}, [0, 4]),
    'mini': Layer(animations.DrainTopDown, {'colour': "yellow", 'frames': 10, 'persistent': True}, [1,2,3]),
})
