import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('photos/shrek_3.jpg')
img = cv.resize(img, (img.shape[1] // 3, img.shape[0] // 3), interpolation=cv.INTER_AREA)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Laplacian
# Вычисляет градиенты в оттенках серого (при переходе от белого к черного и от черного к белому)
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('combined_sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)


cv.waitKey(0)



