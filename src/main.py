import os
import cv2
import easyocr
import matplotlib.pyplot as plt

# Read image
img = cv2.imread(os.path.join('data', 'cedez_passage.jpg'))

# Instance text detector
reader = easyocr.Reader(['fr'], gpu=True)

# Detect text
result = reader.readtext(img)

threshold = 0.25
# Draw bbox and text
for r in result:
    bbox, text, score = r
    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 1)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()