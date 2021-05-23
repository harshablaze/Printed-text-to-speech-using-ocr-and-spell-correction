from PIL import Image
import pytesseract
import re
#not needed
import cv2
import os
from os.path import isfile, join
from os import listdir
#import sys
#import codecs

#pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'.\Tesseract-OCR\tesseract.exe'
#use above path when tesseract is moved to current project directory
# Example config: r'--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR\tessdata"'
# It's important to add double quotes around the dir path.
#tessdata_dir_config = r'--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
tessdata_dir_config = r'--tessdata-dir ".\Tesseract-OCR\tessdata"'
#use above path when tesseract is moved to current project directory
text=''
list = os.listdir('./prepro/') # dir is your directory path
number_of_files = len(list)
print('No of images detected: '+ str(number_of_files))
im2 = Image.open('./output/sample00.jpg')
text_im3 = pytesseract.image_to_string(im2, lang='eng', config=tessdata_dir_config)
file_number = 0
for i in range(0,number_of_files):
    im = Image.open('prepro/test_{}.jpg'.format(file_number))
    im1 = Image.open('roi/Roi_{}.jpg'.format(file_number))
    #sample4.jpg   test2-3.jpg
    text_im1 = pytesseract.image_to_string(im, lang='eng', config=tessdata_dir_config)
    text_im2 = pytesseract.image_to_string(im1, lang='eng', config=tessdata_dir_config)
    if len(text_im1)>= len(text_im2):
        text += text_im1
    else:
        text += text_im2
    #text = pytesseract.image_to_string(im, lang = 'eng')
    #text += '.'
    file_number += 1
text = text.replace('\n',' ')
text_im3 =text_im3.replace('\n',' ')
if (len(text_im3)) > len(text):
    text = text_im3
#print(text)
text = text.replace('\n',' ')
#text = re.sub('[^0-9a-zA-Z.,-]',' ',text)
text = re.sub('\s+',' ',text)

#comparision of preprosed original image ,rois,tests completed
os.remove('./output/sample00.jpg')
mypath = './output/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print(onlyfiles)
for file in onlyfiles:
    img = cv2.imread('./output/{}'.format(file))
    temp_text = pytesseract.image_to_string(im, lang='eng', config=tessdata_dir_config)
    temp_text = temp_text.replace('\n',' ')
    temp_text = re.sub('\s+',' ',temp_text)
    if len(text) <= len(temp_text):
        text = temp_text
#remove unwanted chars recognised by ocr
text = text.replace('_',' ')
text = text.replace("'",'')
text = text.replace('‘','')
#to remove extra spaces
text=re.sub('\s+',' ',text)
text = text.replace('/','   ')
#to remove chars not in [A-Z] [a-z] [0-9] and , . @ $ % & ! # () = + ? / <> {}
print(text)
outFileName="text.txt"
outFile=open('text.txt', "w")
try:
    outFile.write(text)
except:
    text = text.encode('ascii', 'namereplace')
    text = text.decode()
    outFile.write(text)
outFile.close()
