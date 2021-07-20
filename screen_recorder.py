# This is a simple screen recorder using python
# This program takes maney screenshot and coverts it into a avi file
# Hope you like this code
# By S D Sriram 7-I

import cv2 # pip install opencv-python
import numpy as np # pip install numpy
import pyaudio  # pip install pyaudio
import time
import pyautogui # pip install pyautogui

SCREEN_SIZE =(1920,1080) # Describing th screen size

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi",fourcc,20.0,(SCREEN_SIZE))

fps = 120
prev =0
while True:

    time_elapsed = time.time() - prev

    imag = pyautogui.screenshot() # describes the screenshot

    if time_elapsed >1.0/fps:
        prev = time.time()
        frame = np.array(imag)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) # This is the colur that consists of blue , green , red(It think)
        out.write(frame) # This turns into a normal video
    cv2.waitKey(100) # This takes a screenshot for every 100milisecond

cv2.DestroyAllWindows()  # This code will stop reording
out.release() # This code with save the recording

