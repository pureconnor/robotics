import cv2
import numpy as np
from PIL import Image
import os

#Path for faces
path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml");

#Get images and label data
def getImagesAndLabels(path):
	imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
	faceSamples = []
	ids = []
	for imagePath in imagePaths:
		#Convert to grayscale
		PIL_img = Image.open(imagePath).convert('L')
		img_numpy = np.array(PIL_img, 'uint8')
		id = int(os.path.split(imagePath)[-1].split(".")[1])
		faces = detector.detectMultiScale(img_numpy)
		for(x,y,w,h) in faces:
			faceSamples.append(img_numpy[y:y+h,x:x+w])
			ids.append(id)
	return faceSamples,ids
print("\n [INFO] Training faces. This will take a moment...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))
#Save model to trainer/trainer.yml
recognizer.write('trainer/trainer.yml')
#Print number of faces trained and end program
print("\n [INFO] {0} faces were trained. Exiting program.".format(len(np.unique(ids))))

