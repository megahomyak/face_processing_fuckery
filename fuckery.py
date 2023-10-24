from fer import FER
import cv2

detector = FER()

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break
    emotion, score = detector.top_emotion(frame)
    if emotion is not None:
        print(emotion)
