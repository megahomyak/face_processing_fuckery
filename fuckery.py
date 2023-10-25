from fer import FER
import cv2
from statistics import mode
from collections import deque
import numpy
import sounddevice
import argparse

parser = argparse.ArgumentParser(
    description="A vtuber software with visual emotion recognition",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    prog="python -m is_that_you"
)
parser.add_argument("--volume-threshold", "-v", default=0.3, help="the amount of volume from your microphone after which the mouth will open")
parser.add_argument("--emotion-stabilization-frames-amount", "-f", default=10, help="the amount of recent frames that are used to calculate the most frequent emotion. This is used to prevent one-off incorrect emotion recognition. Higher numbers lead to more accurate recognition, but it will take more time for the emotion to switch")
args = parser.parse_args()

detector = FER()
real_camera = cv2.VideoCapture(0)
recent_emotions = deque(maxlen=args.emotion_stabilization_frames_amount)

mouth_open = False
current_emotion = "neutral"

def update_view():
    print(current_emotion, mouth_open)

def process_sound(frames, _frames_amount, _time, _status):
    print(1)
    global last_index, mouth_open
    volume_norm = numpy.linalg.norm(frames)
    print(2)
    if volume_norm > args.volume_threshold:
        if not mouth_open:
            mouth_open = True
            update_view()
    else:
        if mouth_open:
            mouth_open = False
            update_view()

i = sounddevice.InputStream(callback=process_sound, latency=0.1)
i.start()

while True:
    ret, frame = real_camera.read()
    if not ret:
        break
    i.stop() # A workaround to prevent it from segfaulting (or having an "illegal instruction")
    emotion, score = detector.top_emotion(frame)
    i.start()
    if emotion is not None:
        recent_emotions.append(emotion)
        probable_emotion = mode(recent_emotions)
        if current_emotion != probable_emotion:
            current_emotion = probable_emotion
            update_view()
