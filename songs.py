import animations
import random
from programme import Programme, Layer, ComplexLayer

test = Programme('test', {
    'kick': Layer(animations.BottomFlash, {'colour': "off-white", 'frames': 10}, [2]),
    'snare': Layer(animations.DrainBottomUp, {'colour': "yellow", 'frames': 10}, [1]),
    'weird': Layer(animations.DrainMiddleOut, {'colour': "orange", 'frames': 40}, [3]),
    'verb': Layer(animations.Sparkle, {'colour': "orange", 'frames': 2, 'persistent': True}, [x for x in range(5)]),
    'mini': Layer(animations.BorderFlash, {'colour': "red", 'frames': 3000, 'persistent': True}, [4]),
    'juno': Layer(animations.DrainOutsideIn, {'colour': "peach", 'frames': 3000, 'persistent': True}, [2]),
    'moog': Layer(animations.BorderFlash, {'colour': "magenta", 'frames': 60, }, [0]),
})

europe = Programme('europe', {
    'juno': Layer(animations.FullFlash, {'colour': "pastel-violet", 'frames': 60, 'persistent': True}, [0]),
    'mini': Layer(animations.DrainBottomUp, {'colour': "light-blue", 'frames': 30}, [1, 3]),
    'kick': Layer(animations.RowFlash, {'colour': "off-white", 'frames': 3, 'row': 0}, [0,2,4]),
    'snare': Layer(animations.DrainOutsideIn, {'colour': "pastel-blue", 'frames': 4}, [2]),
    '202': Layer(animations.Sparkle, {'colour': "mint", 'frames': 5, 'density': 4}, [4]),
    'blip': Layer(animations.DrainTopDown, {'colour': "mint", 'frames': 10}, [4]),
    'demon': Layer(animations.BorderFlash, {'colour': "red", 'frames': 25}, [0,4]),
    'demon-blue': Layer(animations.BorderFlash, {'colour': "blue", 'frames': 25}, [0,4]),
    'verb': Layer(animations.Sparkle, {'colour': "pastel-green", 'frames': 3, 'density': 2}, [x for x in range(5)]),
    'mini-c': ComplexLayer(
        bottom=64, top=82,
        scale_layers = [Layer(animations.RowFlash, {'colour': 'yellow', 'frames': 15, 'row': x}, [1,3]) for x in range(5)],
    )
})

late_ambient = Programme('late_ambient', {
    '202': Layer(animations.BorderFlash, {'colour': "orange", 'frames': 30}, [0, 4]),
    'mini': Layer(animations.DrainTopDown, {'colour': "yellow", 'frames': 10, 'persistent': True}, [1,2,3]),
})

plain = Programme('plain', {
    'jsample': Layer(animations.DrainOutsideIn, {'colour': 'yellow', 'frames': 30}, [2]),
    'crash': Layer(animations.DrainMiddleOut, {'colour': 'lime', 'frames': 60}, [0,4]),
    'verb': Layer(animations.DrainMiddleOut, {'colour': 'lime', 'frames': 40, 'persistent': True}, [0,1,3,4]),
    'mini': Layer(animations.FullFlash, {'colour': 'neon', 'frames': 40, 'persistent': True}, [1,3]),
    'windy': Layer(animations.RandomLines, {'colour': 'royal-blue', 'frames': 5}, [x for x in range(5)]),
    'boards': Layer(animations.DrainOutsideIn, {'colour': 'off-white', 'frames': 100, 'persistent': True}, [2]),
    'section': ComplexLayer(
        explicit_layers = {
            # A section
            60: Layer(animations.FillMiddleOut, {'colour': 'pastel-blue', 'frames': 120, 'padding': 120}, [0,2,4]),
            61: Layer(animations.FillOutsideIn, {'colour': 'royal-blue', 'frames': 120, 'padding': 120}, [0,2,4]),
            # C Section
            72: Layer(animations.FillTopDown, {'colour': 'pastel-green', 'frames': 30, 'padding': 30}, [0,2,4]),
            73: Layer(animations.FillBottomUp, {'colour': 'pastel-green', 'frames': 30, 'padding': 30}, [0,2,4]),
            74: Layer(animations.FillMiddleOut, {'colour': 'pastel-blue', 'frames': 30, 'padding': 30}, [0,2,4]),
            75: Layer(animations.FillOutsideIn, {'colour': 'pastel-blue', 'frames': 30, 'padding': 30}, [0,2,4]),
        }
    ), 
    'swipe': Layer(animations.DrainBottomUp, {'colour': 'white', 'frames': 8}, [0,4]),
})

octopus = Programme('octopus', {
    '202': ComplexLayer(
        bottom=28, top=60,
        explicit_layers = {
            28: Layer(animations.RowFlash, {'colour': "red", 'frames': 15, 'row': 0}, [1,3]),
            57: Layer(animations.RowFlash, {'colour': "red", 'frames': 15, 'row': 4}, [1,3]),
        },
        scale_layers = [Layer(animations.RowFlash, {'colour': 'red', 'frames': 15, 'row': x}, [1,3]) for x in range(1, 4)],
    ),
    'moog': Layer(animations.FillMiddleOut, {'colour': 'gold', 'frames': 5}, [4]),
    'drums': ComplexLayer(
        explicit_layers = {
            36: Layer(animations.BottomFlash, {'colour': "white", 'frames': 5}, [2]),
            38: Layer(animations.TopFlash, {'colour': "pastel-red", 'frames': 5}, [2]),
            39: Layer(animations.TopFlash, {'colour': "pastel-red", 'frames': 5}, [2]),
            49: Layer(animations.BorderFlash, {'colour': "coral", 'frames': 5}, [0,4]),
        } 
    ),
    'mini': Layer(animations.RandomLines, {'colour': 'mint', 'frames': 5}, [x for x in range(5)]),
})
