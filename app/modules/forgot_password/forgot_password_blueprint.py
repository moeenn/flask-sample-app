from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forgot_password_forms import ForgotPasswordForm, ResetPasswordForm
from flask_login import current_user
from .forgot_password_service import (
    process_forgot_password,
    reset_user_password,
)
from app.utilities.jwt import validate_password_reset_token


forgot_password_blueprint = Blueprint(
    "forgot_password", __name__, template_folder="templates"
)


@forgot_password_blueprint.route("/", methods=["GET", "POST"])
def forgot_password():
    if current_user.is_authenticated:
        flash(
            "You are already logged-in. If you need to update your account password please go to your account settings.",
            "info",
        )
        return redirect(url_for("public_pages.home_page"))

    form = ForgotPasswordForm(request.form)
    if form.validate_on_submit():
        token = process_forgot_password(form.email.data)
        if token:
            flash("You request will be processed: " + token, "info")

    return render_template("forgot_password.html", form=form)


@forgot_password_blueprint.route("/reset/<token>", methods=["GET", "POST"])
def reset_password(token: str):
    user_id = validate_password_reset_token(token)
    if not user_id:
        if request.method == "GET":
            return render_template(
                "errors/error.html",
                status=400,
                message="Invalid or expired link",
            )

    form = ResetPasswordForm(request.form)
    if form.validate_on_submit():
        reset_user_password(user_id, form.password.data)
        flash("Account password updated successfully", "success")
        return redirect(url_for("public_pages.home_page"))

    return render_template("reset_password.html", form=form, token=token)
