# Save the file as OpenCV-Ex1-Draw.py

import cv2
print(cv2.__version__)
import numpy as np

# create a black image of 500x500 pixels
img = np.zeros((500,500,3), np.uint8)
img = cv2.rectangle(img,(0,0),(500,500),(0,255,0),-1)

# Draw a horizontal red line with thickness of 5 px
img = cv2.line(img,(0,250),(500,250),(0,0,255),5)
# Draw a vertical red line with thickness of 5 px
img = cv2.line(img,(250,0),(250,500),(0,0,255),5)

# Draw a rectangle - top-left corner at (125,125) and
# bottom-right corner at (375,375), color: magenta, line thickness 3 px
img = cv2.rectangle(img,(125,125),(375,375),(255,0,255),3)

# Draw 4 circles of diameter 25, centers at 4 corners, line thickness 2 px
img = cv2.circle(img,(125,125), 25, (128,0,128), 2)
img = cv2.circle(img,(375,125), 25, (128,0,128), 2)
img = cv2.circle(img,(125,375), 25, (128,0,128), 2)
img = cv2.circle(img,(375,375), 25, (128,0,128), 2)

# Show everything on img
cv2.imshow('img',img)

cv2.waitKey(0)