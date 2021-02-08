# Save file as OpenCV-5-Text-on-image.py

import cv2
print(cv2.__version__)

# read the image Lena.png and save into img
img = cv2.imread('Resources/lena.png')
# resize the image - img.shape[0] is the height, img.shape[1] is the width
img = cv2.resize(img, (int(img.shape[1]/1.5),int(img.shape[0]/1.5)))

# Select font
font = cv2.FONT_HERSHEY_SIMPLEX
# Put a white text "Lena" on img
cv2.putText(img,'Lena',(10,300), font, 4,(255,255,255),2,cv2.LINE_AA)

# Show the resized image and grayscale image onto two windows
cv2.imshow('Lena',img)

# wait for any key input to terminate the program
cv2.waitKey(0)