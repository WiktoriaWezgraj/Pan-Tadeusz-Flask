from app import app
import requests
from flask import render_template, redirect

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ksiega1")
def ksiega1():
    return render_template("ksiega1.html")

@app.route("/ksiega2")
def ksiega2():
    return render_template("ksiega2.html")

@app.route("/ksiega3")
def ksiega3():
    return render_template("ksiega3.html")
