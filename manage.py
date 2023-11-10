import sys
import unittest
from flask.cli import FlaskGroup
from src import create_app

def create_app_with_config():
    config_name = "config.DevelopmentConfig"
    # Check if the second argument in the command line is 'test'
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        config_name = "config.TestingConfig"
    return create_app(config_name)

cli = FlaskGroup(create_app=create_app_with_config)

if __name__ == "__main__":
    cli()