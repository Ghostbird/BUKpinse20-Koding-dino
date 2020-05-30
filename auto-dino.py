#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Created on Sun May 24 10:37:22 2020

@author: Gijsbert ter Horst
'''
from time import sleep
import numpy as np
import cv2
from pynput.keyboard import Key, Controller, Events
from sys import platform

if platform == 'linux' or platform == 'linux2':
    # GNU/Linux
    from mss.linux import MSS as mss
elif platform == 'darwin':
    # MacOS X
    from mss.darwin import MSS as mss
elif platform == 'win32':
    # Microsoft Windows
    from mss.windows import MSS as mss
else:
    print(f'Unsupported platform {platform}')

class AutoDino:
    def __init__(self, image_box):
        # Definition of the part of the screen where we capture the image.
        self.image_box = image_box
        # Initialise a keyboard
        self.keyboard = Controller()

    def view(self):
        with mss() as screen_capture:
            while cv2.waitKey(10) != 27:
                # Grab the pixels in the box (in full colour)
                image = np.array(screen_capture.grab(self.image_box))
                # Show the captured area.
                cv2.imshow('Captured area', image)

    def start(self):
        print('Click the dino-game window!')
        sleep(1)
        print('3')
        sleep(1)
        print('2')
        sleep(1)
        print('1')
        sleep(1)
        print('START!')
        # F5 to reload page
        self.keyboard.press(Key.f5)
        self.keyboard.release(Key.f5)
        # Wait briefly for page reload
        sleep(0.1)
        # Press space to start the game
        self.keyboard.press(Key.space)
        self.keyboard.release(Key.space)

if __name__ == '__main__':
    dino = AutoDino({ 'top': 630, 'left':350, 'width': 100, 'height': 5 })
    dino.start()
    dino.view()
