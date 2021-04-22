import os
#run image acquisition
print("starting...")

print("acquiring image...")
os.system('python acquireimage.py')
print("image acquired")

print("preprocessing image...")
#run preprocessor
os.system('python prepro.py')

print("running ocr...")
#run ocr
os.system('python ocr.py')

print("running spell correction...")
#run spell correction
#os.system('python spell.py')
os.system('python sym1.py')

print("running text to speech convertor...")
#run tts
os.system('python tts4.py')
