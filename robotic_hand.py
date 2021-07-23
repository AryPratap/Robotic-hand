import Hand_Tracking as htm
import cv2
import ser 

cap = cv2.VideoCapture(0)
detector = htm.hand_detector(maxHand=1, detectionCon= 0.7)
myserial = ser.SerialObject("COM6", 9600)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp()
        print(fingers)
        myserial.sendData(fingers)


            
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)