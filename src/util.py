import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]]) # here insert the bgr values which you want to convert to hsv
    hsv_color = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    lowerLimit = hsv_color[0][0][0] - 10, 100, 100
    upperLimit = hsv_color[0][0][0] + 10, 255, 255
    
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)
    
    return lowerLimit, upperLimit