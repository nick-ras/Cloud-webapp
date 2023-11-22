import sys
import unittest
from flask.cli import FlaskGroup
from src import create_app

#this is where program are started by running python3 manage.py run or test
def create_app_with_config():
    # Check if the second argument in the command line is 'test'
    # if len(sys.argv) > 1 and sys.argv[1] == "test":
    #     config_name = "configs.TestingConfig"
    if len(sys.argv) > 1 and sys.argv[1] == "docker":
        config_name = "config.DockerConfig"
    else:
        config_name = "config.DevelopmentConfig"
    return create_app(config_name)

cli = FlaskGroup(create_app=create_app_with_config)

@cli.command()
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    cli()