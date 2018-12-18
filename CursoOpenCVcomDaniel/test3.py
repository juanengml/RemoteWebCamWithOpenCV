import cv2

classificador = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('beatles.jpg')
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facedetectada = classificador.detectMultiScale(imagemcinza)

print(len(facedetectada))
