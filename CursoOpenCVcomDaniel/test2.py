import cv2

print(cv2.__version__)

imagem = cv2.imread('opencv-python.jpg')
cv2.imshow("Original", imagem)
cv2.waitKey()
