# from scipy.spatial import distance as dist

# def eye_aspect_ratio(eye):
#     A = dist.euclidean(eye[1], eye[5])
#     B = dist.euclidean(eye[2], eye[4])
#     C = dist.euclidean(eye[0], eye[3])
#     ear = (A + B) / (2.0 * C)
#     return ear

# def get_eye_aspect_ratio(landmarks):
#     left_eye = []
#     right_eye = []
#     for n in range(36, 42):
#         left_eye.append((landmarks.part(n).x, landmarks.part(n).y))
#     for n in range(42, 48):
#         right_eye.append((landmarks.part(n).x, landmarks.part(n).y))
    
#     left_ear = eye_aspect_ratio(left_eye)
#     right_ear = eye_aspect_ratio(right_eye)
    
#     return (left_ear + right_ear) / 2.0


# from scipy.spatial import distance as dist

# class EyeAspectRatio:
#     @staticmethod
#     def eye_aspect_ratio(eye):
#         A = dist.euclidean(eye[1], eye[5])
#         B = dist.euclidean(eye[2], eye[4])
#         C = dist.euclidean(eye[0], eye[3])
#         ear = (A + B) / (2.0 * C)
#         return ear

#     @staticmethod
#     def calculate_ear(left_eye, right_eye):
#         left_ear = EyeAspectRatio.eye_aspect_ratio(left_eye)
#         right_ear = EyeAspectRatio.eye_aspect_ratio(right_eye)
#         return (left_ear + right_ear) / 2.0

# def get_eye_aspect_ratio(landmarks):
#     left_eye = []
#     right_eye = []
#     for n in range(36, 42):
#         left_eye.append((landmarks.part(n).x, landmarks.part(n).y))
#     for n in range(42, 48):
#         right_eye.append((landmarks.part(n).x, landmarks.part(n).y))
    
#     ear = EyeAspectRatio.calculate_ear(left_eye, right_eye)
    
#     return ear


from scipy.spatial import distance as dist

class EyeAspectRatio:
    @staticmethod
    def eye_aspect_ratio(eye):
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        C = dist.euclidean(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)
        return ear

    @staticmethod
    def calculate_ear(left_eye, right_eye):
        left_ear = EyeAspectRatio.eye_aspect_ratio(left_eye)
        right_ear = EyeAspectRatio.eye_aspect_ratio(right_eye)
        return (left_ear + right_ear) / 2.0

# Utility function to compute EAR from landmarks
def get_eye_aspect_ratio(landmarks):
    left_eye = [(landmarks.part(n).x, landmarks.part(n).y) for n in range(36, 42)]
    right_eye = [(landmarks.part(n).x, landmarks.part(n).y) for n in range(42, 48)]
    return EyeAspectRatio.calculate_ear(left_eye, right_eye)
