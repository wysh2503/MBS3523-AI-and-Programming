# import tensorflow as tf
# from tensorflow import keras
import cv2
import mediapipe as mp
from keras.models import load_model
import numpy as np
import time

detectFace = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.6)

cam = cv2.VideoCapture(0)
cam.set(3, 1280)
cam.set(4, 720)
font = cv2.FONT_HERSHEY_COMPLEX

model = load_model('keras_model.h5')

# variables for FPS
t_old = 0
t_new = 0

def get_className(classNo):
    if classNo == 0:
        return "wyeung"
    elif classNo == 1:
        return "TonyStark"
    elif classNo == 2:
        return "Lilian"


while True:
    ret, img = cam.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = detectFace.process(imgRGB)
    # print(results.detections)
    if results.detections != None:
        for face in results.detections:
            # drawFace.draw_detection(img, face)
            boundingBox = face.location_data.relative_bounding_box
            x1 = int(boundingBox.xmin * 1280)
            y1 = int(boundingBox.ymin * 720)
            x2 = int((boundingBox.xmin + boundingBox.width) * 1280)
            y2 = int((boundingBox.ymin + boundingBox.height) * 720)
            pt1 = (x1, y1)
            pt2 = (x2,y2)
            cv2.rectangle(img, pt1, pt2, (255, 0, 0), 3)
            crop_img = img[y1:y2, x1:x2]
            imgResize = cv2.resize(crop_img, (224, 224))
            imgReshape = imgResize.reshape(1, 224, 224, 3)
            prediction = model.predict(imgReshape)
            print(prediction)
            classIndex = np.argmax(prediction)
            print(classIndex)
            probabilityValue = np.amax(prediction)
            # print(probabilityValue)

        if classIndex == 0 or 1 or 2:
            cv2.rectangle(img, (x1, y1), (x2, y2), (80, 255, 0), 2)
            cv2.rectangle(img, (x1, y1 - 40), (x2, y1), (80, 255, 0), -2)
            cv2.putText(img, str(get_className(classIndex)), (x1, y1 - 10), font, 0.75, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(img, str(round(probabilityValue * 100, 2)) + "%", (10, 110), font, 1.5, (255, 0, 0), 2,
                    cv2.LINE_AA)

    # Calculate FPS and display on upper left
    t_new = time.time()
    fps = 1 / (t_new - t_old)
    t_old = t_new
    cv2.putText(img, 'FPS = ' + str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Face Recognition Result", img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()
