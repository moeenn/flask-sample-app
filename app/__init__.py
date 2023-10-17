import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    make_response,
)
from turbo_flask import Turbo

app = Flask(__name__)
turbo = Turbo(app)

app.secret_key = os.environ.get("APP_SECRET")


@app.get("/")
def home_page():
    message = "Hello from home page "
    return render_template("home.html", message=message)


@app.get("/login")
def login_page():
    user_id = request.cookies.get("app_login")
    if user_id:
        flash("You are already logged in", "info")
        return redirect("/")

    return render_template("login.html")


@app.post("/api/login")
def user_login():
    email = request.form.get("email")
    password = request.form.get("password")

    if email == "admin@site.com" and password == "123123123":
        resp = make_response(redirect("/dashboard"))
        resp.set_cookie("app_login", "100")
        flash("Login successful", "success")
        return resp

    flash("Invalid email or password", "error")
    return redirect("/login")


@app.get("/logout")
def user_logout():
    user_id = request.cookies.get("app_login")
    if user_id:
        resp = make_response(redirect("/"))
        resp.delete_cookie("app_login")
        return resp

    return redirect("/")


@app.get("/dashboard")
def dashboard_page():
    user_id = request.cookies.get("app_login")
    if not user_id:
        flash("Please login to access this page", "error")
        return redirect("/login")

    return render_template("dashboard.html")
