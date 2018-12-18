import cv2 

video = cv2.VideoCapture(0)

while True:
    conectado, frame = video.read()
    
    cv2.imshow('video', frame)
    
    if cv2.waitkey(1) == ord('q'):
        break
        
video.release()
cv2.destroyAllwindows