import math
import time
import os
from gtts import gTTS
from playsound import playsound
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
cap = cv2.VideoCapture(0)
detector=HandDetector(maxHands=1)
classifier=Classifier("Trained Model/keras_model.h5","Trained Model/labels.txt")
labels =["A","B"]
language = 'en'
while True:
    success, img = cap.read()
    imgOutput = img.copy()    #we make this copy of the img as to customize the boundary box
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
            prediction,index = classifier.getPrediction(imgWhite,draw=False)
            print(prediction,index)


            # for width is larger than height

        else:
            k = 300 / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop,(300, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((300 - hCal) / 2)
            imgWhite[hGap:hCal + hGap,:] = imgResize
            prediction,index = classifier.getPrediction(imgWhite,draw=False)

        cv2.rectangle(imgOutput,(x-25,y-75),(x-25+100,y-25),(255,0,0),cv2.FILLED)
        cv2.putText(imgOutput,labels[index],(x,y-30),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),2)
        cv2.rectangle(imgOutput,(x-25,y-25),(x+w+25,y+h+25),(255,0,0),4)
        cv2.imshow("ImageCrop",imgCrop)
        cv2.imshow("ImageWhite",imgWhite)


        # # Create the text to be spoken
        # prediction_text = labels[index]
        #
        # # Create a speech object from text to be spoken
        # speech_object = gTTS(text=prediction_text, lang=language, slow=False)
        #
        # # Save the speech object in a file called 'prediction.mp3'
        # speech_object.save("prediction.mp3")
        #
        # # Playing the speech using mpg321
        # playsound("prediction.mp3")

    cv2.imshow("Image",imgOutput)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
