import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

# cv.imshow('rectangle', rectangle)
# cv.imshow('circle', circle)

origin = cv.circle(blank.copy(), (200, 200), 200, 255, 1) + cv.rectangle(blank.copy(), (30,30), (370, 370), 255, 1)

# bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
bitwise_and += origin
cv.imshow('AND', bitwise_and)

# bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
bitwise_or += origin
cv.imshow('OR', bitwise_or)

# bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
bitwise_xor += origin
cv.imshow('XOR', bitwise_xor)

# bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
bitwise_xor += origin
cv.imshow('XOR', bitwise_xor)

# bitwise NOT
bitwise_not = cv.bitwise_not(origin)
cv.imshow('NOT', bitwise_not)

cv.waitKey(0)