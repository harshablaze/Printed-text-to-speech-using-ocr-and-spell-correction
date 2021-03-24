# importing opencv CV2 module
import cv2
#for eroison and dilation
import numpy as np
# bat.jpg is the batman image.
img = cv2.imread('test2-1.jpg')

# make sure that you have saved it in the same folder
# Averaging
# You can change the kernel size as you want
avging = cv2.blur(img,(10,10))

cv2.imshow('Averaging',avging)
cv2.waitKey(0)

# Gaussian Blurring
# Again, you can change the kernel size
gausBlur = cv2.GaussianBlur(img, (5,5),0)
cv2.imshow('Gaussian Blurring', gausBlur)
cv2.waitKey(0)

# Median blurring
medBlur = cv2.medianBlur(img,5)
cv2.imshow('Media Blurring', medBlur)
cv2.waitKey(0)

# Bilateral Filtering
bilFilter = cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral Filtering', bilFilter)


# Python program to demonstrate erosion and
# dilation of images.
# Reading the input image
img = cv2.imread('test2-1-1')

# Taking a matrix of size 5 as the kernel
kernel = np.ones((5,5), np.uint8)

# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
