import cv2
import numpy as np
import os
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

#indicate id counter
id=0
#Name related to Id e.g Connor: id=1, etc
names = ['Connor', 'Connor', 'Mike', 'Ethan']

#initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3,640) #width
cam.set(4,480) #height
#Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
while True:
	ret, img = cam.read()
	img = cv2.flip(img, -1) #vertical flip
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (int(minW), int(minH)))
	for(x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
		id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
		#Check confidence
		if(confidence < 100):
			id = names[id]
			condfidence = 100-confidence
		else:
			id = "unknown"
			confidence = 100-confidence

		cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
		cv2.putText(img, str(int(confidence)), (x+5,y+h-5), font, 1, (255,255,0), 2)

	cv2.imshow('camera', img)
	k = cv2.waitKey(10) & 0xff #Press ESC to exit
	if k==27:
		break

#Cleanup
print("\n [INFO] Exiting program and cleaning up resources...")
cam.release()
cv2.destroyAllWindows()
