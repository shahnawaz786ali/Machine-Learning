import cv2
import numpy as np

img=cv2.imread("infusing.jpg")
img=cv2.resize(img, (412,412))
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh=cv2.threshold(gray, 127, 255, 0)
contours,hierarchy=cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Numbers of contours:", str(len(contours)))

cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow("image",img)
cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()