import cv2

cam = cv2.VideoCapture(0)
width,height = (640,480)
centroid = [500,300]
rectW = 20
x=1
y=1
speed = 3
while True:
    ret,frame=cam.read()
    frame = cv2.resize(frame,(width,height))
    frame = cv2.flip(frame,1)

    frame = cv2.rectangle(frame,(centroid[0]-rectW,centroid[1]-rectW),(centroid[0]+rectW,centroid[1]+rectW),(255,0,0),-1)

    if centroid[0]>=width-rectW:
        x=-1
    if centroid[0]<=rectW:
        x=1
    if centroid[1]>=height-rectW:
        y=-1
    if centroid[1]<=rectW:
        y=1

    centroid[0]+=x*speed
    centroid[1]+=y*speed


    cv2.imshow("cam",frame)
    if cv2.waitKey(1)==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()