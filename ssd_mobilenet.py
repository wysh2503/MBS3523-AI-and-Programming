import cv2
print(cv2.__version__)

thres = 0.6 # Threshold to detect object

# img = cv2.imread('Resources/cars.jpg')
cap = cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)
# cap.set(10,70)

classNames= []
classFile = 'coco91.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
# print(classNames)

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    success,img = cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=thres)
    print(classIds,bbox)

    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            print(classId)
            print(classNames[classId-1])
            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
            cv2.putText(img,str(round(confidence*100,2))+'%',(box[0]+120,box[1]+30), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)

    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()