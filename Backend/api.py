# app.py

from flask import Flask, request
from flask import  jsonify
from flask_cors import CORS

import speech_recognition as sr
from googletrans import Translator, constants
from pprint import pprint
import pyttsx3

language = ""

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


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
def get_language():
    print(language)
    response = jsonify({'language': language})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return language



 
if __name__ == '__main__':
    app.run()
