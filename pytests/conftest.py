from distutils import config
import pytest, os, sys
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_dir)
from src import create_app
from src import db as _db
from sqlalchemy.orm import scoped_session

#make app object available to tests
@pytest.fixture()
def test_client():
    """
    Returns session-wide Flask application.
    """
    os.environ['APP_SETTINGS'] = 'config.TestingConfig'
    app = create_app()

    # Create a test client
    with app.test_client() as test_client_obj:
            yield test_client_obj

# #make connection
# @pytest.fixture()
# def session(db, request):
#     """
#     Creates a new database session for a test.
#     """
#     connection = db.engine.connect()
#     transaction = connection.begin()

#     options = dict(bind=connection, binds={})
#     session = scoped_session(db.sessionmaker(**options))

#     db.session = session

#     yield session

#     transaction.rollback()
#     connection.close()
#     session.remove()

#make db for session level
@pytest.fixture()
def db(test_client):
    
    #creates db tables from models
    with test_client.app_context():
        #create tables
        db.create_all()
        #making db object available to tests
    yield db

    # Optionally, you can drop the testing database tables after the test session:
    with create_app().app_context():
        db.drop_all()




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