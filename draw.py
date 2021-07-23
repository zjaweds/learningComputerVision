import cv2 as cv
import numpy as np
blank = np.zeros((500, 200, 3), dtype = 'uint8')
blank[:]= 0, 0, 255

cv.rectangle(blank, (0,0),(260, 260), (255, 0, 0), thickness=3)
cv.imshow('Rectangle',  blank)
cv.imshow('Blank',blank)
img = cv.imread('Photos/cat1.webp')
cv.rectangle(img, (0,0),(260, 260), (255, 0, 0), thickness=3)
cv.imshow('Cat',img)
formattedImg = cv.imread('Photos/cat1.webp')
cv.rectangle(formattedImg, (0,0),(formattedImg.shape[1]//1, formattedImg.shape[0]), (255, 0, 0), thickness=3)
cv.imshow('Enclosed Cat',formattedImg)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 30, (0,255,0), thickness=5)
cv.imshow('Circle', blank)
cv.waitKey(0)