import pyttsx3
engine = pyttsx3.init() # object creation

"""RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print ('speech rate:'+str(rate)+' words/min')                        #printing current voice rate
engine.setProperty('rate', 155)     # setting up new voice rate initial val 125


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. 0 for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


#read text from text file generated by ocr
inFile=open('corrected_text.txt', "r")
text=inFile.read()

#remove new line tags
text = text.replace('\n',' ')


engine.say(text)
#engine.say('My current speaking rate is ' + str(rate))
engine.say("     do you want to hear original text?    enter yes or no")
engine.runAndWait()
choice = input()
if choice == 'yes' or choice == 'y' or choice == 'Y':
    infile1=open('text.txt',"r")
    text=infile1.read()
    engine.say(text)
    engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file(text, 'test.mp3')
print("audio file saved successfully")
engine.runAndWait()