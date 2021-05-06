'''
this is copy of roi.py

this program is an attempt to rectify contour large to small auto sort error
required top to bottom order
remark: module pending at compressing the image
'''
import cv2
import os
def get_contour_precedence(contour, cols):
    tolerance_factor = 10
    origin = cv2.boundingRect(contour)
    return ((origin[1] // tolerance_factor) * tolerance_factor) * cols + origin[0]

# Load image, grayscale, Gaussian blur, adaptive threshold
image = cv2.imread('./images/sample_0.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (9,9), 0)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)
# Dilate to combine adjacent text contours
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
ret,thresh3 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
dilate = cv2.dilate(thresh, kernel, iterations=4)

# Find contours, highlight text areas, and extract ROIs
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cnts = cv2.findContours(thresh3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnts = cnts[0] if len(cnts) == 2 else cnts[1]

#ORDER CONTOURS
cnts.sort(key=lambda x:get_contour_precedence(x, image.shape[1]))

#delete previous roi images in folder roi to avoid
dir = './roi/'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

ROI_number = 0
for c in cnts:
    area = cv2.contourArea(c)
    if area > 10000:
        x,y,w,h = cv2.boundingRect(c)
        #cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 3)
        cv2.rectangle(image, (x, y), (x + w, y + h), (100,100,100), 1)
        #use below code to write roi when results are good
        ROI = image[y:y+h, x:x+w]
        cv2.imwrite('roi/ROI_{}.jpg'.format(ROI_number), ROI)
        ROI_number += 1

cv2.imshow('thresh', thresh)
cv2.imshow('dilate', dilate)
cv2.imshow('image', image)
cv2.waitKey()
