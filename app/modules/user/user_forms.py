from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, validators


class UserRegisterForm(FlaskForm):
    email = EmailField("email", validators=[validators.DataRequired()])
    password = PasswordField(
        "password",
        validators=[
            validators.DataRequired(),
            validators.Length(min=8),
            validators.EqualTo(
                "confirm_password", message="Passwords must match"
            ),
        ],
    )
    confirm_password = PasswordField("confirm_password")
