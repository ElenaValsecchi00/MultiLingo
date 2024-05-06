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
ex1_phrases = ["il gatto è...tappeto","L'oca è...tavolo"]

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def choose_and_translate():
    phrase = ex1_phrases[random.randrange(0,2)]
    translation = translator.translate(phrase,src="it", dest=language)
    return translation.text

@app.route('/')
def get_users():
    print("Using jsonify")
    users = [{'id': 1, 'username': 'sweety'},
             {'id': 2, 'username': 'pallavi'}]
    response = jsonify({'users': users})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return users


@app.route("/language", methods=["POST"])
def language():
    context = request.get_json(force=True)
    global language
    language = context["language"]
    return language

@app.route("/language", methods=["GET"])
def get_phrase():
    phrase = choose_and_translate()
    response = jsonify({'phrase': phrase})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return phrase



 
if __name__ == '__main__':
    app.run()
