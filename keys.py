import time
import keyboard

W = 0x11
A = 0x1E
S = 0x1F
D = 0x20

def PressKey(key):

    print('down')
    keyboard.press(key)
    time.sleep(3)
    print('up')
    keyboard.release(key)