# Save this file as OpenCV-1-Read.py

import cv2
print(cv2.__version__)

# read the image Lena.png and save into img
img = cv2.imread('Resources/lena.png')
# resize the image - img.shape[0] is the height, img.shape[1] is the width
img = cv2.resize(img, (int(img.shape[1]/1.5),int(img.shape[0]/1.5)))
# convert the BGR image to Grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Show the resized image and grayscale image onto two windows
cv2.imshow('Lena',img)
cv2.imshow('Gray Image', imgGray)

# wait for any key input to terminate the program
cv2.waitKey(0)