#!env/bin/python3.5

import socket, time, atexit
import opc, animations, renderer
import keyboard


triangle_1 = renderer.Renderer()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 2346))

print("Starting animation loop")
while True:
    message, address = server_socket.recvfrom(1024)
    print(message)
    if keyboard.is_pressed('space'):
        triangle = animations.FullFlash(colour="peach", frames=60)
        triangle_1.add_layer(triangle)
        
    if keyboard.is_pressed('enter'):
        triangle = animations.FullFlash(colour="mint", frames=10)
        triangle_1.add_layer(triangle)

    triangle_1.render()
    triangle_2.render()

    time.sleep(1/60) # 60 FPS
