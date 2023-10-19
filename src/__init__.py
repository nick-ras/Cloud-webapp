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
from src.core.views import core_bp

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)

from src.accounts.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()



from flask_login import UserMixin # Add this line

from src import bcrypt, db


class User(UserMixin, db.Model): # Change this line

    __tablename__ = "users"
    

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return f"<email {self.email}>"
    
		