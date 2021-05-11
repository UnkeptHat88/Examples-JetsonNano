import cv2
import numpy as np
cam = cv2.VideoCapture(0)
width,height = (640,480)

while True:
    ret, frame = cam.read()
    frame = cv2.resize(frame,(width,height))
    frame = cv2.flip(frame,1)

    #roi = frame[:,0:320,1].copy()
    #roiGray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    #frame[:,0:320] = cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)
    frame[:,:,2]=np.zeros((480,640),dtype=int)
    frame[:,:,0]=np.zeros((480,640),dtype=int)

    cv2.imshow("frame",frame)
    cv2.moveWindow("frame",0,0)
    #cv2.imshow("gray",roi)
    #cv2.moveWindow("gray",640,0)
    if cv2.waitKey(1)==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()