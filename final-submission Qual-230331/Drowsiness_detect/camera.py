import cv2

class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def get_frame(self):
        _, frame = self.camera.read()
        return frame

    def release(self):
        self.camera.release()