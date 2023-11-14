import pytest, os, sys
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_dir)
from flask_login import current_user
import pytest
from flask import url_for
from src import create_app

def test_login(session, test_user):
    # Make a POST request to the login route with valid credentials
		response = session.post(
        url_for("accounts.login"),
        data={"email": f"{session.email}", "password": "testpassword"},
        follow_redirects=True,
    )

    # Check if the response status code is 200 (OK)
		assert response.status_code == 200

    # # Check if the expected success message is present in the response content
    # assert b"You are already logged in." in response.data

    # # Check if the user is authenticated
    # assert current_user.is_authenticated
