import getpass
import unittest

from flask.cli import FlaskGroup

from src.accounts.models import User
from src import app, db

cli = FlaskGroup(app)


@cli.command("test")
def test():
	print("Running tests...")
	app.config.from_object("config.TestingConfig")
	# Rest of your testing setup code
	tests = unittest.TestLoader().discover("tests")
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
			return 0
	else:
			return 1

  

# @cli.command("create_admin")
# def create_admin():
#     """Creates the admin user."""
#     email = input("Enter email address: ")
#     password = getpass.getpass("Enter password: ")
#     confirm_password = getpass.getpass("Enter password again: ")
#     if password != confirm_password:
#         print("Passwords don't match")
#         return 1
#     try:
#         user = User(email=email, password=password, is_admin=True)
#         db.session.add(user)
#         db.session.commit()
#         print(f"Admin with email {email} created successfully!")
#     except Exception:
#         print("Couldn't create admin user.")

if __name__ == "__main__":
    cli()