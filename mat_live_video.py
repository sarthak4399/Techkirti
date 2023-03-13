#/bin/sh:python
import cv2
import numpy   as np 
import os 
import time 
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    low_b = np.uint8([5,5,5])
    high_b = np.uint8([0,0,0])
    mask = cv2.inRange(frame,)
    contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
    length =len(contours)

    if  length >0:
        c = max (contours,key=cv2.contourArea)
        M = cv2.moments(c)
    cv2.drawContours(frame, contours, -1, (0,255,0), 1)
    cv2.imshow("Mask",mask)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
   
