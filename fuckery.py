from deepface import DeepFace
from PIL import Image
import numpy

image = numpy.asarray(Image.open("happy.jpg"))

analyzed = DeepFace.analyze(
    image,
    actions=("emotion",)
)

print(analyzed[0]["dominant_emotion"])

with pyvirtualcam.Camera(width=width, height=height, fps=60, device=args.device, backend=args.backend) as cam:
    logging.debug("Connected the camera using the device %s!", cam.device)
    last_index = 0
    cam.send(frames[last_index])

    frame = cam.

    def process_sound(indata, _frames, _time, _status):
        volume_norm = numpy.linalg.norm(indata)
        if volume_norm > args.volume_threshold:
        cam.send()

    sounddevice.InputStream(callback=process_sound, latency=0.1).start()
    block()
