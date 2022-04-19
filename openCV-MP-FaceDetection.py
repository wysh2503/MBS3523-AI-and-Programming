import cv2
import numpy as np
print(cv2.__version__)
import mediapipe as mp

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

detectFace = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.7)
drawFace = mp.solutions.drawing_utils

while True:
    success, img = cam.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = detectFace.process(imgRGB)
    print(results.detections)
    if results.detections != None:
        for face in results.detections:
            # drawFace.draw_detection(img, face)
            boundingBox = face.location_data.relative_bounding_box
            pt1 = (int(boundingBox.xmin*1280),int(boundingBox.ymin*720))
            pt2 = (int((boundingBox.xmin+boundingBox.width)*1280),int((boundingBox.ymin+boundingBox.height)*720))
            cv2.rectangle(img, pt1, pt2, (255,0,0),3)
    cv2.imshow('MBS3523 Webcam', img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()