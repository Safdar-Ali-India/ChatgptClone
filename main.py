from flask import Flask, render_template,jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api', methods=("GET","POST"))
def qa():
    if request.method == "POST":
        data = {"result":"I'm glad to hear that you find ChatGPT helpful! As an AI language model, my purpose is to assist and provide information to the best of my abilities. If you have any questions or need assistance with anything specific, feel free to ask, and I'll do my best to help you."}
        return jsonify(data)
    data = {"result":"I'm glad to hear that you find ChatGPT helpful! As an AI language model, my purpose is to assist and provide information to the best of my abilities. If you have any questions or need assistance with anything specific, feel free to ask, and I'll do my best to help you."}
    
    return jsonify(data)

app.run(debug =True)