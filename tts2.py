# importing the pyttsx library
import pyttsx3

# initialisation
engine = pyttsx3.init()
inFile=open('text.txt', "r")
text=inFile.read()

#remove new line tags
text = text.replace('\n',' ')

# testing
engine.say(text)
engine.runAndWait()

