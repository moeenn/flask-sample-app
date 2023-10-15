from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    message = "Hello from home page"
    title = "Homepage"
    return render_template("home.html", title=title, message=message)
