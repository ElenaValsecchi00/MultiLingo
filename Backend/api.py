# app.py

from flask import Flask, request
from flask import  jsonify
from flask_cors import CORS
import time

import speech_recognition as sr
from googletrans import Translator, constants
from pprint import pprint
import random
from random import shuffle
import pyttsx3

translator = Translator(service_urls=['translate.googleapis.com'])
language = ""
#key:ex, value = list of tuples (phrase, word possition of guessed word)
lev1_phrases = {"1": [("My mother is a good hiker", 2),("Elena had the chicken pox when she was six",1), ("See this cat, it is striped",1),
                       ("My mother is one amongst english teachers of the school",3)]}
lev1_options = {"1":[("are", "have"),("was", "have"), ("there", "these"), ("a", "the")]}
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin: *'


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
    return response

if __name__ == '__main__':
    app.run()
