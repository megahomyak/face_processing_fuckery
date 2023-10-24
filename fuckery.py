from fer import FER
import cv2
from statistics import mode
from collections import deque


detector = FER()
camera = cv2.VideoCapture(0)

recent_emotions = deque(maxlen=10)

while True:
    ret, frame = camera.read()
    if not ret:
        break
    emotion, score = detector.top_emotion(frame)
    if emotion is not None:
        recent_emotions.append(emotion)
        probable_emotion = mode(recent_emotions)
        print(probable_emotion)
