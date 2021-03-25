from PIL import Image
import pytesseract

#not needed
import cv2

#pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'.\Tesseract-OCR\tesseract.exe'
#use above path when tesseract is moved to current project directory
im = Image.open('test2-3.jpg')
#sample4.jpg

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
print(text)
#print text data to txt Files
outFileName="text.txt"
outFile=open('text.txt', "w")
outFile.write(text)
outFile.close()
