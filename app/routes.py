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

@app.route("/ksiega4")
def ksiega4():
    return render_template("ksiega4.html")

@app.route("/ksiega5")
def ksiega5():
    return render_template("ksiega5.html")

@app.route("/ksiega6")
def ksiega6():
    return render_template("ksiega6.html")

@app.route("/ksiega7")
def ksiega7():
    return render_template("ksiega7.html")

@app.route("/ksiega8")
def ksiega8():
    return render_template("ksiega8.html")

@app.route("/ksiega9")
def ksiega9():
    return render_template("ksiega9.html")

@app.route("/ksiega10")
def ksiega10():
    return render_template("ksiega10.html")

@app.route("/ksiega11")
def ksiega11():
    return render_template("ksiega11.html")

@app.route("/ksiega12")
def ksiega12():
    return render_template("ksiega12.html")
