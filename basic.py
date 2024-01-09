import cv2 as cv

img = cv.imread('photos/shrek_1.jpg')

# Resize
img = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Shrek', img)

# Converting to grayscale
# Интенсивность пикселей
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Shrek_gray', gray)

# Blur
# Устранение шумов
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Shrek_blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Shrek_canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Shrek_dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Shrek_eroded', eroded)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)


cv.waitKey(0)