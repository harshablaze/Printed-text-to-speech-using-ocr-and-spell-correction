import cv2

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#cv2.namedWindow("capture image with printed text")
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("capture image with printed text", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        #save default image when image is not acquired
        image = cv2.imread('./images/sample3.jpg')
        #img_name = "./images/sample_0.jpg"
        cv2.imwrite('./images/sample_0.jpg', image)
        break
    elif k%256 == 32:
        # SPACE pressed
        #img_name = "sample_0.jpg"
        cv2.imwrite('./images/sample_0.jpg', frame)
        print("image saved successfully")
        break
cam.release()

cv2.destroyAllWindows()
 
