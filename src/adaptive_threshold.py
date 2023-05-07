import os
import cv2

img = cv2.imread(os.path.join("data", "handwritten.png"))

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 30) # best results
thresh_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

cv2.imshow("img", img)
cv2.imshow("thresh_mean", thresh_mean)
cv2.imshow("thresh_gaussian", thresh_gaussian)
cv2.waitKey(0)
