# conftest.py
import config, pytest, sys
from src import create_app, db


#The setup method creates all your tables; authors and articles tables. It then defines the session, which is the Session object in SQLAlchemy in which the conversation with the database occurs


def setup_func():#
    app = create_app(config.TestingConfig)
    with app.app_context():
        db.create_all()
        session = db.session
        yield session
        db.session.remove()
        db.drop_all()
    session = app.test_client()
    app.testing = True
    yield app

@pytest.fixture(autouse=True)
def before_and_after():
    # Before each test
    print("Before each test")
    setup_func()
    yield
    # After each test
    print("After each test")    