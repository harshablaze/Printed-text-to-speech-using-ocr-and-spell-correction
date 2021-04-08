import os

#run preprocessor
os.system('python prepro.py')
#run ocr
os.system('python ocr.py')

#run spell correction
#os.system('python spell.py')
os.system('python sym1.py')

#run tts
os.system('python tts4.py')
