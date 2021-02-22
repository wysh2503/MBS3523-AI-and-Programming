# Save this file to your Github as OpenCV-10-Haar-face-eye.py

# import libraries
import cv2
import numpy as np
print(cv2.__version__)

# Load the required xml file to detect frontal face
faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
# Load the required xml file to detect frontal face
eyeCascade = cv2.CascadeClassifier('Resources/haarcascade_eye.xml')

# Read the image and change the image from BGR to grayscale
img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Locate the features in the face(s) and return 4 values: x, y, width and height of the detected faces
faces = faceCascade.detectMultiScale(imgGray, 1.03, 5)

# draw rectangle on each face using the 4 values found for each face
for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
    roiImg = img[y:y+h, x:x+w]
    roiGray = imgGray[y:y+h, x:x+w]
    eyes = eyeCascade.detectMultiScale(roiGray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roiImg, (ex,ey), (ex+ew,ey+eh),(0,255,0),1)

# Show the color image with rectangle on each face
cv2.imshow('Faces Detected',img)
cv2.waitKey(0)