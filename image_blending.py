import numpy as np
import cv2

orange=cv2.imread("orange.jpg")
orange=cv2.resize(orange, (512,512))
apple=cv2.imread("aple.jpg")
apple=cv2.resize(apple, (512,512))

# print(orange.shape)
# print(apple.shape)
apple_orange=np.hstack((apple[:, :256],orange[:, 256:]))

#generate gaussian pyramid of apple
apple_copy=apple.copy()
gp_apple=[apple_copy]

for i in range(6):
    apple_copy=cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

#generate gaussian pyramid of orange
orange_copy=orange.copy()
gp_orange=[orange_copy]

for i in range(6):
    orange_copy=cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)


#laplacian oyramid of apple
apple_copy=gp_apple[5]
lp_apple=[apple_copy]

for i in range(5,0,-1):
    gaussian_expanded=cv2.pyrUp(gp_apple[i])
    laplacian=cv2.subtract(gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)

#laplacian oyramid of orange
orange_copy=gp_orange[5]
lp_orange=[orange_copy]

for i in range(5,0,-1):
    gaussian_expanded=cv2.pyrUp(gp_orange[i])
    laplacian=cv2.subtract(gp_orange[i-1], gaussian_expanded)
    lp_orange.append(laplacian)

#now add left and right half of umages in each level

apple_orange_pyramid=[]
n=0

for apple_lp, orange_lp in zip(lp_apple, lp_orange):
    n=n+1
    cols,rows,ch=apple_lp.shape
    laplacian=np.hstack((apple_lp[:, 0:int(cols/2)], orange_lp[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

#reconstruct
apple_orange_reconstruct=apple_orange_pyramid[0]
for i in range(1,6):
    aple_orange_reconstruct=cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct=cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow("apple",apple)
cv2.imshow("orange",orange)
cv2.imshow("orange_apple",apple_orange)
cv2.imshow("reconstruct", apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()
