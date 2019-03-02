# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:35:55 2019

@author: 25806
"""

import cv2

#cascade_path = "./cascade/haarcascade_frontalcatface.xml"
cascade_path = "./cascade/cascade.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

img_path="./source/a.jpg"
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor= 1.15,
    minNeighbors=3,
    minSize=(20, 20),
    flags=cv2.CASCADE_SCALE_IMAGE
) 
for (x, y, w, h) in faces:
   cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
   cv2.putText(img,'Cat Face',(x,y-7), 3, 1.2, (0, 255, 0), 2, cv2.LINE_AA)


cv2.imshow('Cat?', img)
cv2.imwrite("./output/a.jpg", img)
c = cv2.waitKey(0)