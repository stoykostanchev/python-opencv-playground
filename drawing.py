import sys
import pyautogui
from Xlib import display 

# pyautogui.click()

# pyautogui.moveTo(100, 150)
# pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
# pyautogui.click()
# pyautogui.moveRel(0, -50)
# pyautogui.dragRel(0, 101)  # drag mouse 10 pixels down
# pyautogui.moveRel(0, -50)

from pynput import keyboard, mouse

# The key combination to check
COMBINATION = {keyboard.Key.shift, keyboard.Key.ctrl}

# The currently active modifiers
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

mouseListener = mouse.Listener(on_click=on_click)

def draw():
   global drawnX
   global drawnY
   print("----- draw -----")
   pyautogui.click()
   pyautogui.dragRel(100, 150)
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



import thread


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

   mouseListener.start()

try:
   thread.start_new_thread( observe_keyboard, () )
   thread.start_new_thread( observe_mouse, () )
except:
   print "Error: unable to start thread",  sys.exc_info()[0]

while 1:
   pass

