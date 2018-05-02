import cv2
import cv2.cv as cv
import numpy as np

def circleposition(cap,transform,newcameramtx,mtx,dist):
    done = False
    l=[[1,1],[1,1],[1,1]]
    while True:
        ret, frame = cap.read()
        fframe=cv2.flip(frame,0)
        ffframe=cv2.flip(fframe,1)

        gray = cv2.cvtColor(ffframe, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        circles = cv2.HoughCircles(blur,cv.CV_HOUGH_GRADIENT,1,12,param1=50,param2=10,minRadius=8,maxRadius=12)

        if circles is not None:
            circle = circles[0][0]
            if np.absolute(circle[0]-l[2][0]) > 12 or np.absolute(circle[1]-l[2][1]) > 12:
                l.append([int(circle[0]),int(circle[1])])
                l=l[1:]
            else:
                continue
        else:
            continue
        
        
        point = np.array([l[2]],dtype='float32')
        point = np.array([point])
        point = cv2.undistortPoints(point, mtx, dist, None, newcameramtx)
        pointOut = cv2.perspectiveTransform(point, transform)   

        [[[x,y]]]=pointOut
        yield [x,y]
