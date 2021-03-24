# importing the pyttsx library
import pyttsx3

# initialisation
engine = pyttsx3.init('sapi5')
inFile=open('text.txt', "r")
text=inFile.read()

#remove new line tags
text = text.replace('\n',' ')

# testing
engine.say(text)
engine.runAndWait()

