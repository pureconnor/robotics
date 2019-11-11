import picamera
import numpy as np
import cv2 as cv
import IPython
import io
import time
from PIL import Image

if __name__ == "__main__":

    eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

    #initialize and start realtime video capture
    cam = cv.VideoCapture(0)
    cam.set(3,640) #width
    cam.set(4,480) #height
    #Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:
        ret, img = cam.read()
        img = cv.flip(img, -1) #vertical flip
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        cv.imshow('camera', img)
        k = cv.waitKey(10) & 0xff
        if k==27:
            break

    cam.release()
    cv.destroyAllWindows()