import cv2
import numpy as np
cam = cv2.VideoCapture(0)
width,height = (640,480)
img1 = np.zeros((480,640,1),np.uint8)
img1[:,0:320,:]=[255]

img2 = np.zeros((480,640,1),np.uint8)
img2[150:330,200:440]=[255]

bitAnd = cv2.bitwise_and(img1,img2)
bitXor = cv2.bitwise_xor(img1,img2)

while True:
    ret, frame = cam.read()
    frame = cv2.resize(frame,(width,height))
    frame = cv2.flip(frame,1)


    frame2 = cv2.bitwise_and(frame,frame,mask=img1)


    cv2.imshow("frame",frame)
    cv2.moveWindow("frame",0,0)
    cv2.imshow("img1",img1)
    cv2.moveWindow("img1",640,0)
    cv2.imshow("img2",img2)
    cv2.moveWindow("img2",0,480)
    cv2.imshow("And",bitAnd)
    cv2.moveWindow("And",640,480)
    cv2.imshow("Xor",bitXor)
    cv2.moveWindow("Xor",1280,0)
    cv2.imshow("frame2",frame2)
    cv2.moveWindow("frame2",1280,480)
    if cv2.waitKey(1)==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()