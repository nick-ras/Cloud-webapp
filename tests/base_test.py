import os

from flask_testing import TestCase

from src import app, db
from src.accounts.models import User
from flask import FlaskForm, DataRequired, Email, EqualTo, PasswordField, StringField, validators, ValidationError


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object("config.TestingConfig")
        return app

    def setUp(self):
        db.create_all()
        user = User(email="ad@min.com", password="admin_user")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        testdb_path = os.path.join("src", "testdb.sqlite")
        os.remove(testdb_path)

class RegisterForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[
			DataRequired(),
			validators.Length(min=6, max=100)  # Adjust min and max as per your model requirements
	])
	confirm = PasswordField('Confirm Password', validators=[
			DataRequired(),
			EqualTo('password', message='Passwords must match.')
	])

	def validate_email(self, email):
			user = User.query.filter_by(email=email.data).first()
			if user:
					raise ValidationError('Email already registered. Please use a different one.')