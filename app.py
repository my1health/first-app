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

@app.route("/<name>")
def hello(name):
    
    return f"Hello {escape(name)}!"

    #return f"Hello {name}!"

@app.route("/user/<username>")
def sup(username):

    return f"User {escape(username)}"

@app.route("/post/<int:pid>")
def sp(pid):

    return f"Post {escape(pid)}"

@app.route("/path/<path:spw>")
def ssp(spw):

    return f"Subpath {escape(spw)}"

@app.route("/login", methods= ["POST", "GET"])
def ulogin():
    err= None
    if req.method == "POST":
        #fo= req.form
        #fo= req.form.items()
        #fo= fo.send(None)
        #help(fo)
        #print(dir(fo))
        us= escape(req.form.get("username"))
        pa= escape(req.form.get("password"))
        check_login()
        #print("\n{}, {}\n".format(us, pa))
        return "<h1>You have been logged in</h1>"
    return "<h1>ERROR</h1>"
def check_login(user, passw):
    print("Check Login")

if __name__ == "__main__":
    app.run(debug= True)
