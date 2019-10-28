import picamera
import numpy as np
import cv2 as cv
import IPython
import io
import time
from PIL import Image

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

# Use 'jpeg' instead of 'png' (~5 times faster)
def showarray(a, fmt='jpeg'):
    '''
    Function to display an image within a Jupyter notebook.
    '''
    f = io.BytesIO()
    Image.fromarray(a).save(f, fmt)
    Image.fromarray(a).save('/home/pi/Modules/Module4/Module-4/Exercise 2/faceTest', 'JPEG')
    IPython.display.display(IPython.display.Image(data=f.getvalue(), width = 480, height = 360))

def detectFacesAndEyes(img_array):
    '''
    Function to detect eyes and faces using a Haar-Cascade classifier.
    '''
    gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv.rectangle(img_array,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img_array[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

if __name__ == "__main__":

    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.framerate = 30
        camera.vflip = True
        freshest_frame = np.empty((240, 320, 3), dtype = np.uint8)
        while True:
            camera.capture(freshest_frame, use_video_port = True, format = 'rgb')
            detectFacesAndEyes(freshest_frame)
            showarray(freshest_frame)
            IPython.display.clear_output(wait = True)