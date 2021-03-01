# Save this file to your Github as OpenCV-13-FaceRec1.py

import cv2
print(cv2.__version__)
import face_recognition
print(face_recognition.__version__)

# Load and find the known images location and encode the face
img_Bill = face_recognition.load_image_file('Images_Known/Bill Gates.jpg')
img_Bill = cv2.cvtColor(img_Bill, cv2.COLOR_RGB2BGR)
faceLoc_Bill = face_recognition.face_locations(img_Bill)[0]
encode_Bill = face_recognition.face_encodings(img_Bill)[0]
print(faceLoc_Bill)
cv2.rectangle(img_Bill, (faceLoc_Bill[3],faceLoc_Bill[0]),(faceLoc_Bill[1],faceLoc_Bill[2]),(255,0,255),2)

# Load and find unknown images, encode, and compare to known faces
imgTest = face_recognition.load_image_file('Images_Unknown/bill-gates-2.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_RGB2BGR)
faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]

cv2.rectangle(imgTest, (faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,0),2)

# Compare images
results = face_recognition.compare_faces([encode_Bill],encodeTest)
face_dist = face_recognition.face_distance([encode_Bill],encodeTest)
print(results)
print(face_dist)

cv2.imshow('Bill Gates',img_Bill)
cv2.imshow('Bill Gates Test image', imgTest)

cv2.waitKey(0)