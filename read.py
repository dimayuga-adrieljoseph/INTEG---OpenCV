import cv2 as cv
from readmodules import rescale

#--------------Image Capture-----------------
#returns as a matrix of pixels
image = cv.imread('Images/pic4.jpg')

rescaled_image = rescale.rescaleFrame(image, 0.1)

#display image in a seperate window
cv.imshow('pic1', image)

#displat rescaled image in a seperate window
cv.imshow('rescale pic1', rescaled_image)

#keyboard binding function that waits for a pressed key
cv.waitKey(0)

#--------------Video Capture-----------------

# capture = cv.VideoCapture('Videos/vid1.mp4')

# while True:
#     # reads the video frame by frame and a bolean that will tell if the video has been read or not
#     isTrue, frame = capture.read()
    
#     rescaled_video = rescale.rescaleFrame(frame, 0.3)
    
#     # displays the video frame by frame
#     cv.imshow('Video', rescaled_video)
    
#     #to stop the video from playing indefinitely
#     if cv.waitKey(20) & 255 == ord('d'):
#         break
    
# capture.release()
# cv.destroyAllWindows()
