from PIL import Image
import pytesseract
import re
#import pandas as pd
#from io import StringIO
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
temp1 = text
temp2 = text_im3
#templ = re.sub('\W',' ',temp1)
templ = re.sub('[^0-9a-zA-Z]', ' ', temp1)
temp1 = re.sub("[!#$%&'()*+-:;<=>?@^_`\\]{|}~]", '', temp1)
temp2 = re.sub("[!#$%&'()*+-:;<=>?@^_`\\]{|}~]", '', temp2)
#temp2 = re.sub('\W', ' ', temp2)

if (len(temp1) <= len(temp2)):
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
    text2 = pytesseract.image_to_string(img, lang='eng', config=tessdata_dir_config)
    #print(textdata)
    temp_text = text2
    temp1 = re.sub("[!#$%&'()*+-:;<=>?@^_`\\]{|}~]", '', temp1)
    temp_text = temp_text.replace('\n',' ')
    temp_text = re.sub('\W',' ',temp_text)
    temp_text = re.sub('\s+','',temp_text)
    temp_text = temp_text.replace(' ','')
    temp1 = temp1.replace(' ', '')
    temp1 = temp1.replace('\n',' ')
    temp1 = re.sub('\s+', '', temp1)
    #print('temp text:'+temp_text)
    #print('temp1'+temp1)
    if len(temp1) < len(temp_text):
        text = text2
        temp1 = text
        
    #if len(text) <= len(textdata):
    #    text = textdata
    
#remove unwanted chars recognised by ocr
text = text.replace('_',' ')
text = text.replace("'",'')
text = text.replace('‘','')
text = text.replace('\n',' ')
#to remove extra spaces
text = text.replace('|', '').replace('[',' ').replace(']',' ')
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


'''
textdata = pytesseract.image_to_data(img, lang='eng',config=tessdata_dir_config)
mon = pd.read_csv(StringIO(textdata),sep=r'\s',lineterminator=r'\n',engine='python')
#list2 = mon['text']
df = pd.DataFrame(mon, columns=['text'])
list2 = df.values.tolist()
list2 = [item for elem in list2 for item in elem]
cnt = 0
textdata = ''
for i in list2:
    if i == None:
        list2[cnt] = ' '
    cnt += 1
textdata = ' '.join(str(list2))
textdata = re.sub('\s+',' ',textdata)
'''
