import os
import cv2

img = cv2.imread(os.path.join('data', 'man_portal.jpg'))
print(img.shape)

# Resize the image to 512x512
resized_img = cv2.resize(img, (512, 512))
# resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # Resize the image to be 50% smaller
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)
