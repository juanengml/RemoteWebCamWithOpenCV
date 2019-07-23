# -*- coding: utf-8 -*-
import cv2
import os
import paho.mqtt.client as mqtt
from os import system

def classifer(gray):
   faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50),        
        )
   return faces



def face_DETECT(faces,frame,text):
    x = 0
    y = 0
    font=cv2.FONT_HERSHEY_SIMPLEX
    if len(faces) >= 1:
     print ("Face detect")
     cv2.putText(img = frame, text = 'Face found:' + str(len(faces)), org=(50,50), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0, 0, 255))
     for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 100), 2)
        cv2.imwrite('face.jpg', frame)
    else:
        print ("Not face ")
        cv2.imwrite('face.jpg', frame)
    # DISPLAY THE RESULTING FRAME0
    cv2.imshow(text, frame)
    print (x,y)
    print( "\n")
    
    cv2.putText(faces,'x,y',(x,y),font, 2,(255,255,255),1)
    

def classifer_human(gray):
   faces = humanCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(75, 75),        
        )
   return faces



def human_DETECT(faces,frame,text):
    x = 0
    y = 0
    font=cv2.FONT_HERSHEY_SIMPLEX
    if len(faces) >= 1:
     print ("Human detect")
     cv2.putText(img = frame, text = 'Body found:' + str(len(faces)), org=(50,50), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0, 0, 255))
     for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 100), 1)
        cv2.imwrite('face.jpg', frame)
    else:
        print ("Not Human ")
        cv2.imwrite('face.jpg', frame)
    # DISPLAY THE RESULTING FRAME0
    cv2.imshow(text, frame)
    print (x,y)
    print( "\n")
    
    cv2.putText(faces,'x,y',(x,y),font, 2,(255,255,255),1)
    
def save_data(face0,human0):
    data =  [len(face0) <= 0,len(human0) <= 0 ]
    print (data)
    if data[0] == True and data[1] == True:
     system("echo  '%s %s %s' > data.txt;cat data.txt" % (len(face0),len(human0), 0 ))
    if data[0] == True and data[1] == False:
     system("echo  '%s %s %s' > data.txt;cat data.txt" % (len(face0),len(human0), 1 ))
    if data[0] == False and data[1] == True:
     system("echo  '%s %s %s' > data.txt;cat data.txt" % (len(face0),len(human0), 1 ))
    if data[0] == False and data[1] == False:
     system("echo  '%s %s %s' > data.txt;cat data.txt" % (len(face0),len(human0), 1 )) 

x=0
y=0

cascPath = "cascades/haarcascade_frontalface_default.xml"
cascPath2 = "haarcascade_fullbody.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
humanCascade = cv2.CascadeClassifier(cascPath2)
font=cv2.FONT_HERSHEY_SIMPLEX

cam0 = cv2.VideoCapture(0)
#cam1 = cv2.VideoCapture(1)
#cam2 = cv2.VideoCapture(2)

while True:
    # CAPTURE FRAME0-BY-FRAME0
    ret0, frame0 = cam0.read()
#    ret1, frame1 = cam1.read()
#    ret2, frame2 = cam2.read()

    gray0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
#    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
#    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    face0 = classifer(gray0)
    human0 = classifer_human(gray0)
    data =  ([len(human0) <= 0,len(face0) <= 0 ])
    
#    faces1 = classifer(gray1)
#    faces2 = classifer(gray2)

    # DRAW A RECTANGLE AROUND THE FACES FOUND
    save_data(face0,human0)
    human_DETECT(human0,frame0,"video0")
    face_DETECT(face0,frame0,"video0")


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
