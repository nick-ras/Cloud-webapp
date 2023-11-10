# conftest.py
import config, os, pytest, sys
sys.path.append('/home/VMNick1/webapp2/src')
from src import create_app, db, bcrypt, login_manager, migrate
from flask import url_for

@pytest.fixture
def start():
    app = create_app(configs=config.TestingConfig)
    app.testing = True
    return app

@pytest.fixture
def test_register(client):
    # Create test data for the form
    test_data = {
                    "email": os.getenv("TEST_EMAIL"),
                    "password": os.getenv("TEST_PASSWORD"),
                    "confirm_password": os.getenv("TEST_PASSWORD")
    }

    # Make a POST request to the register endpoint
    response = client.post(url_for('auth.register'), data=test_data)

    # Assertions to check if the register was successful
    assert response.status_code == 200
    # Additional assertions based on the behavior of your register function
