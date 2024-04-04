from flask import Blueprint, render_template
from flask_login import login_required

dashboard_blueprint = Blueprint("dashboard", __name__, template_folder="templates")


@dashboard_blueprint.get("/")
@login_required
def dashboard_page():
    return render_template("dashboard.html")
