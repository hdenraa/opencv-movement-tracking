import cv2
import cv2.cv as cv
import numpy as np
import pygame
import math
import random
import os.path
import pickle
import cProfile
from kallibrer import kallibrer
from findcircle import circleposition
from spriteclasses import Player,Block,Border,BLACK,WHITE,GREEN,RED,BLUE
from puckmovement import puck_movement






 
# Read image
#im = cv2.imread("mpv-shot0001.jpg", cv2.CV_LOAD_IMAGE_GRAYSCALE)
im = cv2.imread("mpv-shot0001.jpg") #, cv2.CV_LOAD_IMAGE_COLOR)

im = cv2.resize(im, None, fx = .5, fy = .5, interpolation = cv2.INTER_CUBIC)
y,x,ch=im.shape
#dest = np.array([ [0,0],[1299,0],[1299,699],[0,699] ],np.float32)
dest = np.array([ [0,0],[y,0],[y,x],[0,x] ],np.float32)

warp = kallibrer(im,dest)

# Blur image to remove noise

#im = np.asarray(im, dtype="float32")
#im = np.array([im])
#print "im: " + str(im)

#imwarp = cv2.perspectiveTransform(im, warp)
imwarp = cv2.warpPerspective(im,warp,(y,x))
cv2.imshow("imwarp", imwarp)
frame=cv2.GaussianBlur(imwarp, (3, 3), 0)

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


main()    
    
pygame.quit()
