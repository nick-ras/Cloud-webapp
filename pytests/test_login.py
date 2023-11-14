import pytest, os, sys
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_dir)
from flask_login import current_user, logout_user
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

def register_and_login(client, email, password, should_pass):
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
    if (should_pass==True):
      assert current_user.is_authenticated
      assert current_user.email == email
      assert b"You registered and are now logged in. Welcome!" in response.data
      return current_user
    else:
      assert current_user.is_anonymous




def test_register_and_login_success(client, session):
    # Register and log in a user using the helper function
    email = "test@example.com"
    password = "testpassword"
    user = register_and_login(client, email, password, should_pass=True)
    
    logout_user()
    email = "testexample.com"
    password = "testpassword"
    user = register_and_login(client, email, password, should_pass=False)

    
    #make for bad password also
    
    #most be done before adding boxes
    all_boxes = session.query(Boxes).all()
    assert len(all_boxes) == 30
    
    new_box = Boxes(size=1, location="Astroid City", in_use=False)
    insert_box(session, new_box)
    
    all_boxes = session.query(Boxes).all()
    assert len(all_boxes) == 31


