# app.py

from flask import Flask, request
from flask import  jsonify
from flask_cors import CORS

import speech_recognition as sr
from googletrans import Translator, constants
from pprint import pprint
import random
import pyttsx3
import argostranslate.package
import argostranslate.translate

translator = Translator(service_urls=['translate.googleapis.com'])
language = ""
lev1_phrases_wait = {"1":["Guarda questo gatto, è a strisce","Mia madre è una tra le insegnanti di inglese della scuola"]}
lev1_options_wait = {"1":[("questo","questi","quelli"),("una","uno","la")]}
lev1_phrases = {"1": ["My mother is a good hiker","I had the chicken pox when I was six", "Look at this cat, it is striped",
                       "My mother is one amongst english teachers of the school"]}
lev1_options = {"1":[("is", "are", "have"),("had", "was", "have"), ("this", "there", "these"), ("one", "a", "the")]}
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin: *'


#function that chooses the phrase and corresponding options and translate them in the right lanuage
def choose_and_translate():
    index = random.randrange(0,len(lev1_phrases["1"]))
    phrase = lev1_phrases["1"][index]
    options = lev1_options["1"][index]
    translation_phrase = translator.translate(phrase,src="en", dest=language)
    print(translation_phrase)
    translation_options = [str(translator.translate(i,src="en", dest=language).text) for i in options]
    return translation_phrase.text, translation_options
    
@app.route('/')
def get_users():
    print("Using jsonify")
    users = [{'id': 1, 'username': 'sweety'},
             {'id': 2, 'username': 'pallavi'}]
    response = jsonify({'users': users})
    return users


@app.route("/ex1", methods=["POST"])
#post the language that the user has selected
def getLanguage():
    context = request.get_json(force=True)
    global language
    language = context["language"]
    return language

@app.route("/ex1", methods=["GET"])
#get the text of exercise
def get_phrase():
    phrase,options = choose_and_translate()
    #dict key:number of option, value:parola
    d = {str(i):opt for (i,opt) in zip(range(len(options)),options)}
    d['phrase']=phrase
    response = jsonify(d)
    response.headers.add("Access-Control-Allow-Origin: *")
    return response

if __name__ == '__main__':
    app.run()
