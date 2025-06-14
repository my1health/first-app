from flask import Flask, render_template as r
from flask import request as req

from markupsafe import escape

import json
import hashlib as h
import os

app= Flask(__name__)

@app.route("/")
def hello_world():

    return r("index.html")

@app.route("/writeups/wiseguy.html")
def wiseguy():
    return r("wiseguy.html")

@app.route("/en/symptoms/")
def symp():
    
    return r("symptoms.html")

def check_login(user, passw):
    print("Check Login")

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 10000)
