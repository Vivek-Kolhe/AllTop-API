from flask import Flask, jsonify, request
from alltop import get_data, viral
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "I_was_bored"
CORS(app)

@app.route('/')
def home():
    return "API UP!"

@app.route('/news')
def news():
    if request.method == 'GET':
        category = request.args.get("category")
        return jsonify(get_data(category))

@app.route('/viral')
def viral_articles():
    if request.method == 'GET':
        return jsonify(viral())

if __name__ == '__main__':
    app.debug = True
    app.run()
