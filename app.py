from flask import Flask, jsonify, request
from alltop import get_data, viral
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "I_was_bored"
CORS(app)

@app.route('/')
def home():
    jsonData = {"APIStatus" : "UP!", "codedBy" : "Made with ❤️ by Vivek.", "sourceCode" : "https://github.com/Vivek-Kolhe/AllTop-API", "reachMeAt" : "https://telegram.dog/pookie_0_0"}
    return jsonify(jsonData)

@app.route('/news')
def news():
    if request.method == 'GET':
        topic = request.args.get("topic")
        return jsonify(get_data(topic))

@app.route('/viral')
def viral_articles():
    if request.method == 'GET':
        return jsonify(viral())

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
