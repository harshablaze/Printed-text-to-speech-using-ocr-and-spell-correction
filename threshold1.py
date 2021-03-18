import cv2

# Load an color image in grayscale
img = cv2.imread('houghlines.jpg',0)
ret, thresh_img = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('grey image',thresh_img)
cv2.imwrite("result11.jpg", thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
