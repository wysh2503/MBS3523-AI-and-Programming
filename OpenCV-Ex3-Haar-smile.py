# Save this file to your Github as OpenCV-Ex3-Haar-smile.py
import cv2
import numpy as np
print(cv2.__version__)

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('Resources/haarcascade_smile.xml')

capture = cv2.VideoCapture('Resources/IU-edited.mp4')
# capture = cv2.VideoCapture(0)
capture.set(3,640)
capture.set(4,480)

font = cv2.FONT_HERSHEY_PLAIN

while True:
    success, img = capture.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 10)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roiImg = img[y:y + h, x:x + w]
        roiGray = imgGray[y:y + h, x:x + w]
        smiles = smileCascade.detectMultiScale(roiGray, 1.8, 8)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roiImg, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 1)
            cv2.putText(img,'SMILE',(x,y),font,1.5, (0,0,255),2)

    cv2.imshow('Frame', img)
    #cv2.moveWindow('Frame', 100,20)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()