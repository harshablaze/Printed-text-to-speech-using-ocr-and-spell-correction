from PIL import Image
import pytesseract
import re
#not needed
import cv2
import os
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
file_number = 0
for i in range(0,number_of_files):
    im = Image.open('prepro/test_{}.jpg'.format(file_number))
    im1 = Image.open('roi/Roi_{}.jpg'.format(file_number))
    #sample4.jpg   test2-3.jpg
    text_im = pytesseract.image_to_string(im, lang='eng', config=tessdata_dir_config)
    text_im1 = pytesseract.image_to_string(im1, lang='eng', config=tessdata_dir_config)
    if len(text_im) > len(text_im1):
        text += text_im
    else:
        text += text_im1

    #text = pytesseract.image_to_string(im, lang = 'eng')
    text += '.'
    file_number += 1

print(text)
#remove unwanted chars recognised by ocr
text = text.replace('\n',' ')
#text = text.replace(':','   ')
#text = text.replace(',',' ')

text = text.replace('_',' ')

#to remove extra spaces
text=re.sub('\s+',' ',text)
text = text.replace('/','   ')
#to remove chars not in [A-Z] [a-z] [0-9] and , . @ $ % & ! # () = + ? / <> {}



print(text)
#print text data to txt Files
outFileName="text.txt"
outFile=open('text.txt', "w")
outFile.write(text)
outFile.close()
