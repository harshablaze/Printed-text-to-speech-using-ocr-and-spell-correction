"""
import pyttsx
# import engineio #engineio module is not needed.

engineio = pyttsx.init()
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 130)    # Aquí puedes seleccionar la velocidad de la voz
engineio.setProperty('voice',voices[1].id)

def speak(text):
    engineio.say(text)
    engineio.runAndWait()

speak("What do you want me to say?")
while(1):
    phrase = input("--> ")
    if (phrase == "exit"):
        exit(0)
    speak(phrase)
    print(voices)
"""

from espeakng import ESpeakNG
esng = ESpeakNG()
esng.say('Hello World')
"""
esng.pitch = 32 esng.speed = 150 esng.say('Hello World!')
esng.voice = ‘german’ esng.say('Hallo Welt!')
"""
"""
import wave
import io
from espeak import ESpeakNG
esng=ESpeakNG()
esng.voice='english-us'
wavs = esng.synth_wav('Hello World!')
wav = wave.open(StringIO.StringIO(wavs))
print(wav.getnchannels(), wav.getframerate(), wav.getnframes())
"""
