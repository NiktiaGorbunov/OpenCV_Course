import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# img = cv.imread('photos/shrek_1.jpg')
# cv.imshow('Shrek', img)

# # 1. Paint the image a certain color
# blank[:] = 0, 255, 0  # green
# # [0:y, 0:x]
# blank[:, 300:400] = 0, 0, 255  # green
# cv.imshow('Green', blank)

# 2. Draw a Rectangle
# (a1, a2, color, толщина линии)
# cv.rectangle(blank, (0, 0), (255, 255), (0,255,0), thickness=2)
cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0,255,0), thickness=-1)

cv.rectangle(blank, (255, 255), (500, 500), (0,255,0), thickness=8)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 0, 255), thickness=3)
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 20, (0, 0, 255), thickness=-1)

# 4. Draw a line
cv.line(blank, (500, 0), (0, 500), (0, 255, 0), thickness=2)

# 5. Write text
cv.putText(blank, 'Hello, my name is Nikita', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)

cv.imshow('Geo', blank)

cv.waitKey(0)