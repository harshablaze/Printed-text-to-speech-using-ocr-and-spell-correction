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
	img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
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
for i in range(0,1):
	img = cv2.imread('./output/sample0{}.jpg'.format(i))
	img1 = img
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
	#ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
	thresh1 = cv2.adaptiveThreshold(thresh3, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
												cv2.THRESH_BINARY, 199, 5)

	#thresh2 = cv2.adaptiveThreshold(thresh3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
	#											cv2.THRESH_BINARY, 199, 5)
	
	#ret, thresh4 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	#thresh5 = cv2.Canny(thresh3,100,200)
	ret, thresh6 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY +
                              cv2.THRESH_OTSU)
	#kernel = np.ones((2, 2), np.uint8)
	#img_erosion = cv2.erode(thresh6, kernel, iterations=2)
	#img_dilation = cv2.dilate(img_erosion, kernel, iterations=5)
	cv2.imwrite('./output/sample1{}.jpg'.format(i), thresh4)
	cv2.imwrite('./output/sample2{}.jpg'.format(i),thresh3)
	#cv2.imwrite('./output/sample3{}.jpg'.format(i),thresh2)
	#cv2.imwrite('./output/sample4{}.jpg'.format(i), thresh1)
	#cv2.imwrite('./output/sample5{}.jpg'.format(i), thresh5)
	#cv2.imwrite('./output/sample6{}.jpg'.format(i), thresh1)
	cv2.imwrite('./output/sample6{}.jpg'.format(i), thresh1)
	cv2.imwrite('./output/sample7{}.jpg'.format(i), img)
	cv2.imwrite('./output/sample5{}.jpg'.format(i), thresh6)
	#cv2.imwrite('./output/sample8{}.jpg'.format(i), img_erosion)
	#cv2.imwrite('./output/sample9{}.jpg'.format(i), img_dilation)
# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
