from flask import Blueprint, render_template, flash, redirect, url_for, request

user_blueprint = Blueprint("user", __name__, template_folder="templates")


@user_blueprint.get("/register")
def user_register_page():
    user_id = request.cookies.get("app_login")
    if user_id:
        flash("You are already logged in", "info")
        return redirect(url_for("public_pages.home_page"))

    return render_template("user_register.html")


@user_blueprint.post("/register")
def user_register():
    flash("Account created successfully", "success")
    return redirect(url_for("auth.login_page"))

