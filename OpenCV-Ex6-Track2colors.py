# Save this file to Github as OpenCV-Track2colors.py

import cv2
import numpy as np

def nothing(): pass

cv2.namedWindow('Trackbars')

cv2.createTrackbar('HueLow','Trackbars',24,179,nothing)
cv2.createTrackbar('HueHigh','Trackbars',86,179,nothing)
cv2.createTrackbar('SatLow','Trackbars',139,255,nothing)
cv2.createTrackbar('SatHigh','Trackbars',255,255,nothing)
cv2.createTrackbar('ValLow','Trackbars',122,255,nothing)
cv2.createTrackbar('ValHigh','Trackbars',255,255,nothing)

##############################################
# Below lines are added for sencond color tracking
cv2.namedWindow('Trackbars2')

cv2.createTrackbar('HueLow2','Trackbars2',24,179,nothing)
cv2.createTrackbar('HueHigh2','Trackbars2',86,179,nothing)
cv2.createTrackbar('SatLow2','Trackbars2',139,255,nothing)
cv2.createTrackbar('SatHigh2','Trackbars2',255,255,nothing)
cv2.createTrackbar('ValLow2','Trackbars2',122,255,nothing)
cv2.createTrackbar('ValHigh2','Trackbars2',255,255,nothing)
###############################################

# Set up webcam
cam = cv2.VideoCapture(1)
# cam.set(3,640)
# cam.set(4,480)

# Start capturing and show frames on window
while True:
    success, img = cam.read()

    img2 = img.copy()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hueLow = cv2.getTrackbarPos('HueLow','Trackbars')
    hueHigh = cv2.getTrackbarPos('HueHigh', 'Trackbars')
    satLow = cv2.getTrackbarPos('SatLow', 'Trackbars')
    satHigh = cv2.getTrackbarPos('SatHigh', 'Trackbars')
    valLow = cv2.getTrackbarPos('ValLow', 'Trackbars')
    valHigh = cv2.getTrackbarPos('ValHigh', 'Trackbars')

    ##############################################
    # Below lines are added for sencond color finding
    hsv2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hueLow2 = cv2.getTrackbarPos('HueLow2','Trackbars2')
    hueHigh2 = cv2.getTrackbarPos('HueHigh2', 'Trackbars2')
    satLow2 = cv2.getTrackbarPos('SatLow2', 'Trackbars2')
    satHigh2 = cv2.getTrackbarPos('SatHigh2', 'Trackbars2')
    valLow2 = cv2.getTrackbarPos('ValLow2', 'Trackbars2')
    valHigh2 = cv2.getTrackbarPos('ValHigh2', 'Trackbars2')
    ##############################################


    FGmask = cv2.inRange(hsv, (hueLow,satLow,valLow),(hueHigh,satHigh,valHigh))
    cv2.imshow('FGmask',FGmask)
    final = cv2.bitwise_and(img,img,mask=FGmask)

    ##############################################
    # Below lines are added for sencond color masking
    FGmask2 = cv2.inRange(hsv2, (hueLow2, satLow2, valLow2), (hueHigh2, satHigh2, valHigh2))
    cv2.imshow('FGmask2', FGmask2)
    final2 = cv2.bitwise_and(img2, img2, mask=FGmask2)
    ##############################################

    FGmaskAdded = cv2.add(FGmask,FGmask2)

    contours, hierarchy = cv2.findContours(FGmaskAdded,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        (x,y,w,h) = cv2.boundingRect(cnt)
        if area > 100:
            #cv2.drawContours(img,[cnt],0,(255,0,0),3)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow('Final', final)
    cv2.imshow('Final2', final2)
    cv2.imshow('Frame', img)
    if cv2.waitKey(1) == 27:
        break

# cam.release()
cv2.destroyAllWindows()