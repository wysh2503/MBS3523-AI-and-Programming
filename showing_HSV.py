import cv2
import numpy as np

img = np.zeros([180,256,3], dtype=np.uint8) # 180rows, 256columns

for row in range(0,180,1):
    for column in range(0,256,1):
        img[row, column] = (row, column, 255) # (hue, sat, value)
hue_sat = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

for row in range(0,180,1):
    for column in range(0,256,1):
        img[row, column] = (row, 255, column)
hue_val = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

while True:
    cv2.imshow('hue_sat',hue_sat)
    cv2.imshow('hue_val', hue_val)
    if cv2.waitKey(5) & 0xff == 27:
        break

cv2.destroyAllWindows()