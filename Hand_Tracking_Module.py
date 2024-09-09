import os
import cv2
import mediapipe as mp


class Hand_Dection():

    def __init__(self,mode = False,maxHands = 2,DetectionConfidence = 0.5,Trackconfidence = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.DetectionConfidence = DetectionConfidence
        self.TrackConfidence = Trackconfidence

        # fancy stuff
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.DetectionConfidence,
            min_tracking_confidence=self.TrackConfidence
        )
        self.mpDraw = mp.solutions.drawing_utils

    def detect_hands(self,frame,draw = True):
        imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for handslms in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame,handslms,self.mpHands.HAND_CONNECTIONS)
        return frame
    
    def FPS_Counter(self, frame, starttime, endtime):
        # Calculate FPS
        fps = 1 / (starttime - endtime)
        cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_DUPLEX, 3, (120, 65, 134), 3)

def main():
    capture = cv2.VideoCapture(0)
    detect = Hand_Dection()

    starttime = 0
    endtime = 0

    while True:
        if not capture.isOpened():
            print("<<<<<<<<<-------------------------------->>>>>>>>>")
            print("camera not found")
            break
        else:
            Success,frame = capture.read()
            frame = detect.detect_hands(frame,True)

            if Success:
                # Update FPS counters
                starttime = os.times()[4] 
                detect.FPS_Counter(frame, starttime, endtime)
                endtime = starttime
                cv2.imshow("camera",frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    break
            else:
                print("frame not found")
                break

if __name__ == "__main__":
    main()