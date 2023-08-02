import cv2 as cv

img=cv.imread("infusing.jpg")

cv.line(img, (0,0), (250,250), (255,0,0),10)
cv.rectangle(img, (50,50), (200,200), (0,0,255), -1)
cv.circle(img, (300,300), 50, (0,255,255), -1)
cv.arrowedLine(img, (30,30), (70,70), (255,255,0), 10)

cv.imshow("img", img)

cv.waitKey(0)
cv.destroyAllWindows()