from flask import Blueprint, render_template, flash, redirect, url_for, request
from .user_repo import create_user
from .user_forms import UserRegisterForm

user_blueprint = Blueprint("user", __name__, template_folder="templates")


@user_blueprint.route("/register", methods=["GET", "POST"])
def user_register():
    form = UserRegisterForm(request.form)
    if form.validate_on_submit():
        create_user(email=form.email.data, password=form.password.data)
        flash("Account created successfully", "success")
        return redirect(url_for("auth.login"))

    return render_template("user_register.html", form=form)
