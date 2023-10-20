from decouple import config
from decouple import config
from flask import Flask
from flask_login import LoginManager # Add this line
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

login_manager = LoginManager() # Add this line
login_manager.init_app(app) # Add this line
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#EXTRA dont knowwhere to put
login_manager.login_view = "accounts.login"
login_manager.login_message_category = "danger"

# Registering blueprints
from src.accounts.views import accounts_bp
# from src.core.views import core_bp

app.register_blueprint(accounts_bp)
# app.register_blueprint(core_bp)

from decouple import config
from flask import Flask
from flask_login import LoginManager # Add this line
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

login_manager = LoginManager() # Add this line
login_manager.init_app(app) # Add this line
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Registering blueprints
from src.accounts.views import accounts_bp
from src.core.views import core_bp

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)