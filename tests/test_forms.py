import unittest

from base_test import BaseTestCase

from src.accounts.forms import LoginForm, RegisterForm

from flask import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from wtforms import StringField, PasswordField, validators
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from src.accounts.models import User
from src import db

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
          
        

class TestRegisterForm(BaseTestCase):
    def test_validate_success_register_form(self):
        # Ensure correct data validates.
        form = RegisterForm(email="new@test.com", password="example", confirm="example")
        self.assertTrue(form.validate())

    def test_validate_invalid_password_format(self):
        # Ensure incorrect data does not validate.
        form = RegisterForm(email="new@test.com", password="ex", confirm="ex")
        self.assertFalse(form.validate())  # Password too short based on validator

    def test_validate_email_already_registered(self):
        # Setup
        user = User(email="ad@min.com", password="admin_user")
        db.session.add(user)
        db.session.commit()

        # Test
        form = RegisterForm(
            email="ad@min.com", password="admin_user", confirm="admin_user"
        )
        self.assertFalse(form.validate())  # Email already exists

if __name__ == "__main__":
    unittest.main()
