import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('photos/shrek_1.jpg')
img = cv.resize(img, (img.shape[1] // 3, img.shape[0] // 3), interpolation=cv.INTER_AREA)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Simple treshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple treshold inverse', thresh_inv)

# Adoptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adoptive Thresholding', adaptive_thresh)



cv.waitKey(0)