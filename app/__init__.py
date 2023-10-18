from flask import Flask
from .database.base import db
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from .errors import make_handler
from .config import Config
from .modules.public_pages.public_pages_blueprint import public_pages_blueprint
from .modules.user.user_blueprint import user_blueprint
from .modules.auth.auth_blueprint import auth_blueprint
from .modules.dashboard.dashboard_blueprint import dashboard_blueprint


app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)
db.init_app(app)
migrate = Migrate(app, db)
app.register_error_handler(404, make_handler(404, "Page not found"))
app.register_error_handler(500, make_handler(500, "Internal server error"))

"""
    register all blueprints (i.e. sub-routers) here
"""
app.register_blueprint(public_pages_blueprint)
app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(dashboard_blueprint, url_prefix="/dashboard")
