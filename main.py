#!env/bin/python3.5

import opc, time, atexit
import animations, renderer
import keyboard


renderboy = renderer.Renderer()

print("Starting animation loop")
while True:
    if keyboard.is_pressed('space'):
        triangle = animations.FullFlash(colour="peach", frames=60)
        renderboy.add_layer(triangle)
        
    if keyboard.is_pressed('enter'):
        triangle = animations.FullFlash(colour="mint", frames=10)
        renderboy.add_layer(triangle)

    
    renderboy.render()

    time.sleep(1/60) # 60 FPS
