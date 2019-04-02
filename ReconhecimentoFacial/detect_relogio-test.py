import os 
import dlib
import cv2
import glob


detectorRelogio = dlib.simple_object_detector("./recursos/detector_relogios.svm")
for imagem in glob.glob(os.path.join("relogios_teste2","*.jpg")):
	img = cv2.imread(imagem)
	objetosDetectados = detectorRelogio(img,2)
	for d in objetosDetectados:
		e , t ,d , b  = (int(d.left()),int(d.top()),int(d.right()),int(d.bottom()))
		cv2.rectangle(img,(e,t),(d,b),(0,0,255),2 )	
	cv2.imshow("Decter Relogius", img)	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

