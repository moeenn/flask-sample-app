from flask import (
    Blueprint,
    request,
    flash,
    redirect,
    render_template,
    make_response,
)

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.get("/login")
def login_page():
    user_id = request.cookies.get("app_login")
    if user_id:
        flash("You are already logged in", "info")
        return redirect("/")

    return render_template("login.html")


@auth_blueprint.post("/login")
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


@auth_blueprint.get("/logout")
def user_logout():
    user_id = request.cookies.get("app_login")
    if user_id:
        resp = make_response(redirect("/"))
        resp.delete_cookie("app_login")
        return resp

    return redirect("/")
