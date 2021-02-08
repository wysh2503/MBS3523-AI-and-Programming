# Save this file as OpenCV-4-Draw.py

import cv2
print(cv2.__version__)
import numpy as np

# create a black image of 500x500 pixels
img = np.zeros((500,500,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(500,500),(255,0,0),5)

# Draw a circle of diameter 50, center at (400,100)
img = cv2.circle(img,(400,100), 50, (0,0,255), -1)

# Draw a rectangle - top-left corner and bottom-right corner of rectangle
img = cv2.rectangle(img,(250,0),(500,125),(0,255,0),3)

# Draw an ellipse: center, axis, angle, start angle, end angle, color, thickness
img = cv2.ellipse(img,(250,250),(100,50),0,0,180,(125,255,255),-1)

# Draw polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

cv2.imshow('img',img)

cv2.waitKey(0)