import os
import cv2

# read video
video_path = os.path.join(os.getcwd(), 'data', 'abstract_video.mp4')

video = cv2.VideoCapture(video_path)

# visualize video
# Get the video's frames per second (FPS)
fps = int(video.get(cv2.CAP_PROP_FPS))

# Calculate the delay between frames in milliseconds
delay = int(1000 / fps)

# Loop through the video frames
while video.isOpened():
    # Read a frame from the video
    ret, frame = video.read()

    # Break the loop if we've reached the end of the video
    if not ret:
        break

    # Display the current frame in a window
    cv2.imshow('frame', frame)

    # Wait for 1ms between frames
    cv2.waitKey(delay)

# Release the VideoCapture object and close all windows
video.release()
cv2.destroyAllWindows()