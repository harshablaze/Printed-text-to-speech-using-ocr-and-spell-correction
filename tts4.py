import pyttsx
from pyttsx import driver
from pyttsx import engine
def onStart():
    print('starting')

def onWord(name, location, length):
    print('word', name, location, length)

def onEnd(name, completed):
    print('finishing', name, completed)

engine = pyttsx.init('sapi5.py')

engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)

sen = 'Geeks for geeks is a computer portal for Geeks'


engine.say(sen)
engine.runAndWait()
