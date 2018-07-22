import numpy as np
from PIL import ImageGrab
import cv2
import time
import keyboard
from keys import PressKey, W, A, S, D

def process_img(image):
    original_image = image
    # convert to grey
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img

def main():

    # countdown delay to get placed into the game
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    last_time = time.time()
    PressKey(W)
    while(True):
        #PressKey(W)
        # 800x600 windowed mode for GTA5, at top left position of main screen
        # 40 px for title bar at top
        screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        #print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        #cv2.imshow('window', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        cv2.imshow('window', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()