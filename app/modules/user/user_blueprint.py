from flask import Blueprint, render_template, flash, redirect, url_for, request
from .user_service import register_user
from .user_forms import UserRegisterForm
from flask_login import current_user

user_blueprint = Blueprint("user", __name__, template_folder="templates")


@user_blueprint.route("/register", methods=["GET", "POST"])
def user_register():
    if current_user.is_authenticated:
        flash("You are already logged-in", "info")
        return redirect(url_for("public_pages.home_page"))

    form = UserRegisterForm(request.form)
    if form.validate_on_submit():
        new_user = register_user(form.email.data, form.password.data)
        if not new_user:
            return render_template("auth.login")

        flash("Account created successfully", "success")
        return redirect(url_for("auth.login"))

    return render_template("user_register.html", form=form)
