import cv2
import numpy as np

img = np.zeros([480,640,3], dtype=np.uint8)
img[:,:]= (125,125,125)

def nil(x):
    pass

cv2.namedWindow('MBS3523')

cv2.createTrackbar('RED','MBS3523',125,255,nil)
cv2.createTrackbar('GREEN','MBS3523',125,255,nil)
cv2.createTrackbar('BLUE','MBS3523',125,255,nil)

while True:
    red = cv2.getTrackbarPos('RED','MBS3523')
    green = cv2.getTrackbarPos('GREEN', 'MBS3523')
    blue = cv2.getTrackbarPos('BLUE', 'MBS3523')
    img[:,:] = (blue, green, red)
    cv2.imshow('MBS3523', img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()