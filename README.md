# 🧠 NLP Web Application

An interactive web app built with **Flask**, offering four core Natural Language Processing (NLP) tools:
- 🔍 Named Entity Recognition (NER)
- 😊 Sentiment Analysis
- 🚫 Abuse Detection
- 🔐 User Authentication (Login/Register/Profile)

Designed with a **modern dark UI** using **Tailwind CSS** and enhanced with **particles.js** for a dynamic background on every page.

---

## 🌟 Features

| Feature               | Description                                              |
|-----------------------|----------------------------------------------------------|
| 👤 Login / Register    | User authentication system with secure form submission  |
| 🧭 Profile Dashboard   | Centralized access to all NLP tools                      |
| 📍 NER Tool            | Extracts named entities from input text                 |
| 😊 Sentiment Tool      | Analyzes polarity & subjectivity of text                |
| 🚫 Abuse Detection     | Detects offensive or abusive words                      |

---

## 🛠 Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML, Tailwind CSS
- **Templates:** Jinja2
- **Effects:** [particles.js](https://vincentgarreau.com/particles.js/)
- **Deployment-ready:** Easily hosted on platforms like Render, Heroku, or local Flask server

---

## 📁 Folder Structure
nlp-web-app/
│
├── static/
│   └── particles.json              # Background animation configuration
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   ├── ner.html
│   ├── sentiment_analysis.html
│   └── abuse_detection.html
│
├── app.py                          # Flask application backend
├── requirements.txt                # List of Python dependencies
└── README.md                       # Project documentation

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/garvit1408/coreNLPX-.git
cd coreNLPX-
pip install -r requirements.txt
python app.py
```
