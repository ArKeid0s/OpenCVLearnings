import os
import cv2

img = cv2.imread(os.path.join("data", "bear.jpg"))

# Thresholding is a fundamental image processing technique in computer vision that is used for image segmentation.
# It involves converting a grayscale image into a binary image, where each pixel is assigned either a black or white value based on a specified threshold.
# Thresholding can help in simplifying the image for further processing, by emphasizing certain features or removing noise.
# It is particularly useful in tasks like object detection, edge detection, and image segmentation, where it can be used to separate objects or regions of interest from the background.

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply global thresholding
ret, thresh = cv2.threshold(
    gray, 70, 255, cv2.THRESH_BINARY
)  # 70 is the threshold value, 255 is the max value. If the pixel value is greater than the threshold value, it is a white pixel, else a black pixel.

# Use blur to remove noise
thresh = cv2.medianBlur(gray, 7)
ret, thresh = cv2.threshold(thresh, 70, 255, cv2.THRESH_BINARY)

cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)
