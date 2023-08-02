'''
dilation
erosion
opening
closing

'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("smarties.png", 0)
_,thresh=cv2.threshold(img, 220,255, cv2.THRESH_BINARY_INV)

kernal=np.ones((2,2),np.uint8)
dilate=cv2.dilate(thresh,kernal,iterations=3)
erosion=cv2.erode(thresh,kernal,iterations=3)
opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernal)
closing=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernal)
GRADIENT=cv2.morphologyEx(thresh,cv2.MORPH_GRADIENT,kernal)

titles=["image","thresh","dilate","erode","opening","CLOSING","gradient"]
images=[img,thresh,dilate,erosion,opening,closing,GRADIENT]

for i in range(7):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
