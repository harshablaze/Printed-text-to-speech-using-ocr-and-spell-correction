import os
import cv2
#run image acquisition
print("starting...")

print("acquiring image...")
os.system('python acquireimage.py')
print("image acquired")

#print("Enter input type:\n1.ID CARD \n2.SIGN BOARD \n 3.")

print("preprocessing image...")

os.system('python roi1.py')

list = os.listdir('./roi/') # dir is your directory path
number_of_files = len(list)

#check if roi returned images or not
if number_of_files == 0:
    image = cv2.imread('./images/sample_0.jpg')
    cv2.imwrite('./roi/ROI_0.jpg', image)

#run preprocessor
os.system('python prepro.py')

print("running ocr...")
#run ocr
os.system('python ocr.py')
words=''
with open('text.txt', 'r') as file:
    words = file.read().replace('\n', '')
words=words.replace(' ','')
if len(words) == 0 :
    print('no text detected \n exiting..')
else :
    os.system('python names.py')
    os.system('python nameidentifier.py')

    print("running spell correction...")
    #run spell correction
    #os.system('python spell.py')
    os.system('python sym1.py')

    print("running text to speech convertor...")
    #run tts
    os.system('python tts4.py')
