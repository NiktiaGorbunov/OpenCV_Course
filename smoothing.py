import cv2 as cv

img = cv.imread('photos/shrek_1.jpg')
img = cv.resize(img, (img.shape[1] // 3, img.shape[0] // 3), interpolation=cv.INTER_AREA)

cv.imshow('shrek', img)

# averaging
average = cv.blur(img, (3, 3))
cv.imshow('avg blur', average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('gauss', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bi', bilateral)

cv.waitKey(0)