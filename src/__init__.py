from decouple import config
from flask import Flask, render_template
from flask_login import LoginManager # Add this line
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from src.accounts.models import User
from decouple import config
from flask_bcrypt import Bcrypt
from src.extend import db, bcrypt, app


login_manager = LoginManager() # Add this line
login_manager.init_app(app) # Add this line

migrate = Migrate(app, db)

# Registering blueprints
from src.accounts.views import accounts_bp
from src.core.views import core_bp
app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)

login_manager.login_view = "accounts.login"
login_manager.login_message_category = "danger"

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


@app.errorhandler(401)
def unauthorized_page(error):
    return render_template("errors/401.html"), 401


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500