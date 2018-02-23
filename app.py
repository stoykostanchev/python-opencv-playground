import numpy as np
import cv2
import time
from mss import mss
from PIL import Image
import pytesseract

mon = {'top':0, 'left':0, 'width':640, 'height': 480}
sct = mss()
pathname = './'

def read_text():
    img = sct.grab(mon)
    #img = img.convert('1')    
    img = Image.frombytes('RGB', img.size, img.rgb)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)   
    #https://stackoverflow.com/questions/7624765/converting-an-opencv-image-to-black-and-white
    img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]    #img = img.convert('L')
    img = Image.fromarray(img)
# Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# It's important to add double quotes around the dir path.    
    txt = pytesseract.image_to_string(img)
    print(txt)
    img = np.array(img)
    cv2.imshow("Text detection result", img)
    cv2.waitKey(0)    
    #sct_img = np.array(img)


    #(thresh, bw_img) = cv2.threshold(bw_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    #img = Image.fromarray(bw_img)
    #txt = pytesseract.image_to_string(img)
    #print(txt)

    #cv2.imshow("Text detection result", sct_img)
    #cv2.waitKey(0)
read_text()
