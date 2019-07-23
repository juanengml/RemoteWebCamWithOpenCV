# -*- coding: utf-8 -*-
import cv2
import sys
from os import system
#import paho.mqtt.client as mqtt

#client = mqtt.Client()
#client.connect("192.168.100.3", 1883)


x=0
y=0


#video_capture = cv2.VideoCapture(0)
video_capture = cv2.VideoCapture("2019-07-20-105528.webm")
total = 0
while True:
    # CAPTURE FRAME-BY-FRAME
    ret, frame = video_capture.read()    
    cv2.imwrite('people.jpg', frame)

    if  not ret:
    	break
    total = total + 1
    print (total)
    cv2.imwrite('data%s.jpg' % total, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
