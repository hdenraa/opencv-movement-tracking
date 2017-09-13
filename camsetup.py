import cv2
import cv2.cv as cv

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    cv2.imshow('frame',frame)

    cv2.waitKey(100)
