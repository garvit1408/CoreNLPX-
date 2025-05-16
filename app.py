from flask import Flask, render_template, request, redirect, url_for, flash
from db import DataBase
from textblob import TextBlob
import json
import spacy

nlp = spacy.load("en_core_web_sm")
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
# Name Entity Recognition


@app.route("/ner")
def ner():
    return render_template("ner.html")


def extract_entities(text):
    doc = nlp(text)
    return [{"entity": ent.text, "label": ent.label_} for ent in doc.ents]


@app.route("/perform_ner", methods=["POST"])
def perform_ner():
    text = request.form.get("text")
    entities = extract_entities(text)
    for i in range(len(entities)):
        print(entities[i]["entity"], entities[i]["label"])
    return render_template("ner.html", response=entities)


# ------------------------------------------------------------

# Sentiment Analysis


@app.route("/sentiment_analysis")
def sentiment_analysis():
    return render_template("sentiment_analysis.html")


def extract_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    sentiment = (
        "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    )

    return {
        "sentiment": sentiment,
        "polarity": round(polarity, 2),
        "subjectivity": round(subjectivity, 2),
    }


@app.route("/perform_sentiment_analysis", methods=["post"])
def perform_sentiment_analysis():
    text = request.form.get("text")
    response = extract_sentiment(text)
    print(response)
    return render_template("sentiment_analysis.html", response=response)


# ---------------------------------------------------------------------------

# abuse detection


@app.route("/abuse_detection")
def abuse_detection():
    return render_template("abuse_detection.html")


def extract_abuse_detection(text):
    abusive_keywords = {
        "idiot",
        "stupid",
        "dumb",
        "nonsense",
        "hate",
        "kill",
        "shit",
        "bastard",
        "asshole",
        "moron",
        "fool",
        "bloody",
        "bitch",
        "crap",
        "fuck",
        "retard",
        "suck",
        "damn",
    }
    found = [word for word in text.lower().split() if word in abusive_keywords]
    is_abusive = len(found) > 0

    return {"is_abusive": is_abusive, "bad_words": found}


@app.route("/perform_abuse_detection", methods=["post"])
def perform_abuse_detection():
    text = request.form.get("text")
    response = extract_abuse_detection(text)
    return render_template("abuse_detection.html", response=response)


app.run(debug=True)
