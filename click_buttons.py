import sys
import pyautogui
import thread
import time
from Xlib import display
from pynput import keyboard, mouse

import numpy as np
from mss import mss
from PIL import Image
import cv2
import json

data = json.load(open('data.json')) W W W W
actions = []

for action in data["actions"]:
    keysRaw = [key.strip() for key in action["shortcut"].split("+")]
    keys = set()

    for key in keysRaw:
        try:
            keys.add(keyboard.Key[key])
        except Exception:
            keys.add(keyboard.KeyCode.from_char(key))
    actions.append({ "name": action["name"], "shortcut": keys, "commands": action["execute"]})


sct = mss()

current = set()


def findBtnCoord(btnImgSrc):
    # screen = sct.grab(mon)
    for num, monitor in enumerate(sct.monitors[1:], 1):
        # Get raw pixels from the screen
        sct_img = sct.grab(monitor)
        # Create the Image

    screen = np.array(sct_img)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGRA2GRAY)
    #cv2.imshow("Origin", screen)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    template = cv2.imread(btnImgSrc,0)

    w, h = template.shape[::-1]

    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc
    #bottom_right = (top_left[0] + w, top_left[1] + h)

    #cv2.rectangle(screen ,top_left, bottom_right, 255, 2)

    #cv2.imshow("Match", screen)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return (top_left[0] + w/2, top_left[1] + h/2)


def clickBtn(btnImgSrc):
    coordinates = findBtnCoord(btnImgSrc)
    qp = display.Display().screen().root.query_pointer()
    pyautogui.moveTo(coordinates[0], coordinates[1])
    pyautogui.click()
    pyautogui.moveTo(qp.root_x, qp.root_y)


def executeAction(act):
    if act["type"] == "text":
        print(act["value"])
    else :
        if act["type"] == "click":
            clickBtn(act["value"])

def executeActionSeries(actionSeries):
   for ass in actionSeries:
       for ad in data["actionDefinitions"]:
           if ad["name"] == ass:
               executeAction(ad)

def on_press(key):
    current.add(key)

    for action in actions:
        if all(k in current for k in action["shortcut"]):
            executeActionSeries(action["commands"])

    if key == keyboard.Key.esc:
        return False


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

def observe_keyboard():
   with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
       listener.join()

observe_keyboard()