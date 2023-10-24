from fer import FER
import cv2

detector = FER()

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break
    try:
        analyzed = detector.top_emotion(frame)
    except ValueError:
        pass
    else:
        print(analyzed)
