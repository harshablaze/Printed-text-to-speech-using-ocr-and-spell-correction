import cv2
import numpy as np
import os
#from PIL import Image, ImageEnhance #for contrast only remove if not used
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
	#image1 = cv2.imread('./roi/ROI_{}.jpg'.format(ROI_number))
	#contrast enhancing roi image
	'''
	image1 = Image.open('./roi/ROI_{}.jpg'.format(ROI_number))
	contrast = ImageEnhance.Contrast(image1)
	contrast.enhance(1.1).save('./roi/ROI_{}.jpg'.format(ROI_number))
	'''
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
	# techniques applied to the input image
	#cv2.imshow('Adaptive Mean', thresh1)
	#cv2.imshow('Adaptive Gaussian', thresh2)
	#cv2.imshow('binary inv', thresh3)
	#cv2.imshow('binary', thresh4)
	cv2.imwrite('prepro/test_{}.jpg'.format(ROI_number), thresh3)
	ROI_number += 1
image1 = cv2.imread('./images/sample_0.jpg')
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
											cv2.THRESH_BINARY, 199, 5)

thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
											cv2.THRESH_BINARY, 199, 5)

	
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

ret,thresh4 = cv2.threshold(thresh1,127,255,cv2.THRESH_BINARY)
cv2.imwrite('./images/sample_01.jpg', thresh2)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
