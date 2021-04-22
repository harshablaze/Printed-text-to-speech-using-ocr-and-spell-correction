from PIL import Image
import pytesseract
import re
#not needed
import cv2

#pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'.\Tesseract-OCR\tesseract.exe'
#use above path when tesseract is moved to current project directory
im = Image.open('images/test2-3.jpg')
#im = Image.open('images/sample12.jpg')
#sample4.jpg   test2-3.jpg

# Example config: r'--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR\tessdata"'
# It's important to add double quotes around the dir path.

#tessdata_dir_config = r'--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
tessdata_dir_config = r'--tessdata-dir ".\Tesseract-OCR\tessdata"'
#use above path when tesseract is moved to current project directory

text = pytesseract.image_to_string(im, lang='eng', config=tessdata_dir_config)

#text = pytesseract.image_to_string(im, lang = 'eng')

print(text)
#remove unwanted chars recognised by ocr
text = text.replace('\n',' ')
text = text.replace(':','   ')
text = text.replace(',',' ')
text = text.replace('.','  ')
text = text.replace('_',' ')

#to remove extra spaces
text=re.sub('\s+',' ',text)

#to remove chars not in [A-Z] [a-z] [0-9] and , . @ $ % & ! # () = + ? / <> {}



print(text)
#print text data to txt Files
outFileName="text.txt"
outFile=open('text.txt', "w")
outFile.write(text)
outFile.close()
