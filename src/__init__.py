from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from decouple import config

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
migrate = Migrate()

def create_app(configarg):
    app = Flask(__name__)
    app.secret_key = config("SECRET_KEY")
    
    if configarg == "configs.TestingConfig":
        print ("TestingConfig from create_app")
        app.config.from_object(configarg)
    else:
        print ("DevelopmentConfig from create_app")
        app.config.from_object("configs.DevelopmentConfig")
        
    # Initialize plugins
    db.init_app(app)
    login_manager.login_view = "accounts.login" 
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from src.accounts.views import accounts_bp
    from src.core.views import core_bp
    app.register_blueprint(core_bp)
    app.register_blueprint(accounts_bp)

    # Error handlers
    @app.errorhandler(401)
    def unauthorized_page(error):
        return render_template("errors/401.html"), 401

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/500.html"), 500

    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        try:
            user_id = int(user_id)
        except ValueError:
            return None
        from src.accounts.models import User
        return User.query.get(user_id)

    return app




# from decouple import config
# from flask import Flask, render_template
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# from dotenv import load_dotenv
# import os


# app = Flask(__name__)
# # sets testing or dev og prod environment from config.py, which is set in the .env file
# app.config.from_object(config('APP_SETTINGS'))
# load_dotenv() 
# #overwrites the config.py file with the .env file
# # app.config.from_object(os.getenv("APP_SETTINGS"))


# login_manager = LoginManager()
# login_manager.init_app(app)
 
# bcrypt = Bcrypt(app)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# ## cleaning up in the database for expired bookings
# import db_update
# from threading import Thread
# if config("APP_SETTINGS") == "config.DevelopmentConfig":
# 	db_update_instance = db_update.update_db()
# 	update_thread = Thread(target=db_update_instance.update_db_infinite)
# 	update_thread.start()

# # Registering blueprints
# from src.accounts.views import accounts_bp
# from src.core.views import core_bp

# app.register_blueprint(core_bp) #uden prefix er det bare http://127.0.0.1:5000/locations. Ellers url_prefix='/core'
# app.register_blueprint(accounts_bp)

# from src.accounts.models import User

# login_manager.login_view = "accounts.login"
# login_manager.login_message_category = "danger"

# @login_manager.user_loader
# def load_user(user_id):
#     try:
#         user_id = int(user_id)
#     except ValueError:
#         return None  # return None if user_id is not an integer
#     return User.query.filter(User.id == user_id).first()


# ########################
# #### error handlers ####
# ########################


# @app.errorhandler(401)
# def unauthorized_page(error):
#     return render_template("errors/401.html"), 401


# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template("errors/404.html"), 404


# @app.errorhandler(500)
# def server_error_page(error):
#     return render_template("errors/500.html"), 500