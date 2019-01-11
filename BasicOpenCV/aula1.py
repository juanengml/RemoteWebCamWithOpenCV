import numpy as np
import cv2 as cv

#image = cv.imread("gato.jpg",0)
image = cv.imread("miojo.png",0)

cv.imshow('image',image)


cv.waitKey(0)
cv.destroyAllWindows()

