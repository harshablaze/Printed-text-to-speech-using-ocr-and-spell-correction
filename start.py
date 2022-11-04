import time
import os
import cv2
import warnings

def fun():
    try:
        start = time.time()
        #run image acquisition
        print("starting...")
        print("acquiring image...")
        os.system('python acquireimage.py')
        print("image acquired")
        start1 = time.time()
        os.system('python textdetect.py')
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
        end1 = time.time()
        start2 = time.time()
        print("running ocr...")
        #run ocr
        os.system('python ocr.py')
        words=''
        with open('text.txt', 'r') as file:
            words = file.read().replace('\n', '')
        words=words.replace(' ','')
        end2 = time.time()
        start3 = time.time()
        if len(words) == 0 :
            print('no text detected \n exiting..')
        else :
            os.system('python names.py')
            
            #os.system('python nameidentifier.py')

            print("running spell correction...")
            #run spell correction
            #os.system('python spell.py')
            os.system('python sym1.py')
            end3 = time.time()
            print("running text to speech convertor...")
            #run tts
            os.system('python tts4.py')

        end = time.time()
        print(f'preprocessing: {int(end1 - start1)} seconds')
        print(f'character recognition: {int(end2 - start2)} seconds')
        if len(words) != 0:
            print(f'postprocessing: {int(end3 - start3)} seconds')
        print(f'Runtime: {int(end - start)} seconds')

    except:
        print (" An error occurred")

paths = ['./output', './roi' , './crop' , './prepro']

for path in paths:
    if not os.path.exists(path):
        os.makedirs(path)
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fun()