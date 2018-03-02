import numpy as np
import cv2
import time
from PIL import Image


img = cv2.imread('test.png')

cv2.imshow('Image', img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey', gray)

edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imshow('Canny', edges)
cv2.moveWindow("Canny", 0,300)

lines = cv2.HoughLines(edges,1,np.pi/180,200)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow('Hugh', img)
cv2.moveWindow("Hugh", 300,700)


minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('Hugh Probabalistic',img)


    #img = img.convert('1')    
#    img = Image.frombytes('RGB', img.size, img.rgb)
#    img = np.array(img)
    #img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)   
    #https://stackoverflow.com/questions/7624765/converting-an-opencv-image-to-black-and-white
    #img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]    #img = img.convert('L')
    #img = Image.fromarray(img)
# Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# It's important to add double quotes around the dir path.    
    #txt = pytesseract.image_to_string(img)
    #print(txt)
    #img = np.array(img)
    #cv2.imshow("Text detection result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    #sct_img = np.array(img)


    #(thresh, bw_img) = cv2.threshold(bw_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    #img = Image.fromarray(bw_img)
    #txt = pytesseract.image_to_string(img)
    #print(txt)

    #cv2.imshow("Text detection result", sct_img)
    #cv2.waitKey(0)