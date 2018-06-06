import cv2
import numpy as np 
import time
import copy

def circleposition(cap,transform,newcameramtx,mtx,dist,mask,maskcorners):
    thresh = 0
    maxValue = 255
    #print "CAP type" + str(type(cap))
    [oldx,oldy] = [0,0]
    #print "maskcorners %s" % str(maskcorners)
    params = cv2.SimpleBlobDetector_Params()
    
    # Change thresholds
    #params.minThreshold = 10;
    #params.maxThreshold = 200;
     
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 75
     
    # Filter by Circularity
    #params.filterByCircularity = True
    #params.minCircularity = 0.8
     
    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.87
     
    # Filter by Inertia
    #params.filterByInertia = True
    #params.minInertiaRatio = 0.01     
    ret, frame = cap.read()
    detector = cv2.SimpleBlobDetector(params)
    h,  w = frame.shape[:2]
    done = False
    l=[[1,1],[1,1],[1,1]]
    while True:
        time1 = time.clock()
        ret, frame = cap.read()
        #time1 = time.clock()
        frame = cv2.undistort(frame, mtx, dist, None, newcameramtx)
        #time2 = time.clock()
        #print 'undistort %0.3f' % (time2-time1)
        #cv2.imshow('frame',frame)
        #cv2.waitKey(3000)
        #ffframe=frame
        #fframe=cv2.flip(frame,0)
        ffframe=cv2.flip(frame,-1)
        
        print maskcorners,h,w
        #ulx = max(maskcorners[0][0] -30,0) ##sorg for ikke at ryge udenfor billede
        #uly = max(maskcorners[0][1] -30,0)
        #brx = min(maskcorners[2][0] + 30,w)
        #bry = min(maskcorners[2][1] + 30,h)
        ulx = maskcorners[0][0] 
        uly = maskcorners[0][1] 
        brx = maskcorners[2][0] 
        bry = maskcorners[2][1] 
        #cv2.imshow('before crop',ffframe)
        #cv2.waitKey(3000)        
        #cv2.circle(ffframe,(ulx,uly),10,(0,0,255),-1)
        #cv2.circle(ffframe,(brx,bry),10,(0,0,255),-1)
        #cv2.imshow('before crop with point',ffframe)
        #cv2.waitKey(3000)    

        #ffframe = ffframe[uly:bry,ulx:brx]
        #ffframe=cv2.flip(frame,-1)
        #cv2.imshow('cropped',ffframe)
        #cv2.waitKey(3000)
               
        #time1 = time.clock()
        gray = cv2.cvtColor(ffframe, cv2.COLOR_BGR2GRAY)
        #time2 = time.clock()
        #print 'cvtColur %0.3f' % (time2-time1)
        #cv2.imshow('gray',gray)
        #cv2.waitKey(10)
        #time1 = time.clock()
        th, dst = cv2.threshold(gray, thresh, maxValue, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        #time2 = time.clock()
        #print 'treshold %0.3f' % (time2-time1)
        #cv2.imshow('dst',dst)
        #cv2.waitKey(10)
        out=dst
        #out = np.zeros_like(dst)
        #out[mask] = dst[mask]
        #cv2.imshow('mask',out)
        #cv2.waitKey(10)

        # Detect blobs.
        dtime1 = time.clock()
        keypoints = detector.detect(out)
        dtime2 = time.clock()
        print 'detector %0.6f' % (dtime2-dtime1)
        #print "keypoints" + str(keypoints)
        if len(keypoints) > 0: 
            keypoint = [keypoints[-1]]
            circle = keypoint[0].pt
            l.append([int(circle[0]),int(circle[1])])
            l=l[1:]
            
        
        adpoint = copy.copy(l[2])
        #adpoint[0]=adpoint[0]+ulx
        #adpoint[1]=adpoint[1]+uly
        point = np.array([adpoint],dtype='float32')
        point = np.array([point])
        #time1 = time.clock()
        #pointUndist = cv2.undistortPoints(point, mtx, dist, None, newcameramtx)
        #time2= time.clock()
        #print 'undistortPoints %0.3f' % (time2-time1)
        #[[[pux,puy]]] = pointUndist
        #pux=w-pux
        #puy=h-puy
        #pointUndist = np.array([[[pux,puy]]],dtype='float32')
        pointOut = cv2.perspectiveTransform(point, transform)   

        #[[[xu,yu]]]=pointUndist
        [[[xo,yo]]]=pointOut
        #yield [[x,y],[xo,yo],[xu,yu]]
        time2 = time.clock()
        print 'findcircle clocktime %0.6f' % (time2-time1)  

        yield adpoint #[xo,yo]
        
