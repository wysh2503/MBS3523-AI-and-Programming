# Save this file to your Github as OpenCV-12-ImageProcessing2.py

import cv2
print(cv2.__version__)
import numpy as np

img = cv2.imread('Resources/lena.png')
# resize the image - img.shape[0] is the height, img.shape[1] is the width
img = cv2.resize(img, (int(img.shape[1]/1.5),int(img.shape[0]/1.5)))
# convert the BGR image to Grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

roi = img[120:260, 120:260].copy()
roiGray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
roiGray = cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)
img[120:260, 120:260] = roiGray

# Show the resized image and grayscale image onto two windows
cv2.imshow('Lena',img)
cv2.imshow('Gray Image', imgGray)
cv2.imshow('ROI Image', roi)
cv2.imshow('Gray ROI', roiGray)

# wait for any key input to terminate the program
cv2.waitKey(0)