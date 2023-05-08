import os
import cv2
import mediapipe as mp

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    # Detect faces
    mp_face_detection = mp.solutions.face_detection
    with mp_face_detection.FaceDetection(
        min_detection_confidence=0.25, model_selection=0
    ) as face_detection:
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out = face_detection.process(img_rgb)

        if out.detections is not None:
            for detection in out.detections:
                location_data = detection.location_data
                bbox = location_data.relative_bounding_box
                x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

                x1 = int(x1 * frame.shape[1])
                y1 = int(y1 * frame.shape[0])
                w = int(w * frame.shape[1])
                h = int(h * frame.shape[0])

                # Blur face
                cv2.blur(frame[y1:y1+h, x1:x1+w], (50, 50), frame[y1:y1+h, x1:x1+w])
                
                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
