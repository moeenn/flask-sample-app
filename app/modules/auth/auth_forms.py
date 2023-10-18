from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, validators


class LoginForm(FlaskForm):
    email = EmailField("email", validators=[validators.DataRequired()])
    password = PasswordField(
        "password",
        validators=[validators.DataRequired(), validators.Length(min=8)],
    )
