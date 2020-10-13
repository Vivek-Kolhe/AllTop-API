from flask import Flask, jsonify, request
from alltop import get_data
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "I_was_bored"
CORS(app)

@app.route('/')
def home():
    return "API UP!"

@app.route('/home')
def news():
    if request.method == 'GET':
        return jsonify(get_data())

if __name__ == '__main__':
    app.debug = True
    app.run()