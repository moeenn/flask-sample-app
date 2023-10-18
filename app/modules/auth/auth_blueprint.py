from flask import (
    Blueprint,
    request,
    flash,
    redirect,
    render_template,
    make_response,
    url_for,
)
from .auth_forms import LoginForm

auth_blueprint = Blueprint("auth", __name__, template_folder="templates")


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        if form.email.data == "admin@site.com" and form.password.data == "abc123123123":
            resp = make_response(redirect(url_for("dashboard.dashboard_page")))
            resp.set_cookie("app_login", "100")
            flash("Login successful", "success")
            return resp

    if request.method == "POST":
        flash("Invalid email / password", "error")
    return render_template("login.html", form=form)


@auth_blueprint.get("/logout")
def user_logout():
    user_id = request.cookies.get("app_login")
    if user_id:
        resp = make_response(redirect(url_for("public_pages.home_page")))
        resp.delete_cookie("app_login")
        return resp

    return redirect(url_for("public_pages.home_page"))
