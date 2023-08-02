'''
Image smoothening/ image blurring
homogeneous
gaussian
median
bilateral
'''
import matplotlib.pyplot as plt
import numpy as np
import cv2

img=cv2.imread("infusing.jpg")
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernal=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-1, kernal)
blur=cv2.blur(img, (5,5))
gblur=cv2.GaussianBlur(img,(5,5), 0)
median=cv2.medianBlur(img, 5)
bilateral=cv2.bilateralFilter(img, 9, 75,75)

images=[img,dst,blur,gblur,median,bilateral]
titles=["original_image","2D convolution","blur","gaussian","median","bilateral"]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.title(titles[i])
    plt.imshow(images[i],"gray")
    plt.xticks([]), plt.yticks([])

plt.show()