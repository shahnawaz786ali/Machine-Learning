import cv2 as cv
import numpy as np

def click_event(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN:
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]
        
        colorimg=np.zeros((512,512,3), np.uint8)
        colorimg[:]=[b,g,r]
        
        cv.imshow("color", colorimg)
        
#img=np.zeros((512,512), np.uint8)
img=cv.imread("infusing.jpg")

cv.imshow("img", img)
points=[]
cv.setMouseCallback("img", click_event)
cv.waitKey(0)
cv.destroyAllWindows()
    

