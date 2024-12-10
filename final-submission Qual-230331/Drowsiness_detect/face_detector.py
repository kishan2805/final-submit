# import dlib
# import cv2

# class FaceDetector:
#     def __init__(self):
#         self.detector = dlib.get_frontal_face_detector()
#         self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#     def detect_faces(self, frame):
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = self.detector(gray)
#         return faces

#     def get_landmarks(self, frame, face):
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         landmarks = self.predictor(gray, face)
#         return landmarks

#     def get_eyes(self, frame, face):
#         """
#         Extracts the left and right eye landmarks.
        
#         :param frame: Input image frame
#         :param face: Detected face bounding box
#         :return: Coordinates of left eye and right eye landmarks
#         """
#         landmarks = self.get_landmarks(frame, face)
#         left_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)]
#         right_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)]
#         return left_eye, right_eye


import dlib
import cv2

class FaceDetector:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return self.detector(gray)

    def get_landmarks(self, frame, face):
        return self.predictor(frame, face)
