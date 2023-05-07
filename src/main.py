import os
import cv2

img = cv2.imread(os.path.join('data', 'man_portal.jpg'))

# Convert BGR to RGB
# img_modified = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert BGR to GRAY
# img_modified = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert BGR to HSV
img_modified = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('img', img)
cv2.imshow('img_modified', img_modified)
cv2.waitKey(0)