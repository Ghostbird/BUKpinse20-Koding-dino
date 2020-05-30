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

## Screen capture

First of all you'll capture a part of the screen to run the calculations on. In general, you only want to capture a small part of the screen. This makes it easier on your computer, as it won't have to run calculations on so many pixels. To find the right place on the screen, you'll start by capturing a larger area, so you can recognise the image, and then you'll move it and scale it down, to be just right.

To do this, append this code to the end of `auto-dino.py`:

```python3
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


```

Remember that in Python the indent at the start of the line is significant. You see two top-level blocks in this piece of code. One starts at `class AutoDino`, the other at `if __name__`….

### Class

The first block is a class definition. The concept of classes is used in my programming languages. You can view a class as the mould for a LEGO brick, the metal form that hot plastic is pushed into, to make a single brick. This form, determines a few properties about the brick, that are the same for every brick. However, it might say that a brick has _a colour_, yet the actual colour is determined for each individual brick, by the plastic used to make it.

### Instance

In this case you can see that the `AutoDino` class has a defined (`def`) _method_. `def __init__(self, image_box)`. This is a standard method in Python that a class must have. In the LEGO brick analogy this is the actual process of injecting the mould with plastic. Here, you inject the `AutoDino` class with an `image_box`. The `self` is necessary too, as it represents the _instance_ you've just made. Therefore you run `self.image_box = image_box`. This says: I know this class has an `image_rect`. Now make the value of _this_* instance of AutoDino's `image_box` equal to the injected `image_box` value.

It is like saying: If you use this mould to create a new LEGO brick, the colour of that specific brick will be the colour of the plastic pushed into the mould.

In short, you have an `AutoDino` class, that can be used to create any desired number of `AutoDino` _instances_, each with their own value for `image_box`

*) While Python uses the word `self`, many other languages use the word `this` instead, which in this case would show this more clearly.

### Main

Now look at the bottom block of the code. This starts with the statement `if __name__ == '__main__':`. This is the Python way of saying: If this piece of code was started directly as the main program. If you were to load this code as part of a bigger program, you can use the `AutoDino` class in that program, and the code in the if is not used. That way the bigger program can choose to use the `AutoDino` in new ways.

The last line of the program states that create an instance of the `AutoDino` class, insert something that has a `top`, `left`,`height` and `width`. This is the image box. It is defined as the position of the top left corner of the box on your screen. The top value is the value between the top of the screen and the top of the rectangle. Similarly the left value is between the left side of the screen and the left side of the rectangle. Both values are in pixels. If you have multiple monitors, the left value is probably measured from the left-most point you can move your mouse across all screens.

### View

After all this background information, you'd like to actually see it do something. Now that you've laid the foundation, you can get to the core of the image capture.

Therefore the `AutoDino` defines a `view()` method. Notice how it only takes a self argument. You don't have to tell it which part of the screen should be captured. The `view` method has the instance `self` of the `AutoDion` which has the injected `image_box`.

First you must initialise the `mss` screen capture _instance_ using: `with mss() as screen_capture:` The advantage of this `with` block is that when the block ends, the screen capture automatically stops and is cleaned up. That way you don't accidentally keep it running. If you don't do this, you might wonder why you program becomes slower and slower over time as forgotten screen capture instances are kept running in the background because you did not clean them up yourself.

Inside this while block comes a `while cv2.waitKey(10) != 27` loop. This states that `cv2` (The OpenCV library) waits 10ms to detect that you have sent it an <kbd>Esc</kbd> key-press. As long as you have not pressed <kbd>Esc</kbd>, it keeps repeating what's in the loop.

Inside the loop you state that you use the `screen_capture` instance to `grab` the pixel data from the part of the screen within the current `image_box`. This data is put in a numpy (`np`) array that you call `image`. Numpy provides functionality to easily handle large amounts of *num*bers in *Py*thon.

Finally you use OpenCV's `cv2.imshow(image)` method to show the image in a window on the screen. So you can see what you capture. Right now, you capture a really large area, but you can reposition it and resize it to only capture a point just in front of the dinosaur, where it should see cacti and low-flying birds.

Now run the program and have a look at the captured image. If you click the window that shows the capture and press <kbd>Esc</kbd>, the loop exists and the program continues to its end and terminates. Note that closing the preview window doesn't work. The while loop will just re-open it.

## Starting the game

Next you want to enable the basic functionality to start the game. To do this we use the `keyboard` from `pynput` as a virtual keyboard. To add a virtual keyboard instance to your `AutoDino` instances add this to the `__init__` method:

```python3
        # Initialise a keyboard
        self.keyboard = Controller()
```

First of all you want to start the game automatically. An easy way to do this is to hit <kbd>F5</kbd> to reload the page. Since you don't load the dino-game from the internet, but from your own computer, this is really fast. You let the program wait for a very short amount of time. Then you hit <kbd>Space</kbd> to start the game:

```python3
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
```

In this case you get four seconds of time to activate the game window once the program starts. Otherwise the key presses are sent to the wrong window.

Now change the bottom of the program. Use the example below, but keep in mind that you should probably use your own `image_box` settings instead of these.

```python3
if __name__ == '__main__':
    dino = AutoDino({ 'top': 630, 'left':350, 'width': 100, 'height': 5 })
    dino.start()
    dino.view()
```

Run the game. You should see the instruction to click the game window, the count-down, and – if you clicked the game window in time – it should refresh the page and start the game, and you can see in the capture window what is being captured.
