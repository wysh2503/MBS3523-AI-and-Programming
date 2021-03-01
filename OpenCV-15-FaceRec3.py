# Save this file to your Github as OpenCV-15-FaceRec3.py

import cv2
print(cv2.__version__)
import face_recognition
print(face_recognition.__version__)
import numpy as np

# Load and find the known images location and encode the face
imgKnown = face_recognition.load_image_file('Images_Known/wy-1.png')
imgKnown = cv2.cvtColor(imgKnown, cv2.COLOR_RGB2BGR)
faceLocKnown = face_recognition.face_locations(imgKnown)[0]
encodeKnown = face_recognition.face_encodings(imgKnown)[0]

capture = cv2.VideoCapture(1)
capture.set(3,640)
capture.set(4,480)

while True:
    success, img = capture.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # From webcam, read and find unknown images, encode, and compare to known faces
    faceLocsCam = face_recognition.face_locations(imgRGB)
    encodesCam = face_recognition.face_encodings(imgRGB, faceLocsCam)

    # Compare faces in webcam to encoded face
    for (top,right,bottom,left),encodeCam in zip(faceLocsCam,encodesCam):
        results = face_recognition.compare_faces([encodeKnown],encodeCam)
        faceDist = face_recognition.face_distance([encodeKnown],encodeCam)
        print(faceDist)
        if faceDist < 0.4:
                cv2.rectangle(img, (left,top),(right,bottom), (255, 0, 0), 2)

    cv2.imshow('Frame', img)
    #cv2.moveWindow('Frame', 100,20)
    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()