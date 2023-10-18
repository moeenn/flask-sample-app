from flask import Blueprint, render_template
from app.modules.user.user_model import User

public_pages_blueprint = Blueprint(
    "public_pages", __name__, template_folder="templates"
)


@public_pages_blueprint.get("/")
def home_page():
    message = "Hello from home page"
    users: list[User] = User.query.all()
    return render_template("home.html", message=message, users=users)
