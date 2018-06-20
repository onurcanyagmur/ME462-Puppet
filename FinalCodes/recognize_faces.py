import cv2
#os module for reading training data directories and paths
import os
#numpy to convert python lists to numpy arrays as it is needed by OpenCV face recognizers
import numpy as np
import time # This will be used for to specify a time for to detect faces

subjects = ["", "abc", "def","ghi", "jkl", "mno","pqr", "serpil", "xwy","simisnis","stu","vahit"]
# Subjects are the name or tag of the people whom their images are going to be used as training data for the classifier.

cap = cv2.VideoCapture(0)  #Uses the first camera object to live stream, you are free to change this.
						   #This can be replaced either by another camera, or a saved image.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#CascadeClassifier is the object that classifies images and detects faces. We use haarcascade_frontalface_default.xml classifier for now.
# Make sure that the directory is correct and you can use any callissifier you want.
# In future this haarcascade classifier should be replaced with a better classifier with tolerance values for detecting unknown subjects

def detect_face(img): #this function is for training 
	#convert the test image to gray scale as opencv face detector expects gray images
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#load OpenCV face detector, I am using LBP which is fast
	#there is also a more accurate but slow: Haar classifier
	face_cascade = cv2.CascadeClassifier('/Users/Onurcan/Desktop/haarcascade_frontalface_default.xml')
	#face_cascade.load('/Users/Onurcan/Desktop/haarcascade_frontalface_alt.xml')
	print(face_cascade.empty())	 
	#let's detect multiscale images(some images may be closer to camera than others)
	#result is a list of faces
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5);
		 
	#if no faces are detected then return original img
	if (len(faces) == 0):
		return None, None
		 
	#under the assumption that there will be only one face,
	#extract the face area
	x, y, w, h = faces[0]
		 
	#return only the face part of the image
	return gray[y:y+w, x:x+h], faces[0]

def prepare_training_data(data_folder_path="/Users/Onurcan/Desktop/training-data"):
 
	#------STEP-1--------
	#get the directories (one directory for each subject) in data folder
	dirs = os.listdir(data_folder_path)
	print(dirs)
	#list to hold all subject faces
	faces = []
	#list to hold labels for all subjects
	labels = []
	 
	#let's go through each directory and read images within it
	for dir_name in dirs:
	 
	#our subject directories start with letter 's' so
	#ignore any non-relevant directories if any
		if not dir_name.startswith("s"):
			continue;
	 
	#------STEP-2--------
	#extract label number of subject from dir_name
	#format of dir name = slabel
	#, so removing letter 's' from dir_name will give us label
		label = int(dir_name.replace("s", ""))
	 
	#build path of directory containing images for current subject subject
	#sample subject_dir_path = "training-data/s1"
		subject_dir_path = data_folder_path + "/" + dir_name
	 
	#get the images names that are inside the given subject directory
		subject_images_names = os.listdir(subject_dir_path)
	 
	#------STEP-3--------
	#go through each image name, read image, 
	#detect face and add face to list of faces
		for image_name in subject_images_names:
	 
	#ignore system files like .DS_Store
			if image_name.startswith("."):
				continue;
	 
	#build image path
	#sample image path = training-data/s1/1.pgm
			image_path = subject_dir_path + "/" + image_name
	 
	#read image
			image = cv2.imread(image_path)
	 
	#display an image window to show the image 
			cv2.imshow("Training on image...", image)
			cv2.waitKey(100)
	 
	#detect face
			face, rect = detect_face(image)
	 
	#------STEP-4--------
	#for the purpose of this tutorial
	#we will ignore faces that are not detected
			if face is not None:
	#add face to list of faces
				faces.append(face)
	#add label for this face
				labels.append(label)
	 
	cv2.destroyAllWindows()
	cv2.waitKey(1)
	cv2.destroyAllWindows()
	 
	return faces, labels

print("Preparing data...")
faces, labels = prepare_training_data("training-data")
print("Data prepared")
 
#print total faces and labels
print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

#face_recognizer = cv2.face.createLBPHFaceRecognizer()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))


def catchImage():
	start=time.time()
	while True :
		ret, img = cap.read()
		gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		ListofFaces=[];
		for (x,y,w,h) in faces :
			cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = gray[y:y+h, x:x+w]
			prediction = face_recognizer.predict(roi_gray)
			prediction_text = subjects[prediction[0]]
			cv2.putText(img, prediction_text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
			print(prediction_text)
			ListofFaces.append(prediction);
		now=time.time()
		if(len(ListofFaces)>0):
			cv2.imshow('img',img)
			return ListofFaces,img
		if((now-start)>2):
			return [],[]



	# def draw_text(img, text, x, y):
	# 	cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

	# def draw_rectangle(img, rect):
	# 	(x, y, w, h) = rect
	# 	cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
	

	



	# def predict():
	# 	ret, img = cap.read()

	# 	#make a copy of the image as we don't want to change original image
	# 	#detect face from the image
	# 	face, rect = detect_face(img)
		 
	# 	#predict the image using our face recognizer 
	# 	label= face_recognizer.predict(face)
	# 	#get name of respective label returned by face recognizer
	# 	print(label)
	# 	label_text = subjects[label[0]]
		 
	# 	#draw a rectangle around face detected
	# 	draw_rectangle(img, rect)
	# 	#draw name of predicted person
	# 	draw_text(img, label_text, rect[0], rect[1]-5)
	# 	cv2.imshow('img',img)

	# 	cv2.waitKey(0)
	# 	cv2.destroyAllWindows()

	# 	pass
		

	

	
