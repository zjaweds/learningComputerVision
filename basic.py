import cv2 as cv
import numpy as np
# img = cv.imread('Photos/cat1.webp',-1)
# cv.imshow('Cat',img)

# # gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# # cv.imshow('Gray Cat',gray)

# # blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
# # cv.imshow('Blur', blur)

# # canny = cv.Canny(img, 125,175) 
# # cv.imshow('Canny', canny)
# # dialated = cv.dilate(canny,(7,7), iterations=3)
# # cv.imshow("Dialated", dialated)

# # eroded = cv.erode(dialated,(7,7), iterations=3)
# # cv.imshow('Eroded',eroded)

# # cropped = eroded[0:45]
# cv.waitKey(0)

# cv.destroyAllWindows()

img = cv.imread(r'Photos/cat1.webp')  
blue = img[100,100,0]
img[100,100] = [100,100,255]
# img.item(10,10,2)
print (img.dtype)