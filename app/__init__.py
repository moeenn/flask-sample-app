from flask import Flask, render_template
from .database.base import db
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from .config import Config
from .modules.public_pages.public_pages_blueprint import public_pages_blueprint
from .modules.user.user_blueprint import user_blueprint
from .modules.auth.auth_blueprint import auth_blueprint
from .modules.dashboard.dashboard_blueprint import dashboard_blueprint


app = Flask(__name__)
app.config["SECRET_KEY"] = Config.app_secret
app.config["SQLALCHEMY_DATABASE_URI"] = Config.database_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
csrf = CSRFProtect(app)
db.init_app(app)
migrate = Migrate(app, db)


@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        "errors/error.html", status=404, message="Page Not Found"
    )


@app.errorhandler(500)
def internal_server_error(error):
    return render_template(
        "errors/error.html", status=500, message="Internal Server Error"
    )


"""
    register all blueprints (i.e. sub-routers) here
"""
app.register_blueprint(public_pages_blueprint)
app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(dashboard_blueprint, url_prefix="/dashboard")
