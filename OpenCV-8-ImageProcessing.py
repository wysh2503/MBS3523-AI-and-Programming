# Save this file as OpenCV-8-ImageProcessing.py

import cv2
import numpy as np
print(cv2.__version__)

# using a 5x5 kernel
kernel = np.ones((5,5),np.uint8)

# Read image from Resources folder
img = cv2.imread('Resources/lena.png')

# Resizing the image
img = cv2.resize(img, (int(img.shape[1]/1.5),int(img.shape[0]/1.5)))

# Convert BGR image to Grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert Grayscale to Gaussian Blur
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 0)

# Convert BGR image to Canny edges
imgCanny = cv2.Canny(img, 100, 100)

# Convert Canny edges image to dilated image
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

# show different processed images on different windows
cv2.imshow('Lena',img)
cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur', imgBlur)
cv2.imshow('Canny', imgCanny)
cv2.imshow('Dilate', imgDilation)

# Wait for a key input from keyboard to terminate the program
cv2.waitKey(0)
