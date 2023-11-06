from decouple import config
from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv() 
#overwrites the config.py file with the .env file
# app.config.from_object(os.getenv("APP_SETTINGS"))


login_manager = LoginManager()
login_manager.init_app(app)

#making instances of the extensions to be used in other files

if os.getenv("FLASK_ENV") == "production":
		app.config.from_object("config.ProductionConfig")
elif os.getenv("FLASK_ENV") == "test":
		app.config.from_object("config.TestingConfig")

elif os.getenv("FLASK_ENV") == "development":
		app.config.from_object("config.DevelopmentConfig")
		# Run the update db logic in seperate thread
else:
	exit("FLASK_ENV not set")
 
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import db_update
from threading import Thread
if os.getenv("FLASK_ENV") == "development":
	db_update_instance = db_update.update_db()
	update_thread = Thread(target=db_update_instance.update_db_infinite)
	update_thread.start()

# Registering blueprints
from src.accounts.views import accounts_bp
from src.core.views import core_bp

app.register_blueprint(core_bp) #uden prefix er det bare http://127.0.0.1:5000/locations. Ellers url_prefix='/core'
app.register_blueprint(accounts_bp)

from src.accounts.models import User

login_manager.login_view = "accounts.login"
login_manager.login_message_category = "danger"

@login_manager.user_loader
def load_user(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        return None  # return None if user_id is not an integer
    return User.query.filter(User.id == user_id).first()


########################
#### error handlers ####
########################


@app.errorhandler(401)
def unauthorized_page(error):
    return render_template("errors/401.html"), 401


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500