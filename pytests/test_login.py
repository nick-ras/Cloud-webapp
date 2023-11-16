import pytest, os, sys
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_dir)

from flask_login import current_user, login_required, logout_user
import pytest
from flask import jsonify, url_for
from src import create_app
from src.accounts.models import User, Boxes

#inserts a box into the boxes table
@login_required
def insert_box(session, box):
    if not current_user.is_admin:
        print("Unauthorized access")
        return jsonify({"error": "Unauthorized access"}), 403
    try:
        session.add(box)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

#inserts a user into the users table
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

#makes different login credentials and tests them with register_and_login function that has asserts
# Also inserts boxes and checks length (normal users are not suppose to do this though)
def test_register_and_login_success(client, session):
    #checking if user can register and login
    email = "test@example.com"
    password = "testpassword"
    user = register_and_login(client, email, password, should_pass=True)
    
    #shuold fail since incorrect email format
    logout_user()
    email = "testexample.com"
    password = "testpassword"
    user = register_and_login(client, email, password, should_pass=False)

    #checks if non-admin can insert box
    all_boxes = session.query(Boxes).all()
    assert len(all_boxes) == 30
    
    new_box = Boxes(size=1, location="Astroid City", in_use=False)
    insert_box(session, new_box)
    
    all_boxes = session.query(Boxes).all()
    assert len(all_boxes) == 30
    
    
    # #todo when i can figure out how to make admin user
    # logout_user()
    # email = "@example.com"
    # password = "testpassword"
    # user = register_and_login(client, email, password, should_pass=False)
    
    
