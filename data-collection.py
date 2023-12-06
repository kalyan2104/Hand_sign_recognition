import math
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import time
cap = cv2.VideoCapture(0)
count = 0
detector=HandDetector(maxHands=1)
while True:
    success, img = cap.read()
    hands, img=detector.findHands(img)
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']
        imgCrop=img[y-25:y+h+25,x-25:x+w+25]

        aspectRatio = h/w

        imgWhite = np.ones((300, 300, 3), np.uint8) * 255

        # for height is larger than width

        if aspectRatio > 1:
            k = 300/h
            wCal = math.ceil(k*w)
            imgResize=cv2.resize(imgCrop,(wCal,300))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((300-wCal)/2)
            imgWhite[:,wGap:wCal+wGap]=imgResize  #height,width are parameters

            # for width is larger than height

        else:
            k = 300 / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (300,hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((300 - hCal) / 2)
            imgWhite[hGap:hCal + hGap,:] = imgResize

        cv2.imshow("ImageCrop",imgCrop)
        cv2.imshow("ImageWhite",imgWhite)


    cv2.imshow("Image",img)
    key =  cv2.waitKey(1)
    if key == ord("s"):
        count +=1
        cv2.imshow(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print(count)

