import sys
import unittest
from flask.cli import FlaskGroup
from src import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)