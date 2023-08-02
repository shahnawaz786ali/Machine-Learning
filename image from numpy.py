import cv2 as cv
import numpy as np

img=np.ones((512,512,3), np.uint8)

cv.imwrite("image.png", img)
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()