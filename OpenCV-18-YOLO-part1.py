# Save this file to Github as OpenCV-18-OpenCV-18-YOLO-part1.py

import cv2
import numpy as np

# Create an empty list - classes[] and point the classesFile to 'coco80.names'
classesFile = 'coco80.names'
classes = []
# Load all classes in coco80.names into classes[]
with open(classesFile, 'r') as f:
    classes = f.read().splitlines()
    print(classes)
    print(len(classes))

cap = cv2.VideoCapture(1)

while True:
    success , img = cap.read()

    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()