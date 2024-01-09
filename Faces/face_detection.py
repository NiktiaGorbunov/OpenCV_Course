import cv2 as cv


# img = cv.imread('../photos/stethem.jpg')
img = cv.imread('../photos/avengers_group.jpg')

img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv.INTER_AREA)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f"Number of faces found = {len(faces_rect)}")

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), thickness=3)


cv.imshow('Person', img)

cv.waitKey(0)