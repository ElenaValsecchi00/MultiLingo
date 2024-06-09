# app.py

from flask import Flask, request, redirect
from flask import  jsonify
from flask_cors import CORS

import speech_recognition as sr
from googletrans import Translator
import pyttsx3

import random
from random import shuffle
from Levenshtein import distance
import spacy
import time
import language_tool_python

tool = language_tool_python.LanguageTool('en')
keywords = [("confirm", 1), ("back", 1), ]

translator = Translator(service_urls=['translate.googleapis.com'])
rec = sr.Recognizer()
mic = sr.Microphone()

language = ""
audio = None
expected_sen = ""
right_answer = ""
def dummy(wait_for_stop):
    print("")
class Back():
    def __init__(self):
        self.back_active = False
stop_in_back = dummy
back = Back()
trigger_word = ""
results1_1 = 0
results1_2 = 0
results1_3 = 0

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
lev2_phrases = {"1": [("This hat really suits me"),("I would love to go out with you"), ("I wish I could speak French")]}

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
        print('tradotta')
    if ex=="2":
        right_option = phrase_list[ex][index][1]
        translation_phrase, translation_options= substitute_with_blank(translation_phrase, translation_options, right_option)

    return translation_phrase, translation_options

#function that records an audio file 
def record():
    global stop_in_back
    mic = sr.Microphone()
    rec = sr.Recognizer()
    with mic as source:
        rec.adjust_for_ambient_noise(source)
        global audio
        audio = rec.listen(source, timeout=3000, phrase_time_limit=20000)
    stop_in_back = rec.listen_in_background(mic, callback)
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

def callback(recognizer, audio):  # this is called from the background thread
    try:
        speech_as_text = recognizer.recognize_google(audio, language = language)
        print(speech_as_text)
        confirm_trigger = "conferma" if language=="it" else "confirma" if language=="es" else "confirm" if language=="en" else "confirme"
        back_trigger = "indietro" if language=="it" else "atras" if language=="es" else "back" if language=="en" else "derrière"
          
        # Look for your "trigger" keyword in speech_as_text
        if confirm_trigger in speech_as_text.lower():
            trigger("confirm")
            #go to next page
        elif back_trigger in speech_as_text.lower():
            trigger("back")
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")


def trigger(trigger):
    global trigger_word, back
    trigger_word=trigger
    #stops the listenng and sets back.back_active to false
    stop_in_back(wait_for_stop=False)
    back.back_active=False
    # interpret the user's words however you normally interpret them


@app.route("/background", methods=["POST"])
#start to listen in background
def start_recognizer():
    global stop_in_back, back
    stop_in_back(wait_for_stop=False)#every time the function gets called, it restarts the listening in bakcground process
    back.back_active = True
    stop_in_back = rec.listen_in_background(mic, callback)
    while back.back_active:
        time.sleep(1.0) # we're still listening even though the main thread is blocked
    #it returns only when back_active is set to false
    return jsonify({"url":trigger_word})

@app.route("/lev2/getLanguage", methods=["POST"])
def get_language():
    context = request.get_json(force=True)
    global startingLanguage
    startingLanguage = context["startingLanguage"]
    return startingLanguage

@app.route("/lev1/phrases", methods=["GET"])
#get the text of exercise
def get_phrase():
    phrase,options = choose_and_translate(lev1_phrases,lev1_options,request.args.get('ex',''))
    #dict key:number of option, value:parola
    d = {str(i):opt for (i,opt) in zip(range(len(options)),options)}
    d['phrase']=phrase
    response = jsonify(d)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response 
    
@app.route("/lev1/ex1/record", methods=["POST"])
#record audio
def record_audio():
    global audio
    stop_in_back(wait_for_stop=False)
    audio = record()
    return jsonify("andato a buon fine")

@app.route("/lev1/ex1/audio", methods=["GET"])
#speech to text
def textify_audio():
    text_of_speech = speech_to_text(audio)
    options = text_of_speech.split()
    global results1_1
    try:
        #check if word has been pronounced correctly
        if is_sentence_correct(text_of_speech):
            results1_1 += 0.5
            print(results1_1)
            response = jsonify(True)
            response.headers["Access-Control-Allow-Origin"] = "*"
            return response
        else: return jsonify(False)
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
        return jsonify("Oops! Didn't catch that")

@app.route("/lev1/ex1_2/check", methods=["POST"])
#record audio
def check():
    data = request.get_json()
    global results1_1, results1_2
    #check if clicked option is correct
    if(data["data"] == right_answer):
        ex = request.args.get('ex','')
        if ex == "1":
            results1_1 += 0.5
        else:
            results1_2 = 1
        return jsonify(True)
    else:
        return jsonify(False)



@app.route("/lev1/ex3/answer", methods=["POST"])
#see if expected stentence is matched
def get_result():
    submitted_phrase = request.get_json()['phrase']
    global results1_3
    if submitted_phrase.strip()==expected_sen:
        results1_3 = 1
        return jsonify(True)
    else:
        return jsonify(False)


@app.route("/lev1/pronounce", methods=["GET"])
def prononuce_phrase():
    #pronounce the sentence
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(expected_sen)
    engine.runAndWait()
    return jsonify("success")

@app.route("/lev2/pronounce", methods=["GET"])
def pron_phrase_2():
    #pronounce the sentence
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    index = random.randrange(0,len(lev2_phrases["1"]))
    phrase = lev2_phrases["1"][index] 
    phrase = translator.translate(phrase,src="en", dest=startingLanguage).text
    engine.say(phrase)
    engine.runAndWait()
    return jsonify("success")

nlp = spacy.load("en_core_web_sm")
#it_core_news_sm
answers = {
    "tool": ["hammer", "shovel", "scissor"],
    "clothe": ["shirt", "trouser", "dress"],
    "fruit": ["apple", "banana", "pear"]
}
def reveal_list(doc):
    for token in doc:
        if token.lemma_ in answers:
            answers_type = token.lemma_
            answers_list = ", ".join(answers[answers_type])
            return f"Which kind of {answers_type} do you want to buy ? We currently have these available: {answers_list}."
    return "I couldn't understand. Can you repeat?"

@app.route("/lev3/conversation", methods=["POST"])
def handle_input():
    phrase = request.get_json()
    phrase = phrase["data"]
    if phrase==None:
        phrase=""
    if phrase.lower() in ["bye", "goodbye"]:
        return jsonify("Goodbye!")
    else:
        doc = nlp(translator.translate(phrase.lower(),src=language, dest="en").text)
        #for token in doc: print(token.lemma_)
        answer = ""
        if any(token.lemma_ in ["tool", "clothe", "fruit"] for token in doc):
            answer = reveal_list(doc)
        elif any(token.lemma_ in answers["tool"] or token.lemma_ in answers["clothe"] or token.lemma_ in answers["fruit"] for token in doc):
            answer = "How many pieces do you need?"
        elif any(token.lemma_ in [str(i) for i in range(1000)]  for token in doc):
            answer = "Are you sure? Would you like to pay cash or by card?" 
        elif any(token.lemma_ in ["cash", "card"] for token in doc):
            answer = "Ok, thanks for the purchase. Have a nice day!"
        else: 
            answer = "I didn't understand. Can you repeat?"   
        return translator.translate(answer,src="en", dest=language).text

@app.route("/lev3/conversation", methods=["GET"])
#get the tedxt of the message in level 3
def get_pronounced_phrase():
    text_of_speech = speech_to_text(audio)
    matches = tool.check(text_of_speech)[1:]
    errors = ""
    for match in matches:
       errors+=match.message
    response = {"data": text_of_speech, "numerrors": len(matches), "errors": errors}
    return response

@app.route("/lev3/record", methods=["POST"])
#record the message in level 3
def record_lev3():
    global audio
    audio = record()
    return jsonify("Registrato")

@app.route("/lev2/phrases", methods=["GET"])
#get the text of exercise
def get_phrase_2():
    ex = request.args.get('ex','')
    index = random.randrange(0,len(lev2_phrases[ex]))
    phrase = lev2_phrases[ex][index] 
    translation_phrase = translator.translate(phrase,src="en", dest=startingLanguage)
    print(startingLanguage, language)
    response = jsonify(translation_phrase.text)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response 

@app.route("/lev1/results", methods=["GET"])
def lev1Results():
    results = {}
    results["1"] = results1_1
    results["2"] = results1_2
    results["3"] = results1_3
    response = jsonify(results)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response 

if __name__ == '__main__':
    app.run()
