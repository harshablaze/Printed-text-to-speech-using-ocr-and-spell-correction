import cv2
from os import listdir
from os.path import isfile, join
mypath='./images/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in onlyfiles:
    name, format1 = file.split('.')
    if format1 == 'png':
        image = cv2.imread('./images/'+ name +'.png')
        cv2.imwrite('./images/'+ name +'.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    if format1 == 'jpeg':
        image = cv2.imread('./images/' + name + '.jpeg')
        cv2.imwrite('./images/' + name + '.jpg', image,
                    [int(cv2.IMWRITE_JPEG_QUALITY), 100])
