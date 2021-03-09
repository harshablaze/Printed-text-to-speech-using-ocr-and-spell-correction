# importing the pyttsx library
import pyttsx3
import os
# initialisation
engine = pyttsx3.init('SAPI.SpVoice',bool)

# testing
engine.say("My first code on text-to-speech")
engine.say("Thank you, Geeksforgeeks")
engine.runAndWait()
