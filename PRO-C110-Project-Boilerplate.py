# To Capture Frame
import cv2

# To process image array
import numpy as np


# import the tensorflow modules and load the model
model = load_model("keras_Model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

# Attaching Cam indexed as 0, with the application software
camera = cv2.VideoCapture(0)

# Infinite loop
while True:

	# Reading / Requesting a Frame from the Camera 
	status , frame = camera.read()

	# if we were sucessfully able to read the frame
	if status:

		# Flip the frame
		frame = cv2.flip(frame , 1)
		
		#resize the frame
		size = (224, 224)
		image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
		
		# normalize it before feeding to the model
		normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

		# get predictions from the model
		prediction = model.predict(data)
		index = np.argmax(prediction)
		class_name = class_names[index]
		confidence_score = prediction[0][index]
		
		print("Class:", class_name[2:], end="")
		print("Confidence Score:", confidence_score)
		# displaying the frames captured
		cv2.imshow('feed' , frame)

		# waiting for 1ms
		code = cv2.waitKey(1)
		
		# if space key is pressed, break the loop
		if code == 32:
			break

# release the camera from the application software
camera.release()

# close the open window
cv2.destroyAllWindows()
