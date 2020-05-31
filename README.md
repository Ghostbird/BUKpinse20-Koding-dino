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

Next you want to enable the basic functionality to start the game. To do this you use the `keyboard` from `pynput` as a virtual keyboard. To add a virtual keyboard instance to your `AutoDino` instances add this to the `__init__` method:

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

## Detecting obstacles

Currently the dinosaur just runs happily into the first cactus encountered and then looks very surprised. You'd want to know when an obstacle is incoming.

### Basic image processing

How do you know that something is incoming. For now we'll use a simple method. A white pixel has a value of 255. The grey pixels used by the game have a lesser value. You know the image box. So if you take the image height × image width × 255 that is the value of an image with no obstacles. Any lesser value can be considered an obstacle.

Now add this method to your `AutoDino` class:

```python3
    def run(self):
        self.start()
        # Wait one second for the zoom effect to end
        sleep(1)
        no_obstacle_value = self.image_box["height"] * self.image_box["width"] * 255
        with mss() as screen_capture:
            while True:
                # Grab the pixels in the box (in full colour)
                image = np.array(screen_capture.grab(self.image_box))
                # Discard unneeded colour information, makes calculations faster
                image_grey = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
                # Calculate the total value of the pixels in the box.
                value = image_grey.sum()
                if value < no_obstacle_value:
                    print('Obstacle!')
```

Once you `run()` the `AutoDino` instance, you first want to start the dino game. If you use Chrome/Chromium, the game zooms to fit the browser window after the start. Therefore you wait a second without doing anything.

Then you calculate the value of a pure white capture area as described above.

Next you initialise the screen capture and inside that you run a loop. Contrary to earlier, this loop will not show a capture window, and therefore cannot be ended by a keypress. For now, just make it infinite.

In the loop, you grab the image just as before. But now you use the OpenCV colour transformation to discard all colour information, and make the image black-and-white. You don't need colours here, and in this case it would make the calculations unnecessary complex. Finally, because the `image_grey` is a numpy array you can call `sum()` on it to get the total of all values in the image.

Now if the calculation gives a `value` that is less than the `no_obstacle_value`, there is probably an obstacle, so you print that.

Change the bottom of the program to match the example below. Keep in mind to use your own image box values:

```python3
if __name__ == '__main__':
    AutoDino({ 'top': 630, 'left':350, 'width': 100, 'height': 5 }).run()
```

Run the program, and if everything went well, you'll see the dinosaur run into the first cactus, and the program will show the text _Obstacle_ a lot, starting the moment the cactus enters the capture area. Note that it doesn't show it only once, but it keeps spamming it in the loop, as long as there's an obstacle in view.

## Control your dinosaur

Now your program can detect obstacles, but the dinosaur still runs into the first cactus. Therefore you must make the dino jump. Luckily this one is fairly easy.

A jump is defined as pressing down the spacebar, waiting a short amount of time, and releasing it:

```python3
    def jump(self):
        self.keyboard.press(Key.space)
        sleep(0.3)
        self.keyboard.release(Key.space)
```

Then, replace the line `print('Obstacle')` in `run()` with:

```python3
        self.jump()
```

Now run the game, and you should see that your dinosaur jumps over the detected obstacles.

### It's a bird, duck

Your dinosaur won't make it that far, until he runs into a low-flying bird. Depending on the detection area, he might jump over it. However that's not a good option if you want the game to work really well.

The simplest option is to make the dinosaur _always_ duck, when he's not jumping. Change the jump method to:

```python3
    def jump(self):
        self.keyboard.release(Key.down)
        self.keyboard.press(Key.space)
        sleep(0.3)
        self.keyboard.release(Key.space)
        self.keyboard.press(Key.down)
```

Run the game and you will see the dinosaur jump and duck. At this point you might have to change the image box values a bit. Otherwise it might try to jump over birds that it can pass more easily by just running under them.

Note that when you stop the game, your computer might think that you're still pressing the down button, since the game never stopped doing that. To fix this, just press and release the down button on the keyboard once.

## Slightly more advanced image processing

Now at this point you might notice that around 700 points, the dino game becomes white on black instead of black on white. This completely throws off your basic image processing. How can you actually still easily recognise everything, even though the colours are inverted? Because the lines are clear against the background, as long as the two colours are different enough.

You can use the Laplacian operator in image processing to get a measure of the difference in an image. This involves some calculus, but luckily OpenCV has a ready made `cv2.Laplacian` method already built-in.

To see how this works, change you `view()` method to:

```python3
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
```

Now change the last line of the program to `view()` instead of `run()`, then start the program. You will see a mostly black capture window with some while lines when an obstacle passes.

### Calculate the difference

You can add this method to calculate the amount of difference (or contrast) in the image:

```python3
    def difference(self, image_grey):
        # Calculate edges
        image_laplacian = cv2.Laplacian(image_grey, cv2.CV_64F)
        # Get the of nonzero values of the laplacian.
        non_zero = image_laplacian.nonzero()
        # Count the nonzero values of the laplacian
        return len(non_zero[0]) + len(non_zero[1])
```

When you give this function the grey-scale image as input, it will:

1. Calculate the Laplacian.
2. Give all non-zero values of the Laplacian
3. Count the number of non-zero values in both dimensions of the 2D image and give you the total

### Make it work

Change your run function to match this, note that only the last part starting from `value = ` actually has changed.

```python3
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
```

Basically when we capture the grey-scale image, we ask the `difference` method to give us the total amount of contrast, and if it is not zero, there must be some obstacle on the screen in addition to the solid colour background. The actual colours of the obstacles and the background no longer matter.

Don't forget to change the final line of the code again to `run()` the game. Give it a try!

## Challenge

Tweak your capture are, the `sleep` time in `jump` etc. to get the best result possible. Post a video of your bot running a high score, in the Discord channel. The to scorer will get a small price. Please be fair and don't cheat.
