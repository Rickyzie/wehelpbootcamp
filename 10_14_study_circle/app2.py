from flask import Flask
from flask import render_template
from flask import Response
from markupsafe import escape
from flask_cors import CORS
from flask import Flask, session

app = Flask(__name__)


@app.route('/')
def set():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000, debug = True) 