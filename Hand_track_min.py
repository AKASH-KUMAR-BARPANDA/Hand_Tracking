import time
import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

# fancy stuff
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

##FPS
starttime = 0
endtime = 0


while True:
    if not cap.isOpened():
        print("<<<<<<<<<-------------------------------->>>>>>>>>")
        print("camera not found")
        break
    else:
        Success,frame = cap.read()
        imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
       # print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for handslms in results.multi_hand_landmarks:
                for id, lm in enumerate(handslms.landmark):
                    # print(id,lm)
                    h, w, c = frame.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    print(id, cx ,cy)
                    # track each point
                    if id==12:
                        cv2.circle(frame,(cx,cy),15,(0,255,0),cv2.FILLED)

                mpDraw.draw_landmarks(frame,handslms,mpHands.HAND_CONNECTIONS)


        # fps config
        starttime = time.time()
        fps = 1/(starttime-endtime)
        endtime = starttime

        cv2.putText(frame,str(int(fps)),(10,70), cv2.FONT_HERSHEY_DUPLEX,3,(120,65,134),3)

        if Success:
            cv2.imshow("camera",frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            print("frame not found")
            break