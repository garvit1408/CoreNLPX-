from flask import Flask, render_template, request, redirect, url_for, flash
from db import DataBase
import json

app = Flask(__name__)

obj = DataBase()


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/perform_registeration", methods=["post"])
def perform_registeration():
    name = request.form.get("user_name")
    email = request.form.get("user_email")
    password = request.form.get("user_password")

    response = obj.insert(name, email, password)

    if response:
        return render_template(
            "login.html", message="Registration successful.Kindly login"
        )
    else:
        return render_template("register.html", message="Email already exists")


@app.route("/perform_login", methods=["post"])
def perform_login():
    email = request.form.get("user_email")
    password = request.form.get("user_password")

    response = obj.search(email, password)
    if response:
        return redirect("/profile")
    else:
        return render_template("login.html", message="Invalid credentials")


@app.route("/profile")
def welcome():
    return render_template("profile.html")


# -------------------------------------------------------------


@app.route("/ner")
def ner():
    return render_template("ner.html")


@app.route("/perform_ner", methods=["post"])
def perform_ner():
    text = request.form.get("text")
    response = obj.ner(text)
    return render_template("ner.html", response=response)


# ------------------------------------------------------------


@app.route("/sentiment_analysis")
def sentiment_analysis():
    return render_template("sentiment_analysis.html")


@app.route("/perform_sentiment_analysis", methods=["post"])
def perform_sentiment_analysis():
    text = request.form.get("text")
    response = obj.sentiment_analysis(text)
    return render_template("sentiment_analysis.html", response=response)


# ---------------------------------------------------------------------------


@app.route("/abuse_detection")
def abuse_detection():
    return render_template("abuse_detection.html")


@app.route("/perform_abuse_detection", methods=["post"])
def perform_abuse_detection():
    text = request.form.get("text")
    response = obj.abuse_detection(text)
    return render_template("abuse_detection.html", response=response)


app.run(debug=True)
