import cv2 as cv
import numpy as np


img = cv.imread('photos/shrek_1.jpg')
img = cv.resize(img, (img.shape[1] // 3, img.shape[0] // 3), interpolation=cv.INTER_AREA)

blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank.copy(), (img.shape[1] // 2 - 60, img.shape[0] // 2 - 10), 150, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Masked Image', masked)


cv.waitKey(0)