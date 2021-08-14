import cv2

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

img = cv2.imread(r'Photos/cat1.webp')  
# save image  
status = cv2.imwrite(r'Photos/cat1.webp',img)  
print("Image written sucess? : ", status)