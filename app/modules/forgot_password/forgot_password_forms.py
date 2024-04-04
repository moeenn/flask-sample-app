from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, validators


class ForgotPasswordForm(FlaskForm):
    email = EmailField("email", validators=[validators.DataRequired()])


class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        "password",
        validators=[
            validators.DataRequired(),
            validators.Length(min=8),
            validators.EqualTo("confirm_password", "Password fields must match"),
        ],
    )
    confirm_password = PasswordField(
        "confirm_password", validators=[validators.DataRequired()]
    )
