import os
import cv2

# read image
image_path = os.path.join(os.getcwd(), 'data', 'man_portal.jpg')

img = cv2.imread(image_path)

# write image
cv2.imwrite(os.path.join(os.getcwd(), 'data', 'man_portal_out.jpg'), img)

# show image
cv2.imshow('frame', img)
cv2.waitKey(0)