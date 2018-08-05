# vstar_lights
LED lighting program receiving events from Max for Live

## Requirements
- Python 3
- https://www.adafruit.com/product/1689
- LED strips arranged in triangles

## Installation
`pip install -r requirements.txt`

## Run it

For random colours, random animations, and animation times randomly selected from range:
`python3 slow_fades.py`

For server to take messages from M4L:
`python3 main.py`

To test new programmes:
`python3 test_programme.py`

```usage: test_programme.py [-h] [-c [COLOUR]] [-p [PROGRAMME]] [-f]

Light All Triangles with colour from colour store

optional arguments:
  -h, --help            show this help message and exit
  -c [COLOUR], --colour [COLOUR]
                        Colour to test
  -p [PROGRAMME], --programme [PROGRAMME]
                        Programme to test
  -f, --freeze          Freeze first frame of animation (good for checking
                        colours)
```
