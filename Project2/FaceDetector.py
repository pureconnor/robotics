import cv2
import numpy as np
import os
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

def getFace():
	#indicate id counter
	id=0
	#Name related to Id e.g Connor: id=1, etc
	names = ['None', 'Connor', 'Mike', 'Stuti']

	#initialize and start realtime video capture
	cam = cv2.VideoCapture(0)
	cam.set(3,640) #width
	cam.set(4,480) #height
	
	#Define min window size to be recognized as a face
	minW = 0.1*cam.get(3)
	minH = 0.1*cam.get(4)

	i = 0
	ITERATIONS = 200

	while i<ITERATIONS:
		i += 1
		ret, img = cam.read()
		img = cv2.flip(img, -1) #vertical flip
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (int(minW), int(minH)))
		for(x,y,w,h) in faces:
			id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
			#Check confidence
			if(confidence < 100 and confidence > 70):
				id = names[id]
				confidence = 100-confidence
				return id
			else:
				id = 'Unknown'
				confidence = 100-confidence
	return id

