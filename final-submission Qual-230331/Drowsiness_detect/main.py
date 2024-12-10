import cv2
import numpy as np
from camera import Camera
from face_detector import FaceDetector
from eye_aspect_ratio import get_eye_aspect_ratio
from drowsiness_detector import DrowsinessDetector
from alert_system import AlertSystem
import time

def main():
    camera = Camera()
    face_detector = FaceDetector()
    drowsiness_detector = DrowsinessDetector()
    alert_system = AlertSystem()

    # Train the drowsiness detector (you would normally do this with a larger dataset)
    X = np.random.rand(1000, 1)  # Replace with actual EAR data
    y = np.random.randint(2, size=1000)  # Replace with actual drowsiness labels
    drowsiness_detector.train(X, y)

    EAR_THRESHOLD = 0.25
    CONSECUTIVE_FRAMES = 20
    counter = 0

    while True:
        frame = camera.get_frame()
        faces = face_detector.detect_faces(frame)

        for face in faces:
            landmarks = face_detector.get_landmarks(frame, face)
            ear = get_eye_aspect_ratio(landmarks)

            if ear < EAR_THRESHOLD:
                counter += 1
                if counter >= CONSECUTIVE_FRAMES:
                    if drowsiness_detector.predict(ear):
                        cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        alert_system.play_alert()
            else:
                counter = 0
                alert_system.stop_alert()

            cv2.putText(frame, f"EAR: {ear:.2f}", (300, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow("Drowsiness Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()