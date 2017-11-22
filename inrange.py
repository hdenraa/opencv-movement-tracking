# Standard imports
import cv2
import numpy as np;
 
# Read image
#im = cv2.imread("mpv-shot0001.jpg", cv2.CV_LOAD_IMAGE_GRAYSCALE)
im = cv2.imread("mpv-shot0001.jpg", cv2.CV_LOAD_IMAGE_COLOR)
# Blur image to remove noise
frame=cv2.GaussianBlur(im, (3, 3), 0)
mask = cv2.inRange(frame, (190, 190, 190), (255, 255, 255))

cv2.imshow("input", frame)

    
# Bitwise-AND of mask and purple only image - only used for display
res = cv2.bitwise_and(frame, frame, mask= mask)

#mask = cv2.erode(mask, None, iterations=1)
# commented out erode call, detection more accurate without it

# dilate makes the in range areas larger
mask = cv2.dilate(mask, None, iterations=1)

cv2.imshow("inRange", mask)
cv2.waitKey(0)
