import cv2 as cv

#Openning an image in a window

# img = cv.imread('Photos/cat1.webp')

# cv.imshow('Cat', img)
# cv.waitKey(10)

#Openning a video and displaying in a window

capture = cv.VideoCapture('Videos/Cat.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xff == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# #Openning Webcam and displaying in a window

# capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
#     if cv.waitKey(20) & 0xff == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()