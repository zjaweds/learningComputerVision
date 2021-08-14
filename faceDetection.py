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
        cv.rectangle(frame, (x,y),(x+w, y+h), (0,255,0),2)
        
    cv.imshow('Video',frame)
    # cv.waitKey()
    if cv.waitKey(1) &0xFF == ord('q'):
        break
videoCapture.release()
cv.destroyAllWindows()