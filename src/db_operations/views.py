from flask_login import login_user
from ..accounts.models import User, Boxes
from src import db
from datetime import datetime, timedelta


def register_user(email, password):
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    login_user(user)

def db_rollback():
		db.session.rollback()
  
def login_a_user(user):
		login_user(user)
    
def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user_boxes(user_id):
    return Boxes.query.filter(Boxes.user_id == user_id).all()

def find_available_box(location, size):
    return Boxes.query.filter_by(location=location, size=size, in_use=False).with_for_update().first()

def update_box_usage(box, duration, user_id):
    box.in_use = True
    box.booked_on = datetime.utcnow()
    box.user_id = user_id
    box.booked_until_interval15 = datetime.utcnow() + timedelta(hours=duration)
    db.session.commit()

def get_available_sizes():
		# This query will return all unique sizes from the Boxes table where boxes are not currently in use
		result = (
						db.session.query(Boxes.size)
						.filter(Boxes.in_use == False)
						.group_by(Boxes.size)
						.all()
    )
		return result

def get_locations_by_size(size):
			# This query will return all unique locations from the Boxes table having boxes of certain size not currently in use
			result = db.session.query(Boxes.location).filter(Boxes.in_use == False, Boxes.size == size).group_by(Boxes.location).all()
			return result
