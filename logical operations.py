import cv2
import numpy as np

img1=np.zeros((412,412,3),np.uint8)
img1=cv2.rectangle(img1, (200,0), (300,100), (255,255,255), cv2.FILLED)
img2=cv2.imread("images.png")
img2=cv2.resize(img2,(412,412))
res1=cv2.bitwise_and(img1,img2,mask=None)
res2=cv2.bitwise_or(img1,img2,mask=None)
res3=cv2.bitwise_xor(img1,img2,mask=None)

while True:

    cv2.imshow("image1",img1)
    cv2.imshow("image2",img2)
    cv2.imshow("result1",res1)
    cv2.imshow("result2",res2)
    cv2.imshow("result3",res3)

    k=cv2.waitKey(1)

    if k==27:
        break
cv2.destroyAllWindows()