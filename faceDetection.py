import cv2 as cv
import os
cascPathface = os.path.dirname(
    cv.__file__) + "/data/haarcascade_frontalface_alt2.xml"
cascPatheyes = os.path.dirname(
    cv.__file__) + "/data/haarcascade_eye_tree_eyeglasses.xml"

faceCascade = cv.CascadeClassifier(cascPathface)
eyeCascade = cv.CascadeClassifier(cascPatheyes)

videoCapture = cv.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                                        scaleFactor= 1.1, 
                                        minNeighbors = 5, 
                                        minSize = (60,60), 
                                        flags = cv.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in faces:
        # cv.rectangle(frame, (x,y),(x+w, y+h), (0,255,0),2)
        faceROI = frame[y:y+h,x:x+w]
        eyes = eyeCascade.detectMultiScale(faceROI)
        for (x2, y2, w2, h2) in eyes:
            eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
            radius = int(round((w2 + h2) * 0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0), 4)
    cv.imshow('Video',frame)
    if cv.waitKey(1) &0xFF == ord('q'):
        break
videoCapture.release()
cv.destroyAllWindows()