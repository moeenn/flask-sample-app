from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    message = "Hello from home page"
    return render_template("home.html", message=message)
