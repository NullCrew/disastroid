import cv2
import sys, os, time
def create_image_dataset(uname):
	cpt = 0
	# name = input("Enter Your Name :")
	name = uname
	path = "media/train/"+ name
	os.mkdir(path)
	print("press q to stop ")
	vidStream = cv2.VideoCapture(0)
	while True:
		
		ret, frame = vidStream.read() # read frame and return code.
		
		#cv2.imshow("test window", frame) # show image in window
		if cpt ==0:
			print("Be Ready!")
			time.sleep(5)
		cv2.imwrite("media/train/"+name+"/image%04i.jpg" %cpt, frame)    #Give path to  train-images/0/ and keep image%04i.jpg as it is in this line. Your images will be stored at train-images/0/ folder
		cpt += 1
		if cpt == 10:
			cv2.destroyAllWindows()
			break

