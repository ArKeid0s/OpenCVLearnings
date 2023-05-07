import os
import cv2

img = cv2.imread(os.path.join("data", "freelancer.jpeg"))
img_noise = cv2.imread(os.path.join("data", "cow-salt-peper.png"))

# Blur filters
# k_size = 11  # larger k_size means more blur
# img_blur = cv2.blur(img, (k_size, k_size))
# img_blur = cv2.GaussianBlur(img, (k_size, k_size), 5)
# img_blur = cv2.medianBlur(img, k_size)

# Use blur to remove noise
k_size = 7
img_noise_blur = cv2.blur(img_noise, (k_size, k_size))
img_noise_blur_gaussian = cv2.GaussianBlur(img_noise, (k_size, k_size), 5)
img_noise_blur_median = cv2.medianBlur(img_noise, k_size) # the noise is removed better

# cv2.imshow("img", img)
# cv2.imshow("img_blur", img_blur)
cv2.imshow("img_noise", img_noise)
cv2.imshow("img_noise_blur", img_noise_blur)
cv2.imshow("img_noise_blur_gaussian", img_noise_blur_gaussian)
cv2.imshow("img_noise_blur_median", img_noise_blur_median)
cv2.waitKey(0)
