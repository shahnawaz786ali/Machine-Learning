import cv2 as cv
import numpy as np

def nothing(x):
    print(x)
img=cv.imread("infusing.jpg")

cv.namedWindow("Tracking")

cv.createTrackbar("b", "Tracking", 0, 255, nothing)
cv.createTrackbar("g", "Tracking", 0, 255, nothing)
cv.createTrackbar("r", "Tracking", 0, 255, nothing)
switch="0: OFF\n 1:ON"
cv.createTrackbar(switch, "Tracking", 0, 1, nothing)

while True:
    cv.imshow("img", img)
    k=cv.waitKey(1) & 0xff
    
    if k== 27:
        break
    
    b=cv.getTrackbarPos("b", "Tracking")
    g=cv.getTrackbarPos("g", "Tracking")
    r=cv.getTrackbarPos("r", "Tracking")
    s=cv.getTrackbarPos(switch, "Tracking")
    
    if s==0:
        img[:]= 0
    else:
        img[:]=b,g,r
    
cv.destroyAllWindows()