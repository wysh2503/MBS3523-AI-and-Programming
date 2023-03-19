import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

# t_old = 0
# t_new = 0

colorDots = mp_drawing.DrawingSpec(color=(80,110,10), thickness=3, circle_radius=1)
colorConnects = mp_drawing.DrawingSpec(color=(80,256,121), thickness=3, circle_radius=1)

# Initiate holistic model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while True:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Process holistic Detections
        results = holistic.process(imgRGB)
        # print(results.face_landmarks)

        # face_landmarks, pose_landmarks, left_hand_landmarks, right_hand_landmarks

        # Draw face landmarks
        mp_drawing.draw_landmarks(img, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS,
                                  landmark_drawing_spec=(colorDots),
                                  connection_drawing_spec=(colorConnects))

        # Right hand
        mp_drawing.draw_landmarks(img, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        # Left Hand
        mp_drawing.draw_landmarks(img, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        # Pose Detections
        mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        # t_new = time.time()
        # fps = 1 / (t_new - t_old)
        # t_old = t_new
        #
        # cv2.putText(img, 'FPS = ' + str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
        #             (255, 0, 255), 3)

        cv2.imshow('Webcam', img)

        if cv2.waitKey(1) == 27:
            break

cap.release()
cv2.destroyAllWindows()