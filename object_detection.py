import cv2
import numpy as np

def nothing(x):
    pass
cv2.namedWindow("Tracking")

cv2.createTrackbar("u_h","Tracking", 0, 255, nothing)
cv2.createTrackbar("u_s","Tracking", 0, 255, nothing)
cv2.createTrackbar("u_v","Tracking", 0, 255, nothing)
cv2.createTrackbar("l_h","Tracking", 255, 255, nothing)
cv2.createTrackbar("l_s","Tracking", 255, 255, nothing)
cv2.createTrackbar("l_v","Tracking", 255, 255, nothing)


while True:
    frame=cv2.imread("smarties.png")
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    u_h=cv2.getTrackbarPos("u_h","Tracking")
    u_s=cv2.getTrackbarPos("u_s","Tracking")
    u_v=cv2.getTrackbarPos("u_v","Tracking")
    l_h=cv2.getTrackbarPos("l_h","Tracking")
    l_s=cv2.getTrackbarPos("l_s","Tracking")
    l_v=cv2.getTrackbarPos("l_v","Tracking")

    # u_b=np.array([165,0,0])
    # l_b=np.array([255,255,85])
    u_b=np.array([u_h,u_s,u_v])
    l_b=np.array([l_h,l_s,l_v])

    mask=cv2.inRange(frame,u_b,l_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("image",frame)
    cv2.imshow("result",res)

    k=cv2.waitKey(1)

    if k==27:
        break
cv2.destroyAllWindows()