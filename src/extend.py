from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from decouple import config
from flask import Flask

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
bcrypt = Bcrypt()
db = SQLAlchemy(app)