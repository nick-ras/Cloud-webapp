import threading
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

#creation of FLASK app
def create_app():
    app = Flask(__name__)
    app.secret_key = config("SECRET_KEY")
    app.config.from_object(config("APP_SETTINGS"))
    
        
    # Initialize plugins
    db.init_app(app)
    login_manager.login_view = "accounts.login" 
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    
    # #clean out booking table
    # from db_update import update_db
    # thread = threading.Thread(name='update_db', target=update_db.update_db_infinite)
    # thread.start()
    # print("Back in app.py after thread.start()")
    
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
