from flask import Blueprint, render_template

public_pages_blueprint = Blueprint("public_pages", __name__, template_folder="templates")


@public_pages_blueprint.get("/")
def home_page():
    message = "Hello from home page"
    return render_template("home.html", message=message)
