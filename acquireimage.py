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
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "sample_0.jpg"
        cv2.imwrite(img_name, frame)
        print("image saved successfully")
        break 
cam.release()

cv2.destroyAllWindows()
