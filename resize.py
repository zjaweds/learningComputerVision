import cv2 as cv

#Openning a video and displaying in a window

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Videos/Cat.mp4')
while True:
    isTrue, frame = capture.read()
    resized_frame = rescaleFrame(frame, scale=.4)

    cv.imshow('Video', frame)
    cv.imshow('Resized Video', resized_frame)
    if cv.waitKey(20) & 0xff == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
