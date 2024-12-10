import streamlit as st
import cv2
import numpy as np
from drowsiness_detector import DrowsinessDetector
from face_detector import FaceDetector
from eye_aspect_ratio import get_eye_aspect_ratio
from generate_alert import GenerateAlert
import tempfile
import os

# Initialize components
face_detector = FaceDetector()
generate_alert = GenerateAlert()
drowsiness_detector = DrowsinessDetector()

# Simulated training data
sample_X = np.random.rand(100, 1)  # 100 random EAR values
sample_y = np.random.randint(2, size=100)  # 0 for not drowsy, 1 for drowsy
drowsiness_detector.train(sample_X, sample_y)

st.title("Drowsiness Detection System")

# File uploader for video
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    # Open the video file
    cap = cv2.VideoCapture(tfile.name)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    video_placeholder = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detect faces
        faces = face_detector.detect_faces(frame)
        for face in faces:
            # Get EAR (Eye Aspect Ratio)
            ear = get_eye_aspect_ratio(face_detector.get_landmarks(frame, face))

            # Predict drowsiness
            is_drowsy = drowsiness_detector.predict(ear)

            if is_drowsy:
                generate_alert.sound_alarm()
                cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Display frame
        video_placeholder.image(frame, channels="BGR", use_column_width=True)

    cap.release()
    os.unlink(tfile.name)

st.write("Video processing complete.")
