import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import argparse


parser = argparse.ArgumentParser(description='Test von face recognition')
parser.add_argument('-i','--input', help='bild, das analysiert werden soll', required=True)
args = vars(parser.parse_args())
file_name = "./unknown/kurs.png"
file_name = args['input']


# gesuchte gesichter laden
hartmann_image = face_recognition.load_image_file("./known/andreas_hartmann.png")
hartmann_face_encoding = face_recognition.face_encodings(hartmann_image)[0]

glaser_image = face_recognition.load_image_file("./known/beate_glaser.png")
glaser_face_encoding = face_recognition.face_encodings(glaser_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    hartmann_face_encoding,
    glaser_face_encoding
]
known_face_names = [
    "Dr H is in the house",
    "Beate Glaser auch"
]

# lade das Bild, das durchsucht werden soll
unknown_image = face_recognition.load_image_file(file_name)

# Suche alle Gesichter im Bild und encodiere die Bilddaten
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)


# Ab hier nur noch Speichern des Bildes
pil_image = Image.fromarray(unknown_image)
# Eine Kopie des Bildes, auf dem gezeichnet werden kann
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "UNKNOWN"

    # berechne die Distanz zu den Beispielbildern und suche den Anzeigenamen
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]


    if (name != "UNKNOWN"):
        # Zeichne Rechteck und Namen
        draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 255))

        text_width, text_height = 20,10    
        draw.rectangle(((left - 30, bottom + text_height), (right + text_width, bottom + 2*text_height)), fill=(127, 127, 127), outline=(127, 127, 127))
        draw.text((left + 6 - 30, bottom + text_height), name, fill=(255, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw

# Zeige das Bild an (dazu wird die Standardanwendung des Betriebssystem genutzt)
pil_image.show()
