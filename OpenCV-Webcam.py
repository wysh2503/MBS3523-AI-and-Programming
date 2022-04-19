import cv2
import numpy as np
print(cv2.__version__)

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


while True:
    success, img = cam.read()

    cv2.imshow('MBS3523 Webcam', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()