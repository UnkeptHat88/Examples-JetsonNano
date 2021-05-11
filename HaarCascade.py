import cv2
# import numpy as np
cam = cv2.VideoCapture(0)
width, height = (640, 480)
face_cascade = cv2.CascadeClassifier(
    'cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

while True:
    ret, frame = cam.read()
    frame = cv2.resize(frame, (width, height))
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (x, y, w, h) in eyes:
            cv2.rectangle(roi_color, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("frame", frame)
    cv2.moveWindow("frame", 0, 0)
    if cv2.waitKey(1) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
