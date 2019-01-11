import numpy as np 
import cv2 as cv

image = cv.imread("miojo.png",0) ## seleciona 

cv.imshow("Miojo ",image)
cv.waitKey(0)
cv.destroyAllWindows()


