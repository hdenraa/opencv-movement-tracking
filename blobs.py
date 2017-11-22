# Standard imports
import cv2
import numpy as np;
 
# Read image
im = cv2.imread("mpv-shot0001.jpg", cv2.IMREAD_GRAYSCALE)
im = cv2.resize(im, None, fx = .5, fy = .5, interpolation = cv2.INTER_CUBIC)
cv2.imshow("input", im)
thresh = 0
maxValue = 255
th, dst = cv2.threshold(im, thresh, maxValue, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.imshow("threshold", dst)
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector()
 
# Detect blobs.
keypoints = detector.detect(dst)
#pts = np.float([keypoints[idx].pt for idx in len(keypoints)]).reshape(-1,1,2) 
#pts = np.float(keypoints[1].pt).reshape(-1,1,2)
#print "pts" + str(pts) 
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
x,y = keypoints[1].pt 

print "point "+str(x)+ " " + str(y) 

size = keypoints[1].size
print "size " + str(size)



cv2.circle(im_with_keypoints,(int(x)+int(size)/4,int(y)-int(size)/4),5,(0,255,0),-1)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
