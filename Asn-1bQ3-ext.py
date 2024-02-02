import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cam.read()
    width = cam.get(3) # columnq
    height = cam.get(4) # Row
    # print(height,width)
    splitFrame = np.zeros(frame.shape, np.uint8)
    frameResize = cv2.resize(frame, (int(width/2),int(height/2)))
    splitFrame[:int(height/2),:int(width/2)]=frameResize
    frameFlip0 = cv2.flip(frameResize,0)
    frameFlip0 = cv2.cvtColor(frameFlip0, cv2.COLOR_BGR2HSV)
    splitFrame[int(height/2):,:int(width/2)]=frameFlip0
    frameFlip1 = cv2.flip(frameResize,1)
    frameFlip1 = cv2.cvtColor(frameFlip1, cv2.COLOR_BGR2GRAY)
    # print(frameFlip1.shape)
    frameFlip1 = cv2.cvtColor(frameFlip1, cv2.COLOR_GRAY2BGR)
    # print(frameFlip1.shape)
    splitFrame[:int(height/2),int(width/2):]= frameFlip1
    frameFlip2 = cv2.flip(frameResize,-1)
    frameFlip2 = cv2.GaussianBlur(frameFlip2,(25,25),0)
    splitFrame[int(height/2):,int(width/2):]= frameFlip2
    # cv2.imshow("Webcam", frame)
    # cv2.imshow("Webcam Resized", frameResize)
    cv2.putText(splitFrame,"Original",(5,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv2.putText(splitFrame,"Vertical Flip + HSV output",(5,30+int(height/2)),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
    cv2.putText(splitFrame,"Horizontal Flip + Gray",(5+int(width/2),30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    cv2.putText(splitFrame,"Double Flip + Guassian Blur",(5+int(width/2),30+int(height/2)),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,255),2)
    cv2.imshow("Multiple outputs", splitFrame)

    cur_time = time.time()
    # print(cur_time)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('s'):
        cv2.imwrite('screencap_{}.jpg'.format(cur_time), splitFrame)

cam.release()
cv2.destroyAllWindows()