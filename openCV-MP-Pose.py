import cv2
import numpy as np
print(cv2.__version__)
import mediapipe as mp

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

myPose = mp.solutions.pose.Pose(False,False,True,0.5,0.5)
drawPose = mp.solutions.drawing_utils

while True:
    success, img = cam.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = myPose.process(imgRGB)
    # print(results)
    landmarks=[]
    if results.pose_landmarks != None:
        # drawPose.draw_landmarks(img, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
        # print(results.pose_landmarks)
        for lm in results.pose_landmarks.landmark:
            print(lm.x,lm.y)
            landmarks.append((int(lm.x*1280),int(lm.y*720)))
        print(landmarks)
        # cv2.circle(img,landmarks[0], 20,(0,0,255),5)
        cv2.circle(img, landmarks[1], 5, (255, 0, 255), 5)
        cv2.circle(img, landmarks[4], 5, (255, 0, 255), 5)

    cv2.imshow('MBS3523 Webcam', img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()