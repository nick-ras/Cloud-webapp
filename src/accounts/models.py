from datetime import datetime

from flask_login import UserMixin

from src import bcrypt, db

from sqlalchemy import CheckConstraint



class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return f"<email {self.email}>"
    
class Box(db.Model):

		__tablename__ = "boxes"

		id = db.Column(db.Integer, primary_key=True)
		size = db.Column(db.Integer, nullable=False, check=(db.Column('size', db.Integer, CheckConstraint('size IN (1, 2, 3)'))))
		location = db.Column(db.String(100), nullable=False)
		in_use = db.Column(db.Boolean, nullable=False, default=False)
		booked_on = db.Column(db.DateTime, nullable=True)  # assuming you may want to track when the box was booked

		def __init__(self, size, location):
				self.size = size
				self.location = location

		def __repr__(self):
				return f"<Box {self.id} - Size {self.size} - Location {self.location}>"
