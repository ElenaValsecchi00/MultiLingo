import speech_recognition as sr
from googletrans import Translator, constants
from pprint import pprint
import pyttsx3

rec = sr.Recognizer()
mic = sr.Microphone()
afile = sr.AudioFile('audio_files/rec5.wav')
translator = Translator()

with mic as source:
    print("Parla, sciocca!")
    audio = rec.listen(source)
    #audio = rec.record(source)
try:
    # recognize speech using Google Speech Recognition
    value = rec.recognize_google(audio, language="fr-FR")
    print("You said {}".format(value))
except sr.UnknownValueError:
    print("Oops! Didn't catch that")
except sr.RequestError as e:
    print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))


translation = translator.translate(value,src="fr", dest="it")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.say(translation.text)
engine.runAndWait()