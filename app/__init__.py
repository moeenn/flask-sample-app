from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

# TODO: read from env
app.secret_key="abc123123123"


@app.get("/")
def home_page():
    message = "Hello from home page"
    return render_template("home.html", message=message)


@app.get("/login")
def login_page():
    return render_template("login.html")


@app.post("/api/login")
def user_login():
    email = request.form.get("email")
    password = request.form.get("password")

    if email == "admin@site.com" and password == "123123123":
        flash("Login successful", "success")
        return redirect("/dashboard")

    flash("Invalid email or password", "error")
    return redirect("/login")


@app.get("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")
