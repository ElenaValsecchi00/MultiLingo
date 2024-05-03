# app.py

from flask import Flask
from flask import  jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@app.route('/', methods=['POST'])
@app.route('/', methods=['DELETE'])
@app.route('/', methods=['PUT'])

def get_users():
    print("Using jsonify")
    users = [{'id': 1, 'username': 'sweety'},
             {'id': 2, 'username': 'pallavi'}]
    response = jsonify({'users': users})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
 
 
if __name__ == '__main__':
    app.run()
