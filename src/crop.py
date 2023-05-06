import os
import cv2

image = cv2.imread(os.path.join("data", "man_portal.jpg"))
print(image.shape)

# select the region of interest in the image
height, width, channels = image.shape
upper_left = (width // 4, height // 4)
bottom_right = (width * 3 // 4, height * 3 // 4)
# draw in the image
cv2.rectangle(image, upper_left, bottom_right, (0, 255, 0), thickness=1)

# Calculate the center of the image and the top-left corner and bottom-right corner of the cropped image
h, w = 300, 300
x = height//2 - w//2
y = width//2 - h//2
# Crop the image
cropped_image = image[int(y):int(y+h), int(x):int(x+w)]

print(cropped_image.shape)

cv2.imshow("img", image)
cv2.imshow("cropped_img", cropped_image)
cv2.waitKey(0)