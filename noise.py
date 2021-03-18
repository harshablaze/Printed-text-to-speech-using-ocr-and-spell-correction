import cv2
import numpy as np

# This will import Image and ImageChops modules
from PIL import Image, ImageEnhance


img = cv2.imread('C:\sample2.jpg')
#new_image = cv2.resize(img, (400,400))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((1,1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
#img = cv2.GaussianBlur(img, (5,5), 0)
#img = cv2.medianBlur(img,5)
cv2.imwrite("sample4.jpg",img)




# Opening Image
img = Image.open("sample4.jpg")
# Creating object of Sharpness class
im3 = ImageEnhance.Sharpness(img)
# showing resultant image
#im3.enhance(5.0).show()
