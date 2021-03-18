import cv2

#Read gray image
img = cv2.imread("sample4.jpg",0)

#Create default parametrization LSD
lsd = cv2.createLineSegmentDetector(0)

#Detect lines in the image
lines = lsd.detect(img)[0] #Position 0 of the returned tuple are the detected lines

#Draw the detected lines
drawn_img = lsd.drawSegments(img,lines)

#Save the image with the detected lines
cv2.imwrite('lsdsaved.png', drawn_img)
