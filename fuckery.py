from deepface import DeepFace
import cv2

camera = cv2.VideoCapture()

while True:
    ret, frame = camera.read()
    if not ret:
        break
    analyzed = DeepFace.analyze(
        frame,
        actions=("emotion",)
    )

    print(analyzed[0]["dominant_emotion"])
    break
