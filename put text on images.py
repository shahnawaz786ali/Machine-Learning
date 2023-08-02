import cv2 as cv
import numpy as np

img=np.zeros((512,512,3), np.uint8)

font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,"openCV" ,(50,350), font, 3, (255,0,0), 15)
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
