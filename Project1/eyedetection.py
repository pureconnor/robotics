import picamera
import numpy as np
import cv2 as cv
import IPython
import io
import time
from PIL import Image

# Use 'jpeg' instead of 'png' (~5 times faster)
def showarray(a, fmt='jpeg'):
    '''
    Function to display an image within a Jupyter notebook.
    '''
    f = io.BytesIO()
    Image.fromarray(a).save(f, fmt)
    IPython.display.display(IPython.display.Image(data=f.getvalue(), width = 480, height = 360))

def detectFacesAndEyes(img, gray):
    '''
    Function to detect eyes and faces using a Haar-Cascade classifier.
    '''
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
    eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

if __name__ == "__main__":

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
        detectFacesAndEyes(img, gray)
        cv.imshow('camera', img)
        k = cv.waitKey(10) & 0xff
        if k==27:
            break
        IPython.display.clear_output(wait = True)