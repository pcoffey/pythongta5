import numpy as np
from PIL import ImageGrab
import cv2
import time
import keyboard
from keys import PressKey, W, A, S, D

def roi(img, vertices):
    # blank mask
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(original_image):
    # convert to grey
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    #Shape the mask
    vertices = np.array([[10,500], [10,300], [300, 200], [500,200], [800,500]], np.int32)
    processed_img = roi(processed_img, [vertices])
    return processed_img

def main():

    # countdown delay to get placed into the game
#    for i in list(range(4))[::-1]:
#        print(i + 1)
#        time.sleep(1)

    last_time = time.time()
    #PressKey(W)
    while(True):
        #PressKey(W)
        # 800x600 windowed mode for GTA5, at top left position of main screen
        # 40 px for title bar at top
        screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        new_screen = process_img(screen)
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()

        #cv2.imshow('window', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        cv2.imshow('window', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()