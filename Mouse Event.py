import cv2 as cv
import numpy as np

def click_event(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN:
        font=cv.FONT_HERSHEY_SIMPLEX
        
        xy=str(x)+ ',' +str(y)
        cv.putText(img, xy, (x,y), font, 1, (255,0,0), 2)
        cv.imshow("img", img)
        
    if event==cv.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        
        font=cv.FONT_HERSHEY_SIMPLEX
        xy=str(blue)+ ',' +str(green)+ ',' +str(red)
        cv.putText(img, xy, (x,y), font, 1, (255,0,0), 2)
        cv.imshow("img", img)
        
img=cv.imread("infusing.jpg")
img=cv.resize(img, (412,412))
cv.imshow("img", img)

cv.setMouseCallback("img", click_event)
cv.waitKey(0)
cv.destroyAllWindows()