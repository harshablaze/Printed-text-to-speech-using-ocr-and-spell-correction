'''
attempting prepro for multiple rois and preprocess multiple rois
remark: module solved and completed

'''
import cv2
import numpy as np
import os
# path to input image is specified and
# image is loaded with imread command
#image1 = cv2.imread('images/sample111.jpg')

#clear prepro folder
dir = './prepro/'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))


#count rois in roi folder
list = os.listdir('./roi/') # dir is your directory path
number_of_files = len(list)
print('No of ROIs detected: '+ str(number_of_files))

ROI_number = 0
for i in range(0,number_of_files):
	image1 = cv2.imread('./roi/ROI_{}.jpg'.format(ROI_number))

	#image1 = cv2.imread('roi/ROI_0.jpg')
	#initial sample4
	# cv2.cvtColor is applied over the
	# image input with applied parameters
	# to convert the image in grayscale
	img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

	# applying different thresholding
	# techniques on the input image
	thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
											cv2.THRESH_BINARY, 199, 5)

	thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
											cv2.THRESH_BINARY, 199, 5)

	
	ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

	ret,thresh4 = cv2.threshold(thresh1,127,255,cv2.THRESH_BINARY)
	# the window showing output images
	# with the corresponding thresholding
	# techniques applied to the input image
	#cv2.imshow('Adaptive Mean', thresh1)
	#cv2.imshow('Adaptive Gaussian', thresh2)
	#cv2.imshow('binary inv', thresh3)
	#cv2.imshow('binary', thresh4)

	#cv2.imwrite("test2-1.jpg", thresh1)
	#cv2.imwrite("test2-2.jpg", thresh2)
	#cv2.imwrite("prepro/test_0.jpg", thresh3)
	cv2.imwrite('prepro/test_{}.jpg'.format(ROI_number), thresh3)
	ROI_number += 1
#cv2.imwrite("test2-4.jpg", thresh4)

#thresholding completed

#noise removal code
# Median blurring
#medBlur = cv2.medianBlur(thresh1,5)
#cv2.imshow('Media Blurring', medBlur)
#cv2.imwrite("images/test2-1-1.jpg", medBlur)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
