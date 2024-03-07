from flask import Flask, request, render_template, redirect, url_for
from morse_code import *

app = Flask(__name__)

@app.route("/", methods=["get" ,"post"])
def encodeMessage():
    if request.method == "POST":
        message = request.form.get("message") if request.form.get("message") else ""
        code = generateMorseCode(message)
        return render_template("index.html", message=message, morse_code=code)
    return render_template("index.html", message="", morse_code="")

@app.route("/decode", methods=["get", "post"])
def decodeMessage():
    if request.method == "POST":
        code = request.form.get("code") if request.form.get("code") else ""
        message = decodeMorseCode(code)
        return render_template("decode.html", message=message, morse_code=code)
    return render_template("decode.html" ,message="", morse_code="")

if __name__ == "__main__":
    app.run(debug=True)