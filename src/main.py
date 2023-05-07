import os
import cv2

img = cv2.imread(os.path.join("data", "birds.jpg"))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    if cv2.contourArea(contour) > 200:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.drawContours(img, contour, -1, (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)
