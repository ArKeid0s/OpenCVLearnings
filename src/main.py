import os
from PIL import Image
import cv2

from util import get_limits

color = (255, 128, 0)

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_array = Image.fromarray(mask)
    bbox = mask_array.getbbox()

    if bbox:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
