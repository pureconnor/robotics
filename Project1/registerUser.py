import cv2
import os
cam = cv2.VideoCapture(0)
cam.set(3,640) # width
cam.set(4,480) # height
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

face_id = input('\n Enter User ID. End press <return> ==> ')
print("\n [INFO] Initialization face capture. Look at the camera and wait...")

count = 0
while(True):
	ret, img = cam.read()
	img = cv2.flip(img, -1) # vertical flip
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_detector.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
		count += 1
		#save
		cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
		cv2.imshow('image', img)
	k = cv2.waitKey(100) & 0xff # press ESC to quit
	if k==27:
		break
	elif count >= 30: #take 30 face samples and stop video
		break

print("\n [INFO] Exiting Program and cleaning up")
cam.release()
cv2.destroyAllWindows()
