from flask import Blueprint, request, flash, redirect, render_template, url_for

dashboard_blueprint = Blueprint(
    "dashboard", __name__, template_folder="templates"
)


@dashboard_blueprint.get("/")
def dashboard_page():
    user_id = request.cookies.get("app_login")
    if not user_id:
        flash("Please login to access this page", "error")
        return redirect(url_for("auth.login"))

    return render_template("dashboard.html")
