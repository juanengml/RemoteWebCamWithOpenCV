import numpy as np 
import cv2

#video = cv2.VideoCapture(0)
video = cv2.VideoCapture("simulacao.mp4")

while (video.isOpened()):
	ret, imagem = video.read()
	cv2.imshow("Me", imagem)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


video.release()
cv2.destroyAllWindows()		