from deepface import DeepFace
import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break
    try:
        analyzed = DeepFace.analyze(
            frame,
            actions=("emotion",)
        )
    except ValueError:
        pass
    else:
        emotions = analyzed[0]["emotion"]
        print(emotions)
        for emotion_name, emotion_value in emotions.items():
            if emotion_value > 60:
                print(emotion_name)
            break
        else:
            print("No dominant emotion")
