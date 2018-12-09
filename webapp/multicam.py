# -*- coding: utf-8 -*-
import cv2
import os
import paho.mqtt.client as mqtt
import threading

client = mqtt.Client()
client.connect("192.168.100.3", 1883)

def StartServer(port):
   print os.popen("python -m SimpleHTTPServer %s " % port).read()

t = threading.Thread(target=StartServer,args=(5000,))
t.start()

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
     print "Face detect"
     client.publish("home/sala/porta/01/status/"," 1 ")
     for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 100), 1)
        stringxy="+%s,%s"%(x,y) 
        cv2.putText(frame, stringxy, (x+w/2,y+h/2), font, 1,(0,0,255),1)
        cv2.imwrite('face.jpg', frame)
    else:
        print "Not face "
        client.publish("home/sala/porta/01/status/"," 0 ")
        cv2.imwrite('face.jpg', frame)
    # DISPLAY THE RESULTING FRAME0
    cv2.imshow(text, frame)
    print x,y,
    print"\n"
    
    cv2.putText(faces,'x,y',(x,y),font, 2,(255,255,255),1)
    



x=0
y=0

cascPath = "cascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
font=cv2.FONT_HERSHEY_SIMPLEX

cam0 = cv2.VideoCapture(0)
#cam1 = cv2.VideoCapture(1)
#cam2 = cv2.VideoCapture(2)

while True and t.isAlive():
    # CAPTURE FRAME0-BY-FRAME0
    ret0, frame0 = cam0.read()
#    ret1, frame1 = cam1.read()
#    ret2, frame2 = cam2.read()

    gray0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
#    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
#    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    face0 = classifer(gray0)
#    faces1 = classifer(gray1)
#    faces2 = classifer(gray2)

    # DRAW A RECTANGLE AROUND THE FACES FOUND
    face_DETECT(face0,frame0,"video0")


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()