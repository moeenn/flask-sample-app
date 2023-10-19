from flask import Blueprint, render_template, request, flash
from .forgot_password_forms import ForgotPasswordForm, ResetPasswordForm


forgot_password_blueprint = Blueprint("forgot_password", __name__, template_folder="templates")


@forgot_password_blueprint.route("/", methods=["GET", "POST"])
def forgot_password():
    form = ForgotPasswordForm(request.form)
    if request.method == "POST":
        flash("You request will be processed", "info")
    return render_template("forgot_password.html", form=form)


@forgot_password_blueprint.route("/reset", methods=["GET", "POST"])
def reset_password():
    form = ResetPasswordForm(request.form)
    if form.validate_on_submit():
        flash("Account password updated successfully", "success")

    return render_template("reset_password.html", form=form)
