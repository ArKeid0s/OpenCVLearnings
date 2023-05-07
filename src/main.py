import os
import cv2
import numpy as np

img = cv2.imread(os.path.join("data", "whiteboard.png"))

# Lines
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# Rectangles
cv2.rectangle(img, (200, 350), (450, 600), (0, 0, 255), -1)

# Circles
cv2.circle(img, (800, 200), 75, (255, 0, 0), 10)

# Text
cv2.putText(img, "OpenCV", (600, 450), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
