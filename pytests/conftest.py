from distutils import config
import pytest, os, sys
from src import create_app, db
from sqlalchemy.orm import scoped_session
from flask import current_app

@pytest.fixture(scope='module')
def test_client():
    os.environ['APP_SETTINGS'] = 'config.TestingConfig'
    app = create_app()
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client

@pytest.fixture()       
def logged_in_client(test_client):
    username = "testuser"
    password = "password"

    # Perform a POST request to your login endpoint with credentials
    response = test_client.post(
        '/login',  # Replace with the actual URL of your login endpoint
        data={'username': username, 'password': password},
        follow_redirects=True
    )

    # Check if the login was successful (you might need to customize this)
    assert response.status_code == 200

    return response
        
# #make app object available to tests
# @pytest.fixture()
# def db_conn(test_client, logged_in_client):
#     os.environ['APP_SETTINGS'] = 'config.TestingConfig'
#     # Create a test client
#     with test_client.application.app_context() as context:
#         db.create_all()
#         yield context
#         db.session.remove()
#         db.drop_all()




# from flask import g

# def get_db():
#     if 'db' not in g:
#         g.db = connect_to_database()

#     return g.db

# @app.teardown_appcontext
# def teardown_db(exception):
#     db = g.pop('db', None)

#     if db is not None:
#         db.close()