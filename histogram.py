import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('photos/shrek_1.jpg')
img = cv.resize(img, (img.shape[1] // 3, img.shape[0] // 3), interpolation=cv.INTER_AREA)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('shrek', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank.copy(), (img.shape[1] // 2 - 60, img.shape[0] // 2 - 10), 150, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('mask', masked)

# # Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], circle, [256], [0, 256])
#
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# Colour histogram
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])

    plt.plot(hist, color=col)


plt.xlim([0, 256])
plt.show()


cv.waitKey(0)