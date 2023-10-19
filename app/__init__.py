from flask import Flask
from .database.base import db
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from app.modules.user.user_model import User
from .errors import make_handler
from .config import Config
from .modules.public_pages.public_pages_blueprint import public_pages_blueprint
from .modules.user.user_blueprint import user_blueprint
from .modules.auth.auth_blueprint import auth_blueprint
from .modules.forgot_password.forgot_password_blueprint import (
    forgot_password_blueprint,
)
from .modules.dashboard.dashboard_blueprint import dashboard_blueprint


"""
instantiation of main application and crucial plugins
"""
app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)
db.init_app(app)
migrate = Migrate(app, db)


"""
login manager configuration
"""
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.user_loader(lambda user_id: User.query.get(int(user_id)))


"""
global error handlers 
"""
app.register_error_handler(401, make_handler(401, "Unauthorized"))
app.register_error_handler(404, make_handler(404, "Page not found"))
app.register_error_handler(500, make_handler(500, "Internal server error"))


"""
    register all blueprints (i.e. sub-routers) here
"""
app.register_blueprint(public_pages_blueprint)
app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(forgot_password_blueprint, url_prefix="/forgot-password")
app.register_blueprint(dashboard_blueprint, url_prefix="/dashboard")
