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

jellyfish = Programme('jellyfish', {
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
    'volca': Layer(animations.FillMiddleOut, {'colour': 'coral', 'frames': 12, 'padding': 12}, [4]),
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

teenager = Programme('teenager', {
    'kick': Layer(animations.DrainBottomUp, {'colour': 'off-white', 'frames': 5}, [2]),
    'rim': Layer(animations.RowFlash, {'colour': 'pastel-yellow', 'frames': 4, 'row': 4}, [0,2,4]),
    'snare': Layer(animations.RowFlash, {'colour': 'pastel-red', 'frames': 4, 'row': 3}, [0,2,4]),
    'mini': Layer(animations.FullFlash, {'colour': 'red', 'frames': 20}, [0,2,4]),
    '202': Layer(animations.DrainOutsideIn, {'colour': "gold", 'frames': 15, 'density': 4}, [1]),
    'verb': Layer(animations.DrainTopDown, {'colour': "pastel-orange", 'frames': 100, 'persistent': True}, [x for x in range(5)]),
    'goof': Layer(animations.RandomLines, {'colour': 'neon', 'frames': 5}, [x for x in range(5)]),
    'juno': Layer(animations.Sparkle, {'colour': "orange", 'frames': 5, 'density': 4}, [3]),
})

beg = Programme('beg', {
    'filter': Layer(animations.DrainTopDown, {'colour': 'mint', 'frames': 100, 'persistent': True}, [x for x in range(5)]),
    'rhodes': Layer(animations.BorderFlash, {'colour': 'pastel-green', 'frames': 10}, [x for x in range(5)]),
    'kick': Layer(animations.DrainTopDown, {'colour': 'pastel-green', 'frames': 5}, [2]),
    'blip': Layer(animations.DrainOutsideIn, {'colour': 'pastel-green', 'frames': 10}, [0, 4]),
    'grime': Layer(animations.Sparkle, {'colour': 'pastel-blue', 'frames': 10}, [1, 3]),
    '202': ComplexLayer(
        bottom=57, top=73,
        explicit_layers = {
            57: Layer(animations.RowFlash, {'colour': 'pastel-blue', 'frames': 15, 'row': 0}, [0,2,4]),
            64: Layer(animations.RowFlash, {'colour': 'royal-blue', 'frames': 15, 'row': 1}, [0,2,4]),
            66: Layer(animations.RowFlash, {'colour': 'royal-blue', 'frames': 15, 'row': 2}, [0,2,4]),
            68: Layer(animations.RowFlash, {'colour': 'royal-blue', 'frames': 15, 'row': 3}, [0,2,4]),
            85: Layer(animations.RowFlash, {'colour': 'pastel-blue', 'frames': 15, 'row': 4}, [0,2,4]),
        },
        scale_layers = [Layer(animations.RowFlash, {'colour': 'royal-blue', 'frames': 15, 'row': x}, [0,2,4]) for x in range(5)],
    ),
})

waited = Programme('waited', {
    # Drums
    'kick': Layer(animations.BottomFlash, {'colour': 'pastel-blue', 'frames': 5}, [2]),
    'rim': Layer(animations.RowFlash, {'colour': 'off-white', 'frames': 2, 'row': 4}, [1,3]),

    'saw': Layer(animations.DrainBottomUp, {'colour': 'mellow-violet', 'frames': 100, 'persistent': True}, [2]),
    'saw-2': Layer(animations.DrainBottomUp, {'colour': 'peach', 'frames': 100, 'persistent': True}, [2]),
    'pluck': Layer(animations.DrainOutsideIn, {'colour': 'pastel-violet', 'frames': 7}, [4]),
    'pluck-2': Layer(animations.DrainOutsideIn, {'colour': 'pastel-yellow', 'frames': 7}, [4]),
    'signal': Layer(animations.DrainTopDown, {'colour': 'pastel-red', 'frames': 15}, [0]),
    '202': Layer(animations.Sparkle, {'colour': 'coral', 'frames': 5, 'padding': 20}, [x for x in range(5)]),
    'mini': Layer(animations.BorderFlash, {'colour': 'pastel-orange', 'frames': 10}, [1,3]),
    'verb': Layer(animations.RandomLines, {'colour': 'off-white', 'frames': 5}, [x for x in range(5)]),
    'dusty': Layer(animations.DrainOutsideIn, {'colour': 'pastel-red', 'frames': 100, 'persistent': True}, [1]),
})

moog_layers = []
for x in range(5):
    for y in range(5):
        moog_layers.append(
            Layer(animations.RowFlash, {'colour': 'orange', 'frames': 7, 'row': y}, [x])
        )

blinds = Programme('blinds', {
    # Drums
    'kick': Layer(animations.DrainOutsideIn, {'colour': 'pastel-yellow', 'frames': 5}, [2]),
    'pole': Layer(animations.DrainMiddleOut, {'colour': 'pastel-orange', 'frames': 5}, [0,4]),

    'pads': Layer(animations.DrainOutsideIn, {'colour': 'magenta', 'frames': 100, 'persistent': True}, [1]),
    'scout': Layer(animations.DrainOutsideIn, {'colour': 'reddish', 'frames': 100, 'persistent': True}, [4]),
    'pluck': Layer(animations.DrainTopDown, {'colour': 'gold', 'frames': 7}, [3]),
    'moog': ComplexLayer(
        bottom=27, top=70,
        explicit_layers = {
            21: Layer(animations.BorderFlash, {'colour': "red", 'frames': 5}, [0,4]),
            22: Layer(animations.BorderFlash, {'colour': "reddish", 'frames': 5}, [1,3]),
            23: Layer(animations.BorderFlash, {'colour': "reddish", 'frames': 5}, [1,3]),
            24: Layer(animations.BorderFlash, {'colour': "coral", 'frames': 5}, [2]),
            25: Layer(animations.BorderFlash, {'colour': "pastel-red", 'frames': 5}, [2]),
        },
        scale_layers = moog_layers
    )    
})

hoodie = Programme('hoodie', {
    # Juno
    'juno-a': Layer(animations.FullFlash, {'colour': 'teal', 'frames': 15}, [1,3]),
    'juno-b': ComplexLayer(
        bottom=53, top=81,
        scale_layers = [
            Layer(animations.RowFlash, {'colour': 'teal', 'frames': 10, 'row': x}, [1,3]) for x in range(5)
        ]
    ),
    'juno-c': ComplexLayer(
        bottom=60, top=84,
        scale_layers = [
            Layer(animations.FullFlash, {'colour': 'royal-blue', 'frames': 15}, [1,3]),
            Layer(animations.FullFlash, {'colour': 'cyan', 'frames': 15}, [1,3]),
            Layer(animations.FullFlash, {'colour': 'teal', 'frames': 15}, [1,3]),
            Layer(animations.FullFlash, {'colour': 'pastel-blue', 'frames': 15}, [1,3]),
            Layer(animations.FullFlash, {'colour': 'white', 'frames': 15}, [1,3]),
        ]
    ),

    'bass': ComplexLayer(
        bottom=48, top=65,
        scale_layers = [
            Layer(animations.RowFlash, {'colour': "off-white", 'frames': 3, 'row': x}, [0,2,4]) for x in range(3)
        ],
        explicit_layers = {
            69: Layer(animations.RowFlash, {'colour': "off-white", 'frames': 3, 'row': 3}, [0,2,4])
        }
    ),

    'mini': Layer(animations.TopFlash, {'colour': 'white', 'frames': 100, 'persistent': True}, [x for x in range(5)]),

    'section': ComplexLayer(
        explicit_layers = {
            # A section
            60: Layer(animations.FillMiddleOut, {'colour': 'pastel-blue', 'frames': 55, 'padding': 55}, [0,2,4]),
            61: Layer(animations.FillOutsideIn, {'colour': 'pastel-violet', 'frames': 55, 'padding': 55}, [0,2,4]),
            62: Layer(animations.FillMiddleOut, {'colour': 'cyan', 'frames': 55, 'padding': 55}, [0,2,4]),
            63: Layer(animations.FillOutsideIn, {'colour': 'indigo', 'frames': 55, 'padding': 55}, [0,2,4]),
            # B Section
            72: Layer(animations.FillTopDown, {'colour': 'pastel-yellow', 'frames': 20, 'padding': 20}, [0,2,4]),
            73: Layer(animations.FillBottomUp, {'colour': 'pastel-green', 'frames': 20, 'padding': 20}, [0,2,4]),
            74: Layer(animations.FillTopDown, {'colour': 'mellow-yellow', 'frames': 20, 'padding': 20}, [0,2,4]),
            75: Layer(animations.FillBottomUp, {'colour': 'mint', 'frames': 20, 'padding': 20}, [0,2,4]),

            # C Section
            84: Layer(animations.FillBottomUp, {'colour': 'royal-blue', 'frames': 45, 'padding': 45}, [0,2,4]),
            85: Layer(animations.FillTopDown, {'colour': 'violet', 'frames': 45, 'padding': 45}, [0,2,4]),
            86: Layer(animations.FillMiddleOut, {'colour': 'indigo', 'frames': 45, 'padding': 45}, [0,2,4]),
            87: Layer(animations.FillOutsideIn, {'colour': 'magenta', 'frames': 45, 'padding': 45}, [0,2,4]),

        }
    ), 
})
