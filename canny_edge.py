import cv2
import numpy as np

# Canny edge detection method

img=cv2.imread("infusing.jpg")
img=cv2.resize(img,(300,300))

edges=cv2.Canny(img, 50, 200)
edges=cv2.resize(edges,(300,300))

while True:
    cv2.imshow("img",img)
    cv2.imshow('res',edges)

    k=cv2.waitKey(1)

    if k==27:
        break

cv2.destroyAllWindows()