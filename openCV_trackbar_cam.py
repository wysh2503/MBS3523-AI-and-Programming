import cv2
import numpy as np

cam = cv2.VideoCapture(0)

def nil(x):
    pass

cv2.namedWindow('MBS3523')

cv2.createTrackbar('RED','MBS3523',125,255,nil)
cv2.createTrackbar('GREEN','MBS3523',125,255,nil)
cv2.createTrackbar('BLUE','MBS3523',125,255,nil)

cv2.createTrackbar('RADIUS','MBS3523',100,240,nil)
cv2.createTrackbar('CENTER X','MBS3523',320,640,nil)
cv2.createTrackbar('CENTER Y','MBS3523',240,480,nil)

while True:
    success, img = cam.read()
    red = cv2.getTrackbarPos('RED','MBS3523')
    green = cv2.getTrackbarPos('GREEN', 'MBS3523')
    blue = cv2.getTrackbarPos('BLUE', 'MBS3523')
    # img[:,:, 2] = red
    # img[:, :, 1] = green
    img[:, :, 0] = blue
    rad = cv2.getTrackbarPos('RADIUS', 'MBS3523')
    x = cv2.getTrackbarPos('CENTER X', 'MBS3523')
    y = cv2.getTrackbarPos('CENTER Y', 'MBS3523')
    cv2.circle(img,(x,y),rad,(255,0,0),3)
    cv2.imshow('MBS3523', img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()