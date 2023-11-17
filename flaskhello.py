from flask import Flask
from flask import render_template

apphello = Flask(__name__)

@apphello.route("/")
def hello_world():
    return "<h1>Hello World!!</h1>"

@apphello.route("/alpro")
def helloalpro():
    return "<h2>Alpro sulit??</h2>"

@apphello.route("/initemplate")
@apphello.route("/initemplate/<name>")
def templaterun(name=None):
    return render_template("temps.html", name=name)
