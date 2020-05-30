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

    def view(self):
        with mss() as screen_capture:
            while cv2.waitKey(10) != 27:
                # Grab the pixels in the box (in full colour)
                image = np.array(screen_capture.grab(self.image_box))
                # Show the captured area.
                cv2.imshow('Captured area', image)

if __name__ == '__main__':
    AutoDino({ 'top': 0, 'left': 0, 'width': 1000, 'height': 500 }).view()
