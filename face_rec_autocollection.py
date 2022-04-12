import cv2
import os

cam = cv2.VideoCapture(0)

facedetect = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

count = 0

nameID = str(input("Enter Your Name: ")).lower()

path = 'images/' + nameID

if os.path.exists(path):
    print("Name Already Taken")
    nameID = str(input("Enter Your Name Again: "))
else:
    os.makedirs(path)

while True:
    ret, img = cam.read()
    faces=facedetect.detectMultiScale(img, 1.1, 5)
    for x,y,w,h in faces:
        count=count+1
        name = './images/'+nameID+'/' + str(count) + '.jpg'
        print("Creating Images........." + name)
        cv2.imwrite(name, img[y:y+h,x:x+w])
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
    cv2.imshow("Webcam Image", img)
    cv2.waitKey(1)
    if count > 500:
        break

cam.release()
cv2.destroyAllWindows()