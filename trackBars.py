import cv2


def nothing(x):
    pass


cam = cv2.VideoCapture(0)
width, height = (640, 480)
cv2.namedWindow('frame')
cv2.createTrackbar("xVal", "frame", 20, width, nothing)
cv2.createTrackbar("yVal", "frame", 20, height, nothing)
cv2.createTrackbar("raDius", "frame", 20, 240, nothing)

while True:
    ret, frame = cam.read()
    frame = cv2.resize(frame, (width, height))
    frame = cv2.flip(frame, 1)

    xVal = cv2.getTrackbarPos('xVal', 'frame')
    yVal = cv2.getTrackbarPos('yVal', 'frame')
    raDius = cv2.getTrackbarPos('raDius', 'frame')
    frame = cv2.circle(frame, (xVal, yVal), raDius, (200, 50, 100), 2)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
