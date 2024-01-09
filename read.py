import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(3, height)




# Reading photos
img1 = cv.imread('photos/shrek_1.jpg')
cv.imshow('origin Shrek', img1)

resized_image = rescaleFrame(img1, scale=.2)
cv.imshow('resize Shrek', resized_image)

cv.waitKey(0)


# Reading Videos
capture = cv.VideoCapture('videos/Танец огров.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


