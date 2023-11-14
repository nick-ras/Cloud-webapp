import pytest, os, sys
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_dir)
from src import create_app
from src import db as _db

@pytest.fixture(scope='session')
def app():
    """
    Returns session-wide Flask application.
    """
    return create_app("configs.TestingConfig")

@pytest.fixture(scope='session')
def db(app, request):
    """
    Returns session-wide initialized database.
    """
    with app.app_context():
        _db.create_all()

    yield _db  # this is where the testing happens!

    _db.drop_all()

@pytest.fixture(scope='function')
def session(db, request):
    """
    Creates a new database session for a test.
    """
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()

        