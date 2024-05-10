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


translator = Translator()
language = ""
lev1_phrases_wait = {"1":["Guarda questo gatto, è a strisce","Mia madre è una tra le insegnanti di inglese della scuola"]}
lev1_options_wait = {"1":[("questo","questi","quelli"),("una","uno","la")]}
lev1_phrases = {"1": ["My mother is a good hiker","I had the chicken pox when I was six", "Look at this cat, it is striped",
                       "My mother is one amongst english teachers of the school"]}
lev1_options = {"1":[("is", "are", "have"),("had", "was", "have"), ("this", "there", "these"), ("one", "a", "the")]}
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



# Download and install Argos Translate package
#argostranslate.package.update_package_index()
#available_packages = argostranslate.package.get_available_packages()
#package_to_install = next(
#    filter(
#        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
#    )
#)
#argostranslate.package.install_from_path(package_to_install.download())



#function that chooses the phrase and corresponding options and translate them in the right lanuage
def choose_and_translate():
    index = random.randrange(0,len(lev1_phrases["1"]))
    phrase = lev1_phrases["1"][index]
    options = lev1_options["1"][index]
    #translation_phrase = translator.translate(phrase,src="en", dest=language)
    # Translate
    to_code = language
    from_code = "en"
    translatedText = argostranslate.translate.translate(phrase, from_code, to_code)
    print(translatedText)
    translation_options = [argostranslate.translate.translate(i,from_code, to_code) for i in options]
    return translatedText, translation_options

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
    #dict key:number of option, value:parola
    d = {str(i):opt for (i,opt) in zip(range(len(options)),options)}
    d['phrase']=phrase
    response = jsonify(d)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return d

 
if __name__ == '__main__':
    app.run()
