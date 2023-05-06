import cv2

# read webcam
webcam = cv2.VideoCapture(0)

# visualize webcam
while webcam.isOpened():
    # Read a frame from the webcam
	ret, frame = webcam.read()

	# Break the loop if we've reached the end of the video
	if not ret:
		break

	# Display the current frame in a window
	cv2.imshow('frame', frame)

	# Wait for 1ms between frames
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# Release the VideoCapture object and close all windows
webcam.release()
cv2.destroyAllWindows()