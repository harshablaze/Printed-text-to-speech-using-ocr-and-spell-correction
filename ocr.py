from PIL import Image
import pytesseract

#not needed
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
im = Image.open('test1.jpg')
#C:\sample2.jpg

# Example config: r'--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR\tessdata"'
# It's important to add double quotes around the dir path.
tessdata_dir_config = r'--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
text = pytesseract.image_to_string(im, lang='eng', config=tessdata_dir_config)

#text = pytesseract.image_to_string(im, lang = 'eng')

print(text)


#print text data to txt Files
outFileName="text.txt"
outFile=open('text.txt', "w")
outFile.write(text)
outFile.close()
