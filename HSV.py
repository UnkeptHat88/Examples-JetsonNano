import cv2
import numpy as np
print(cv2.__version__)


def nothing(x):
    pass


cam = cv2.VideoCapture(0)
width, height = (640, 480)
# frame = cv2.imread("smarties.png")
# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

cv2.namedWindow('Trackbar')
cv2.moveWindow('Trackbar', 1500, 0)

cv2.createTrackbar('Hue-Low', 'Trackbar', 50, 179, nothing)
cv2.createTrackbar('Hue-High', 'Trackbar', 100, 179, nothing)

cv2.createTrackbar('Hue-Low2', 'Trackbar', 50, 179, nothing)
cv2.createTrackbar('Hue-High2', 'Trackbar', 100, 179, nothing)

cv2.createTrackbar('Sat-Low', 'Trackbar', 100, 255, nothing)
cv2.createTrackbar('Sat-High', 'Trackbar', 255, 255, nothing)

cv2.createTrackbar('Val-Low', 'Trackbar', 100, 255, nothing)
cv2.createTrackbar('Val-High', 'Trackbar', 255, 255, nothing)


def hsValue():
    global hueLow, hueLow2, hueHigh2, hueHigh, SatLow, SatHigh, ValLow, ValHigh
    hueLow = cv2.getTrackbarPos('Hue-Low', 'Trackbar')
    hueHigh = cv2.getTrackbarPos('Hue-High', 'Trackbar')

    hueLow2 = cv2.getTrackbarPos('Hue-Low2', 'Trackbar')
    hueHigh2 = cv2.getTrackbarPos('Hue-High2', 'Trackbar')

    SatLow = cv2.getTrackbarPos('Sat-Low', 'Trackbar')
    SatHigh = cv2.getTrackbarPos('Sat-High', 'Trackbar')

    ValLow = cv2.getTrackbarPos('Val-Low', 'Trackbar')
    ValHigh = cv2.getTrackbarPos('Val-High', 'Trackbar')


while True:
    ret, frame = cam.read()
    rame = cv2.resize(frame, (width, height))
    frame = cv2.flip(frame, 1)
    # frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hsValue()
    l_b = np.array([hueLow, SatLow, ValLow])
    h_b = np.array([hueHigh, SatHigh, ValHigh])

    l_b2 = np.array([hueLow2, SatLow, ValLow])
    h_b2 = np.array([hueHigh2, SatHigh, ValHigh])

    FGMask = cv2.inRange(hsv, l_b, h_b)
    FGMask2 = cv2.inRange(hsv, l_b2, h_b2)
    FGMaskComp = cv2.add(FGMask, FGMask2)
    FG = cv2.bitwise_and(frame, frame, mask=FGMaskComp)

    BGMask = cv2.bitwise_not(FGMaskComp)
    BG = cv2.bitwise_and(frame, frame, mask=BGMask)

    final = cv2.add(FG, cv2.cvtColor(BGMask, cv2.COLOR_GRAY2BGR))

    cv2.imshow("FGMaskComp", FGMaskComp)
    cv2.moveWindow('FGMaskComp', 420, 0)
    cv2.imshow("BGMask", BGMask)
    cv2.moveWindow('BGMask', 840, 0)
    cv2.imshow("FG", FG)
    cv2.moveWindow('FG', 0, 500)
    cv2.imshow("BG", BG)
    cv2.moveWindow('BG', 640, 500)
    cv2.imshow("frame", final)

    if cv2.waitKey(1) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
