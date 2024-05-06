# app.py

from flask import Flask, request
from flask import  jsonify
from flask_cors import CORS

import speech_recognition as sr
from googletrans import Translator, constants
from pprint import pprint
import random
import pyttsx3

translator = Translator()
language = ""
ex1_phrases = {"1":["Guarda ... gatto, è a strisce","Mia madre è ... tra le insegnanti di inglese della scuola"]}
ex1_options = {"1":[("questo","questi","quelli"),("una","uno","la")]}

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#function that chooses the phrase and corresponding options and translate them in the right lanuage
def choose_and_translate():
    index = random.randrange(0,2)
    phrase = ex1_phrases["1"][index]
    options = ex1_options["1"][index]
    translation_phrase = translator.translate(phrase,src="it", dest=language)
    translation_options = [translator.translate(i,src="it", dest=language).text for i in options]
    return translation_phrase.text, translation_options

@app.route('/')
def get_users():
    print("Using jsonify")
    users = [{'id': 1, 'username': 'sweety'},
             {'id': 2, 'username': 'pallavi'}]
    response = jsonify({'users': users})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return users


@app.route("/ex1", methods=["POST"])
#post the language that the user has selected
def language():
    context = request.get_json(force=True)
    global language
    language = context["language"]
    return language

@app.route("/ex1", methods=["GET"])
#get the text of exercise
def get_phrase():
    phrase,options = choose_and_translate()
    d = {str(i):opt for (i,opt) in zip(range(len(options)),options)}
    d['phrase']=phrase
    response = jsonify(d)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return d


 
if __name__ == '__main__':
    app.run()
