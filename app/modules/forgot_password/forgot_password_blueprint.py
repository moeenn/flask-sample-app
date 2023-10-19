from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forgot_password_forms import ForgotPasswordForm, ResetPasswordForm
from flask_login import current_user


forgot_password_blueprint = Blueprint("forgot_password", __name__, template_folder="templates")


@forgot_password_blueprint.route("/", methods=["GET", "POST"])
def forgot_password():
    if current_user.is_authenticated:
        flash("You are already logged-in. If you need to update your account password please go to your account settings.", "info")
        return redirect(url_for("public_pages.home_page"))

    form = ForgotPasswordForm(request.form)
    if request.method == "POST":
        flash("You request will be processed", "info")
    return render_template("forgot_password.html", form=form)


@forgot_password_blueprint.route("/reset", methods=["GET", "POST"])
def reset_password():
    token: str | None = request.args.get("token")
    if not token:
        flash("Invalid or expired link", "error")

    form = ResetPasswordForm(request.form)
    if form.validate_on_submit():
        flash("Account password updated successfully", "success")

    return render_template("reset_password.html", form=form)
