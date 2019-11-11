import picamera
import numpy as np
import cv2 as cv
import IPython
import io
import time
from PIL import Image

if __name__ == "__main__":

    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
    smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')

    #initialize and start realtime video capture
    cam = cv.VideoCapture(0)
    cam.set(3,640) #width
    cam.set(4,480) #height
    #Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    captured = False

    while True:
        ret, img = cam.read()
        img = cv.flip(img, -1) #vertical flip
        img_copy = img
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            roi_gray = gray[y:y + h, x:x + w] 
            roi_color = img[y:y + h, x:x + w]
            smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
            for(sx,sy,sw,sh) in smiles:
                smile = cv.rectangle(roi_color,(sx,sy),((sx+sw),(sy+sh)),(255,0,0),2)
                if smile is not None and captured is False:
                    print("\n [PROMPT] Would you like to save this photo? (y/n):")
                    cv.imshow('Capture', img_copy)
                    choice=cv.waitKey(0) & 0xff
                    if choice==121:
                        captured = True
                        print("\n [INFO] Photo saved to current working directory")
                        break
                    if choice==110:
                        print("\n [INFO] Photo released.")
                        break 

        cv.imshow('camera', img)
        k = cv.waitKey(10) & 0xff
        if k==27:
            break

    cam.release()
    cv.destroyAllWindows()