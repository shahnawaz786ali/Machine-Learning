import cv2 as cv

img=cv.imread("infusing.jpg")

cv.imshow("img", img)

cv.waitKey(0)
cv.destroyAllWindows()