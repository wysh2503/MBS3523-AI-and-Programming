import cv2
print(cv2.__version__)

def NIL(x):
    pass

cv2.namedWindow('MBS3523')

cv2.createTrackbar('HL','MBS3523', 35, 179, NIL)
cv2.createTrackbar('HH','MBS3523', 55, 179, NIL)
cv2.createTrackbar('SL','MBS3523', 110, 255, NIL)
cv2.createTrackbar('SH','MBS3523', 255, 255, NIL)
cv2.createTrackbar('VL','MBS3523', 70, 255, NIL)
cv2.createTrackbar('VH','MBS3523', 255, 255, NIL)

cam = cv2.VideoCapture(0) # try 1, 2 or 3 if you have error

while True:
    success, img = cam.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hueLow = cv2.getTrackbarPos('HL','MBS3523')
    hueHigh = cv2.getTrackbarPos('HH', 'MBS3523')
    satLow = cv2.getTrackbarPos('SL', 'MBS3523')
    satHigh = cv2.getTrackbarPos('SH', 'MBS3523')
    valueLow = cv2.getTrackbarPos('VL', 'MBS3523')
    valueHigh = cv2.getTrackbarPos('VH', 'MBS3523')

    mask1 = cv2.inRange(imgHSV,(hueLow,satLow,valueLow),(hueHigh,satHigh,valueHigh))
    print(mask1.shape)
    cv2.imshow('Mask 1', mask1)
    # mask2 = cv2.bitwise_not(mask1)
    # cv2.imshow('Mask 2', mask2)

    Contours, no_use = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(img,Contours,-1, (0,0,255),3 )

    for cont in Contours:
        area = cv2.contourArea(cont)
        (x,y,w,h) = cv2.boundingRect(cont)
        if area > 100:
            # cv2.drawContours(img, [cont], -1, (0, 0, 255), 3)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

    # cv2.imshow('MBS3523', imgHSV)
    cv2.imshow('MBS3523', img)
    if cv2.waitKey(5) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()