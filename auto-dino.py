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
                # Discard unneeded colour information, makes calculations faster
                image_grey = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
                # Calculate edges
                image_laplacian = cv2.Laplacian(image_grey, cv2.CV_64F)
                # Show the captured area laplacian.
                cv2.imshow('Captured area', image_laplacian)

    def run(self):
        self.start()
        # Wait one second for the zoom effect to end
        sleep(1)
        with mss() as screen_capture:
            while True:
                # Grab the pixels in the box (in full colour)
                image = np.array(screen_capture.grab(self.image_box))
                # Discard unneeded colour information, makes calculations faster
                image_grey = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
                # Calculate difference in image
                value = self.difference(image_grey)
                if value > 0:
                    self.jump()

    def jump(self):
        self.keyboard.release(Key.down)
        self.keyboard.press(Key.space)
        sleep(0.3)
        self.keyboard.release(Key.space)
        self.keyboard.press(Key.down)

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
    
    def difference(self, image_grey):
        # Calculate Laplacian
        image_laplacian = cv2.Laplacian(image_grey, cv2.CV_64F)
        # Get the nonzero values of the laplacian.
        non_zero = image_laplacian.nonzero()
        # Count the nonzero values of the laplacian in both dimensions
        return len(non_zero[0]) + len(non_zero[1])

if __name__ == '__main__':
    AutoDino({ 'top': 635, 'left':360, 'width': 100, 'height': 5 }).run()
