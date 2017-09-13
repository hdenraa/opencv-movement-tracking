import numpy as np
import cv2

corners = []
clicked = False

ffframe = None
clickcount = 0

def onMouse(event, x, y, flags, param):
    global clicked
    global ffframe
    global clickcount
    global corners
    print "MOUSE" + str(x) + " " + str(y) + " " + str(cv2.cv.CV_EVENT_LBUTTONUP) + " " + str(event)
    if event == cv2.cv.CV_EVENT_LBUTTONUP:
        print "mouse"
        cv2.circle(ffframe,(x,y),10,(0,0,255),-1)
        clicked = True
        clickcount = clickcount + 1
        corners.append((x,y))
   
def kallibrer(cap,dest):        
    global ffframe
    global clickcount
    
    success, frame = cap.read()
    
    fframe=cv2.flip(frame,0)
    ffframe=cv2.flip(fframe,1)


    blurred = cv2.GaussianBlur(ffframe, (5, 5), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    ##dest = np.array([ [0,0],[1299,0],[1299,699],[0,699] ],np.float32)




    cv2.namedWindow('img')
    cv2.setMouseCallback('img', onMouse)

    cv2.imshow('img',ffframe)

    clickcount = 0

    while success and cv2.waitKey(1) == -1 and clickcount < 4:
        cv2.imshow('img',ffframe)
        pass

    cv2.waitKey(10)
    cv2.destroyWindow('img')


    npacorners = np.array(corners,np.float32)
    transform = cv2.getPerspectiveTransform(npacorners,dest)
    print "transform:"
    print transform
    return transform



##cv2.destroyAllWindows()
