import cv2
print(cv2.__version__)
webcam = cv2.VideoCapture(0)
while True:
    ret, image = webcam.read()
    cv2.imshow('HDAIR Year 1', image)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()
