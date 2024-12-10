import pygame

class AlertSystem:
    def __init__(self):
        pygame.mixer.init()
        self.alert_sound = pygame.mixer.Sound("alert.wav")

    def play_alert(self):
        self.alert_sound.play()

    def stop_alert(self):
        self.alert_sound.stop()