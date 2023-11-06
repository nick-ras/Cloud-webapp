import os
from src import bcrypt

from flask_testing import TestCase
from src import app, db
from src.accounts.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

class BaseTestCase(TestCase):
		def create_app(self):
				app.config.from_object("config.TestingConfig")
				return app

		def setUp(self):
				db.create_all()
				hashed_password = bcrypt.generate_password_hash("testuser")
				user = User(email="test@test.com", password=hashed_password, is_admin=True)
				db.session.add(user)
				db.session.commit()

		def tearDown(self):
			db.session.remove()
			db.drop_all()
			testdb_path = os.path.join("src", "testdb.sqlite")
			# Only remove the test database file if it exists to avoid file not found error.
			if os.path.exists(testdb_path):
					os.remove(testdb_path)
