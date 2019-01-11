import numpy as np 
import cv2 

stream = cv2.VideoCapture(0)

while (stream.isOpened()):
	 ret, frame = stream.read()
	 cv2.imshow("Imagem stream webcam", frame)
	 if cv2.waitKey(1) & 0xFF == ord('q'):
	 	break

stream.release()
cv2.destroyAllWindows()	 