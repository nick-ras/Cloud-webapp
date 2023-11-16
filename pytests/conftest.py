import pytest, os, sys
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_dir)
from src import create_app
from src import db as _db
from sqlalchemy.orm import scoped_session

#make app object available to tests
@pytest.fixture(scope='session')
def app():
    """
    Returns session-wide Flask application.
    """
    return create_app("configs.TestingConfig")

#make db for session level
@pytest.fixture(scope='session')
def db(app, request):
    """
    Returns session-wide initialized database.
    """
    with app.app_context():
        _db.create_all()

    yield _db  # this is where the testing happens!

    # with app.app_context():
    #     _db.drop_all()

#make connection on function level
@pytest.fixture(scope='function')
def session(db, request):
    """
    Creates a new database session for a test.
    """
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = scoped_session(db.sessionmaker(**options))

    db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()

        