import cv2 as cv
import numpy as np

video=cv.VideoCapture(0)

while True:
    ret, frame=video.read()
    
    if cv.waitKey(1) & 0xFF==ord('s'):
        break 
    cv.imshow("frame", frame)
    
video.release()
cv.destroyAllWindows()