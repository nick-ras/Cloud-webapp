from datetime import datetime
from flask_login import UserMixin
from src import bcrypt, db
from sqlalchemy import CheckConstraint, ForeignKey, func
from sqlalchemy.orm import relationship

#user table schema from azure db, and encrypts password including salts. SQLAlchemy ORM used
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    boxes = relationship('Boxes', back_populates='user')  # Establishing relationship with Box model

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password, 12)
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return f"<email {self.email}>"

#box table schema from azure db, and some methods to get available sizes and locations. SQLAlchemy ORM used
class Boxes(db.Model):
		__tablename__ = "boxes"
		id = db.Column(db.Integer, primary_key=True)
		size = db.Column(db.Integer, nullable=False)
		location = db.Column(db.String(100), nullable=False)
		in_use = db.Column(db.Boolean, nullable=False, default=False)
		booked_until_interval15 = db.Column(db.DateTime, nullable=True)
		user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=True)  # Foreign key to the users table            
		user = relationship('User', back_populates='boxes')  # Establishing relationship with User model
				
		__table_args__ = (
				CheckConstraint('size IN (1, 2, 3)'), 
		)
                
		def __repr__(self):
				user_info = f"User ID {self.user_id} - User Email {self.user.email}" if self.user else "No user assigned"
				return f"<Boxes {self.id} - Size {self.size} - Location {self.location} - {user_info}>"
		
                
      
