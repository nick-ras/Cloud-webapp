import pytest, os, sys
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_dir)
from flask_login import current_user
import pytest
from flask import url_for
from src import create_app
from src.accounts.models import User, Boxes

def insert_box(session, box):
    try:
        session.add(box)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

def register_and_login(client, email, password):
    response = client.post(
        url_for("accounts.register"),
        data={
            "email": email,
            "password": password,
            "confirm": password,
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert current_user.is_authenticated
    assert b"You registered and are now logged in. Welcome!" in response.data

    return current_user

def test_register_and_login_success(client, session):
    # Register and log in a user using the helper function
    email = "test@example.com"
    password = "testpassword"
    user = register_and_login(client, email, password)
    assert user.email == email

    new_box = Boxes(size=1, location="Astroid City", in_use=False)
    insert_box(session, new_box)
    # You can perform additional tests on the user or other actions here
    # For example, you can check user attributes or make authenticated requests

