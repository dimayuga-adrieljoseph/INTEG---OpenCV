import cv2 as cv
from readmodules import rescale

#--------------Image Capture-----------------
# #returns as a matrix of pixels
# image = cv.imread('Images/pic4.jpg')

# rescaled_image = rescale.rescaleFrame(image, 0.1)

# #display image in a seperate window
# cv.imshow('pic1', image)

# #displat rescaled image in a seperate window
# cv.imshow('rescale pic1', rescaled_image)

# #keyboard binding function that waits for a pressed key
# cv.waitKey(0)

#--------------Video Capture-----------------

# capture = cv.VideoCapture('Videos/vid1.mp4')

# while True:
#     # reads the video frame by frame 
#     # and a bolean that will tell if the video has been read or not
#     isTrue, frame = capture.read()
    
#     rescaled_video = rescale.rescaleFrame(frame, 0.3)
    
#     # displays the video frame by frame
#     cv.imshow('Video', rescaled_video)
    
#     #to stop the video from playing indefinitely
#     if cv.waitKey(20) & 255 == ord('d'):
#         break

# #Once the video is done, it stop capturing the video and exits the window
# capture.release()
# cv.destroyAllWindows()

capture = cv.VideoCapture(1)

# requests that the camera should take in a frame in a specific resolution
# rescale.changeRes(capture, 1280, 720)

while True:
    # reads the video frame by frame 
    # and a bolean that will tell if the video has been read or not
    isTrue, frame = capture.read()
    
    rescaled_video = rescale.rescaleFrame(frame, 1)
    
    # takes in the full resolution of the video and resize it after
    # resized_video = cv.resize(rescaled_video, (1280,720))
    
    # displays the video frame by frame
    cv.imshow('Video', rescaled_video)
    
    #to stop the video from playing indefinitely
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
#------------------Get Resolution---------------------------------
# get the resolution of the camera
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
print(f"Camera resolution: {int(width)} x {int(height)}")

#Once the video is done, it stop capturing the video and exits the window
capture.release()
cv.destroyAllWindows()