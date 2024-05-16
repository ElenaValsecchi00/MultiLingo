# app.py

from flask import Flask, request, redirect, url_for
from flask import  jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

import speech_recognition as sr
from googletrans import Translator, constants
from pprint import pprint
import random
from random import shuffle
import speech_recognition as sr

rec = sr.Recognizer()
translator = Translator(service_urls=['translate.googleapis.com'])
language = ""

#key:ex, value = list of tuples (phrase, word possition of guessed word)
lev1_phrases = {"1": [("My mother is a good hiker", 2),("Elena had the chicken pox when she was six",1), ("See this cat, it is striped",1),
                       ("My mother is one amongst english teachers of the school",3)]}
lev1_options = {"1":[("are", "have"),("was", "have"), ("there", "these"), ("a", "the")]}
UPLOAD_FOLDER = 'audios'

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#function that chooses the phrase and corresponding options and translate them in the right lanuage
def choose_and_translate():
    index = random.randrange(0,len(lev1_phrases["1"]))
    phrase = lev1_phrases["1"][index][0]
    right_option = lev1_phrases["1"][index][1]
    options = lev1_options["1"][index]
    translation_options = [str(translator.translate(i,src="en", dest=language).text).lower() for i in options]
    translation_phrase = translator.translate(phrase,src="en", dest=language)
    #split, substitute element with ... and recompose
    translation_phrase=translation_phrase.text.split()
    translation_options.append(translation_phrase[right_option])
    shuffle(translation_options)
    translation_phrase[right_option]="..."
    translation_phrase = " ".join(translation_phrase)
    
    return translation_phrase, translation_options

#funtion that takes an audio file and transcribe it
def speech_to_text(audio):
    audio = sr.AudioFile(audio)
    with audio as source:
        audio = rec.record(audio)
        try:
            # recognize speech using Google Speech Recognition
            value = rec.recognize_google(source, language=language)
            return value
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
            return None
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            return None

@app.route("/", methods=["POST"])
#post the language that the user has selected
def postLanguage():
    context = request.get_json(force=True)
    global language
    language = context["language"]
    return language

@app.route("/lev1/ex1", methods=["GET"])
#get the text of exercise
def get_phrase():
    phrase,options = choose_and_translate()
    #dict key:number of option, value:parola
    d = {str(i):opt for (i,opt) in zip(range(len(options)),options)}
    d['phrase']=phrase
    response = jsonify(d)
    return response

@app.route("/lev1/ex1/audio", methods=["GET"])
#get the text of exercise
def get_audio():
    #filename = secure_filename(request.args.get('yourfilename.wav'))       
    text = speech_to_text(app.config['UPLOAD_FOLDER']+"/"+"yourfilename.wav")
    return jsonify(text)

@app.route("/lev1/ex1/audio", methods=["POST"])
def post_audio():
    file = request.files['audio']
    file.save(app.config['UPLOAD_FOLDER']+"/"+file.filename)
    return redirect(url_for('get_audio', name=file.filename))

if __name__ == '__main__':
    app.run()
