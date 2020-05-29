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
