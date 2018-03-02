import sys
import pyautogui
import thread
from Xlib import display 
from pynput import keyboard, mouse
import numpy as np
from mss import mss
from PIL import Image
import cv2


COMBINATION = {keyboard.Key.shift, keyboard.Key.ctrl}
current = set()
drawnX = 0
drawnY = 0


def on_click(x, y, button, pressed):
    global drawnX
    global drawnY

    if not pressed:
        return True


    qp = display.Display().screen().root.query_pointer()
    print("Current values for drawn x and y", drawnX, drawnY, ", cur pos:", qp.root_x, qp.root_y)

    if qp.root_x == drawnX and qp.root_y == drawnY:
        print('Preventing a new draw since last click was from a draw')
    else :
        if all(k in current for k in COMBINATION) and pressed:
            print('All modifiers active!')
            draw()

def getLineCoordinates():
    qp = display.Display().screen().root.query_pointer()
    print(qp)
    mon = {
        'top': qp.root_y,
        'left': qp.root_x, 
        'width': 400,
        'height': 400
    }
    sct = mss()
    pathname = './'

    img = sct.grab(mon)
    img = Image.frombytes('RGB', img.size, img.rgb)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)   
    #img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]    #img = img.convert('L')
    #img = Image.fromarray(img)
    #img = np.array(img)
    cv2.imshow("Text detection result", img)
    cv2.waitKey(0)    

    return (100, 150)

def draw():
   global drawnX
   global drawnY
   print("----- draw -----")
   pyautogui.click()
   coordinates = getLineCoordinates()
   pyautogui.dragRel(coordinates[0], coordinates[1])
   pyautogui.click()

   qp = display.Display().screen().root.query_pointer()
   drawnX = qp.root_x
   drawnY = qp.root_y
   print("Drawn x and y changed to:", drawnX, drawnY)


def on_press(key):
    if key in COMBINATION:
        current.add(key)
    if key == keyboard.Key.esc:
        return False


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

def observe_keyboard():
   global COMBINATION
   global current

   with keyboard.Listener(
           on_press=on_press,
           on_release=on_release
           ) as listener:
       listener.join()

def observe_mouse():
   global COMBINATION
   global current

   mouseListener = mouse.Listener(on_click=on_click)
   mouseListener.start()

def main():
    try:
       thread.start_new_thread( observe_keyboard, () )
       thread.start_new_thread( observe_mouse, () )
    except:
       print "Error: unable to start thread",  sys.exc_info()[0]
    while 1:
       pass

#main()
getLineCoordinates()
