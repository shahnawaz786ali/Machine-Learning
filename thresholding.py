import cv2 as cv
import numpy as np

img=cv.imread("infusing.jpg")

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img=cv.resize(img, (512,512))

ret,thr1=cv.threshold(img, 140, 255, cv.THRESH_BINARY)
ret,thr2=cv.threshold(img, 140, 255, cv.THRESH_BINARY_INV)
ret,thr3=cv.threshold(img, 210, 255, cv.THRESH_TOZERO)
ret,thr4=cv.threshold(img, 210, 255, cv.THRESH_TOZERO_INV)
ret,thr5=cv.threshold(img, 210, 255, cv.THRESH_TRUNC)

cv.imshow("img", img)
cv.imshow("thr1", thr1)
cv.imshow("thr2", thr2)
cv.imshow("thr3", thr3)
cv.imshow("thr4", thr4)
cv.imshow("thr5", thr5)

cv.waitKey(0)
cv.destroyAllWindows()