# import numpy as np
# from scipy.io import wavfile
# import pygame

# class GenerateAlert:
#     def __init__(self):
#         self.sample_rate = 44100
#         self.alert_file = 'alert.wav'
#         self.generate_alert_sound()
#         pygame.mixer.init()
#         pygame.mixer.music.load(self.alert_file)

#     def generate_beep(self, duration_ms=1000, freq=440):
#         t = np.linspace(0, duration_ms/1000, int(self.sample_rate * duration_ms/1000), False)
#         note = np.sin(freq * 2 * np.pi * t)
#         return note

#     def generate_alert_sound(self):
#         beep = self.generate_beep(duration_ms=1000, freq=440)

#         # Apply fade in and fade out
#         fade_duration = int(0.1 * self.sample_rate)
#         fade_in = np.linspace(0, 1, fade_duration)
#         fade_out = np.linspace(1, 0, fade_duration)
#         beep[:fade_duration] *= fade_in
#         beep[-fade_duration:] *= fade_out

#         # Normalize the audio
#         beep = np.int16(beep / np.max(np.abs(beep)) * 32767)

#         # Save the WAV file
#         wavfile.write(self.alert_file, self.sample_rate, beep)

#     def sound_alarm(self):
#         pygame.mixer.music.play()

# if __name__ == "__main__":
#     alert = GenerateAlert()
#     print(f"{alert.alert_file} has been generated successfully.")


import numpy as np
from scipy.io import wavfile
import pygame
import tempfile
import os

class GenerateAlert:
    def __init__(self):
        self.sample_rate = 44100
        self.temp_dir = tempfile.mkdtemp()
        self.alert_file = os.path.join(self.temp_dir, 'alert.wav')
        self.generate_alert_sound()
        pygame.mixer.init()
        pygame.mixer.music.load(self.alert_file)

    def generate_beep(self, duration_ms=1000, freq=440):
        t = np.linspace(0, duration_ms/1000, int(self.sample_rate * duration_ms/1000), False)
        note = np.sin(freq * 2 * np.pi * t)
        return note

    def generate_alert_sound(self):
        beep = self.generate_beep(duration_ms=1000, freq=440)

        # Apply fade in and fade out
        fade_duration = int(0.1 * self.sample_rate)
        fade_in = np.linspace(0, 1, fade_duration)
        fade_out = np.linspace(1, 0, fade_duration)
        beep[:fade_duration] *= fade_in
        beep[-fade_duration:] *= fade_out

        # Normalize the audio
        beep = np.int16(beep / np.max(np.abs(beep)) * 32767)

        # Save the WAV file
        wavfile.write(self.alert_file, self.sample_rate, beep)

    def sound_alarm(self):
        pygame.mixer.music.play()

    def __del__(self):
        # Clean up the temporary file when the object is destroyed
        if os.path.exists(self.alert_file):
            os.remove(self.alert_file)
        if os.path.exists(self.temp_dir):
            os.rmdir(self.temp_dir)

if __name__ == "__main__":
    alert = GenerateAlert()
    print(f"Alert sound file generated at: {alert.alert_file}")

