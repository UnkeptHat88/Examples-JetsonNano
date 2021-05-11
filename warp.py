import cv2
import numpy as np
pts1 = []
def click_event(event, x, y, flags, params):
    global pts1
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        pts1.append([x,y])
  

img = cv2.imread('ped.jpg')
#print(type(img))


cv2.imshow("win",img)
cv2.setMouseCallback('win', click_event)
cv2.waitKey(0)
print(pts1)
for i in range(0,4):
    cv2.circle(img,(pts1[i][0],pts1[i][1]),5,(0,0,255),cv2.FILLED)
#cv2.imshow('win',img)
pts1=np.float32(pts1)
width,height=300,300
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow('out',imgOutput)
cv2.waitKey(0)