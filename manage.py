import unittest

from flask.cli import FlaskGroup

from src import create_app

cli = FlaskGroup(create_app())

@cli.command("test")
def test():
	print("Running tests from manage.py cli command test")
	# Rest of your testing setup code
	tests = unittest.TestLoader().discover("tests")
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
			return 0
	else:
			return 1

if __name__ == "__main__":
    cli()