import cv2 as cv
import numpy as np

def a(x):
    print(x)

cv.namedWindow("Tracking")

img=cv.imread("infusing.jpg")

img1=np.zeros((512,512,3),np.uint8)
img=cv.resize(img,(512,512))

addw=cv.addWeighted(img, 0.5,img1,0.1, 0)
cv.createTrackbar("a","Tracking", 0,255, a)
b=cv.getTrackbarPos("a","Tracking")
ret,th1=cv.threshold(img, b, 255, cv.THRESH_BINARY)
font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(addw, "SHAHNAWAZ", (300,300),font, 1, (0,0,255), 5)


while True:
    cv.imshow("addw",addw)
    cv.imshow("img", img)
    cv.imshow("th1", th1)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cv.destroyAllWindows()