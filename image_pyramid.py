import cv2
import numpy as np

img=cv2.imread("infusing.jpg")
img=cv2.resize(img, (512,512))

layer=img.copy()
gp=[layer]

for i in range(5):
    layer=cv2.pyrDown(layer)
    gp.append(layer)

for i in range(5,0,-1):
    gaussian_expanded=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1],gaussian_expanded)
    cv2.imshow(str(i), laplacian)

cv2.imshow("Original_image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
