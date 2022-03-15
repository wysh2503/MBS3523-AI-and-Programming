import cv2
import numpy as np

# img = np.zeros([512,512,3], np.uint8)
EVT = 0

def draw_circle(event,x,y,flags,param):
    global EVT
    global PNT
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # print('Event = ', event)
        # print(x,y)
        EVT = event
        PNT = (x,y)
        # cv2.circle(img, (x,y), 100, (255,0,0),-1)
    if event == cv2.EVENT_RBUTTONUP:
        EVT = event
        print(event)

cv2.namedWindow('MBS3523')
cv2.setMouseCallback('MBS3523',draw_circle)

cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()
    if EVT == 7:
        cv2.circle(img, PNT, 100, (255, 0, 0), -1)
        cv2.imshow('MBS3523',img)
    if EVT == 5:
        cv2.imshow('MBS3523', img)
    cv2.imshow('MBS3523', img)
    if cv2.waitKey(1) & 0xff == 27: break

cv2.destroyAllWindows()
