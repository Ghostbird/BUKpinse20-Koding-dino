# Auto Dino Python image processing tutorial

In this tutorial you're going to learn basic image processing using Python and OpenCV. You're going to learn how to capture part of you computer screen and count the total brightness of that image where a black pixel has a value of 0 and a white pixel has a value of 255. Thus the pixel score of a 10×10 pixel square will be 25500 if it is white, 0 if it is black, and 12750 if it is grey. However it will also have a value of 12750 if it contains an equal amount of black and white pixels. As you can see this is a _very_ basic form of image processing.

## Prerequisites

- Install the [most recent Python](https://www.python.org/downloads/release)
- Install these packages: `pynput` `cv2` `numpy` and `mss`
  - Windows: `python -m pip install pynput cv2 numpy mss`
  - MacOS: `pip install pynput cv2 numpy mss`
  - Linux: I expect you to be able to find out how to install these packages on your distro. If you really don't know, start with `sudo pip3 install pynput cv2 numpy mss` which is likely to work, and unlikely to mess up anything if it fails.
- Run the dino game either in:
  - [Google Chrome](https://chrome.google.com)
  - Chromium (not recommended on Windows / MacOS)
  - In any browser from [this download](https://github.com/wayou/t-rex-runner)

### Verification

Download [the starting code](https://github.com/Ghostbird/BUKpinse20-Koding-dino/archive/0-prerequisites.zip), run auto-dino.py and verify that it prints no errors.
