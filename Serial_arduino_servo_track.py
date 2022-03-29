import cv2
import serial
import time
import numpy as np

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

ser = serial.Serial('COM7',baudrate=115200,timeout=1)
time.sleep(0.5)
pos = 90
# print(type(pos))

cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.05, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
        errorPan = (x + w/2) - 640/2
        print('errorPan', errorPan)
        # print(type(errorPan))
        if abs(errorPan) > 20:
            pos = pos - errorPan/30
            print(type(pos))
        if pos > 160:
            pos = 160
            print("Out of range")
        if pos < 0:
            pos = 0
            print("out of range")
        servoPos = str(pos) + '\r'
        ser.write(servoPos.encode())
        print('servoPos = ', servoPos)
        # print(type(pos))
        time.sleep(0.1)
    cv2.imshow('MBS3523 Webcam', img)

    if cv2.waitKey(1) & 0xff == 27:
        break

ser.close()
cam.release()
cv2.destroyAllWindows()