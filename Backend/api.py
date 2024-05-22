# app.py

from flask import Flask, request
from flask import  jsonify
from flask_cors import CORS

import speech_recognition as sr
from googletrans import Translator
import pyttsx3

import random
from random import shuffle
from Levenshtein import distance


translator = Translator(service_urls=['translate.googleapis.com'])
rec = sr.Recognizer()

language = ""
audio = None
expected_sen = ""

#key:ex, value = list of tuples (phrase, word position of guessed word) for ex 1, for ex 3 (phrase,None)
lev1_phrases = {"1": [("My mother is a good hiker", 2),("Elena had chicken pox when she was six",1), ("See this cat, it is striped",1),
                       ("My mother is one amongst the english teachers of the school",3)],
                "3":[("life is full of crossroades",None),("I have been in this queue for ages",None),
                     ("are you joking? This can not be real!",None)],
                "2":[("My favourite color is green",4), ("I really like working out",2),("I just adopted a dog",4)]}
lev1_options = {"1":[("are", "have"),("was", "have"), ("there", "these"), ("a", "the")],
                "3":[("dive", "are", "fool", "you"),
                     ("due", "of", "these","dude"),
                     ("that", "could", "pounding", "deal","He")],
                "2":[("yellow", "red"),("enjoy","don't like"), ("child","cat")]}
UPLOAD_FOLDER = 'audios'

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#computes the similarity between the expected sentence and the pronunciated one
def is_sentence_correct(actual_sen):
    dist = distance(expected_sen,actual_sen)
    return dist < 5

#split, substitute element with ... and recompose
def substitute_with_blank(translation_phrase, translation_options, right_option):
    translation_phrase=translation_phrase.text.split()
    translation_options.append(translation_phrase[right_option])
    #set the right answer as phrase
    global right_answer
    right_answer = translation_phrase[right_option]
    shuffle(translation_options)
    translation_phrase[right_option]="..."
    translation_phrase = " ".join(translation_phrase)
    return translation_phrase, translation_options
    
#function that chooses the phrase and corresponding options and translate them in the right lanuage
def choose_and_translate(phrase_list,options_list, ex):
    index = random.randrange(0,len(phrase_list[ex]))
    phrase = phrase_list[ex][index][0] 
    options = options_list[ex][index]
    translation_options = [str(translator.translate(i,src="en", dest=language).text).lower() for i in options]
    translation_phrase = translator.translate(phrase,src="en", dest=language)
    #sets the expected sentence to be guessed by the user
    global expected_sen
    expected_sen = translation_phrase.text
    #depending on the level gives out the right phrase and options
    if ex=="1":
        right_option = phrase_list[ex][index][1]
        translation_phrase, translation_options= substitute_with_blank(translation_phrase, translation_options, right_option)
    if ex=="3":
        translation_options.extend(translation_phrase.text.split())
        shuffle(translation_options)
        translation_phrase = translation_phrase.text
    if ex=="2":
        right_option = phrase_list[ex][index][1]
        translation_phrase, translation_options= substitute_with_blank(translation_phrase, translation_options, right_option)

    return translation_phrase, translation_options

#function that records an audio file 
def record():
    mic = sr.Microphone()
    
    with mic as source:
        rec.adjust_for_ambient_noise(source)
        global audio
        audio = rec.listen(source, timeout=3000, phrase_time_limit=20000)
    return audio

#function that transcribes the audio file
def speech_to_text(audio):      
    try:
        # recognize speech using Google Speech Recognition
        value = rec.recognize_google(audio, language=language)
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

@app.route("/lev1/phrases", methods=["GET"])
#get the text of exercise
def get_phrase_ex1():
    phrase,options = choose_and_translate(lev1_phrases,lev1_options,request.args.get('ex',''))
    #dict key:number of option, value:parola
    d = {str(i):opt for (i,opt) in zip(range(len(options)),options)}
    d['phrase']=phrase
    response = jsonify(d)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response 
    
@app.route("/lev1/ex1/audio", methods=["POST"])
#record audio
def record_audio():
    global audio
    global score
    data = request.get_json()
    audio = record()
    return jsonify(True) if(data["data"] == right_answer) else jsonify(False)
    #return data

@app.route("/lev1/ex1/audio", methods=["GET"])
#speech to text
def textify_audio():
    text_of_speech = speech_to_text(audio)
    options = text_of_speech.split()
    try:
        #check if word has been pronounced correctly
        if is_sentence_correct(text_of_speech):
            response = jsonify(True)
            response.headers["Access-Control-Allow-Origin"] = "*"
            return response
        else: return jsonify(False)
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
        return jsonify("Oops! Didn't catch that")
    
@app.route("/lev1/ex3", methods=["GET"])
def get_phrase_ex3():
    phrase,options = choose_and_translate(lev1_phrases,lev1_options,"3")
    d = {str(i):opt for (i,opt) in zip(range(len(options)),options)}
    d['phrase']=phrase
    response = jsonify(d)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route("/lev1/ex3/answer", methods=["POST"])
def get_result():
    submitted_phrase = request.get_json()['phrase']
    if submitted_phrase.strip()==expected_sen:
        return jsonify("Corretto")
    else:
        return jsonify("Sbagliato")


@app.route("/lev1/pronounce", methods=["GET"])
def prononuce_phrase():
    #pronounce the sentence
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(expected_sen)
    engine.runAndWait()
    return jsonify("success")

      
if __name__ == '__main__':
    app.run()
