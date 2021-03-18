import cv2 as cv

img = cv.imread('C:\sample2.jpg',0)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
        cv.THRESH_BINARY,11,2)
cv.imwrite("sample3.jpg",th3)
