import cv2 as cv
import numpy as np
import datetime

img=cv.imread("infusing.jpg")

img=cv.resize(img, (412,412))


while True:
    datet=str(datetime.datetime.now())
    font=cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, datet, (-200,300),font, 1, (0,0,255), 1)

    cv.imshow("img", img)
    k=cv.waitKey(1)& 0xff
    
    if k == 27:
        break
    
cv.destroyAllWindows()