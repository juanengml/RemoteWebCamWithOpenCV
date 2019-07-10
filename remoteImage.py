import urllib
import cv2
import numpy as np 

url = "http://192.168.100.6:8080/shot.jpg"
imgResp =  urllib.urlopen(url)

x=0
y=0

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
font=cv2.FONT_HERSHEY_SIMPLEX



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
     for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 100), 1)
        stringxy="+%s,%s"%(x,y) 
        cv2.putText(frame, stringxy, (x+w/2,y+h/2), font, 1,(0,0,255),1)
        cv2.imwrite('face.jpg', frame)
    else:
        print "Not face "
        cv2.imwrite('face.jpg', frame)
    # DISPLAY THE RESULTING FRAME0
    #cv2.imshow(text, frame)
    print x,y,
    print"\n"
    
    #cv2.putText(faces,'x,y',(x,y),font, 2,(255,255,255),1)
    




while True:
    imgResp=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    frame0 = img
    gray0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
    face0 = classifer(gray0)
    face_DETECT(face0,frame0,"video0")
    #cv2.imshow('test',img)
    if ord('q')==cv2.waitKey(10):
        exit(0)

video_capture.release()
cv2.destroyAllWindows()