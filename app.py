import numpy as np
import cv2
import time
from mss import mss
from PIL import Image

mon = {'top':0, 'left':0, 'width':640, 'height': 480}
sct = mss()
pathname = './'

def screen_record():
    #while(True):
	#https://github.com/opencv/opencv_contrib/blob/master/modules/text/samples/textdetection.py
       sct_img = sct.grab(mon)
       img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
       sct_img = np.array(img)
       #cv2.imshow('OpenCV/Numpy normal', sct_img)
       #img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
       # Here maybe turn the image to a black and white, 1 and 0s
       channels = cv2.text.computeNMChannels(sct_img)
       cn = len(channels)-1

       for c in range(0, cn):
           channels.append((255-channels[c]))

       for channel in channels:
           erc1 = cv2.text.loadClassifierNM1(pathname+'/trained_classifierNM1.xml')
           er1 = cv2.text.createERFilterNM1(erc1,16,0.00015,0.13,0.2,True,0.1)
           erc2 = cv2.text.loadClassifierNM2(pathname+'/trained_classifierNM2.xml')
           er2 = cv2.text.createERFilterNM2(erc2,0.5)     
           regions = cv2.text.detectRegions(channel,er1,er2)
           rects = cv2.text.erGrouping(sct_img,channel,[r.tolist() for r in regions])
       
       	   #Visualization
           for r in range(0,np.shape(rects)[0]):
               rect = rects[r]
               cv2.rectangle(sct_img, (rect[0],rect[1]), (rect[0]+rect[2],rect[1]+rect[3]), (0, 0, 0), 2)
               cv2.rectangle(sct_img, (rect[0],rect[1]), (rect[0]+rect[2],rect[1]+rect[3]), (255, 255, 255), 1)
       
       #Visualization
       cv2.imshow("Text detection result", sct_img)
       cv2.waitKey(0)
       
       if cv2.waitKey(25) & 0xFF == ord('q'):
           cv2.destroyAllWindows()
       #break

screen_record()
