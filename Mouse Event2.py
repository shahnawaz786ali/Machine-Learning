import cv2 as cv
import numpy as np

def click_event(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), 3, (255,255,255), -1)
        points.append((x,y))
        
        if len(points)> 2:
            cv.line(img, points[-1], points[-2], (255,255,255), 4)

        cv.imshow("img", img)
        
img=np.zeros((512,512), np.uint8)

cv.imshow("img", img)
points=[]
cv.setMouseCallback("img", click_event)
cv.waitKey(0)
cv.destroyAllWindows()
    
