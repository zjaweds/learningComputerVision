import cv2 as cv

img = cv.imread('Photos/cat1.webp')
cv.imshow('Cat',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Cat',gray)
cv.waitKey(0)