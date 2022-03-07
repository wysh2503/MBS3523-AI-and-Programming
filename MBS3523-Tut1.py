# Answer to Tutorial 1
import cv2
import numpy as np
import time

img = np.zeros((8,12,3),dtype=np.uint8)
img[:,:] = 255

# Answer to T1-Q1
img[2,3] = (0,0,255) # ONE Red pixel at R2C3; BGR
# Answer to T1-Q2
img[:,11:12] = (0,255,0) # One green line at rightmost column
# Answer to T1-Q3
img[4:7,6:9] = (255,0,0) # Blue square R4-6 C6-8

cv2.imshow('img',img)
cv2.waitKey(5000)


# Answer to T1-Q4
img[2,3] = (0,255,0) # replace the red pixel by a green pixel
# Answer to T1-Q5
img[:,11:12] = (0,0,255) # replace the green line by a red line
# Answer to T1-Q6
img[4:7,6:9] = (0,255,0) # replace the blue square by a green square


cv2.imshow('img',img)
cv2.waitKey(5000)
