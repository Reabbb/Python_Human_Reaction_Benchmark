import cv2
import numpy as np
import pyautogui
import keyboard
import time

# define green color range in HSV
lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])

while True:
    # take screenshot of the screen
    screenshot = np.array(pyautogui.screenshot())

    # convert screenshot to HSV color space
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)

    # get color under cursor
    x, y = pyautogui.position()
    color = hsv[y, x]

    # check if color is within green range
    if np.all(color > lower_green) and np.all(color < upper_green):
        print("Hello World")
        
        # perform left click after 0.01 seconds
        time.sleep(0.01)
        pyautogui.click(button='left')

    # check if 'q' key is pressed to exit program
    if keyboard.is_pressed('q'):
        break
