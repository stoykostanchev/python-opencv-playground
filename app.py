import numpy as np
import cv2
import time
from mss import mss
from PIL import Image

mon = {'top':0, 'left':0, 'width':640, 'height': 480}
sct = mss()

def screen_record():
    last_time = time.time()
    
    while(True):
       
       printscreen = np.array(sct.grab(mon))
       print('look took {} seconds'.format(time.time() - last_time))
       last_time = time.time()
       cv2.imshow('window', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))

       if cv2.waitKey(25) & 0xFF == ord('q'):
           cv2.destroyAllWindows()
           break

screen_record()
