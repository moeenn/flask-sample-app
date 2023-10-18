from flask import (
    Blueprint,
    request,
    flash,
    redirect,
    render_template,
    url_for,
)
from .auth_forms import LoginForm
from app.utilities.password_hasher import password_hasher
from app.modules.user.user_model import User
from flask_login import login_user, logout_user


auth_blueprint = Blueprint("auth", __name__, template_folder="templates")


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash("Invalid email / password", "error")
            return render_template("login.html", form=form)

        try:
            password_hasher.verify(user.password, form.password.data)
        except Exception:
            flash("Invalid email / password", "error")
            return render_template("login.html", form=form)

        # login is valid
        login_user(user)
        flash("Login successful", "success")
        return redirect(url_for("dashboard.dashboard_page"))

    if request.method == "POST":
        flash("Invalid email / password", "error")
    return render_template("login.html", form=form)


@auth_blueprint.get("/logout")
def user_logout():
    logout_user()
    return redirect(url_for("public_pages.home_page"))
