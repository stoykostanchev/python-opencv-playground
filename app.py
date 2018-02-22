import numpy as np
import cv2
import time
from mss import mss
from PIL import Image

mon = {'top':0, 'left':0, 'width':640, 'height': 480}
sct = mss()

def screen_record():
    while(True):
       frame = np.array(sct.grab(mon))
       hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

       lower_red = np.array([30,150,50])
       upper_red = np.array([255,255,180])
       mask = cv2.inRange(hsv, lower_red, upper_red)
       res = cv2.bitwise_and(frame, frame, mask = mask)
       cv2.imshow('frame', frame)
       cv2.imshow('mask', mask)
       cv2.imshow('res', res)

       if cv2.waitKey(25) & 0xFF == ord('q'):
           cv2.destroyAllWindows()
           break

screen_record()
