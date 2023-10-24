from deepface import DeepFace
from PIL import Image
import numpy

image = numpy.asarray(Image.open("happy.jpg"))

analyzed = DeepFace.analyze(
    image,
    actions=("emotion",)
)

print(analyzed[0]["dominant_emotion"])
