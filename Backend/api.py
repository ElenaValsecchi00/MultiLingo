# app.py

from flask import Flask
from flask import  jsonify
from flask_cors import CORS

import speech_recognition as sr
from googletrans import Translator, constants
from pprint import pprint
import pyttsx3

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


@app.route('/', methods=['POST'])
def post_language(data):
    data = data.load(data)
    print(data)
    return(data)



 
if __name__ == '__main__':
    app.run()
