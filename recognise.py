import face_recognition
import numpy as np
from PIL import Image, ImageDraw

known_image = face_recognition.load_image_file("saka.jpg")
encoding = face_recognition.face_encodings(known_image)[0]

unknown_image = face_recognition.load_image_file("team photo.jpg")
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
pil_image = Image.fromarray(unknown_image)

draw = ImageDraw.Draw(pil_image)
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces([encoding], face_encoding)
    face_distance = face_recognition.face_distance([encoding], face_encoding)
    best_match_index = np.argmin(face_distance)
    if matches[best_match_index] and face_distance < 0.3:
        draw.rectangle(((left-20, top-20), (right+20, bottom+20)), outline=(0, 255, 0), width = 20)
del draw
pil_image.show()




