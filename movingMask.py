import cv2
# import numpy as np
cam = cv2.VideoCapture(0)
width, height = (640, 480)
cvLogo = cv2.imread('cv.jpg')
cvLogo = cv2.resize(cvLogo, (50, 50))
cvLogoGray = cv2.cvtColor(cvLogo, cv2.COLOR_BGR2GRAY)
cv2.imshow('logo', cvLogo)
cv2.moveWindow('logo', 640, 0)

_, BGMask = cv2.threshold(cvLogoGray, 225, 255, cv2.THRESH_BINARY)
cv2.imshow('BG Mask', BGMask)
cv2.moveWindow('BG Mask', 740, 0)

FGM = cv2.bitwise_not(BGMask)

FGMask = cv2.bitwise_and(cvLogo, cvLogo, mask=FGM)

centroid = [500, 300]
x = 1
y = 1
speed = 2
rectW = 30
while True:
    ret, frame = cam.read()
    frame = cv2.resize(frame, (width, height))
    frame = cv2.flip(frame, 1)

    frameTmp = frame[centroid[1]-25:centroid[1] +
                     25, centroid[0]-25:centroid[0]+25]
    BG = cv2.bitwise_and(frameTmp, frameTmp, mask=BGMask)
    FG = cv2.add(BG, FGMask)
    frame[centroid[1]-25:centroid[1]+25, centroid[0]-25:centroid[0]+25] = FG

    if centroid[0] >= width-rectW:
        x = -1
    if centroid[0] <= rectW:
        x = 1
    if centroid[1] >= height-rectW:
        y = -1
    if centroid[1] <= rectW:
        y = 1

    centroid[0] += x*speed
    centroid[1] += y*speed

    cv2.imshow("frame", frame)
    cv2.moveWindow("frame", 0, 0)
    cv2.imshow("BG", BG)
    cv2.moveWindow("BG", 840, 0)
    cv2.imshow("FG", FG)
    cv2.moveWindow("FG", 840, 100)

    if cv2.waitKey(1) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
