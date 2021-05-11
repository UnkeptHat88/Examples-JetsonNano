import cv2
import numpy as np
cam = cv2.VideoCapture(0)
width,height = (320,240)
cvLogo = cv2.imread('cv.jpg')
cvLogo = cv2.resize(cvLogo,(width,height))
cvLogoGray = cv2.cvtColor(cvLogo,cv2.COLOR_BGR2GRAY)
cv2.imshow('logo',cvLogo)
cv2.moveWindow('logo',0,240)

_,BGMask = cv2.threshold(cvLogoGray,225,255,cv2.THRESH_BINARY)
cv2.imshow('BG Mask',BGMask)
cv2.moveWindow('BG Mask',320,0)

FGM = cv2.bitwise_not(BGMask)
cv2.imshow('FG M',FGM)
cv2.moveWindow("FG M",640,0)

FG = cv2.bitwise_and(cvLogo,cvLogo,mask=FGM)
cv2.imshow("FG",FG)
cv2.moveWindow('FG',640,240)


while True:
    ret, frame = cam.read()
    frame = cv2.resize(frame,(width,height))
    frame = cv2.flip(frame,1)

    BG = cv2.bitwise_and(frame,frame,mask=BGMask)
    compositeImage = cv2.add(BG,FG)
    Blended = cv2.addWeighted(frame,1,FG,.5,0)

    cv2.imshow("frame",frame)
    cv2.moveWindow("frame",0,0)
    cv2.imshow("BG",BG)
    cv2.moveWindow("BG",320,240)
    cv2.imshow("composite",compositeImage)
    cv2.moveWindow("composite",960,240)
    cv2.imshow("Blended",Blended)
    cv2.moveWindow("Blended",960,0)

    if cv2.waitKey(1)==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()