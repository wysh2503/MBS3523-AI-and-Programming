# Save this file as OpenCV-7-Text-on-webcam.py

import cv2
#import numpy as np
print(cv2.__version__)

# you may need to change the number inside () to 0 1 or 2,
# depending on which webcam you are using
capture = cv2.VideoCapture(0)
# Below 2 lines are used to set the webcam window size
capture.set(3,640) # 3 is the width of the frame
capture.set(4,480) # 4 is the height of the frame

# Select font
font = cv2.FONT_HERSHEY_SIMPLEX

# Start capturing and show frames on window named 'Frame'
while True:
    success, img = capture.read()

    # Put a red text on img
    cv2.putText(img, 'Hello! I am Winston Yeung!', (20, 50), font, 1.3, (0, 255, 0), 2)

    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()