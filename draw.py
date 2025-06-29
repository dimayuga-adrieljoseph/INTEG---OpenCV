import cv2 as cv
import numpy

image = cv.imread('Images/pic4.jpg')
cv.imshow('pic4', image)

# displays black image
# height and width is 500 with 3 color channel
blank_image = numpy.zeros((500, 500, 3), dtype = 'uint8')
# cv.imshow("blank", blank_image)

#adding color to the blank image
#by default, it is blue-green-red
# blank_image[:] = 255, 255, 255

#adding color to a specific area only
# blank_image[200:300, 200:300] = 255, 255, 255
# cv.imshow('color', blank_image)

#draw a rectangle
cv.rectangle(image, (1000,1500), (1500,1000), (255,0,0), 10 )
cv.imshow('rectangle', image)

cv.waitKey(0)